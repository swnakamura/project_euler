n=600851475143
i=2

while i<=n:
	if n%i==0:
		ans=i
		n/=i
	else:
		i+=1


print(ans)
