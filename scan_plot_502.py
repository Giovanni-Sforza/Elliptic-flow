from v2recinb import v2
import numpy as np




N = 50

"""tq0 =  0.35144489795918366
ts0 =  0.4226755102040817
tc0 =  0.7117061224489797
a2 =  0.04091224489795919"""
"""tq0 =  0.36001428571428573
ts0 =  0.433795918367347
tc0 =  0.7944510204081634
a2 =  0.6939081632653061"""

tq0 =  0.35144489795918366
ts0 =  0.4449163265306123
tc0 =  0.811
a2 =  1.0205061224489795

tq0 =  0.41143061224489796
ts0 =  0.4449163265306123
tc0 =  0.7613530612244899
a2 =  0.6123387755102041

v2pion502_05 = v2( IDpart   = 1, Task = 2,Isys = 2,c = 0.025,tq0 =  tq0, tc0 =  tc0,a2 =  a2, ts0 = ts0,
              plotname   =  "pion 5.02TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 05.dat"  ,  size_v2   = (9, 4),endrow_v2 =9,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c025 c.txt"  ,  size_spectrum   = (60,6),endrow_spectrum =60,
              scan_loop = N
              )
v2pion502_05.plot()

v2pion502_1020 = v2( IDpart   = 1, Task = 2,Isys = 2,c = 0.15,tq0 =  tq0, tc0 =  tc0,a2 =  a2, ts0 = ts0,
              plotname   =  "pion 5.02TeV 10-20% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 1020.dat"  ,  size_v2   = (9, 4),endrow_v2 =9,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c15  c.txt"  ,  size_spectrum   = (60,6),endrow_spectrum =60,
              scan_loop = N
              )
v2pion502_1020.plot()
v2pion502_2030 = v2( IDpart   = 1, Task = 2,Isys = 2,c = 0.25,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "pion 5.02TeV 20-30% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 2030.dat"  ,  size_v2   = (9, 4),endrow_v2 =9,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c25  c.txt"  ,   size_spectrum   = (60,6),endrow_spectrum =60,
              scan_loop = N
              )
v2pion502_2030.plot()

v2pion502_3040 = v2( IDpart   = 1, Task = 2,Isys = 2,c = 0.35,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "pion 5.02TeV 30-40% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 3040.dat"  ,  size_v2   = (9, 4),endrow_v2 =9,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c35  c.txt"  ,   size_spectrum   = (60,6),endrow_spectrum =60,
              scan_loop = N
              )
v2pion502_3040.plot()






v2D0502_3050 = v2( IDpart   = 9, Task = 2,Isys = 2,c = 0.40,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "D0 5.02TeV 30-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "D0/v2 D0 502 3050.dat"  ,  size_v2   = (6, 4),endrow_v2 =4,
              filename_spectrum   =  "D0/dNptdpt_PbPb502_D0_c40  c.txt" ,  size_spectrum   = (60,6),endrow_spectrum =60,
              scan_loop = N)
v2D0502_3050.plot()

v2Ds502_3050 = v2( IDpart   = 10, Task = 2,Isys = 2,c = 0.40,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "Ds 5.02TeV 30-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "Ds/v2 Ds 502 40.txt"  ,  size_v2   = (3, 4),endrow_v2 =3,
              filename_spectrum   =  "Ds/dNptdpt_PbPb502_Ds_c40  c.txt" , size_spectrum   = (60,6),endrow_spectrum =60,
              scan_loop = N)
v2Ds502_3050.plot()

v2Jpsi502_3050 = v2( IDpart   = 8, Task = 2,Isys = 2,c = 0.30,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "Jpsi 5.02TeV 20-40% y = -0.5 -- 0.5" ,
              filename_v2   =  "Jpsi/v2 Jpsi 502 30.txt"  ,  size_v2   = (3, 5),endrow_v2 =3,
              filename_spectrum   =  "Jpsi/dNptdpt_PbPb502_Jpsi_c30  c.txt" ,  size_spectrum   = (59,6),endrow_spectrum =59,
              scan_loop = N)
v2Jpsi502_3050.plot()

v2proton502_05 = v2( IDpart   = 3, Task = 2,Isys = 2,c = 0.025,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "proton 5.02TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 502 05.dat"  ,  size_v2   = (7, 4),endrow_v2 = 7,
              filename_spectrum   =  "proton/dNptdpt_PbPb502_proton_c025 c.txt"  , size_spectrum   = (40,8),endrow_spectrum =60,
              scan_loop = N
              )
v2proton502_05.plot()

v2proton502_1020 = v2( IDpart   = 3, Task = 2,Isys = 2,c = 0.15,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "proton 5.02TeV 10-20% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 502 1020.dat"  ,  size_v2   = (7, 4),endrow_v2 = 7,
              filename_spectrum   =  "proton/dNptdpt_PbPb502_proton_c15  c.txt"  ,size_spectrum   = (40,8),endrow_spectrum =60,
              scan_loop = N
              )
v2proton502_1020.plot()

v2proton502_2030 = v2( IDpart   = 3, Task = 2,Isys = 2,c = 0.25,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "proton 5.02TeV 20-30% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 502 2030.dat"  ,  size_v2   = (7, 4),endrow_v2 = 7,
              filename_spectrum   =  "proton/dNptdpt_PbPb502_proton_c25  c.txt"  , size_spectrum   = (40,8),endrow_spectrum =60,
              scan_loop = N
              )
v2proton502_2030.plot()


v2proton502_3040 = v2( IDpart   = 3, Task = 2,Isys = 2,c = 0.35,tq0 =  tq0, tc0 =  tc0,a2 =  a2,ts0 = ts0,
              plotname   =  "proton 5.02TeV 30-40% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 502 3040.dat"  ,   size_v2   = (7, 4),endrow_v2 = 7,
              filename_spectrum   =  "proton/dNptdpt_PbPb502_proton_c35  c.txt"  ,  size_spectrum   = (40,8),endrow_spectrum =60,
              scan_loop = N
              )
v2proton502_3040.plot()