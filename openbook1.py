def list_ipname_ip(address,netmask,name):
	d={}
	d[name]=(address,netmask)
	return d

def interchanging_mask(d):
	for i in range(len(d)):
		val=d[i][0]
		val1=d[i][1]
		if val == 172 or val== 192:
			val.replace(val,"10")
			val1.replace(val1,"255.0.0.0")
	return d


l=[]
fout=open("running-config.cfg")
for interface in fout:
	l.append(interface.strip().split(" "))
	#print(l)
for i in range(len(l)):
	if type(l[i]) ==list:
		if l[i][0]=="nameif":
			name=l[i][1]
		elif l[i][0]=="ip":
			add=l[i][2]
			netmask=l[i][3]
			d=list_ipname_ip(add,netmask,name)
			print(interchanging_mask(d))
