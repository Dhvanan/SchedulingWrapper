def ljf_core(hosts,req):
	'''
	input: 	hosts list with each host as a dictionary
			req dict: {vm-default:[{},{}],vm-custom:[{},{}]} 

	output:	VM:Host Mapping		
	'''
	#Sort Host Ascending (Best Fit - Most Used Host)
	for host in hosts:
		host['free_vcpus'] = host['free_vcpus']/100
	hostlist = sorted(hosts, key=lambda k: k['free_vcpus'])

	mapping = []
	for vm_type in req:

		#Sort Requests desc (Largest Job First)
		requests = sorted(req[vm_type], key=lambda k: k['cores'],reverse = True)
		
		mapping_dict = {}
		for request in requests:
			cores_req = request['cores']
			for host in hostlist:
				host_cores = host['free_vcpus']

				if(cores_req<=host_cores):
					mapping_dict[request['name']] = host['host']
					host['free_vcpus']-=cores_req
					break
			hostlist = sorted(hosts, key=lambda k: k['free_vcpus'])		
		mapping.append(mapping_dict)
	
	return mapping


#h = [{'host':'host1','vcpus':12,'memory_mb':4096,'local_gb':500,'free_vcpus':12,'memory_mb_used':0,'free_vcpus':4096},{'host':'host2','vcpus':12,'memory_mb':4096,'local_gb':500,'free_vcpus':12,'memory_mb_used':0,'free_vcpus':4096}]
#r = {"vm-default":[{"name" : "VM1","description":"VM","image":"cirros image","cores":1024,"cores":2,"instance_count":1,"host-affinity" : "packed"},{"name" : "VM2","description":"VM","image":"cirros image","cores":1024,"cores":2,"instance_count":1,"host-affinity" : "packed"}]}
#r = {"vm-default":[{"name" : "VM1","cores":1024},{"name" : "VM2","cores":1024},{"name" : "VM1","cores":2048},{"name" : "VM2","cores":1024},{"name" : "VM3","cores":1024},{"name" : "VM4","cores":2048},{"name" : "VM5","cores":1024},{"name" : "VM6","cores":1024},{"name" : "VM7","cores":4096},{"name" : "VM8","cores":2048}]}
#h = [{'host':'host1','free_vcpus':10000},{'host':'host2','free_vcpus':10000},{'host':'host3','free_vcpus':10000},{'host':'host4','free_vcpus':10000},{'host':'host5','free_vcpus':5000},{'host':'host6','free_vcpus':10000}]
#r= r = {"vm-default":[{"name" : "VM1","cores":1},{"name" : "VM2","cores":1},{"name" : "VM3","cores":1},{"name" : "VM4","cores":2},{"name" : "VM5","cores":4},{"name" : "VM6","cores":4},{"name" : "VM7","cores":1}]}
#h = [{'host':'host1','free_vcpus':6},{'host':'host2','free_vcpus':7}]
#res = ljf_cores(h,r)
#print res
