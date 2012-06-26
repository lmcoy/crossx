# SOFTSUSY3.3.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.1       # version number
Block MODSEL  # Select model
     1    1   # sugra
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    4.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    3.45000000e+02   # m0
     2    5.50000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.81312682e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03893551e+01   # MW
        25     1.17473510e+02   # h0
        35     6.52443196e+02   # H0
        36     6.52376253e+02   # A0
        37     6.57658314e+02   # H+
   1000021     1.25834386e+03   # ~g
   1000022     2.28728101e+02   # ~neutralino(1)
   1000023     4.35804190e+02   # ~neutralino(2)
   1000024     4.35874758e+02   # ~chargino(1)
   1000025    -7.56013542e+02   # ~neutralino(3)
   1000035     7.63914796e+02   # ~neutralino(4)
   1000037     7.64405595e+02   # ~chargino(2)
   1000001     1.19425376e+03   # ~d_L
   1000002     1.19173258e+03   # ~u_L
   1000003     1.19421887e+03   # ~s_L
   1000004     1.19169761e+03   # ~c_L
   1000005     9.98110436e+02   # ~b_1
   1000006     8.55766738e+02   # ~t_1
   1000011     5.06794898e+02   # ~e_L
   1000012     5.00297854e+02   # ~nue_L
   1000013     5.06837142e+02   # ~mu_L
   1000014     5.00159226e+02   # ~numu_L
   1000015     2.30352853e+02   # ~stau_1
   1000016     4.52839309e+02   # ~nu_tau_L
   2000001     1.14726440e+03   # ~d_R
   2000002     1.15095922e+03   # ~u_R
   2000003     1.14719507e+03   # ~s_R
   2000004     1.15095484e+03   # ~c_R
   2000005     1.06648282e+03   # ~b_2
   2000006     1.07142582e+03   # ~t_2
   2000011     4.04028174e+02   # ~e_R
   2000013     4.03679504e+02   # ~mu_R
   2000015     4.81530042e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60953577e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97489679e-01   # N_{1,1}
  1  2    -8.89605693e-03   # N_{1,2}
  1  3     6.66758905e-02   # N_{1,3}
  1  4    -2.21252244e-02   # N_{1,4}
  2  1     2.11237319e-02   # N_{2,1}
  2  2     9.83534232e-01   # N_{2,2}
  2  3    -1.54454533e-01   # N_{2,3}
  2  4     9.14220986e-02   # N_{2,4}
  3  1    -3.09656407e-02   # N_{3,1}
  3  2     4.54571137e-02   # N_{3,2}
  3  3     7.04209842e-01   # N_{3,3}
  3  4     7.07858233e-01   # N_{3,4}
  4  1    -6.00770905e-02   # N_{4,1}
  4  2     1.74685220e-01   # N_{4,2}
  4  3     6.89772876e-01   # N_{4,3}
  4  4    -7.00063709e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.76012165e-01   # U_{1,1}
  1  2    -2.17715991e-01   # U_{1,2}
  2  1     2.17715991e-01   # U_{2,1}
  2  2     9.76012165e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91367212e-01   # V_{1,1}
  1  2    -1.31114648e-01   # V_{1,2}
  2  1     1.31114648e-01   # V_{2,1}
  2  2     9.91367212e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.53855731e-01   # F_{11}
  1  2     8.91075179e-01   # F_{12}
  2  1     8.91075179e-01   # F_{21}
  2  2    -4.53855731e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.11094909e-01   # F_{11}
  1  2     5.84914565e-01   # F_{12}
  2  1    -5.84914565e-01   # F_{21}
  2  2     8.11094909e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.36720758e-01   # F_{11}
  1  2     9.41604551e-01   # F_{12}
  2  1     9.41604551e-01   # F_{21}
  2  2    -3.36720758e-01   # F_{22}
Block gauge Q= 9.30217357e+02  # SM gauge couplings
     1     3.62334069e-01   # g'(Q)MSSM DRbar
     2     6.41896573e-01   # g(Q)MSSM DRbar
     3     1.05658495e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.30217357e+02  
  3  3     8.53289595e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.30217357e+02  
  3  3     4.90684975e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.30217357e+02  
  3  3     4.27529298e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.30217357e+02 # Higgs mixing parameters
     1     7.52805319e+02    # mu(Q)MSSM DRbar
     2     3.92128528e+01    # tan beta(Q)MSSM DRbar
     3     2.43913125e+02    # higgs vev(Q)MSSM DRbar
     4     5.40388303e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.30217357e+02  # MSSM DRbar SUSY breaking parameters
     1     2.32433109e+02      # M_1(Q)
     2     4.30639669e+02      # M_2(Q)
     3     1.22095090e+03      # M_3(Q)
    21    -1.31679963e+05      # mH1^2(Q)
    22    -5.58038613e+05      # mH2^2(Q)
    31     5.00867797e+02      # meL(Q)
    32     5.00728821e+02      # mmuL(Q)
    33     4.56298077e+02      # mtauL(Q)
    34     3.99322153e+02      # meR(Q)
    35     3.98969399e+02      # mmuR(Q)
    36     2.69801736e+02      # mtauR(Q)
    41     1.15646573e+03      # mqL1(Q)
    42     1.15643013e+03      # mqL2(Q)
    43     9.94495083e+02      # mqL3(Q)
    44     1.11628307e+03      # muR(Q)
    45     1.11627862e+03      # mcR(Q)
    46     8.65719746e+02      # mtR(Q)
    47     1.11145278e+03      # mdR(Q)
    48     1.11138226e+03      # msR(Q)
    49     1.01172516e+03      # mbR(Q)
Block au Q= 9.30217357e+02  
  1  1    -1.58554800e+03      # Au(Q)MSSM DRbar
  2  2    -1.58550970e+03      # Ac(Q)MSSM DRbar
  3  3    -1.10091679e+03      # At(Q)MSSM DRbar
Block ad Q= 9.30217357e+02  
  1  1    -1.83992665e+03      # Ad(Q)MSSM DRbar
  2  2    -1.83982911e+03      # As(Q)MSSM DRbar
  3  3    -1.54945400e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.30217357e+02  
  1  1    -6.46052335e+02      # Ae(Q)MSSM DRbar
  2  2    -6.45731944e+02      # Amu(Q)MSSM DRbar
  3  3    -5.38592842e+02      # Atau(Q)MSSM DRbar
