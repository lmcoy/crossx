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
     1    1.20000000e+05   # lambda
     2    1.00000000e+09   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.00000000e+09 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03971521e+01   # MW
        25     1.13647224e+02   # h0
        35     7.55852577e+02   # H0
        36     7.55739288e+02   # A0
        37     7.60243386e+02   # H+
   1000021     9.32677880e+02   # ~g
   1000022     1.60213674e+02   # ~neutralino(1)
   1000023     3.10277495e+02   # ~neutralino(2)
   1000024     3.10440417e+02   # ~chargino(1)
   1000025    -6.28446430e+02   # ~neutralino(3)
   1000035     6.37720259e+02   # ~neutralino(4)
   1000037     6.37991674e+02   # ~chargino(2)
   1000039     2.84400000e-05   # ~gravitino
   1000001     1.19297803e+03   # ~d_L
   1000002     1.19049525e+03   # ~u_L
   1000003     1.19297457e+03   # ~s_L
   1000004     1.19049178e+03   # ~c_L
   1000005     1.09041995e+03   # ~b_1
   1000006     9.33002265e+02   # ~t_1
   1000011     4.67109240e+02   # ~e_L
   1000012     4.60042203e+02   # ~nue_L
   1000013     4.67136819e+02   # ~mu_L
   1000014     4.60036508e+02   # ~numu_L
   1000015     2.48018858e+02   # ~stau_1
   1000016     4.58034797e+02   # ~nu_tau_L
   2000001     1.10934025e+03   # ~d_R
   2000002     1.11760105e+03   # ~u_R
   2000003     1.10933530e+03   # ~s_R
   2000004     1.11759854e+03   # ~c_R
   2000005     1.11166358e+03   # ~b_2
   2000006     1.12035405e+03   # ~t_2
   2000011     2.58430821e+02   # ~e_R
   2000013     2.58410361e+02   # ~mu_R
   2000015     4.67036994e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.12175406e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96417894e-01   # N_{1,1}
  1  2    -1.53244138e-02   # N_{1,2}
  1  3     7.91723660e-02   # N_{1,3}
  1  4    -2.54613404e-02   # N_{1,4}
  2  1     3.05873062e-02   # N_{2,1}
  2  2     9.81531166e-01   # N_{2,2}
  2  3    -1.66046924e-01   # N_{2,3}
  2  4     8.99411230e-02   # N_{2,4}
  3  1    -3.69100000e-02   # N_{3,1}
  3  2     5.51783778e-02   # N_{3,2}
  3  3     7.02942307e-01   # N_{3,3}
  3  4     7.08142014e-01   # N_{3,4}
  4  1    -6.96667041e-02   # N_{4,1}
  4  2     1.82529666e-01   # N_{4,2}
  4  3     6.87046046e-01   # N_{4,3}
  4  4    -6.99855130e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.72368217e-01   # U_{1,1}
  1  2    -2.33452458e-01   # U_{1,2}
  2  1     2.33452458e-01   # U_{2,1}
  2  2     9.72368217e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91725833e-01   # V_{1,1}
  1  2    -1.28373954e-01   # V_{1,2}
  2  1     1.28373954e-01   # V_{2,1}
  2  2     9.91725833e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.30317088e-01   # F_{11}
  1  2     9.73115635e-01   # F_{12}
  2  1     9.73115635e-01   # F_{21}
  2  2    -2.30317088e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     6.54142490e-01   # F_{11}
  1  2     7.56371339e-01   # F_{12}
  2  1     7.56371339e-01   # F_{21}
  2  2    -6.54142490e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.05635142e-01   # F_{11}
  1  2     9.94404956e-01   # F_{12}
  2  1     9.94404956e-01   # F_{21}
  2  2    -1.05635142e-01   # F_{22}
Block gauge Q= 9.98317947e+02  # SM gauge couplings
     1     3.62765353e-01   # g'(Q)MSSM DRbar
     2     6.43399134e-01   # g(Q)MSSM DRbar
     3     1.06114340e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.98317947e+02  
  3  3     8.61444320e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.98317947e+02  
  3  3     1.99669659e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.98317947e+02  
  3  3     1.50927181e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.98317947e+02 # Higgs mixing parameters
     1     6.21331823e+02    # mu(Q)MSSM DRbar
     2     1.44998710e+01    # tan beta(Q)MSSM DRbar
     3     2.43880136e+02    # higgs vev(Q)MSSM DRbar
     4     6.02207685e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.98317947e+02  # MSSM DRbar SUSY breaking parameters
     1     1.63982583e+02      # M_1(Q)
     2     3.06648244e+02      # M_2(Q)
     3     8.44108925e+02      # M_3(Q)
    21     1.80507686e+05      # mH1^2(Q)
    22    -3.69135291e+05      # mH2^2(Q)
    31     4.62956826e+02      # meL(Q)
    32     4.62951155e+02      # mmuL(Q)
    33     4.61223409e+02      # mtauL(Q)
    34     2.50795429e+02      # meR(Q)
    35     2.50774339e+02      # mmuR(Q)
    36     2.44273821e+02      # mtauR(Q)
    41     1.16508805e+03      # mqL1(Q)
    42     1.16508450e+03      # mqL2(Q)
    43     1.07973261e+03      # mqL3(Q)
    44     1.09143595e+03      # muR(Q)
    45     1.09143337e+03      # mcR(Q)
    46     9.06994920e+02      # mtR(Q)
    47     1.08159039e+03      # mdR(Q)
    48     1.08158527e+03      # msR(Q)
    49     1.07202909e+03      # mbR(Q)
Block au Q= 9.98317947e+02  
  1  1    -5.61110032e+02      # Au(Q)MSSM DRbar
  2  2    -5.61108130e+02      # Ac(Q)MSSM DRbar
  3  3    -4.83593805e+02      # At(Q)MSSM DRbar
Block ad Q= 9.98317947e+02  
  1  1    -6.38609382e+02      # Ad(Q)MSSM DRbar
  2  2    -6.38606740e+02      # As(Q)MSSM DRbar
  3  3    -6.09414144e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.98317947e+02  
  1  1    -8.31161164e+01      # Ae(Q)MSSM DRbar
  2  2    -8.31144678e+01      # Amu(Q)MSSM DRbar
  3  3    -8.26129467e+01      # Atau(Q)MSSM DRbar
