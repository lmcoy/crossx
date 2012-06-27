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
     1    2.50000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.79618233e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03902885e+01   # MW
        25     1.16113400e+02   # h0
        35     8.71386292e+02   # H0
        36     8.71136104e+02   # A0
        37     8.75079286e+02   # H+
   1000021     1.35972600e+03   # ~g
   1000022     2.48080776e+02   # ~neutralino(1)
   1000023     4.69479346e+02   # ~neutralino(2)
   1000024     4.69658426e+02   # ~chargino(1)
   1000025    -7.45916322e+02   # ~neutralino(3)
   1000035     7.58344393e+02   # ~neutralino(4)
   1000037     7.57967579e+02   # ~chargino(2)
   1000001     1.26245100e+03   # ~d_L
   1000002     1.26012137e+03   # ~u_L
   1000003     1.26244788e+03   # ~s_L
   1000004     1.26011824e+03   # ~c_L
   1000005     1.15387686e+03   # ~b_1
   1000006     9.66440423e+02   # ~t_1
   1000011     4.75471492e+02   # ~e_L
   1000012     4.68696644e+02   # ~nue_L
   1000013     4.75588550e+02   # ~mu_L
   1000014     4.68691905e+02   # ~numu_L
   1000015     3.32179237e+02   # ~stau_1
   1000016     4.67089194e+02   # ~nu_tau_L
   2000001     1.20956593e+03   # ~d_R
   2000002     1.21393599e+03   # ~u_R
   2000003     1.20956269e+03   # ~s_R
   2000004     1.21393264e+03   # ~c_R
   2000005     1.20473077e+03   # ~b_2
   2000006     1.19236878e+03   # ~t_2
   2000011     3.38929668e+02   # ~e_R
   2000013     3.38916358e+02   # ~mu_R
   2000015     4.75573497e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05842117e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96960820e-01   # N_{1,1}
  1  2    -1.26725847e-02   # N_{1,2}
  1  3     7.07346384e-02   # N_{1,3}
  1  4    -3.00855553e-02   # N_{1,4}
  2  1     2.86983603e-02   # N_{2,1}
  2  2     9.76071762e-01   # N_{2,2}
  2  3    -1.77771618e-01   # N_{2,3}
  2  4     1.21891640e-01   # N_{2,4}
  3  1    -2.81011970e-02   # N_{3,1}
  3  2     4.07220302e-02   # N_{3,2}
  3  3     7.04491872e-01   # N_{3,3}
  3  4     7.07985339e-01   # N_{3,4}
  4  1    -6.67521606e-02   # N_{4,1}
  4  2     2.13225322e-01   # N_{4,2}
  4  3     6.83436219e-01   # N_{4,3}
  4  4    -6.94977731e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.67973882e-01   # U_{1,1}
  1  2    -2.51050918e-01   # U_{1,2}
  2  1     2.51050918e-01   # U_{2,1}
  2  2     9.67973882e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.84758733e-01   # V_{1,1}
  1  2    -1.73925957e-01   # V_{1,2}
  2  1     1.73925957e-01   # V_{2,1}
  2  2     9.84758733e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.76400203e-01   # F_{11}
  1  2     9.26457169e-01   # F_{12}
  2  1     9.26457169e-01   # F_{21}
  2  2    -3.76400203e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.84694854e-01   # F_{11}
  1  2     1.74287248e-01   # F_{12}
  2  1    -1.74287248e-01   # F_{21}
  2  2     9.84694854e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.17705655e-01   # F_{11}
  1  2     9.93048528e-01   # F_{12}
  2  1     9.93048528e-01   # F_{21}
  2  2    -1.17705655e-01   # F_{22}
Block gauge Q= 1.04170408e+03  # SM gauge couplings
     1     3.62709542e-01   # g'(Q)MSSM DRbar
     2     6.41982438e-01   # g(Q)MSSM DRbar
     3     1.05178750e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.04170408e+03  
  3  3     8.55346619e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.04170408e+03  
  3  3     1.34155902e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.04170408e+03  
  3  3     1.00387910e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.04170408e+03 # Higgs mixing parameters
     1     7.40401460e+02    # mu(Q)MSSM DRbar
     2     9.65263893e+00    # tan beta(Q)MSSM DRbar
     3     2.43891067e+02    # higgs vev(Q)MSSM DRbar
     4     7.85636702e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.04170408e+03  # MSSM DRbar SUSY breaking parameters
     1     2.53147122e+02      # M_1(Q)
     2     4.67930669e+02      # M_2(Q)
     3     1.31903023e+03      # M_3(Q)
    21     1.95227843e+05      # mH1^2(Q)
    22    -5.27521143e+05      # mH2^2(Q)
    31     4.68079084e+02      # meL(Q)
    32     4.68074327e+02      # mmuL(Q)
    33     4.66636491e+02      # mtauL(Q)
    34     3.32682619e+02      # meR(Q)
    35     3.32669048e+02      # mmuR(Q)
    36     3.28547464e+02      # mtauR(Q)
    41     1.21966410e+03      # mqL1(Q)
    42     1.21966092e+03      # mqL2(Q)
    43     1.12151229e+03      # mqL3(Q)
    44     1.17433794e+03      # muR(Q)
    45     1.17433454e+03      # mcR(Q)
    46     9.60799833e+02      # mtR(Q)
    47     1.16881316e+03      # mdR(Q)
    48     1.16880985e+03      # msR(Q)
    49     1.16277590e+03      # mbR(Q)
Block au Q= 1.04170408e+03  
  1  1    -1.34272959e+03      # Au(Q)MSSM DRbar
  2  2    -1.34272361e+03      # Ac(Q)MSSM DRbar
  3  3    -1.03875946e+03      # At(Q)MSSM DRbar
Block ad Q= 1.04170408e+03  
  1  1    -1.63947108e+03      # Ad(Q)MSSM DRbar
  2  2    -1.63946554e+03      # As(Q)MSSM DRbar
  3  3    -1.53277306e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.04170408e+03  
  1  1    -3.56333925e+02      # Ae(Q)MSSM DRbar
  2  2    -3.56327591e+02      # Amu(Q)MSSM DRbar
  3  3    -3.54414206e+02      # Atau(Q)MSSM DRbar
