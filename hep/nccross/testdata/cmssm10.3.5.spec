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
     3    1.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    5.00000000e+02   # m0
     2    7.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.71271549e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03882095e+01   # MW
        25     1.17525857e+02   # h0
        35     1.13499106e+03   # H0
        36     1.13476038e+03   # A0
        37     1.13787632e+03   # H+
   1000021     1.68029952e+03   # ~g
   1000022     3.14643204e+02   # ~neutralino(1)
   1000023     5.95336257e+02   # ~neutralino(2)
   1000024     5.95549492e+02   # ~chargino(1)
   1000025    -9.05766527e+02   # ~neutralino(3)
   1000035     9.16975899e+02   # ~neutralino(4)
   1000037     9.16603923e+02   # ~chargino(2)
   1000001     1.59640008e+03   # ~d_L
   1000002     1.59460015e+03   # ~u_L
   1000003     1.59639598e+03   # ~s_L
   1000004     1.59459604e+03   # ~c_L
   1000005     1.45226745e+03   # ~b_1
   1000006     1.21860869e+03   # ~t_1
   1000011     7.07475256e+02   # ~e_L
   1000012     7.02834547e+02   # ~nue_L
   1000013     7.07657833e+02   # ~mu_L
   1000014     7.02826736e+02   # ~numu_L
   1000015     5.66705467e+02   # ~stau_1
   1000016     7.00283828e+02   # ~nu_tau_L
   2000001     1.53237788e+03   # ~d_R
   2000002     1.53812933e+03   # ~u_R
   2000003     1.53237366e+03   # ~s_R
   2000004     1.53812489e+03   # ~c_R
   2000005     1.52503795e+03   # ~b_2
   2000006     1.48178163e+03   # ~t_2
   2000011     5.74258568e+02   # ~e_R
   2000013     5.74239198e+02   # ~mu_R
   2000015     7.06033693e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05086825e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97911589e-01   # N_{1,1}
  1  2    -8.59473567e-03   # N_{1,2}
  1  3     5.86248361e-02   # N_{1,3}
  1  4    -2.57239180e-02   # N_{1,4}
  2  1     2.05077442e-02   # N_{2,1}
  2  2     9.81203663e-01   # N_{2,2}
  2  3    -1.56542251e-01   # N_{2,3}
  2  4     1.10965433e-01   # N_{2,4}
  3  1    -2.29121782e-02   # N_{3,1}
  3  2     3.29810380e-02   # N_{3,2}
  3  3     7.05375086e-01   # N_{3,3}
  3  4     7.07695748e-01   # N_{3,4}
  4  1    -5.68060328e-02   # N_{4,1}
  4  2     1.89941446e-01   # N_{4,2}
  4  3     6.88842247e-01   # N_{4,3}
  4  4    -6.97274466e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.75278600e-01   # U_{1,1}
  1  2    -2.20978849e-01   # U_{1,2}
  2  1     2.20978849e-01   # U_{2,1}
  2  2     9.75278600e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.87404341e-01   # V_{1,1}
  1  2    -1.58217154e-01   # V_{1,2}
  2  1     1.58217154e-01   # V_{2,1}
  2  2     9.87404341e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.05592362e-01   # F_{11}
  1  2     9.52162438e-01   # F_{12}
  2  1     9.52162438e-01   # F_{21}
  2  2    -3.05592362e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.93322030e-01   # F_{11}
  1  2     1.15374801e-01   # F_{12}
  2  1    -1.15374801e-01   # F_{21}
  2  2     9.93322030e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.29519903e-02   # F_{11}
  1  2     9.95670592e-01   # F_{12}
  2  1     9.95670592e-01   # F_{21}
  2  2    -9.29519903e-02   # F_{22}
Block gauge Q= 1.30504035e+03  # SM gauge couplings
     1     3.63072980e-01   # g'(Q)MSSM DRbar
     2     6.40696618e-01   # g(Q)MSSM DRbar
     3     1.04051070e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.30504035e+03  
  3  3     8.48238048e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.30504035e+03  
  3  3     1.32782339e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.30504035e+03  
  3  3     1.00133897e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.30504035e+03 # Higgs mixing parameters
     1     8.99716679e+02    # mu(Q)MSSM DRbar
     2     9.62625593e+00    # tan beta(Q)MSSM DRbar
     3     2.43620130e+02    # higgs vev(Q)MSSM DRbar
     4     1.32894640e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.30504035e+03  # MSSM DRbar SUSY breaking parameters
     1     3.19640773e+02      # M_1(Q)
     2     5.87616466e+02      # M_2(Q)
     3     1.62259917e+03      # M_3(Q)
    21     4.50377802e+05      # mH1^2(Q)
    22    -7.72128997e+05      # mH2^2(Q)
    31     7.00542239e+02      # meL(Q)
    32     7.00534381e+02      # mmuL(Q)
    33     6.98156205e+02      # mtauL(Q)
    34     5.69552946e+02      # meR(Q)
    35     5.69533420e+02      # mmuR(Q)
    36     5.63602939e+02      # mtauR(Q)
    41     1.54486304e+03      # mqL1(Q)
    42     1.54485885e+03      # mqL2(Q)
    43     1.41212423e+03      # mqL3(Q)
    44     1.48979177e+03      # muR(Q)
    45     1.48978725e+03      # mcR(Q)
    46     1.20042507e+03      # mtR(Q)
    47     1.48302468e+03      # mdR(Q)
    48     1.48302039e+03      # msR(Q)
    49     1.47515315e+03      # mbR(Q)
Block au Q= 1.30504035e+03  
  1  1    -1.63801264e+03      # Au(Q)MSSM DRbar
  2  2    -1.63800541e+03      # Ac(Q)MSSM DRbar
  3  3    -1.27138369e+03      # At(Q)MSSM DRbar
Block ad Q= 1.30504035e+03  
  1  1    -1.99495423e+03      # Ad(Q)MSSM DRbar
  2  2    -1.99494756e+03      # As(Q)MSSM DRbar
  3  3    -1.86629587e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.30504035e+03  
  1  1    -4.40789334e+02      # Ae(Q)MSSM DRbar
  2  2    -4.40781605e+02      # Amu(Q)MSSM DRbar
  3  3    -4.38445209e+02      # Atau(Q)MSSM DRbar
