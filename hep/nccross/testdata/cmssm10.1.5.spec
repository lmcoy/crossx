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
     1    1.75000000e+02   # m0
     2    7.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.67758832e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03891195e+01   # MW
        25     1.17041891e+02   # h0
        35     9.77391172e+02   # H0
        36     9.77173911e+02   # A0
        37     9.80685468e+02   # H+
   1000021     1.56483266e+03   # ~g
   1000022     2.91304906e+02   # ~neutralino(1)
   1000023     5.51252542e+02   # ~neutralino(2)
   1000024     5.51453663e+02   # ~chargino(1)
   1000025    -8.53985592e+02   # ~neutralino(3)
   1000035     8.65424482e+02   # ~neutralino(4)
   1000037     8.65065598e+02   # ~chargino(2)
   1000001     1.43588609e+03   # ~d_L
   1000002     1.43385855e+03   # ~u_L
   1000003     1.43588263e+03   # ~s_L
   1000004     1.43385509e+03   # ~c_L
   1000005     1.31648106e+03   # ~b_1
   1000006     1.10981662e+03   # ~t_1
   1000011     5.01784496e+02   # ~e_L
   1000012     4.95354298e+02   # ~nue_L
   1000013     5.01845552e+02   # ~mu_L
   1000014     4.95349769e+02   # ~numu_L
   1000015     3.11196636e+02   # ~stau_1
   1000016     4.93766512e+02   # ~nu_tau_L
   2000001     1.37282112e+03   # ~d_R
   2000002     1.37833264e+03   # ~u_R
   2000003     1.37281751e+03   # ~s_R
   2000004     1.37832892e+03   # ~c_R
   2000005     1.36730720e+03   # ~b_2
   2000006     1.35166742e+03   # ~t_2
   2000011     3.18466967e+02   # ~e_R
   2000013     3.18452669e+02   # ~mu_R
   2000015     5.01781233e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05491382e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97677917e-01   # N_{1,1}
  1  2    -9.66213081e-03   # N_{1,2}
  1  3     6.18648248e-02   # N_{1,3}
  1  4    -2.67985142e-02   # N_{1,4}
  2  1     2.25527559e-02   # N_{2,1}
  2  2     9.80088824e-01   # N_{2,2}
  2  3    -1.61644862e-01   # N_{2,3}
  2  4     1.13084964e-01   # N_{2,4}
  3  1    -2.43725147e-02   # N_{3,1}
  3  2     3.51937327e-02   # N_{3,2}
  3  3     7.05139015e-01   # N_{3,3}
  3  4     7.07775637e-01   # N_{3,4}
  4  1    -5.94653463e-02   # N_{4,1}
  4  2     1.95176693e-01   # N_{4,2}
  4  3     6.87621009e-01   # N_{4,3}
  4  4    -6.96812226e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73744124e-01   # U_{1,1}
  1  2    -2.27645298e-01   # U_{1,2}
  2  1     2.27645298e-01   # U_{2,1}
  2  2     9.73744124e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86997202e-01   # V_{1,1}
  1  2    -1.60737436e-01   # V_{1,2}
  2  1     1.60737436e-01   # V_{2,1}
  2  2     9.86997202e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.48634588e-01   # F_{11}
  1  2     9.37258728e-01   # F_{12}
  2  1     9.37258728e-01   # F_{21}
  2  2    -3.48634588e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.84770266e-01   # F_{11}
  1  2     1.73860643e-01   # F_{12}
  2  1    -1.73860643e-01   # F_{21}
  2  2     9.84770266e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.00645367e-01   # F_{11}
  1  2     9.94922364e-01   # F_{12}
  2  1     9.94922364e-01   # F_{21}
  2  2    -1.00645367e-01   # F_{22}
Block gauge Q= 1.18938077e+03  # SM gauge couplings
     1     3.63061441e-01   # g'(Q)MSSM DRbar
     2     6.41310014e-01   # g(Q)MSSM DRbar
     3     1.04482581e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18938077e+03  
  3  3     8.50716754e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18938077e+03  
  3  3     1.33190913e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18938077e+03  
  3  3     1.00304658e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18938077e+03 # Higgs mixing parameters
     1     8.48464977e+02    # mu(Q)MSSM DRbar
     2     9.63736295e+00    # tan beta(Q)MSSM DRbar
     3     2.43746166e+02    # higgs vev(Q)MSSM DRbar
     4     9.89104689e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18938077e+03  # MSSM DRbar SUSY breaking parameters
     1     2.97327800e+02      # M_1(Q)
     2     5.47572422e+02      # M_2(Q)
     3     1.52282634e+03      # M_3(Q)
    21     2.13389137e+05      # mH1^2(Q)
    22    -6.91702289e+05      # mH2^2(Q)
    31     4.92939177e+02      # meL(Q)
    32     4.92934631e+02      # mmuL(Q)
    33     4.91558803e+02      # mtauL(Q)
    34     3.10286163e+02      # meR(Q)
    35     3.10271474e+02      # mmuR(Q)
    36     3.05798687e+02      # mtauR(Q)
    41     1.38759802e+03      # mqL1(Q)
    42     1.38759450e+03      # mqL2(Q)
    43     1.28009420e+03      # mqL3(Q)
    44     1.33342207e+03      # muR(Q)
    45     1.33341830e+03      # mcR(Q)
    46     1.09942371e+03      # mtR(Q)
    47     1.32676101e+03      # mdR(Q)
    48     1.32675735e+03      # msR(Q)
    49     1.32010162e+03      # mbR(Q)
Block au Q= 1.18938077e+03  
  1  1    -1.54201492e+03      # Au(Q)MSSM DRbar
  2  2    -1.54200809e+03      # Ac(Q)MSSM DRbar
  3  3    -1.19579980e+03      # At(Q)MSSM DRbar
Block ad Q= 1.18938077e+03  
  1  1    -1.87941518e+03      # Ad(Q)MSSM DRbar
  2  2    -1.87940888e+03      # As(Q)MSSM DRbar
  3  3    -1.75791750e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.18938077e+03  
  1  1    -4.12824497e+02      # Ae(Q)MSSM DRbar
  2  2    -4.12817228e+02      # Amu(Q)MSSM DRbar
  3  3    -4.10617134e+02      # Atau(Q)MSSM DRbar
