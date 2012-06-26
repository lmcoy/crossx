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
     1    1.17000000e+05   # lambda
     2    1.30000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.30000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03977205e+01   # MW
        25     1.14216693e+02   # h0
        35     5.90790506e+02   # H0
        36     5.90524207e+02   # A0
        37     5.96227596e+02   # H+
   1000021     1.09527358e+03   # ~g
   1000022     1.90923756e+02   # ~neutralino(1)
   1000023     3.53356792e+02   # ~neutralino(2)
   1000024     3.53323625e+02   # ~chargino(1)
   1000025    -4.59660114e+02   # ~neutralino(3)
   1000035     4.91703123e+02   # ~neutralino(4)
   1000037     4.90286333e+02   # ~chargino(2)
   1000039     3.60477000e-09   # ~gravitino
   1000001     1.31059535e+03   # ~d_L
   1000002     1.30836692e+03   # ~u_L
   1000003     1.31059357e+03   # ~s_L
   1000004     1.30836514e+03   # ~c_L
   1000005     1.24245365e+03   # ~b_1
   1000006     1.15736507e+03   # ~t_1
   1000011     4.10055506e+02   # ~e_L
   1000012     4.02041968e+02   # ~nue_L
   1000013     4.10052043e+02   # ~mu_L
   1000014     4.02040165e+02   # ~numu_L
   1000015     1.98436755e+02   # ~stau_1
   1000016     4.01246537e+02   # ~nu_tau_L
   2000001     1.25097347e+03   # ~d_R
   2000002     1.25491683e+03   # ~u_R
   2000003     1.25097100e+03   # ~s_R
   2000004     1.25491556e+03   # ~c_R
   2000005     1.26215716e+03   # ~b_2
   2000006     1.27183564e+03   # ~t_2
   2000011     2.04124308e+02   # ~e_R
   2000013     2.04117118e+02   # ~mu_R
   2000015     4.10657731e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.33552357e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.89895030e-01   # N_{1,1}
  1  2    -2.78647638e-02   # N_{1,2}
  1  3     1.25555717e-01   # N_{1,3}
  1  4    -5.97255898e-02   # N_{1,4}
  2  1     8.97874873e-02   # N_{2,1}
  2  2     8.74604192e-01   # N_{2,2}
  2  3    -3.72450177e-01   # N_{2,3}
  2  4     2.97130578e-01   # N_{2,4}
  3  1    -4.43882497e-02   # N_{3,1}
  3  2     6.22211672e-02   # N_{3,2}
  3  3     7.01041065e-01   # N_{3,3}
  3  4     7.09013141e-01   # N_{3,4}
  4  1    -1.00377885e-01   # N_{4,1}
  4  2     4.80020405e-01   # N_{4,2}
  4  3     5.95027774e-01   # N_{4,3}
  4  4    -6.36746919e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.45032821e-01   # U_{1,1}
  1  2    -5.34714438e-01   # U_{1,2}
  2  1     5.34714438e-01   # U_{2,1}
  2  2     8.45032821e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.02834263e-01   # V_{1,1}
  1  2    -4.29988713e-01   # V_{1,2}
  2  1     4.29988713e-01   # V_{2,1}
  2  2     9.02834263e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.24832490e-01   # F_{11}
  1  2     9.74397430e-01   # F_{12}
  2  1     9.74397430e-01   # F_{21}
  2  2    -2.24832490e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.80313443e-01   # F_{11}
  1  2     9.24857657e-01   # F_{12}
  2  1     9.24857657e-01   # F_{21}
  2  2    -3.80313443e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.31076066e-02   # F_{11}
  1  2     9.95656052e-01   # F_{12}
  2  1     9.95656052e-01   # F_{21}
  2  2    -9.31076066e-02   # F_{22}
Block gauge Q= 1.18854888e+03  # SM gauge couplings
     1     3.63445959e-01   # g'(Q)MSSM DRbar
     2     6.43599045e-01   # g(Q)MSSM DRbar
     3     1.05287004e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18854888e+03  
  3  3     8.58081787e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18854888e+03  
  3  3     2.02179694e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18854888e+03  
  3  3     1.51223540e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18854888e+03 # Higgs mixing parameters
     1     4.51092813e+02    # mu(Q)MSSM DRbar
     2     1.44683873e+01    # tan beta(Q)MSSM DRbar
     3     2.43362604e+02    # higgs vev(Q)MSSM DRbar
     4     3.86178403e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18854888e+03  # MSSM DRbar SUSY breaking parameters
     1     1.97797770e+02      # M_1(Q)
     2     3.70800191e+02      # M_2(Q)
     3     9.97189000e+02      # M_3(Q)
    21     1.43191415e+05      # mH1^2(Q)
    22    -1.75218000e+05      # mH2^2(Q)
    31     4.03307036e+02      # meL(Q)
    32     4.03305232e+02      # mmuL(Q)
    33     4.02753021e+02      # mtauL(Q)
    34     1.93653686e+02      # meR(Q)
    35     1.93646101e+02      # mmuR(Q)
    36     1.91310276e+02      # mtauR(Q)
    41     1.27538583e+03      # mqL1(Q)
    42     1.27538399e+03      # mqL2(Q)
    43     1.23139451e+03      # mqL3(Q)
    44     1.22177367e+03      # muR(Q)
    45     1.22177236e+03      # mcR(Q)
    46     1.13172057e+03      # mtR(Q)
    47     1.21657417e+03      # mdR(Q)
    48     1.21657160e+03      # msR(Q)
    49     1.21160022e+03      # mbR(Q)
Block au Q= 1.18854888e+03  
  1  1    -3.03356167e+02      # Au(Q)MSSM DRbar
  2  2    -3.03355738e+02      # Ac(Q)MSSM DRbar
  3  3    -2.85813288e+02      # At(Q)MSSM DRbar
Block ad Q= 1.18854888e+03  
  1  1    -3.22762465e+02      # Ad(Q)MSSM DRbar
  2  2    -3.22761868e+02      # As(Q)MSSM DRbar
  3  3    -3.16160843e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.18854888e+03  
  1  1    -3.17671023e+01      # Ae(Q)MSSM DRbar
  2  2    -3.17668677e+01      # Amu(Q)MSSM DRbar
  3  3    -3.16950607e+01      # Atau(Q)MSSM DRbar
