import string
number_of_insertions=1
s=string.ascii_lowercase
word='and'
i1=[i for i in s]# all letters from a-z
n=number_of_insertions
def inserting(i1):#function to find possibilities of words to be added
	inserted=[]
	for i in i1:# loop to add a-z for every letter
		for j in list(s):#loop to add a-z
			inserted.append(i+j)
	return inserted
i2=[]#to store all the possible words
for j in range(n-1):#loop over the function depending  upon the number of insertions
	i1=inserting(i1)
for i in i1:#adding the word at end of every possible words found
	i2.append(i+word)
print(i2)
