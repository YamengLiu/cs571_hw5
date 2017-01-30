import random
import math

m=100
n=100

heads=[]
for i in range(m):
	a=random.random()
	if(a<=0.5):
		num=0
		for j in range(n):
			b=random.random()
			if(b<=0.8):
				num+=1
		heads.append(num)
		print str(i+1)+" th sample includes "+str(num)+" heads"
	else:
		num=0
		for j in range(n):
			b=random.random()
			if(b<=0.35):
				num+=1
		heads.append(num)
		print str(i+1)+" th sample includes "+str(num)+" heads"

thetaA=0.0
thetaB=0.0
thetaA_new=0.6 
thetaB_new=0.4
value=10**(-4)
while( abs(thetaA-thetaA_new)>value and abs(thetaB-thetaB_new)>value ):
	thetaA=thetaA_new
	thetaB=thetaB_new

	#E-step
	w=[]
	for i in range(m):
		coeff=float(math.factorial(n))/(math.factorial(heads[i])*math.factorial(n-heads[i]))
		weight_A=coeff*thetaA**float(heads[i])*(1-thetaA)**float(n-heads[i])
		weight_B=coeff*thetaB**float(heads[i])*(1-thetaB)**float(n-heads[i])
		weight=float(weight_A)/(weight_A+weight_B)
		w.append(weight)

	#M-step
	A_head=0
	A_total=0
	B_head=0
	B_total=0
	for i in range(m):
		A_head+=heads[i]*w[i]
		A_total+=n*w[i]
		B_head+=heads[i]*(1-w[i])
		B_total+=n*(1-w[i])
	thetaA_new=float(A_head)/A_total
	thetaB_new=float(B_head)/B_total

print "theta A is "+str(thetaA)
print "theta B is "+str(thetaB)

