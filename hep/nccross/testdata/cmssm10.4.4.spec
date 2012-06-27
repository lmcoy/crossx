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
     1    1.05000000e+03   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.05577194e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03917295e+01   # MW
        25     1.15544943e+02   # h0
        35     1.24711255e+03   # H0
        36     1.24706021e+03   # A0
        37     1.24975944e+03   # H+
   1000021     1.19854622e+03   # ~g
   1000022     2.07727163e+02   # ~neutralino(1)
   1000023     3.93580964e+02   # ~neutralino(2)
   1000024     3.93752608e+02   # ~chargino(1)
   1000025    -6.31878393e+02   # ~neutralino(3)
   1000035     6.46747012e+02   # ~neutralino(4)
   1000037     6.46161727e+02   # ~chargino(2)
   1000001     1.46196738e+03   # ~d_L
   1000002     1.46000536e+03   # ~u_L
   1000003     1.46196231e+03   # ~s_L
   1000004     1.46000029e+03   # ~c_L
   1000005     1.26998629e+03   # ~b_1
   1000006     1.01663215e+03   # ~t_1
   1000011     1.09844070e+03   # ~e_L
   1000012     1.09530149e+03   # ~nue_L
   1000013     1.09848055e+03   # ~mu_L
   1000014     1.09528661e+03   # ~numu_L
   1000015     1.05579248e+03   # ~stau_1
   1000016     1.09072416e+03   # ~nu_tau_L
   2000001     1.43359314e+03   # ~d_R
   2000002     1.43557499e+03   # ~u_R
   2000003     1.43358821e+03   # ~s_R
   2000004     1.43556951e+03   # ~c_R
   2000005     1.42393455e+03   # ~b_2
   2000006     1.29132625e+03   # ~t_2
   2000011     1.06599543e+03   # ~e_R
   2000013     1.06596471e+03   # ~mu_R
   2000015     1.09459901e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04674238e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95667699e-01   # N_{1,1}
  1  2    -1.74295096e-02   # N_{1,2}
  1  3     8.41732501e-02   # N_{1,3}
  1  4    -3.54529244e-02   # N_{1,4}
  2  1     3.92616933e-02   # N_{2,1}
  2  2     9.67918645e-01   # N_{2,2}
  2  3    -2.05202425e-01   # N_{2,3}
  2  4     1.39585029e-01   # N_{2,4}
  3  1    -3.34066810e-02   # N_{3,1}
  3  2     4.83568748e-02   # N_{3,2}
  3  3     7.03490157e-01   # N_{3,3}
  3  4     7.08270573e-01   # N_{3,4}
  4  1    -7.73844092e-02   # N_{4,1}
  4  2     2.45949835e-01   # N_{4,2}
  4  3     6.75209913e-01   # N_{4,3}
  4  4    -6.91094715e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.56769239e-01   # U_{1,1}
  1  2    -2.90848111e-01   # U_{1,2}
  2  1     2.90848111e-01   # U_{2,1}
  2  2     9.56769239e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.79775204e-01   # V_{1,1}
  1  2    -2.00101347e-01   # V_{1,2}
  2  1     2.00101347e-01   # V_{2,1}
  2  2     9.79775204e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.33437806e-01   # F_{11}
  1  2     9.72371735e-01   # F_{12}
  2  1     9.72371735e-01   # F_{21}
  2  2    -2.33437806e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.99109442e-01   # F_{11}
  1  2     4.21938772e-02   # F_{12}
  2  1    -4.21938772e-02   # F_{21}
  2  2     9.99109442e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.38306995e-01   # F_{11}
  1  2     9.90389406e-01   # F_{12}
  2  1     9.90389406e-01   # F_{21}
  2  2    -1.38306995e-01   # F_{22}
Block gauge Q= 1.11566663e+03  # SM gauge couplings
     1     3.62447046e-01   # g'(Q)MSSM DRbar
     2     6.41727462e-01   # g(Q)MSSM DRbar
     3     1.05155876e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.11566663e+03  
  3  3     8.57595319e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.11566663e+03  
  3  3     1.35240683e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.11566663e+03  
  3  3     9.95315426e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.11566663e+03 # Higgs mixing parameters
     1     6.24258645e+02    # mu(Q)MSSM DRbar
     2     9.64097846e+00    # tan beta(Q)MSSM DRbar
     3     2.43616244e+02    # higgs vev(Q)MSSM DRbar
     4     1.58755376e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.11566663e+03  # MSSM DRbar SUSY breaking parameters
     1     2.10763126e+02      # M_1(Q)
     2     3.89834487e+02      # M_2(Q)
     3     1.10030636e+03      # M_3(Q)
    21     1.14795994e+06      # mH1^2(Q)
    22    -3.54209984e+05      # mH2^2(Q)
    31     1.09541669e+03      # meL(Q)
    32     1.09540184e+03      # mmuL(Q)
    33     1.09097932e+03      # mtauL(Q)
    34     1.06371542e+03      # meR(Q)
    35     1.06368468e+03      # mmuR(Q)
    36     1.05450939e+03      # mtauR(Q)
    41     1.42927295e+03      # mqL1(Q)
    42     1.42926774e+03      # mqL2(Q)
    43     1.24150025e+03      # mqL3(Q)
    44     1.40576242e+03      # muR(Q)
    45     1.40575679e+03      # mcR(Q)
    46     9.92271421e+02      # mtR(Q)
    47     1.40300834e+03      # mdR(Q)
    48     1.40300328e+03      # msR(Q)
    49     1.39328728e+03      # mbR(Q)
Block au Q= 1.11566663e+03  
  1  1    -1.11909692e+03      # Au(Q)MSSM DRbar
  2  2    -1.11909194e+03      # Ac(Q)MSSM DRbar
  3  3    -8.63760091e+02      # At(Q)MSSM DRbar
Block ad Q= 1.11566663e+03  
  1  1    -1.36841148e+03      # Ad(Q)MSSM DRbar
  2  2    -1.36840688e+03      # As(Q)MSSM DRbar
  3  3    -1.27872595e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.11566663e+03  
  1  1    -2.97202983e+02      # Ae(Q)MSSM DRbar
  2  2    -2.97197693e+02      # Amu(Q)MSSM DRbar
  3  3    -2.95625520e+02      # Atau(Q)MSSM DRbar
