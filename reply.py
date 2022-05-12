import dataset as ds

def ans(strg):
	l=strg.split(' ')
	for i in l:
		if i in ds.dataset:
			reply=ds.dataset[i]
			break
		else:
			reply="not getting..."
	return reply

"""
[+] For manual use, to check implimentation of function:
strg=input("enter question: ")
reply=ans(strg)
print("\nQuestion Asked: ",strg)
print("response: ",reply)
"""