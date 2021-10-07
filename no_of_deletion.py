word='abd'
no_of_word=len(word)
d=[]# Empty list to store deleted words
n=2#number of deletion
if(n<no_of_word):
	for j in range(no_of_word):#loop around all the letters
		x=list(word)#list of letters in the word
		if(j<no_of_word-n):#to prevent from index out of boundry
			for i in range(n):#loops according to no of deletions
				del x[j+1:j+2]#deletes from 1th index
		elif(j==no_of_word-n):#to operate on first and last index
			for i in reversed(range(n)):
				del x[-i]#deletes first and last element
		elif(j>no_of_word-n):#operates on remaining letters 
			for i in range(n):
				del x[-j:-j+1]
		d.append(x)
	print(d)
	

