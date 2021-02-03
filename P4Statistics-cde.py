import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from scipy import optimize 


plt.rcParams.update({'font.size': 22})

data1 = np.loadtxt('hd000142.txt') # HD142
data2 = np.loadtxt('hd027442.txt') # HD27442
data3 = np.loadtxt('hd102117.txt') # HD102117

#_________________________ FUNCTION __________________________________________#
def lombscargle(dataset): # from Numerical Recipies
    
    # Define parameters
    time = dataset[:,0] # Times at which radial velocity was measured, days
    rv = dataset[:,1] # Radial velocities
    sigma = dataset[:,2] # Measurement error
    meanrv = np.mean(rv) # Mean of the measured radial velocities
    
    # Define frequency range using the Nyquist frequency
    w = omega(dataset) # Angular frequency interval  
    
    # Tau #
    tau = np.zeros(len(w))
    for i in range(len(w)):
        abov = np.sum(np.cos(2*w[i]*time)/(sigma**2))
        belo = np.sum(np.sin(2*w[i]*time)/(sigma**2))
        tau[i] = (1/(2*w[i]))*np.arctan(abov/belo)
    
    # Lomb Scargle
    P = np.zeros(len(w))
    norm = 1/2 #(2*np.var(rv))
    h = rv - meanrv
    for i in range(len(w)):
        c = np.cos(w[i]*(time - tau[i]))
        s = np.sin(w[i]*(time - tau[i]))
        aboveleft = np.sum((h*c)/sigma**2)
        aboveright = np.sum((h*s)/sigma**2)
        belowleft = np.sum((c**2)/sigma**2)
        belowright = np.sum((s**2)/sigma**2)
        P[i] = norm*(((aboveleft**2)/belowleft) + ((aboveright**2)/belowright))
    
    return P

def fold(dataset):
    time = dataset[:,0] # Times at which radial velocity was measured, days
    rv = dataset[:,1] # Radial velocities
   
    # Define frequency range using the Nyquist frequency
    w = omega(dataset) # Angular frequency interval  
    
    # Obtain period from Lomb Scargle
    lombi = lombscargle(dataset)
    wmax = w[lombi == np.max(lombi)] # Most likely angular frequency
    fmax = wmax/(2*np.pi)
    period = 1/fmax
    phases = np.mod(time, period)

    # Fit sinus curve
    def fitsin(time, A, B, C):
    
        return A*np.sin(2*np.pi*fmax*time + B) + C
    
    fits, covar = optimize.curve_fit(fitsin, phases, rv, p0=[0,0,0])
    A = fits[0] # Amplitude of the sinus curve we need
    B = fits[1]
    C = fits[2]
    
    # Plot the folded data and overplot sinus curve
    sint = np.linspace(min(phases), max(phases), 500)
    curve = A*np.sin(2*np.pi*fmax*sint + B) + C
    plt.figure(figsize=[10,4])
    plt.scatter(phases, rv)
    plt.plot(sint, curve, label=('\n A = %.2f $m \, s^{-1}$ \n' % np.abs(A)))
    plt.ylabel(r' RV [$ m \, s^{-1} $]')
    plt.xlabel(r' Time [days]')
    plt.legend()
    #plt.savefig('fold3_2.png', dpi=150, bbox_inches='tight')
    
    
    # Sinus curve over the raw data
    sint2 = np.linspace(min(time), max(time), 500)
    curve2 = A*np.sin(2*np.pi*fmax*sint2 + B) + C
    plt.figure(figsize=[10,4])
    plt.scatter(time, rv)
    plt.plot(sint2, curve2)
    plt.ylabel(r' RV [$ km \, s^{-1} $]')
    plt.xlabel(r' Time [days]')
    #plt.savefig('sin1.png', dpi=150, bbox_inches='tight')

    return period


def omega(dataset):
    w = 2*np.pi*np.linspace(0.0001, 0.5, 500) # Arbitrary angular frequency interval  
    time = dataset[:,0] # Times at which radial velocity was measured, days
    maxdif = time[1:] - time[:-1]   
    step = 1/(2*np.max(maxdif))

    # This gives the most likely frequency
    lombi = lombscargle(dataset)
    fmax = w[lombi == np.max(lombi)]/(2*np.pi) # Max frequency to be inspected
    
   # Calculate the real most likely frequency
    omegas = 2*np.pi*np.arange(step, 0.5, step)
    
    return omegas

def plot(dataset):
    time = dataset[:,0] # Times at which radial velocity was measured, days
    rv = dataset[:,1] # Radial velocities 
    w = omega(dataset) # Angular frequency interval 
   
    # Calculate period    
    lombi = lombscargle(dataset)
    wmax = w[lombi == np.max(lombi)] # Most likely angular frequency
    fmax = wmax/(2*np.pi)
    period = 1/fmax
    
#    # Calculate uncertainty levels for input dataset
#    z = np.asarray([np.max(lombi)*0.9999, np.max(lombi)*0.99,
#          np.max(lombi)*0.5 ])
#    M = -6.362 + 1.193*len(rv) + 0.00098*len(rv)**2
#    FAP = 1 - (1 - np.e**(-z))**M
    
    plt.figure(figsize=[10,4])
    plt.plot(w/(2*np.pi), lombscargle(dataset), label=('\n P = %.2f days \n' % period))
    plt.ylabel(r' P($\omega$) ')
    plt.xlabel(r' $\omega \, [days^{-1}]$')
    plt.legend()
    #plt.savefig('LS3_2.png', dpi=150, bbox_inches='tight')


    return period

#_________________________ REPORT PLOTS ______________________________________#
# Raw plots
plt.figure(figsize=[7,4])
plt.title('HD 102117 ')
plt.scatter(data1[:,0], data1[:,1])
plt.ylabel(r' RV [$ m \, s^{-1} $]')
plt.xlabel(r' Time [days]')
#plt.savefig('raw1.png', dpi=150, bbox_inches='tight')

plt.figure(figsize=[7,4])
plt.title('HD 102117 ')
plt.scatter(data2[:,0], data2[:,1])
plt.ylabel(r' RV [$ m \, s^{-1} $]')
plt.xlabel(r' Time [days]')
#plt.savefig('raw2.png', dpi=150, bbox_inches='tight')

plt.figure(figsize=[7,4])
plt.title('HD 102117 ')
plt.scatter(data3[:,0], data3[:,1])
plt.ylabel(r' RV [$ m \, s^{-1} $]')
plt.xlabel(r' Time [days]')
#plt.savefig('raw3.png', dpi=150, bbox_inches='tight')
