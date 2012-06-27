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
     1    2.25000000e+02   # m0
     2    5.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.84665354e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03913002e+01   # MW
        25     1.15551555e+02   # h0
        35     8.03225807e+02   # H0
        36     8.02955199e+02   # A0
        37     8.07221570e+02   # H+
   1000021     1.25464515e+03   # ~g
   1000022     2.26266822e+02   # ~neutralino(1)
   1000023     4.28030903e+02   # ~neutralino(2)
   1000024     4.28190982e+02   # ~chargino(1)
   1000025    -6.91123566e+02   # ~neutralino(3)
   1000035     7.04128023e+02   # ~neutralino(4)
   1000037     7.03748396e+02   # ~chargino(2)
   1000001     1.16486717e+03   # ~d_L
   1000002     1.16232633e+03   # ~u_L
   1000003     1.16486428e+03   # ~s_L
   1000004     1.16232344e+03   # ~c_L
   1000005     1.06439107e+03   # ~b_1
   1000006     8.88773756e+02   # ~t_1
   1000011     4.34556470e+02   # ~e_L
   1000012     4.27156208e+02   # ~nue_L
   1000013     4.34674713e+02   # ~mu_L
   1000014     4.27151869e+02   # ~numu_L
   1000015     3.01542721e+02   # ~stau_1
   1000016     4.25683896e+02   # ~nu_tau_L
   2000001     1.11646223e+03   # ~d_R
   2000002     1.12029346e+03   # ~u_R
   2000003     1.11645922e+03   # ~s_R
   2000004     1.12029037e+03   # ~c_R
   2000005     1.11223090e+03   # ~b_2
   2000006     1.10564904e+03   # ~t_2
   2000011     3.08214547e+02   # ~e_R
   2000013     3.08202330e+02   # ~mu_R
   2000015     4.34979005e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06182315e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96459280e-01   # N_{1,1}
  1  2    -1.47711275e-02   # N_{1,2}
  1  3     7.62953054e-02   # N_{1,3}
  1  4    -3.20896167e-02   # N_{1,4}
  2  1     3.28605876e-02   # N_{2,1}
  2  2     9.73513056e-01   # N_{2,2}
  2  3    -1.87338259e-01   # N_{2,3}
  2  4     1.26873510e-01   # N_{2,4}
  3  1    -3.04455032e-02   # N_{3,1}
  3  2     4.42212716e-02   # N_{3,2}
  3  3     7.04035478e-01   # N_{3,3}
  3  4     7.08132471e-01   # N_{3,4}
  4  1    -7.11488331e-02   # N_{4,1}
  4  2     2.23827214e-01   # N_{4,2}
  4  3     6.80747713e-01   # N_{4,3}
  4  4    -6.93845640e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.64299204e-01   # U_{1,1}
  1  2    -2.64815114e-01   # U_{1,2}
  2  1     2.64815114e-01   # U_{2,1}
  2  2     9.64299204e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.83434204e-01   # V_{1,1}
  1  2    -1.81265460e-01   # V_{1,2}
  2  1     1.81265460e-01   # V_{2,1}
  2  2     9.83434204e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.97111139e-01   # F_{11}
  1  2     9.17770529e-01   # F_{12}
  2  1     9.17770529e-01   # F_{21}
  2  2    -3.97111139e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.82322997e-01   # F_{11}
  1  2     1.87193831e-01   # F_{12}
  2  1    -1.87193831e-01   # F_{21}
  2  2     9.82322997e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.28678681e-01   # F_{11}
  1  2     9.91686340e-01   # F_{12}
  2  1     9.91686340e-01   # F_{21}
  2  2    -1.28678681e-01   # F_{22}
Block gauge Q= 9.61582155e+02  # SM gauge couplings
     1     3.62545774e-01   # g'(Q)MSSM DRbar
     2     6.42424272e-01   # g(Q)MSSM DRbar
     3     1.05598349e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.61582155e+02  
  3  3     8.58077765e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.61582155e+02  
  3  3     1.34706367e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.61582155e+02  
  3  3     1.00445864e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.61582155e+02 # Higgs mixing parameters
     1     6.85616862e+02    # mu(Q)MSSM DRbar
     2     9.66208316e+00    # tan beta(Q)MSSM DRbar
     3     2.43985306e+02    # higgs vev(Q)MSSM DRbar
     4     6.67794647e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.61582155e+02  # MSSM DRbar SUSY breaking parameters
     1     2.31164983e+02      # M_1(Q)
     2     4.28185184e+02      # M_2(Q)
     3     1.21648897e+03      # M_3(Q)
    21     1.62306149e+05      # mH1^2(Q)
    22    -4.53380861e+05      # mH2^2(Q)
    31     4.27437733e+02      # meL(Q)
    32     4.27433385e+02      # mmuL(Q)
    33     4.26120492e+02      # mtauL(Q)
    34     3.01938499e+02      # meR(Q)
    35     3.01926018e+02      # mmuR(Q)
    36     2.98138582e+02      # mtauR(Q)
    41     1.12493741e+03      # mqL1(Q)
    42     1.12493447e+03      # mqL2(Q)
    43     1.03434450e+03      # mqL3(Q)
    44     1.08353532e+03      # muR(Q)
    45     1.08353218e+03      # mcR(Q)
    46     8.86538264e+02      # mtR(Q)
    47     1.07850973e+03      # mdR(Q)
    48     1.07850667e+03      # msR(Q)
    49     1.07291401e+03      # mbR(Q)
Block au Q= 9.61582155e+02  
  1  1    -1.24212645e+03      # Au(Q)MSSM DRbar
  2  2    -1.24212090e+03      # Ac(Q)MSSM DRbar
  3  3    -9.59661300e+02      # At(Q)MSSM DRbar
Block ad Q= 9.61582155e+02  
  1  1    -1.51815133e+03      # Ad(Q)MSSM DRbar
  2  2    -1.51814619e+03      # As(Q)MSSM DRbar
  3  3    -1.41898994e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.61582155e+02  
  1  1    -3.27924683e+02      # Ae(Q)MSSM DRbar
  2  2    -3.27918824e+02      # Amu(Q)MSSM DRbar
  3  3    -3.26150449e+02      # Atau(Q)MSSM DRbar
