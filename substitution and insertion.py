import string
word='and'
no_of_substitution=1
s=list(string.ascii_lowercase)
s1=[i for i in s if i!=word[0]]
def sub(s1,w):
	substitute=[]
	s2=[i for i in s if i!=word[w]]
	for i in s2:
		for j in s1:
			substitute.append(j+i)
	return substitute
	
for i in range(no_of_substitution-1):
	s1=sub(s1,w=i+1)

i1=[i for i in s]
no_of_insertion=1
def inserting(i1):
	inserted=[]
	for i in i1:
		for j in list(s):
			inserted.append(i+j)
	return inserted

for j in range(no_of_insertion-1):
	i1=inserting(i1)

x=[]
y=[]
for i in s1:
	for j in i1:
		x.append(i+j)

for i in x:
	y.append(i+word[no_of_substitution:])
print(y)
