import sys
sys.path.append('/home/dhvanan/IISc/WORK/SchedulingWrapper')

def update_host(host,req):
	'''Updating the state of the host'''
	print "UPDATE-HOST"
	print
	req_cpu = config.flavors[req['flavor']][2]
        req_ram = config.flavors[req['flavor']][0]

	host['running_vms']+=1
	host['memory_mb_used']+= req_ram
	#print str(host['vcpus_used']) + '  ' +str(req_cpu)
        host['vcpus_used']+= req_cpu
	host['free_ram']-= req_ram
	host['free_vcpus']-= req_cpu
	print str(host)
	
	return host