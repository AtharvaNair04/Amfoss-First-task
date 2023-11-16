file=open("example.txt","r")
read=file.read().split()
print(read)
for i in range(len(read)):
	if read[i].startswith("ADJECTIVE"):
		print("Enter an adjective:")
		A=input()
		read[i]=A
	elif read[i].startswith("NOUN"):
		print("Enter a noun:")
		N=input()
		read[i]=N
	elif read[i].startswith("ADVERB"):
		print("Enter a verb:")
		Av=input()
		read[i]=Av
	elif read[i].startswith("VERB"):
		print("Enter a verb:")
		V=input()
		read[i]=V
f=open("example.txt","w")
for i in read:
	f.write(f"{i} ")
f.close()
