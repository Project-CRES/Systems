from rocketcea.cea_obj import CEA_Obj
from rocketcea.cea_obj_w_units import CEA_Obj
import matplotlib.pyplot as plt
import numpy as np


C = CEA_Obj( oxName='LOX', fuelName='Isopropanol', pressure_units='Bar', temperature_units='K', isp_units='sec',cstar_units='m/s')

# MCC pressure (bar)
Pc = 40

# atmospheric pressure (bar)
Pa = 1.01325

OFRatio = []
IspArray = []
Temperatures = []
CharV = []



for i in np.arange (0.5, 3.1, 0.1):
    eps = C.get_eps_at_PcOvPe(Pc=Pc, MR=i, PcOvPe= Pc/Pa, frozen=0, frozenAtThroat=0) # eps is nozzle expansion ratio, idk what it is so function converts Pc/Pa to eps

    AmbIsp = C.estimate_Ambient_Isp(Pc=Pc, MR=i, eps=eps, Pamb=Pa, frozen=0, frozenAtThroat=0) # Pamb is ambient pressure (14.7 psia), get_isp is specific thrust in vacuum so use estimate_ambient_isp

    Temp = C.get_Temperatures(Pc=Pc, MR=i, eps=eps, frozen=0, frozenAtThroat=0)

    CSt = C.get_Cstar(Pc = Pc, MR = i)


    OFRatio.append(i)
    IspArray.append(AmbIsp[0])
    Temperatures.append(Temp[0])
    CharV.append(CSt)

    print(f"O/F ratio: {i:.2f} Isp: {AmbIsp[0]:.2f} Temp: {Temp[0]:.2f} C*: {CSt:.2f}")

    #print(round(AmbIsp[0], 2))
    #print(round(Temp[0], 2))
    #print(round(CSt, 2))



maxIsp = max(IspArray)

ind = IspArray.index(maxIsp)

ReqOF = OFRatio[ind]
ReqTemp = Temperatures[ind]
ReqCharV = CharV[ind]



if __name__ == "__main__":
    # Print results only when running CEA.py directly

    print(f"O/F ratio: {ReqOF:.2f} Chamber Temp (K): {ReqTemp:.2f} max isp: {maxIsp:.2f} C*: {ReqCharV:.2f}")

    plt.figure(figsize=(8, 5)) # size of the plt window
    plt.figure(1)
    plt.title("LOX/IPA - Isp vs O/F")
    plt.plot(OFRatio, IspArray)
    plt.xlabel("O/F Ratio")
    plt.ylabel("Isp (sec)")
    plt.ylim(200, ) # y lim is set to 200 - largest value


    plt.figure(figsize=(8, 5))
    plt.figure(2)
    plt.title("LOX/IPA - Temp vs O/F")
    plt.plot(OFRatio, Temperatures)
    plt.xlabel("O/F Ratio")
    plt.ylabel("Temperatures (K)")
    plt.ylim(200, )


    plt.figure(figsize=(8, 5))
    plt.figure(3)
    plt.title("LOX/IPA - C* vs O/F")
    plt.plot(OFRatio, CharV)
    plt.xlabel("O/F Ratio")
    plt.ylabel("C* (m/s)")
    plt.ylim(200, )


    plt.show()
