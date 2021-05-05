#!/usr/bin/env python
# coding: utf-8

# In[7]:


#GRAPH - 2 COPPER
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-8,-7,-6,-5,-4,-3,-2,-1,0]                                                              #abscissa
y1=[0.00,0.72,1.72,2.72,3.72,4.72,5.72,6.72,7.72]                                           #ordinate
x2=[-8,-7,-6,-5,-4,-3,-2,-1,0]
y2=[0.00,1.07,2.57,4.07,5.57,7.07,8.57,10.07,11.57]
x3=[-8,-7,-6,-5,-4,-3,-2,-1,0]
y3=[0.00,1.43,3.43,5.43,7.43,9.43,11.43,13.43,15.43]
plt.plot(x1,y1, linestyle='--', marker='+', color='indigo',label="Int-10w/m^2 Area-0.1cm^2") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Int-15w/m^2 Area-0.1cm^2")
plt.plot(x3,y3, linestyle='--', marker='+',color='green',label="Int-20w/m^2 Area-0.1cm^2")
plt.grid(True)                                                                               #grid              
plt.xlabel('POTENTIAL')                                                                      #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                                 #ordinate_name
plt.title("CONST WAVEL-100nm" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=2.0MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                                     #legend
plt.show()


# In[8]:


#GRAPH - 2 COPPER
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-8,-7,-6,-5,-4,-3,-2,-1,0,0.5,1]                                                             #abscissa
y1=[0.00,0.72,1.72,2.72,3.72,4.72,5.72,6.72,7.72,7.72,7.72]                                      #ordinate
x2=[-8,-7,-6,-5,-4,-3,-2,-1,0,0.5,1]
y2=[0.00,1.07,2.57,4.07,5.57,7.07,8.57,10.07,11.57,11.57,11.57]
x3=[-8,-7,-6,-5,-4,-3,-2,-1,0,0.5,1]
y3=[0.00,1.43,3.43,5.43,7.43,9.43,11.43,13.43,15.43,15.43,15.43]
plt.plot(x1,y1, linestyle='--', marker='+', color='indigo',label="Int-10w/m^2 Area-0.1cm^2")     #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Int-15w/m^2 Area-0.1cm^2")
plt.plot(x3,y3, linestyle='--', marker='+',color='green',label="Int-20w/m^2 Area-0.1cm^2")
plt.grid(True)                                                                                   #grid              
plt.xlabel('POTENTIAL')                                                                          #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                                     #ordinate_name
plt.title("CONST WAVEL-100nm" "  " "Scale-XAxis-1Div=2.0V" "  ""YAxis-1Div=2.0MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                                         #legend
plt.show()


# In[9]:


#GRAPH - 2 PLATINUM
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-6.1,-5.1,-4.1,-3.1,-2.1,-1.1,-0.1,0.0]                                                    #abscissa
y1=[0.00,1.45,2.95,4.45,5.95,7.45,8.95,9.10]                                                   #ordinate
x2=[-6.1,-5.1,-4.1,-3.1,-2.1,-1.1,-0.1,0.0]
y2=[0.00,1.93,3.93,5.93,7.93,9.93,11.93,12.13]
x3=[-6.1,-5.1,-4.1,-3.1,-2.1,-1.1,-0.1,0.0]
y3=[0.00,0.97,1.97,2.97,3.97,4.97,5.97,6.07]
plt.plot(x1,y1, linestyle='--', marker='+', color='deeppink',label="Int-10w/m^2 Area-0.1cm^2") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='navy',label="Int-15w/m^2 Area-0.1cm^2")
plt.plot(x3,y3, linestyle='--', marker='+',color='darkgreen',label="Int-20w/m^2 Area-0.1cm^2")
plt.grid(True)                                                                                 #grid              
plt.xlabel('POTENTIAL')                                                                        #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                                   #ordinate_name
plt.title("CONST WAVEL-100nm" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=2.0MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                                       #legend
plt.show()


# In[8]:


#GRAPH - 2 PLATINUM
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-6.1,-5.1,-4.1,-3.1,-2.1,-1.1,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.7]                            #abscissa
y1=[0.00,1.45,2.95,4.45,5.95,7.45,8.95,9.10,9.10,9.10,9.10,9.10,9.10,9.10]                     #ordinate
x2=[-6.1,-5.1,-4.1,-3.1,-2.1,-1.1,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.7]
y2=[0.00,1.93,3.93,5.93,7.93,9.93,11.93,12.13,12.13,12.13,12.13,12.13,12.13,12.13]
x3=[-6.1,-5.1,-4.1,-3.1,-2.1,-1.1,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.7]
y3=[0.00,0.97,1.97,2.97,3.97,4.97,5.97,6.07,6.07,6.07,6.07,6.07,6.07,6.07]
plt.plot(x1,y1, linestyle='--', marker='+', color='deeppink',label="Int-10w/m^2 Area-0.1cm^2") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='navy',label="Int-15w/m^2 Area-0.1cm^2")
plt.plot(x3,y3, linestyle='--', marker='+',color='darkgreen',label="Int-20w/m^2 Area-0.1cm^2")
plt.grid(True)                                                                                 #grid              
plt.xlabel('POTENTIAL')                                                                        #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                                   #ordinate_name
plt.title("CONST WAVEL-100nm" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=2.0MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                                       #legend
plt.show()


# In[15]:


#GRAPH - 2 ZINC 
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-8.2,-7.2,-6.2,-5.2,-4.2,-3.2,-2.2,-1.2]                                                   #abscissa
y1=[0.00,0.92,1.92,2.92,3.92,4.92,5.92,6.92]                                                   #ordinate
x2=[-8.2,-7.2,-6.2,-5.2,-4.2,-3.2,-2.2,-1.2]
y2=[0.00,1.37,2.87,4.37,5.87,7.37,8.87,10.37]
x3=[-8.2,-7.2,-6.2,-5.2,-4.2,-3.2,-2.2,-1.2]
y3=[0.00,1.83,3.83,5.83,7.83,9.83,11.83,13.83]
plt.plot(x1,y1, linestyle='--', marker='+', color='magenta',label="Int-10w/m^2 Area-0.1cm^2") #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Int-15w/m^2 Area-0.1cm^2")
plt.plot(x3,y3, linestyle='--', marker='+',color='darkgreen',label="Int-20w/m^2 Area-0.1cm^2")
plt.grid(True)                                                                                 #grid              
plt.xlabel('POTENTIAL')                                                                        #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                                   #ordinate_name
plt.title("CONST WAVEL-100nm" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=2.0MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                                       #legend
plt.show()


# In[16]:


#GRAPH - 2 ZINC 
import matplotlib.pyplot as plt
# values of x and y axis
x1=[-8.2,-7.2,-6.2,-5.2,-4.2,-3.2,-2.2,-1.2,-0.2,0.2,0.3,0.4,0.5,0.7]                           #abscissa
y1=[0.00,0.92,1.92,2.92,3.92,4.92,5.92,6.92,6.92,6.92,6.92,6.92,6.92,6.92]                      #ordinate
x2=[-8.2,-7.2,-6.2,-5.2,-4.2,-3.2,-2.2,-1.2,-0.2,0.2,0.3,0.4,0.5,0.7]
y2=[0.00,1.37,2.87,4.37,5.87,7.37,8.87,10.37,10.37,10.37,10.37,10.37,10.37,10.37]
x3=[-8.2,-7.2,-6.2,-5.2,-4.2,-3.2,-2.2,-1.2,-0.2,0.2,0.3,0.4,0.5,0.7]
y3=[0.00,1.83,3.83,5.83,7.83,9.83,11.83,13.83,13.83,13.83,13.83,13.83,13.83,13.83]
plt.plot(x1,y1, linestyle='--', marker='+', color='magenta',label="Int-10w/m^2 Area-0.1cm^2")  #+-plus
plt.plot(x2,y2, linestyle='--', marker='+', color='red',label="Int-15w/m^2 Area-0.1cm^2")
plt.plot(x3,y3, linestyle='--', marker='+',color='darkgreen',label="Int-20w/m^2 Area-0.1cm^2")
plt.grid(True)                                                                                 #grid              
plt.xlabel('POTENTIAL')                                                                        #abscissa_name
plt.ylabel('PHOTOCURRENT-I')                                                                   #ordinate_name
plt.title("CONST WAVEL-100nm" "  " "Scale-XAxis-1Div=1.0V" "  ""YAxis-1Div=2.0MicrAmp",loc='right',rotation=0)
plt.legend(loc = "best")                                                                       #legend
plt.show()


# In[ ]:




