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
     1    2.00000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.90428644e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03926223e+01   # MW
        25     1.14916673e+02   # h0
        35     7.34462756e+02   # H0
        36     7.34165231e+02   # A0
        37     7.38820317e+02   # H+
   1000021     1.14894005e+03   # ~g
   1000022     2.04513187e+02   # ~neutralino(1)
   1000023     3.86561561e+02   # ~neutralino(2)
   1000024     3.86694935e+02   # ~chargino(1)
   1000025    -6.35681657e+02   # ~neutralino(3)
   1000035     6.49351630e+02   # ~neutralino(4)
   1000037     6.48973333e+02   # ~chargino(2)
   1000001     1.06668330e+03   # ~d_L
   1000002     1.06389038e+03   # ~u_L
   1000003     1.06668066e+03   # ~s_L
   1000004     1.06388772e+03   # ~c_L
   1000005     9.74353847e+02   # ~b_1
   1000006     8.10511013e+02   # ~t_1
   1000011     3.93674219e+02   # ~e_L
   1000012     3.85514476e+02   # ~nue_L
   1000013     3.93793595e+02   # ~mu_L
   1000014     3.85510538e+02   # ~numu_L
   1000015     2.70931021e+02   # ~stau_1
   1000016     3.84178465e+02   # ~nu_tau_L
   2000001     1.02272395e+03   # ~d_R
   2000002     1.02600767e+03   # ~u_R
   2000003     1.02272119e+03   # ~s_R
   2000004     1.02600484e+03   # ~c_R
   2000005     1.01912737e+03   # ~b_2
   2000006     1.01874917e+03   # ~t_2
   2000011     2.77584711e+02   # ~e_R
   2000013     2.77573596e+02   # ~mu_R
   2000015     3.94457512e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06642924e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95802682e-01   # N_{1,1}
  1  2    -1.74841194e-02   # N_{1,2}
  1  3     8.29653422e-02   # N_{1,3}
  1  4    -3.44684770e-02   # N_{1,4}
  2  1     3.81534083e-02   # N_{2,1}
  2  2     9.70374191e-01   # N_{2,2}
  2  3    -1.98393759e-01   # N_{2,3}
  2  4     1.32507217e-01   # N_{2,4}
  3  1    -3.32398584e-02   # N_{3,1}
  3  2     4.84031687e-02   # N_{3,2}
  3  3     7.03443184e-01   # N_{3,3}
  3  4     7.08321912e-01   # N_{3,4}
  4  1    -7.62656383e-02   # N_{4,1}
  4  2     2.36062211e-01   # N_{4,2}
  4  3     6.77439558e-01   # N_{4,3}
  4  4    -6.92483812e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.59760559e-01   # U_{1,1}
  1  2    -2.80819638e-01   # U_{1,2}
  2  1     2.80819638e-01   # U_{2,1}
  2  2     9.59760559e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.81853504e-01   # V_{1,1}
  1  2    -1.89640970e-01   # V_{1,2}
  2  1     1.89640970e-01   # V_{2,1}
  2  2     9.81853504e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.19802170e-01   # F_{11}
  1  2     9.07615633e-01   # F_{12}
  2  1     9.07615633e-01   # F_{21}
  2  2    -4.19802170e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.79310295e-01   # F_{11}
  1  2     2.02364390e-01   # F_{12}
  2  1    -2.02364390e-01   # F_{21}
  2  2     9.79310295e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.41717879e-01   # F_{11}
  1  2     9.89907088e-01   # F_{12}
  2  1     9.89907088e-01   # F_{21}
  2  2    -1.41717879e-01   # F_{22}
Block gauge Q= 8.81032534e+02  # SM gauge couplings
     1     3.62367066e-01   # g'(Q)MSSM DRbar
     2     6.42912338e-01   # g(Q)MSSM DRbar
     3     1.06063219e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.81032534e+02  
  3  3     8.61107013e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.81032534e+02  
  3  3     1.35316106e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.81032534e+02  
  3  3     1.00508563e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.81032534e+02 # Higgs mixing parameters
     1     6.30127658e+02    # mu(Q)MSSM DRbar
     2     9.67252422e+00    # tan beta(Q)MSSM DRbar
     3     2.44090642e+02    # higgs vev(Q)MSSM DRbar
     4     5.58629273e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.81032534e+02  # MSSM DRbar SUSY breaking parameters
     1     2.09265032e+02      # M_1(Q)
     2     3.88503950e+02      # M_2(Q)
     3     1.11336298e+03      # M_3(Q)
    21     1.32434046e+05      # mH1^2(Q)
    22    -3.84066432e+05      # mH2^2(Q)
    31     3.86785724e+02      # meL(Q)
    32     3.86781787e+02      # mmuL(Q)
    33     3.85594352e+02      # mtauL(Q)
    34     2.71218656e+02      # meR(Q)
    35     2.71207270e+02      # mmuR(Q)
    36     2.67755537e+02      # mtauR(Q)
    41     1.02962175e+03      # mqL1(Q)
    42     1.02961905e+03      # mqL2(Q)
    43     9.46650749e+02      # mqL3(Q)
    44     9.92131237e+02      # muR(Q)
    45     9.92128360e+02      # mcR(Q)
    46     8.11805645e+02      # mtR(Q)
    47     9.87601195e+02      # mdR(Q)
    48     9.87598382e+02      # msR(Q)
    49     9.82452273e+02      # mbR(Q)
Block au Q= 8.81032534e+02  
  1  1    -1.14061308e+03      # Au(Q)MSSM DRbar
  2  2    -1.14060796e+03      # Ac(Q)MSSM DRbar
  3  3    -8.79950590e+02      # At(Q)MSSM DRbar
Block ad Q= 8.81032534e+02  
  1  1    -1.39561256e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39560781e+03      # As(Q)MSSM DRbar
  3  3    -1.30409309e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.81032534e+02  
  1  1    -2.99397514e+02      # Ae(Q)MSSM DRbar
  2  2    -2.99392134e+02      # Amu(Q)MSSM DRbar
  3  3    -2.97770061e+02      # Atau(Q)MSSM DRbar
