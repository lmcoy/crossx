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
     1    2.75000000e+02   # m0
     2    6.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.75139158e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03894950e+01   # MW
        25     1.16615915e+02   # h0
        35     9.39009374e+02   # H0
        36     9.38775357e+02   # A0
        37     9.42444990e+02   # H+
   1000021     1.46443243e+03   # ~g
   1000022     2.69953475e+02   # ~neutralino(1)
   1000023     5.10915569e+02   # ~neutralino(2)
   1000024     5.11108439e+02   # ~chargino(1)
   1000025    -8.00119238e+02   # ~neutralino(3)
   1000035     8.12042870e+02   # ~neutralino(4)
   1000037     8.11671494e+02   # ~chargino(2)
   1000001     1.35948583e+03   # ~d_L
   1000002     1.35733580e+03   # ~u_L
   1000003     1.35948248e+03   # ~s_L
   1000004     1.35733244e+03   # ~c_L
   1000005     1.24286157e+03   # ~b_1
   1000006     1.04354071e+03   # ~t_1
   1000011     5.16403665e+02   # ~e_L
   1000012     5.10152747e+02   # ~nue_L
   1000013     5.16519531e+02   # ~mu_L
   1000014     5.10147609e+02   # ~numu_L
   1000015     3.62832981e+02   # ~stau_1
   1000016     5.08411121e+02   # ~nu_tau_L
   2000001     1.30209182e+03   # ~d_R
   2000002     1.30699450e+03   # ~u_R
   2000003     1.30208833e+03   # ~s_R
   2000004     1.30699089e+03   # ~c_R
   2000005     1.29667761e+03   # ~b_2
   2000006     1.27890093e+03   # ~t_2
   2000011     3.69707368e+02   # ~e_R
   2000013     3.69692973e+02   # ~mu_R
   2000015     5.16216228e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05586082e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97354152e-01   # N_{1,1}
  1  2    -1.10124658e-02   # N_{1,2}
  1  3     6.60194554e-02   # N_{1,3}
  1  4    -2.83699244e-02   # N_{1,4}
  2  1     2.53562858e-02   # N_{2,1}
  2  2     9.78191888e-01   # N_{2,2}
  2  3    -1.69412918e-01   # N_{2,3}
  2  4     1.17460431e-01   # N_{2,4}
  3  1    -2.61050791e-02   # N_{3,1}
  3  2     3.77495478e-02   # N_{3,2}
  3  3     7.04851385e-01   # N_{3,3}
  3  4     7.07868647e-01   # N_{3,4}
  4  1    -6.29307487e-02   # N_{4,1}
  4  2     2.03946876e-01   # N_{4,2}
  4  3     6.85656779e-01   # N_{4,3}
  4  4    -6.95931156e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.70999487e-01   # U_{1,1}
  1  2    -2.39081568e-01   # U_{1,2}
  2  1     2.39081568e-01   # U_{2,1}
  2  2     9.70999487e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.85881758e-01   # V_{1,1}
  1  2    -1.67443004e-01   # V_{1,2}
  2  1     1.67443004e-01   # V_{2,1}
  2  2     9.85881758e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.57271425e-01   # F_{11}
  1  2     9.34000604e-01   # F_{12}
  2  1     9.34000604e-01   # F_{21}
  2  2    -3.57271425e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.86597237e-01   # F_{11}
  1  2     1.63174423e-01   # F_{12}
  2  1    -1.63174423e-01   # F_{21}
  2  2     9.86597237e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.08361344e-01   # F_{11}
  1  2     9.94111573e-01   # F_{12}
  2  1     9.94111573e-01   # F_{21}
  2  2    -1.08361344e-01   # F_{22}
Block gauge Q= 1.12142728e+03  # SM gauge couplings
     1     3.62860703e-01   # g'(Q)MSSM DRbar
     2     6.41578767e-01   # g(Q)MSSM DRbar
     3     1.04796771e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.12142728e+03  
  3  3     8.52862806e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.12142728e+03  
  3  3     1.33654844e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.12142728e+03  
  3  3     1.00334073e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.12142728e+03 # Higgs mixing parameters
     1     7.94553488e+02    # mu(Q)MSSM DRbar
     2     9.64402589e+00    # tan beta(Q)MSSM DRbar
     3     2.43806007e+02    # higgs vev(Q)MSSM DRbar
     4     9.12028430e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.12142728e+03  # MSSM DRbar SUSY breaking parameters
     1     2.75204834e+02      # M_1(Q)
     2     5.07734841e+02      # M_2(Q)
     3     1.42104284e+03      # M_3(Q)
    21     2.31195428e+05      # mH1^2(Q)
    22    -6.06376765e+05      # mH2^2(Q)
    31     5.08704614e+02      # meL(Q)
    32     5.08699449e+02      # mmuL(Q)
    33     5.07137166e+02      # mtauL(Q)
    34     3.63443543e+02      # meR(Q)
    35     3.63428889e+02      # mmuR(Q)
    36     3.58974661e+02      # mtauR(Q)
    41     1.31385516e+03      # mqL1(Q)
    42     1.31385174e+03      # mqL2(Q)
    43     1.20820230e+03      # mqL3(Q)
    44     1.26459370e+03      # muR(Q)
    45     1.26459003e+03      # mcR(Q)
    46     1.03463445e+03      # mtR(Q)
    47     1.25856636e+03      # mdR(Q)
    48     1.25856282e+03      # msR(Q)
    49     1.25209236e+03      # mbR(Q)
Block au Q= 1.12142728e+03  
  1  1    -1.44250827e+03      # Au(Q)MSSM DRbar
  2  2    -1.44250187e+03      # Ac(Q)MSSM DRbar
  3  3    -1.11730215e+03      # At(Q)MSSM DRbar
Block ad Q= 1.12142728e+03  
  1  1    -1.75968755e+03      # Ad(Q)MSSM DRbar
  2  2    -1.75968163e+03      # As(Q)MSSM DRbar
  3  3    -1.64554804e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.12142728e+03  
  1  1    -3.84634734e+02      # Ae(Q)MSSM DRbar
  2  2    -3.84627930e+02      # Amu(Q)MSSM DRbar
  3  3    -3.82570712e+02      # Atau(Q)MSSM DRbar
