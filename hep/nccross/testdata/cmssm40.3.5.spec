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
     1    1.20000000e+03   # m0
     2    4.50000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.08931841e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03908320e+01   # MW
        25     1.16884645e+02   # h0
        35     9.44106268e+02   # H0
        36     9.44212640e+02   # A0
        37     9.47775312e+02   # H+
   1000021     1.10030030e+03   # ~g
   1000022     1.88518267e+02   # ~neutralino(1)
   1000023     3.60117388e+02   # ~neutralino(2)
   1000024     3.60199310e+02   # ~chargino(1)
   1000025    -6.19872636e+02   # ~neutralino(3)
   1000035     6.30411265e+02   # ~neutralino(4)
   1000037     6.30836632e+02   # ~chargino(2)
   1000001     1.50616580e+03   # ~d_L
   1000002     1.50421282e+03   # ~u_L
   1000003     1.50611400e+03   # ~s_L
   1000004     1.50416095e+03   # ~c_L
   1000005     1.18342315e+03   # ~b_1
   1000006     9.83223974e+02   # ~t_1
   1000011     1.23339844e+03   # ~e_L
   1000012     1.23051432e+03   # ~nue_L
   1000013     1.23313663e+03   # ~mu_L
   1000014     1.23021198e+03   # ~numu_L
   1000015     9.95442131e+02   # ~stau_1
   1000016     1.13138814e+03   # ~nu_tau_L
   2000001     1.48466063e+03   # ~d_R
   2000002     1.48591199e+03   # ~u_R
   2000003     1.48456162e+03   # ~s_R
   2000004     1.48590523e+03   # ~c_R
   2000005     1.31126547e+03   # ~b_2
   2000006     1.21430194e+03   # ~t_2
   2000011     1.21108634e+03   # ~e_R
   2000013     1.21046953e+03   # ~mu_R
   2000015     1.13750011e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59217521e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96170817e-01   # N_{1,1}
  1  2    -1.28157328e-02   # N_{1,2}
  1  3     8.20773340e-02   # N_{1,3}
  1  4    -2.72538519e-02   # N_{1,4}
  2  1     3.11446861e-02   # N_{2,1}
  2  2     9.75141305e-01   # N_{2,2}
  2  3    -1.88439530e-01   # N_{2,3}
  2  4     1.12338717e-01   # N_{2,4}
  3  1    -3.78270206e-02   # N_{3,1}
  3  2     5.54613290e-02   # N_{3,2}
  3  3     7.02896466e-01   # N_{3,3}
  3  4     7.08117021e-01   # N_{3,4}
  4  1    -7.24073839e-02   # N_{4,1}
  4  2     2.14147690e-01   # N_{4,2}
  4  3     6.80948172e-01   # N_{4,3}
  4  4    -6.96568392e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.64069995e-01   # U_{1,1}
  1  2    -2.65648349e-01   # U_{1,2}
  2  1     2.65648349e-01   # U_{2,1}
  2  2     9.64069995e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86940279e-01   # V_{1,1}
  1  2    -1.61086579e-01   # V_{1,2}
  2  1     1.61086579e-01   # V_{2,1}
  2  2     9.86940279e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.95764766e-01   # F_{11}
  1  2     9.55260804e-01   # F_{12}
  2  1     9.55260804e-01   # F_{21}
  2  2    -2.95764766e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.83829583e-01   # F_{11}
  1  2     1.79107097e-01   # F_{12}
  2  1    -1.79107097e-01   # F_{21}
  2  2     9.83829583e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.51019924e-01   # F_{11}
  1  2     9.88530719e-01   # F_{12}
  2  1     9.88530719e-01   # F_{21}
  2  2    -1.51019924e-01   # F_{22}
Block gauge Q= 1.06743794e+03  # SM gauge couplings
     1     3.62257177e-01   # g'(Q)MSSM DRbar
     2     6.41708065e-01   # g(Q)MSSM DRbar
     3     1.05405400e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.06743794e+03  
  3  3     8.54155021e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.06743794e+03  
  3  3     5.15980603e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.06743794e+03  
  3  3     4.12802853e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.06743794e+03 # Higgs mixing parameters
     1     6.12006996e+02    # mu(Q)MSSM DRbar
     2     3.92069918e+01    # tan beta(Q)MSSM DRbar
     3     2.43612676e+02    # higgs vev(Q)MSSM DRbar
     4     1.07297864e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.06743794e+03  # MSSM DRbar SUSY breaking parameters
     1     1.90401809e+02      # M_1(Q)
     2     3.52811480e+02      # M_2(Q)
     3     9.97151229e+02      # M_3(Q)
    21     5.38235839e+05      # mH1^2(Q)
    22    -3.57823799e+05      # mH2^2(Q)
    31     1.23047044e+03      # meL(Q)
    32     1.23016889e+03      # mmuL(Q)
    33     1.13385541e+03      # mtauL(Q)
    34     1.20893259e+03      # meR(Q)
    35     1.20831559e+03      # mmuR(Q)
    36     1.00069300e+03      # mtauR(Q)
    41     1.47875983e+03      # mqL1(Q)
    42     1.47870712e+03      # mqL2(Q)
    43     1.16484484e+03      # mqL3(Q)
    44     1.46163641e+03      # muR(Q)
    45     1.46162952e+03      # mcR(Q)
    46     9.68031617e+02      # mtR(Q)
    47     1.45972550e+03      # mdR(Q)
    48     1.45962458e+03      # msR(Q)
    49     1.28514658e+03      # mbR(Q)
Block au Q= 1.06743794e+03  
  1  1    -1.35325971e+03      # Au(Q)MSSM DRbar
  2  2    -1.35322616e+03      # Ac(Q)MSSM DRbar
  3  3    -9.19284907e+02      # At(Q)MSSM DRbar
Block ad Q= 1.06743794e+03  
  1  1    -1.56522527e+03      # Ad(Q)MSSM DRbar
  2  2    -1.56513986e+03      # As(Q)MSSM DRbar
  3  3    -1.29440046e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.06743794e+03  
  1  1    -5.92817382e+02      # Ae(Q)MSSM DRbar
  2  2    -5.92512745e+02      # Amu(Q)MSSM DRbar
  3  3    -4.97600421e+02      # Atau(Q)MSSM DRbar
