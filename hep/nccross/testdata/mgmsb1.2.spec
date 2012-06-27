# SOFTSUSY3.3.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.1       # version number
Block MODSEL  # Select model
     1    2   # gmsb
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.50000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    4.00000000e+04   # lambda
     2    8.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=8.00000000e+04 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04057056e+01   # MW
        25     1.11157102e+02   # h0
        35     3.86008956e+02   # H0
        36     3.85659417e+02   # A0
        37     3.94214201e+02   # H+
   1000021     9.45962522e+02   # ~g
   1000022     1.62901752e+02   # ~neutralino(1)
   1000023     2.68744274e+02   # ~neutralino(2)
   1000024     2.65895170e+02   # ~chargino(1)
   1000025    -3.15507052e+02   # ~neutralino(3)
   1000035     3.86476803e+02   # ~neutralino(4)
   1000037     3.84736137e+02   # ~chargino(2)
   1000039     7.58400000e-10   # ~gravitino
   1000001     9.02046146e+02   # ~d_L
   1000002     8.98669832e+02   # ~u_L
   1000003     9.02045010e+02   # ~s_L
   1000004     8.98668691e+02   # ~c_L
   1000005     8.58305616e+02   # ~b_1
   1000006     8.05238517e+02   # ~t_1
   1000011     2.62646524e+02   # ~e_L
   1000012     2.50059730e+02   # ~nue_L
   1000013     2.62685869e+02   # ~mu_L
   1000014     2.50058636e+02   # ~numu_L
   1000015     1.24151753e+02   # ~stau_1
   1000016     2.49559462e+02   # ~nu_tau_L
   2000001     8.66763374e+02   # ~d_R
   2000002     8.68146046e+02   # ~u_R
   2000003     8.66761786e+02   # ~s_R
   2000004     8.68145238e+02   # ~c_R
   2000005     8.73457441e+02   # ~b_2
   2000006     8.90069895e+02   # ~t_2
   2000011     1.30907691e+02   # ~e_R
   2000013     1.30903439e+02   # ~mu_R
   2000015     2.64576650e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.89238177e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.64849949e-01   # N_{1,1}
  1  2    -6.51727042e-02   # N_{1,2}
  1  3     2.20679468e-01   # N_{1,3}
  1  4    -1.26955374e-01   # N_{1,4}
  2  1    -2.33235773e-01   # N_{2,1}
  2  2    -6.35479777e-01   # N_{2,2}
  2  3     5.51910574e-01   # N_{2,3}
  2  4    -4.86992038e-01   # N_{2,4}
  3  1    -6.00529625e-02   # N_{3,1}
  3  2     8.12362453e-02   # N_{3,2}
  3  3     6.95698785e-01   # N_{3,3}
  3  4     7.11194428e-01   # N_{3,4}
  4  1    -1.05163168e-01   # N_{4,1}
  4  2     7.65061203e-01   # N_{4,2}
  4  3     4.03359010e-01   # N_{4,3}
  4  4    -4.90839661e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.70000629e-01   # U_{1,1}
  1  2     8.21644256e-01   # U_{1,2}
  2  1    -8.21644256e-01   # U_{2,1}
  2  2    -5.70000629e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.90873054e-01   # V_{1,1}
  1  2     7.22976087e-01   # V_{1,2}
  2  1    -7.22976087e-01   # V_{2,1}
  2  2    -6.90873054e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.62137828e-01   # F_{11}
  1  2     9.32124559e-01   # F_{12}
  2  1     9.32124559e-01   # F_{21}
  2  2    -3.62137828e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.67115609e-01   # F_{11}
  1  2     8.23638201e-01   # F_{12}
  2  1     8.23638201e-01   # F_{21}
  2  2    -5.67115609e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.52501350e-01   # F_{11}
  1  2     9.88303262e-01   # F_{12}
  2  1     9.88303262e-01   # F_{21}
  2  2    -1.52501350e-01   # F_{22}
Block gauge Q= 8.20582997e+02  # SM gauge couplings
     1     3.62661640e-01   # g'(Q)MSSM DRbar
     2     6.45025696e-01   # g(Q)MSSM DRbar
     3     1.06791209e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.20582997e+02  
  3  3     8.68561017e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.20582997e+02  
  3  3     2.06161360e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.20582997e+02  
  3  3     1.52071026e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.20582997e+02 # Higgs mixing parameters
     1     3.06454351e+02    # mu(Q)MSSM DRbar
     2     1.45355705e+01    # tan beta(Q)MSSM DRbar
     3     2.43932095e+02    # higgs vev(Q)MSSM DRbar
     4     1.70052684e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.20582997e+02  # MSSM DRbar SUSY breaking parameters
     1     1.73046710e+02      # M_1(Q)
     2     3.27231065e+02      # M_2(Q)
     3     9.01438959e+02      # M_3(Q)
    21     5.57286099e+04      # mH1^2(Q)
    22    -8.42647857e+04      # mH2^2(Q)
    31     2.53782896e+02      # meL(Q)
    32     2.53781819e+02      # mmuL(Q)
    33     2.53451220e+02      # mtauL(Q)
    34     1.18734862e+02      # meR(Q)
    35     1.18730183e+02      # mmuR(Q)
    36     1.17286038e+02      # mtauR(Q)
    41     8.66830157e+02      # mqL1(Q)
    42     8.66828986e+02      # mqL2(Q)
    43     8.39044534e+02      # mqL3(Q)
    44     8.36112139e+02      # muR(Q)
    45     8.36111312e+02      # mcR(Q)
    46     7.79722172e+02      # mtR(Q)
    47     8.33361831e+02      # mdR(Q)
    48     8.33360202e+02      # msR(Q)
    49     8.30181468e+02      # mbR(Q)
Block au Q= 8.20582997e+02  
  1  1    -2.73807709e+02      # Au(Q)MSSM DRbar
  2  2    -2.73807321e+02      # Ac(Q)MSSM DRbar
  3  3    -2.57999470e+02      # At(Q)MSSM DRbar
Block ad Q= 8.20582997e+02  
  1  1    -2.91459232e+02      # Ad(Q)MSSM DRbar
  2  2    -2.91458689e+02      # As(Q)MSSM DRbar
  3  3    -2.85497744e+02      # Ab(Q)MSSM DRbar
Block ae Q= 8.20582997e+02  
  1  1    -2.73061445e+01      # Ae(Q)MSSM DRbar
  2  2    -2.73059452e+01      # Amu(Q)MSSM DRbar
  3  3    -2.72448047e+01      # Atau(Q)MSSM DRbar
