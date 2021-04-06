import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

#preso da https://scipy-lectures.org/intro/scipy/auto_examples/plot_curve_fit.html

# Seed the random number generator for reproducibility
#np.random.seed(0)

x_data=np.zeros(1280)#hardcoded perché mi secco
y_data=x_data
i=0

fh=open("incandescenza.txt")
for riga in fh :
    numeri=riga.split()
    x_data[i]=float(numeri[0])
    y_data[i]=float(numeri[1])
    i+=1#stampando dopo i+=1 vedo gli indici come se fosse matlab
    #print("i=",i,"x=",numeri[0],"y=",numeri[1])
    #print(numeri[0],numeri[1])
for i in range(len(y_data)) :
    print(y_data[i])



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


def planck(x, h, c, k, T):
    return (2*h*c**2)/((x)**5*(np.exp(h*c/(x*k*T))-1))

params, params_covariance = optimize.curve_fit(planck, x_data, y_data,
                                               p0=[1e-34, 1e8, 1e-23, 1e3])

#print(params)
print("h fit:",params[0])
#print("h teorico:",h)

print("c fit:",params[1])
#print("c teorico:",c)

print("k fit:",params[2])
#print("k teorico:",k)

print("T fit:",params[3])
#print("T teorico:",T)

plt.figure(figsize=(6, 4))
plt.plot(x_data, y_data, label='Data')
plt.plot(x_data, planck(x_data, params[0], params[1], params[2], params[3]),
         label='Fitted function')

plt.legend(loc='best')

plt.show()
