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
     1    7.50000000e+02   # m0
     2    3.50000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.31298275e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03964484e+01   # MW
        25     1.13056977e+02   # h0
        35     8.96503274e+02   # H0
        36     8.96450622e+02   # A0
        37     9.00113606e+02   # H+
   1000021     8.63201748e+02   # ~g
   1000022     1.41973073e+02   # ~neutralino(1)
   1000023     2.67298330e+02   # ~neutralino(2)
   1000024     2.67304363e+02   # ~chargino(1)
   1000025    -4.69710118e+02   # ~neutralino(3)
   1000035     4.86827424e+02   # ~neutralino(4)
   1000037     4.86321266e+02   # ~chargino(2)
   1000001     1.04981438e+03   # ~d_L
   1000002     1.04700768e+03   # ~u_L
   1000003     1.04981071e+03   # ~s_L
   1000004     1.04700400e+03   # ~c_L
   1000005     9.10507531e+02   # ~b_1
   1000006     7.24401178e+02   # ~t_1
   1000011     7.84038173e+02   # ~e_L
   1000012     7.79742198e+02   # ~nue_L
   1000013     7.84058464e+02   # ~mu_L
   1000014     7.79731364e+02   # ~numu_L
   1000015     7.53605232e+02   # ~stau_1
   1000016     7.76425088e+02   # ~nu_tau_L
   2000001     1.02998201e+03   # ~d_R
   2000002     1.03083230e+03   # ~u_R
   2000003     1.02997843e+03   # ~s_R
   2000004     1.03082835e+03   # ~c_R
   2000005     1.02310778e+03   # ~b_2
   2000006     9.40685787e+02   # ~t_2
   2000011     7.61569146e+02   # ~e_R
   2000013     7.61546861e+02   # ~mu_R
   2000015     7.81833198e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05405084e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.91954445e-01   # N_{1,1}
  1  2    -3.20014204e-02   # N_{1,2}
  1  3     1.13830228e-01   # N_{1,3}
  1  4    -4.52213128e-02   # N_{1,4}
  2  1     6.59733330e-02   # N_{2,1}
  2  2     9.54766747e-01   # N_{2,2}
  2  3    -2.44725234e-01   # N_{2,3}
  2  4     1.55491277e-01   # N_{2,4}
  3  1    -4.58590247e-02   # N_{3,1}
  3  2     6.71567839e-02   # N_{3,2}
  3  3     7.00267768e-01   # N_{3,3}
  3  4     7.09233367e-01   # N_{3,4}
  4  1    -9.78307111e-02   # N_{4,1}
  4  2     2.87899867e-01   # N_{4,2}
  4  3     6.60891286e-01   # N_{4,3}
  4  4    -6.86123551e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.36947059e-01   # U_{1,1}
  1  2    -3.49471326e-01   # U_{1,2}
  2  1     3.49471326e-01   # U_{2,1}
  2  2     9.36947059e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.74355134e-01   # V_{1,1}
  1  2    -2.25015718e-01   # V_{1,2}
  2  1     2.25015718e-01   # V_{2,1}
  2  2     9.74355134e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.08898189e-01   # F_{11}
  1  2     9.51095110e-01   # F_{12}
  2  1     9.51095110e-01   # F_{21}
  2  2    -3.08898189e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98173268e-01   # F_{11}
  1  2     6.04162848e-02   # F_{12}
  2  1    -6.04162848e-02   # F_{21}
  2  2     9.98173268e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.99402982e-01   # F_{11}
  1  2     9.79917573e-01   # F_{12}
  2  1     9.79917573e-01   # F_{21}
  2  2    -1.99402982e-01   # F_{22}
Block gauge Q= 8.02108698e+02  # SM gauge couplings
     1     3.61744459e-01   # g'(Q)MSSM DRbar
     2     6.43484261e-01   # g(Q)MSSM DRbar
     3     1.06904150e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.02108698e+02  
  3  3     8.69041368e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.02108698e+02  
  3  3     1.37624996e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.02108698e+02  
  3  3     9.97678829e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.02108698e+02 # Higgs mixing parameters
     1     4.62134331e+02    # mu(Q)MSSM DRbar
     2     9.68061398e+00    # tan beta(Q)MSSM DRbar
     3     2.44040915e+02    # higgs vev(Q)MSSM DRbar
     4     8.20778082e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.02108698e+02  # MSSM DRbar SUSY breaking parameters
     1     1.45226160e+02      # M_1(Q)
     2     2.70906028e+02      # M_2(Q)
     3     7.90012653e+02      # M_3(Q)
    21     5.83328879e+05      # mH1^2(Q)
    22    -1.98221194e+05      # mH2^2(Q)
    31     7.81420806e+02      # meL(Q)
    32     7.81410014e+02      # mmuL(Q)
    33     7.78208202e+02      # mtauL(Q)
    34     7.59369565e+02      # meR(Q)
    35     7.59347246e+02      # mmuR(Q)
    36     7.52709197e+02      # mtauR(Q)
    41     1.02506094e+03      # mqL1(Q)
    42     1.02505716e+03      # mqL2(Q)
    43     8.88859610e+02      # mqL3(Q)
    44     1.00897608e+03      # muR(Q)
    45     1.00897202e+03      # mcR(Q)
    46     7.09017104e+02      # mtR(Q)
    47     1.00712616e+03      # mdR(Q)
    48     1.00712247e+03      # msR(Q)
    49     9.99998369e+02      # mbR(Q)
Block au Q= 8.02108698e+02  
  1  1    -8.13495570e+02      # Au(Q)MSSM DRbar
  2  2    -8.13491900e+02      # Ac(Q)MSSM DRbar
  3  3    -6.24407322e+02      # At(Q)MSSM DRbar
Block ad Q= 8.02108698e+02  
  1  1    -9.98877089e+02      # Ad(Q)MSSM DRbar
  2  2    -9.98873682e+02      # As(Q)MSSM DRbar
  3  3    -9.32423499e+02      # Ab(Q)MSSM DRbar
Block ae Q= 8.02108698e+02  
  1  1    -2.11385533e+02      # Ae(Q)MSSM DRbar
  2  2    -2.11381690e+02      # Amu(Q)MSSM DRbar
  3  3    -2.10243557e+02      # Atau(Q)MSSM DRbar
