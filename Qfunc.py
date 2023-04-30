from scipy.special import erfc
from scipy.optimize import root_scalar
from math import sqrt

def Q(x):
	result = 0.5 * erfc(x / (2**0.5))
	return result

def Qinv(Q_target):
	def func(x):
	    return erfc(x / 2**0.5) - 2*Q_target

	result = root_scalar(func, bracket=[0, 100])
	return result.root


def print_sci(x) -> str:
	return "{:.10e}".format(x)

"""
USAGE OF Q-functions

get value:
value: float = Q(x)
get string 
string_value: str = print_sci(Q(x))



print(Q(3))
print(Qinv(Q(3))) # I shloud get ~3 
"""

def PBER_BPSK(PBER): # get Eb/N0
	# Q(sqrt(2*Eb/NO))
	q_inv = Qinv(PBER)
	return((q_inv**2)/2)

PBER = 10**-5
print(PBER_BPSK(PBER))




#SNR -> Eb_N0 = > Eb/N0, bits => number of bits per symbol
def SNR(Eb_N0,bits):

	return (Eb_N0) + 10*log(bits)


"""
k = log_2(M) || log_10(M)/log_10(2)
M = 2^k

-----------------------
	M	|	k	| 
-----------------------
	2	|	1	|
-----------------------
	4	|	2	|
-----------------------
	8	|	3	|
-----------------------
	16	|	4	|
-----------------------
	32	|	5	|
-----------------------
	64	|	6	|
-----------------------
	128	|	7	|
-----------------------
	256	|	8	|

"""