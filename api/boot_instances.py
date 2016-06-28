
import sys
import os
sys.path.append('/root/SchedulingWrapper')
from spawn_instance import Spawn
from Scheduler.scheduler import Scheduler

def boot(requests):
	#os.system('nova boot --image "cirros image" --flavor m1.tiny --nic net-id=6e0c41ed-1745-42ba-95ef-f1fbbd4bff2b test')
	
	request_list=requests
	#for i in requests:
		#request_list.append(requests[i])				#assuming only the vm-default for now

		
	#Request Format
	#instance-name , image , flavor , instance_count
	#Image not in the schema (add IT!)
	
	
	algo='subsetram'
	#algo = 'bestfit_ram'
	s = Scheduler()
	#for vm_type in request_list:
		#for request in vm_type:
	selected_hosts = s.schedule(request_list,algo)
	#print chosen_host['host']
	print "Selected HOSTS: "+str(selected_hosts)
	Spawn(request_list,selected_hosts)
	
