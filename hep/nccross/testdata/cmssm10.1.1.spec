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
     1    1.25000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.87388442e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03930579e+01   # MW
        25     1.14892204e+02   # h0
        35     7.18140006e+02   # H0
        36     7.17854591e+02   # A0
        37     7.22569411e+02   # H+
   1000021     1.14670940e+03   # ~g
   1000022     2.04183457e+02   # ~neutralino(1)
   1000023     3.85946340e+02   # ~neutralino(2)
   1000024     3.86077415e+02   # ~chargino(1)
   1000025    -6.35540374e+02   # ~neutralino(3)
   1000035     6.49194255e+02   # ~neutralino(4)
   1000037     6.48819376e+02   # ~chargino(2)
   1000001     1.05543979e+03   # ~d_L
   1000002     1.05261320e+03   # ~u_L
   1000003     1.05543721e+03   # ~s_L
   1000004     1.05261062e+03   # ~c_L
   1000005     9.66000420e+02   # ~b_1
   1000006     8.04631855e+02   # ~t_1
   1000011     3.61733392e+02   # ~e_L
   1000012     3.52850833e+02   # ~nue_L
   1000013     3.61817347e+02   # ~mu_L
   1000014     3.52847485e+02   # ~numu_L
   1000015     2.22721799e+02   # ~stau_1
   1000016     3.51679963e+02   # ~nu_tau_L
   2000001     1.01085780e+03   # ~d_R
   2000002     1.01417729e+03   # ~u_R
   2000003     1.01085510e+03   # ~s_R
   2000004     1.01417454e+03   # ~c_R
   2000005     1.00760514e+03   # ~b_2
   2000006     1.01157934e+03   # ~t_2
   2000011     2.29860427e+02   # ~e_R
   2000013     2.29849989e+02   # ~mu_R
   2000015     3.62871916e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06794552e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95809497e-01   # N_{1,1}
  1  2    -1.74818809e-02   # N_{1,2}
  1  3     8.29067888e-02   # N_{1,3}
  1  4    -3.44135644e-02   # N_{1,4}
  2  1     3.81129786e-02   # N_{2,1}
  2  2     9.70434774e-01   # N_{2,2}
  2  3    -1.98230664e-01   # N_{2,3}
  2  4     1.32319137e-01   # N_{2,4}
  3  1    -3.32368391e-02   # N_{3,1}
  3  2     4.84166871e-02   # N_{3,2}
  3  3     7.03439888e-01   # N_{3,3}
  3  4     7.08324404e-01   # N_{3,4}
  4  1    -7.61981535e-02   # N_{4,1}
  4  2     2.35810427e-01   # N_{4,2}
  4  3     6.77497891e-01   # N_{4,3}
  4  4    -6.92519958e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.59912609e-01   # U_{1,1}
  1  2    -2.80299453e-01   # U_{1,2}
  2  1     2.80299453e-01   # U_{2,1}
  2  2     9.59912609e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.81960351e-01   # V_{1,1}
  1  2    -1.89086935e-01   # V_{1,2}
  2  1     1.89086935e-01   # V_{2,1}
  2  2     9.81960351e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.26525136e-01   # F_{11}
  1  2     9.04475709e-01   # F_{12}
  2  1     9.04475709e-01   # F_{21}
  2  2    -4.26525136e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.75364008e-01   # F_{11}
  1  2     2.20601570e-01   # F_{12}
  2  1    -2.20601570e-01   # F_{21}
  2  2     9.75364008e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.42005039e-01   # F_{11}
  1  2     9.89865935e-01   # F_{12}
  2  1     9.89865935e-01   # F_{21}
  2  2    -1.42005039e-01   # F_{22}
Block gauge Q= 8.74722550e+02  # SM gauge couplings
     1     3.62418203e-01   # g'(Q)MSSM DRbar
     2     6.42999474e-01   # g(Q)MSSM DRbar
     3     1.06092143e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.74722550e+02  
  3  3     8.61213928e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.74722550e+02  
  3  3     1.35311290e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.74722550e+02  
  3  3     1.00517767e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.74722550e+02 # Higgs mixing parameters
     1     6.30053718e+02    # mu(Q)MSSM DRbar
     2     9.67348907e+00    # tan beta(Q)MSSM DRbar
     3     2.44103501e+02    # higgs vev(Q)MSSM DRbar
     4     5.34632585e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.74722550e+02  # MSSM DRbar SUSY breaking parameters
     1     2.09262598e+02      # M_1(Q)
     2     3.88491971e+02      # M_2(Q)
     3     1.11349825e+03      # M_3(Q)
    21     1.09131599e+05      # mH1^2(Q)
    22    -3.84508082e+05      # mH2^2(Q)
    31     3.54245368e+02      # meL(Q)
    32     3.54242034e+02      # mmuL(Q)
    33     3.53236792e+02      # mtauL(Q)
    34     2.22008396e+02      # meR(Q)
    35     2.21997576e+02      # mmuR(Q)
    36     2.18714789e+02      # mtauR(Q)
    41     1.01845984e+03      # mqL1(Q)
    42     1.01845721e+03      # mqL2(Q)
    43     9.38675162e+02      # mqL3(Q)
    44     9.80443266e+02      # muR(Q)
    45     9.80440475e+02      # mcR(Q)
    46     8.07104728e+02      # mtR(Q)
    47     9.75844814e+02      # mdR(Q)
    48     9.75842071e+02      # msR(Q)
    49     9.70837134e+02      # mbR(Q)
Block au Q= 8.74722550e+02  
  1  1    -1.14087709e+03      # Au(Q)MSSM DRbar
  2  2    -1.14087197e+03      # Ac(Q)MSSM DRbar
  3  3    -8.80209755e+02      # At(Q)MSSM DRbar
Block ad Q= 8.74722550e+02  
  1  1    -1.39589316e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39588841e+03      # As(Q)MSSM DRbar
  3  3    -1.30437391e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.74722550e+02  
  1  1    -2.99390756e+02      # Ae(Q)MSSM DRbar
  2  2    -2.99385376e+02      # Amu(Q)MSSM DRbar
  3  3    -2.97763502e+02      # Atau(Q)MSSM DRbar
