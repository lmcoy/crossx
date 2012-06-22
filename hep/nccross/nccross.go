package nccross

// BUG(Lennart): negative masses of neutralinos in lhe not file supported! Sigma will fail silently!

import (
	"math"
	"physics/hep"
	"physics/hep/kinematics"
	"physics/hep/pdf"
	"physics/math/linalg"
	"physics/math/mcintegrator"
)

var sw = math.Sqrt(hep.Sw2)
var cw = math.Cos(math.Asin(sw))

type cache struct {
	L              float64
	R              float64
	A_L_Chargino   float64
	A_L_c_Chargino float64
	A_L_t          float64
	A_L_u          float64
}

func cA_L_Chargino(j int, U *linalg.Matrix2) float64 {
	return 1.0 / math.Sqrt2 * U.At(j, 0) / sw
}

func cA_L_c_Chargino(j int, V *linalg.Matrix2) float64 {
	return 1.0 / math.Sqrt2 * V.At(j, 0) / sw
}

func cA_L(i int, q, T3 float64, N *linalg.Matrix4) float64 {
	// convert N from bino-wino to photino-zino basis
	Ni1 := N.At(i, 0)*cw + N.At(i, 1)*sw
	Ni2 := -N.At(i, 0)*sw + N.At(i, 1)*cw

	return (sw*q*Ni1 + 1.0/cw*Ni2*(T3-q*hep.Sw2)) / sw
}

func cL(i, j int, N *linalg.Matrix4, V *linalg.Matrix2) float64 {
	// convert N from bino-wino to photino-zino basis
	Ni4 := N.At(i, 3)
	Ni1 := N.At(i, 0)*cw + N.At(i, 1)*sw
	Ni2 := -N.At(i, 0)*sw + N.At(i, 1)*cw

	return 1.0 / math.Sqrt2 / sw * (Ni4*V.At(j, 1) - math.Sqrt2*(sw*Ni1+cw*Ni2)*V.At(j, 0))
}

func cR(i, j int, N *linalg.Matrix4, U *linalg.Matrix2) float64 {
	// convert N from bino-wino to photino-zino basis
	Ni3 := N.At(i, 2)
	Ni1 := N.At(i, 0)*cw + N.At(i, 1)*sw
	Ni2 := -N.At(i, 0)*sw + N.At(i, 1)*cw

	return 1.0 / (math.Sqrt2 * sw) * (-Ni3*U.At(j, 1) - math.Sqrt2*(sw*Ni1+cw*Ni2)*U.At(j, 0))
}

// m2 returns the squared matrix element of pp -> chi_1^+ chi_2^0
//
// Parameter
//  i       Neutralino (0..3)
//  j       Chargino (0..1)
//	s		Mandelstam variable s
//	cos_theta	angle in cms
//	quarks		0: u and d quarks as initial states, any other value: c and s quarks as initial states
//	p		SUSY Parameter e.g. quark masses
//  c       cache for L,R, ..., if nil all values will be calculated
func m2(i, j int, s, cos_theta float64, quarks int, p *Parameter, c *cache) float64 {
	l := 1.0 / math.Sqrt2 / sw

	if i < 0 || i > 3 {
		return 0.0
	}
	if j < 0 || j > 1 {
		return 0.0
	}
	M_i := p.M_n[i]
	M_j := p.M_c[j]

	t := kinematics.Mandelstam_t(cos_theta, s, M_i, M_j)

	if c == nil {
		c = &cache{
			L:              cL(i, j, p.N, p.V),
			R:              cR(i, j, p.N, p.U),
			A_L_Chargino:   cA_L_Chargino(j, p.U),
			A_L_c_Chargino: cA_L_c_Chargino(j, p.V),
			A_L_t:          cA_L(i, -1.0/3.0, -1.0/2.0, p.N),
			A_L_u:          cA_L(i, 2.0/3.0, 1.0/2.0, p.N),
		}
	}

	// u = mc^2 + md^2 - s - t
	u := M_i*M_i + M_j*M_j - s - t
	u_i := u - M_i*M_i
	t_i := t - M_i*M_i
	u_j := u - M_j*M_j
	t_j := t - M_j*M_j

	t_q := 0.0
	u_q := 0.0
	if quarks == 0 {
		t_q = t - p.M_sd*p.M_sd
		u_q = u - p.M_su*p.M_su
	} else {
		t_q = t - p.M_ss*p.M_ss
		u_q = u - p.M_sc*p.M_sc
	}

	s_q := s - hep.Mw*hep.Mw

	l2 := l * l
	L2 := c.L * c.L
	R2 := c.R * c.R

	// s channel
	ss := 2.0 / s_q / s_q * (L2*l2*u_i*u_j + s*M_i*M_j*l2*2*c.L*c.R + R2*l2*t_i*t_j)
	// t channel
	tt := 1.0 / t_q / t_q * c.A_L_t * c.A_L_t * c.A_L_Chargino * c.A_L_Chargino * t_i * t_j
	// u channel
	uu := 1.0 / u_q / u_q * c.A_L_u * c.A_L_u * c.A_L_c_Chargino * c.A_L_c_Chargino * u_i * u_j

	// interference terms
	ts := 2.0 / t_q / s_q * (l*c.L*M_i*M_j*s + l*c.R*t_i*t_j) * c.A_L_t * c.A_L_Chargino
	us := 2.0 / u_q / s_q * (l*c.L*u_i*u_j + M_i*M_j*c.R*l*s) * (c.A_L_c_Chargino * c.A_L_u)
	tu := 2.0 / t_q / u_q * M_i * M_j * s * c.A_L_t * c.A_L_u * c.A_L_Chargino * c.A_L_c_Chargino

	return 0.5*ss + tt + uu + ts - us - tu
}

// DSigma2 returns d𝜎/dcos𝜃 for pp -> 𝜒_1^+ 𝜒_2^0
//
// It's a different implementation of DSigma.
// Warning:
//	Only u,d quarks as initial states
func DSigma2(s, cos_theta float64, p *Parameter) float64 {
	M_i := p.M_n[1]
	M_j := p.M_c[0]
	t := kinematics.Mandelstam_t(cos_theta, s, M_i, M_j)

	// u = mc^2 + md^2 - s - t
	u := M_i*M_i + M_j*M_j - s - t
	u_i := u - M_i*M_i
	t_i := t - M_i*M_i
	u_j := u - M_j*M_j
	t_j := t - M_j*M_j

	t_q := t - p.M_sd*p.M_sd
	u_q := u - p.M_su*p.M_su
	s_q := s - hep.Mw*hep.Mw

	// Prefetch values of N
	N23 := p.N.At(1, 2)
	N24 := p.N.At(1, 3)
	//N21 := p.N.At(1, 0)*cw + p.N.At(1, 1)*sw
	//N22 := -p.N.At(1, 0)*sw + p.N.At(1, 1)*cw
	N21 := p.N.At(1, 0)
	N22 := p.N.At(1, 1)

	Q_LL := 1.0 / hep.Sw2 / math.Sqrt2 * ((N22*p.V.At(0, 0)-N24*p.V.At(0, 1)/math.Sqrt2)/s_q +
		+p.V.At(0, 0)/cw*(N21*(2.0/3.0-0.5)*sw+N22*0.5*cw)/u_q)

	Q_LR := 1.0 / hep.Sw2 / math.Sqrt2 * ((N22*p.U.At(0, 0)+N23*p.U.At(0, 1)/math.Sqrt2)/s_q -
		p.U.At(0, 0)/cw*(N21*(-1/3.0+0.5)*sw+N22*(-0.5)*cw)/t_q)

	m3 := M_i
	m4 := M_j
	m3_2 := m3 * m3
	m3_4 := m3_2 * m3_2
	m4_2 := m4 * m4
	p_prime := math.Sqrt((m3_4-2*m3_2*(m4_2+s)+(m4_2-s)*(m4_2-s))/s) / 2.0

	return math.Pi * hep.Alpha * hep.Alpha / 3.0 / s / s * (Q_LL*Q_LL*u_i*u_j + Q_LR*Q_LR*t_i*t_j + 2*Q_LL*Q_LR*M_i*M_j*s) * math.Sqrt(s) * p_prime
}

// DSigma returns d𝜎/dcos𝜃 for pp -> 𝜒_1^+ 𝜒_2^0
//
// Parameter
//  i		Neutralino (0..3)
//  j       Chargino (0,1)
//	s		Mandelstam variable s
//	cos_theta	angle in cms
//	quarks		0: u and d quarks as initial states, any other value: c and s quarks as initial states
//	p		SUSY Parameter e.g. quark masses
func DSigma(i, j int, s, cos𝜃 float64, quarks int, p *Parameter, c *cache) float64 {
	if i < 0 || i > 3 {
		return 0.0
	}
	if j < 0 || j > 1 {
		return 0.0
	}
	M_i := p.M_n[i]
	M_j := p.M_c[j]
	// precalculate powers of the masses
	m3 := M_i
	m4 := M_j
	m3_2 := m3 * m3
	m3_4 := m3_2 * m3_2
	m4_2 := m4 * m4
	p_prime := math.Sqrt((m3_4-2*m3_2*(m4_2+s)+(m4_2-s)*(m4_2-s))/s) / 2.0
	// |p| = sqrt(s)/2
	// d𝜎 /dcos𝜃 = d𝜎/ dt * dt/dcos𝜃 = d𝜎/dt * 2|p||p'|
	// d𝜎/dt = 1/16𝜋 1/s² |M|²
	// |M|² = e^4 m2
	return hep.Alpha * hep.Alpha * math.Pi / 3.0 / s / s * m2(i, j, s, cos𝜃, quarks, p, c) * math.Sqrt(s) * p_prime
}

// Sigma returns the total cross section of the process pp -> 𝜒_1^+ 𝜒_2^0.
//
//  i		Neutralino (0..3)
//  j       Chargino (0,1)
// 	s: mandelstam, e.g. s = (14000 GeV)²
// 	Q: factorization scale for the pdfs
// 	N: number of monte carlo integration iterations
// 	p: SUSY parameter
//
// only i = 1, j = 0 tested!
// negative masses of neutralinos in lhe not supported! Sigma will fail silently!
// If i or j is not valid this function returns -1.0, 0.0 as cross section.
func Sigma(i, j int, s, Q float64, N int, p *Parameter) (sigma float64, error float64) {
	if i < 0 || i > 3 {
		return -1.0, 0.0
	}
	if j < 0 || j > 1 {
		return -1.0, 0.0
	}
	M_i := p.M_n[i]
	M_j := p.M_c[j]
	tau := (M_i + M_j) * (M_i + M_j)

	// precalculate for |M|²
	c := &cache{
		L:              cL(i, j, p.N, p.V),
		R:              cR(i, j, p.N, p.U),
		A_L_Chargino:   cA_L_Chargino(j, p.U),
		A_L_c_Chargino: cA_L_c_Chargino(j, p.V),
		A_L_t:          cA_L(i, -1.0/3.0, -1.0/2.0, p.N),
		A_L_u:          cA_L(i, 2.0/3.0, 1.0/2.0, p.N),
	}

	Integrand := func(x1, x2, t float64) float64 {
		// minimal value of s: 
		// x1*x2*s = (p3+p4)² >= (m3 + m4)² with non moving particles 3+4.
		// set integrand to 0.0 if the values do not obey the above inequality.
		h := hep.Heaviside(x1*x2*s - tau)
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

		return (fu_x1*fd_x2+fd_x1*fu_x2)*DSigma(i, j, x1*x2*s, t, 0, p, c) + (fc_x1*fs_x2+fs_x1*fc_x2)*DSigma(i, j, x1*x2*s, t, 1, p, c)
	}

	// Integrate over cos𝜃 = -1..1
	tmin := -1.0
	tmax := 1.0

	// Integrate the diff. cross section
	sigma, error = mcintegrator.Integrate3(Integrand, []float64{0.0, 0.0, tmin}, []float64{1.0, 1.0, tmax}, N)
	sigma *= hep.CrossSectionToPb // Convert 1/GeV^2 in pb
	error *= hep.CrossSectionToPb
	return
}
