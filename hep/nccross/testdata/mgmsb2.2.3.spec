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
     1    1.40000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03942570e+01   # MW
        25     1.14912146e+02   # h0
        35     9.33742754e+02   # H0
        36     9.33696319e+02   # A0
        37     9.37354455e+02   # H+
   1000021     1.05886106e+03   # ~g
   1000022     1.86562837e+02   # ~neutralino(1)
   1000023     3.59539199e+02   # ~neutralino(2)
   1000024     3.59692438e+02   # ~chargino(1)
   1000025    -7.38413136e+02   # ~neutralino(3)
   1000035     7.45947426e+02   # ~neutralino(4)
   1000037     7.46341637e+02   # ~chargino(2)
   1000039     3.31800000e+00   # ~gravitino
   1000001     1.29685972e+03   # ~d_L
   1000002     1.29459690e+03   # ~u_L
   1000003     1.29685456e+03   # ~s_L
   1000004     1.29459174e+03   # ~c_L
   1000005     1.14617302e+03   # ~b_1
   1000006     9.11753497e+02   # ~t_1
   1000011     6.23568521e+02   # ~e_L
   1000012     6.18212515e+02   # ~nue_L
   1000013     6.23665171e+02   # ~mu_L
   1000014     6.18199188e+02   # ~numu_L
   1000015     4.08613420e+02   # ~stau_1
   1000016     6.13855513e+02   # ~nu_tau_L
   2000001     1.16705561e+03   # ~d_R
   2000002     1.19043557e+03   # ~u_R
   2000003     1.16704795e+03   # ~s_R
   2000004     1.19043180e+03   # ~c_R
   2000005     1.17537761e+03   # ~b_2
   2000006     1.18855854e+03   # ~t_2
   2000011     4.23402800e+02   # ~e_R
   2000013     4.23363578e+02   # ~mu_R
   2000015     6.20696304e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.02942425e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97453809e-01   # N_{1,1}
  1  2    -1.14272771e-02   # N_{1,2}
  1  3     6.70535269e-02   # N_{1,3}
  1  4    -2.14275795e-02   # N_{1,4}
  2  1     2.23919886e-02   # N_{2,1}
  2  2     9.86910241e-01   # N_{2,2}
  2  3    -1.40834485e-01   # N_{2,3}
  2  4     7.53154852e-02   # N_{2,4}
  3  1    -3.15811813e-02   # N_{3,1}
  3  2     4.71618508e-02   # N_{3,2}
  3  3     7.04036290e-01   # N_{3,3}
  3  4     7.07892146e-01   # N_{3,4}
  4  1    -5.98926300e-02   # N_{4,1}
  4  2     1.53796466e-01   # N_{4,2}
  4  3     6.92822037e-01   # N_{4,3}
  4  4    -7.01966627e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.80203051e-01   # U_{1,1}
  1  2    -1.97994896e-01   # U_{1,2}
  2  1     1.97994896e-01   # U_{2,1}
  2  2     9.80203051e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.94210456e-01   # V_{1,1}
  1  2    -1.07450308e-01   # V_{1,2}
  2  1     1.07450308e-01   # V_{2,1}
  2  2     9.94210456e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.11811829e-01   # F_{11}
  1  2     9.77310467e-01   # F_{12}
  2  1     9.77310467e-01   # F_{21}
  2  2    -2.11811829e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.62124123e-01   # F_{11}
  1  2     8.86815254e-01   # F_{12}
  2  1     8.86815254e-01   # F_{21}
  2  2    -4.62124123e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.01320206e-02   # F_{11}
  1  2     9.95929826e-01   # F_{12}
  2  1     9.95929826e-01   # F_{21}
  2  2    -9.01320206e-02   # F_{22}
Block gauge Q= 1.01068085e+03  # SM gauge couplings
     1     3.62543729e-01   # g'(Q)MSSM DRbar
     2     6.42381635e-01   # g(Q)MSSM DRbar
     3     1.05773418e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.01068085e+03  
  3  3     8.58287375e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.01068085e+03  
  3  3     1.98160387e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.01068085e+03  
  3  3     1.50816529e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.01068085e+03 # Higgs mixing parameters
     1     7.32161881e+02    # mu(Q)MSSM DRbar
     2     1.45007875e+01    # tan beta(Q)MSSM DRbar
     3     2.43954063e+02    # higgs vev(Q)MSSM DRbar
     4     9.10381502e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.01068085e+03  # MSSM DRbar SUSY breaking parameters
     1     1.89764424e+02      # M_1(Q)
     2     3.52254793e+02      # M_2(Q)
     3     9.72647169e+02      # M_3(Q)
    21     3.28155450e+05      # mH1^2(Q)
    22    -5.19322010e+05      # mH2^2(Q)
    31     6.20007035e+02      # meL(Q)
    32     6.19993741e+02      # mmuL(Q)
    33     6.15942080e+02      # mtauL(Q)
    34     4.18498822e+02      # meR(Q)
    35     4.18459166e+02      # mmuR(Q)
    36     4.06229765e+02      # mtauR(Q)
    41     1.26679165e+03      # mqL1(Q)
    42     1.26678635e+03      # mqL2(Q)
    43     1.14335397e+03      # mqL3(Q)
    44     1.16090435e+03      # muR(Q)
    45     1.16090044e+03      # mcR(Q)
    46     8.80863003e+02      # mtR(Q)
    47     1.13542198e+03      # mdR(Q)
    48     1.13541403e+03      # msR(Q)
    49     1.12090659e+03      # mbR(Q)
Block au Q= 1.01068085e+03  
  1  1    -9.06014084e+02      # Au(Q)MSSM DRbar
  2  2    -9.06009508e+02      # Ac(Q)MSSM DRbar
  3  3    -7.20190833e+02      # At(Q)MSSM DRbar
Block ad Q= 1.01068085e+03  
  1  1    -1.08312636e+03      # Ad(Q)MSSM DRbar
  2  2    -1.08312003e+03      # As(Q)MSSM DRbar
  3  3    -1.01316107e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.01068085e+03  
  1  1    -2.00105480e+02      # Ae(Q)MSSM DRbar
  2  2    -2.00098586e+02      # Amu(Q)MSSM DRbar
  3  3    -1.98003335e+02      # Atau(Q)MSSM DRbar
