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
     1    1.15000000e+03   # m0
     2    5.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.99385539e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03908527e+01   # MW
        25     1.16164347e+02   # h0
        35     1.36272440e+03   # H0
        36     1.36266519e+03   # A0
        37     1.36516373e+03   # H+
   1000021     1.30875173e+03   # ~g
   1000022     2.29774801e+02   # ~neutralino(1)
   1000023     4.35620590e+02   # ~neutralino(2)
   1000024     4.35817746e+02   # ~chargino(1)
   1000025    -6.83636682e+02   # ~neutralino(3)
   1000035     6.97999785e+02   # ~neutralino(4)
   1000037     6.97407673e+02   # ~chargino(2)
   1000001     1.59829758e+03   # ~d_L
   1000002     1.59651811e+03   # ~u_L
   1000003     1.59829205e+03   # ~s_L
   1000004     1.59651257e+03   # ~c_L
   1000005     1.38892516e+03   # ~b_1
   1000006     1.11319093e+03   # ~t_1
   1000011     1.20325396e+03   # ~e_L
   1000012     1.20036441e+03   # ~nue_L
   1000013     1.20330131e+03   # ~mu_L
   1000014     1.20034819e+03   # ~numu_L
   1000015     1.15652346e+03   # ~stau_1
   1000016     1.19537043e+03   # ~nu_tau_L
   2000001     1.56702280e+03   # ~d_R
   2000002     1.56935595e+03   # ~u_R
   2000003     1.56701744e+03   # ~s_R
   2000004     1.56934997e+03   # ~c_R
   2000005     1.55646752e+03   # ~b_2
   2000006     1.40833865e+03   # ~t_2
   2000011     1.16751031e+03   # ~e_R
   2000013     1.16747681e+03   # ~mu_R
   2000015     1.19891533e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04580814e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96290934e-01   # N_{1,1}
  1  2    -1.48654086e-02   # N_{1,2}
  1  3     7.79209426e-02   # N_{1,3}
  1  4    -3.33424811e-02   # N_{1,4}
  2  1     3.43671191e-02   # N_{2,1}
  2  2     9.70515622e-01   # N_{2,2}
  2  3    -1.96156951e-01   # N_{2,3}
  2  4     1.35796832e-01   # N_{2,4}
  3  1    -3.07059745e-02   # N_{3,1}
  3  2     4.43092056e-02   # N_{3,2}
  3  3     7.04053355e-01   # N_{3,3}
  3  4     7.08097953e-01   # N_{3,4}
  4  1    -7.26664914e-02   # N_{4,1}
  4  2     2.36463828e-01   # N_{4,2}
  4  3     6.78055787e-01   # N_{4,3}
  4  4    -6.92130615e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.60654509e-01   # U_{1,1}
  1  2    -2.77746133e-01   # U_{1,2}
  2  1     2.77746133e-01   # U_{2,1}
  2  2     9.60654509e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.80923868e-01   # V_{1,1}
  1  2    -1.94392299e-01   # V_{1,2}
  2  1     1.94392299e-01   # V_{2,1}
  2  2     9.80923868e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.15108266e-01   # F_{11}
  1  2     9.76590208e-01   # F_{12}
  2  1     9.76590208e-01   # F_{21}
  2  2    -2.15108266e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.99268209e-01   # F_{11}
  1  2     3.82497887e-02   # F_{12}
  2  1    -3.82497887e-02   # F_{21}
  2  2     9.99268209e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.24887427e-01   # F_{11}
  1  2     9.92170918e-01   # F_{12}
  2  1     9.92170918e-01   # F_{21}
  2  2    -1.24887427e-01   # F_{22}
Block gauge Q= 1.21973816e+03  # SM gauge couplings
     1     3.62637387e-01   # g'(Q)MSSM DRbar
     2     6.41265452e-01   # g(Q)MSSM DRbar
     3     1.04699770e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.21973816e+03  
  3  3     8.54619417e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.21973816e+03  
  3  3     1.34621124e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.21973816e+03  
  3  3     9.94656164e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.21973816e+03 # Higgs mixing parameters
     1     6.75833672e+02    # mu(Q)MSSM DRbar
     2     9.63055569e+00    # tan beta(Q)MSSM DRbar
     3     2.43506913e+02    # higgs vev(Q)MSSM DRbar
     4     1.89532704e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.21973816e+03  # MSSM DRbar SUSY breaking parameters
     1     2.32807803e+02      # M_1(Q)
     2     4.29633191e+02      # M_2(Q)
     3     1.20230851e+03      # M_3(Q)
    21     1.37826985e+06      # mH1^2(Q)
    22    -4.13154076e+05      # mH2^2(Q)
    31     1.20004586e+03      # meL(Q)
    32     1.20002967e+03      # mmuL(Q)
    33     1.19520402e+03      # mtauL(Q)
    34     1.16516228e+03      # meR(Q)
    35     1.16512877e+03      # mmuR(Q)
    36     1.15511593e+03      # mtauR(Q)
    41     1.56297641e+03      # mqL1(Q)
    42     1.56297074e+03      # mqL2(Q)
    43     1.35818583e+03      # mqL3(Q)
    44     1.53698616e+03      # muR(Q)
    45     1.53698002e+03      # mcR(Q)
    46     1.08602901e+03      # mtR(Q)
    47     1.53392705e+03      # mdR(Q)
    48     1.53392153e+03      # msR(Q)
    49     1.52335648e+03      # mbR(Q)
Block au Q= 1.21973816e+03  
  1  1    -1.21874605e+03      # Au(Q)MSSM DRbar
  2  2    -1.21874066e+03      # Ac(Q)MSSM DRbar
  3  3    -9.42057796e+02      # At(Q)MSSM DRbar
Block ad Q= 1.21973816e+03  
  1  1    -1.48861300e+03      # Ad(Q)MSSM DRbar
  2  2    -1.48860802e+03      # As(Q)MSSM DRbar
  3  3    -1.39144241e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.21973816e+03  
  1  1    -3.25523013e+02      # Ae(Q)MSSM DRbar
  2  2    -3.25517253e+02      # Amu(Q)MSSM DRbar
  3  3    -3.23803530e+02      # Atau(Q)MSSM DRbar
