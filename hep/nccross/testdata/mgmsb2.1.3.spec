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
     1    9.00000000e+04   # lambda
     2    1.00000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.00000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04035080e+01   # MW
        25     1.12333107e+02   # h0
        35     4.62210012e+02   # H0
        36     4.61876149e+02   # A0
        37     4.69136775e+02   # H+
   1000021     8.64442966e+02   # ~g
   1000022     1.45061046e+02   # ~neutralino(1)
   1000023     2.65578317e+02   # ~neutralino(2)
   1000024     2.65237474e+02   # ~chargino(1)
   1000025    -3.68263620e+02   # ~neutralino(3)
   1000035     4.01172789e+02   # ~neutralino(4)
   1000037     3.99786121e+02   # ~chargino(2)
   1000039     2.13300000e-09   # ~gravitino
   1000001     1.03055504e+03   # ~d_L
   1000002     1.02766897e+03   # ~u_L
   1000003     1.03055363e+03   # ~s_L
   1000004     1.02766756e+03   # ~c_L
   1000005     9.76737889e+02   # ~b_1
   1000006     9.13292062e+02   # ~t_1
   1000011     3.17776264e+02   # ~e_L
   1000012     3.07425053e+02   # ~nue_L
   1000013     3.17802115e+02   # ~mu_L
   1000014     3.07423651e+02   # ~numu_L
   1000015     1.52911445e+02   # ~stau_1
   1000016     3.06803567e+02   # ~nu_tau_L
   2000001     9.85001716e+02   # ~d_R
   2000002     9.87536543e+02   # ~u_R
   2000003     9.84999761e+02   # ~s_R
   2000004     9.87535543e+02   # ~c_R
   2000005     9.93583041e+02   # ~b_2
   2000006     1.00616396e+03   # ~t_2
   2000011     1.58936222e+02   # ~e_R
   2000013     1.58930733e+02   # ~mu_R
   2000015     3.19055502e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.59182115e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.83916947e-01   # N_{1,1}
  1  2    -4.32830141e-02   # N_{1,2}
  1  3     1.57616598e-01   # N_{1,3}
  1  4    -7.20488011e-02   # N_{1,4}
  2  1     1.21891492e-01   # N_{2,1}
  2  2     8.64328477e-01   # N_{2,2}
  2  3    -3.88772477e-01   # N_{2,3}
  2  4     2.94846925e-01   # N_{2,4}
  3  1    -5.62220184e-02   # N_{3,1}
  3  2     7.93619201e-02   # N_{3,2}
  3  3     6.97353622e-01   # N_{3,3}
  3  4     7.10097666e-01   # N_{3,4}
  4  1    -1.17851559e-01   # N_{4,1}
  4  2     4.94736850e-01   # N_{4,2}
  4  3     5.81128983e-01   # N_{4,3}
  4  4    -6.35323197e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.26584689e-01   # U_{1,1}
  1  2    -5.62812359e-01   # U_{1,2}
  2  1     5.62812359e-01   # U_{2,1}
  2  2     8.26584689e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.02523329e-01   # V_{1,1}
  1  2    -4.30640964e-01   # V_{1,2}
  2  1     4.30640964e-01   # V_{2,1}
  2  2     9.02523329e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.77264073e-01   # F_{11}
  1  2     9.60793752e-01   # F_{12}
  2  1     9.60793752e-01   # F_{21}
  2  2    -2.77264073e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.75747005e-01   # F_{11}
  1  2     8.79582166e-01   # F_{12}
  2  1     8.79582166e-01   # F_{21}
  2  2    -4.75747005e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.22936191e-01   # F_{11}
  1  2     9.92414577e-01   # F_{12}
  2  1     9.92414577e-01   # F_{21}
  2  2    -1.22936191e-01   # F_{22}
Block gauge Q= 9.37894019e+02  # SM gauge couplings
     1     3.62939846e-01   # g'(Q)MSSM DRbar
     2     6.44927187e-01   # g(Q)MSSM DRbar
     3     1.06542076e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.37894019e+02  
  3  3     8.66415442e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.37894019e+02  
  3  3     2.04689905e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.37894019e+02  
  3  3     1.51452433e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.37894019e+02 # Higgs mixing parameters
     1     3.59449888e+02    # mu(Q)MSSM DRbar
     2     1.45087713e+01    # tan beta(Q)MSSM DRbar
     3     2.43650293e+02    # higgs vev(Q)MSSM DRbar
     4     2.36636596e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.37894019e+02  # MSSM DRbar SUSY breaking parameters
     1     1.51688984e+02      # M_1(Q)
     2     2.86304757e+02      # M_2(Q)
     3     7.85300436e+02      # M_3(Q)
    21     8.47392236e+04      # mH1^2(Q)
    22    -1.13697584e+05      # mH2^2(Q)
    31     3.11334681e+02      # meL(Q)
    32     3.11333292e+02      # mmuL(Q)
    33     3.10909265e+02      # mtauL(Q)
    34     1.48353242e+02      # meR(Q)
    35     1.48347355e+02      # mmuR(Q)
    36     1.46539699e+02      # mtauR(Q)
    41     1.00167225e+03      # mqL1(Q)
    42     1.00167079e+03      # mqL2(Q)
    43     9.66802079e+02      # mqL3(Q)
    44     9.60964093e+02      # muR(Q)
    45     9.60963057e+02      # mcR(Q)
    46     8.89692443e+02      # mtR(Q)
    47     9.57082755e+02      # mdR(Q)
    48     9.57080725e+02      # msR(Q)
    49     9.53123849e+02      # mbR(Q)
Block au Q= 9.37894019e+02  
  1  1    -2.41593904e+02      # Au(Q)MSSM DRbar
  2  2    -2.41593559e+02      # Ac(Q)MSSM DRbar
  3  3    -2.27470076e+02      # At(Q)MSSM DRbar
Block ad Q= 9.37894019e+02  
  1  1    -2.57312375e+02      # Ad(Q)MSSM DRbar
  2  2    -2.57311894e+02      # As(Q)MSSM DRbar
  3  3    -2.51992309e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.37894019e+02  
  1  1    -2.43958408e+01      # Ae(Q)MSSM DRbar
  2  2    -2.43956603e+01      # Amu(Q)MSSM DRbar
  3  3    -2.43405649e+01      # Atau(Q)MSSM DRbar
