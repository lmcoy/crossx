# SOFTSUSY3.3.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.1       # version number
     3   # Warning: stau LSP
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
     1    3.90000000e+02   # m0
     2    7.00000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.67406876e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03878721e+01   # MW
        25     1.18668374e+02   # h0
        35     7.97649324e+02   # H0
        36     7.97544605e+02   # A0
        37     8.01868977e+02   # H+
   1000021     1.57089388e+03   # ~g
   1000022     2.94222857e+02   # ~neutralino(1)
   1000023     5.59323163e+02   # ~neutralino(2)
   1000024     5.59422318e+02   # ~chargino(1)
   1000025    -9.12504325e+02   # ~neutralino(3)
   1000035     9.19985632e+02   # ~neutralino(4)
   1000037     9.20324740e+02   # ~chargino(2)
   1000001     1.47779631e+03   # ~d_L
   1000002     1.47579169e+03   # ~u_L
   1000003     1.47775660e+03   # ~s_L
   1000004     1.47575191e+03   # ~c_L
   1000005     1.25302213e+03   # ~b_1
   1000006     1.08842597e+03   # ~t_1
   1000011     6.10375748e+02   # ~e_L
   1000012     6.04953963e+02   # ~nue_L
   1000013     6.10393192e+02   # ~mu_L
   1000014     6.04809186e+02   # ~numu_L
   1000015     2.93114778e+02   # ~stau_1
   1000016     5.54503188e+02   # ~nu_tau_L
   2000001     1.41689770e+03   # ~d_R
   2000002     1.42222005e+03   # ~u_R
   2000003     1.41681867e+03   # ~s_R
   2000004     1.42221501e+03   # ~c_R
   2000005     1.31880055e+03   # ~b_2
   2000006     1.31750870e+03   # ~t_2
   2000011     4.71612958e+02   # ~e_R
   2000013     4.71235513e+02   # ~mu_R
   2000015     5.78438573e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59815059e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98236397e-01   # N_{1,1}
  1  2    -6.14452531e-03   # N_{1,2}
  1  3     5.57141083e-02   # N_{1,3}
  1  4    -1.95519466e-02   # N_{1,4}
  2  1     1.53990956e-02   # N_{2,1}
  2  2     9.86732576e-01   # N_{2,2}
  2  3    -1.36982209e-01   # N_{2,3}
  2  4     8.57762565e-02   # N_{2,4}
  3  1    -2.52720715e-02   # N_{3,1}
  3  2     3.67782288e-02   # N_{3,2}
  3  3     7.05185482e-01   # N_{3,3}
  3  4     7.07617213e-01   # N_{3,4}
  4  1    -5.14614995e-02   # N_{4,1}
  4  2     1.58014020e-01   # N_{4,2}
  4  3     6.93430060e-01   # N_{4,3}
  4  4    -7.01097736e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.81195897e-01   # U_{1,1}
  1  2    -1.93014537e-01   # U_{1,2}
  2  1     1.93014537e-01   # U_{2,1}
  2  2     9.81195897e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.92429782e-01   # V_{1,1}
  1  2    -1.22813383e-01   # V_{1,2}
  2  1     1.22813383e-01   # V_{2,1}
  2  2     9.92429782e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.01218110e-01   # F_{11}
  1  2     9.15982548e-01   # F_{12}
  2  1     9.15982548e-01   # F_{21}
  2  2    -4.01218110e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.06143673e-01   # F_{11}
  1  2     5.91719849e-01   # F_{12}
  2  1    -5.91719849e-01   # F_{21}
  2  2     8.06143673e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.87585532e-01   # F_{11}
  1  2     9.57754959e-01   # F_{12}
  2  1     9.57754959e-01   # F_{21}
  2  2    -2.87585532e-01   # F_{22}
Block gauge Q= 1.16477812e+03  # SM gauge couplings
     1     3.62838796e-01   # g'(Q)MSSM DRbar
     2     6.40789545e-01   # g(Q)MSSM DRbar
     3     1.04507387e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.16477812e+03  
  3  3     8.45783527e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.16477812e+03  
  3  3     4.89386829e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.16477812e+03  
  3  3     4.27961220e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.16477812e+03 # Higgs mixing parameters
     1     9.09582350e+02    # mu(Q)MSSM DRbar
     2     3.91594967e+01    # tan beta(Q)MSSM DRbar
     3     2.43663611e+02    # higgs vev(Q)MSSM DRbar
     4     8.11665666e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.16477812e+03  # MSSM DRbar SUSY breaking parameters
     1     2.98763070e+02      # M_1(Q)
     2     5.50320309e+02      # M_2(Q)
     3     1.52736316e+03      # M_3(Q)
    21    -1.79305835e+05      # mH1^2(Q)
    22    -8.09944326e+05      # mH2^2(Q)
    31     6.03174848e+02      # meL(Q)
    32     6.03029150e+02      # mmuL(Q)
    33     5.56015000e+02      # mtauL(Q)
    34     4.66340274e+02      # meR(Q)
    35     4.65958489e+02      # mmuR(Q)
    36     3.26016238e+02      # mtauR(Q)
    41     1.43150762e+03      # mqL1(Q)
    42     1.43146716e+03      # mqL2(Q)
    43     1.24318468e+03      # mqL3(Q)
    44     1.37920035e+03      # muR(Q)
    45     1.37919523e+03      # mcR(Q)
    46     1.08719944e+03      # mtR(Q)
    47     1.37282263e+03      # mdR(Q)
    48     1.37274233e+03      # msR(Q)
    49     1.25721055e+03      # mbR(Q)
Block au Q= 1.16477812e+03  
  1  1    -1.88756517e+03      # Au(Q)MSSM DRbar
  2  2    -1.88752147e+03      # Ac(Q)MSSM DRbar
  3  3    -1.33471559e+03      # At(Q)MSSM DRbar
Block ad Q= 1.16477812e+03  
  1  1    -2.17634242e+03      # Ad(Q)MSSM DRbar
  2  2    -2.17623115e+03      # As(Q)MSSM DRbar
  3  3    -1.84333180e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.16477812e+03  
  1  1    -7.06542636e+02      # Ae(Q)MSSM DRbar
  2  2    -7.06203196e+02      # Amu(Q)MSSM DRbar
  3  3    -5.92097548e+02      # Atau(Q)MSSM DRbar
