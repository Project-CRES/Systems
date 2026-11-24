import CEA
import PressureCode

F_MCC = 15000 # MCC thrust (N)
g = 9.81
ISP = 3 #Specific impulse, get it from somewhere

m_dot_total = F_MCC/(CEA.maxIsp*g) # kg/s
m_dot_fuel = m_dot_total/(CEA.ReqOF + 1) # kg/s
m_dot_ox = CEA.ReqOF * m_dot_fuel


# Preburner stuff
OF_Pb = 0 # for now
m_dot_fuel_Pb = m_dot_fuel
m_dot_ox_Pb = OF_Pb * m_dot_fuel_Pb
m_dot_total_Pb = m_dot_ox_Pb + m_dot_fuel_Pb

# Turbine
m_dot_total_turb = m_dot_total_Pb



print(round(m_dot_ox, 3))
