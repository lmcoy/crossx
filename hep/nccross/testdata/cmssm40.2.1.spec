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
     1    5.50000000e+02   # m0
     2    4.50000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.02154218e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03910758e+01   # MW
        25     1.16558519e+02   # h0
        35     6.30724277e+02   # H0
        36     6.30695359e+02   # A0
        37     6.36235961e+02   # H+
   1000021     1.06240384e+03   # ~g
   1000022     1.86428213e+02   # ~neutralino(1)
   1000023     3.55657587e+02   # ~neutralino(2)
   1000024     3.55703223e+02   # ~chargino(1)
   1000025    -6.44979774e+02   # ~neutralino(3)
   1000035     6.53664888e+02   # ~neutralino(4)
   1000037     6.54288917e+02   # ~chargino(2)
   1000001     1.09458753e+03   # ~d_L
   1000002     1.09186340e+03   # ~u_L
   1000003     1.09455253e+03   # ~s_L
   1000004     1.09182831e+03   # ~c_L
   1000005     8.94643230e+02   # ~b_1
   1000006     7.50185662e+02   # ~t_1
   1000011     6.27353742e+02   # ~e_L
   1000012     6.21993789e+02   # ~nue_L
   1000013     6.27250144e+02   # ~mu_L
   1000014     6.21822804e+02   # ~numu_L
   1000015     4.23423506e+02   # ~stau_1
   1000016     5.64285272e+02   # ~nu_tau_L
   2000001     1.06129482e+03   # ~d_R
   2000002     1.06353689e+03   # ~u_R
   2000003     1.06122614e+03   # ~s_R
   2000004     1.06353248e+03   # ~c_R
   2000005     9.69942546e+02   # ~b_2
   2000006     9.60093453e+02   # ~t_2
   2000011     5.76242501e+02   # ~e_R
   2000013     5.75869959e+02   # ~mu_R
   2000015     5.83990142e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60625868e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96575184e-01   # N_{1,1}
  1  2    -1.21188785e-02   # N_{1,2}
  1  3     7.79479308e-02   # N_{1,3}
  1  4    -2.48023387e-02   # N_{1,4}
  2  1     2.78913589e-02   # N_{2,1}
  2  2     9.79607428e-01   # N_{2,2}
  2  3    -1.73032023e-01   # N_{2,3}
  2  4     9.82409178e-02   # N_{2,4}
  3  1    -3.67071651e-02   # N_{3,1}
  3  2     5.42136925e-02   # N_{3,2}
  3  3     7.03051971e-01   # N_{3,3}
  3  4     7.08118200e-01   # N_{3,4}
  4  1    -6.86480828e-02   # N_{4,1}
  4  2     1.93088827e-01   # N_{4,2}
  4  3     6.85348061e-01   # N_{4,3}
  4  4    -6.98786220e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.69737787e-01   # U_{1,1}
  1  2    -2.44148774e-01   # U_{1,2}
  2  1     2.44148774e-01   # U_{2,1}
  2  2     9.69737787e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.89983183e-01   # V_{1,1}
  1  2    -1.41185328e-01   # V_{1,2}
  2  1     1.41185328e-01   # V_{2,1}
  2  2     9.89983183e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.51801472e-01   # F_{11}
  1  2     8.92118507e-01   # F_{12}
  2  1     8.92118507e-01   # F_{21}
  2  2    -4.51801472e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.87290808e-01   # F_{11}
  1  2     4.61210389e-01   # F_{12}
  2  1    -4.61210389e-01   # F_{21}
  2  2     8.87290808e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.13287261e-01   # F_{11}
  1  2     9.49658408e-01   # F_{12}
  2  1     9.49658408e-01   # F_{21}
  2  2    -3.13287261e-01   # F_{22}
Block gauge Q= 8.23123784e+02  # SM gauge couplings
     1     3.61862727e-01   # g'(Q)MSSM DRbar
     2     6.42448415e-01   # g(Q)MSSM DRbar
     3     1.06387658e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.23123784e+02  
  3  3     8.58471850e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.23123784e+02  
  3  3     4.97228091e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.23123784e+02  
  3  3     4.23547250e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.23123784e+02 # Higgs mixing parameters
     1     6.40345247e+02    # mu(Q)MSSM DRbar
     2     3.92488991e+01    # tan beta(Q)MSSM DRbar
     3     2.44087434e+02    # higgs vev(Q)MSSM DRbar
     4     5.09268075e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.23123784e+02  # MSSM DRbar SUSY breaking parameters
     1     1.88924219e+02      # M_1(Q)
     2     3.51468739e+02      # M_2(Q)
     3     1.01086683e+03      # M_3(Q)
    21    -2.92560066e+03      # mH1^2(Q)
    22    -4.04628872e+05      # mH2^2(Q)
    31     6.23754864e+02      # meL(Q)
    32     6.23584299e+02      # mmuL(Q)
    33     5.68119819e+02      # mtauL(Q)
    34     5.73353909e+02      # meR(Q)
    35     5.72979892e+02      # mmuR(Q)
    36     4.41257074e+02      # mtauR(Q)
    41     1.06298978e+03      # mqL1(Q)
    42     1.06295353e+03      # mqL2(Q)
    43     8.85971536e+02      # mqL3(Q)
    44     1.03452388e+03      # muR(Q)
    45     1.03451931e+03      # mcR(Q)
    46     7.58313070e+02      # mtR(Q)
    47     1.03117593e+03      # mdR(Q)
    48     1.03110492e+03      # msR(Q)
    49     9.26506817e+02      # mbR(Q)
Block au Q= 8.23123784e+02  
  1  1    -1.37479248e+03      # Au(Q)MSSM DRbar
  2  2    -1.37475808e+03      # Ac(Q)MSSM DRbar
  3  3    -9.37384343e+02      # At(Q)MSSM DRbar
Block ad Q= 8.23123784e+02  
  1  1    -1.60156423e+03      # Ad(Q)MSSM DRbar
  2  2    -1.60147662e+03      # As(Q)MSSM DRbar
  3  3    -1.33787215e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.23123784e+02  
  1  1    -6.02772157e+02      # Ae(Q)MSSM DRbar
  2  2    -6.02464889e+02      # Amu(Q)MSSM DRbar
  3  3    -5.01802895e+02      # Atau(Q)MSSM DRbar
