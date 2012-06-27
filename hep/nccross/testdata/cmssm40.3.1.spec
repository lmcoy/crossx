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
     1    1.00000000e+03   # m0
     2    3.50000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.26602815e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03915634e+01   # MW
        25     1.15481533e+02   # h0
        35     7.81321246e+02   # H0
        36     7.81503158e+02   # A0
        37     7.85729967e+02   # H+
   1000021     8.75984248e+02   # ~g
   1000022     1.44897664e+02   # ~neutralino(1)
   1000023     2.76968113e+02   # ~neutralino(2)
   1000024     2.77000639e+02   # ~chargino(1)
   1000025    -5.23808667e+02   # ~neutralino(3)
   1000035     5.34363102e+02   # ~neutralino(4)
   1000037     5.35086103e+02   # ~chargino(2)
   1000001     1.23234675e+03   # ~d_L
   1000002     1.22991475e+03   # ~u_L
   1000003     1.23230204e+03   # ~s_L
   1000004     1.22986994e+03   # ~c_L
   1000005     9.54990929e+02   # ~b_1
   1000006     7.84149493e+02   # ~t_1
   1000011     1.02429256e+03   # ~e_L
   1000012     1.02087340e+03   # ~nue_L
   1000013     1.02405909e+03   # ~mu_L
   1000014     1.02061289e+03   # ~numu_L
   1000015     8.23211542e+02   # ~stau_1
   1000016     9.36224331e+02   # ~nu_tau_L
   2000001     1.21644151e+03   # ~d_R
   2000002     1.21698566e+03   # ~u_R
   2000003     1.21635612e+03   # ~s_R
   2000004     1.21697986e+03   # ~c_R
   2000005     1.06995213e+03   # ~b_2
   2000006     9.92686388e+02   # ~t_2
   2000011     1.00826943e+03   # ~e_R
   2000013     1.00773976e+03   # ~mu_R
   2000015     9.43634099e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60316325e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.94743137e-01   # N_{1,1}
  1  2    -1.78918609e-02   # N_{1,2}
  1  3     9.64248610e-02   # N_{1,3}
  1  4    -2.94655438e-02   # N_{1,4}
  2  1     4.06271686e-02   # N_{2,1}
  2  2     9.71565648e-01   # N_{2,2}
  2  3    -2.04628762e-01   # N_{2,3}
  2  4     1.11967380e-01   # N_{2,4}
  3  1    -4.57359859e-02   # N_{3,1}
  3  2     6.78880198e-02   # N_{3,2}
  3  3     7.00929736e-01   # N_{3,3}
  3  4     7.08517425e-01   # N_{3,4}
  4  1    -8.21202992e-02   # N_{4,1}
  4  2     2.26122289e-01   # N_{4,2}
  4  3     6.76407289e-01   # N_{4,3}
  4  4    -6.96130840e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.57410575e-01   # U_{1,1}
  1  2    -2.88729963e-01   # U_{1,2}
  2  1     2.88729963e-01   # U_{2,1}
  2  2     9.57410575e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86958623e-01   # V_{1,1}
  1  2    -1.60974147e-01   # V_{1,2}
  2  1     1.60974147e-01   # V_{2,1}
  2  2     9.86958623e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.42501806e-01   # F_{11}
  1  2     9.39517170e-01   # F_{12}
  2  1     9.39517170e-01   # F_{21}
  2  2    -3.42501806e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.77823961e-01   # F_{11}
  1  2     2.09428510e-01   # F_{12}
  2  1    -2.09428510e-01   # F_{21}
  2  2     9.77823961e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.82486939e-01   # F_{11}
  1  2     9.83208278e-01   # F_{12}
  2  1     9.83208278e-01   # F_{21}
  2  2    -1.82486939e-01   # F_{22}
Block gauge Q= 8.61257298e+02  # SM gauge couplings
     1     3.61775070e-01   # g'(Q)MSSM DRbar
     2     6.42806347e-01   # g(Q)MSSM DRbar
     3     1.06554622e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.61257298e+02  
  3  3     8.61791585e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.61257298e+02  
  3  3     5.18982327e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.61257298e+02  
  3  3     4.12410366e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.61257298e+02 # Higgs mixing parameters
     1     5.15837825e+02    # mu(Q)MSSM DRbar
     2     3.92586686e+01    # tan beta(Q)MSSM DRbar
     3     2.43874484e+02    # higgs vev(Q)MSSM DRbar
     4     7.35838167e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.61257298e+02  # MSSM DRbar SUSY breaking parameters
     1     1.46693363e+02      # M_1(Q)
     2     2.73422600e+02      # M_2(Q)
     3     7.89216514e+02      # M_3(Q)
    21     3.60223940e+05      # mH1^2(Q)
    22    -2.57498230e+05      # mH2^2(Q)
    31     1.02169411e+03      # meL(Q)
    32     1.02143448e+03      # mmuL(Q)
    33     9.39124056e+02      # mtauL(Q)
    34     1.00623646e+03      # meR(Q)
    35     1.00570651e+03      # mmuR(Q)
    36     8.28478006e+02      # mtauR(Q)
    41     1.21017711e+03      # mqL1(Q)
    42     1.21013167e+03      # mqL2(Q)
    43     9.41710713e+02      # mqL3(Q)
    44     1.19788707e+03      # muR(Q)
    45     1.19788119e+03      # mcR(Q)
    46     7.75215662e+02      # mtR(Q)
    47     1.19655376e+03      # mdR(Q)
    48     1.19646687e+03      # msR(Q)
    49     1.04748613e+03      # mbR(Q)
Block au Q= 8.61257298e+02  
  1  1    -1.14589157e+03      # Au(Q)MSSM DRbar
  2  2    -1.14586174e+03      # Ac(Q)MSSM DRbar
  3  3    -7.59360368e+02      # At(Q)MSSM DRbar
Block ad Q= 8.61257298e+02  
  1  1    -1.33462281e+03      # Ad(Q)MSSM DRbar
  2  2    -1.33454686e+03      # As(Q)MSSM DRbar
  3  3    -1.09403054e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.61257298e+02  
  1  1    -5.53007457e+02      # Ae(Q)MSSM DRbar
  2  2    -5.52715099e+02      # Amu(Q)MSSM DRbar
  3  3    -4.62067093e+02      # Atau(Q)MSSM DRbar
