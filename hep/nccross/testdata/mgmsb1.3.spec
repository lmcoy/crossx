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
     1    4.50000000e+04   # lambda
     2    9.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=9.00000000e+04 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04021948e+01   # MW
        25     1.12046127e+02   # h0
        35     4.31778408e+02   # H0
        36     4.31467772e+02   # A0
        37     4.39133888e+02   # H+
   1000021     1.05206372e+03   # ~g
   1000022     1.84858519e+02   # ~neutralino(1)
   1000023     3.04848220e+02   # ~neutralino(2)
   1000024     3.02280718e+02   # ~chargino(1)
   1000025    -3.48796368e+02   # ~neutralino(3)
   1000035     4.24311159e+02   # ~neutralino(4)
   1000037     4.22644058e+02   # ~chargino(2)
   1000039     9.59850000e-10   # ~gravitino
   1000001     1.00382517e+03   # ~d_L
   1000002     1.00081314e+03   # ~u_L
   1000003     1.00382391e+03   # ~s_L
   1000004     1.00081187e+03   # ~c_L
   1000005     9.55637889e+02   # ~b_1
   1000006     8.95299865e+02   # ~t_1
   1000011     2.94112020e+02   # ~e_L
   1000012     2.82909171e+02   # ~nue_L
   1000013     2.94141244e+02   # ~mu_L
   1000014     2.82907948e+02   # ~numu_L
   1000015     1.39384948e+02   # ~stau_1
   1000016     2.82348807e+02   # ~nu_tau_L
   2000001     9.64096668e+02   # ~d_R
   2000002     9.65952802e+02   # ~u_R
   2000003     9.64094905e+02   # ~s_R
   2000004     9.65951903e+02   # ~c_R
   2000005     9.71220956e+02   # ~b_2
   2000006     9.86096953e+02   # ~t_2
   2000011     1.45767936e+02   # ~e_R
   2000013     1.45763110e+02   # ~mu_R
   2000015     2.95685249e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.69049991e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.71224108e-01   # N_{1,1}
  1  2    -5.39633609e-02   # N_{1,2}
  1  3     2.00092674e-01   # N_{1,3}
  1  4    -1.17365279e-01   # N_{1,4}
  2  1    -2.12030703e-01   # N_{2,1}
  2  2    -6.13840435e-01   # N_{2,2}
  2  3     5.65292931e-01   # N_{2,3}
  2  4    -5.08612627e-01   # N_{2,4}
  3  1    -5.38967991e-02   # N_{3,1}
  3  2     7.26931031e-02   # N_{3,2}
  3  3     6.97921301e-01   # N_{3,3}
  3  4     7.10434167e-01   # N_{3,4}
  4  1    -9.41373863e-02   # N_{4,1}
  4  2     7.84221646e-01   # N_{4,2}
  4  3     3.91551634e-01   # N_{4,3}
  4  4    -4.72040127e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.52349645e-01   # U_{1,1}
  1  2     8.33612541e-01   # U_{1,2}
  2  1    -8.33612541e-01   # U_{2,1}
  2  2    -5.52349645e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.63155237e-01   # V_{1,1}
  1  2     7.48481884e-01   # V_{1,2}
  2  1    -7.48481884e-01   # V_{2,1}
  2  2    -6.63155237e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.33001084e-01   # F_{11}
  1  2     9.42926444e-01   # F_{12}
  2  1     9.42926444e-01   # F_{21}
  2  2    -3.33001084e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.35519358e-01   # F_{11}
  1  2     8.44522953e-01   # F_{12}
  2  1     8.44522953e-01   # F_{21}
  2  2    -5.35519358e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.35342712e-01   # F_{11}
  1  2     9.90798845e-01   # F_{12}
  2  1     9.90798845e-01   # F_{21}
  2  2    -1.35342712e-01   # F_{22}
Block gauge Q= 9.11118559e+02  # SM gauge couplings
     1     3.62884948e-01   # g'(Q)MSSM DRbar
     2     6.44410820e-01   # g(Q)MSSM DRbar
     3     1.06221077e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.11118559e+02  
  3  3     8.64758262e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.11118559e+02  
  3  3     2.05019606e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.11118559e+02  
  3  3     1.51967627e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.11118559e+02 # Higgs mixing parameters
     1     3.39955963e+02    # mu(Q)MSSM DRbar
     2     1.45173632e+01    # tan beta(Q)MSSM DRbar
     3     2.43803956e+02    # higgs vev(Q)MSSM DRbar
     4     2.12483517e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.11118559e+02  # MSSM DRbar SUSY breaking parameters
     1     1.94940038e+02      # M_1(Q)
     2     3.67492971e+02      # M_2(Q)
     3     1.00341294e+03      # M_3(Q)
    21     7.05614498e+04      # mH1^2(Q)
    22    -1.02350223e+05      # mH2^2(Q)
    31     2.85054036e+02      # meL(Q)
    32     2.85052824e+02      # mmuL(Q)
    33     2.84680432e+02      # mtauL(Q)
    34     1.33834901e+02      # meR(Q)
    35     1.33829657e+02      # mmuR(Q)
    36     1.32208818e+02      # mtauR(Q)
    41     9.65415590e+02      # mqL1(Q)
    42     9.65414290e+02      # mqL2(Q)
    43     9.34577415e+02      # mqL3(Q)
    44     9.30612558e+02      # muR(Q)
    45     9.30611638e+02      # mcR(Q)
    46     8.67984042e+02      # mtR(Q)
    47     9.27470558e+02      # mdR(Q)
    48     9.27468749e+02      # msR(Q)
    49     9.23947367e+02      # mbR(Q)
Block au Q= 9.11118559e+02  
  1  1    -3.03324206e+02      # Au(Q)MSSM DRbar
  2  2    -3.03323778e+02      # Ac(Q)MSSM DRbar
  3  3    -2.85892333e+02      # At(Q)MSSM DRbar
Block ad Q= 9.11118559e+02  
  1  1    -3.22735024e+02      # Ad(Q)MSSM DRbar
  2  2    -3.22734426e+02      # As(Q)MSSM DRbar
  3  3    -3.16164003e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.11118559e+02  
  1  1    -3.07527242e+01      # Ae(Q)MSSM DRbar
  2  2    -3.07524999e+01      # Amu(Q)MSSM DRbar
  3  3    -3.06835903e+01      # Atau(Q)MSSM DRbar
