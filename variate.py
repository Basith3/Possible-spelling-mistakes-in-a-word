import string
def variate(word,no_of_insertion,no_of_deletion,no_of_substitution):
	#insertion
	s=string.ascii_lowercase
	i1=[i for i in s]
	def inserting(i1):
		inserted=[]
		for i in i1:
			for j in list(s):
				inserted.append(i+j)
		return inserted
	i2=[]
	for j in range(no_of_insertion-1):
		i1=inserting(i1)
	for i in i1:
		i2.append(i+word)
	print(i2)
	
	#deletion
	no_of_word=len(word)
	d=[]
	if(no_of_deletion<no_of_word):
		for j in range(no_of_word):
			x=list(word)
			if(j<no_of_word-no_of_deletion):
				for i in range(no_of_deletion):
					del x[j+1:j+2]
			elif(j==no_of_word-no_of_deletion):
				for i in reversed(range(no_of_deletion)):
					del x[-i]
			elif(j>no_of_word-no_of_deletion): 
				for i in range(no_of_deletion):
					del x[-j:-j+1]
			rst=''
			for i in x:
				rst+=i
			d.append(rst)
		print(d)
	
	#substitution
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
	for i in range(no_of_substitution-1):
		s1=sub(s1,w=i+1)
	for i in s1:
		s3.append(i+word[no_of_substitution:])
	print(s3)
	
	#subtitution and insertion
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

variate('and',no_of_insertion=1,no_of_deletion=1,no_of_substitution=1)
	
	