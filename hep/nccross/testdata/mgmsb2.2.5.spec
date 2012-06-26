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
     1    1.60000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03929819e+01   # MW
        25     1.15800368e+02   # h0
        35     1.05799442e+03   # H0
        36     1.05795113e+03   # A0
        37     1.06120001e+03   # H+
   1000021     1.19511564e+03   # ~g
   1000022     2.13897007e+02   # ~neutralino(1)
   1000023     4.12136742e+02   # ~neutralino(2)
   1000024     4.12302431e+02   # ~chargino(1)
   1000025    -8.31851516e+02   # ~neutralino(3)
   1000035     8.38699128e+02   # ~neutralino(4)
   1000037     8.39052491e+02   # ~chargino(2)
   1000039     3.79200000e+00   # ~gravitino
   1000001     1.46948030e+03   # ~d_L
   1000002     1.46750433e+03   # ~u_L
   1000003     1.46947449e+03   # ~s_L
   1000004     1.46749851e+03   # ~c_L
   1000005     1.29911604e+03   # ~b_1
   1000006     1.03323124e+03   # ~t_1
   1000011     7.09694311e+02   # ~e_L
   1000012     7.04961426e+02   # ~nue_L
   1000013     7.09783841e+02   # ~mu_L
   1000014     7.04946355e+02   # ~numu_L
   1000015     4.66285559e+02   # ~stau_1
   1000016     7.00031055e+02   # ~nu_tau_L
   2000001     1.32104287e+03   # ~d_R
   2000002     1.34815238e+03   # ~u_R
   2000003     1.32103423e+03   # ~s_R
   2000004     1.34814811e+03   # ~c_R
   2000005     1.33064199e+03   # ~b_2
   2000006     1.34214902e+03   # ~t_2
   2000011     4.82454467e+02   # ~e_R
   2000013     4.82410086e+02   # ~mu_R
   2000015     7.06048385e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.00915077e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98007386e-01   # N_{1,1}
  1  2    -8.99042083e-03   # N_{1,2}
  1  3     5.94165561e-02   # N_{1,3}
  1  4    -1.92380405e-02   # N_{1,4}
  2  1     1.77804718e-02   # N_{2,1}
  2  2     9.89399055e-01   # N_{2,2}
  2  3    -1.26703652e-01   # N_{2,3}
  2  4     6.86989775e-02   # N_{2,4}
  3  1    -2.79377673e-02   # N_{3,1}
  3  2     4.16071173e-02   # N_{3,2}
  3  3     7.04709111e-01   # N_{3,3}
  3  4     7.07724098e-01   # N_{3,4}
  4  1    -5.37084071e-02   # N_{4,1}
  4  2     1.38843546e-01   # N_{4,2}
  4  3     6.95557997e-01   # N_{4,3}
  4  4    -7.02877621e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.84044805e-01   # U_{1,1}
  1  2    -1.77920829e-01   # U_{1,2}
  2  1     1.77920829e-01   # U_{2,1}
  2  2     9.84044805e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.95199540e-01   # V_{1,1}
  1  2    -9.78666187e-02   # V_{1,2}
  2  1     9.78666187e-02   # V_{2,1}
  2  2     9.95199540e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     1.87082116e-01   # F_{11}
  1  2     9.82344279e-01   # F_{12}
  2  1     9.82344279e-01   # F_{21}
  2  2    -1.87082116e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.13782167e-01   # F_{11}
  1  2     9.10375921e-01   # F_{12}
  2  1     9.10375921e-01   # F_{21}
  2  2    -4.13782167e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     7.87645340e-02   # F_{11}
  1  2     9.96893248e-01   # F_{12}
  2  1     9.96893248e-01   # F_{21}
  2  2    -7.87645340e-02   # F_{22}
Block gauge Q= 1.14414473e+03  # SM gauge couplings
     1     3.62805387e-01   # g'(Q)MSSM DRbar
     2     6.41726514e-01   # g(Q)MSSM DRbar
     3     1.05131166e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.14414473e+03  
  3  3     8.54078767e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.14414473e+03  
  3  3     1.96967247e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.14414473e+03  
  3  3     1.50689509e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.14414473e+03 # Higgs mixing parameters
     1     8.25493221e+02    # mu(Q)MSSM DRbar
     2     1.44797687e+01    # tan beta(Q)MSSM DRbar
     3     2.43804701e+02    # higgs vev(Q)MSSM DRbar
     4     1.16832610e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.14414473e+03  # MSSM DRbar SUSY breaking parameters
     1     2.17278020e+02      # M_1(Q)
     2     4.02020956e+02      # M_2(Q)
     3     1.09852222e+03      # M_3(Q)
    21     4.26645224e+05      # mH1^2(Q)
    22    -6.58338836e+05      # mH2^2(Q)
    31     7.05989750e+02      # meL(Q)
    32     7.05974697e+02      # mmuL(Q)
    33     7.01380497e+02      # mtauL(Q)
    34     4.77462000e+02      # meR(Q)
    35     4.77417184e+02      # mmuR(Q)
    36     4.63578946e+02      # mtauR(Q)
    41     1.43615324e+03      # mqL1(Q)
    42     1.43614726e+03      # mqL2(Q)
    43     1.29671910e+03      # mqL3(Q)
    44     1.31512753e+03      # muR(Q)
    45     1.31512311e+03      # mcR(Q)
    46     9.98545002e+02      # mtR(Q)
    47     1.28584033e+03      # mdR(Q)
    48     1.28583137e+03      # msR(Q)
    49     1.26949423e+03      # mbR(Q)
Block au Q= 1.14414473e+03  
  1  1    -1.01773798e+03      # Au(Q)MSSM DRbar
  2  2    -1.01773288e+03      # Ac(Q)MSSM DRbar
  3  3    -8.10560228e+02      # At(Q)MSSM DRbar
Block ad Q= 1.14414473e+03  
  1  1    -1.21490973e+03      # Ad(Q)MSSM DRbar
  2  2    -1.21490267e+03      # As(Q)MSSM DRbar
  3  3    -1.13692863e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.14414473e+03  
  1  1    -2.26842949e+02      # Ae(Q)MSSM DRbar
  2  2    -2.26835196e+02      # Amu(Q)MSSM DRbar
  3  3    -2.24475525e+02      # Atau(Q)MSSM DRbar
