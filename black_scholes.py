import math
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):

    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call_price = (S * norm.cdf(d1) -K * math.exp(-r * T) * norm.cdf(d2))
    return call_price

def black_scholes_put(S, K, T, r, sigma):

    d1 = (math.log(S / K) +(r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    put_price = (K * math.exp(-r * T) * norm.cdf(-d2) -S * norm.cdf(-d1))
    return put_price

S = 100      
K = 105      
T = 1        
r = 0.05     
sigma = 0.2  

call = black_scholes_call(S, K, T, r, sigma)
put = black_scholes_put(S, K, T, r, sigma)

print("Call Option Price:", round(call, 2))
print("Put Option Price :", round(put, 2))