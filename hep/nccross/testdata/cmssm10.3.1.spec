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
     1    3.00000000e+02   # m0
     2    4.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.02229289e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03935532e+01   # MW
        25     1.14248725e+02   # h0
        35     7.06900910e+02   # H0
        36     7.06572504e+02   # A0
        37     7.11461618e+02   # H+
   1000021     1.04791644e+03   # ~g
   1000022     1.83354255e+02   # ~neutralino(1)
   1000023     3.46108590e+02   # ~neutralino(2)
   1000024     3.46206895e+02   # ~chargino(1)
   1000025    -5.79746841e+02   # ~neutralino(3)
   1000035     5.94272472e+02   # ~neutralino(4)
   1000037     5.93887402e+02   # ~chargino(2)
   1000001     9.96942141e+02   # ~d_L
   1000002     9.93947067e+02   # ~u_L
   1000003     9.96939545e+02   # ~s_L
   1000004     9.93944462e+02   # ~c_L
   1000005     9.05265925e+02   # ~b_1
   1000006     7.47293073e+02   # ~t_1
   1000011     4.27897508e+02   # ~e_L
   1000012     4.20343570e+02   # ~nue_L
   1000013     4.27990437e+02   # ~mu_L
   1000014     4.20338699e+02   # ~numu_L
   1000015     3.40317146e+02   # ~stau_1
   1000016     4.18769619e+02   # ~nu_tau_L
   2000001     9.58962209e+02   # ~d_R
   2000002     9.61586813e+02   # ~u_R
   2000003     9.58959519e+02   # ~s_R
   2000004     9.61584033e+02   # ~c_R
   2000005     9.55208418e+02   # ~b_2
   2000006     9.50008196e+02   # ~t_2
   2000011     3.46579401e+02   # ~e_R
   2000013     3.46567422e+02   # ~mu_R
   2000015     4.28312428e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06818961e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.94902588e-01   # N_{1,1}
  1  2    -2.10568617e-02   # N_{1,2}
  1  3     9.12316777e-02   # N_{1,3}
  1  4    -3.74463710e-02   # N_{1,4}
  2  1     4.51186549e-02   # N_{2,1}
  2  2     9.66266918e-01   # N_{2,2}
  2  3    -2.11773696e-01   # N_{2,3}
  2  4     1.39443367e-01   # N_{2,4}
  3  1    -3.66332205e-02   # N_{3,1}
  3  2     5.34574983e-02   # N_{3,2}
  3  3     7.02664665e-01   # N_{3,3}
  3  4     7.08563809e-01   # N_{3,4}
  4  1    -8.24084661e-02   # N_{4,1}
  4  2     2.51052083e-01   # N_{4,2}
  4  3     6.73120383e-01   # N_{4,3}
  4  4    -6.90717486e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.53756267e-01   # U_{1,1}
  1  2    -3.00581075e-01   # U_{1,2}
  2  1     3.00581075e-01   # U_{2,1}
  2  2     9.53756267e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.79737116e-01   # V_{1,1}
  1  2    -2.00287752e-01   # V_{1,2}
  2  1     2.00287752e-01   # V_{2,1}
  2  2     9.79737116e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.24953187e-01   # F_{11}
  1  2     9.05215327e-01   # F_{12}
  2  1     9.05215327e-01   # F_{21}
  2  2    -4.24953187e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.84114055e-01   # F_{11}
  1  2     1.77537393e-01   # F_{12}
  2  1    -1.77537393e-01   # F_{21}
  2  2     9.84114055e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.57075612e-01   # F_{11}
  1  2     9.87586580e-01   # F_{12}
  2  1     9.87586580e-01   # F_{21}
  2  2    -1.57075612e-01   # F_{22}
Block gauge Q= 8.16366488e+02  # SM gauge couplings
     1     3.62093501e-01   # g'(Q)MSSM DRbar
     2     6.43252491e-01   # g(Q)MSSM DRbar
     3     1.06501401e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.16366488e+02  
  3  3     8.64205379e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.16366488e+02  
  3  3     1.36015573e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.16366488e+02  
  3  3     1.00477208e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.16366488e+02 # Higgs mixing parameters
     1     5.73900203e+02    # mu(Q)MSSM DRbar
     2     9.68143319e+00    # tan beta(Q)MSSM DRbar
     3     2.44171431e+02    # higgs vev(Q)MSSM DRbar
     4     5.16441857e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.16366488e+02  # MSSM DRbar SUSY breaking parameters
     1     1.87532033e+02      # M_1(Q)
     2     3.48973996e+02      # M_2(Q)
     3     1.00887002e+03      # M_3(Q)
    21     1.62339231e+05      # mH1^2(Q)
    22    -3.18486063e+05      # mH2^2(Q)
    31     4.22495191e+02      # meL(Q)
    32     4.22490328e+02      # mmuL(Q)
    33     4.21026503e+02      # mtauL(Q)
    34     3.42015258e+02      # meR(Q)
    35     3.42003122e+02      # mmuR(Q)
    36     3.38336228e+02      # mtauR(Q)
    41     9.62639443e+02      # mqL1(Q)
    42     9.62636783e+02      # mqL2(Q)
    43     8.79071056e+02      # mqL3(Q)
    44     9.30367346e+02      # muR(Q)
    45     9.30364513e+02      # mcR(Q)
    46     7.48640570e+02      # mtR(Q)
    47     9.26497904e+02      # mdR(Q)
    48     9.26495159e+02      # msR(Q)
    49     9.21435709e+02      # mbR(Q)
Block au Q= 8.16366488e+02  
  1  1    -1.03682976e+03      # Au(Q)MSSM DRbar
  2  2    -1.03682509e+03      # Ac(Q)MSSM DRbar
  3  3    -7.98524533e+02      # At(Q)MSSM DRbar
Block ad Q= 8.16366488e+02  
  1  1    -1.27020673e+03      # Ad(Q)MSSM DRbar
  2  2    -1.27020239e+03      # As(Q)MSSM DRbar
  3  3    -1.18651986e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.16366488e+02  
  1  1    -2.70638357e+02      # Ae(Q)MSSM DRbar
  2  2    -2.70633464e+02      # Amu(Q)MSSM DRbar
  3  3    -2.69162279e+02      # Atau(Q)MSSM DRbar
