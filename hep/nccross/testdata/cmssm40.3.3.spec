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
     1    1.10000000e+03   # m0
     2    4.00000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.16928234e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03920191e+01   # MW
        25     1.16234227e+02   # h0
        35     8.62987776e+02   # H0
        36     8.63108858e+02   # A0
        37     8.66990304e+02   # H+
   1000021     9.88587735e+02   # ~g
   1000022     1.66668343e+02   # ~neutralino(1)
   1000023     3.18506589e+02   # ~neutralino(2)
   1000024     3.18566790e+02   # ~chargino(1)
   1000025    -5.72252810e+02   # ~neutralino(3)
   1000035     5.82806312e+02   # ~neutralino(4)
   1000037     5.83360371e+02   # ~chargino(2)
   1000001     1.36941863e+03   # ~d_L
   1000002     1.36725083e+03   # ~u_L
   1000003     1.36937039e+03   # ~s_L
   1000004     1.36720250e+03   # ~c_L
   1000005     1.06944912e+03   # ~b_1
   1000006     8.83962707e+02   # ~t_1
   1000011     1.12881340e+03   # ~e_L
   1000012     1.12568680e+03   # ~nue_L
   1000013     1.12856561e+03   # ~mu_L
   1000014     1.12540548e+03   # ~numu_L
   1000015     9.09392320e+02   # ~stau_1
   1000016     1.03382164e+03   # ~nu_tau_L
   2000001     1.35073431e+03   # ~d_R
   2000002     1.35163733e+03   # ~u_R
   2000003     1.35064213e+03   # ~s_R
   2000004     1.35163106e+03   # ~c_R
   2000005     1.19078261e+03   # ~b_2
   2000006     1.10343959e+03   # ~t_2
   2000011     1.10966064e+03   # ~e_R
   2000013     1.10908760e+03   # ~mu_R
   2000015     1.04052526e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59700301e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95556569e-01   # N_{1,1}
  1  2    -1.50037290e-02   # N_{1,2}
  1  3     8.85486318e-02   # N_{1,3}
  1  4    -2.83045067e-02   # N_{1,4}
  2  1     3.52759534e-02   # N_{2,1}
  2  2     9.73567114e-01   # N_{2,2}
  2  3    -1.95773478e-01   # N_{2,3}
  2  4     1.12229346e-01   # N_{2,4}
  3  1    -4.13867977e-02   # N_{3,1}
  3  2     6.10265316e-02   # N_{3,2}
  3  3     7.02058877e-01   # N_{3,3}
  3  4     7.08291062e-01   # N_{3,4}
  4  1    -7.68755961e-02   # N_{4,1}
  4  2     2.19585347e-01   # N_{4,2}
  4  3     6.78929465e-01   # N_{4,3}
  4  4    -6.96367145e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.61140537e-01   # U_{1,1}
  1  2    -2.76059537e-01   # U_{1,2}
  2  1     2.76059537e-01   # U_{2,1}
  2  2     9.61140537e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86938225e-01   # V_{1,1}
  1  2    -1.61099159e-01   # V_{1,2}
  2  1     1.61099159e-01   # V_{2,1}
  2  2     9.86938225e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.17836805e-01   # F_{11}
  1  2     9.48145435e-01   # F_{12}
  2  1     9.48145435e-01   # F_{21}
  2  2    -3.17836805e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.81164867e-01   # F_{11}
  1  2     1.93172213e-01   # F_{12}
  2  1    -1.93172213e-01   # F_{21}
  2  2     9.81164867e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.65525145e-01   # F_{11}
  1  2     9.86205570e-01   # F_{12}
  2  1     9.86205570e-01   # F_{21}
  2  2    -1.65525145e-01   # F_{22}
Block gauge Q= 9.64493602e+02  # SM gauge couplings
     1     3.62030118e-01   # g'(Q)MSSM DRbar
     2     6.42222345e-01   # g(Q)MSSM DRbar
     3     1.05942645e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.64493602e+02  
  3  3     8.57714894e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.64493602e+02  
  3  3     5.17374823e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.64493602e+02  
  3  3     4.12633790e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.64493602e+02 # Higgs mixing parameters
     1     5.64387489e+02    # mu(Q)MSSM DRbar
     2     3.92311255e+01    # tan beta(Q)MSSM DRbar
     3     2.43738541e+02    # higgs vev(Q)MSSM DRbar
     4     8.96972881e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.64493602e+02  # MSSM DRbar SUSY breaking parameters
     1     1.68503746e+02      # M_1(Q)
     2     3.13077141e+02      # M_2(Q)
     3     8.93578692e+02      # M_3(Q)
    21     4.44725049e+05      # mH1^2(Q)
    22    -3.06081115e+05      # mH2^2(Q)
    31     1.12606014e+03      # meL(Q)
    32     1.12577965e+03      # mmuL(Q)
    33     1.03648986e+03      # mtauL(Q)
    34     1.10757472e+03      # meR(Q)
    35     1.10700144e+03      # mmuR(Q)
    36     9.14626763e+02      # mtauR(Q)
    41     1.34462887e+03      # mqL1(Q)
    42     1.34457981e+03      # mqL2(Q)
    43     1.05347006e+03      # mqL3(Q)
    44     1.32993053e+03      # muR(Q)
    45     1.32992415e+03      # mcR(Q)
    46     8.71851111e+02      # mtR(Q)
    47     1.32831040e+03      # mdR(Q)
    48     1.32821650e+03      # msR(Q)
    49     1.16651291e+03      # mbR(Q)
Block au Q= 9.64493602e+02  
  1  1    -1.25024206e+03      # Au(Q)MSSM DRbar
  2  2    -1.25021036e+03      # Ac(Q)MSSM DRbar
  3  3    -8.39830074e+02      # At(Q)MSSM DRbar
Block ad Q= 9.64493602e+02  
  1  1    -1.45068736e+03      # Ad(Q)MSSM DRbar
  2  2    -1.45060665e+03      # As(Q)MSSM DRbar
  3  3    -1.19487882e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.64493602e+02  
  1  1    -5.72928253e+02      # Ae(Q)MSSM DRbar
  2  2    -5.72629807e+02      # Amu(Q)MSSM DRbar
  3  3    -4.79847522e+02      # Atau(Q)MSSM DRbar
