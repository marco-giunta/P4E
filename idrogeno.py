import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

#preso da https://scipy-lectures.org/intro/scipy/auto_examples/plot_curve_fit.html

x_data=np.zeros(1280)#hardcoded perché mi secco
y_data=x_data
i=0

fh=open("idrogeno.txt")
for riga in fh :
    numeri=riga.split()
    x_data[i]=float(numeri[0])
    y_data[i]=float(numeri[1])
    i+=1#stampando dopo i+=1 vedo gli indici come se fosse matlab
    #print("i=",i,"x=",numeri[0],"y=",numeri[1])
    #print(numeri[0],numeri[1])
#for i in range(len(y_data)) :
#    print(y_data[i])



#x_data = np.linspace(1, 3000, num=100)*1e-9
#h=6.626e-34;#cost planck SI
#k=1.38e-23;#cost boltzmann SI
#c=299792458;#vel luce SI
#T=2700
#y_data = (2*h*c**2)/((x_data)**5*(np.exp(h*c/(x_data*k*T))-1))

# And plot it

x_data*=1e-9
plt.figure(figsize=(6, 4))
plt.plot(x_data, y_data)

x=x_data[593:705]
y=y_data[593:705]

def lorentz(x, l0, gamma):
    pi=3.141592
    c=299792458;#vel luce SI
    return (1/(2*pi))*gamma/((2*pi*c*(1/x-1/l0))**2+(gamma/2)**2)

params, params_covariance = optimize.curve_fit(lorentz, x, y,
                                               p0=[6.56e-7, 1e9])

#print(params)
print("l0 fit:",params[0])
#print("h teorico:",h)

print("gamma fit:",params[1])
#print("c teorico:",c)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label='Data')
plt.plot(x, lorentz(x, params[0], params[1]),
         label='Fitted function')

plt.legend(loc='best')

plt.show()
