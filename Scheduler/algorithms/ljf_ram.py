def ljf_ram(hosts,req):
	'''
	input: 	hosts list with each host as a dictionary
			req dict: {vm-default:[{},{}],vm-custom:[{},{}]} 

	output:	VM:Host Mapping		
	'''
	print "IN LJF"	
	hostlist = sorted(hosts, key=lambda k: k['free_ram'])
	mapping = []
	#print hostlist
	for vm_type in req:
		requests = sorted(req[vm_type], key=lambda k: k['ram'],reverse = True)
		#print requests
		mapping_dict = {}
		for request in requests:
			ram_req = request['ram']
			
			for host in hostlist:
				host_ram = host['free_ram']

				if(ram_req<=host_ram):
					mapping_dict[request['name']] = host['host']
					host['free_ram']-=ram_req
					break
			hostlist = sorted(hosts, key=lambda k: k['free_ram'])		
		mapping.append(mapping_dict)
	'''	for d in mapping:
		for i in d:
			f.write(str(i)+','+str(d[i])+'\n')	
	'''
	return mapping


#h = [{'host':'host1','vcpus':12,'memory_mb':4096,'local_gb':500,'free_vcpus':12,'memory_mb_used':0,'free_ram':4096},{'host':'host2','vcpus':12,'memory_mb':4096,'local_gb':500,'free_vcpus':12,'memory_mb_used':0,'free_ram':4096}]
#r = {"vm-default":[{"name" : "VM1","description":"VM","image":"cirros image","ram":1024,"cores":2,"instance_count":1,"host-affinity" : "packed"},{"name" : "VM2","description":"VM","image":"cirros image","ram":1024,"cores":2,"instance_count":1,"host-affinity" : "packed"}]}
#r = {"vm-default":[{"name" : "VM1","ram":1024},{"name" : "VM2","ram":1024},{"name" : "VM1","ram":2048},{"name" : "VM2","ram":1024},{"name" : "VM3","ram":1024},{"name" : "VM4","ram":2048},{"name" : "VM5","ram":1024},{"name" : "VM6","ram":1024},{"name" : "VM7","ram":4096},{"name" : "VM8","ram":2048}]}
#h = [{'host':'host1','free_ram':10000},{'host':'host2','free_ram':10000},{'host':'host3','free_ram':10000},{'host':'host4','free_ram':10000},{'host':'host5','free_ram':5000},{'host':'host6','free_ram':10000}]
#r= r = {"vm-default":[{"name" : "VM1","ram":1},{"name" : "VM2","ram":1},{"name" : "VM3","ram":1},{"name" : "VM4","ram":2},{"name" : "VM5","ram":4},{"name" : "VM6","ram":4},{"name" : "VM7","ram":1}]}
#h = [{'host':'host1','free_ram':6},{'host':'host2','free_ram':7}]
#res = ljf_ram(h,r)
#print res
