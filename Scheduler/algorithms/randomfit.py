import sys
sys.path.append('/home/dhvanan/IISc/WORK/SchedulingWrapper')
import random
#from hostManager.hostManager import update_host	

def RandomFit(hosts,req):
	print "In RANDOM FIT"

	selected_hosts = []
	for vm_type in req:
		hosts_dict = {}
		instance_count=0
		for request in req[vm_type]:
			print("In randomfit!!"+str(hosts))
			chosen_host = random.choice(hosts[0:len(hosts)])	
			
			chosen_host = update_host(chosen_host,request)
			hosts_dict[instance_count]=chosen_host['host']
			instance_count+=1
			print(hosts)
		selected_hosts.append(hosts_dict)
	return selected_hosts
