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
     1    3.60000000e+02   # m0
     2    6.00000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.76138253e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03887357e+01   # MW
        25     1.17909185e+02   # h0
        35     7.01217455e+02   # H0
        36     7.01137541e+02   # A0
        37     7.06054929e+02   # H+
   1000021     1.36306268e+03   # ~g
   1000022     2.50491787e+02   # ~neutralino(1)
   1000023     4.76945509e+02   # ~neutralino(2)
   1000024     4.77027474e+02   # ~chargino(1)
   1000025    -8.08624769e+02   # ~neutralino(3)
   1000035     8.16381463e+02   # ~neutralino(4)
   1000037     8.16810640e+02   # ~chargino(2)
   1000001     1.28922714e+03   # ~d_L
   1000002     1.28690438e+03   # ~u_L
   1000003     1.28919065e+03   # ~s_L
   1000004     1.28686781e+03   # ~c_L
   1000005     1.08360244e+03   # ~b_1
   1000006     9.34100739e+02   # ~t_1
   1000011     5.41148257e+02   # ~e_L
   1000012     5.35055080e+02   # ~nue_L
   1000013     5.41182187e+02   # ~mu_L
   1000014     5.34914673e+02   # ~numu_L
   1000015     2.51524569e+02   # ~stau_1
   1000016     4.86679224e+02   # ~nu_tau_L
   2000001     1.23762680e+03   # ~d_R
   2000002     1.24186868e+03   # ~u_R
   2000003     1.23755425e+03   # ~s_R
   2000004     1.24186409e+03   # ~c_R
   2000005     1.15103057e+03   # ~b_2
   2000006     1.15359877e+03   # ~t_2
   2000011     4.26413481e+02   # ~e_R
   2000013     4.26055533e+02   # ~mu_R
   2000015     5.13635927e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60516242e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97789375e-01   # N_{1,1}
  1  2    -7.78917106e-03   # N_{1,2}
  1  3     6.25083377e-02   # N_{1,3}
  1  4    -2.11754352e-02   # N_{1,4}
  2  1     1.88518943e-02   # N_{2,1}
  2  2     9.84768715e-01   # N_{2,2}
  2  3    -1.47922727e-01   # N_{2,3}
  2  4     8.94094542e-02   # N_{2,4}
  3  1    -2.87921056e-02   # N_{3,1}
  3  2     4.21312630e-02   # N_{3,2}
  3  3     7.04606394e-01   # N_{3,3}
  3  4     7.07761118e-01   # N_{3,4}
  4  1    -5.68505343e-02   # N_{4,1}
  4  2     1.68507754e-01   # N_{4,2}
  4  3     6.91188400e-01   # N_{4,3}
  4  4    -7.00451104e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.78029661e-01   # U_{1,1}
  1  2    -2.08465782e-01   # U_{1,2}
  2  1     2.08465782e-01   # U_{2,1}
  2  2     9.78029661e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91755783e-01   # V_{1,1}
  1  2    -1.28142373e-01   # V_{1,2}
  2  1     1.28142373e-01   # V_{2,1}
  2  2     9.91755783e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.35424359e-01   # F_{11}
  1  2     9.00225321e-01   # F_{12}
  2  1     9.00225321e-01   # F_{21}
  2  2    -4.35424359e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.09730935e-01   # F_{11}
  1  2     5.86801340e-01   # F_{12}
  2  1    -5.86801340e-01   # F_{21}
  2  2     8.09730935e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.19157332e-01   # F_{11}
  1  2     9.47701745e-01   # F_{12}
  2  1     9.47701745e-01   # F_{21}
  2  2    -3.19157332e-01   # F_{22}
Block gauge Q= 1.00889398e+03  # SM gauge couplings
     1     3.62517065e-01   # g'(Q)MSSM DRbar
     2     6.41498352e-01   # g(Q)MSSM DRbar
     3     1.05239062e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.00889398e+03  
  3  3     8.50557251e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.00889398e+03  
  3  3     4.90259310e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.00889398e+03  
  3  3     4.27702502e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.00889398e+03 # Higgs mixing parameters
     1     8.05551666e+02    # mu(Q)MSSM DRbar
     2     3.91933026e+01    # tan beta(Q)MSSM DRbar
     3     2.43820945e+02    # higgs vev(Q)MSSM DRbar
     4     6.25121975e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.00889398e+03  # MSSM DRbar SUSY breaking parameters
     1     2.54468158e+02      # M_1(Q)
     2     4.70475753e+02      # M_2(Q)
     3     1.32360209e+03      # M_3(Q)
    21    -1.47087245e+05      # mH1^2(Q)
    22    -6.37512190e+05      # mH2^2(Q)
    31     5.34814258e+02      # meL(Q)
    32     5.34673281e+02      # mmuL(Q)
    33     4.89455829e+02      # mtauL(Q)
    34     4.21534172e+02      # meR(Q)
    35     4.21172072e+02      # mmuR(Q)
    36     2.88562858e+02      # mtauR(Q)
    41     1.24858150e+03      # mqL1(Q)
    42     1.24854429e+03      # mqL2(Q)
    43     1.07784707e+03      # mqL3(Q)
    44     1.20436765e+03      # muR(Q)
    45     1.20436298e+03      # mcR(Q)
    46     9.40035294e+02      # mtR(Q)
    47     1.19902495e+03      # mdR(Q)
    48     1.19895120e+03      # msR(Q)
    49     1.09401322e+03      # mbR(Q)
Block au Q= 1.00889398e+03  
  1  1    -1.68706685e+03      # Au(Q)MSSM DRbar
  2  2    -1.68702673e+03      # Ac(Q)MSSM DRbar
  3  3    -1.17944591e+03      # At(Q)MSSM DRbar
Block ad Q= 1.00889398e+03  
  1  1    -1.95303366e+03      # Ad(Q)MSSM DRbar
  2  2    -1.95293150e+03      # As(Q)MSSM DRbar
  3  3    -1.64820907e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.00889398e+03  
  1  1    -6.66219635e+02      # Ae(Q)MSSM DRbar
  2  2    -6.65892904e+02      # Amu(Q)MSSM DRbar
  3  3    -5.56418063e+02      # Atau(Q)MSSM DRbar
