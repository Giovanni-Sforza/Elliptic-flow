import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si
from scipy.special import ellipeinc as ellip
from scipy.interpolate import CubicSpline
from scipy.special import beta



class v2:
    """
    Elliptic flow calculator


    parameters
    ------------------------------------------------------------------
    cT Tq
    cc Tc : (float) the parameter for fitting the meson spectra by the recombination model with recombination_v16.f90
    cs Ts

    tq0 tc0 ts0 : (float) the parameter for fitting the Elliptic flow

    b : (float) the impact parameter, whose dependence on the centrality can found in arXiv:1301.4361v3 [nucl-ex]

    c2phiS, c2phiJ : (float) the phi-dependent part of the ridge and minijet contribution

    a2 : the amplitudes for <cos n phi >_j , determined by fitting the Elliptic flow

    Npart : (float) can found in ALICE Collaboration / ALICE-PUBLIC-2018-011

    scan_loop : (int) the times of loops when scanning the parameters ( tq0 tc0 ts0 a2 )

    IDpart : (int) the ID label the particles

    Task : (int) choose the program tasks

    Isys : (int) collision system

    plotname : (string) the name of the picture

    filename_v2 , filename_spectrum : (string) the data file name which can found in ALICE.
    Heeding : you mast load with your local path to this file

    size_v2 , size_spectrum : (tuple) the data size

    errj : (numpy array) the error for saving the error when fitting the Elliptic flow


    --------------------------------------------------------------------------------------
    methods
    --------------------------------------------------------------------------------------

    openfile : (static method) open file of meson spectrum and elliptic flow
               return numpy array

    c2phiS : (static method) calculate the  <cos 2 phi >_S
              return float

    fbc , fCq_c , fNpart_c : (instance methods) determine the dependence b, CT, Cs on centrality by interpolation
              return float

    Bh , Rh , Mh : (instance methods) the base, ridge, and minijet distribution
              return numpy array

    v2clcu : (instance methods) the final calculator for the elliptic flow
              return numpy array

    plot : (instance methods) plot the fit picture
              show the picture & save them in your\local\path\cache

    scan : (instance methods) scan the fitting parameters for the elliptic flow ( tq0 tc0 ts0 a2 )
              return numpy array of error

    """

    """
    IDpart = 1 for pion, 2 for Kaon, 3 for proton, 4 for lambda^0, 5 for Xi, 6 for Phi, 
             7 for Omega,  8 for Jpsi, 9 for D^0, 10 for D_s
    
    Isys = 1 for PbPb at 2.76, 2 for PbPb at 5.02
    
    Task = 1 for scanning, 2 for plot
    """
    def __init__(self,**kwargs):


        self.Isys = kwargs.get('Isys')
        self.Isys = int(self.Isys)
        self.IDpart ,self.Task = kwargs.get('IDpart'), kwargs.get('Task')
        self.IDpart = int(self.IDpart )
        self.Task = int(self.Task)




        self.c= kwargs.get('c')

        #self.cT, self.cs , self.cc = kwargs.get('cT'), kwargs.get('cs'), kwargs.get('cc')
        #self.Tq , self.Tc , self.Ts  = kwargs.get('Tq') , kwargs.get('Tc') , kwargs.get('Ts')

        self.fbc()
        self.fCq_c()
        self.fNpart_c()

        if self.Task == 1:
            self.scan_loop = kwargs.get('scan_loop')
            self.scan_loop = int(self.scan_loop)
        elif self.Task == 2:

            self.tq0, self.tc0, self.ts0 = kwargs.get('tq0'), kwargs.get('tc0'), kwargs.get('ts0')
            self.a2 =  kwargs.get('a2')
            self.c2phiJ = self.a2*self.b/np.pi

        self.c2phiS = self.c2phiSf(self.b)

        if(self.Isys == 1):
            self.Tq = 0.39
            self.Ts = 0.51
            self.Tc = 0.646
        elif(self.Isys == 2):
            self.Tq = 0.42
            self.Ts = 0.545
            self.Tc = 0.811


        self.plotname = kwargs.get('plotname')

        self.filename_v2, self.size_v2,self.endrow_v2 = kwargs.get('filename_v2'), kwargs.get('size_v2'),kwargs.get('endrow_v2')

        self.filename_spectrum , self.size_spectrum ,self.endrow_spectrum = kwargs.get('filename_spectrum'), kwargs.get('size_spectrum') , kwargs.get('endrow_spectrum')


        self.data_v2 = self.openfile(self.filename_v2, self.size_v2, 1,self.endrow_v2)

        self.data_spectrum = self.openfile(self.filename_spectrum, self.size_spectrum  ,2 ,self.endrow_spectrum)

        self.data_v2 = np.array( self.data_v2 )
        self.data_spectrum = np.array( self.data_spectrum )

        self.v2pt = self.data_v2[:,0]

        self.spectrumpt = self.data_spectrum[:,0]

        if np.shape(self.data_v2)[1] == 3:
            self.pterror = np.zeros(np.shape(self.data_v2[:,0]))
            self.v2data = self.data_v2[:, 1]
            self.v2dataerror = self.data_v2[:, 2]
        elif np.shape(self.data_v2)[1] == 4:
            self.pterror = self.data_v2[:, 1]
            self.v2data = self.data_v2[:, 2]
            self.v2dataerror = self.data_v2[:, 3]#*3**(1/2)

        elif np.shape(self.data_v2)[1]  == 5:
            self.pterror = [self.data_v2[:, 1], self.data_v2[:, 2]]
            # self.pterror = np.transpose(self.pterror)
            self.v2data = self.data_v2[:, 3]
            self.v2dataerror = self.data_v2[:, 4]



        self.Bh = np.vectorize(self.Bh)
        self.Rh = np.vectorize(self.Rh)

        alph0 = 1.75
        beta0 = 1.05

        self.g_p_pri = beta(alph0+2 , beta0+2 ) * beta(alph0+2 ,alph0 + beta0 +4 )
        self.g_p = (beta(alph0+1 , alph0+beta0+2 ) * beta(alph0+1 , beta0+1 ))**(-1)
        self.g_st_pri = 1/6
        self.errj = []
        #return self


    @staticmethod
    def openfile(filename, size, biginrow,endrow):
        file = open(filename, "r")  # 以只读模式打开文件
        lines = file.readlines()  # 获取所有行并保存到lines列表中
        data = []
        # 指定开始读取的行
        for line in lines[int(biginrow) - 1:]:  # 读取指定的所有行
            line = line.strip('\n')  # 去掉换行符
            line = line.split()
            data = np.hstack((data, line))  # 去掉空格
        file.close()  # 关闭文件
        data = np.array(data, dtype=float)
        data = np.reshape(data, size)
        if int(endrow) < size[0]:
            data = np.delete(data,range(int(endrow),size[0]),0)
        return data


    def fbc(self):
        c = np.array(
            [0.5, 1.5, 2.5, 3.5, 4.5, 7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5, 52.5, 57.5, 62.5, 67.5, 72.5,
             77.5, 82.5, 87.5])/100
        b = np.array(
            [0.785, 1.895, 2.465, 2.92, 3.315, 4.22, 5.495, 6.515, 7.395, 8.18, 8.89, 9.555, 10.175, 10.755, 11.31,
             11.835, 12.335, 12.815, 13.285, 13.745, 14.2, 14.695])
        f_b = CubicSpline(c, b)
        self.b = f_b(self.c)/7
        print("b = ",self.b)
        return self.b


    def fCq_c(self):
        if (self.Isys == 1):
            c = np.array([2.5, 15, 30, 50])/100
            Cq = np.array([23.2, 19.5, 15.5, 11])
            Cs = np.array([11, 9.2, 7.33, 5.04])
            deg = len(c)
            if(self.c < 0.2):
                self.cc =  0.766
            else:
                self.cc =  0.326

        elif(self.Isys == 2):
            c = np.array([2.5, 35, 50])/100
            Cq = np.array([22, 13.4, 6.8])
            Cs = np.array([10, 6.55, 3.4])
            deg = len(c)
            if(self.c < 0.2):
                self.cc =  0.481
            else:
                self.cc =  0.201

        f_Cq = CubicSpline(c, Cq)
        f_Cs = CubicSpline(c, Cs)

        self.cT = f_Cq(self.c)
        self.cs = f_Cs(self.c)
        print("CT = ",self.cT,"cs = ",self.cs)

        return self.cT,self.cs

    def fNpart_c(self):
        if (self.Isys ==1):
            c = np.array(
                [0.5, 1.5,2.5, 7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5,
                 47.5, 52.5, 57.5, 62.5, 67.5, 72.5, 77.5, 82.5, 87.5, 92.5, 97.5])/100
            deg = len(c)
            Npart = np.array(
                [400.8, 392.4, 381.5, 327.8, 280.1, 238.5, 202.1,
                 170.8, 142.7, 117.6, 96.09, 77.27, 61.08, 47.47, 35.76, 26.31, 18.67, 12.91, 8.588, 5.438, 3.315,
                 2.238])
        elif(self.Isys == 2):
            c = np.array(
                [0.5, 1.5, 2.5, 7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5,
                 47.5, 52.5, 57.5, 62.5, 67.5, 72.5, 77.5, 82.5, 87.5, 92.5, 97.5])/100
            deg = len(c)
            Npart = np.array(
                [401.9, 393.9,  383.4, 331.2, 283, 241, 204.1, 171.7,
                 143.2, 118.4, 96.58, 77.68, 61.28, 47.39, 35.7, 26.23, 18.63, 12.8, 8.481, 5.433, 3.309, 2.241])
        f_CNpart = CubicSpline(c, Npart)
        self.Npart = f_CNpart(self.c)
        print("Npart = ",self.Npart)
        return 0


    @staticmethod
    def c2phiSf(b):
        def S2(phi,b):
            h = np.sqrt(1 - b ** 2 / 4)
            w = 1 - b / 2
            sigma = 0.33
            phi2 = phi + sigma
            phi1 = phi - sigma
            alpha = 1 - (w / h) ** 2
            def theta(phi):  # for an analytic continuation of phi in range(0,2pi)
                if np.array(phi) <= np.pi / 2:
                    theta_ = np.arctan((h / w) * np.tan(phi))
                elif np.pi / 2 < np.array(phi) <= np.pi:
                    theta_ = np.pi / 2 + abs(np.arctan(1 / ((h / w) * np.tan(phi))))
                elif np.pi < np.array(phi) <= 3 * np.pi / 2:
                    theta_ = np.pi + abs(np.arctan((h / w) * np.tan(phi)))
                elif 3 * np.pi / 2 < np.array(phi) <= 2 * np.pi:
                    theta_ = 3 * np.pi / 2 + abs(np.arctan(1 / ((h / w) * np.tan(phi))))
                else:
                    theta_ = 2 * np.pi + np.arctan((h / w) * np.tan(phi))
                return theta_
            theta1 = theta(phi1)
            theta2 = theta(phi2)
            fun = h * (ellip(theta2, alpha) - ellip(theta1, alpha))
            return fun

        def tS(phi,b):
            def f(t):
                return S2((phi-t),b)
            result , err = si.quad(f, -np.pi/4 , np.pi/4,epsrel = 1e-015,limit = 100)
            return result*2/np.pi

        def normalforS(b):
            result , err = si.quad(tS,0.0000001 , 2*np.pi , args = (b),epsrel = 1e-015,limit = 100)
            result = 2*np.pi/result
            return result

        def f1(phi,b):
            return np.cos(2 * phi) *tS(phi,b)
        result ,err = si.quad(f1,0.0000001,2*np.pi,args = (b),epsrel = 1e-015,limit = 100)
        results = result / 2 / np.pi * normalforS(b)
        #print(results)
        return results



    def Bh(self,pt):
        if self.IDpart == 1:
            u = (2.8 + 0.003 * self.Npart) * np.e ** (-pt / 0.45)
            C = (1 + u) * self.cT ** 2 / 6
            funt0 = np.e ** (-pt / self.tq0)
            B = C * funt0

        elif self.IDpart == 3:
            B = self.g_p *self.g_p_pri*self.g_st_pri *self.cT**3 * pt**2 / ((0.938 ** 2 + pt ** 2) ** (1 / 2)) * np.e ** (-pt /self.tq0)

        elif self.IDpart == 8:
            B = self.cc ** 2 * pt / (4 * (3.0969 ** 2 + pt ** 2) ** (1 / 2)) * np.e ** (-pt / self.tc0)

        elif self.IDpart == 9:
            C = 12 * 2.3 * self.cc * self.cT / ((1.865 ** 2 + pt ** 2) ** (1 / 2) * pt ** 5)
            ft0 = lambda x: x ** 2 * (pt - x) ** 3 * np.e ** (-x / self.tq0 - (pt - x) / self.tc0)
            funt0, err = si.quad(ft0, 0.0000001, pt,limit = 100,epsrel = 1e-015)
            B = C * funt0

        elif self.IDpart == 10:
            C = 60 * self.cc * self.cs / ((1.968 ** 2 + pt ** 2) ** (1 / 2) * pt ** 7)
            ft0 = lambda x: x ** 3 * (pt - x) ** 4 * np.e ** (-x / self.ts0 - (pt - x) / self.tc0)
            funt0, err = si.quad(ft0, 0.0000001, pt,limit = 100,epsrel = 1e-015)
            B = C * funt0

        return B  # N is neglected either
    #Bh = np.vectorize(Bh)#,excluded=['self'])


    def Rh(self,pt):


        if self.IDpart == 1:
            u = (2.8 + 0.003 * self.Npart) * np.e ** (-pt / 0.45)
            C = (1 + u) * self.cT ** 2 / 6
            funt0 = np.e ** (-pt / self.tq0)
            funT = np.e ** (-pt / self.Tq)
            R = C * (funT - funt0)

        elif self.IDpart == 3:
            C_0 = self.g_p *self.g_p_pri*self.g_st_pri *self.cT**3 * pt**2 /((0.938 ** 2 + pt ** 2) ** (1 / 2)) * np.e ** (-pt /self.tq0)
            C =  self.g_p *self.g_p_pri*self.g_st_pri *self.cT**3 * pt**2 /((0.938 ** 2 + pt ** 2) ** (1 / 2))* np.e ** (-pt /self.Tq)
            R = C - C_0

        elif self.IDpart == 8:
            C_0 = self.cc ** 2 * pt / (4 * (3.0969 ** 2 + pt ** 2) ** (1 / 2)) * np.e ** (-pt / self.tc0)
            C = self.cc ** 2 * pt / (4 * (3.0969 ** 2 + pt ** 2) ** (1 / 2)) * np.e ** (-pt / self.Tc)
            R = C - C_0

        elif self.IDpart == 9:
            C = 12 * 2.3 * self.cc * self.cT / ((1.865 ** 2 + pt ** 2) ** (1 / 2) * pt ** 5)
            fT = lambda x: x ** 2 * (pt - x) ** 3 * np.e ** (-x / self.Tq - (pt - x) / self.Tc)
            ft0 = lambda x: x ** 2 * (pt - x) ** 3 * np.e ** (-x / self.tq0 - (pt - x) / self.tc0)
            funT, err = si.quad(fT, 0.0000001, pt,limit = 100,epsrel = 1e-015)
            funt0, err = si.quad(ft0, 0.0000001, pt,limit = 100,epsrel = 1e-015)
            R = C * (funT - funt0)

        elif self.IDpart == 10:
            C = 60 * self.cc * self.cs / ((1.968 ** 2 + pt ** 2) ** (1 / 2) * pt ** 7)
            fT = lambda x: x ** 3 * (pt - x) ** 4 * np.e ** (-x / self.Ts - (pt - x) / self.Tc)
            ft0 = lambda x: x ** 3 * (pt - x) ** 4 * np.e ** (-x / self.ts0 - (pt - x) / self.tc0)
            funT, err = si.quad(fT, 0.0000001, pt,limit = 100,epsrel = 1e-015)
            funt0, err = si.quad(ft0, 0.0000001, pt,limit = 100,epsrel = 1e-015)
            R = C * (funT - funt0)

        return R
    #Rh = np.vectorize(Rh)#,excluded=['self'])


    def Mh(self):

        M = self.data_spectrum[:,2]
        return M

    def v2clcu(self):
        if self.Task == 1:
            pt = self.v2pt

        else:
            pt = self.spectrumpt


        result = (self.Rh(pt) * self.c2phiS + self.Mh() * self.c2phiJ) / (self.Bh(pt) + self.Rh(pt) + self.Mh())
        return result

    def plot(self):
        if self.IDpart == 1:
            plt.xlim(0, 2 )
            plt.ylim(0, 0.3)
        elif self.IDpart ==9 or self.IDpart ==10:
            plt.xlim(0,8 )
            plt.ylim(np.min(self.v2data-self.v2dataerror)-0.05,  np.max(self.v2data+self.v2dataerror)+0.05)
        elif self.IDpart == 8 :
            plt.xlim(0,12 )
            plt.ylim(np.min(self.v2data)-0.5, np.max(self.v2data) +0.5)


        plt.title(self.plotname)
        plt.plot(self.spectrumpt, self.v2clcu(), label="recombination")
        plt.errorbar(self.v2pt, self.v2data,xerr = self.pterror, yerr=self.v2dataerror, fmt='o', capsize=3, label='alice')

        plt.xlabel("$P_{T}$(GeV/c)")
        plt.ylabel("v2(pT,b)")
        plt.savefig("cache\ "+self.plotname+'.png', bbox_inches='tight')
        plt.legend()
        plt.show()


    def scan(self):

        self.tq0_save = self.Tq
        self.tc0_save = self.Tc
        self.ts0_save = self.Ts

        if self.IDpart == 1:
            for self.tq0 in np.linspace(0.0001,self.tq0_save,num =self.scan_loop):
                for self.a2 in np.linspace(0.0001,10,num =self.scan_loop):
                    self.c2phiJ = self.a2 * self.b / np.pi
                    erri = np.sum((self.v2clcu() - self.v2data) ** 2/self.v2data**2)/np.shape(self.v2data)[0]


                    self.errj.append(erri)
            print("err = ", np.sum(self.Rh(self.v2pt) + self.Bh(self.v2pt) - self.data_spectrum[:, 1]))

            #self.errj = np.reshape(self.errj, ( int(self.scan_loop), int(self.scan_loop)))

        elif self.IDpart == 3:
            for self.tq0 in np.linspace(0.0001,self.tq0_save,num =self.scan_loop):
                for self.a2 in np.linspace(0.0001,10,num =self.scan_loop):
                    self.c2phiJ = self.a2 * self.b / np.pi
                    erri = np.sum((self.v2clcu() - self.v2data) ** 2/self.v2data**2)/np.shape(self.v2data)[0]


                    self.errj.append(erri)
            print("err = ", np.sum(self.Rh(self.v2pt) + self.Bh(self.v2pt) - self.data_spectrum[:, 1]))

        elif self.IDpart == 8:
            for self.tc0 in np.linspace(0.0001,self.tc0_save,num =self.scan_loop):
                for self.a2 in np.linspace(0.0001,10,num =self.scan_loop):

                    self.c2phiJ = self.a2 * self.b / np.pi
                    erri = np.sum((self.v2clcu() - self.v2data) ** 2/self.v2data**2)/np.shape(self.v2data)[0]
                    self.errj.append(erri)
            print("err = ", np.sum(self.Rh(self.v2pt) + self.Bh(self.v2pt) - self.data_spectrum[:, 1]))



        elif self.IDpart == 9:

            for self.tc0 in np.linspace(0.0001, self.tc0_save, num=self.scan_loop):
                for self.tq0 in np.linspace(0.0001,self.tq0_save,num =self.scan_loop):

                    for self.a2 in np.linspace(0.0001, 10, num =self.scan_loop):
                        self.c2phiJ = self.a2 * self.b / np.pi
                        erri = np.sum((self.v2clcu() - self.v2data) ** 2/self.v2data**2)/np.shape(self.v2data)[0]

                        self.errj.append(erri)
            print("err = ", np.sum(self.Rh(self.v2pt) + self.Bh(self.v2pt) - self.data_spectrum[:, 1]))


        elif self.IDpart == 10:
            for self.ts0 in np.linspace(0.0001,self.ts0_save,num =self.scan_loop):
                for self.tc0 in np.linspace(0.0001, self.tc0_save, num =self.scan_loop):
                    for self.a2 in np.linspace(0.0001, 10,num = self.scan_loop):
                        self.c2phiJ = self.a2 * self.b / np.pi
                        erri = np.sum((self.v2clcu() - self.v2data) ** 2/self.v2data**2)/np.shape(self.v2data)[0]


                        self.errj.append(erri)
            print("err = ", np.sum(self.Rh(self.v2pt) + self.Bh(self.v2pt) - self.data_spectrum[:, 1]))


        self.errj = np.array(self.errj)
        print("finished scanning parameters" , self.IDpart)
        return self.errj

