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
     1    1.08000000e+05   # lambda
     2    1.20000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.20000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03992015e+01   # MW
        25     1.13657632e+02   # h0
        35     5.48389844e+02   # H0
        36     5.48105471e+02   # A0
        37     5.54242214e+02   # H+
   1000021     1.01890570e+03   # ~g
   1000022     1.75659204e+02   # ~neutralino(1)
   1000023     3.24198699e+02   # ~neutralino(2)
   1000024     3.24087967e+02   # ~chargino(1)
   1000025    -4.29664042e+02   # ~neutralino(3)
   1000035     4.61896777e+02   # ~neutralino(4)
   1000037     4.60481752e+02   # ~chargino(2)
   1000039     3.07152000e-09   # ~gravitino
   1000001     1.21782085e+03   # ~d_L
   1000002     1.21540846e+03   # ~u_L
   1000003     1.21781920e+03   # ~s_L
   1000004     1.21540680e+03   # ~c_L
   1000005     1.15451965e+03   # ~b_1
   1000006     1.07656355e+03   # ~t_1
   1000011     3.79284486e+02   # ~e_L
   1000012     3.70623591e+02   # ~nue_L
   1000013     3.79290748e+02   # ~mu_L
   1000014     3.70621922e+02   # ~numu_L
   1000015     1.83226478e+02   # ~stau_1
   1000016     3.69885786e+02   # ~nu_tau_L
   2000001     1.16292472e+03   # ~d_R
   2000002     1.16640517e+03   # ~u_R
   2000003     1.16292242e+03   # ~s_R
   2000004     1.16640399e+03   # ~c_R
   2000005     1.17313753e+03   # ~b_2
   2000006     1.18360754e+03   # ~t_2
   2000011     1.88972304e+02   # ~e_R
   2000013     1.88965677e+02   # ~mu_R
   2000015     3.80084210e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.39902839e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.88405422e-01   # N_{1,1}
  1  2    -3.18328027e-02   # N_{1,2}
  1  3     1.34365004e-01   # N_{1,3}
  1  4    -6.31461769e-02   # N_{1,4}
  2  1     9.82343132e-02   # N_{2,1}
  2  2     8.72153260e-01   # N_{2,2}
  2  3    -3.76820424e-01   # N_{2,3}
  2  4     2.96150432e-01   # N_{2,4}
  3  1    -4.76996513e-02   # N_{3,1}
  3  2     6.70062037e-02   # N_{3,2}
  3  3     7.00098565e-01   # N_{3,3}
  3  4     7.09293248e-01   # N_{3,4}
  4  1    -1.05496370e-01   # N_{4,1}
  4  2     4.83575777e-01   # N_{4,2}
  4  3     5.91451108e-01   # N_{4,3}
  4  4    -6.36561521e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.40370501e-01   # U_{1,1}
  1  2    -5.42012381e-01   # U_{1,2}
  2  1     5.42012381e-01   # U_{2,1}
  2  2     8.40370501e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.03061671e-01   # V_{1,1}
  1  2    -4.29510907e-01   # V_{1,2}
  2  1     4.29510907e-01   # V_{2,1}
  2  2     9.03061671e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.39611323e-01   # F_{11}
  1  2     9.70868896e-01   # F_{12}
  2  1     9.70868896e-01   # F_{21}
  2  2    -2.39611323e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.10632856e-01   # F_{11}
  1  2     9.11800777e-01   # F_{12}
  2  1     9.11800777e-01   # F_{21}
  2  2    -4.10632856e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.01454436e-01   # F_{11}
  1  2     9.94840187e-01   # F_{12}
  2  1     9.94840187e-01   # F_{21}
  2  2    -1.01454436e-01   # F_{22}
Block gauge Q= 1.10539593e+03  # SM gauge couplings
     1     3.63291239e-01   # g'(Q)MSSM DRbar
     2     6.43999387e-01   # g(Q)MSSM DRbar
     3     1.05665984e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.10539593e+03  
  3  3     8.60596586e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.10539593e+03  
  3  3     2.02935982e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.10539593e+03  
  3  3     1.51295882e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.10539593e+03 # Higgs mixing parameters
     1     4.21084380e+02    # mu(Q)MSSM DRbar
     2     1.44806158e+01    # tan beta(Q)MSSM DRbar
     3     2.43449137e+02    # higgs vev(Q)MSSM DRbar
     4     3.32829646e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.10539593e+03  # MSSM DRbar SUSY breaking parameters
     1     1.82412805e+02      # M_1(Q)
     2     3.42665440e+02      # M_2(Q)
     3     9.27062219e+02      # M_3(Q)
    21     1.22017733e+05      # mH1^2(Q)
    22    -1.53594221e+05      # mH2^2(Q)
    31     3.72681103e+02      # meL(Q)
    32     3.72679437e+02      # mmuL(Q)
    33     3.72169931e+02      # mtauL(Q)
    34     1.78534480e+02      # meR(Q)
    35     1.78527459e+02      # mmuR(Q)
    36     1.76367181e+02      # mtauR(Q)
    41     1.18471292e+03      # mqL1(Q)
    42     1.18471121e+03      # mqL2(Q)
    43     1.14373328e+03      # mqL3(Q)
    44     1.13541884e+03      # muR(Q)
    45     1.13541762e+03      # mcR(Q)
    46     1.05157037e+03      # mtR(Q)
    47     1.13066278e+03      # mdR(Q)
    48     1.13066039e+03      # msR(Q)
    49     1.12602364e+03      # mbR(Q)
Block au Q= 1.10539593e+03  
  1  1    -2.82993373e+02      # Au(Q)MSSM DRbar
  2  2    -2.82992972e+02      # Ac(Q)MSSM DRbar
  3  3    -2.66573417e+02      # At(Q)MSSM DRbar
Block ad Q= 1.10539593e+03  
  1  1    -3.01190953e+02      # Ad(Q)MSSM DRbar
  2  2    -3.01190394e+02      # As(Q)MSSM DRbar
  3  3    -2.95010114e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.10539593e+03  
  1  1    -2.93101939e+01      # Ae(Q)MSSM DRbar
  2  2    -2.93099773e+01      # Amu(Q)MSSM DRbar
  3  3    -2.92437367e+01      # Atau(Q)MSSM DRbar
