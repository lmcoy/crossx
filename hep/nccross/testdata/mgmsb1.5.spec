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
     1    5.50000000e+04   # lambda
     2    1.10000000e+05   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.10000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03977206e+01   # MW
        25     1.13489776e+02   # h0
        35     5.21244378e+02   # H0
        36     5.20987537e+02   # A0
        37     5.27360557e+02   # H+
   1000021     1.26128666e+03   # ~g
   1000022     2.28536471e+02   # ~neutralino(1)
   1000023     3.75252534e+02   # ~neutralino(2)
   1000024     3.73000049e+02   # ~chargino(1)
   1000025    -4.13421651e+02   # ~neutralino(3)
   1000035     4.99920151e+02   # ~neutralino(4)
   1000037     4.98421211e+02   # ~chargino(2)
   1000039     1.43385000e-09   # ~gravitino
   1000001     1.20488621e+03   # ~d_L
   1000002     1.20241052e+03   # ~u_L
   1000003     1.20488470e+03   # ~s_L
   1000004     1.20240901e+03   # ~c_L
   1000005     1.14758217e+03   # ~b_1
   1000006     1.07334741e+03   # ~t_1
   1000011     3.57159403e+02   # ~e_L
   1000012     3.47956648e+02   # ~nue_L
   1000013     3.57168207e+02   # ~mu_L
   1000014     3.47955166e+02   # ~numu_L
   1000015     1.70021948e+02   # ~stau_1
   1000016     3.47279000e+02   # ~nu_tau_L
   2000001     1.15609433e+03   # ~d_R
   2000002     1.15885454e+03   # ~u_R
   2000003     1.15609223e+03   # ~s_R
   2000004     1.15885346e+03   # ~c_R
   2000005     1.16444207e+03   # ~b_2
   2000006     1.17679296e+03   # ~t_2
   2000011     1.75958490e+02   # ~e_R
   2000013     1.75952536e+02   # ~mu_R
   2000015     3.58174020e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.44797008e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.79046551e-01   # N_{1,1}
  1  2    -3.93572439e-02   # N_{1,2}
  1  3     1.70883330e-01   # N_{1,3}
  1  4    -1.03526546e-01   # N_{1,4}
  2  1    -1.83675851e-01   # N_{2,1}
  2  2    -5.63345381e-01   # N_{2,2}
  2  3     5.90917888e-01   # N_{2,3}
  2  4    -5.47468002e-01   # N_{2,4}
  3  1    -4.48679497e-02   # N_{3,1}
  3  2     6.02068345e-02   # N_{3,2}
  3  3     7.00739851e-01   # N_{3,3}
  3  4     7.09454485e-01   # N_{3,4}
  4  1    -7.56167927e-02   # N_{4,1}
  4  2     8.23084519e-01   # N_{4,2}
  4  3     3.61356610e-01   # N_{4,3}
  4  4    -4.31549969e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.08193970e-01   # U_{1,1}
  1  2     8.61242642e-01   # U_{1,2}
  2  1    -8.61242642e-01   # U_{2,1}
  2  2    -5.08193970e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.04390729e-01   # V_{1,1}
  1  2     7.96688049e-01   # V_{1,2}
  2  1    -7.96688049e-01   # V_{2,1}
  2  2    -6.04390729e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.84785514e-01   # F_{11}
  1  2     9.58591264e-01   # F_{12}
  2  1     9.58591264e-01   # F_{21}
  2  2    -2.84785514e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.68726357e-01   # F_{11}
  1  2     8.83343423e-01   # F_{12}
  2  1     8.83343423e-01   # F_{21}
  2  2    -4.68726357e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.09717737e-01   # F_{11}
  1  2     9.93962785e-01   # F_{12}
  2  1     9.93962785e-01   # F_{21}
  2  2    -1.09717737e-01   # F_{22}
Block gauge Q= 1.09054318e+03  # SM gauge couplings
     1     3.63266657e-01   # g'(Q)MSSM DRbar
     2     6.43389051e-01   # g(Q)MSSM DRbar
     3     1.05266427e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.09054318e+03  
  3  3     8.58400582e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.09054318e+03  
  3  3     2.03114469e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.09054318e+03  
  3  3     1.51779851e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.09054318e+03 # Higgs mixing parameters
     1     4.04656210e+02    # mu(Q)MSSM DRbar
     2     1.44866942e+01    # tan beta(Q)MSSM DRbar
     3     2.43590011e+02    # higgs vev(Q)MSSM DRbar
     4     3.09094969e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.09054318e+03  # MSSM DRbar SUSY breaking parameters
     1     2.38807722e+02      # M_1(Q)
     2     4.47855596e+02      # M_2(Q)
     3     1.20463514e+03      # M_3(Q)
    21     1.05465611e+05      # mH1^2(Q)
    22    -1.42401483e+05      # mH2^2(Q)
    31     3.47477648e+02      # meL(Q)
    32     3.47476168e+02      # mmuL(Q)
    33     3.47020264e+02      # mtauL(Q)
    34     1.64107926e+02      # meR(Q)
    35     1.64101557e+02      # mmuR(Q)
    36     1.62129230e+02      # mtauR(Q)
    41     1.16012032e+03      # mqL1(Q)
    42     1.16011876e+03      # mqL2(Q)
    43     1.12328665e+03      # mqL3(Q)
    44     1.11707423e+03      # muR(Q)
    45     1.11707312e+03      # mcR(Q)
    46     1.04218024e+03      # mtR(Q)
    47     1.11313348e+03      # mdR(Q)
    48     1.11313132e+03      # msR(Q)
    49     1.10893830e+03      # mbR(Q)
Block au Q= 1.09054318e+03  
  1  1    -3.61151887e+02      # Au(Q)MSSM DRbar
  2  2    -3.61151380e+02      # Ac(Q)MSSM DRbar
  3  3    -3.40561839e+02      # At(Q)MSSM DRbar
Block ad Q= 1.09054318e+03  
  1  1    -3.83971693e+02      # Ad(Q)MSSM DRbar
  2  2    -3.83970987e+02      # As(Q)MSSM DRbar
  3  3    -3.76215691e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.09054318e+03  
  1  1    -3.76460826e+01      # Ae(Q)MSSM DRbar
  2  2    -3.76458083e+01      # Amu(Q)MSSM DRbar
  3  3    -3.75613797e+01      # Atau(Q)MSSM DRbar
