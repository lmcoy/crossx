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
     1    4.50000000e+02   # m0
     2    6.75000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.77099207e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03889122e+01   # MW
        25     1.16894565e+02   # h0
        35     1.02973530e+03   # H0
        36     1.02946881e+03   # A0
        37     1.03290454e+03   # H+
   1000021     1.52394535e+03   # ~g
   1000022     2.81626332e+02   # ~neutralino(1)
   1000023     5.33061679e+02   # ~neutralino(2)
   1000024     5.33262641e+02   # ~chargino(1)
   1000025    -8.26230993e+02   # ~neutralino(3)
   1000035     8.38043269e+02   # ~neutralino(4)
   1000037     8.37659640e+02   # ~chargino(2)
   1000001     1.44834094e+03   # ~d_L
   1000002     1.44633881e+03   # ~u_L
   1000003     1.44833721e+03   # ~s_L
   1000004     1.44633508e+03   # ~c_L
   1000005     1.31714050e+03   # ~b_1
   1000006     1.10255622e+03   # ~t_1
   1000011     6.37627681e+02   # ~e_L
   1000012     6.32503559e+02   # ~nue_L
   1000013     6.37809399e+02   # ~mu_L
   1000014     6.32496478e+02   # ~numu_L
   1000015     5.10126168e+02   # ~stau_1
   1000016     6.30192990e+02   # ~nu_tau_L
   2000001     1.39091800e+03   # ~d_R
   2000002     1.39590633e+03   # ~u_R
   2000003     1.39091416e+03   # ~s_R
   2000004     1.39590231e+03   # ~c_R
   2000005     1.38440936e+03   # ~b_2
   2000006     1.34949316e+03   # ~t_2
   2000011     5.17270425e+02   # ~e_R
   2000013     5.17252876e+02   # ~mu_R
   2000015     6.36570900e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05289155e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97504747e-01   # N_{1,1}
  1  2    -1.03213341e-02   # N_{1,2}
  1  3     6.40951227e-02   # N_{1,3}
  1  4    -2.77410487e-02   # N_{1,4}
  2  1     2.40652623e-02   # N_{2,1}
  2  2     9.78849845e-01   # N_{2,2}
  2  3    -1.66539640e-01   # N_{2,3}
  2  4     1.16354593e-01   # N_{2,4}
  3  1    -2.52387105e-02   # N_{3,1}
  3  2     3.64313180e-02   # N_{3,2}
  3  3     7.05004279e-01   # N_{3,3}
  3  4     7.07816879e-01   # N_{3,4}
  4  1    -6.13852679e-02   # N_{4,1}
  4  2     2.01045291e-01   # N_{4,2}
  4  3     6.86385701e-01   # N_{4,3}
  4  4    -6.96194879e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.71944013e-01   # U_{1,1}
  1  2    -2.35212319e-01   # U_{1,2}
  2  1     2.35212319e-01   # U_{2,1}
  2  2     9.71944013e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86119259e-01   # V_{1,1}
  1  2    -1.66038571e-01   # V_{1,2}
  2  1     1.66038571e-01   # V_{2,1}
  2  2     9.86119259e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.29937345e-01   # F_{11}
  1  2     9.44002833e-01   # F_{12}
  2  1     9.44002833e-01   # F_{21}
  2  2    -3.29937345e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.92006738e-01   # F_{11}
  1  2     1.26184908e-01   # F_{12}
  2  1    -1.26184908e-01   # F_{21}
  2  2     9.92006738e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.03806905e-01   # F_{11}
  1  2     9.94597470e-01   # F_{12}
  2  1     9.94597470e-01   # F_{21}
  2  2    -1.03806905e-01   # F_{22}
Block gauge Q= 1.18416096e+03  # SM gauge couplings
     1     3.62869781e-01   # g'(Q)MSSM DRbar
     2     6.41216610e-01   # g(Q)MSSM DRbar
     3     1.04544016e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18416096e+03  
  3  3     8.51442057e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18416096e+03  
  3  3     1.33431987e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18416096e+03  
  3  3     1.00206288e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18416096e+03 # Higgs mixing parameters
     1     8.20365922e+02    # mu(Q)MSSM DRbar
     2     9.63740724e+00    # tan beta(Q)MSSM DRbar
     3     2.43728717e+02    # higgs vev(Q)MSSM DRbar
     4     1.09415741e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18416096e+03  # MSSM DRbar SUSY breaking parameters
     1     2.86365344e+02      # M_1(Q)
     2     5.27763607e+02      # M_2(Q)
     3     1.47089124e+03      # M_3(Q)
    21     3.64942178e+05      # mH1^2(Q)
    22    -6.43271356e+05      # mH2^2(Q)
    31     6.31160087e+02      # meL(Q)
    32     6.31152969e+02      # mmuL(Q)
    33     6.29001188e+02      # mtauL(Q)
    34     5.12686976e+02      # meR(Q)
    35     5.12669275e+02      # mmuR(Q)
    36     5.07298353e+02      # mtauR(Q)
    41     1.40106562e+03      # mqL1(Q)
    42     1.40106181e+03      # mqL2(Q)
    43     1.28042024e+03      # mqL3(Q)
    44     1.35172893e+03      # muR(Q)
    45     1.35172483e+03      # mcR(Q)
    46     1.08885712e+03      # mtR(Q)
    47     1.34569678e+03      # mdR(Q)
    48     1.34569287e+03      # msR(Q)
    49     1.33851150e+03      # mbR(Q)
Block au Q= 1.18416096e+03  
  1  1    -1.49040759e+03      # Au(Q)MSSM DRbar
  2  2    -1.49040098e+03      # Ac(Q)MSSM DRbar
  3  3    -1.15498185e+03      # At(Q)MSSM DRbar
Block ad Q= 1.18416096e+03  
  1  1    -1.81736756e+03      # Ad(Q)MSSM DRbar
  2  2    -1.81736146e+03      # As(Q)MSSM DRbar
  3  3    -1.69964167e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.18416096e+03  
  1  1    -3.98607813e+02      # Ae(Q)MSSM DRbar
  2  2    -3.98600780e+02      # Amu(Q)MSSM DRbar
  3  3    -3.96476829e+02      # Atau(Q)MSSM DRbar
