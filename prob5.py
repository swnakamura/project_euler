ans=1

def gcd(a,b):#aとbの最大公約数を算出する関数
	if a<b:
		a,b=b,a
	while(b!=0):
		a,b=b,a%b
	
	return a

for i in range(1,21):#iは1から20まで変わりながら実行されることに注意
	ans*=i/gcd(i,ans)

print(ans)
