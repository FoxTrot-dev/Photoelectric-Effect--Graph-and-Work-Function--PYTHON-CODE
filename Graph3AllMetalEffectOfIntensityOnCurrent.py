#!/usr/bin/env python
# coding: utf-8

# In[13]:


#GRAPH - 3 PLATINUM
import matplotlib.pyplot as plt
# values of x and y axis
x=[0,5,10,15,20,25,30]                                                #abscissa
y=[0,2.53,5.07,7.60,10.13,12.66,15.20]                                #ordinate
plt.plot(x,y, linestyle='--', marker='o', color='darkgreen',label="Platinum") #o-round
plt.grid(True)                                                        #grid              
plt.xlabel('INTENSITY')                                               #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                          #ordinate_name
plt.title("CONST POTEN=1V & WAVEL=100nm" "  " "Scale-XAxis-1Div=5W/m^2" "  ""YAxis-1Div=2.5MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                            #legend
plt.show()                                                   


# In[5]:


#GRAPH - 3 COPPER 
import matplotlib.pyplot as plt
# values of x and y axis
x=[0,5,10,15,20,25,30]                                              #abscissa
y=[0,3.36,6.72,10.07,13.43,16.79,20.15]                             #ordinate
plt.plot(x,y, linestyle='--', marker='o', color='b',label="Copper") #o-round
plt.grid(True)                                                      #grid              
plt.xlabel('INTENSITY')                                             #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                        #ordinate_name
plt.title("CONST POTEN=1V & WAVEL=100nm" "  " "Scale-XAxis-1Div=5W/m^2" "  ""YAxis-1Div=2.5MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                            #legend
plt.show()  


# In[14]:


#GRAPH - 3 ZINC
import matplotlib.pyplot as plt
# values of x and y axis
x=[0,5,10,15,20,25,30]                                                    #abscissa
y=[0,3.56,7.12,10.67,14.23,17.79,21.35]                                   #ordinate
plt.plot(x,y, linestyle='--', marker='o', color='indigo',label="Zinc")    #o-round
plt.grid(True)                                                            #grid              
plt.xlabel('INTENSITY')                                                   #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                              #ordinate_name
plt.title("CONST POTEN=1V & WAVEL=100nm" "  " "Scale-XAxis-1Div=5W/m^2" "  ""YAxis-1Div=2.5MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                  #legend
plt.show()


# In[ ]:




