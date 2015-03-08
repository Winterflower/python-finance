"""
Studying the valuation of a European call option using Monte Carlo simulations
and Black-Scholes-Merton
"""
import numpy as np

#defining parameter values
S_0=100.
K=105.
T=1.0
r=0.05
sigma=0.2

#define the number of values we want to draw from standard distribution

I=100000

z=np.random.standard_normal(I)
# add print and type statements to examine contents
print z, type(z)
S_T=S_0*np.exp((r-0.5*sigma ** 2)*T + sigma * np.sqrt(T)*z)
print S_T, type(S_T)
hT=np.maximum(S_T-K,0)
C_0=np.exp(-r *T)* sum(hT)/ I

print "Value of the European Call Option %5.3f" % C_0



