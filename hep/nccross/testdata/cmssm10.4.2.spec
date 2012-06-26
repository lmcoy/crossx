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
     1    8.50000000e+02   # m0
     2    4.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.21145582e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03943433e+01   # MW
        25     1.14020950e+02   # h0
        35     1.01410003e+03   # H0
        36     1.01405152e+03   # A0
        37     1.01731252e+03   # H+
   1000021     9.75874972e+02   # ~g
   1000022     1.63828712e+02   # ~neutralino(1)
   1000023     3.09433957e+02   # ~neutralino(2)
   1000024     3.09518296e+02   # ~chargino(1)
   1000025    -5.25040567e+02   # ~neutralino(3)
   1000035     5.41252438e+02   # ~neutralino(4)
   1000037     5.40704658e+02   # ~chargino(2)
   1000001     1.18779283e+03   # ~d_L
   1000002     1.18533508e+03   # ~u_L
   1000003     1.18778869e+03   # ~s_L
   1000004     1.18533093e+03   # ~c_L
   1000005     1.03083514e+03   # ~b_1
   1000006     8.22278370e+02   # ~t_1
   1000011     8.88825465e+02   # ~e_L
   1000012     8.85007447e+02   # ~nue_L
   1000013     8.88851772e+02   # ~mu_L
   1000014     8.84995256e+02   # ~numu_L
   1000015     8.54332992e+02   # ~stau_1
   1000016     8.81268410e+02   # ~nu_tau_L
   2000001     1.16514905e+03   # ~d_R
   2000002     1.16639452e+03   # ~u_R
   2000003     1.16514502e+03   # ~s_R
   2000004     1.16639006e+03   # ~c_R
   2000005     1.15732701e+03   # ~b_2
   2000006     1.05756055e+03   # ~t_2
   2000011     8.63017390e+02   # ~e_R
   2000013     8.62992276e+02   # ~mu_R
   2000015     8.86043029e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05046982e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.93667889e-01   # N_{1,1}
  1  2    -2.54317990e-02   # N_{1,2}
  1  3     1.01400923e-01   # N_{1,3}
  1  4    -4.11728388e-02   # N_{1,4}
  2  1     5.41290987e-02   # N_{2,1}
  2  2     9.60398657e-01   # N_{2,2}
  2  3    -2.28934456e-01   # N_{2,3}
  2  4     1.49309999e-01   # N_{2,4}
  3  1    -4.07197781e-02   # N_{3,1}
  3  2     5.93724354e-02   # N_{3,2}
  3  3     7.01722680e-01   # N_{3,3}
  3  4     7.08803283e-01   # N_{3,4}
  4  1    -8.96441103e-02   # N_{4,1}
  4  2     2.71039772e-01   # N_{4,2}
  4  3     6.67002360e-01   # N_{4,3}
  4  4    -6.88192726e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.45458765e-01   # U_{1,1}
  1  2    -3.25741806e-01   # U_{1,2}
  2  1     3.25741806e-01   # U_{2,1}
  2  2     9.45458765e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.76588311e-01   # V_{1,1}
  1  2    -2.15116877e-01   # V_{1,2}
  2  1     2.15116877e-01   # V_{2,1}
  2  2     9.76588311e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.79615088e-01   # F_{11}
  1  2     9.60112182e-01   # F_{12}
  2  1     9.60112182e-01   # F_{21}
  2  2    -2.79615088e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98599610e-01   # F_{11}
  1  2     5.29038734e-02   # F_{12}
  2  1    -5.29038734e-02   # F_{21}
  2  2     9.98599610e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.74488897e-01   # F_{11}
  1  2     9.84659141e-01   # F_{12}
  2  1     9.84659141e-01   # F_{21}
  2  2    -1.74488897e-01   # F_{22}
Block gauge Q= 9.06849845e+02  # SM gauge couplings
     1     3.62005529e-01   # g'(Q)MSSM DRbar
     2     6.42820628e-01   # g(Q)MSSM DRbar
     3     1.06242128e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.06849845e+02  
  3  3     8.64699736e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.06849845e+02  
  3  3     1.36720679e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.06849845e+02  
  3  3     9.96815947e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.06849845e+02 # Higgs mixing parameters
     1     5.17566414e+02    # mu(Q)MSSM DRbar
     2     9.66566894e+00    # tan beta(Q)MSSM DRbar
     3     2.43879181e+02    # higgs vev(Q)MSSM DRbar
     4     1.05003496e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.06849845e+02  # MSSM DRbar SUSY breaking parameters
     1     1.66961069e+02      # M_1(Q)
     2     3.10461335e+02      # M_2(Q)
     3     8.94256388e+02      # M_3(Q)
    21     7.50489670e+05      # mH1^2(Q)
    22    -2.46521531e+05      # mH2^2(Q)
    31     8.86105644e+02      # meL(Q)
    32     8.86093491e+02      # mmuL(Q)
    33     8.82482674e+02      # mtauL(Q)
    34     8.60818921e+02      # meR(Q)
    35     8.60793778e+02      # mmuR(Q)
    36     8.53305425e+02      # mtauR(Q)
    41     1.16038773e+03      # mqL1(Q)
    42     1.16038347e+03      # mqL2(Q)
    43     1.00689963e+03      # mqL3(Q)
    44     1.14183073e+03      # muR(Q)
    45     1.14182614e+03      # mcR(Q)
    46     8.03817788e+02      # mtR(Q)
    47     1.13968153e+03      # mdR(Q)
    48     1.13967737e+03      # msR(Q)
    49     1.13168085e+03      # mbR(Q)
Block au Q= 9.06849845e+02  
  1  1    -9.16620804e+02      # Au(Q)MSSM DRbar
  2  2    -9.16616691e+02      # Ac(Q)MSSM DRbar
  3  3    -7.05033396e+02      # At(Q)MSSM DRbar
Block ad Q= 9.06849845e+02  
  1  1    -1.12374558e+03      # Ad(Q)MSSM DRbar
  2  2    -1.12374177e+03      # As(Q)MSSM DRbar
  3  3    -1.04940057e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.06849845e+02  
  1  1    -2.40150427e+02      # Ae(Q)MSSM DRbar
  2  2    -2.40146095e+02      # Amu(Q)MSSM DRbar
  3  3    -2.38861524e+02      # Atau(Q)MSSM DRbar
