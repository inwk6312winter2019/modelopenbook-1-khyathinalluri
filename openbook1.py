def list_ipname_ip(interface,name):
	d={}
	ipaddress,netmask=interface.split(" ")
	d[name]=(ipaddress,netmask)
	print(d)

fout=open("running-config.cfg")
for interface in fout:
	if interface!= "!":
		
	else:
		continue 


