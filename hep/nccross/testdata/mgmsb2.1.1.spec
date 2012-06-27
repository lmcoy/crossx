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
     1    7.20000000e+04   # lambda
     2    8.00000000e+04   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=8.00000000e+04 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04111657e+01   # MW
        25     1.10611648e+02   # h0
        35     3.73622306e+02   # H0
        36     3.73206072e+02   # A0
        37     3.82155954e+02   # H+
   1000021     7.07214681e+02   # ~g
   1000022     1.14264919e+02   # ~neutralino(1)
   1000023     2.06538754e+02   # ~neutralino(2)
   1000024     2.05764289e+02   # ~chargino(1)
   1000025    -3.04619197e+02   # ~neutralino(3)
   1000035     3.38714173e+02   # ~neutralino(4)
   1000037     3.37422049e+02   # ~chargino(2)
   1000039     1.36512000e-09   # ~gravitino
   1000001     8.40570044e+02   # ~d_L
   1000002     8.36983946e+02   # ~u_L
   1000003     8.40568893e+02   # ~s_L
   1000004     8.36982790e+02   # ~c_L
   1000005     7.95940644e+02   # ~b_1
   1000006     7.47814567e+02   # ~t_1
   1000011     2.56403716e+02   # ~e_L
   1000012     2.43494551e+02   # ~nue_L
   1000013     2.56449027e+02   # ~mu_L
   1000014     2.43493414e+02   # ~numu_L
   1000015     1.22809088e+02   # ~stau_1
   1000016     2.42992215e+02   # ~nu_tau_L
   2000001     8.04159438e+02   # ~d_R
   2000002     8.05699292e+02   # ~u_R
   2000003     8.04157835e+02   # ~s_R
   2000004     8.05698476e+02   # ~c_R
   2000005     8.11583760e+02   # ~b_2
   2000006     8.27438895e+02   # ~t_2
   2000011     1.29436285e+02   # ~e_R
   2000013     1.29431957e+02   # ~mu_R
   2000015     2.58333129e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.96331050e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.75215590e-01   # N_{1,1}
  1  2    -6.35503617e-02   # N_{1,2}
  1  3     1.93875694e-01   # N_{1,3}
  1  4    -8.56044393e-02   # N_{1,4}
  2  1     1.61789996e-01   # N_{2,1}
  2  2     8.50472882e-01   # N_{2,2}
  2  3    -4.05479444e-01   # N_{2,3}
  2  4     2.93438742e-01   # N_{2,4}
  3  1    -6.88337059e-02   # N_{3,1}
  3  2     9.77373432e-02   # N_{3,2}
  3  3     6.92438038e-01   # N_{3,3}
  3  4     7.11504671e-01   # N_{3,4}
  4  1    -1.34314821e-01   # N_{4,1}
  4  2     5.12937268e-01   # N_{4,2}
  4  3     5.64383026e-01   # N_{4,3}
  4  4    -6.32713749e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.03668247e-01   # U_{1,1}
  1  2    -5.95077600e-01   # U_{1,2}
  2  1     5.95077600e-01   # U_{2,1}
  2  2     8.03668247e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.00614400e-01   # V_{1,1}
  1  2    -4.34619031e-01   # V_{1,2}
  2  1     4.34619031e-01   # V_{2,1}
  2  2     9.00614400e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.27997915e-01   # F_{11}
  1  2     9.44678447e-01   # F_{12}
  2  1     9.44678447e-01   # F_{21}
  2  2    -3.27997915e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.41229482e-01   # F_{11}
  1  2     8.40874930e-01   # F_{12}
  2  1     8.40874930e-01   # F_{21}
  2  2    -5.41229482e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.54151091e-01   # F_{11}
  1  2     9.88047287e-01   # F_{12}
  2  1     9.88047287e-01   # F_{21}
  2  2    -1.54151091e-01   # F_{22}
Block gauge Q= 7.68693779e+02  # SM gauge couplings
     1     3.62511547e-01   # g'(Q)MSSM DRbar
     2     6.46102985e-01   # g(Q)MSSM DRbar
     3     1.07638115e+00   # g3(Q)MSSM DRbar
Block yu Q= 7.68693779e+02  
  3  3     8.73703942e-01   # Yt(Q)MSSM DRbar
Block yd Q= 7.68693779e+02  
  3  3     2.06896701e-01   # Yb(Q)MSSM DRbar
Block ye Q= 7.68693779e+02  
  3  3     1.51624556e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 7.68693779e+02 # Higgs mixing parameters
     1     2.95115595e+02    # mu(Q)MSSM DRbar
     2     1.45437264e+01    # tan beta(Q)MSSM DRbar
     3     2.43902584e+02    # higgs vev(Q)MSSM DRbar
     4     1.54852163e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 7.68693779e+02  # MSSM DRbar SUSY breaking parameters
     1     1.21036979e+02      # M_1(Q)
     2     2.29805678e+02      # M_2(Q)
     3     6.41114065e+02      # M_3(Q)
    21     5.42289991e+04      # mH1^2(Q)
    22    -7.85631250e+04      # mH2^2(Q)
    31     2.49843523e+02      # meL(Q)
    32     2.49842411e+02      # mmuL(Q)
    33     2.49503981e+02      # mtauL(Q)
    34     1.18260516e+02      # meR(Q)
    35     1.18255773e+02      # mmuR(Q)
    36     1.16803171e+02      # mtauR(Q)
    41     8.15912006e+02      # mqL1(Q)
    42     8.15910813e+02      # mqL2(Q)
    43     7.87291770e+02      # mqL3(Q)
    44     7.83708465e+02      # muR(Q)
    45     7.83707619e+02      # mcR(Q)
    46     7.25287080e+02      # mtR(Q)
    47     7.80682995e+02      # mdR(Q)
    48     7.80681330e+02      # msR(Q)
    49     7.77421679e+02      # mbR(Q)
Block au Q= 7.68693779e+02  
  1  1    -1.99092654e+02      # Au(Q)MSSM DRbar
  2  2    -1.99092367e+02      # Ac(Q)MSSM DRbar
  3  3    -1.87348365e+02      # At(Q)MSSM DRbar
Block ad Q= 7.68693779e+02  
  1  1    -2.12229841e+02      # Ad(Q)MSSM DRbar
  2  2    -2.12229440e+02      # As(Q)MSSM DRbar
  3  3    -2.07802421e+02      # Ab(Q)MSSM DRbar
Block ae Q= 7.68693779e+02  
  1  1    -1.94806144e+01      # Ae(Q)MSSM DRbar
  2  2    -1.94804701e+01      # Amu(Q)MSSM DRbar
  3  3    -1.94365418e+01      # Atau(Q)MSSM DRbar
