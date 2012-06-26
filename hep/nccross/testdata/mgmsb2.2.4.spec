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
     1    1.50000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03935592e+01   # MW
        25     1.15375656e+02   # h0
        35     9.96034428e+02   # H0
        36     9.95989675e+02   # A0
        37     9.99429977e+02   # H+
   1000021     1.12717797e+03   # ~g
   1000022     2.00227435e+02   # ~neutralino(1)
   1000023     3.85865623e+02   # ~neutralino(2)
   1000024     3.86025917e+02   # ~chargino(1)
   1000025    -7.85301592e+02   # ~neutralino(3)
   1000035     7.92473207e+02   # ~neutralino(4)
   1000037     7.92845094e+02   # ~chargino(2)
   1000039     3.55500000e+00   # ~gravitino
   1000001     1.38332557e+03   # ~d_L
   1000002     1.38121547e+03   # ~u_L
   1000003     1.38332008e+03   # ~s_L
   1000004     1.38120998e+03   # ~c_L
   1000005     1.22282125e+03   # ~b_1
   1000006     9.72540775e+02   # ~t_1
   1000011     6.66661785e+02   # ~e_L
   1000012     6.61638072e+02   # ~nue_L
   1000013     6.66754828e+02   # ~mu_L
   1000014     6.61623872e+02   # ~numu_L
   1000015     4.37461444e+02   # ~stau_1
   1000016     6.56993798e+02   # ~nu_tau_L
   2000001     1.24421110e+03   # ~d_R
   2000002     1.26945642e+03   # ~u_R
   2000003     1.24420295e+03   # ~s_R
   2000004     1.26945240e+03   # ~c_R
   2000005     1.25312399e+03   # ~b_2
   2000006     1.26540461e+03   # ~t_2
   2000011     4.52932884e+02   # ~e_R
   2000013     4.52891075e+02   # ~mu_R
   2000015     6.63395397e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.01806351e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97757799e-01   # N_{1,1}
  1  2    -1.00941155e-02   # N_{1,2}
  1  3     6.29829792e-02   # N_{1,3}
  1  4    -2.02639426e-02   # N_{1,4}
  2  1     1.98753628e-02   # N_{2,1}
  2  2     9.88260795e-01   # N_{2,2}
  2  3    -1.33362003e-01   # N_{2,3}
  2  4     7.18341644e-02   # N_{2,4}
  3  1    -2.96429400e-02   # N_{3,1}
  3  2     4.42046694e-02   # N_{3,2}
  3  3     7.04404696e-01   # N_{3,3}
  3  4     7.07800302e-01   # N_{3,4}
  4  1    -5.66183740e-02   # N_{4,1}
  4  2     1.45892621e-01   # N_{4,2}
  4  3     6.94306665e-01   # N_{4,3}
  4  4    -7.02458509e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.82289781e-01   # U_{1,1}
  1  2    -1.87368049e-01   # U_{1,2}
  2  1     1.87368049e-01   # U_{2,1}
  2  2     9.82289781e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.94743258e-01   # V_{1,1}
  1  2    -1.02400447e-01   # V_{1,2}
  2  1     1.02400447e-01   # V_{2,1}
  2  2     9.94743258e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     1.98682484e-01   # F_{11}
  1  2     9.80063912e-01   # F_{12}
  2  1     9.80063912e-01   # F_{21}
  2  2    -1.98682484e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.37513511e-01   # F_{11}
  1  2     8.99211837e-01   # F_{12}
  2  1     8.99211837e-01   # F_{21}
  2  2    -4.37513511e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     8.40793697e-02   # F_{11}
  1  2     9.96459061e-01   # F_{12}
  2  1     9.96459061e-01   # F_{21}
  2  2    -8.40793697e-02   # F_{22}
Block gauge Q= 1.07749911e+03  # SM gauge couplings
     1     3.62678733e-01   # g'(Q)MSSM DRbar
     2     6.42042375e-01   # g(Q)MSSM DRbar
     3     1.05440310e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.07749911e+03  
  3  3     8.56103976e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.07749911e+03  
  3  3     1.97541622e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.07749911e+03  
  3  3     1.50751218e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.07749911e+03 # Higgs mixing parameters
     1     7.79011790e+02    # mu(Q)MSSM DRbar
     2     1.44898955e+01    # tan beta(Q)MSSM DRbar
     3     2.43876390e+02    # higgs vev(Q)MSSM DRbar
     4     1.03567604e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.07749911e+03  # MSSM DRbar SUSY breaking parameters
     1     2.03514882e+02      # M_1(Q)
     2     3.77146351e+02      # M_2(Q)
     3     1.03575640e+03      # M_3(Q)
    21     3.75816846e+05      # mH1^2(Q)
    22    -5.87029250e+05      # mH2^2(Q)
    31     6.63035888e+02      # meL(Q)
    32     6.63021713e+02      # mmuL(Q)
    33     6.58698213e+02      # mtauL(Q)
    34     4.47993471e+02      # meR(Q)
    35     4.47951228e+02      # mmuR(Q)
    36     4.34915349e+02      # mtauR(Q)
    41     1.35162526e+03      # mqL1(Q)
    42     1.35161962e+03      # mqL2(Q)
    43     1.22016657e+03      # mqL3(Q)
    44     1.23816802e+03      # muR(Q)
    45     1.23816386e+03      # mcR(Q)
    46     9.39806858e+02      # mtR(Q)
    47     1.21078546e+03      # mdR(Q)
    48     1.21077700e+03      # msR(Q)
    49     1.19535148e+03      # mbR(Q)
Block au Q= 1.07749911e+03  
  1  1    -9.62107481e+02      # Au(Q)MSSM DRbar
  2  2    -9.62102638e+02      # Ac(Q)MSSM DRbar
  3  3    -7.65542235e+02      # At(Q)MSSM DRbar
Block ad Q= 1.07749911e+03  
  1  1    -1.14931412e+03      # Ad(Q)MSSM DRbar
  2  2    -1.14930743e+03      # As(Q)MSSM DRbar
  3  3    -1.07531631e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.07749911e+03  
  1  1    -2.13502133e+02      # Ae(Q)MSSM DRbar
  2  2    -2.13494808e+02      # Amu(Q)MSSM DRbar
  3  3    -2.11266837e+02      # Atau(Q)MSSM DRbar
