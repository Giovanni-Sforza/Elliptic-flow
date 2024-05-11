from v2recinb import v2
import numpy as np

"""tq0 =  0.3343
tc0 =  0.646
a2 =  1.224565306122449"""

tq0 =  0.39
tc0 =  0.5141836734693878
a2 =  0.6123387755102041


#errpion = 0.012 , errD0 = 0.133

N = 100
v2pion276_05 = v2( IDpart   = 1, Task = 2,Isys = 1,c = 0.025,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "pion 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 05.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c025 c.txt"  ,  size_spectrum   = (60,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_05.plot()

v2pion276_1020 = v2( IDpart   = 1, Task = 2,Isys = 1,c = 0.15,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "pion 2.76TeV 10-20% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 1020.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c15  c.txt"  ,  size_spectrum   = (60,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_1020.plot()


v2pion276_2030 = v2( IDpart   = 1, Task = 2,Isys = 1,c = 0.25,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "pion 2.76TeV 20-30% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 2030.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c25  c.txt"  ,  size_spectrum   = (60,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_2030.plot()

v2pion276_3040 = v2( IDpart   = 1, Task = 2,Isys = 1,c = 0.35,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "pion 2.76TeV 30-40% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 3040.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c35  c.txt"  ,  size_spectrum   = (60,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_3040.plot()

#================================================     charm     =======================================================

v2D0276_010 = v2( IDpart   = 9, Task = 2,Isys = 1,c = 0.05,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "D0 2.76TeV 0-10% y = -0.5 -- 0.5" ,
              filename_v2   =  "D0/v2 D0 276 010.dat"  ,  size_v2   = (4, 4),endrow_v2 = 4,
              filename_spectrum   =  "D0/dNptdpt_PbPb276_D0_c05  c.txt"  ,  size_spectrum = (60,6),endrow_spectrum = 60,
              scan_loop = N)
v2D0276_010.plot()


v2D0276_1020 = v2( IDpart   = 9, Task = 2,Isys = 1,c = 0.40,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "D0 2.76TeV 30-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "D0/v2 D0 276 3050.dat"  ,  size_v2   = (4, 4),endrow_v2 = 3,
              filename_spectrum   =  "D0/dNptdpt_PbPb276_D0_c40  c.txt" , size_spectrum = (60,6),endrow_spectrum = 60,
              scan_loop = N)
v2D0276_1020.plot()



#==================================  proton  ========================================================

v2proton276_05 = v2( IDpart   = 3, Task = 2,Isys = 1,c = 0.025,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 276 05.dat"  ,  size_v2   = (17, 3),endrow_v2 = 17,
              filename_spectrum   =  "proton/dNptdpt_PbPb276_proton_c025 c.txt"  ,  size_spectrum   = (40,8),endrow_spectrum = 40,
              scan_loop = N
              )
v2proton276_05.plot()

v2proton276_1020 = v2( IDpart   = 3, Task = 2,Isys = 1,c = 0.15,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "proton 2.76TeV 10-20% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 276 1020.dat"  ,  size_v2   = (17, 3),endrow_v2 = 17,
              filename_spectrum   =  "proton/dNptdpt_PbPb276_proton_c15  c.txt"  ,  size_spectrum   = (40,8),endrow_spectrum = 40,
              scan_loop = N
              )
v2proton276_1020.plot()

v2proton276_2030 = v2( IDpart   = 3, Task = 2,Isys = 1,c = 0.25,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "proton 2.76TeV 20-30% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 276 2030.dat"  ,   size_v2   = (17, 3),endrow_v2 = 17,
              filename_spectrum   =  "proton/dNptdpt_PbPb276_proton_c25  c.txt"  ,   size_spectrum   = (40,8),endrow_spectrum = 40,
              scan_loop = N
              )
v2proton276_2030.plot()


v2proton276_3040 = v2( IDpart   = 3, Task = 2,Isys = 1,c = 0.35,tq0 =  tq0, tc0 =  tc0,a2 =  a2,
              plotname   =  "proton 2.76TeV 30-40% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 276 3040.dat"  ,   size_v2   = (17, 3),endrow_v2 = 17,
              filename_spectrum   =  "proton/dNptdpt_PbPb276_proton_c35  c.txt"  ,   size_spectrum   = (40,8),endrow_spectrum = 40,
              scan_loop = N
              )
v2proton276_3040.plot()


