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
     1    1.50000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.76362810e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03906185e+01   # MW
        25     1.16087123e+02   # h0
        35     8.48919129e+02   # H0
        36     8.48675401e+02   # A0
        37     8.52696122e+02   # H+
   1000021     1.35674048e+03   # ~g
   1000022     2.47628688e+02   # ~neutralino(1)
   1000023     4.68627482e+02   # ~neutralino(2)
   1000024     4.68804556e+02   # ~chargino(1)
   1000025    -7.45909744e+02   # ~neutralino(3)
   1000035     7.58309898e+02   # ~neutralino(4)
   1000037     7.57937574e+02   # ~chargino(2)
   1000001     1.24683269e+03   # ~d_L
   1000002     1.24446980e+03   # ~u_L
   1000003     1.24682967e+03   # ~s_L
   1000004     1.24446677e+03   # ~c_L
   1000005     1.14230062e+03   # ~b_1
   1000006     9.58317773e+02   # ~t_1
   1000011     4.31799675e+02   # ~e_L
   1000012     4.24349502e+02   # ~nue_L
   1000013     4.31872024e+02   # ~mu_L
   1000014     4.24345562e+02   # ~numu_L
   1000015     2.66980895e+02   # ~stau_1
   1000016     4.22968007e+02   # ~nu_tau_L
   2000001     1.19307409e+03   # ~d_R
   2000002     1.19750136e+03   # ~u_R
   2000003     1.19307093e+03   # ~s_R
   2000004     1.19749812e+03   # ~c_R
   2000005     1.18864330e+03   # ~b_2
   2000006     1.18208219e+03   # ~t_2
   2000011     2.74092918e+02   # ~e_R
   2000013     2.74080531e+02   # ~mu_R
   2000015     4.32304461e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05965482e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96968823e-01   # N_{1,1}
  1  2    -1.26642116e-02   # N_{1,2}
  1  3     7.06531798e-02   # N_{1,3}
  1  4    -3.00151872e-02   # N_{1,4}
  2  1     2.86388259e-02   # N_{2,1}
  2  2     9.76162556e-01   # N_{2,2}
  2  3    -1.77488156e-01   # N_{2,3}
  2  4     1.21591269e-01   # N_{2,4}
  3  1    -2.80934503e-02   # N_{3,1}
  3  2     4.07290254e-02   # N_{3,2}
  3  3     7.04490019e-01   # N_{3,3}
  3  4     7.07987088e-01   # N_{3,4}
  4  1    -6.66613924e-02   # N_{4,1}
  4  2     2.12808433e-01   # N_{4,2}
  4  3     6.83520223e-01   # N_{4,3}
  4  4    -6.95031607e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.68163765e-01   # U_{1,1}
  1  2    -2.50317648e-01   # U_{1,2}
  2  1     2.50317648e-01   # U_{2,1}
  2  2     9.68163765e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.84891640e-01   # V_{1,1}
  1  2    -1.73171756e-01   # V_{1,2}
  2  1     1.73171756e-01   # V_{2,1}
  2  2     9.84891640e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.84564581e-01   # F_{11}
  1  2     9.23098090e-01   # F_{12}
  2  1     9.23098090e-01   # F_{21}
  2  2    -3.84564581e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.81013815e-01   # F_{11}
  1  2     1.93937862e-01   # F_{12}
  2  1    -1.93937862e-01   # F_{21}
  2  2     9.81013815e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.18019599e-01   # F_{11}
  1  2     9.93011266e-01   # F_{12}
  2  1     9.93011266e-01   # F_{21}
  2  2    -1.18019599e-01   # F_{22}
Block gauge Q= 1.03290036e+03  # SM gauge couplings
     1     3.62766248e-01   # g'(Q)MSSM DRbar
     2     6.42078774e-01   # g(Q)MSSM DRbar
     3     1.05211768e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.03290036e+03  
  3  3     8.55466641e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.03290036e+03  
  3  3     1.34151110e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.03290036e+03  
  3  3     1.00403124e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.03290036e+03 # Higgs mixing parameters
     1     7.40492875e+02    # mu(Q)MSSM DRbar
     2     9.65376204e+00    # tan beta(Q)MSSM DRbar
     3     2.43906487e+02    # higgs vev(Q)MSSM DRbar
     4     7.46510798e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.03290036e+03  # MSSM DRbar SUSY breaking parameters
     1     2.53143954e+02      # M_1(Q)
     2     4.67914665e+02      # M_2(Q)
     3     1.31922198e+03      # M_3(Q)
    21     1.56967958e+05      # mH1^2(Q)
    22    -5.28529058e+05      # mH2^2(Q)
    31     4.23699386e+02      # meL(Q)
    32     4.23695442e+02      # mmuL(Q)
    33     4.22503833e+02      # mtauL(Q)
    34     2.66167383e+02      # meR(Q)
    35     2.66154613e+02      # mmuR(Q)
    36     2.62272713e+02      # mtauR(Q)
    41     1.20417094e+03      # mqL1(Q)
    42     1.20416787e+03      # mqL2(Q)
    43     1.11039933e+03      # mqL3(Q)
    44     1.15810279e+03      # muR(Q)
    45     1.15809950e+03      # mcR(Q)
    46     9.54169201e+02      # mtR(Q)
    47     1.15248064e+03      # mdR(Q)
    48     1.15247743e+03      # msR(Q)
    49     1.14663708e+03      # mbR(Q)
Block au Q= 1.03290036e+03  
  1  1    -1.34309855e+03      # Au(Q)MSSM DRbar
  2  2    -1.34309257e+03      # Ac(Q)MSSM DRbar
  3  3    -1.03911825e+03      # At(Q)MSSM DRbar
Block ad Q= 1.03290036e+03  
  1  1    -1.63986568e+03      # Ad(Q)MSSM DRbar
  2  2    -1.63986014e+03      # As(Q)MSSM DRbar
  3  3    -1.53316655e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.03290036e+03  
  1  1    -3.56324535e+02      # Ae(Q)MSSM DRbar
  2  2    -3.56318202e+02      # Amu(Q)MSSM DRbar
  3  3    -3.54404887e+02      # Atau(Q)MSSM DRbar
