import string
word='and'
n=1
s=list(string.ascii_lowercase)
s1=[i for i in s if i!=word[0]]
def sub(s1,w):
	substitute=[]
	s2=[i for i in s if i!=word[w]]
	for i in s2:
		for j in s1:
			substitute.append(j+i)
	return substitute
s3=[]	
for i in range(n-1):
	s1=sub(s1,w=i+1)
for i in s1:
	s3.append(i+word[n:])
print(s3)

