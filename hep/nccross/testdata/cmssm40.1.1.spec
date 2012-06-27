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
     1    3.30000000e+02   # m0
     2    5.00000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.87195530e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03901532e+01   # MW
        25     1.16991032e+02   # h0
        35     6.03255547e+02   # H0
        36     6.03205194e+02   # A0
        37     6.08917331e+02   # H+
   1000021     1.15301975e+03   # ~g
   1000022     2.07039796e+02   # ~neutralino(1)
   1000023     3.94700019e+02   # ~neutralino(2)
   1000024     3.94756521e+02   # ~chargino(1)
   1000025    -7.02918827e+02   # ~neutralino(3)
   1000035     7.10965519e+02   # ~neutralino(4)
   1000037     7.11534052e+02   # ~chargino(2)
   1000001     1.09878790e+03   # ~d_L
   1000002     1.09603263e+03   # ~u_L
   1000003     1.09875461e+03   # ~s_L
   1000004     1.09599924e+03   # ~c_L
   1000005     9.12027434e+02   # ~b_1
   1000006     7.76558160e+02   # ~t_1
   1000011     4.72677832e+02   # ~e_L
   1000012     4.65719115e+02   # ~nue_L
   1000013     4.72714584e+02   # ~mu_L
   1000014     4.65581921e+02   # ~numu_L
   1000015     2.08882544e+02   # ~stau_1
   1000016     4.19075114e+02   # ~nu_tau_L
   2000001     1.05637861e+03   # ~d_R
   2000002     1.05951931e+03   # ~u_R
   2000003     1.05631246e+03   # ~s_R
   2000004     1.05951515e+03   # ~c_R
   2000005     9.81453286e+02   # ~b_2
   2000006     9.89122882e+02   # ~t_2
   2000011     3.81821281e+02   # ~e_R
   2000013     3.81481503e+02   # ~mu_R
   2000015     4.49663231e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.61458034e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97115640e-01   # N_{1,1}
  1  2    -1.02800808e-02   # N_{1,2}
  1  3     7.15329049e-02   # N_{1,3}
  1  4    -2.31897321e-02   # N_{1,4}
  2  1     2.39151637e-02   # N_{2,1}
  2  2     9.82071449e-01   # N_{2,2}
  2  3    -1.61892632e-01   # N_{2,3}
  2  4     9.35655360e-02   # N_{2,4}
  3  1    -3.35095276e-02   # N_{3,1}
  3  2     4.93690814e-02   # N_{3,2}
  3  3     7.03707660e-01   # N_{3,3}
  3  4     7.07979756e-01   # N_{3,4}
  4  1    -6.37618751e-02   # N_{4,1}
  4  2     1.81638879e-01   # N_{4,2}
  4  3     6.88091091e-01   # N_{4,3}
  4  4    -6.99623035e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73596197e-01   # U_{1,1}
  1  2    -2.28277122e-01   # U_{1,2}
  2  1     2.28277122e-01   # U_{2,1}
  2  2     9.73596197e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.90940513e-01   # V_{1,1}
  1  2    -1.34301527e-01   # V_{1,2}
  2  1     1.34301527e-01   # V_{2,1}
  2  2     9.90940513e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.73104298e-01   # F_{11}
  1  2     8.81006426e-01   # F_{12}
  2  1     8.81006426e-01   # F_{21}
  2  2    -4.73104298e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.12165461e-01   # F_{11}
  1  2     5.83427171e-01   # F_{12}
  2  1    -5.83427171e-01   # F_{21}
  2  2     8.12165461e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.55481852e-01   # F_{11}
  1  2     9.34683183e-01   # F_{12}
  2  1     9.34683183e-01   # F_{21}
  2  2    -3.55481852e-01   # F_{22}
Block gauge Q= 8.50964967e+02  # SM gauge couplings
     1     3.62132281e-01   # g'(Q)MSSM DRbar
     2     6.42330919e-01   # g(Q)MSSM DRbar
     3     1.06123404e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.50964967e+02  
  3  3     8.56314631e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.50964967e+02  
  3  3     4.91087746e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.50964967e+02  
  3  3     4.27314697e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.50964967e+02 # Higgs mixing parameters
     1     6.99521352e+02    # mu(Q)MSSM DRbar
     2     3.92346811e+01    # tan beta(Q)MSSM DRbar
     3     2.44017040e+02    # higgs vev(Q)MSSM DRbar
     4     4.61505860e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.50964967e+02  # MSSM DRbar SUSY breaking parameters
     1     2.10481864e+02      # M_1(Q)
     2     3.90868426e+02      # M_2(Q)
     3     1.11771484e+03      # M_3(Q)
    21    -1.16779271e+05      # mH1^2(Q)
    22    -4.83189476e+05      # mH2^2(Q)
    31     4.67133721e+02      # meL(Q)
    32     4.66996443e+02      # mmuL(Q)
    33     4.23258376e+02      # mtauL(Q)
    34     3.77269226e+02      # meR(Q)
    35     3.76925408e+02      # mmuR(Q)
    36     2.51010164e+02      # mtauR(Q)
    41     1.06388408e+03      # mqL1(Q)
    42     1.06385008e+03      # mqL2(Q)
    43     9.10630562e+02      # mqL3(Q)
    44     1.02772127e+03      # muR(Q)
    45     1.02771705e+03      # mcR(Q)
    46     7.90835790e+02      # mtR(Q)
    47     1.02339963e+03      # mdR(Q)
    48     1.02333231e+03      # msR(Q)
    49     9.28932882e+02      # mbR(Q)
Block au Q= 8.50964967e+02  
  1  1    -1.48306178e+03      # Au(Q)MSSM DRbar
  2  2    -1.48302531e+03      # Ac(Q)MSSM DRbar
  3  3    -1.02170229e+03      # At(Q)MSSM DRbar
Block ad Q= 8.50964967e+02  
  1  1    -1.72572418e+03      # Ad(Q)MSSM DRbar
  2  2    -1.72563132e+03      # As(Q)MSSM DRbar
  3  3    -1.44980386e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.50964967e+02  
  1  1    -6.25888577e+02      # Ae(Q)MSSM DRbar
  2  2    -6.25574506e+02      # Amu(Q)MSSM DRbar
  3  3    -5.20787887e+02      # Atau(Q)MSSM DRbar
