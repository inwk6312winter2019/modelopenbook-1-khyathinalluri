def list_ipname_ip(address,netmask,name):
	d={}
	d[name]=(address,netmask)
	return d

l=[]
name=[]
add=[]
netmask=[]
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
			print(list_ipname_ip(add,netmask,name))
