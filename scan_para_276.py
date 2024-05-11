from v2recinb import v2
import numpy as np
import time


time_start = time.time()  # 记录开始时间
# function()   执行的程序




N = 50
v2pion276_05 = v2( IDpart   = 1, Task = 1,Isys = 1,c = 0.025,
              plotname   =  "pion 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 05.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c025 .txt"  ,  size_spectrum   = (39,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_05.scan()

v2pion276_510 = v2( IDpart   = 1, Task = 1,Isys = 1,c = 0.075,
              plotname   =  "pion 2.76TeV 5-10% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 510.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c075 .txt"  ,  size_spectrum   = (39,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_510.scan()

v2pion276_1020 = v2( IDpart   = 1, Task = 1,Isys = 1,c = 0.15,
              plotname   =  "pion 2.76TeV 10-20% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 1020.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c15  .txt"  ,  size_spectrum   = (39,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_1020.scan()

v2pion276_2030 = v2( IDpart   = 1, Task = 1,Isys = 1,c = 0.25,
              plotname   =  "pion 2.76TeV 20-30% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 2030.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c25  .txt"  ,  size_spectrum   = (39,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_2030.scan()

v2pion276_3040 = v2( IDpart   = 1, Task = 1,Isys = 1,c = 0.35,
              plotname   =  "pion 2.76TeV 30-40% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 3040.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c35  .txt"  ,  size_spectrum   = (39,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_3040.scan()


v2pion276_4050 = v2( IDpart   = 1, Task = 1,Isys = 1,c = 0.45,
              plotname   =  "pion 2.76TeV 40-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 4050.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c45  .txt"  ,  size_spectrum   = (39,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_4050.scan()

v2pion276_5060 = v2( IDpart   = 1, Task = 1,Isys = 1,c = 0.55,
              plotname   =  "pion 2.76TeV 50-60% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 276 5060.dat"  ,  size_v2   = (39, 3),endrow_v2 = 20,
              filename_spectrum   =  "pion/dNptdpt_PbPb276_pion_c55  .txt"  ,  size_spectrum   = (39,6),endrow_spectrum = 20,
              scan_loop = N
              )
v2pion276_5060.scan()





data_pion = v2pion276_1020.errj + v2pion276_2030.errj  + v2pion276_510.errj  + v2pion276_3040.errj + v2pion276_05.errj # + v2pion276_4050.errj + v2pion276_5060.errj
data_pion = data_pion
#data_pion = np.transpose(data_pion)

#np.savetxt('pion 276 para .csv',data_pion,delimiter =" ",header = "tq a2 np.reshape(N,N)" )


del v2pion276_3040, v2pion276_2030, v2pion276_1020, v2pion276_510, v2pion276_05#,v2pion276_5060, v2pion276_4050,
#================================================================================================================



v2D0276_010 = v2( IDpart   = 9, Task = 1,Isys = 1,c = 0.05,
              plotname   =  "D0 2.76TeV 0-10% y = -0.5 -- 0.5" ,
              filename_v2   =  "D0/v2 D0 276 010.dat"  ,  size_v2   = (4, 4),endrow_v2 = 3,
              filename_spectrum   =  "D0/dNptdpt_PbPb276_D0_c05  .txt"  ,  size_spectrum = (4,6),endrow_spectrum = 3,
              scan_loop = N)
v2D0276_010.scan()


v2D0276_1020 = v2( IDpart   = 9, Task = 1,Isys = 1,c = 0.40,
              plotname   =  "D0 2.76TeV 30-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "D0/v2 D0 276 3050.dat"  ,  size_v2   = (4, 4),endrow_v2 = 3,
              filename_spectrum   =  "D0/dNptdpt_PbPb276_D0_c40  .txt" , size_spectrum = (4,6),endrow_spectrum = 3,
              scan_loop = N)
v2D0276_1020.scan()

data_D0 = v2D0276_010.errj + v2D0276_1020.errj
#data_D0 = np.transpose(data_D0)
del v2D0276_1020,v2D0276_010

v2proton276_05 = v2( IDpart   = 3, Task = 1,Isys = 1,c = 0.025,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 276 05.dat"  ,  size_v2   = (17, 3),endrow_v2 = 17,
              filename_spectrum   =  "proton/dNptdpt_PbPb276_proton_c025 .txt"  ,  size_spectrum   = (17,8),endrow_spectrum = 17,
              scan_loop = N
              )
v2proton276_05.scan()

v2proton276_1020 = v2( IDpart   = 3, Task = 1,Isys = 1,c = 0.15,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 276 1020.dat"  ,  size_v2   = (17, 3),endrow_v2 = 17,
              filename_spectrum   =  "proton/dNptdpt_PbPb276_proton_c15  .txt"  ,  size_spectrum   = (17,8),endrow_spectrum = 17,
              scan_loop = N
              )
v2proton276_1020.scan()

v2proton276_2030 = v2( IDpart   = 3, Task = 1,Isys = 1,c = 0.25,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 276 2030.dat"  ,   size_v2   = (17, 3),endrow_v2 = 17,
              filename_spectrum   =  "proton/dNptdpt_PbPb276_proton_c25  .txt"  ,   size_spectrum   = (17,8),endrow_spectrum = 17,
              scan_loop = N
              )
v2proton276_2030.scan()


v2proton276_3040 = v2( IDpart   = 3, Task = 1,Isys = 1,c = 0.35,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 276 3040.dat"  ,   size_v2   = (17, 3),endrow_v2 = 17,
              filename_spectrum   =  "proton/dNptdpt_PbPb276_proton_c35  .txt"  ,   size_spectrum   = (17,8),endrow_spectrum = 17,
              scan_loop = N
              )
v2proton276_3040.scan()

data_proton = v2proton276_05.errj + v2proton276_1020.errj + v2proton276_2030.errj + v2proton276_3040.errj
del v2proton276_05 , v2proton276_1020 , v2proton276_2030 , v2proton276_3040
#np.savetxt('D0 276 para .csv',data_D0,delimiter =" ",header = "tc tq a2 np.reshape(N,N)" )

minerr = 1000000
times = 0

"""for j in range(N):
    dataerr = np.reshape(data_D0,(N,N*N))[j,:] + data_pion + data_proton

    indexi = np.argmin(dataerr)

    if dataerr[indexi]<minerr:
        times +=1
        print(indexi,times)
        minerr = dataerr[indexi]

        ani = int(indexi%N)
        tqi = int((indexi-ani)/N)

        tci = j"""

indexi = np.argmin( data_proton)
#indexi = np.argmin(data_proton)
ani = int(indexi%N)
tqi = int((indexi - ani)/N)
data_D0i = np.reshape(data_D0, (N, N, N))[:,tqi, ani]
tci = np.argmin(data_D0i)

Ts = 0.51
Tc = 0.646
Tq = 0.39


tq0 = np.linspace(0.0001,Tq,int(N)) #0.32     ##0.34#up
aaray = np.linspace(0.0001,10,N)
tc0 = np.linspace(0.0001,Tc,N) #0.48     ##0.56#down
#ts0 = np.linspace(0.0001,Ts,int(N)) #0.32     ##0.34#up

time_end = time.time()  # 记录结束时间
time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
print(time_sum)






print("==========================2.76==================================")
print("errtotal = ",minerr)
print("tq0 = " , tq0[tqi])
#print("ts0 = " , ts0[ts0i])
print("tc0 = " , tc0[tci])
print("a2 = " , aaray[ani])
print("errpion = ", data_pion[indexi])
print("errD0 = ", data_D0[int(tci*N**2+indexi)])
#print("errDs = ", dataDS[ts0i,tc0i*N+ai])



