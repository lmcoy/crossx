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
     1    1.30000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03951210e+01   # MW
        25     1.14403107e+02   # h0
        35     8.71086923e+02   # H0
        36     8.71042937e+02   # A0
        37     8.74946939e+02   # H+
   1000021     9.90133574e+02   # ~g
   1000022     1.72902342e+02   # ~neutralino(1)
   1000023     3.33149632e+02   # ~neutralino(2)
   1000024     3.33293524e+02   # ~chargino(1)
   1000025    -6.91159357e+02   # ~neutralino(3)
   1000035     6.99102710e+02   # ~neutralino(4)
   1000037     6.99524110e+02   # ~chargino(2)
   1000039     3.08100000e+00   # ~gravitino
   1000001     1.21005853e+03   # ~d_L
   1000002     1.20762020e+03   # ~u_L
   1000003     1.21005371e+03   # ~s_L
   1000004     1.20761537e+03   # ~c_L
   1000005     1.06914444e+03   # ~b_1
   1000006     8.50668476e+02   # ~t_1
   1000011     5.80412401e+02   # ~e_L
   1000012     5.74673042e+02   # ~nue_L
   1000013     5.80512757e+02   # ~mu_L
   1000014     5.74660593e+02   # ~numu_L
   1000015     3.79739516e+02   # ~stau_1
   1000016     5.70604593e+02   # ~nu_tau_L
   2000001     1.08954962e+03   # ~d_R
   2000002     1.11106210e+03   # ~u_R
   2000003     1.08954245e+03   # ~s_R
   2000004     1.11105858e+03   # ~c_R
   2000005     1.09738327e+03   # ~b_2
   2000006     1.11162479e+03   # ~t_2
   2000011     3.93866344e+02   # ~e_R
   2000013     3.93829728e+02   # ~mu_R
   2000015     5.77952072e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.04403400e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97077509e-01   # N_{1,1}
  1  2    -1.30604027e-02   # N_{1,2}
  1  3     7.17482881e-02   # N_{1,3}
  1  4    -2.27607060e-02   # N_{1,4}
  2  1     2.54560807e-02   # N_{2,1}
  2  2     9.85288708e-01   # N_{2,2}
  2  3    -1.49281503e-01   # N_{2,3}
  2  4     7.92034278e-02   # N_{2,4}
  3  1    -3.38047471e-02   # N_{3,1}
  3  2     5.05600882e-02   # N_{3,2}
  3  3     7.03584260e-01   # N_{3,3}
  3  4     7.08004312e-01   # N_{3,4}
  4  1    -6.36055637e-02   # N_{4,1}
  4  2     1.62724508e-01   # N_{4,2}
  4  3     6.91040090e-01   # N_{4,3}
  4  4    -7.01383391e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.77692337e-01   # U_{1,1}
  1  2    -2.10042127e-01   # U_{1,2}
  2  1     2.10042127e-01   # U_{2,1}
  2  2     9.77692337e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.93582295e-01   # V_{1,1}
  1  2    -1.13111553e-01   # V_{1,2}
  2  1     1.13111553e-01   # V_{2,1}
  2  2     9.93582295e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.26383239e-01   # F_{11}
  1  2     9.74038310e-01   # F_{12}
  2  1     9.74038310e-01   # F_{21}
  2  2    -2.26383239e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.87342452e-01   # F_{11}
  1  2     8.73210933e-01   # F_{12}
  2  1     8.73210933e-01   # F_{21}
  2  2    -4.87342452e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.70824252e-02   # F_{11}
  1  2     9.95276345e-01   # F_{12}
  2  1     9.95276345e-01   # F_{21}
  2  2    -9.70824252e-02   # F_{22}
Block gauge Q= 9.43683879e+02  # SM gauge couplings
     1     3.62399190e-01   # g'(Q)MSSM DRbar
     2     6.42748105e-01   # g(Q)MSSM DRbar
     3     1.06134245e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.43683879e+02  
  3  3     8.60653808e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.43683879e+02  
  3  3     1.98830333e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.43683879e+02  
  3  3     1.50885827e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.43683879e+02 # Higgs mixing parameters
     1     6.84909976e+02    # mu(Q)MSSM DRbar
     2     1.45125611e+01    # tan beta(Q)MSSM DRbar
     3     2.44038677e+02    # higgs vev(Q)MSSM DRbar
     4     7.92511924e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.43683879e+02  # MSSM DRbar SUSY breaking parameters
     1     1.76027569e+02      # M_1(Q)
     2     3.27345245e+02      # M_2(Q)
     3     9.09165521e+02      # M_3(Q)
    21     2.83669543e+05      # mH1^2(Q)
    22    -4.55271926e+05      # mH2^2(Q)
    31     5.76897749e+02      # meL(Q)
    32     5.76885342e+02      # mmuL(Q)
    33     5.73106747e+02      # mtauL(Q)
    34     3.88976069e+02      # meR(Q)
    35     3.88939016e+02      # mmuR(Q)
    36     3.77520528e+02      # mtauR(Q)
    41     1.18162698e+03      # mqL1(Q)
    42     1.18162202e+03      # mqL2(Q)
    43     1.06625958e+03      # mqL3(Q)
    44     1.08331088e+03      # muR(Q)
    45     1.08330724e+03      # mcR(Q)
    46     8.21695569e+02      # mtR(Q)
    47     1.05972390e+03      # mdR(Q)
    48     1.05971647e+03      # msR(Q)
    49     1.04613411e+03      # mbR(Q)
Block au Q= 9.43683879e+02  
  1  1    -8.49418677e+02      # Au(Q)MSSM DRbar
  2  2    -8.49414371e+02      # Ac(Q)MSSM DRbar
  3  3    -6.74478326e+02      # At(Q)MSSM DRbar
Block ad Q= 9.43683879e+02  
  1  1    -1.01629588e+03      # Ad(Q)MSSM DRbar
  2  2    -1.01628991e+03      # As(Q)MSSM DRbar
  3  3    -9.50416709e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.43683879e+02  
  1  1    -1.86648946e+02      # Ae(Q)MSSM DRbar
  2  2    -1.86642488e+02      # Amu(Q)MSSM DRbar
  3  3    -1.84681059e+02      # Atau(Q)MSSM DRbar
