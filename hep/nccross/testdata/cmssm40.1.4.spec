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
     1    3.75000000e+02   # m0
     2    6.50000000e+02   # m12
     5   -5.00000000e+02   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.71536983e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03882538e+01   # MW
        25     1.18305518e+02   # h0
        35     7.49610052e+02   # H0
        36     7.49517237e+02   # A0
        37     7.54118245e+02   # H+
   1000021     1.46723062e+03   # ~g
   1000022     2.72325078e+02   # ~neutralino(1)
   1000023     5.18119601e+02   # ~neutralino(2)
   1000024     5.18210941e+02   # ~chargino(1)
   1000025    -8.60779672e+02   # ~neutralino(3)
   1000035     8.68395839e+02   # ~neutralino(4)
   1000037     8.68775408e+02   # ~chargino(2)
   1000001     1.38373298e+03   # ~d_L
   1000002     1.38158054e+03   # ~u_L
   1000003     1.38369489e+03   # ~s_L
   1000004     1.38154238e+03   # ~c_L
   1000005     1.16855776e+03   # ~b_1
   1000006     1.01164863e+03   # ~t_1
   1000011     5.75687953e+02   # ~e_L
   1000012     5.69950599e+02   # ~nue_L
   1000013     5.75713615e+02   # ~mu_L
   1000014     5.69808126e+02   # ~numu_L
   1000015     2.72434371e+02   # ~stau_1
   1000016     5.20572650e+02   # ~nu_tau_L
   2000001     1.32749510e+03   # ~d_R
   2000002     1.33227901e+03   # ~u_R
   2000003     1.32741931e+03   # ~s_R
   2000004     1.33227419e+03   # ~c_R
   2000005     1.23512690e+03   # ~b_2
   2000006     1.23562977e+03   # ~t_2
   2000011     4.48949293e+02   # ~e_R
   2000013     4.48581737e+02   # ~mu_R
   2000015     5.45948306e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60139373e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98033869e-01   # N_{1,1}
  1  2    -6.88842866e-03   # N_{1,2}
  1  3     5.88892403e-02   # N_{1,3}
  1  4    -2.03224690e-02   # N_{1,4}
  2  1     1.69734364e-02   # N_{2,1}
  2  2     9.85822976e-01   # N_{2,2}
  2  3    -1.42139529e-01   # N_{2,3}
  2  4     8.75289454e-02   # N_{2,4}
  3  1    -2.69130751e-02   # N_{3,1}
  3  2     3.92685753e-02   # N_{3,2}
  3  3     7.04925197e-01   # N_{3,3}
  3  4     7.07682226e-01   # N_{3,4}
  4  1    -5.39998580e-02   # N_{4,1}
  4  2     1.62983398e-01   # N_{4,2}
  4  3     6.92393587e-01   # N_{4,3}
  4  4    -7.00793514e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.79736210e-01   # U_{1,1}
  1  2    -2.00292182e-01   # U_{1,2}
  2  1     2.00292182e-01   # U_{2,1}
  2  2     9.79736210e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.92108904e-01   # V_{1,1}
  1  2    -1.25379116e-01   # V_{1,2}
  2  1     1.25379116e-01   # V_{2,1}
  2  2     9.92108904e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.17857222e-01   # F_{11}
  1  2     9.08512709e-01   # F_{12}
  2  1     9.08512709e-01   # F_{21}
  2  2    -4.17857222e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.08078552e-01   # F_{11}
  1  2     5.89074744e-01   # F_{12}
  2  1    -5.89074744e-01   # F_{21}
  2  2     8.08078552e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.02791129e-01   # F_{11}
  1  2     9.53056941e-01   # F_{12}
  2  1     9.53056941e-01   # F_{21}
  2  2    -3.02791129e-01   # F_{22}
Block gauge Q= 1.08706316e+03  # SM gauge couplings
     1     3.62684488e-01   # g'(Q)MSSM DRbar
     2     6.41130789e-01   # g(Q)MSSM DRbar
     3     1.04857343e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.08706316e+03  
  3  3     8.48067926e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.08706316e+03  
  3  3     4.89823855e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.08706316e+03  
  3  3     4.27844129e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.08706316e+03 # Higgs mixing parameters
     1     8.57799151e+02    # mu(Q)MSSM DRbar
     2     3.91756203e+01    # tan beta(Q)MSSM DRbar
     3     2.43738321e+02    # higgs vev(Q)MSSM DRbar
     4     7.15582732e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.08706316e+03  # MSSM DRbar SUSY breaking parameters
     1     2.76580116e+02      # M_1(Q)
     2     5.10370920e+02      # M_2(Q)
     3     1.42572397e+03      # M_3(Q)
    21    -1.62971601e+05      # mH1^2(Q)
    22    -7.21510671e+05      # mH2^2(Q)
    31     5.68928093e+02      # meL(Q)
    32     5.68784862e+02      # mmuL(Q)
    33     5.22702115e+02      # mtauL(Q)
    34     4.43880295e+02      # meR(Q)
    35     4.43508501e+02      # mmuR(Q)
    36     3.07299472e+02      # mtauR(Q)
    41     1.34025434e+03      # mqL1(Q)
    42     1.34021551e+03      # mqL2(Q)
    43     1.16073090e+03      # mqL3(Q)
    44     1.29199873e+03      # muR(Q)
    45     1.29199383e+03      # mcR(Q)
    46     1.01384499e+03      # mtR(Q)
    47     1.28614013e+03      # mdR(Q)
    48     1.28606311e+03      # msR(Q)
    49     1.17583118e+03      # mbR(Q)
Block au Q= 1.08706316e+03  
  1  1    -1.78771297e+03      # Au(Q)MSSM DRbar
  2  2    -1.78767105e+03      # Ac(Q)MSSM DRbar
  3  3    -1.25735959e+03      # At(Q)MSSM DRbar
Block ad Q= 1.08706316e+03  
  1  1    -2.06514423e+03      # Ad(Q)MSSM DRbar
  2  2    -2.06503749e+03      # As(Q)MSSM DRbar
  3  3    -1.74614623e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.08706316e+03  
  1  1    -6.86384417e+02      # Ae(Q)MSSM DRbar
  2  2    -6.86051334e+02      # Amu(Q)MSSM DRbar
  3  3    -5.74254942e+02      # Atau(Q)MSSM DRbar
