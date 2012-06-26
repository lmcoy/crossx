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
     1    1.37500000e+02   # m0
     2    5.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.81499687e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03916813e+01   # MW
        25     1.15526085e+02   # h0
        35     7.83852307e+02   # H0
        36     7.83590366e+02   # A0
        37     7.87933210e+02   # H+
   1000021     1.25186472e+03   # ~g
   1000022     2.25876400e+02   # ~neutralino(1)
   1000023     4.27298073e+02   # ~neutralino(2)
   1000024     4.27456034e+02   # ~chargino(1)
   1000025    -6.91039669e+02   # ~neutralino(3)
   1000035     7.04022090e+02   # ~neutralino(4)
   1000037     7.03646437e+02   # ~chargino(2)
   1000001     1.15145612e+03   # ~d_L
   1000002     1.14888168e+03   # ~u_L
   1000003     1.15145332e+03   # ~s_L
   1000004     1.14887888e+03   # ~c_L
   1000005     1.05444156e+03   # ~b_1
   1000006     8.81725172e+02   # ~t_1
   1000011     3.96774340e+02   # ~e_L
   1000012     3.88673781e+02   # ~nue_L
   1000013     3.96852460e+02   # ~mu_L
   1000014     3.88670136e+02   # ~numu_L
   1000015     2.44857205e+02   # ~stau_1
   1000016     3.87396941e+02   # ~nu_tau_L
   2000001     1.10230491e+03   # ~d_R
   2000002     1.10618235e+03   # ~u_R
   2000003     1.10230199e+03   # ~s_R
   2000004     1.10617935e+03   # ~c_R
   2000005     1.09844875e+03   # ~b_2
   2000006     1.09694608e+03   # ~t_2
   2000011     2.51953220e+02   # ~e_R
   2000013     2.51941803e+02   # ~mu_R
   2000015     3.97576303e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06319085e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96466798e-01   # N_{1,1}
  1  2    -1.47654425e-02   # N_{1,2}
  1  3     7.62246631e-02   # N_{1,3}
  1  4    -3.20265878e-02   # N_{1,4}
  2  1     3.28096999e-02   # N_{2,1}
  2  2     9.73589456e-01   # N_{2,2}
  2  3    -1.87115127e-01   # N_{2,3}
  2  4     1.26629474e-01   # N_{2,4}
  3  1    -3.04399966e-02   # N_{3,1}
  3  2     4.42314141e-02   # N_{3,2}
  3  3     7.04032972e-01   # N_{3,3}
  3  4     7.08134565e-01   # N_{3,4}
  4  1    -7.10693330e-02   # N_{4,1}
  4  2     2.23493030e-01   # N_{4,2}
  4  3     6.80819582e-01   # N_{4,3}
  4  4    -6.93890994e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.64471765e-01   # U_{1,1}
  1  2    -2.64185946e-01   # U_{1,2}
  2  1     2.64185946e-01   # U_{2,1}
  2  2     9.64471765e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.83554944e-01   # V_{1,1}
  1  2    -1.80609171e-01   # V_{1,2}
  2  1     1.80609171e-01   # V_{2,1}
  2  2     9.83554944e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.04673607e-01   # F_{11}
  1  2     9.14461192e-01   # F_{12}
  2  1     9.14461192e-01   # F_{21}
  2  2    -4.04673607e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.78498080e-01   # F_{11}
  1  2     2.06255927e-01   # F_{12}
  2  1    -2.06255927e-01   # F_{21}
  2  2     9.78498080e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.28981725e-01   # F_{11}
  1  2     9.91646971e-01   # F_{12}
  2  1     9.91646971e-01   # F_{21}
  2  2    -1.28981725e-01   # F_{22}
Block gauge Q= 9.54039501e+02  # SM gauge couplings
     1     3.62600000e-01   # g'(Q)MSSM DRbar
     2     6.42516445e-01   # g(Q)MSSM DRbar
     3     1.05629482e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.54039501e+02  
  3  3     8.58191811e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.54039501e+02  
  3  3     1.34701535e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.54039501e+02  
  3  3     1.00458106e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.54039501e+02 # Higgs mixing parameters
     1     6.85615474e+02    # mu(Q)MSSM DRbar
     2     9.66313234e+00    # tan beta(Q)MSSM DRbar
     3     2.43999515e+02    # higgs vev(Q)MSSM DRbar
     4     6.36672348e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.54039501e+02  # MSSM DRbar SUSY breaking parameters
     1     2.31162293e+02      # M_1(Q)
     2     4.28171263e+02      # M_2(Q)
     3     1.21665182e+03      # M_3(Q)
    21     1.31974738e+05      # mH1^2(Q)
    22    -4.54072748e+05      # mH2^2(Q)
    31     3.89001342e+02      # meL(Q)
    32     3.88997702e+02      # mmuL(Q)
    33     3.87898984e+02      # mtauL(Q)
    34     2.44093298e+02      # meR(Q)
    35     2.44081499e+02      # mmuR(Q)
    36     2.40498035e+02      # mtauR(Q)
    41     1.11162929e+03      # mqL1(Q)
    42     1.11162644e+03      # mqL2(Q)
    43     1.02481616e+03      # mqL3(Q)
    44     1.06959472e+03      # muR(Q)
    45     1.06959168e+03      # mcR(Q)
    46     8.80885864e+02      # mtR(Q)
    47     1.06448650e+03      # mdR(Q)
    48     1.06448352e+03      # msR(Q)
    49     1.05905811e+03      # mbR(Q)
Block au Q= 9.54039501e+02  
  1  1    -1.24244193e+03      # Au(Q)MSSM DRbar
  2  2    -1.24243637e+03      # Ac(Q)MSSM DRbar
  3  3    -9.59969606e+02      # At(Q)MSSM DRbar
Block ad Q= 9.54039501e+02  
  1  1    -1.51848761e+03      # Ad(Q)MSSM DRbar
  2  2    -1.51848247e+03      # As(Q)MSSM DRbar
  3  3    -1.41932589e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.54039501e+02  
  1  1    -3.27916441e+02      # Ae(Q)MSSM DRbar
  2  2    -3.27910583e+02      # Amu(Q)MSSM DRbar
  3  3    -3.26142352e+02      # Atau(Q)MSSM DRbar
