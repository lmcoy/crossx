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
     1    7.00000000e+02   # m0
     2    6.00000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.84350400e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03886092e+01   # MW
        25     1.18041726e+02   # h0
        35     8.06852409e+02   # H0
        36     8.06781335e+02   # A0
        37     8.11101485e+02   # H+
   1000021     1.38405489e+03   # ~g
   1000022     2.51957674e+02   # ~neutralino(1)
   1000023     4.79887260e+02   # ~neutralino(2)
   1000024     4.79976720e+02   # ~chargino(1)
   1000025    -8.00366783e+02   # ~neutralino(3)
   1000035     8.08675629e+02   # ~neutralino(4)
   1000037     8.09060851e+02   # ~chargino(2)
   1000001     1.41604330e+03   # ~d_L
   1000002     1.41397755e+03   # ~u_L
   1000003     1.41600190e+03   # ~s_L
   1000004     1.41393608e+03   # ~c_L
   1000005     1.17749681e+03   # ~b_1
   1000006     1.00407080e+03   # ~t_1
   1000011     8.05697866e+02   # ~e_L
   1000012     8.01473115e+02   # ~nue_L
   1000013     8.05621328e+02   # ~mu_L
   1000014     8.01275254e+02   # ~numu_L
   1000015     5.63326993e+02   # ~stau_1
   1000016     7.33670416e+02   # ~nu_tau_L
   2000001     1.37095666e+03   # ~d_R
   2000002     1.37464477e+03   # ~u_R
   2000003     1.37087528e+03   # ~s_R
   2000004     1.37463946e+03   # ~c_R
   2000005     1.25389932e+03   # ~b_2
   2000006     1.23010193e+03   # ~t_2
   2000011     7.35512088e+02   # ~e_R
   2000013     7.35076857e+02   # ~mu_R
   2000015     7.48846257e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59490757e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97721876e-01   # N_{1,1}
  1  2    -7.90290240e-03   # N_{1,2}
  1  3     6.33760665e-02   # N_{1,3}
  1  4    -2.17273328e-02   # N_{1,4}
  2  1     1.94562160e-02   # N_{2,1}
  2  2     9.83845706e-01   # N_{2,2}
  2  3    -1.51736679e-01   # N_{2,3}
  2  4     9.29788259e-02   # N_{2,4}
  3  1    -2.90078379e-02   # N_{3,1}
  3  2     4.23543891e-02   # N_{3,2}
  3  3     7.04589641e-01   # N_{3,3}
  3  4     7.07755670e-01   # N_{3,4}
  4  1    -5.77153330e-02   # N_{4,1}
  4  2     1.73756370e-01   # N_{4,2}
  4  3     6.90299132e-01   # N_{4,3}
  4  4    -6.99974837e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.76835842e-01   # U_{1,1}
  1  2    -2.13990040e-01   # U_{1,2}
  2  1     2.13990040e-01   # U_{2,1}
  2  2     9.76835842e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91068016e-01   # V_{1,1}
  1  2    -1.33357370e-01   # V_{1,2}
  2  1     1.33357370e-01   # V_{2,1}
  2  2     9.91068016e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.86633313e-01   # F_{11}
  1  2     9.22233529e-01   # F_{12}
  2  1     9.22233529e-01   # F_{21}
  2  2    -3.86633313e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.06382899e-01   # F_{11}
  1  2     4.22457147e-01   # F_{12}
  2  1    -4.22457147e-01   # F_{21}
  2  2     9.06382899e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.53567598e-01   # F_{11}
  1  2     9.67317669e-01   # F_{12}
  2  1     9.67317669e-01   # F_{21}
  2  2    -2.53567598e-01   # F_{22}
Block gauge Q= 1.07991182e+03  # SM gauge couplings
     1     3.62459844e-01   # g'(Q)MSSM DRbar
     2     6.41114348e-01   # g(Q)MSSM DRbar
     3     1.04982510e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.07991182e+03  
  3  3     8.49340749e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.07991182e+03  
  3  3     4.95936066e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.07991182e+03  
  3  3     4.23680139e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.07991182e+03 # Higgs mixing parameters
     1     7.95932777e+02    # mu(Q)MSSM DRbar
     2     3.91836819e+01    # tan beta(Q)MSSM DRbar
     3     2.43765150e+02    # higgs vev(Q)MSSM DRbar
     4     8.32287721e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.07991182e+03  # MSSM DRbar SUSY breaking parameters
     1     2.54874843e+02      # M_1(Q)
     2     4.70870465e+02      # M_2(Q)
     3     1.31978258e+03      # M_3(Q)
    21     3.02252795e+04      # mH1^2(Q)
    22    -6.19218377e+05      # mH2^2(Q)
    31     8.01542435e+02      # meL(Q)
    32     8.01344525e+02      # mmuL(Q)
    33     7.36148548e+02      # mtauL(Q)
    34     7.32531650e+02      # meR(Q)
    35     7.32095110e+02      # mmuR(Q)
    36     5.77375499e+02      # mtauR(Q)
    41     1.37567334e+03      # mqL1(Q)
    42     1.37563051e+03      # mqL2(Q)
    43     1.15997576e+03      # mqL3(Q)
    44     1.33677145e+03      # muR(Q)
    45     1.33676597e+03      # mcR(Q)
    46     9.99603830e+02      # mtR(Q)
    47     1.33211543e+03      # mdR(Q)
    48     1.33203146e+03      # msR(Q)
    49     1.20519669e+03      # mbR(Q)
Block au Q= 1.07991182e+03  
  1  1    -1.68093528e+03      # Au(Q)MSSM DRbar
  2  2    -1.68089540e+03      # Ac(Q)MSSM DRbar
  3  3    -1.17389009e+03      # At(Q)MSSM DRbar
Block ad Q= 1.07991182e+03  
  1  1    -1.94217060e+03      # Ad(Q)MSSM DRbar
  2  2    -1.94206907e+03      # As(Q)MSSM DRbar
  3  3    -1.63448502e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.07991182e+03  
  1  1    -6.62797971e+02      # Ae(Q)MSSM DRbar
  2  2    -6.62471834e+02      # Amu(Q)MSSM DRbar
  3  3    -5.55158005e+02      # Atau(Q)MSSM DRbar
