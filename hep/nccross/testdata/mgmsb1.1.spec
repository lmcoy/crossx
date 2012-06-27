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
     1    3.50000000e+04   # lambda
     2    7.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# Low energy data in SOFTSUSY: MIXING=0 TOLERANCE=1.00000000e-03
# mgut=7.00000000e+04 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04108250e+01   # MW
        25     1.10110173e+02   # h0
        35     3.39330997e+02   # H0
        36     3.38928313e+02   # A0
        37     3.48629298e+02   # H+
   1000021     8.38683484e+02   # ~g
   1000022     1.40797306e+02   # ~neutralino(1)
   1000023     2.32119168e+02   # ~neutralino(2)
   1000024     2.28817276e+02   # ~chargino(1)
   1000025    -2.81440270e+02   # ~neutralino(3)
   1000035     3.48500566e+02   # ~neutralino(4)
   1000037     3.46709516e+02   # ~chargino(2)
   1000039     5.80650000e-10   # ~gravitino
   1000001     7.99285229e+02   # ~d_L
   1000002     7.95445134e+02   # ~u_L
   1000003     7.99284221e+02   # ~s_L
   1000004     7.95444120e+02   # ~c_L
   1000005     7.59917053e+02   # ~b_1
   1000006     7.14433409e+02   # ~t_1
   1000011     2.31259111e+02   # ~e_L
   1000012     2.16881079e+02   # ~nue_L
   1000013     2.31308333e+02   # ~mu_L
   1000014     2.16880111e+02   # ~numu_L
   1000015     1.09010848e+02   # ~stau_1
   1000016     2.16442566e+02   # ~nu_tau_L
   2000001     7.68369269e+02   # ~d_R
   2000002     7.69254369e+02   # ~u_R
   2000003     7.68367859e+02   # ~s_R
   2000004     7.69253654e+02   # ~c_R
   2000005     7.74764112e+02   # ~b_2
   2000006     7.93599053e+02   # ~t_2
   2000011     1.16276691e+02   # ~e_R
   2000013     1.16273020e+02   # ~mu_R
   2000015     2.33618849e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -8.19993277e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.55291628e-01   # N_{1,1}
  1  2    -8.09368517e-02   # N_{1,2}
  1  3     2.47861731e-01   # N_{1,3}
  1  4    -1.39397613e-01   # N_{1,4}
  2  1    -2.62565760e-01   # N_{2,1}
  2  2    -6.53326794e-01   # N_{2,2}
  2  3     5.37955992e-01   # N_{2,3}
  2  4    -4.63493984e-01   # N_{2,4}
  3  1    -6.79289881e-02   # N_{3,1}
  3  2     9.21949443e-02   # N_{3,2}
  3  3     6.92496200e-01   # N_{3,3}
  3  4     7.12274356e-01   # N_{3,4}
  4  1    -1.17740310e-01   # N_{4,1}
  4  2     7.47069889e-01   # N_{4,2}
  4  3     4.11845756e-01   # N_{4,3}
  4  4    -5.08337363e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.83088593e-01   # U_{1,1}
  1  2     8.12408575e-01   # U_{1,2}
  2  1    -8.12408575e-01   # U_{2,1}
  2  2    -5.83088593e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -7.17099254e-01   # V_{1,1}
  1  2     6.96971061e-01   # V_{1,2}
  2  1    -6.96971061e-01   # V_{2,1}
  2  2    -7.17099254e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.95230470e-01   # F_{11}
  1  2     9.18581992e-01   # F_{12}
  2  1     9.18581992e-01   # F_{21}
  2  2    -3.95230470e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.95744401e-01   # F_{11}
  1  2     8.03174084e-01   # F_{12}
  2  1     8.03174084e-01   # F_{21}
  2  2    -5.95744401e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.73835388e-01   # F_{11}
  1  2     9.84774724e-01   # F_{12}
  2  1     9.84774724e-01   # F_{21}
  2  2    -1.73835388e-01   # F_{22}
Block gauge Q= 7.29474222e+02  # SM gauge couplings
     1     3.62409029e-01   # g'(Q)MSSM DRbar
     2     6.45740513e-01   # g(Q)MSSM DRbar
     3     1.07446075e+00   # g3(Q)MSSM DRbar
Block yu Q= 7.29474222e+02  
  3  3     8.72934219e-01   # Yt(Q)MSSM DRbar
Block yd Q= 7.29474222e+02  
  3  3     2.07477342e-01   # Yb(Q)MSSM DRbar
Block ye Q= 7.29474222e+02  
  3  3     1.52180847e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 7.29474222e+02 # Higgs mixing parameters
     1     2.71989893e+02    # mu(Q)MSSM DRbar
     2     1.45563639e+01    # tan beta(Q)MSSM DRbar
     3     2.44078953e+02    # higgs vev(Q)MSSM DRbar
     4     1.31655452e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 7.29474222e+02  # MSSM DRbar SUSY breaking parameters
     1     1.51184739e+02      # M_1(Q)
     2     2.86908592e+02      # M_2(Q)
     3     7.98376720e+02      # M_3(Q)
    21     4.26439314e+04      # mH1^2(Q)
    22    -6.75547566e+04      # mH2^2(Q)
    31     2.22466717e+02      # meL(Q)
    32     2.22465775e+02      # mmuL(Q)
    33     2.22177001e+02      # mtauL(Q)
    34     1.03662836e+02      # meR(Q)
    35     1.03658727e+02      # mmuR(Q)
    36     1.02392023e+02      # mtauR(Q)
    41     7.67259205e+02      # mqL1(Q)
    42     7.67258165e+02      # mqL2(Q)
    43     7.42570595e+02      # mqL3(Q)
    44     7.40596878e+02      # muR(Q)
    45     7.40596146e+02      # mcR(Q)
    46     6.90531337e+02      # mtR(Q)
    47     7.38232340e+02      # mdR(Q)
    48     7.38230892e+02      # msR(Q)
    49     7.35400339e+02      # mbR(Q)
Block au Q= 7.29474222e+02  
  1  1    -2.43801563e+02      # Au(Q)MSSM DRbar
  2  2    -2.43801216e+02      # Ac(Q)MSSM DRbar
  3  3    -2.29653669e+02      # At(Q)MSSM DRbar
Block ad Q= 7.29474222e+02  
  1  1    -2.59648692e+02      # Ad(Q)MSSM DRbar
  2  2    -2.59648206e+02      # As(Q)MSSM DRbar
  3  3    -2.54310784e+02      # Ab(Q)MSSM DRbar
Block ae Q= 7.29474222e+02  
  1  1    -2.38596094e+01      # Ae(Q)MSSM DRbar
  2  2    -2.38594352e+01      # Amu(Q)MSSM DRbar
  3  3    -2.38060723e+01      # Atau(Q)MSSM DRbar
