#!/usr/bin/env python
# coding: utf-8

# In[2]:


#GRAPH - 1 COPPER
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-7.8,-7.3,-6.8,-6.3,-5.8,-5.3,-4.8,-4.3,-3.8]                                      #abscissa
y1=[0.00,0.21,0.46,0.71,0.96,1.21,1.46,1.71,1.96]                                      #ordinate
x2=[-5.7,-5.3,-4.7,-4.3,-3.7,-3.3,-2.7,-2.3,-1.7]
y2=[0.00,0.17,0.47,0.67,0.97,1.17,1.47,1.67,1.97]
x3=[-4.2,-3.7,-3.2,-2.7,-2.2,-1.7,-1.2,-0.5,-0.2]
y3=[0.00,0.23,0.48,0.73,0.98,1.23,1.48,1.83,1.98]
plt.plot(x1,y1, linestyle='--', marker='+', color='indigo',label="Wav-100nm f=3*10^6") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Wav-120nm f=2.5*10^6")
plt.plot(x3,y3, linestyle='--', marker='+',color='green',label="Wav-140nm f=2.14*10^6")
plt.grid(True)                                                                         #grid              
plt.xlabel('POTENTIAL')                                                                #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                           #ordinate_name
plt.title("CONST INTENS-5w/m^2" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=0.50MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                               #legend
plt.show()


# In[4]:


#GRAPH - 1 COPPER
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-7.8,-7.3,-6.8,-6.3,-5.8,-5.3,-4.8,-4.3,-3.8,-2.8,-1.8,-0.8,0.8,1.0,1.3]           #abscissa
y1=[0.00,0.21,0.46,0.71,0.96,1.21,1.46,1.71,1.96,1.96,1.96,1.96,1.96,1.96,1.96]        #ordinate
x2=[-5.7,-5.3,-4.7,-4.3,-3.7,-3.3,-2.7,-2.3,-1.7]
y2=[0.00,0.17,0.47,0.67,0.97,1.17,1.47,1.67,1.97]
x3=[-4.2,-3.7,-3.2,-2.7,-2.2,-1.7,-1.2,-0.5,-0.2]
y3=[0.00,0.23,0.48,0.73,0.98,1.23,1.48,1.83,1.98]
plt.plot(x1,y1, linestyle='--', marker='+', color='indigo',label="Wav-100nm f=3*10^6") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Wav-120nm f=2.5*10^6")
plt.plot(x3,y3, linestyle='--', marker='+',color='green',label="Wav-140nm f=2.14*10^6")
plt.grid(True)                                                                         #grid              
plt.xlabel('POTENTIAL')                                                                #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                           #ordinate_name
plt.title("CONST INTENS-5w/m^2" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=0.50MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                               #legend
plt.show()


# In[6]:


#GRAPH - 1 PLATINUM
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-6.1,-5.6,-5.1,-4.6,-4.1,-3.6]                                  #abscissa
y1=[0.00,0.23,0.48,0.73,0.98,1.23]                                  #ordinate
x2=[-4.0,-3.5,-3.0,-2.5,-2.0,-1.5]
y2=[0.00,0.25,0.50,0.75,1.00,1.25]
x3=[-2.6,-1.9,-1.6,-1.3,-0.6,0.0]
y3=[0.00,0.31,0.46,0.61,0.96,1.26 ]
plt.plot(x1,y1, linestyle='--', marker='+', color='indigo',label="Wav-100nm f=3*10^6") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Wav-120nm f=2.5*10^6")
plt.plot(x3,y3, linestyle='--', marker='+',color='green',label="Wav-140nm f=2.14*10^6")
plt.grid(True)                                                                         #grid              
plt.xlabel('POTENTIAL')                                                                #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                           #ordinate_name
plt.title("CONST INTENS-5w/m^2" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=0.50MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                               #legend
plt.show()


# In[7]:


#GRAPH - 1 PLATINUM
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-6.1,-5.6,-5.1,-4.6,-4.1,-3.6,-2.6,-1.6,-0.6,0.6,0.3,0.5]                          #abscissa
y1=[0.00,0.23,0.48,0.73,0.98,1.23,1.23,1.23,1.23,1.23,1.23,1.23]                       #ordinate
x2=[-4.0,-3.5,-3.0,-2.5,-2.0,-1.5,-0.5,0.3,0.4,0.5,0.8,0.9]
y2=[0.00,0.25,0.50,0.75,1.00,1.25,1.25,1.25,1.25,1.25,1.25,1.25]
x3=[-2.6,-1.9,-1.6,-1.3,-0.6,0.0,0.1,0.2,0.3,0.4,0.5,0.7]
y3=[0.00,0.31,0.46,0.61,0.96,1.26,1.26,1.26,1.26,1.26,1.26,1.26 ]
plt.plot(x1,y1, linestyle='--', marker='+', color='indigo',label="Wav-100nm f=3*10^6") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Wav-120nm f=2.5*10^6")
plt.plot(x3,y3, linestyle='--', marker='+',color='green',label="Wav-140nm f=2.14*10^6")
plt.grid(True)                                                                         #grid              
plt.xlabel('POTENTIAL')                                                                #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                           #ordinate_name
plt.title("CONST INTENS-5w/m^2" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=0.50MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                               #legend
plt.show()


# In[11]:


#GRAPH - 1 ZINC
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-8.2,-7.7,-7.2,-6.7,-6.2,-5.7,-5.2,-4.7,-4.2,-3.7]                                  #abscissa
y1=[0.00,0.21,0.46,0.71,0.96,1.21,1.46,1.71,1.96,2.21]                                 #ordinate
x2=[-6.1,-5.6,-5.1,-4.6,-4.1,-3.6,-3.1,-2.6,-2.1,-1.6]
y2=[0.00,0.22,0.47,0.72,0.97,1.22,1.47,1.72,1.97,2.22]
x3=[-4.6,-4,-3.6,-3,-2.6,-2,-1.6,-1,-0.6,0]
y3=[0.00,0.28,0.48,0.78,0.98,1.28,1.48,1.78,1.98,2.26]
plt.plot(x1,y1, linestyle='--', marker='+', color='indigo',label="Wav-100nm f=3*10^6") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Wav-120nm f=2.5*10^6")
plt.plot(x3,y3, linestyle='--', marker='+',color='green',label="Wav-150nm f=2.14*10^6")
plt.grid(True)                                                                         #grid              
plt.xlabel('POTENTIAL')                                                                #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                           #ordinate_name
plt.title("CONST INTENS-5w/m^2" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=0.50MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                               #legend
plt.show()


# In[12]:


#GRAPH - 1 ZINC
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-8.2,-7.7,-7.2,-6.7,-6.2,-5.7,-5.2,-4.7,-4.2,-3.7,-2.7,-1.7,-0.7,0.1,0.3,0.7]          #abscissa
y1=[0.00,0.21,0.46,0.71,0.96,1.21,1.46,1.71,1.96,2.21,2.21,2.21,2.21,2.21,2.21,2.21]       #ordinate
x2=[-6.1,-5.6,-5.1,-4.6,-4.1,-3.6,-3.1,-2.6,-2.1,-1.6,-0.6,0.1,0.2,0.4,0.5,0.6]
y2=[0.00,0.22,0.47,0.72,0.97,1.22,1.47,1.72,1.97,2.22,2.22,2.22,2.22,2.22,2.22,2.22]
x3=[-4.6,-4,-3.6,-3,-2.6,-2,-1.6,-1,-0.6,0,0.1,0.2,0.3,0.4,0.5,0.6]
y3=[0.00,0.28,0.48,0.78,0.98,1.28,1.48,1.78,1.98,2.26,2.26,2.26,2.26,2.26,2.26,2.26]
plt.plot(x1,y1, linestyle='--', marker='+', color='indigo',label="Wav-100nm f=3*10^6")     #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Wav-120nm f=2.5*10^6")
plt.plot(x3,y3, linestyle='--', marker='+',color='green',label="Wav-150nm f=2.14*10^6")
plt.grid(True)                                                                             #grid              
plt.xlabel('POTENTIAL')                                                                    #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                               #ordinate_name
plt.title("CONST INTENS-5w/m^2" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=0.50MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                                   #legend
plt.show()

