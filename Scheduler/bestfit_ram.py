import sys
sys.path.append('/home/dhvanan/IISc/WORK/SchedulingWrapper')
import operator
import config
ram_allocation_ratio = 1
from hostManager.HostManager import update_host


def BestFit_Ram(hosts,req):
	'''
	input:  hosts list with each host as a dictionary
                        req dict: {vm-default:[{},{}],vm-custom:[{},{}]}

        output: VM:Host Mapping
        '''
	print "In BESTFIT RAM"
	print "HOSTS : " + str(hosts)
	print "REQUESTS : " +str(req)
        mapping=[]
	host_list ={}
	hosts_dict={}
        for host in hosts:
                host_list[host['host']] = int(host['free_ram'] * ram_allocation_ratio)
		hosts_dict[host['host']] = host
	
	print "HostList : "+str(host_list)
	sorted_hostlist = sorted(host_list.items(), key = operator.itemgetter(1))
	instance_count=0
	for vm_type in req:
		mapping_dict = {}
		for request in req[vm_type]:
                        ram_req = config.flavors[request['flavor']][0]
			print "REQ : "+str(ram_req)
			for host in sorted_hostlist:
				print "host : " + str(host)
				print(host[1]>ram_req)
				if(host[1]>ram_req):
					host_list[host[0]]-=ram_req
					mapping_dict[instance_count] = host[0]
					break
			instance_count+=1
			sorted_hostlist = sorted(host_list.items(), key = operator.itemgetter(1))		
		mapping.append(mapping_dict)
	return mapping
