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
     1    4.00000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.83925327e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03899447e+01   # MW
        25     1.16162599e+02   # h0
        35     9.23431750e+02   # H0
        36     9.23122003e+02   # A0
        37     9.26953518e+02   # H+
   1000021     1.36671065e+03   # ~g
   1000022     2.48734851e+02   # ~neutralino(1)
   1000023     4.70780886e+02   # ~neutralino(2)
   1000024     4.70962671e+02   # ~chargino(1)
   1000025    -7.45501100e+02   # ~neutralino(3)
   1000035     7.58036234e+02   # ~neutralino(4)
   1000037     7.57643996e+02   # ~chargino(2)
   1000001     1.29918619e+03   # ~d_L
   1000002     1.29693321e+03   # ~u_L
   1000003     1.29918283e+03   # ~s_L
   1000004     1.29692984e+03   # ~c_L
   1000005     1.18103217e+03   # ~b_1
   1000006     9.85395496e+02   # ~t_1
   1000011     5.67741715e+02   # ~e_L
   1000012     5.62012198e+02   # ~nue_L
   1000013     5.67922836e+02   # ~mu_L
   1000014     5.62005849e+02   # ~numu_L
   1000015     4.53536126e+02   # ~stau_1
   1000016     5.59943967e+02   # ~nu_tau_L
   2000001     1.24831367e+03   # ~d_R
   2000002     1.25253063e+03   # ~u_R
   2000003     1.24831020e+03   # ~s_R
   2000004     1.25252701e+03   # ~c_R
   2000005     1.24267094e+03   # ~b_2
   2000006     1.21675889e+03   # ~t_2
   2000011     4.60314125e+02   # ~e_R
   2000013     4.60298413e+02   # ~mu_R
   2000015     5.67109703e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05593294e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96945485e-01   # N_{1,1}
  1  2    -1.26778611e-02   # N_{1,2}
  1  3     7.08938889e-02   # N_{1,3}
  1  4    -3.02163487e-02   # N_{1,4}
  2  1     2.88262768e-02   # N_{2,1}
  2  2     9.75821083e-01   # N_{2,2}
  2  3    -1.78565119e-01   # N_{2,3}
  2  4     1.22705982e-01   # N_{2,4}
  3  1    -2.81213929e-02   # N_{3,1}
  3  2     4.07197433e-02   # N_{3,2}
  3  3     7.04494627e-01   # N_{3,3}
  3  4     7.07981928e-01   # N_{3,4}
  4  1    -6.69173550e-02   # N_{4,1}
  4  2     2.14369746e-01   # N_{4,2}
  4  3     6.83209979e-01   # N_{4,3}
  4  4    -6.94832213e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.67617290e-01   # U_{1,1}
  1  2    -2.52421828e-01   # U_{1,2}
  2  1     2.52421828e-01   # U_{2,1}
  2  2     9.67617290e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.84510276e-01   # V_{1,1}
  1  2    -1.75326885e-01   # V_{1,2}
  2  1     1.75326885e-01   # V_{2,1}
  2  2     9.84510276e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.57606514e-01   # F_{11}
  1  2     9.33872358e-01   # F_{12}
  2  1     9.33872358e-01   # F_{21}
  2  2    -3.57606514e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.90232262e-01   # F_{11}
  1  2     1.39427640e-01   # F_{12}
  2  1    -1.39427640e-01   # F_{21}
  2  2     9.90232262e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.17317345e-01   # F_{11}
  1  2     9.93094477e-01   # F_{12}
  2  1     9.93094477e-01   # F_{21}
  2  2    -1.17317345e-01   # F_{22}
Block gauge Q= 1.06248430e+03  # SM gauge couplings
     1     3.62643319e-01   # g'(Q)MSSM DRbar
     2     6.41801759e-01   # g(Q)MSSM DRbar
     3     1.05102681e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.06248430e+03  
  3  3     8.55078113e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.06248430e+03  
  3  3     1.34168988e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.06248430e+03  
  3  3     1.00286384e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.06248430e+03 # Higgs mixing parameters
     1     7.39753761e+02    # mu(Q)MSSM DRbar
     2     9.65001584e+00    # tan beta(Q)MSSM DRbar
     3     2.43853262e+02    # higgs vev(Q)MSSM DRbar
     4     8.80209822e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.06248430e+03  # MSSM DRbar SUSY breaking parameters
     1     2.53242162e+02      # M_1(Q)
     2     4.68027832e+02      # M_2(Q)
     3     1.31814344e+03      # M_3(Q)
    21     2.88449594e+05      # mH1^2(Q)
    22    -5.24478369e+05      # mH2^2(Q)
    31     5.61698311e+02      # meL(Q)
    32     5.61691939e+02      # mmuL(Q)
    33     5.59767891e+02      # mtauL(Q)
    34     4.55809598e+02      # meR(Q)
    35     4.55793735e+02      # mmuR(Q)
    36     4.50986237e+02      # mtauR(Q)
    41     1.25620680e+03      # mqL1(Q)
    42     1.25620337e+03      # mqL2(Q)
    43     1.14777534e+03      # mqL3(Q)
    44     1.21258407e+03      # muR(Q)
    45     1.21258039e+03      # mcR(Q)
    46     9.76458519e+02      # mtR(Q)
    47     1.20728047e+03      # mdR(Q)
    48     1.20727694e+03      # msR(Q)
    49     1.20079110e+03      # mbR(Q)
Block au Q= 1.06248430e+03  
  1  1    -1.34117684e+03      # Au(Q)MSSM DRbar
  2  2    -1.34117087e+03      # Ac(Q)MSSM DRbar
  3  3    -1.03748315e+03      # At(Q)MSSM DRbar
Block ad Q= 1.06248430e+03  
  1  1    -1.63760759e+03      # Ad(Q)MSSM DRbar
  2  2    -1.63760207e+03      # As(Q)MSSM DRbar
  3  3    -1.53100115e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.06248430e+03  
  1  1    -3.56207914e+02      # Ae(Q)MSSM DRbar
  2  2    -3.56201585e+02      # Amu(Q)MSSM DRbar
  3  3    -3.54292428e+02      # Atau(Q)MSSM DRbar
