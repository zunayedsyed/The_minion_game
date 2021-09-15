def minion_game(string,list1,list2,vowel):
		for i in range(len(string)):
			if string[i] in vowel:
				for j in range(i+1,len(string)+1):
					list1.append(string[i:j])
				    
			else:
				for j in range(i+1,len(string)+1):
					list2.append(string[i:j])
		if len(list1)>len(list2):
			print("Kevin:",len(list1))
		elif len(list1)<len(list2):
			print("Stuart:",len(list2))
		else:
			print("Draw") 
string=input().upper()
list1=[] 
list2=[] 
vowel="AEIOU"  
minion_game(string,list1,list2,vowel)  