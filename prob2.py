ans=0

a,b = 1,1

while(a<4000000):
	a,b = a+b,a
	if a%2==0 : ans+=a

print(ans)
