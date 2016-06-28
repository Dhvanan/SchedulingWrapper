import os

def Spawn(req_list,host_list):
	i=0
	print "IN SPAWN"
	print req_list
	print "HOST LIST: "+str(host_list)
	for vm_type in req_list:
		j=0
		print vm_type
		for request in req_list[vm_type]:
			print "In request"
			print request
			print "host list[i]: "+str(host_list[i])+"\tj: "+str(j)	
			if(j in host_list[i]):
				instance_name = request['name']+'_'+host_list[i][j]
				flavor = request['flavor']
				image = request['image']

				print 'nova boot --image '+'"'+image+'"'+' --flavor '+flavor+' --nic net-id=6e0c41ed-1745-42ba-95ef-f1fbbd4bff2b '+instance_name	
				os.system('nova boot --image '+'"'+image+'"'+' --flavor '+flavor+' --nic net-id=6e0c41ed-1745-42ba-95ef-f1fbbd4bff2b '+instance_name)
			j+=1
		i+=1
	
