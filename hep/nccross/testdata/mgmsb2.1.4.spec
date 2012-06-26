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
     1    9.90000000e+04   # lambda
     2    1.10000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.10000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04010787e+01   # MW
        25     1.13034493e+02   # h0
        35     5.05552140e+02   # H0
        36     5.05245726e+02   # A0
        37     5.11893602e+02   # H+
   1000021     9.41981842e+02   # ~g
   1000022     1.60375143e+02   # ~neutralino(1)
   1000023     2.94940900e+02   # ~neutralino(2)
   1000024     2.94730690e+02   # ~chargino(1)
   1000025    -3.99214216e+02   # ~neutralino(3)
   1000035     4.31731167e+02   # ~neutralino(4)
   1000037     4.30325064e+02   # ~chargino(2)
   1000039     2.58093000e-09   # ~gravitino
   1000001     1.12449263e+03   # ~d_L
   1000002     1.12186415e+03   # ~u_L
   1000003     1.12449110e+03   # ~s_L
   1000004     1.12186262e+03   # ~c_L
   1000005     1.06596822e+03   # ~b_1
   1000006     9.95197777e+02   # ~t_1
   1000011     3.48521602e+02   # ~e_L
   1000012     3.39093725e+02   # ~nue_L
   1000013     3.48537644e+02   # ~mu_L
   1000014     3.39092190e+02   # ~numu_L
   1000015     1.68048967e+02   # ~stau_1
   1000016     3.38413852e+02   # ~nu_tau_L
   2000001     1.07428813e+03   # ~d_R
   2000002     1.07729989e+03   # ~u_R
   2000003     1.07428600e+03   # ~s_R
   2000004     1.07729880e+03   # ~c_R
   2000005     1.08363007e+03   # ~b_2
   2000006     1.09504774e+03   # ~t_2
   2000011     1.73902857e+02   # ~e_R
   2000013     1.73896797e+02   # ~mu_R
   2000015     3.49544696e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.48160005e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.86480692e-01   # N_{1,1}
  1  2    -3.68340487e-02   # N_{1,2}
  1  3     1.44862038e-01   # N_{1,3}
  1  4    -6.71869616e-02   # N_{1,4}
  2  1     1.08689427e-01   # N_{2,1}
  2  2     8.68802069e-01   # N_{2,2}
  2  3    -3.82228196e-01   # N_{2,3}
  2  4     2.95416958e-01   # N_{2,4}
  3  1    -5.15876195e-02   # N_{3,1}
  3  2     7.26360842e-02   # N_{3,2}
  3  3     6.98903526e-01   # N_{3,3}
  3  4     7.09645389e-01   # N_{3,4}
  4  1    -1.11270710e-01   # N_{4,1}
  4  2     4.88416028e-01   # N_{4,2}
  4  3     5.86899018e-01   # N_{4,3}
  4  4    -6.36096026e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.34336958e-01   # U_{1,1}
  1  2    -5.51254788e-01   # U_{1,2}
  2  1     5.51254788e-01   # U_{2,1}
  2  2     8.34336958e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.02961776e-01   # V_{1,1}
  1  2    -4.29720875e-01   # V_{1,2}
  2  1     4.29720875e-01   # V_{2,1}
  2  2     9.02961776e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.57032835e-01   # F_{11}
  1  2     9.66402671e-01   # F_{12}
  2  1     9.66402671e-01   # F_{21}
  2  2    -2.57032835e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.42657051e-01   # F_{11}
  1  2     8.96690992e-01   # F_{12}
  2  1     8.96690992e-01   # F_{21}
  2  2    -4.42657051e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.11267123e-01   # F_{11}
  1  2     9.93790535e-01   # F_{12}
  2  1     9.93790535e-01   # F_{21}
  2  2    -1.11267123e-01   # F_{22}
Block gauge Q= 1.02185061e+03  # SM gauge couplings
     1     3.63123364e-01   # g'(Q)MSSM DRbar
     2     6.44439149e-01   # g(Q)MSSM DRbar
     3     1.06081873e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.02185061e+03  
  3  3     8.63357958e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.02185061e+03  
  3  3     2.03767577e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.02185061e+03  
  3  3     1.51372128e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.02185061e+03 # Higgs mixing parameters
     1     3.90558778e+02    # mu(Q)MSSM DRbar
     2     1.44940023e+01    # tan beta(Q)MSSM DRbar
     3     2.43544477e+02    # higgs vev(Q)MSSM DRbar
     4     2.82964046e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.02185061e+03  # MSSM DRbar SUSY breaking parameters
     1     1.67042763e+02      # M_1(Q)
     2     3.14501064e+02      # M_2(Q)
     3     8.56450195e+02      # M_3(Q)
    21     1.02533202e+05      # mH1^2(Q)
    22    -1.33073995e+05      # mH2^2(Q)
    31     3.42024492e+02      # meL(Q)
    32     3.42022965e+02      # mmuL(Q)
    33     3.41556186e+02      # mtauL(Q)
    34     1.63433796e+02      # meR(Q)
    35     1.63427342e+02      # mmuR(Q)
    36     1.61443103e+02      # mtauR(Q)
    41     1.09349455e+03      # mqL1(Q)
    42     1.09349296e+03      # mqL2(Q)
    43     1.05555422e+03      # mqL3(Q)
    44     1.04850240e+03      # muR(Q)
    45     1.04850127e+03      # mcR(Q)
    46     9.70912333e+02      # mtR(Q)
    47     1.04418584e+03      # mdR(Q)
    48     1.04418364e+03      # msR(Q)
    49     1.03988491e+03      # mbR(Q)
Block au Q= 1.02185061e+03  
  1  1    -2.62414431e+02      # Au(Q)MSSM DRbar
  2  2    -2.62414058e+02      # Ac(Q)MSSM DRbar
  3  3    -2.47133484e+02      # At(Q)MSSM DRbar
Block ad Q= 1.02185061e+03  
  1  1    -2.79383559e+02      # Ad(Q)MSSM DRbar
  2  2    -2.79383039e+02      # As(Q)MSSM DRbar
  3  3    -2.73629647e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.02185061e+03  
  1  1    -2.68531130e+01      # Ae(Q)MSSM DRbar
  2  2    -2.68529144e+01      # Amu(Q)MSSM DRbar
  3  3    -2.67922441e+01      # Atau(Q)MSSM DRbar
