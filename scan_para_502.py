from v2recinb import v2
import numpy as np




N = 50


v2pion502_05 = v2( IDpart   = 1, Task = 1,Isys = 2,c = 0.025,
              plotname   =  "pion 2.76TeV 10-20% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 05.dat"  ,  size_v2   = (9, 4),endrow_v2 =9,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c025 .txt"  ,  size_spectrum   = (9,6),endrow_spectrum =12,
              scan_loop = N
              )
v2pion502_05.scan()

v2pion502_1020 = v2( IDpart   = 1, Task = 1,Isys = 2,c = 0.15,
              plotname   =  "pion 2.76TeV 10-20% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 1020.dat"  ,  size_v2   = (9, 4),endrow_v2 =9,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c15  .txt"  ,  size_spectrum   = (9,6),endrow_spectrum =12,
              scan_loop = N
              )
v2pion502_1020.scan()
v2pion502_2030 = v2( IDpart   = 1, Task = 1,Isys = 2,c = 0.25,
              plotname   =  "pion 2.76TeV 20-30% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 2030.dat"  ,  size_v2   = (9, 4),endrow_v2 =9,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c25  .txt"  ,  size_spectrum   = (9,6),endrow_spectrum =12,
              scan_loop = N
              )
v2pion502_2030.scan()

v2pion502_3040 = v2( IDpart   = 1, Task = 1,Isys = 2,c = 0.35,
              plotname   =  "pion 2.76TeV 30-40% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 3040.dat"  ,  size_v2   = (9, 4),endrow_v2 =9,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c35  .txt"  ,  size_spectrum   = (9,6),endrow_spectrum =12,
              scan_loop = N
              )
v2pion502_3040.scan()

"""v2pion502_4050 = v2( IDpart   = 1, Task = 1,Isys = 2,c = 0.45,
              plotname   =  "pion 2.76TeV 40-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "pion/v2 pion 502 4050.dat"  ,  size_v2   = (21, 3),endrow_v2 =12,
              filename_spectrum   =  "pion/dNptdpt_PbPb502_pion_c45  .txt"  ,  size_spectrum   = (21,6),endrow_spectrum =12,
              scan_loop = N
              )
v2pion502_4050.scan()
"""






data_pion = v2pion502_05.errj + v2pion502_1020.errj + v2pion502_2030.errj + v2pion502_3040.errj #+ v2pion502_4050.errj

#data_pion = np.reshape(data_pion,(N*N))
"""index = np.argmin(data_pion)
ani = int(index%N)
tqi = int((index - ani)/N)
"""
del  v2pion502_3040, v2pion502_2030, v2pion502_1020, v2pion502_05 #, v2pion502_4050
#np.savetxt('pion 502 para .csv',data_pion,delimiter =" ",header = "tq a2 np.reshape(N,N)" )

#================================================================================================================



v2D0502_3050 = v2( IDpart   = 9, Task = 1,Isys = 2,c = 0.40,
              plotname   =  "D0 2.76TeV 30-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "D0/v2 D0 502 3050.dat"  ,  size_v2   = (6, 4),endrow_v2 =6,
              filename_spectrum   =  "D0/dNptdpt_PbPb502_D0_c40  .txt" , size_spectrum = (11,6),endrow_spectrum =6,
              scan_loop = N)
v2D0502_3050.scan()

v2Ds502_3050 = v2( IDpart   = 10, Task = 1,Isys = 2,c = 0.40,
              plotname   =  "Ds 2.76TeV 30-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "Ds/v2 Ds 502 40.txt"  ,  size_v2   = (3, 4),endrow_v2 =3,
              filename_spectrum   =  "Ds/dNptdpt_PbPb502_Ds_c40  .txt" , size_spectrum = (5,6),endrow_spectrum =3,
              scan_loop = N)
v2Ds502_3050.scan()

v2Jpsi502_3050 = v2( IDpart   = 8, Task = 1,Isys = 2,c = 0.30,
              plotname   =  "Jpsi 2.76TeV 30-50% y = -0.5 -- 0.5" ,
              filename_v2   =  "Jpsi/v2 Jpsi 502 30.txt"  ,  size_v2   = (3, 5),endrow_v2 =3,
              filename_spectrum   =  "Jpsi/dNptdpt_PbPb502_Jpsi_c30  .txt" , size_spectrum = (3,6),endrow_spectrum =3,
              scan_loop = N)
v2Jpsi502_3050.scan()

#np.savetxt('D0 502 para .csv',v2D0502_3050.errj,delimiter =" ",header = "tc tq a2 np.reshape(N,N)" )
#np.savetxt('Ds 502 para .csv',v2Ds502_3050.errj,delimiter =" ",header = "ts tc a2 np.reshape(N,N)" )
#np.savetxt('Jpsi 502 para .csv',v2Jpsi502_3050.errj,delimiter =" ",header = "tc a2 np.reshape(N,N)" )

v2proton502_05 = v2( IDpart   = 3, Task = 1,Isys = 2,c = 0.025,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 502 05.dat"  ,   size_v2   = (7, 4),endrow_v2 = 7,
              filename_spectrum   =  "proton/dNptdpt_PbPb502_proton_c025 .txt"  ,  size_spectrum   = (7,8),endrow_spectrum = 7,
              scan_loop = N
              )
v2proton502_05.scan()

v2proton502_1020 = v2( IDpart   = 3, Task = 1,Isys = 2,c = 0.15,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 502 1020.dat"  ,   size_v2   = (7, 4),endrow_v2 = 7,
              filename_spectrum   =  "proton/dNptdpt_PbPb502_proton_c15  .txt"  ,  size_spectrum   = (7,8),endrow_spectrum = 7,
              scan_loop = N
              )
v2proton502_1020.scan()

v2proton502_2030 = v2( IDpart   = 3, Task = 1,Isys = 2,c = 0.25,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 502 2030.dat"  ,   size_v2   = (7, 4),endrow_v2 = 7,
              filename_spectrum   =  "proton/dNptdpt_PbPb502_proton_c25  .txt"  , size_spectrum   = (7,8),endrow_spectrum = 7,
              scan_loop = N
              )
v2proton502_2030.scan()


v2proton502_3040 = v2( IDpart   = 3, Task = 1,Isys = 2,c = 0.35,
              plotname   =  "proton 2.76TeV 0-5% y = -0.5 -- 0.5" ,
              filename_v2   =  "proton/v2 proton 502 3040.dat"  ,   size_v2   = (7, 4),endrow_v2 = 7,
              filename_spectrum   =  "proton/dNptdpt_PbPb502_proton_c35  .txt"  ,  size_spectrum   = (7,8),endrow_spectrum = 7,
              scan_loop = N
              )
v2proton502_3040.scan()

data_proton = v2proton502_05.errj + v2proton502_1020.errj + v2proton502_2030.errj + v2proton502_3040.errj
del v2proton502_05 , v2proton502_1020 , v2proton502_2030 , v2proton502_3040

minerr = 10000000
times = 0
"""for k in range(N):#for Tq
    for i in range(N):#for Tc
        for j in range(N):#for Ts
            dataerr = (np.reshape(v2D0502_3050.errj,(N,N,N))[i,k,:]+np.reshape(v2Ds502_3050.errj,(N,N,N))[j,i,:]
                       + np.reshape(data_pion,(N,N))[k,:])#+ np.reshape(v2Jpsi502_3050.errj,(N,N))[i,:]
            indexi = np.argmin(dataerr)
            if dataerr[indexi]<minerr:
                times +=1
                print(indexi,times)
                minerr = dataerr[indexi]

                ani = indexi
                tci = i
                tsi = j
                tqi = k"""


#data_pioni = np.reshape(data_pion, (N, N))
indexi = np.argmin(data_proton)
ani = int(indexi%N)
tqi = int((indexi - ani)/N)



for j in range(N):#for Ts
    dataerr = 10*np.reshape(v2D0502_3050.errj,(N,N,N))[:,tqi,ani]+np.reshape(v2Ds502_3050.errj,(N,N,N))[j,:,ani]#+np.reshape(v2Jpsi502_3050.errj,(N,N))[:,ani]
    indexi = np.argmin(dataerr)
    if dataerr[indexi]<minerr:
        times +=1
        print(indexi,times)
        minerr = dataerr[indexi]
        tci = indexi
        tsi = j

Ts = 0.545
Tc = 0.811
Tq = 0.42


tq0 = np.linspace(0.0001,Tq,int(N)) #0.32     ##0.34#up
aaray = np.linspace(0.0001,10,N)
tc0 = np.linspace(0.0001,Tc,N) #0.48     ##0.56#down
ts0 = np.linspace(0.0001,Ts,int(N)) #0.32     ##0.34#up


print("==========================5.02==================================")
print("errtotal = ",minerr)
print("tq0 = " , tq0[tqi])
print("ts0 = " , ts0[tsi])
print("tc0 = " , tc0[tci])
print("a2 = " , aaray[ani])
#print("errJpsi = ", dataJpsi[tc0i*N+ai])
#print("errD0 = ", dataD0[tq0i,tc0i*N+ai])
#print("errDs = ", dataDS[ts0i,tc0i*N+ai])

