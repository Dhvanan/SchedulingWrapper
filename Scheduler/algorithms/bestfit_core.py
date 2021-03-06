import sys
sys.path.append('/home/dhvanan/IISc/WORK/SchedulingWrapper')
import operator
#import config
cores_allocation_ratio = 1
#from hostManager.HostManager import update_host

flavors={'m1.tiny':[512,1,1],'m1.small':[2048,20,1],'m1.medium':[4096,40,2],'m1.large':[8192,80,4],'m1.xlarge':[16384,160,8],'custom_1':[256,1,1],'custom_2':[1024,1,1],'custom_3':[1024,1,2],'custom_4':[2048,1,2],'custom_5':[1024,20,3],'custom_6':[4096,1,1],'custom_7':[2048,1,1]}

def bestfit_core(hosts,req):
	'''
	input:  hosts list with each host as a dictionary
                        req dict: {vm-default:[{},{}],vm-custom:[{},{}]}

	output: VM:Host Mapping
	'''
	
	mapping1=[]
	mapping=[]
	host_list =[]
	hosts_dict={}
	cnt=0
	cores_list = []
	for host in hosts:
		host_list.append([host['host'],host['free_vcpus']/100 * cores_allocation_ratio])
	host_list.sort(key=lambda x:x[1])
		#cores_list.append(host['free_vcpus'])
		#hosts_dict[host['host']] = host
	#sorted_hostlist = sorted(host_list.items(), key = operator.itemgetter(1))

	instance_count=0
	for vm_type in req:
		mapping_dict = {}
		for request in req[vm_type]:
			cores_req = request['cores']
			for host in host_list:
				if(host[1]>=cores_req):
					host[1]-=cores_req
					mapping_dict[request['name']] = host[0]
					cores_list.append(host[1])
					break
			instance_count+=1
			#sorted_hostlist = sorted(host_list.items(), key = operator.itemgetter(1))		
		mapping.append(mapping_dict)
	return mapping