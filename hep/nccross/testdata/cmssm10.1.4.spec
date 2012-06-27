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
     1    1.62500000e+02   # m0
     2    6.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.71820143e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03897808e+01   # MW
        25     1.16588974e+02   # h0
        35     9.13412571e+02   # H0
        36     9.13183440e+02   # A0
        37     9.16930480e+02   # H+
   1000021     1.46104655e+03   # ~g
   1000022     2.69438836e+02   # ~neutralino(1)
   1000023     5.09943437e+02   # ~neutralino(2)
   1000024     5.10134364e+02   # ~chargino(1)
   1000025    -8.00208590e+02   # ~neutralino(3)
   1000035     8.12098556e+02   # ~neutralino(4)
   1000037     8.11732144e+02   # ~chargino(2)
   1000001     1.34162666e+03   # ~d_L
   1000002     1.33944387e+03   # ~u_L
   1000003     1.34162342e+03   # ~s_L
   1000004     1.33944063e+03   # ~c_L
   1000005     1.22963209e+03   # ~b_1
   1000006     1.03433429e+03   # ~t_1
   1000011     4.66804116e+02   # ~e_L
   1000012     4.59903452e+02   # ~nue_L
   1000013     4.66870776e+02   # ~mu_L
   1000014     4.59899216e+02   # ~numu_L
   1000015     2.89093732e+02   # ~stau_1
   1000016     4.58418366e+02   # ~nu_tau_L
   2000001     1.28322860e+03   # ~d_R
   2000002     1.28820000e+03   # ~u_R
   2000003     1.28322522e+03   # ~s_R
   2000004     1.28819653e+03   # ~c_R
   2000005     1.27824659e+03   # ~b_2
   2000006     1.26698874e+03   # ~t_2
   2000011     2.96267110e+02   # ~e_R
   2000013     2.96253764e+02   # ~mu_R
   2000015     4.67042594e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05697490e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97362483e-01   # N_{1,1}
  1  2    -1.10020086e-02   # N_{1,2}
  1  3     6.59283244e-02   # N_{1,3}
  1  4    -2.82929151e-02   # N_{1,4}
  2  1     2.52896196e-02   # N_{2,1}
  2  2     9.78295708e-01   # N_{2,2}
  2  3    -1.69069722e-01   # N_{2,3}
  2  4     1.17104108e-01   # N_{2,4}
  3  1    -2.60953360e-02   # N_{3,1}
  3  2     3.77536659e-02   # N_{3,2}
  3  3     7.04850067e-01   # N_{3,3}
  3  4     7.07870099e-01   # N_{3,4}
  4  1    -6.28294976e-02   # N_{4,1}
  4  2     2.03448088e-01   # N_{4,2}
  4  3     6.85751609e-01   # N_{4,3}
  4  4    -6.95992860e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.71204129e-01   # U_{1,1}
  1  2    -2.38248902e-01   # U_{1,2}
  2  1     2.38248902e-01   # U_{2,1}
  2  2     9.71204129e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86025404e-01   # V_{1,1}
  1  2    -1.66595027e-01   # V_{1,2}
  2  1     1.66595027e-01   # V_{2,1}
  2  2     9.86025404e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.65916216e-01   # F_{11}
  1  2     9.30647797e-01   # F_{12}
  2  1     9.30647797e-01   # F_{21}
  2  2    -3.65916216e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.83067993e-01   # F_{11}
  1  2     1.83241156e-01   # F_{12}
  2  1    -1.83241156e-01   # F_{21}
  2  2     9.83067993e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.08682477e-01   # F_{11}
  1  2     9.94076516e-01   # F_{12}
  2  1     9.94076516e-01   # F_{21}
  2  2    -1.08682477e-01   # F_{22}
Block gauge Q= 1.11133780e+03  # SM gauge couplings
     1     3.62919423e-01   # g'(Q)MSSM DRbar
     2     6.41678607e-01   # g(Q)MSSM DRbar
     3     1.04831416e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.11133780e+03  
  3  3     8.52987915e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.11133780e+03  
  3  3     1.33650126e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.11133780e+03  
  3  3     1.00352154e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.11133780e+03 # Higgs mixing parameters
     1     7.94756551e+02    # mu(Q)MSSM DRbar
     2     9.64521448e+00    # tan beta(Q)MSSM DRbar
     3     2.43822521e+02    # higgs vev(Q)MSSM DRbar
     4     8.64024879e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.11133780e+03  # MSSM DRbar SUSY breaking parameters
     1     2.75200971e+02      # M_1(Q)
     2     5.07716617e+02      # M_2(Q)
     3     1.42126466e+03      # M_3(Q)
    21     1.84107330e+05      # mH1^2(Q)
    22    -6.07770532e+05      # mH2^2(Q)
    31     4.58344043e+02      # meL(Q)
    32     4.58339797e+02      # mmuL(Q)
    33     4.57055832e+02      # mtauL(Q)
    34     2.88231444e+02      # meR(Q)
    35     2.88217711e+02      # mmuR(Q)
    36     2.84039424e+02      # mtauR(Q)
    41     1.29614412e+03      # mqL1(Q)
    42     1.29614082e+03      # mqL2(Q)
    43     1.19547750e+03      # mqL3(Q)
    44     1.24602840e+03      # muR(Q)
    45     1.24602487e+03      # mcR(Q)
    46     1.02700222e+03      # mtR(Q)
    47     1.23988853e+03      # mdR(Q)
    48     1.23988510e+03      # msR(Q)
    49     1.23363480e+03      # mbR(Q)
Block au Q= 1.11133780e+03  
  1  1    -1.44293251e+03      # Au(Q)MSSM DRbar
  2  2    -1.44292611e+03      # Ac(Q)MSSM DRbar
  3  3    -1.11771260e+03      # At(Q)MSSM DRbar
Block ad Q= 1.11133780e+03  
  1  1    -1.76014286e+03      # Ad(Q)MSSM DRbar
  2  2    -1.76013694e+03      # As(Q)MSSM DRbar
  3  3    -1.64600123e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.11133780e+03  
  1  1    -3.84624534e+02      # Ae(Q)MSSM DRbar
  2  2    -3.84617731e+02      # Amu(Q)MSSM DRbar
  3  3    -3.82560492e+02      # Atau(Q)MSSM DRbar
