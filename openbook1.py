def list_ipname_ip(address,netmask,name):
	d={}
	d[name]=(address,netmask)
	return d

def interchanging_mask(d):
		res={}
		a=list(d.values())
		k=list(d.keys())
		val=str(a[0][0])
		#print(val)
		val1=a[0][1]
		#print(val1)
		val=val.split(".")
		print(val)
		if val[0] == "172" or val[0] == "192":
				val[0]=10
				val1="255.0.0.0"
				res[k[0]]=(val,val1)
		return res


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
