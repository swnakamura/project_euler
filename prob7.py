#10001番目の素数は100万以下だろうと予想
#エラトステネスの篩を用いて解く
n=1000000

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
	if(num==10001):
		print(i)
		break




