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
     1    3.50000000e+02   # m0
     2    5.25000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.92108488e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03913899e+01   # MW
        25     1.15297387e+02   # h0
        35     8.15902858e+02   # H0
        36     8.15585856e+02   # A0
        37     8.19872946e+02   # H+
   1000021     1.20810708e+03   # ~g
   1000022     2.15976041e+02   # ~neutralino(1)
   1000023     4.08473733e+02   # ~neutralino(2)
   1000024     4.08624544e+02   # ~chargino(1)
   1000025    -6.63411439e+02   # ~neutralino(3)
   1000035     6.76830220e+02   # ~neutralino(4)
   1000037     6.76435484e+02   # ~chargino(2)
   1000001     1.14878471e+03   # ~d_L
   1000002     1.14621191e+03   # ~u_L
   1000003     1.14878173e+03   # ~s_L
   1000004     1.14620892e+03   # ~c_L
   1000005     1.04380194e+03   # ~b_1
   1000006     8.66979367e+02   # ~t_1
   1000011     4.97825728e+02   # ~e_L
   1000012     4.91315888e+02   # ~nue_L
   1000013     4.98006535e+02   # ~mu_L
   1000014     4.91310276e+02   # ~numu_L
   1000015     3.96933619e+02   # ~stau_1
   1000016     4.89492850e+02   # ~nu_tau_L
   2000001     1.10440019e+03   # ~d_R
   2000002     1.10783224e+03   # ~u_R
   2000003     1.10439711e+03   # ~s_R
   2000004     1.10782904e+03   # ~c_R
   2000005     1.09966962e+03   # ~b_2
   2000006     1.08358892e+03   # ~t_2
   2000011     4.03407219e+02   # ~e_R
   2000013     4.03393363e+02   # ~mu_R
   2000015     4.97674848e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06062797e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96139706e-01   # N_{1,1}
  1  2    -1.60289305e-02   # N_{1,2}
  1  3     7.96054097e-02   # N_{1,3}
  1  4    -3.33427433e-02   # N_{1,4}
  2  1     3.54457713e-02   # N_{2,1}
  2  2     9.71804385e-01   # N_{2,2}
  2  3    -1.93302407e-01   # N_{2,3}
  2  4     1.30284358e-01   # N_{2,4}
  3  1    -3.17918541e-02   # N_{3,1}
  3  2     4.61995797e-02   # N_{3,2}
  3  3     7.03765146e-01   # N_{3,3}
  3  4     7.08215713e-01   # N_{3,4}
  4  1    -7.37466046e-02   # N_{4,1}
  4  2     2.30661894e-01   # N_{4,2}
  4  3     6.78978480e-01   # N_{4,3}
  4  4    -6.93069082e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.61825001e-01   # U_{1,1}
  1  2    -2.73665246e-01   # U_{1,2}
  2  1     2.73665246e-01   # U_{2,1}
  2  2     9.61825001e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.82449481e-01   # V_{1,1}
  1  2    -1.86528866e-01   # V_{1,2}
  2  1     1.86528866e-01   # V_{2,1}
  2  2     9.82449481e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.89064123e-01   # F_{11}
  1  2     9.21210675e-01   # F_{12}
  2  1     9.21210675e-01   # F_{21}
  2  2    -3.89064123e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.87749877e-01   # F_{11}
  1  2     1.56045442e-01   # F_{12}
  2  1    -1.56045442e-01   # F_{21}
  2  2     9.87749877e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.34529110e-01   # F_{11}
  1  2     9.90909642e-01   # F_{12}
  2  1     9.90909642e-01   # F_{21}
  2  2    -1.34529110e-01   # F_{22}
Block gauge Q= 9.39920310e+02  # SM gauge couplings
     1     3.62387503e-01   # g'(Q)MSSM DRbar
     2     6.42470894e-01   # g(Q)MSSM DRbar
     3     1.05745852e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.39920310e+02  
  3  3     8.59270777e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.39920310e+02  
  3  3     1.35018062e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.39920310e+02  
  3  3     1.00375920e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.39920310e+02 # Higgs mixing parameters
     1     6.57686057e+02    # mu(Q)MSSM DRbar
     2     9.66449065e+00    # tan beta(Q)MSSM DRbar
     3     2.43998492e+02    # higgs vev(Q)MSSM DRbar
     4     6.87488382e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.39920310e+02  # MSSM DRbar SUSY breaking parameters
     1     2.20289819e+02      # M_1(Q)
     2     4.08424624e+02      # M_2(Q)
     3     1.16420331e+03      # M_3(Q)
    21     2.20911218e+05      # mH1^2(Q)
    22    -4.16086022e+05      # mH2^2(Q)
    31     4.92147386e+02      # meL(Q)
    32     4.92141765e+02      # mmuL(Q)
    33     4.90446962e+02      # mtauL(Q)
    34     3.98919552e+02      # meR(Q)
    35     3.98905544e+02      # mmuR(Q)
    36     3.94665838e+02      # mtauR(Q)
    41     1.11013238e+03      # mqL1(Q)
    42     1.11012933e+03      # mqL2(Q)
    43     1.01405244e+03      # mqL3(Q)
    44     1.07219943e+03      # muR(Q)
    45     1.07219617e+03      # mcR(Q)
    46     8.63106823e+02      # mtR(Q)
    47     1.06761712e+03      # mdR(Q)
    48     1.06761397e+03      # msR(Q)
    49     1.06183478e+03      # mbR(Q)
Block au Q= 9.39920310e+02  
  1  1    -1.19008661e+03      # Au(Q)MSSM DRbar
  2  2    -1.19008128e+03      # Ac(Q)MSSM DRbar
  3  3    -9.18732057e+02      # At(Q)MSSM DRbar
Block ad Q= 9.39920310e+02  
  1  1    -1.45535892e+03      # Ad(Q)MSSM DRbar
  2  2    -1.45535399e+03      # As(Q)MSSM DRbar
  3  3    -1.36008662e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.39920310e+02  
  1  1    -3.13562825e+02      # Ae(Q)MSSM DRbar
  2  2    -3.13557208e+02      # Amu(Q)MSSM DRbar
  3  3    -3.11865505e+02      # Atau(Q)MSSM DRbar
