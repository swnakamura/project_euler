ans=0

for i in range(1001):
	if i%3 == 0:
		ans+=i
	elif i%5==0:
		ans+=i

print(ans)
