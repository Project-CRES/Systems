
#########################################
#   INPUTS
#########################################


# Tank Pressures (bar)
Pf_tank = 4
Pox_tank = 5


# Main combustion chamber pressure (bar)
MCCPressure = 40

# Pressure losses (bar)

dP_MCCInj = MCCPressure * 0.2

dP_OxPipe_03 = 0.5
dP_OxPipe_04 = 0.5
dP_OxPipe_02 = 0.5
dP_OxPipe_01 = 0.2

dP_FuPipe_03 = 0.5
dP_FuPipe_02 = 0.5
dP_FuPipe_01 = 0.2

dP_Regen = 0.15*MCCPressure


# Pipe pressure retention factors
PipeLgPipe_02 = 0.98
PipeLgPipe_01 = 0.925


# Turbine pressure ratio
TurbinePressureRatio = 1.4


# Preburner injector pressure drop (bar)
dP_Pb = 14.8


# CALCULATED PRESSUERS

# MCC pressures (bar)
GasPMCCInj = MCCPressure + dP_MCCInj
MCC_Inj = MCCPressure + dP_MCCInj


# Turbine Pressures (bar)
TurbineOutletP = GasPMCCInj/PipeLgPipe_02
TurbineInletP = TurbineOutletP*TurbinePressureRatio


# Preburner pressures (bar)
Pb_ChamberP = TurbineInletP/PipeLgPipe_01
Pb_injectorP = Pb_ChamberP + dP_Pb


# Regen Pressures (bar) 
RegenOut = Pb_injectorP + dP_FuPipe_03
RegenIn = RegenOut + dP_Regen


# Oxygen Pump Pressures (bar)

POx_Pb = Pb_injectorP + dP_OxPipe_04
POx_MCC = MCC_Inj + dP_OxPipe_03


# Required Pressures (bar)
ReqP_MCC = MCC_Inj + dP_OxPipe_03
ReqP_Pb = Pb_injectorP + dP_OxPipe_04


OxPumpIn = Pox_tank - dP_OxPipe_01
OxPumpOut = max(ReqP_Pb, ReqP_MCC) + dP_OxPipe_02

dP_OxPump = OxPumpOut - OxPumpIn 


# Fuel Pump Pressures (bar)
FuPumpIn = Pf_tank - dP_FuPipe_01
FuPumpOut = RegenIn + dP_FuPipe_02


if __name__ == "__main__":
    # Print results only when running CEA.py directly
    print("Fuel pump in: ", round(FuPumpIn,1))
    print("Fuel pump out: ", round(FuPumpOut,1))
    print("Regen in: ", round(RegenIn,1))
    print("Regen out: ", round(RegenOut,1))
    print("PB injector: ", round(Pb_injectorP, 1))
    print("Ox Pump in:", round(OxPumpIn,1))
    print("OX pump out: ", round(OxPumpOut, 1))
    print("Required MCC pressure: ", round(ReqP_MCC,1))
    print("Required PB pressure: ", round(ReqP_Pb,1))
    print("Pb injector: ", round(Pb_injectorP,1))
    print("MCC injector: ", round(MCC_Inj,1))
    print("Ox pump pressure rise: ", round(dP_OxPump,1))
    print("Pressure of gas at MCC injector: ", round(GasPMCCInj,1))
    print("Turbine outlet pressure: ", round(TurbineOutletP,1))
    print("Turbine inlet pressure: ", round(TurbineInletP,1))
    print("Preburner chambere pressure:", round(Pb_ChamberP,1))
