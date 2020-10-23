# pow(x, y) is equal to x^y
# pow(x, y, z) is equal to x^y % z

# Fermat’s little theorem

def nPrmoduloN(n,r,N):
	num,den = 1,1	#numerator and denominator
	
	for i in range(r):
		num = (num*(n-i))%N
		den = (den*(i+1))%N

	return (num*pow(den,N-2,N))%N


n,r,N = 10,2,13
print(nPrmoduloN(n,r,N))