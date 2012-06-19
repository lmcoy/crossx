package hep

import (
	"fmt"
	"math"
	"physics/hep/lhe"
	"physics/hep/pdf"
	"physics/hep/pdg"
	"physics/math/linalg"
	"physics/math/mcintegrator"
)

type SUSY struct {
	Mu      float64
	TanBeta float64
	// squarks masses
	M_su float64
	M_sd float64
	M_ss float64
	M_sc float64
	// bino & wino masses
	M_bino float64
	M_wino float64
}

const (
	// All values are given in GeV
	GeV = 1.0
	MeV = 1.0e-3
	KeV = 1.0e-6
	TeV = 1.0e+3
	// Converts a cross section in 1/GeV² to pb
	// Usage: s[pb] = s[1/GeV²]*CrossSectionToPb
	CrossSectionToPb = 3.8937944929e8
)

const (
	// sin(𝜃w)²
	Sw2   = 0.2312
	Alpha = 1.0 / 127.934
	//Alpha = 1.0 / 137.0
	// Z boson mass
	Mz = 91.1876 * GeV
	// W boson mass
	Mw = 80.385 * GeV
	// electron mass
	Me = 0.510998928 * MeV
	// proton mass
	Mp = 0.93827204 * GeV
	// neutron mass
	Mn = 939.565378 * MeV
	// charged pion mass
	Mpi = 139.57018 * MeV
	// pion mass
	Mpi0 = 134.9766 * MeV
)

var sw = math.Sqrt(Sw2)
var cw = math.Cos(math.Asin(sw))

// NeutralinoMassMatrix returns the mass matrix for neutralinos with the SUSY parameters in susy.
//
// 	mass matrix (symmetric):
// 		( M_bino,     0,      -cos(𝛽)*sw*Mz,   sin(𝛽)*sw*Mz ) 
// 		(    0,    M_wino,     cos(𝛽)*cw*Mz,  -sin(𝛽)*cw*Mz )
// 		(    *,       *,             0,             -µ      )
// 		(    *,       *,            -µ,              0      )
func NeutralinoMassMatrix(susy *SUSY) (m *linalg.Matrix4) {
	m = linalg.NewMatrix4()
	sb := math.Sin(math.Atan(susy.TanBeta))
	cb := math.Cos(math.Atan(susy.TanBeta))

	// precalculate values
	A := -cb * sw * Mz
	B := sb * sw * Mz
	C := cb * cw * Mz
	D := -sb * cw * Mz
	m.Set(0, 0, susy.M_bino)
	m.Set(0, 1, 0.0)
	m.Set(0, 2, A)
	m.Set(0, 3, B)
	m.Set(1, 0, 0.0)
	m.Set(1, 1, susy.M_wino)
	m.Set(1, 2, C)
	m.Set(1, 3, D)
	m.Set(2, 0, A)
	m.Set(2, 1, C)
	m.Set(2, 2, 0.0)
	m.Set(2, 3, -susy.Mu)
	m.Set(3, 0, B)
	m.Set(3, 1, D)
	m.Set(3, 2, -susy.Mu)
	m.Set(3, 3, 0.0)
	return
}

// CharginoMassMatrix returns the 2x2 chargino mass matrix.
//
//	M =
// 		( M_wino,        √2*Mw*cos(𝛽) )
// 		( √2*Mw*sin(𝛽),       µ       )
func CharginoMassMatrix(susy *SUSY) (m *linalg.Matrix2) {
	m = linalg.NewMatrix2()
	sb := math.Sin(math.Atan(susy.TanBeta))
	cb := math.Cos(math.Atan(susy.TanBeta))

	m.Set(0, 0, susy.M_wino)
	m.Set(0, 1, math.Sqrt2*Mw*cb)
	m.Set(1, 0, math.Sqrt2*Mw*sb)
	m.Set(1, 1, susy.Mu)
	return
}

func A_L_Chargino(j int, U *linalg.Matrix2) float64 {
	return 1.0 / math.Sqrt2 * U.At(j, 0) / sw
}

func A_L_c_Chargino(j int, V *linalg.Matrix2) float64 {
	return 1.0 / math.Sqrt2 * V.At(j, 0) / sw
}

func A_L(i int, q, T3 float64, N *linalg.Matrix4) float64 {
	// convert N from bino-wino to photino-zino basis
	Ni1 := N.At(i, 0)*cw + N.At(i, 1)*sw
	Ni2 := -N.At(i, 0)*sw + N.At(i, 1)*cw

	return (sw*q*Ni1 + 1.0/cw*Ni2*(T3-q*Sw2)) / sw
}

func L(i, j int, N *linalg.Matrix4, V *linalg.Matrix2) float64 {
	// convert N from bino-wino to photino-zino basis
	Ni4 := N.At(i, 3)
	Ni1 := N.At(i, 0)*cw + N.At(i, 1)*sw
	Ni2 := -N.At(i, 0)*sw + N.At(i, 1)*cw

	return 1.0 / math.Sqrt2 / sw * (Ni4*V.At(j, 1) - math.Sqrt2*(sw*Ni1+cw*Ni2)*V.At(j, 0))
}

func R(i, j int, N *linalg.Matrix4, U *linalg.Matrix2) float64 {
	// convert N from bino-wino to photino-zino basis
	Ni3 := N.At(i, 2)
	Ni1 := N.At(i, 0)*cw + N.At(i, 1)*sw
	Ni2 := -N.At(i, 0)*sw + N.At(i, 1)*cw

	return 1.0 / (math.Sqrt2 * sw) * (-Ni3*U.At(j, 1) - math.Sqrt2*(sw*Ni1+cw*Ni2)*U.At(j, 0))
}

// Mandelstam_t calculates t for a given value of cos𝜃.
//
// m3,m4: masses of the outgoing particles.
func Mandelstam_t(cos_theta, s, m3, m4 float64) float64 {
	m3_2 := m3 * m3
	m3_4 := m3_2 * m3_2
	m4_2 := m4 * m4
	p_prime := math.Sqrt((m3_4-2*m3_2*(m4_2+s)+(m4_2-s)*(m4_2-s))/s) / 2.0
	E3 := math.Sqrt(m3_2 + p_prime*p_prime)

	return m3_2 + math.Sqrt(s)*(p_prime*cos_theta-E3)
	//return -0.5*s*(1-math.Cos(theta))
}

type Parameter struct {
	Susy           *SUSY
	M_chargino     *linalg.Matrix2 // Chargino mass matrix (not diagonal)
	M_neutralino   *linalg.Matrix4 // Neutralino mass matrix (not diagonal)
	N              *linalg.Matrix4 // Matrix for diagonalizing the neutralino mass matrix via N^T.M.N
	U              *linalg.Matrix2
	V              *linalg.Matrix2
	M_i            float64 // Neutralino2 mass
	M_j            float64 // Chargino1 mass
	L              float64
	R              float64
	A_L_Chargino   float64
	A_L_c_Chargino float64
	A_L_t          float64
	A_L_u          float64
}

// NewParameterFromLheFile reads the parameters from an input file at path.
func NewParameterFromLheFile(path string) (*Parameter, error) {
	lfile := lhe.NewFile()
	lfile.AddBlockCmd("mass", lhe.ReadList)
	lfile.AddBlockCmd("nmix", lhe.ReadMatrix4)
	lfile.AddBlockCmd("umix", lhe.ReadMatrix2)
	lfile.AddBlockCmd("vmix", lhe.ReadMatrix2)
	data, err := lfile.ReadFromFile(path)
	if err != nil {
		return nil, err
	}

	tmp, ok := data.Blocks["mass"]
	if ok != true {
		return nil, fmt.Errorf("no mass block in file: %s", path)
	}
	masses := tmp.(map[int]float64)

	N := data.Blocks["nmix"].(*linalg.Matrix4)
	U := data.Blocks["umix"].(*linalg.Matrix2)
	V := data.Blocks["vmix"].(*linalg.Matrix2)

	i := 1 // use chi_2^0
	j := 0 // use chi_1^+

	// precalculate values for |M|²
	L := L(i, j, N, V)
	R := R(i, j, N, U)
	A_L_Chargino := A_L_Chargino(j, U)
	A_L_c_Chargino := A_L_c_Chargino(j, V)
	A_L_t := A_L(i, -1.0/3.0, -1.0/2.0, N)
	A_L_u := A_L(i, 2.0/3.0, 1.0/2.0, N)
	susy := &SUSY{
		M_su: masses[pdg.SUQuarkL],
		M_sd: masses[pdg.SDQuarkL],
		M_ss: masses[pdg.SSQuarkL],
		M_sc: masses[pdg.SCQuarkL],
	}

	return &Parameter{
		Susy:           susy,
		N:              N,
		U:              U,
		V:              V,
		M_i:            masses[pdg.Neutralino2],
		M_j:            masses[pdg.Chargino1],
		L:              L,
		R:              R,
		A_L_Chargino:   A_L_Chargino,
		A_L_c_Chargino: A_L_c_Chargino,
		A_L_t:          A_L_t,
		A_L_u:          A_L_u,
	}, nil
}

// NewParameter is an old function which should not be used anymore.
func NewParameter(mu float64, M1 float64, M2 float64, tan_beta float64, M_su float64, M_sd float64) *Parameter {
	susy := &SUSY{
		Mu:      mu,
		M_su:    M_su,
		M_sd:    M_sd,
		M_bino:  M1,
		M_wino:  M2,
		TanBeta: tan_beta,
	}
	M_chargino := CharginoMassMatrix(susy)
	M_neutralino := NeutralinoMassMatrix(susy)

	U, V, values := M_chargino.SingularValueDecomposition()
	ev, N := M_neutralino.Eigen()

	// Sort eigenvalues w.r.t. their absolute value
	// (use a simple bubble sort)
	evc := ev.Copy()
	for i, _ := range evc {
		evc[i] = math.Abs(evc[i])
	}

	for n := 4; n > 1; n-- {
		for k := 0; k < n-1; k++ {
			if evc[k] > evc[k+1] {
				evc[k], evc[k+1] = evc[k+1], evc[k]
				N.SwapColumns(k, k+1)
			}
		}
	}
	//------------------------------------

	// Print debug messages
	/*fmt.Printf("N = \n%s\n", N.MultilineString())
	fmt.Printf("N.M.N^T =\n%s\n", N.Transposed().Times(M_neutralino).Times(N).MultilineString())

	fmt.Printf("U = \n%s\n", U.MultilineString())
	fmt.Printf("V = \n%s\n", V.MultilineString())
	fmt.Printf("U^T.M.V =\n%s\n", U.Transposed().Times(M_chargino).Times(V).MultilineString())*/

	// Formular for chargino mass matrix diagonalization: U*.M.V^{-1}
	// Rewrite previously calculated matrices in this notation
	U = U.Transposed()
	V, _ = V.Inverted()

	N.Set(0, 0, 9.92797628E-01)
	N.Set(0, 1, -3.04145381E-02)
	N.Set(0, 2, 1.09080644E-01)
	N.Set(0, 3, -3.91054708E-02)
	N.Set(1, 0, 5.84996523E-02)
	N.Set(1, 1, 9.66019640E-01)
	N.Set(1, 2, -2.17829192E-01)
	N.Set(1, 3, 1.26231093E-01)
	N.Set(2, 0, -4.69368399E-02)
	N.Set(2, 1, 6.81242959E-02)
	N.Set(2, 2, 7.00360055E-01)
	N.Set(2, 3, 7.08979412E-01)
	N.Set(3, 0, -9.34215858E-02)
	N.Set(3, 1, 2.47467354E-01)
	N.Set(3, 2, 6.70930436E-01)
	N.Set(3, 3, -6.92737083E-01)

	fmt.Printf("N.M.N^T =\n%s\n", N.Times(M_neutralino).Times(N.Transposed()).MultilineString())

	U.Set(0, 0, 9.48909352E-01)
	U.Set(0, 1, -3.15548795E-01)
	U.Set(1, 0, 3.15548795E-01)
	U.Set(1, 1, 9.48909352E-01)

	V.Set(0, 0, 9.83010683E-01)
	V.Set(0, 1, -1.83548349E-01)
	V.Set(1, 0, 1.83548349E-01)
	V.Set(1, 1, 9.83010683E-01)

	fmt.Printf("V.M.U^T =\n%s\n", V.Times(M_chargino).Times(U.Transposed()).MultilineString())
	fmt.Printf("U.M.V^T =\n%s\n", U.Times(M_chargino).Times(V.Transposed()).MultilineString())

	fmt.Printf("U = \n%s\n", U.MultilineString())
	fmt.Printf("V = \n%s\n", V.MultilineString())

	m_i := evc[1]    // mass of chi_2^0
	m_j := values[0] // mass of chi_1^+
	fmt.Printf("m_neutralino_2 = %f\n", m_i)
	fmt.Printf("m_chargino_1 = %f\n", m_j)

	i := 1 // use chi_2^0
	j := 0 // use chi_1^+

	// precalculate values for |M|²
	L := L(i, j, N, V)
	R := R(i, j, N, U)
	A_L_Chargino := A_L_Chargino(j, U)
	A_L_c_Chargino := A_L_c_Chargino(j, V)
	A_L_t := A_L(i, -1.0/3.0, -1.0/2.0, N)
	A_L_u := A_L(i, 2.0/3.0, 1.0/2.0, N)

	// Print debug informations
	/*fmt.Printf("L = %f\n", L)
	fmt.Printf("R = %f\n", R)
	fmt.Printf("A_L_t = %f\n", A_L_t)
	fmt.Printf("A_L_u = %f\n", A_L_u)
	fmt.Printf("A_L_Chargino = %f\n", A_L_Chargino)
	fmt.Printf("A_L_c_Chargino = %f\n", A_L_c_Chargino)*/

	return &Parameter{
		Susy:           susy,
		M_chargino:     M_chargino,
		M_neutralino:   M_neutralino,
		N:              N,
		U:              U,
		V:              V,
		M_i:            2.35046162E+02, /*m_i*/
		M_j:            2.37406034E+02, /*m_j*/
		L:              L,
		R:              R,
		A_L_Chargino:   A_L_Chargino,
		A_L_c_Chargino: A_L_c_Chargino,
		A_L_t:          A_L_t,
		A_L_u:          A_L_u,
	}
}

// M2 returns the squared matrix element of pp -> chi_1^+ chi_2^0
//
// Parameter
//	s		Mandelstam variable s
//	cos_theta	angle in cms
//	quarks		0: u and d quarks as initial states, any other value: c and s quarks as initial states
//	p		SUSY Parameter e.g. quark masses
func M2(s, cos_theta float64, quarks int, p *Parameter) float64 {
	l := 1.0 / math.Sqrt2 / sw

	t := Mandelstam_t(cos_theta, s, p.M_i, p.M_j)

	// u = mc^2 + md^2 - s - t
	u := p.M_i*p.M_i + p.M_j*p.M_j - s - t
	u_i := u - p.M_i*p.M_i
	t_i := t - p.M_i*p.M_i
	u_j := u - p.M_j*p.M_j
	t_j := t - p.M_j*p.M_j

	t_q := 0.0
	u_q := 0.0
	if quarks == 0 {
		t_q = t - p.Susy.M_sd*p.Susy.M_sd
		u_q = u - p.Susy.M_su*p.Susy.M_su
	} else {
		t_q = t - p.Susy.M_ss*p.Susy.M_ss
		u_q = u - p.Susy.M_sc*p.Susy.M_sc
	}

	s_q := s - Mw*Mw

	l2 := l * l
	L2 := p.L * p.L
	R2 := p.R * p.R

	// s channel
	ss := 2.0 / s_q / s_q * (L2*l2*u_i*u_j + s*p.M_i*p.M_j*l2*2*p.L*p.R + R2*l2*t_i*t_j)
	// t channel
	tt := 1.0 / t_q / t_q * p.A_L_t * p.A_L_t * p.A_L_Chargino * p.A_L_Chargino * t_i * t_j
	// u channel
	uu := 1.0 / u_q / u_q * p.A_L_u * p.A_L_u * p.A_L_c_Chargino * p.A_L_c_Chargino * u_i * u_j

	// interference terms
	ts := 2.0 / t_q / s_q * (l*p.L*p.M_i*p.M_j*s + l*p.R*t_i*t_j) * p.A_L_t * p.A_L_Chargino
	us := 2.0 / u_q / s_q * (l*p.L*u_i*u_j + p.M_i*p.M_j*p.R*l*s) * (p.A_L_c_Chargino * p.A_L_u)
	tu := 2.0 / t_q / u_q * p.M_i * p.M_j * s * p.A_L_t * p.A_L_u * p.A_L_Chargino * p.A_L_c_Chargino

	//return (0.5*ss + 16.0*tt + 16.0*uu + 4.0*ts - 4.0*us - 16.0*tu)/5.0
	return 0.5*ss + tt + uu + ts - us - tu
}

// DSigma2 returns d𝜎/dcos𝜃 for pp -> 𝜒_1^+ 𝜒_2^0
//
// It's a different implementation of DSigma.
// Warning:
//	Only u,d quarks as initial states
func DSigma2(s, cos_theta float64, p *Parameter) float64 {
	t := Mandelstam_t(cos_theta, s, p.M_i, p.M_j)

	// u = mc^2 + md^2 - s - t
	u := p.M_i*p.M_i + p.M_j*p.M_j - s - t
	u_i := u - p.M_i*p.M_i
	t_i := t - p.M_i*p.M_i
	u_j := u - p.M_j*p.M_j
	t_j := t - p.M_j*p.M_j

	t_q := t - p.Susy.M_sd*p.Susy.M_sd
	u_q := u - p.Susy.M_su*p.Susy.M_su
	s_q := s - Mw*Mw

	// Prefetch values of N
	N23 := p.N.At(1, 2)
	N24 := p.N.At(1, 3)
	//N21 := p.N.At(1, 0)*cw + p.N.At(1, 1)*sw
	//N22 := -p.N.At(1, 0)*sw + p.N.At(1, 1)*cw
	N21 := p.N.At(1, 0)
	N22 := p.N.At(1, 1)

	Q_LL := 1.0 / Sw2 / math.Sqrt2 * ((N22*p.V.At(0, 0)-N24*p.V.At(0, 1)/math.Sqrt2)/s_q +
		+p.V.At(0, 0)/cw*(N21*(2.0/3.0-0.5)*sw+N22*0.5*cw)/u_q)

	Q_LR := 1.0 / Sw2 / math.Sqrt2 * ((N22*p.U.At(0, 0)+N23*p.U.At(0, 1)/math.Sqrt2)/s_q -
		p.U.At(0, 0)/cw*(N21*(-1/3.0+0.5)*sw+N22*(-0.5)*cw)/t_q)

	m3 := p.M_i
	m4 := p.M_j
	m3_2 := m3 * m3
	m3_4 := m3_2 * m3_2
	m4_2 := m4 * m4
	p_prime := math.Sqrt((m3_4-2*m3_2*(m4_2+s)+(m4_2-s)*(m4_2-s))/s) / 2.0

	return math.Pi * Alpha * Alpha / 3.0 / s / s * (Q_LL*Q_LL*u_i*u_j + Q_LR*Q_LR*t_i*t_j + 2*Q_LL*Q_LR*p.M_i*p.M_j*s) * math.Sqrt(s) * p_prime
}

// DSigma3 returns d𝜎/dcos𝜃 for e^+e^- -> µ^+ µ^- (massless particles).
//
// This function is for testing purpose.
func DSigma3(s, cos_theta float64, p *Parameter) float64 {
	t := Mandelstam_t(cos_theta, s, 0, 0)
	u := -s - t
	e2 := 4.0 * math.Pi * Alpha
	M2 := 2.0 * e2 * e2 * (t*t + u*u) / (s * s)

	return 1.0 / (16.0 * math.Pi * s * s) * M2 * s / 2.0
}

// Heaviside returns 0.0 if x < 0 and 1.0 otherwise.
func Heaviside(x float64) float64 {
	if x < 0.0 {
		return 0.0
	}
	return 1.0
}

// DSigma returns d𝜎/dcos𝜃 for pp -> 𝜒_1^+ 𝜒_2^0
//
// Parameter
//	s		Mandelstam variable s
//	cos_theta	angle in cms
//	quarks		0: u and d quarks as initial states, any other value: c and s quarks as initial states
//	p		SUSY Parameter e.g. quark masses
func DSigma(s, cos𝜃 float64, quarks int, p *Parameter) float64 {
	// precalculate powers of the masses
	m3 := p.M_i
	m4 := p.M_j
	m3_2 := m3 * m3
	m3_4 := m3_2 * m3_2
	m4_2 := m4 * m4
	p_prime := math.Sqrt((m3_4-2*m3_2*(m4_2+s)+(m4_2-s)*(m4_2-s))/s) / 2.0
	// |p| = sqrt(s)/2
	// d𝜎 /dcos𝜃 = d𝜎/ dt * dt/dcos𝜃 = d𝜎/dt * 2|p||p'|
	// d𝜎/dt = 1/16𝜋 1/s² |M|²
	// |M|² = e^4 M2
	return Alpha * Alpha * math.Pi / 3.0 / s / s * M2(s, cos𝜃, quarks, p) * math.Sqrt(s) * p_prime
}

// Sigma returns the total cross section of the process pp -> 𝜒_1^+ 𝜒_2^0.
//
// 	s: mandelstam, e.g. s = (14000 GeV)²
// 	Q: factorization scale for the pdfs
// 	N: number of monte carlo integration iterations
// 	p: SUSY parameter
func Sigma(s, Q float64, N int, p *Parameter) (sigma float64, error float64) {
	tau := (p.M_i + p.M_j) * (p.M_i + p.M_j)

	Integrand := func(x1, x2, t float64) float64 {
		// minimal value of s: 
		// x1*x2*s = (p3+p4)² >= (m3 + m4)² with non moving particles 3+4.
		// set integrand to 0.0 if the values do not obey the above inequality.
		h := Heaviside(x1*x2*s - tau)
		if h == 0.0 {
			return 0.0
		}
		// get values of pdfs
		fu_x1 := pdf.Xfx(x1, Q, pdf.UQuark) / x1
		fd_x2 := pdf.Xfx(x2, Q, pdf.DBarQuark) / x2
		fu_x2 := pdf.Xfx(x2, Q, pdf.UQuark) / x2
		fd_x1 := pdf.Xfx(x1, Q, pdf.DBarQuark) / x1

		fc_x1 := pdf.Xfx(x1, Q, pdf.CQuark) / x1
		fs_x2 := pdf.Xfx(x2, Q, pdf.SBarQuark) / x2
		fc_x2 := pdf.Xfx(x2, Q, pdf.CQuark) / x2
		fs_x1 := pdf.Xfx(x1, Q, pdf.SBarQuark) / x1

		return (fu_x1*fd_x2+fd_x1*fu_x2)*DSigma(x1*x2*s, t, 0, p) + (fc_x1*fs_x2+fs_x1*fc_x2)*DSigma(x1*x2*s, t, 1, p)
	}

	// Integrate over cos𝜃 = -1..1
	tmin := -1.0
	tmax := 1.0

	fmt.Printf("start int\n")

	// Integrate the diff. cross section
	sigma, error = integrator.Integrate3(Integrand, []float64{0.0, 0.0, tmin}, []float64{1.0, 1.0, tmax}, N)
	sigma *= CrossSectionToPb // Convert 1/GeV^2 in pb
	error *= CrossSectionToPb
	return
}
