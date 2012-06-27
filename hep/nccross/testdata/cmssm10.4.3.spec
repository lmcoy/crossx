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
     1    9.50000000e+02   # m0
     2    4.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.12728622e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03928621e+01   # MW
        25     1.14838547e+02   # h0
        35     1.13093253e+03   # H0
        36     1.13088386e+03   # A0
        37     1.13383197e+03   # H+
   1000021     1.08761761e+03   # ~g
   1000022     1.85745247e+02   # ~neutralino(1)
   1000023     3.51522808e+02   # ~neutralino(2)
   1000024     3.51658803e+02   # ~chargino(1)
   1000025    -5.79051118e+02   # ~neutralino(3)
   1000035     5.94526641e+02   # ~neutralino(4)
   1000037     5.93954804e+02   # ~chargino(2)
   1000001     1.32515230e+03   # ~d_L
   1000002     1.32296887e+03   # ~u_L
   1000003     1.32514769e+03   # ~s_L
   1000004     1.32296426e+03   # ~c_L
   1000005     1.15063984e+03   # ~b_1
   1000006     9.19675476e+02   # ~t_1
   1000011     9.93629356e+02   # ~e_L
   1000012     9.90187060e+02   # ~nue_L
   1000013     9.93662194e+02   # ~mu_L
   1000014     9.90173518e+02   # ~numu_L
   1000015     9.55062295e+02   # ~stau_1
   1000016     9.86027994e+02   # ~nu_tau_L
   2000001     1.29965750e+03   # ~d_R
   2000002     1.30127810e+03   # ~u_R
   2000003     1.29965302e+03   # ~s_R
   2000004     1.30127314e+03   # ~c_R
   2000005     1.29090891e+03   # ~b_2
   2000006     1.17428590e+03   # ~t_2
   2000011     9.64495837e+02   # ~e_R
   2000013     9.64467914e+02   # ~mu_R
   2000015     9.90304330e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04820066e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.94832714e-01   # N_{1,1}
  1  2    -2.08140416e-02   # N_{1,2}
  1  3     9.18157201e-02   # N_{1,3}
  1  4    -3.80068359e-02   # N_{1,4}
  2  1     4.56182420e-02   # N_{2,1}
  2  2     9.64637073e-01   # N_{2,2}
  2  3    -2.15972454e-01   # N_{2,3}
  2  4     1.44049271e-01   # N_{2,4}
  3  1    -3.66759179e-02   # N_{3,1}
  3  2     5.32717732e-02   # N_{3,2}
  3  3     7.02743870e-01   # N_{3,3}
  3  4     7.08497035e-01   # N_{3,4}
  4  1    -8.29561534e-02   # N_{4,1}
  4  2     2.57301790e-01   # N_{4,2}
  4  3     6.71622533e-01   # N_{4,3}
  4  4    -6.89809567e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.51843771e-01   # U_{1,1}
  1  2    -3.06583490e-01   # U_{1,2}
  2  1     3.06583490e-01   # U_{2,1}
  2  2     9.51843771e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.78357117e-01   # V_{1,1}
  1  2    -2.06923539e-01   # V_{1,2}
  2  1     2.06923539e-01   # V_{2,1}
  2  2     9.78357117e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.54724185e-01   # F_{11}
  1  2     9.67013748e-01   # F_{12}
  2  1     9.67013748e-01   # F_{21}
  2  2    -2.54724185e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98895829e-01   # F_{11}
  1  2     4.69800177e-02   # F_{12}
  2  1    -4.69800177e-02   # F_{21}
  2  2     9.98895829e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.54543256e-01   # F_{11}
  1  2     9.87986023e-01   # F_{12}
  2  1     9.87986023e-01   # F_{21}
  2  2    -1.54543256e-01   # F_{22}
Block gauge Q= 1.01137151e+03  # SM gauge couplings
     1     3.62237819e-01   # g'(Q)MSSM DRbar
     2     6.42241429e-01   # g(Q)MSSM DRbar
     3     1.05665582e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.01137151e+03  
  3  3     8.60925953e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.01137151e+03  
  3  3     1.35934441e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.01137151e+03  
  3  3     9.96032080e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.01137151e+03 # Higgs mixing parameters
     1     5.71549324e+02    # mu(Q)MSSM DRbar
     2     9.65258839e+00    # tan beta(Q)MSSM DRbar
     3     2.43739203e+02    # higgs vev(Q)MSSM DRbar
     4     1.30571439e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.01137151e+03  # MSSM DRbar SUSY breaking parameters
     1     1.88810870e+02      # M_1(Q)
     2     3.50107706e+02      # M_2(Q)
     3     9.97650977e+02      # M_3(Q)
    21     9.38699908e+05      # mH1^2(Q)
    22    -2.98597375e+05      # mH2^2(Q)
    31     9.90770420e+02      # meL(Q)
    32     9.90756913e+02      # mmuL(Q)
    33     9.86739272e+02      # mtauL(Q)
    34     9.62267599e+02      # meR(Q)
    35     9.62239650e+02      # mmuR(Q)
    36     9.53905726e+02      # mtauR(Q)
    41     1.29509781e+03      # mqL1(Q)
    42     1.29509307e+03      # mqL2(Q)
    43     1.12442280e+03      # mqL3(Q)
    44     1.27406526e+03      # muR(Q)
    45     1.27406015e+03      # mcR(Q)
    46     8.98215661e+02      # mtR(Q)
    47     1.27161457e+03      # mdR(Q)
    48     1.27160996e+03      # msR(Q)
    49     1.26274984e+03      # mbR(Q)
Block au Q= 1.01137151e+03  
  1  1    -1.01843200e+03      # Au(Q)MSSM DRbar
  2  2    -1.01842745e+03      # Ac(Q)MSSM DRbar
  3  3    -7.84780531e+02      # At(Q)MSSM DRbar
Block ad Q= 1.01137151e+03  
  1  1    -1.24684803e+03      # Ad(Q)MSSM DRbar
  2  2    -1.24684382e+03      # As(Q)MSSM DRbar
  3  3    -1.16476577e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.01137151e+03  
  1  1    -2.68750273e+02      # Ae(Q)MSSM DRbar
  2  2    -2.68745460e+02      # Amu(Q)MSSM DRbar
  3  3    -2.67316280e+02      # Atau(Q)MSSM DRbar
