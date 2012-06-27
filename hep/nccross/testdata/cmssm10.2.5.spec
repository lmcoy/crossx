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
     1    3.00000000e+02   # m0
     2    7.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.71121749e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03888643e+01   # MW
        25     1.17069390e+02   # h0
        35     1.00614783e+03   # H0
        36     1.00592697e+03   # A0
        37     1.00936159e+03   # H+
   1000021     1.56862013e+03   # ~g
   1000022     2.91882824e+02   # ~neutralino(1)
   1000023     5.52345988e+02   # ~neutralino(2)
   1000024     5.52549021e+02   # ~chargino(1)
   1000025    -8.53782234e+02   # ~neutralino(3)
   1000035     8.65260406e+02   # ~neutralino(4)
   1000037     8.64896121e+02   # ~chargino(2)
   1000001     1.45601548e+03   # ~d_L
   1000002     1.45402009e+03   # ~u_L
   1000003     1.45601189e+03   # ~s_L
   1000004     1.45401650e+03   # ~c_L
   1000005     1.33138761e+03   # ~b_1
   1000006     1.12011761e+03   # ~t_1
   1000011     5.57342561e+02   # ~e_L
   1000012     5.51536915e+02   # ~nue_L
   1000013     5.57457254e+02   # ~mu_L
   1000014     5.51531380e+02   # ~numu_L
   1000015     3.93498956e+02   # ~stau_1
   1000016     5.49661932e+02   # ~nu_tau_L
   2000001     1.39408800e+03   # ~d_R
   2000002     1.39951887e+03   # ~u_R
   2000003     1.39408427e+03   # ~s_R
   2000004     1.39951500e+03   # ~c_R
   2000005     1.38811499e+03   # ~b_2
   2000006     1.36524107e+03   # ~t_2
   2000011     4.00531985e+02   # ~e_R
   2000013     4.00516512e+02   # ~mu_R
   2000015     5.56890132e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05390604e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97669369e-01   # N_{1,1}
  1  2    -9.67420457e-03   # N_{1,2}
  1  3     6.19646712e-02   # N_{1,3}
  1  4    -2.68815769e-02   # N_{1,4}
  2  1     2.26253485e-02   # N_{2,1}
  2  2     9.79973153e-01   # N_{2,2}
  2  3    -1.62046968e-01   # N_{2,3}
  2  4     1.13496662e-01   # N_{2,4}
  3  1    -2.43840422e-02   # N_{3,1}
  3  2     3.51922329e-02   # N_{3,2}
  3  3     7.05139895e-01   # N_{3,3}
  3  4     7.07774437e-01   # N_{3,4}
  4  1    -5.95763543e-02   # N_{4,1}
  4  2     1.95756316e-01   # N_{4,2}
  4  3     6.87516463e-01   # N_{4,3}
  4  4    -6.96743307e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73526694e-01   # U_{1,1}
  1  2    -2.28573349e-01   # U_{1,2}
  2  1     2.28573349e-01   # U_{2,1}
  2  2     9.73526694e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86843942e-01   # V_{1,1}
  1  2    -1.61675709e-01   # V_{1,2}
  2  1     1.61675709e-01   # V_{2,1}
  2  2     9.86843942e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.39616208e-01   # F_{11}
  1  2     9.40564103e-01   # F_{12}
  2  1     9.40564103e-01   # F_{21}
  2  2    -3.39616208e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.88147841e-01   # F_{11}
  1  2     1.53505196e-01   # F_{12}
  2  1    -1.53505196e-01   # F_{21}
  2  2     9.88147841e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.00319718e-01   # F_{11}
  1  2     9.94955252e-01   # F_{12}
  2  1     9.94955252e-01   # F_{21}
  2  2    -1.00319718e-01   # F_{22}
Block gauge Q= 1.20077857e+03  # SM gauge couplings
     1     3.63001074e-01   # g'(Q)MSSM DRbar
     2     6.41207171e-01   # g(Q)MSSM DRbar
     3     1.04446514e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.20077857e+03  
  3  3     8.50587293e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.20077857e+03  
  3  3     1.33195536e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.20077857e+03  
  3  3     1.00283833e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.20077857e+03 # Higgs mixing parameters
     1     8.48132011e+02    # mu(Q)MSSM DRbar
     2     9.63611571e+00    # tan beta(Q)MSSM DRbar
     3     2.43728649e+02    # higgs vev(Q)MSSM DRbar
     4     1.04685533e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.20077857e+03  # MSSM DRbar SUSY breaking parameters
     1     2.97332480e+02      # M_1(Q)
     2     5.47592979e+02      # M_2(Q)
     3     1.52257357e+03      # M_3(Q)
    21     2.70205425e+05      # mH1^2(Q)
    22    -6.89848085e+05      # mH2^2(Q)
    31     5.49311264e+02      # meL(Q)
    32     5.49305694e+02      # mmuL(Q)
    33     5.47619441e+02      # mtauL(Q)
    34     3.94216215e+02      # meR(Q)
    35     3.94200483e+02      # mmuR(Q)
    36     3.89415057e+02      # mtauR(Q)
    41     1.40755562e+03      # mqL1(Q)
    42     1.40755196e+03      # mqL2(Q)
    43     1.29445507e+03      # mqL3(Q)
    44     1.35434865e+03      # muR(Q)
    45     1.35434472e+03      # mcR(Q)
    46     1.10807907e+03      # mtR(Q)
    47     1.34781568e+03      # mdR(Q)
    48     1.34781189e+03      # msR(Q)
    49     1.34090929e+03      # mbR(Q)
Block au Q= 1.20077857e+03  
  1  1    -1.54153421e+03      # Au(Q)MSSM DRbar
  2  2    -1.54152739e+03      # Ac(Q)MSSM DRbar
  3  3    -1.19533710e+03      # At(Q)MSSM DRbar
Block ad Q= 1.20077857e+03  
  1  1    -1.87889747e+03      # Ad(Q)MSSM DRbar
  2  2    -1.87889117e+03      # As(Q)MSSM DRbar
  3  3    -1.75740310e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.20077857e+03  
  1  1    -4.12835249e+02      # Ae(Q)MSSM DRbar
  2  2    -4.12827978e+02      # Amu(Q)MSSM DRbar
  3  3    -4.10628011e+02      # Atau(Q)MSSM DRbar
