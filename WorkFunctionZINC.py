#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python  
#Photoelectric effect- Calculation of WorkFunction
#Error Calculation from Theoretical and Calculated Value
# Amrutha V-lab Simulation Result
 
#ZINC #ZINC #ZINC #ZINC #ZINC #ZINC
       
#Variable declaration


e = 1.6e-19; # Charge on an electron, C
h = 6.626e-34; # Planck's constant, Js
c = 3.0e+08; # Speed of light in vacuum, m/s
W_Theo = 4.31; # Theoretical Value of Work Function of Zn in eV
lamb = float(input("Enter the Wavelenghth (in meter) :")); # Wavelength of incident light (meter)
V_0 = float(input("Enter the Stopping potential (-ve) :" )); # Stopping potential for emitted electrons, V                


#Calculation

f = c/lamb; # Frequency of incident radiation , Hz
E = (h*f); # Energy carried by one photon from Planck's law, J
K_max = (e*V_0); # Maximum kinetic energy of electrons, J
 # We have, WorkFunction W = E-K_max
W_in_joule = ((h*f)-(e*V_0));
 #Converting to eV, Dividing by e=1.6e-19 to get WorkFunction
W_in_eV = (W_in_joule/e)


#Result


print("The work function of Zn metal (in joule) = ")
print (W_in_joule , "joule")
print("The work function of Zn metal (in eV) = ")
print (W_in_eV,"eV")

#Error Calculation
print("Theoretical Value of WorkFunction of Zn:-", W_Theo ,"eV" )
print("Calculated Value of WorkFunction of Zn:-",W_in_eV,"eV")

#Error=(|theoreticalValue-CalculatedValue|)/theoreticalValue
Error=(W_Theo-W_in_eV)/(W_Theo)
print("ErrorCalculated=",Error)

#Error%=Error*100
Error_Percent = Error*100
print("ErrorPercentage=",Error_Percent,"%")


# In[ ]:





# In[ ]:




