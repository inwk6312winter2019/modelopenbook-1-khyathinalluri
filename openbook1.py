def list_ipname_ip(address,netmask,name):
	d={}
	d[name]=(address,netmask)
	return d

l=[]
fout=open("running-config.cfg")
for interface in fout:
	l.append(interface.split())
	#print(l)
for i in range(len(l)):
	if l[i] =="nameif":
		name=l[i+2]
	elif l[i] == "ip":
		address=l[i+3]
		netwmask=l[i++5]
		print(list_ipname_ip(address,netmask,name)) 
	
