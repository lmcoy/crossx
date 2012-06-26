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
     1    1.70000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03925026e+01   # MW
        25     1.16191678e+02   # h0
        35     1.11965002e+03   # H0
        36     1.11960801e+03   # A0
        37     1.12268726e+03   # H+
   1000021     1.26270119e+03   # ~g
   1000022     2.27572098e+02   # ~neutralino(1)
   1000023     4.38358976e+02   # ~neutralino(2)
   1000024     4.38528836e+02   # ~chargino(1)
   1000025    -8.78086156e+02   # ~neutralino(3)
   1000035     8.84642364e+02   # ~neutralino(4)
   1000037     8.84980214e+02   # ~chargino(2)
   1000039     4.02900000e+00   # ~gravitino
   1000001     1.55534515e+03   # ~d_L
   1000002     1.55348793e+03   # ~u_L
   1000003     1.55533900e+03   # ~s_L
   1000004     1.55348177e+03   # ~c_L
   1000005     1.37508171e+03   # ~b_1
   1000006     1.09369882e+03   # ~t_1
   1000011     7.52668395e+02   # ~e_L
   1000012     7.48192198e+02   # ~nue_L
   1000013     7.52754501e+02   # ~mu_L
   1000014     7.48176261e+02   # ~numu_L
   1000015     4.95087461e+02   # ~stau_1
   1000016     7.42976821e+02   # ~nu_tau_L
   2000001     1.39757410e+03   # ~d_R
   2000002     1.42654731e+03   # ~u_R
   2000003     1.39756497e+03   # ~s_R
   2000004     1.42654279e+03   # ~c_R
   2000005     1.40794785e+03   # ~b_2
   2000006     1.41878260e+03   # ~t_2
   2000011     5.11966094e+02   # ~e_R
   2000013     5.11919157e+02   # ~mu_R
   2000015     7.48655162e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.00211494e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98215170e-01   # N_{1,1}
  1  2    -8.06546010e-03   # N_{1,2}
  1  3     5.62635741e-02   # N_{1,3}
  1  4    -1.83257537e-02   # N_{1,4}
  2  1     1.60161324e-02   # N_{2,1}
  2  2     9.90368420e-01   # N_{2,2}
  2  3    -1.20732198e-01   # N_{2,3}
  2  4     6.58605591e-02   # N_{2,4}
  3  1    -2.64255098e-02   # N_{3,1}
  3  2     3.93067448e-02   # N_{3,2}
  3  3     7.04963693e-01   # N_{3,3}
  3  4     7.07660133e-01   # N_{3,4}
  4  1    -5.11043110e-02   # N_{4,1}
  4  2     1.32515363e-01   # N_{4,2}
  4  3     6.96623527e-01   # N_{4,3}
  4  4    -7.03238004e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.85536344e-01   # U_{1,1}
  1  2    -1.69464198e-01   # U_{1,2}
  2  1     1.69464198e-01   # U_{2,1}
  2  2     9.85536344e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.95593675e-01   # V_{1,1}
  1  2    -9.37722469e-02   # V_{1,2}
  2  1     9.37722469e-02   # V_{2,1}
  2  2     9.95593675e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     1.76672455e-01   # F_{11}
  1  2     9.84269701e-01   # F_{12}
  2  1     9.84269701e-01   # F_{21}
  2  2    -1.76672455e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.91122281e-01   # F_{11}
  1  2     9.20338721e-01   # F_{12}
  2  1     9.20338721e-01   # F_{21}
  2  2    -3.91122281e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     7.40627656e-02   # F_{11}
  1  2     9.97253582e-01   # F_{12}
  2  1     9.97253582e-01   # F_{21}
  2  2    -7.40627656e-02   # F_{22}
Block gauge Q= 1.21062430e+03  # SM gauge couplings
     1     3.62924663e-01   # g'(Q)MSSM DRbar
     2     6.41431021e-01   # g(Q)MSSM DRbar
     3     1.04842931e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.21062430e+03  
  3  3     8.52191502e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.21062430e+03  
  3  3     1.96431693e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.21062430e+03  
  3  3     1.50631056e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.21062430e+03 # Higgs mixing parameters
     1     8.71634594e+02    # mu(Q)MSSM DRbar
     2     1.44703117e+01    # tan beta(Q)MSSM DRbar
     3     2.43738228e+02    # higgs vev(Q)MSSM DRbar
     4     1.30826756e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.21062430e+03  # MSSM DRbar SUSY breaking parameters
     1     2.31053026e+02      # M_1(Q)
     2     4.26879572e+02      # M_2(Q)
     3     1.16096963e+03      # M_3(Q)
    21     4.80632722e+05      # mH1^2(Q)
    22    -7.33200078e+05      # mH2^2(Q)
    31     7.48873456e+02      # meL(Q)
    32     7.48857530e+02      # mmuL(Q)
    33     7.43993693e+02      # mtauL(Q)
    34     5.06906105e+02      # meR(Q)
    35     5.06858731e+02      # mmuR(Q)
    36     4.92221973e+02      # mtauR(Q)
    41     1.52039757e+03      # mqL1(Q)
    42     1.52039126e+03      # mqL2(Q)
    43     1.37303035e+03      # mqL3(Q)
    44     1.39180499e+03      # muR(Q)
    45     1.39180032e+03      # mcR(Q)
    46     1.05709281e+03      # mtR(Q)
    47     1.36060903e+03      # mdR(Q)
    48     1.36059957e+03      # msR(Q)
    49     1.34335678e+03      # mbR(Q)
Block au Q= 1.21062430e+03  
  1  1    -1.07293938e+03      # Au(Q)MSSM DRbar
  2  2    -1.07293401e+03      # Ac(Q)MSSM DRbar
  3  3    -8.55268797e+02      # At(Q)MSSM DRbar
Block ad Q= 1.21062430e+03  
  1  1    -1.27995679e+03      # Ad(Q)MSSM DRbar
  2  2    -1.27994938e+03      # As(Q)MSSM DRbar
  3  3    -1.19803792e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.21062430e+03  
  1  1    -2.40131499e+02      # Ae(Q)MSSM DRbar
  2  2    -2.40123322e+02      # Amu(Q)MSSM DRbar
  3  3    -2.37632903e+02      # Atau(Q)MSSM DRbar
