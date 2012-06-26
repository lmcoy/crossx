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
     1    7.50000000e+02   # m0
     2    6.50000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.79740925e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03881496e+01   # MW
        25     1.18444005e+02   # h0
        35     8.64601594e+02   # H0
        36     8.64520001e+02   # A0
        37     8.68549095e+02   # H+
   1000021     1.48997517e+03   # ~g
   1000022     2.73952223e+02   # ~neutralino(1)
   1000023     5.21377414e+02   # ~neutralino(2)
   1000024     5.21476453e+02   # ~chargino(1)
   1000025    -8.51037819e+02   # ~neutralino(3)
   1000035     8.59226754e+02   # ~neutralino(4)
   1000037     8.59561877e+02   # ~chargino(2)
   1000001     1.52211253e+03   # ~d_L
   1000002     1.52020260e+03   # ~u_L
   1000003     1.52206897e+03   # ~s_L
   1000004     1.52015897e+03   # ~c_L
   1000005     1.27055472e+03   # ~b_1
   1000006     1.08717430e+03   # ~t_1
   1000011     8.65163602e+02   # ~e_L
   1000012     8.61211934e+02   # ~nue_L
   1000013     8.65102574e+02   # ~mu_L
   1000014     8.61004585e+02   # ~numu_L
   1000015     6.09241351e+02   # ~stau_1
   1000016     7.89894370e+02   # ~nu_tau_L
   2000001     1.47303929e+03   # ~d_R
   2000002     1.47719714e+03   # ~u_R
   2000003     1.47295363e+03   # ~s_R
   2000004     1.47719153e+03   # ~c_R
   2000005     1.34756421e+03   # ~b_2
   2000006     1.31988685e+03   # ~t_2
   2000011     7.88645137e+02   # ~e_R
   2000013     7.88188052e+02   # ~mu_R
   2000015     8.03947209e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59205354e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97966533e-01   # N_{1,1}
  1  2    -7.00789613e-03   # N_{1,2}
  1  3     5.98033104e-02   # N_{1,3}
  1  4    -2.09105881e-02   # N_{1,4}
  2  1     1.76008926e-02   # N_{2,1}
  2  2     9.84841721e-01   # N_{2,2}
  2  3    -1.46329204e-01   # N_{2,3}
  2  4     9.14590476e-02   # N_{2,4}
  3  1    -2.71361537e-02   # N_{3,1}
  3  2     3.95012449e-02   # N_{3,2}
  3  3     7.04907041e-01   # N_{3,3}
  3  4     7.07678843e-01   # N_{3,4}
  4  1    -5.49239199e-02   # N_{4,1}
  4  2     1.68752262e-01   # N_{4,2}
  4  3     6.91460333e-01   # N_{4,3}
  4  4    -7.00277549e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.78471305e-01   # U_{1,1}
  1  2    -2.06382908e-01   # U_{1,2}
  2  1     2.06382908e-01   # U_{2,1}
  2  2     9.78471305e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91364221e-01   # V_{1,1}
  1  2    -1.31137261e-01   # V_{1,2}
  2  1     1.31137261e-01   # V_{2,1}
  2  2     9.91364221e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.67697526e-01   # F_{11}
  1  2     9.29945444e-01   # F_{12}
  2  1     9.29945444e-01   # F_{21}
  2  2    -3.67697526e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.11604905e-01   # F_{11}
  1  2     4.11067509e-01   # F_{12}
  2  1    -4.11067509e-01   # F_{21}
  2  2     9.11604905e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.37491558e-01   # F_{11}
  1  2     9.71389603e-01   # F_{12}
  2  1     9.71389603e-01   # F_{21}
  2  2    -2.37491558e-01   # F_{22}
Block gauge Q= 1.16443814e+03  # SM gauge couplings
     1     3.62624476e-01   # g'(Q)MSSM DRbar
     2     6.40742319e-01   # g(Q)MSSM DRbar
     3     1.04601080e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.16443814e+03  
  3  3     8.46855471e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.16443814e+03  
  3  3     4.95468783e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.16443814e+03  
  3  3     4.23688557e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.16443814e+03 # Higgs mixing parameters
     1     8.46571567e+02    # mu(Q)MSSM DRbar
     2     3.91662038e+01    # tan beta(Q)MSSM DRbar
     3     2.43680248e+02    # higgs vev(Q)MSSM DRbar
     4     9.55918411e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.16443814e+03  # MSSM DRbar SUSY breaking parameters
     1     2.77020754e+02      # M_1(Q)
     2     5.10796007e+02      # M_2(Q)
     3     1.42162697e+03      # M_3(Q)
    21     4.48932003e+04      # mH1^2(Q)
    22    -6.98977579e+05      # mH2^2(Q)
    31     8.60784117e+02      # meL(Q)
    32     8.60576596e+02      # mmuL(Q)
    33     7.91995055e+02      # mtauL(Q)
    34     7.85602131e+02      # meR(Q)
    35     7.85143758e+02      # mmuR(Q)
    36     6.22399350e+02      # mtauR(Q)
    41     1.47886636e+03      # mqL1(Q)
    42     1.47882132e+03      # mqL2(Q)
    43     1.25027392e+03      # mqL3(Q)
    44     1.43646765e+03      # muR(Q)
    45     1.43646187e+03      # mcR(Q)
    46     1.07896461e+03      # mtR(Q)
    47     1.43136953e+03      # mdR(Q)
    48     1.43128120e+03      # msR(Q)
    49     1.29701726e+03      # mbR(Q)
Block au Q= 1.16443814e+03  
  1  1    -1.78111967e+03      # Au(Q)MSSM DRbar
  2  2    -1.78107801e+03      # Ac(Q)MSSM DRbar
  3  3    -1.25140933e+03      # At(Q)MSSM DRbar
Block ad Q= 1.16443814e+03  
  1  1    -2.05359694e+03      # Ad(Q)MSSM DRbar
  2  2    -2.05349087e+03      # As(Q)MSSM DRbar
  3  3    -1.73164033e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.16443814e+03  
  1  1    -6.82814653e+02      # Ae(Q)MSSM DRbar
  2  2    -6.82482192e+02      # Amu(Q)MSSM DRbar
  3  3    -5.72968446e+02      # Atau(Q)MSSM DRbar
