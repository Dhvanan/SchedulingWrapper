import sys
sys.path.append('/home/dhvanan/IISc/WORK/SchedulingWrapper')
import operator
import random
ram_allocation_ratio = 1


def randomfit_ram(hosts,req):
	'''
	input:  hosts list with each host as a dictionary
                        req dict: {vm-default:[{},{}],vm-custom:[{},{}]}

	output: VM:Host Mapping
	'''
	mapping=[]
	host_list ={}
	hosts_dict={}


	instance_count=0
	for vm_type in req:
		mapping_dict = {}
		for request in req[vm_type]:
			ram_req = request['ram']
			host = hosts[random.randint(0,len(hosts)-1)]
			if(host['free_ram']>=ram_req):
				host['free_ram']-=ram_req
				mapping_dict[request['name']] = host['host']
		mapping.append(mapping_dict)
	return mapping


#r = {"vm-default":[{"name" : "VM1","ram":1},{"name" : "VM2","ram":1},{"name" : "VM3","ram":1},{"name" : "VM4","ram":2},{"name" : "VM5","ram":4},{"name" : "VM6","ram":4},{"name" : "VM7","ram":1}]}
#h = [{'host':'host1','free_ram':6},{'host':'host2','free_ram':7}]
#res = FirstFit_Ram(h,r)
#print res
