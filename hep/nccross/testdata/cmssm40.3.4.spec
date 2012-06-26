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
     1    1.15000000e+03   # m0
     2    4.25000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=2.12766038e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03913822e+01   # MW
        25     1.16570509e+02   # h0
        35     9.03615690e+02   # H0
        36     9.03728884e+02   # A0
        37     9.07444637e+02   # H+
   1000021     1.04455469e+03   # ~g
   1000022     1.77580867e+02   # ~neutralino(1)
   1000023     3.39303734e+02   # ~neutralino(2)
   1000024     3.39375428e+02   # ~chargino(1)
   1000025    -5.96181057e+02   # ~neutralino(3)
   1000035     6.06726982e+02   # ~neutralino(4)
   1000037     6.07212635e+02   # ~chargino(2)
   1000001     1.43783822e+03   # ~d_L
   1000002     1.43578312e+03   # ~u_L
   1000003     1.43778820e+03   # ~s_L
   1000004     1.43573302e+03   # ~c_L
   1000005     1.12649545e+03   # ~b_1
   1000006     9.33659976e+02   # ~t_1
   1000011     1.18109947e+03   # ~e_L
   1000012     1.17809955e+03   # ~nue_L
   1000013     1.18084463e+03   # ~mu_L
   1000014     1.17780774e+03   # ~numu_L
   1000015     9.52427400e+02   # ~stau_1
   1000016     1.08260696e+03   # ~nu_tau_L
   2000001     1.41774786e+03   # ~d_R
   2000002     1.41882614e+03   # ~u_R
   2000003     1.41765226e+03   # ~s_R
   2000004     1.41881962e+03   # ~c_R
   2000005     1.25107001e+03   # ~b_2
   2000006     1.15886451e+03   # ~t_2
   2000011     1.16036976e+03   # ~e_R
   2000013     1.15977486e+03   # ~mu_R
   2000015     1.08900224e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59444291e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95884387e-01   # N_{1,1}
  1  2    -1.38366187e-02   # N_{1,2}
  1  3     8.51588688e-02   # N_{1,3}
  1  4    -2.77633405e-02   # N_{1,4}
  2  1     3.30802418e-02   # N_{2,1}
  2  2     9.74403435e-01   # N_{2,2}
  2  3    -1.91926622e-01   # N_{2,3}
  2  4     1.12284524e-01   # N_{2,4}
  3  1    -3.95214664e-02   # N_{3,1}
  3  2     5.81048177e-02   # N_{3,2}
  3  3     7.02507476e-01   # N_{3,3}
  3  4     7.08198510e-01   # N_{3,4}
  4  1    -7.45522590e-02   # N_{4,1}
  4  2     2.16726379e-01   # N_{4,2}
  4  3     6.79996607e-01   # N_{4,3}
  4  4    -6.96474158e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.62694955e-01   # U_{1,1}
  1  2    -2.70589032e-01   # U_{1,2}
  2  1     2.70589032e-01   # U_{2,1}
  2  2     9.62694955e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86940527e-01   # V_{1,1}
  1  2    -1.61085058e-01   # V_{1,2}
  2  1     1.61085058e-01   # V_{2,1}
  2  2     9.86940527e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.06490189e-01   # F_{11}
  1  2     9.51873817e-01   # F_{12}
  2  1     9.51873817e-01   # F_{21}
  2  2    -3.06490189e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.82569372e-01   # F_{11}
  1  2     1.85896287e-01   # F_{12}
  2  1    -1.85896287e-01   # F_{21}
  2  2     9.82569372e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.57996584e-01   # F_{11}
  1  2     9.87439659e-01   # F_{12}
  2  1     9.87439659e-01   # F_{21}
  2  2    -1.57996584e-01   # F_{22}
Block gauge Q= 1.01600237e+03  # SM gauge couplings
     1     3.62146716e-01   # g'(Q)MSSM DRbar
     2     6.41957965e-01   # g(Q)MSSM DRbar
     3     1.05665808e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.01600237e+03  
  3  3     8.55880434e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.01600237e+03  
  3  3     5.16655480e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.01600237e+03  
  3  3     4.12725402e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.01600237e+03 # Higgs mixing parameters
     1     5.88326949e+02    # mu(Q)MSSM DRbar
     2     3.92186774e+01    # tan beta(Q)MSSM DRbar
     3     2.43673481e+02    # higgs vev(Q)MSSM DRbar
     4     9.83140507e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.01600237e+03  # MSSM DRbar SUSY breaking parameters
     1     1.79439229e+02      # M_1(Q)
     2     3.32933642e+02      # M_2(Q)
     3     9.45464105e+02      # M_3(Q)
    21     4.90339033e+05      # mH1^2(Q)
    22    -3.31589481e+05      # mH2^2(Q)
    31     1.17826100e+03      # meL(Q)
    32     1.17797000e+03      # mmuL(Q)
    33     1.08517140e+03      # mtauL(Q)
    34     1.15825154e+03      # meR(Q)
    35     1.15765644e+03      # mmuR(Q)
    36     9.57664690e+02      # mtauR(Q)
    41     1.41173927e+03      # mqL1(Q)
    42     1.41168838e+03      # mqL2(Q)
    43     1.10920535e+03      # mqL3(Q)
    44     1.39583005e+03      # muR(Q)
    45     1.39582342e+03      # mcR(Q)
    46     9.19993750e+02      # mtR(Q)
    47     1.39406499e+03      # mdR(Q)
    48     1.39396758e+03      # msR(Q)
    49     1.22588038e+03      # mbR(Q)
Block au Q= 1.01600237e+03  
  1  1    -1.30191496e+03      # Au(Q)MSSM DRbar
  2  2    -1.30188233e+03      # Ac(Q)MSSM DRbar
  3  3    -8.79676362e+02      # At(Q)MSSM DRbar
Block ad Q= 1.01600237e+03  
  1  1    -1.50814727e+03      # Ad(Q)MSSM DRbar
  2  2    -1.50806420e+03      # As(Q)MSSM DRbar
  3  3    -1.24480239e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.01600237e+03  
  1  1    -5.82877078e+02      # Ae(Q)MSSM DRbar
  2  2    -5.82575541e+02      # Amu(Q)MSSM DRbar
  3  3    -4.88725848e+02      # Atau(Q)MSSM DRbar
