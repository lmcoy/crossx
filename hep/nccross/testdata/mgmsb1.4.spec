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
     1    6.00000000e+04   # lambda
     2    1.00000000e+05   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=1.00000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03961200e+01   # MW
        25     1.14112262e+02   # h0
        35     5.59353846e+02   # H0
        36     5.59114198e+02   # A0
        37     5.65058320e+02   # H+
   1000021     1.39043432e+03   # ~g
   1000022     2.55825029e+02   # ~neutralino(1)
   1000023     4.07227022e+02   # ~neutralino(2)
   1000024     4.04489360e+02   # ~chargino(1)
   1000025    -4.37240183e+02   # ~neutralino(3)
   1000035     5.44211157e+02   # ~neutralino(4)
   1000037     5.42922821e+02   # ~chargino(2)
   1000039     1.42200000e-09   # ~gravitino
   1000001     1.31154954e+03   # ~d_L
   1000002     1.30928582e+03   # ~u_L
   1000003     1.31154795e+03   # ~s_L
   1000004     1.30928423e+03   # ~c_L
   1000005     1.25016748e+03   # ~b_1
   1000006     1.17118120e+03   # ~t_1
   1000011     3.88633031e+02   # ~e_L
   1000012     3.80173689e+02   # ~nue_L
   1000013     3.88630887e+02   # ~mu_L
   1000014     3.80172143e+02   # ~numu_L
   1000015     1.85139955e+02   # ~stau_1
   1000016     3.79459499e+02   # ~nu_tau_L
   2000001     1.25840151e+03   # ~d_R
   2000002     1.26155679e+03   # ~u_R
   2000003     1.25839930e+03   # ~s_R
   2000004     1.26155565e+03   # ~c_R
   2000005     1.26813883e+03   # ~b_2
   2000006     1.27953335e+03   # ~t_2
   2000011     1.90781077e+02   # ~e_R
   2000013     1.90774820e+02   # ~mu_R
   2000015     3.89391599e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.38340922e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.78807313e-01   # N_{1,1}
  1  2    -3.67977216e-02   # N_{1,2}
  1  3     1.70043030e-01   # N_{1,3}
  1  4    -1.08016388e-01   # N_{1,4}
  2  1    -1.90817283e-01   # N_{2,1}
  2  2    -4.82833571e-01   # N_{2,2}
  2  3     6.20656235e-01   # N_{2,3}
  2  4    -5.87576671e-01   # N_{2,4}
  3  1    -4.15483319e-02   # N_{3,1}
  3  2     5.52833246e-02   # N_{3,2}
  3  3     7.01621406e-01   # N_{3,3}
  3  4     7.09186078e-01   # N_{3,4}
  4  1    -6.16339610e-02   # N_{4,1}
  4  2     8.73190371e-01   # N_{4,2}
  4  3     3.05938897e-01   # N_{4,3}
  4  4    -3.74354407e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -4.29070567e-01   # U_{1,1}
  1  2     9.03270972e-01   # U_{1,2}
  2  1    -9.03270972e-01   # U_{2,1}
  2  2    -4.29070567e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -5.22630254e-01   # V_{1,1}
  1  2     8.52559451e-01   # V_{1,2}
  2  1    -8.52559451e-01   # V_{2,1}
  2  2    -5.22630254e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.64093816e-01   # F_{11}
  1  2     9.64496997e-01   # F_{12}
  2  1     9.64496997e-01   # F_{21}
  2  2    -2.64093816e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.16564627e-01   # F_{11}
  1  2     9.09106106e-01   # F_{12}
  2  1     9.09106106e-01   # F_{21}
  2  2    -4.16564627e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.82039833e-02   # F_{11}
  1  2     9.95166307e-01   # F_{12}
  2  1     9.95166307e-01   # F_{21}
  2  2    -9.82039833e-02   # F_{22}
Block gauge Q= 1.18796807e+03  # SM gauge couplings
     1     3.63456274e-01   # g'(Q)MSSM DRbar
     2     6.42915627e-01   # g(Q)MSSM DRbar
     3     1.04797862e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18796807e+03  
  3  3     8.55389197e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18796807e+03  
  3  3     2.02410022e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18796807e+03  
  3  3     1.51700960e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18796807e+03 # Higgs mixing parameters
     1     4.28337148e+02    # mu(Q)MSSM DRbar
     2     1.44725173e+01    # tan beta(Q)MSSM DRbar
     3     2.43489389e+02    # higgs vev(Q)MSSM DRbar
     4     3.57074707e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18796807e+03  # MSSM DRbar SUSY breaking parameters
     1     2.66936268e+02      # M_1(Q)
     2     4.99433815e+02      # M_2(Q)
     3     1.33309514e+03      # M_3(Q)
    21     1.25656323e+05      # mH1^2(Q)
    22    -1.57214429e+05      # mH2^2(Q)
    31     3.78262512e+02      # meL(Q)
    32     3.78260964e+02      # mmuL(Q)
    33     3.77783589e+02      # mtauL(Q)
    34     1.78695742e+02      # meR(Q)
    35     1.78689079e+02      # mmuR(Q)
    36     1.76623839e+02      # mtauR(Q)
    41     1.26284331e+03      # mqL1(Q)
    42     1.26284168e+03      # mqL2(Q)
    43     1.22428367e+03      # mqL3(Q)
    44     1.21596261e+03      # muR(Q)
    45     1.21596145e+03      # mcR(Q)
    46     1.13761316e+03      # mtR(Q)
    47     1.21167649e+03      # mdR(Q)
    48     1.21167423e+03      # msR(Q)
    49     1.20728375e+03      # mbR(Q)
Block au Q= 1.18796807e+03  
  1  1    -3.84512080e+02      # Au(Q)MSSM DRbar
  2  2    -3.84511561e+02      # Ac(Q)MSSM DRbar
  3  3    -3.63464048e+02      # At(Q)MSSM DRbar
Block ad Q= 1.18796807e+03  
  1  1    -4.07919859e+02      # Ad(Q)MSSM DRbar
  2  2    -4.07919137e+02      # As(Q)MSSM DRbar
  3  3    -3.99994783e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.18796807e+03  
  1  1    -4.02919615e+01      # Ae(Q)MSSM DRbar
  2  2    -4.02916787e+01      # Amu(Q)MSSM DRbar
  3  3    -4.02045607e+01      # Atau(Q)MSSM DRbar
