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
     1    8.10000000e+04   # lambda
     2    9.00000000e+04   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=9.00000000e+04 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04067372e+01   # MW
        25     1.11534357e+02   # h0
        35     4.18274251e+02   # H0
        36     4.17905188e+02   # A0
        37     4.25915196e+02   # H+
   1000021     7.86217092e+02   # ~g
   1000022     1.29700232e+02   # ~neutralino(1)
   1000023     2.36107381e+02   # ~neutralino(2)
   1000024     2.35589921e+02   # ~chargino(1)
   1000025    -3.36755311e+02   # ~neutralino(3)
   1000035     3.70182550e+02   # ~neutralino(4)
   1000037     3.68831062e+02   # ~chargino(2)
   1000039     1.72773000e-09   # ~gravitino
   1000001     9.35941283e+02   # ~d_L
   1000002     9.32742677e+02   # ~u_L
   1000003     9.35940003e+02   # ~s_L
   1000004     9.32741393e+02   # ~c_L
   1000005     8.86756935e+02   # ~b_1
   1000006     8.30835710e+02   # ~t_1
   1000011     2.87062798e+02   # ~e_L
   1000012     2.75578313e+02   # ~nue_L
   1000013     2.87098435e+02   # ~mu_L
   1000014     2.75577045e+02   # ~numu_L
   1000015     1.37825101e+02   # ~stau_1
   1000016     2.75015891e+02   # ~nu_tau_L
   2000001     8.94990043e+02   # ~d_R
   2000002     8.97036060e+02   # ~u_R
   2000003     8.94988263e+02   # ~s_R
   2000004     8.97035152e+02   # ~c_R
   2000005     9.02930518e+02   # ~b_2
   2000006     9.16951647e+02   # ~t_2
   2000011     1.44100579e+02   # ~e_R
   2000013     1.44095667e+02   # ~mu_R
   2000015     2.88640119e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.74394490e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.80369472e-01   # N_{1,1}
  1  2    -5.18311431e-02   # N_{1,2}
  1  3     1.73494234e-01   # N_{1,3}
  1  4    -7.80319306e-02   # N_{1,4}
  2  1     1.38979059e-01   # N_{2,1}
  2  2     8.58397207e-01   # N_{2,2}
  2  3    -3.96528656e-01   # N_{2,3}
  2  4     2.94285712e-01   # N_{2,4}
  3  1    -6.18480294e-02   # N_{3,1}
  3  2     8.75468857e-02   # N_{3,2}
  3  3     6.95287544e-01   # N_{3,3}
  3  4     7.10693743e-01   # N_{3,4}
  4  1    -1.25440589e-01   # N_{4,1}
  4  2     5.02795495e-01   # N_{4,2}
  4  3     5.73794395e-01   # N_{4,3}
  4  4    -6.34209225e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.16611900e-01   # U_{1,1}
  1  2    -5.77187150e-01   # U_{1,2}
  2  1     5.77187150e-01   # U_{2,1}
  2  2     8.16611900e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.01738963e-01   # V_{1,1}
  1  2    -4.32280976e-01   # V_{1,2}
  2  1     4.32280976e-01   # V_{2,1}
  2  2     9.01738963e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.00730563e-01   # F_{11}
  1  2     9.53709142e-01   # F_{12}
  2  1     9.53709142e-01   # F_{21}
  2  2    -3.00730563e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.08996713e-01   # F_{11}
  1  2     8.60768462e-01   # F_{12}
  2  1     8.60768462e-01   # F_{21}
  2  2    -5.08996713e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.36990031e-01   # F_{11}
  1  2     9.90572426e-01   # F_{12}
  2  1     9.90572426e-01   # F_{21}
  2  2    -1.36990031e-01   # F_{22}
Block gauge Q= 8.53510726e+02  # SM gauge couplings
     1     3.62737400e-01   # g'(Q)MSSM DRbar
     2     6.45475812e-01   # g(Q)MSSM DRbar
     3     1.07056387e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.53510726e+02  
  3  3     8.69834485e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.53510726e+02  
  3  3     2.05723524e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.53510726e+02  
  3  3     1.51536743e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.53510726e+02 # Higgs mixing parameters
     1     3.27672932e+02    # mu(Q)MSSM DRbar
     2     1.45252155e+01    # tan beta(Q)MSSM DRbar
     3     2.43768736e+02    # higgs vev(Q)MSSM DRbar
     4     1.93909138e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.53510726e+02  # MSSM DRbar SUSY breaking parameters
     1     1.36353074e+02      # M_1(Q)
     2     2.58073912e+02      # M_2(Q)
     3     7.13548595e+02      # M_3(Q)
    21     6.86372832e+04      # mH1^2(Q)
    22    -9.55101796e+04      # mH2^2(Q)
    31     2.80608771e+02      # meL(Q)
    32     2.80607521e+02      # mmuL(Q)
    33     2.80226275e+02      # mtauL(Q)
    34     1.33294722e+02      # meR(Q)
    35     1.33289406e+02      # mmuR(Q)
    36     1.31658937e+02      # mtauR(Q)
    41     9.09174504e+02      # mqL1(Q)
    42     9.09173180e+02      # mqL2(Q)
    43     8.77409331e+02      # mqL3(Q)
    44     8.72730171e+02      # muR(Q)
    45     8.72729230e+02      # mcR(Q)
    46     8.07844767e+02      # mtR(Q)
    47     8.69279360e+02      # mdR(Q)
    48     8.69277511e+02      # msR(Q)
    49     8.65666784e+02      # mbR(Q)
Block au Q= 8.53510726e+02  
  1  1    -2.20500119e+02      # Au(Q)MSSM DRbar
  2  2    -2.20499803e+02      # Ac(Q)MSSM DRbar
  3  3    -2.07554076e+02      # At(Q)MSSM DRbar
Block ad Q= 8.53510726e+02  
  1  1    -2.34942618e+02      # Ad(Q)MSSM DRbar
  2  2    -2.34942176e+02      # As(Q)MSSM DRbar
  3  3    -2.30064295e+02      # Ab(Q)MSSM DRbar
Block ae Q= 8.53510726e+02  
  1  1    -2.19383509e+01      # Ae(Q)MSSM DRbar
  2  2    -2.19381884e+01      # Amu(Q)MSSM DRbar
  3  3    -2.18886733e+01      # Atau(Q)MSSM DRbar
