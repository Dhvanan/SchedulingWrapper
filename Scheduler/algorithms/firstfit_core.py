import sys
sys.path.append('/home/dhvanan/IISc/WORK/SchedulingWrapper')
import operator
#import config
ram_allocation_ratio = 1
#from hostManager.HostManager import update_host

flavors={'m1.tiny':[512,1,1],'m1.small':[2048,20,1],'m1.medium':[4096,40,2],'m1.large':[8192,80,4],'m1.xlarge':[16384,160,8],'custom_1':[256,1,1],'custom_2':[1024,1,1],'custom_3':[1024,1,2],'custom_4':[2048,1,2],'custom_5':[1024,20,3],'custom_6':[4096,1,1],'custom_7':[2048,1,1]}

def FirstFit_Core(hosts,req):
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
			core_req = request['cores']
			for host in hosts:
				host_cap = host['free_vcpus']/100
				if(host_cap>=core_req):
					host['free_vcpus']-=core_req*100
					mapping_dict[request['name']] = host['host']
					break
		mapping.append(mapping_dict)
	return mapping


#r = {"vm-default":[{"name" : "VM1","ram":1},{"name" : "VM2","ram":1},{"name" : "VM3","ram":1},{"name" : "VM4","ram":2},{"name" : "VM5","ram":4},{"name" : "VM6","ram":4},{"name" : "VM7","ram":1}]}
#h = [{'host':'host1','free_ram':6},{'host':'host2','free_ram':7}]
#res = FirstFit_Ram(h,r)
#print res