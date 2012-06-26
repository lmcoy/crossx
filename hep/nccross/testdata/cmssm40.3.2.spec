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
     1    1.05000000e+03   # m0
     2    3.75000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.21608857e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03905257e+01   # MW
        25     1.15871497e+02   # h0
        35     8.22261625e+02   # H0
        36     8.22434574e+02   # A0
        37     8.26493770e+02   # H+
   1000021     9.32454564e+02   # ~g
   1000022     1.55752154e+02   # ~neutralino(1)
   1000023     2.97724401e+02   # ~neutralino(2)
   1000024     2.97771706e+02   # ~chargino(1)
   1000025    -5.48244005e+02   # ~neutralino(3)
   1000035     5.58793951e+02   # ~neutralino(4)
   1000037     5.59427081e+02   # ~chargino(2)
   1000001     1.30095335e+03   # ~d_L
   1000002     1.29866079e+03   # ~u_L
   1000003     1.30090687e+03   # ~s_L
   1000004     1.29861423e+03   # ~c_L
   1000005     1.01229655e+03   # ~b_1
   1000006     8.34130449e+02   # ~t_1
   1000011     1.07654529e+03   # ~e_L
   1000012     1.07327973e+03   # ~nue_L
   1000013     1.07630460e+03   # ~mu_L
   1000014     1.07300882e+03   # ~numu_L
   1000015     8.66296574e+02   # ~stau_1
   1000016     9.85019185e+02   # ~nu_tau_L
   2000001     1.28366385e+03   # ~d_R
   2000002     1.28438897e+03   # ~u_R
   2000003     1.28357506e+03   # ~s_R
   2000004     1.28438293e+03   # ~c_R
   2000005     1.13043459e+03   # ~b_2
   2000006     1.04805596e+03   # ~t_2
   2000011     1.05896000e+03   # ~e_R
   2000013     1.05840864e+03   # ~mu_R
   2000015     9.92060612e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59987883e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95183293e-01   # N_{1,1}
  1  2    -1.63314149e-02   # N_{1,2}
  1  3     9.22549088e-02   # N_{1,3}
  1  4    -2.88535917e-02   # N_{1,4}
  2  1     3.77431664e-02   # N_{2,1}
  2  2     9.72651553e-01   # N_{2,2}
  2  3    -1.99914889e-01   # N_{2,3}
  2  4     1.12064479e-01   # N_{2,4}
  3  1    -4.34405725e-02   # N_{3,1}
  3  2     6.42593274e-02   # N_{3,2}
  3  3     7.01540380e-01   # N_{3,3}
  3  4     7.08395899e-01   # N_{3,4}
  4  1    -7.93636132e-02   # N_{4,1}
  4  2     2.22604988e-01   # N_{4,2}
  4  3     6.77764091e-01   # N_{4,3}
  4  4    -6.96264513e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.59423196e-01   # U_{1,1}
  1  2    -2.81970090e-01   # U_{1,2}
  2  1     2.81970090e-01   # U_{2,1}
  2  2     9.59423196e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86958483e-01   # V_{1,1}
  1  2    -1.60975004e-01   # V_{1,2}
  2  1     1.60975004e-01   # V_{2,1}
  2  2     9.86958483e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.29812688e-01   # F_{11}
  1  2     9.44046392e-01   # F_{12}
  2  1     9.44046392e-01   # F_{21}
  2  2    -3.29812688e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.79588481e-01   # F_{11}
  1  2     2.01013453e-01   # F_{12}
  2  1    -2.01013453e-01   # F_{21}
  2  2     9.79588481e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.73681864e-01   # F_{11}
  1  2     9.84801813e-01   # F_{12}
  2  1     9.84801813e-01   # F_{21}
  2  2    -1.73681864e-01   # F_{22}
Block gauge Q= 9.12917028e+02  # SM gauge couplings
     1     3.61906247e-01   # g'(Q)MSSM DRbar
     2     6.42507258e-01   # g(Q)MSSM DRbar
     3     1.06238302e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.12917028e+02  
  3  3     8.59696408e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.12917028e+02  
  3  3     5.18154083e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.12917028e+02  
  3  3     4.12539432e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.12917028e+02 # Higgs mixing parameters
     1     5.40342591e+02    # mu(Q)MSSM DRbar
     2     3.92443827e+01    # tan beta(Q)MSSM DRbar
     3     2.43798486e+02    # higgs vev(Q)MSSM DRbar
     4     8.14605104e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.12917028e+02  # MSSM DRbar SUSY breaking parameters
     1     1.57565631e+02      # M_1(Q)
     2     2.93230468e+02      # M_2(Q)
     3     8.41552262e+02      # M_3(Q)
    21     4.01287289e+05      # mH1^2(Q)
    22    -2.81501098e+05      # mH2^2(Q)
    31     1.07387233e+03      # meL(Q)
    32     1.07360227e+03      # mmuL(Q)
    33     9.87798757e+02      # mtauL(Q)
    34     1.05690273e+03      # meR(Q)
    35     1.05635111e+03      # mmuR(Q)
    36     8.71541498e+02      # mtauR(Q)
    41     1.27747283e+03      # mqL1(Q)
    42     1.27742558e+03      # mqL2(Q)
    43     9.97652135e+02      # mqL3(Q)
    44     1.26398019e+03      # muR(Q)
    45     1.26397406e+03      # mcR(Q)
    46     8.23592340e+02      # mtR(Q)
    47     1.26250410e+03      # mdR(Q)
    48     1.26241371e+03      # msR(Q)
    49     1.10706952e+03      # mbR(Q)
Block au Q= 9.12917028e+02  
  1  1    -1.19830965e+03      # Au(Q)MSSM DRbar
  2  2    -1.19827888e+03      # Ac(Q)MSSM DRbar
  3  3    -7.99745765e+02      # At(Q)MSSM DRbar
Block ad Q= 9.12917028e+02  
  1  1    -1.39295052e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39287216e+03      # As(Q)MSSM DRbar
  3  3    -1.14469385e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.12917028e+02  
  1  1    -5.62976292e+02      # Ae(Q)MSSM DRbar
  2  2    -5.62680862e+02      # Amu(Q)MSSM DRbar
  3  3    -4.70952641e+02      # Atau(Q)MSSM DRbar
