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
     1    6.00000000e+02   # m0
     2    5.50000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.88615812e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03892496e+01   # MW
        25     1.17593219e+02   # h0
        35     7.29957074e+02   # H0
        36     7.29902751e+02   # A0
        37     7.34675008e+02   # H+
   1000021     1.27421942e+03   # ~g
   1000022     2.29842167e+02   # ~neutralino(1)
   1000023     4.38019150e+02   # ~neutralino(2)
   1000024     4.38095491e+02   # ~chargino(1)
   1000025    -7.50568174e+02   # ~neutralino(3)
   1000035     7.58896173e+02   # ~neutralino(4)
   1000037     7.59352502e+02   # ~chargino(2)
   1000001     1.28681129e+03   # ~d_L
   1000002     1.28451699e+03   # ~u_L
   1000003     1.28677295e+03   # ~s_L
   1000004     1.28447856e+03   # ~c_L
   1000005     1.06728062e+03   # ~b_1
   1000006     9.07729531e+02   # ~t_1
   1000011     7.03579921e+02   # ~e_L
   1000012     6.98785876e+02   # ~nue_L
   1000013     7.03507911e+02   # ~mu_L
   1000014     6.98606494e+02   # ~numu_L
   1000015     4.72329376e+02   # ~stau_1
   1000016     6.37450946e+02   # ~nu_tau_L
   2000001     1.24462293e+03   # ~d_R
   2000002     1.24793572e+03   # ~u_R
   2000003     1.24454716e+03   # ~s_R
   2000004     1.24793082e+03   # ~c_R
   2000005     1.14106961e+03   # ~b_2
   2000006     1.12643756e+03   # ~t_2
   2000011     6.35100279e+02   # ~e_R
   2000013     6.34701545e+02   # ~mu_R
   2000015     6.55496441e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59929496e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97437081e-01   # N_{1,1}
  1  2    -8.97942111e-03   # N_{1,2}
  1  3     6.73138141e-02   # N_{1,3}
  1  4    -2.25275499e-02   # N_{1,4}
  2  1     2.15747692e-02   # N_{2,1}
  2  2     9.82861677e-01   # N_{2,2}
  2  3    -1.57141518e-01   # N_{2,3}
  2  4     9.39361339e-02   # N_{2,4}
  3  1    -3.11263462e-02   # N_{3,1}
  3  2     4.56195897e-02   # N_{3,2}
  3  3     7.04199549e-01   # N_{3,3}
  3  4     7.07850972e-01   # N_{3,4}
  4  1    -6.07037889e-02   # N_{4,1}
  4  2     1.78384831e-01   # N_{4,2}
  4  3     6.89114206e-01   # N_{4,3}
  4  4    -6.99725313e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.75131552e-01   # U_{1,1}
  1  2    -2.21626840e-01   # U_{1,2}
  2  1     2.21626840e-01   # U_{2,1}
  2  2     9.75131552e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.90871574e-01   # V_{1,1}
  1  2    -1.34809211e-01   # V_{1,2}
  2  1     1.34809211e-01   # V_{2,1}
  2  2     9.90871574e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.16064472e-01   # F_{11}
  1  2     9.09335117e-01   # F_{12}
  2  1     9.09335117e-01   # F_{21}
  2  2    -4.16064472e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.87091006e-01   # F_{11}
  1  2     4.61594569e-01   # F_{12}
  2  1    -4.61594569e-01   # F_{21}
  2  2     8.87091006e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.82685063e-01   # F_{11}
  1  2     9.59212779e-01   # F_{12}
  2  1     9.59212779e-01   # F_{21}
  2  2    -2.82685063e-01   # F_{22}
Block gauge Q= 9.81994335e+02  # SM gauge couplings
     1     3.62275814e-01   # g'(Q)MSSM DRbar
     2     6.41577431e-01   # g(Q)MSSM DRbar
     3     1.05451209e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.81994335e+02  
  3  3     8.52279260e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.81994335e+02  
  3  3     4.95308686e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.81994335e+02  
  3  3     4.24533834e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.81994335e+02 # Higgs mixing parameters
     1     7.46384976e+02    # mu(Q)MSSM DRbar
     2     3.92050292e+01    # tan beta(Q)MSSM DRbar
     3     2.43878183e+02    # higgs vev(Q)MSSM DRbar
     4     6.82156889e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.81994335e+02  # MSSM DRbar SUSY breaking parameters
     1     2.32720146e+02      # M_1(Q)
     2     4.30924445e+02      # M_2(Q)
     3     1.21817794e+03      # M_3(Q)
    21    -1.32421618e+04      # mH1^2(Q)
    22    -5.46536881e+05      # mH2^2(Q)
    31     6.99419214e+02      # meL(Q)
    32     6.99239855e+02      # mmuL(Q)
    33     6.40419277e+02      # mtauL(Q)
    34     6.32007184e+02      # meR(Q)
    35     6.31606891e+02      # mmuR(Q)
    36     4.89455241e+02      # mtauR(Q)
    41     1.24910267e+03      # mqL1(Q)
    42     1.24906303e+03      # mqL2(Q)
    43     1.05430879e+03      # mqL3(Q)
    44     1.21280813e+03      # muR(Q)
    45     1.21280310e+03      # mcR(Q)
    46     9.08907580e+02      # mtR(Q)
    47     1.20847851e+03      # mdR(Q)
    48     1.20840067e+03      # msR(Q)
    49     1.09291033e+03      # mbR(Q)
Block au Q= 9.81994335e+02  
  1  1    -1.58112168e+03      # Au(Q)MSSM DRbar
  2  2    -1.58108357e+03      # Ac(Q)MSSM DRbar
  3  3    -1.09686164e+03      # At(Q)MSSM DRbar
Block ad Q= 9.81994335e+02  
  1  1    -1.83184160e+03      # Ad(Q)MSSM DRbar
  2  2    -1.83174453e+03      # As(Q)MSSM DRbar
  3  3    -1.53910509e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.81994335e+02  
  1  1    -6.43383751e+02      # Ae(Q)MSSM DRbar
  2  2    -6.43063796e+02      # Amu(Q)MSSM DRbar
  3  3    -5.37489902e+02      # Atau(Q)MSSM DRbar
