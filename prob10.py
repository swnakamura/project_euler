#prob7を解いていれば、それを使うことで余裕


n=2000010#余裕をもたせておく

prime_or_not=[1]*n
num=0
for i in range(2,n):
	j=i
	if(prime_or_not[j]==1):
		j+=i
		num+=1
		while(j<n):
			prime_or_not[j]=0
			j+=i

ans=0
for i in range(2,2000001):
	if prime_or_not[i]==1:
		ans+=i

print(ans)
