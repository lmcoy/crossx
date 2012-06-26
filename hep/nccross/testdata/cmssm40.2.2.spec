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
     3    4.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    5.00000000e+02   # m0
     2    6.00000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.80441506e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03886567e+01   # MW
        25     1.18006077e+02   # h0
        35     7.38297925e+02   # H0
        36     7.38250762e+02   # A0
        37     7.42953955e+02   # H+
   1000021     1.37076775e+03   # ~g
   1000022     2.51152899e+02   # ~neutralino(1)
   1000023     4.78170999e+02   # ~neutralino(2)
   1000024     4.78256020e+02   # ~chargino(1)
   1000025    -8.05886246e+02   # ~neutralino(3)
   1000035     8.13829930e+02   # ~neutralino(4)
   1000037     8.14245570e+02   # ~chargino(2)
   1000001     1.33338592e+03   # ~d_L
   1000002     1.33115578e+03   # ~u_L
   1000003     1.33334767e+03   # ~s_L
   1000004     1.33111745e+03   # ~c_L
   1000005     1.11679734e+03   # ~b_1
   1000006     9.58509650e+02   # ~t_1
   1000011     6.41701056e+02   # ~e_L
   1000012     6.36498756e+02   # ~nue_L
   1000013     6.41762082e+02   # ~mu_L
   1000014     6.36336967e+02   # ~numu_L
   1000015     3.84381278e+02   # ~stau_1
   1000016     5.80666889e+02   # ~nu_tau_L
   2000001     1.28411017e+03   # ~d_R
   2000002     1.28816517e+03   # ~u_R
   2000003     1.28403437e+03   # ~s_R
   2000004     1.28816031e+03   # ~c_R
   2000005     1.18618240e+03   # ~b_2
   2000006     1.17986824e+03   # ~t_2
   2000011     5.49312358e+02   # ~e_R
   2000013     5.48932573e+02   # ~mu_R
   2000015     6.02041390e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59921897e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97768410e-01   # N_{1,1}
  1  2    -7.83045814e-03   # N_{1,2}
  1  3     6.27778194e-02   # N_{1,3}
  1  4    -2.13501589e-02   # N_{1,4}
  2  1     1.90448590e-02   # N_{2,1}
  2  2     9.84484224e-01   # N_{2,2}
  2  3    -1.49107348e-01   # N_{2,3}
  2  4     9.05268208e-02   # N_{2,4}
  3  1    -2.88566947e-02   # N_{3,1}
  3  2     4.21946777e-02   # N_{3,2}
  3  3     7.04603116e-01   # N_{3,3}
  3  4     7.07757974e-01   # N_{3,4}
  4  1    -5.71207886e-02   # N_{4,1}
  4  2     1.70144369e-01   # N_{4,2}
  4  3     6.90912725e-01   # N_{4,3}
  4  4    -7.00305445e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.77619220e-01   # U_{1,1}
  1  2    -2.10382176e-01   # U_{1,2}
  2  1     2.10382176e-01   # U_{2,1}
  2  2     9.77619220e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91519796e-01   # V_{1,1}
  1  2    -1.29955740e-01   # V_{1,2}
  2  1     1.29955740e-01   # V_{2,1}
  2  2     9.91519796e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.18172161e-01   # F_{11}
  1  2     9.08367791e-01   # F_{12}
  2  1     9.08367791e-01   # F_{21}
  2  2    -4.18172161e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.50685451e-01   # F_{11}
  1  2     5.25675055e-01   # F_{12}
  2  1    -5.25675055e-01   # F_{21}
  2  2     8.50685451e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.93621148e-01   # F_{11}
  1  2     9.55921870e-01   # F_{12}
  2  1     9.55921870e-01   # F_{21}
  2  2    -2.93621148e-01   # F_{22}
Block gauge Q= 1.03331474e+03  # SM gauge couplings
     1     3.62466377e-01   # g'(Q)MSSM DRbar
     2     6.41336678e-01   # g(Q)MSSM DRbar
     3     1.05148190e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.03331474e+03  
  3  3     8.50068583e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.03331474e+03  
  3  3     4.92272728e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.03331474e+03  
  3  3     4.26698667e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.03331474e+03 # Higgs mixing parameters
     1     8.02378402e+02    # mu(Q)MSSM DRbar
     2     3.91902486e+01    # tan beta(Q)MSSM DRbar
     3     2.43818784e+02    # higgs vev(Q)MSSM DRbar
     4     6.98097375e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.03331474e+03  # MSSM DRbar SUSY breaking parameters
     1     2.54578572e+02      # M_1(Q)
     2     4.70593104e+02      # M_2(Q)
     3     1.32244264e+03      # M_3(Q)
    21    -8.77991160e+04      # mH1^2(Q)
    22    -6.31545103e+05      # mH2^2(Q)
    31     6.36491889e+02      # meL(Q)
    32     6.36329731e+02      # mmuL(Q)
    33     5.83317491e+02      # mtauL(Q)
    34     5.45523113e+02      # meR(Q)
    35     5.45140927e+02      # mmuR(Q)
    36     4.07615070e+02      # mtauR(Q)
    41     1.29253368e+03      # mqL1(Q)
    42     1.29249451e+03      # mqL2(Q)
    43     1.10611650e+03      # mqL3(Q)
    44     1.25026200e+03      # muR(Q)
    45     1.25025705e+03      # mcR(Q)
    46     9.60424027e+02      # mtR(Q)
    47     1.24517149e+03      # mdR(Q)
    48     1.24509417e+03      # msR(Q)
    49     1.13259325e+03      # mbR(Q)
Block au Q= 1.03331474e+03  
  1  1    -1.68524183e+03      # Au(Q)MSSM DRbar
  2  2    -1.68520179e+03      # Ac(Q)MSSM DRbar
  3  3    -1.17774452e+03      # At(Q)MSSM DRbar
Block ad Q= 1.03331474e+03  
  1  1    -1.94947462e+03      # Ad(Q)MSSM DRbar
  2  2    -1.94937267e+03      # As(Q)MSSM DRbar
  3  3    -1.64357331e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.03331474e+03  
  1  1    -6.64943298e+02      # Ae(Q)MSSM DRbar
  2  2    -6.64616730e+02      # Amu(Q)MSSM DRbar
  3  3    -5.55665880e+02      # Atau(Q)MSSM DRbar
