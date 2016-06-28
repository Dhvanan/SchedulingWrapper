import sys
sys.path.append('/root/SchedulingWrapper')
import MySQLdb
import config
from HostManager.HostManager import get_all_hosts

class Scheduler():

	def __init__(self):
		self.hosts=get_all_hosts()
		pass

	def schedule(self,req,algo_chosen):
		
		'''
		selected_hosts = []
		
		for vm_type in req:
			hosts={}
                	instance_count=0
			for request in vm_type:
				name = request['name']
				chosen_host = self.select_destinations(request,algo_chosen)
				#Add extra capability to vm request and write a filter to remove all other hosts except for the chosen one.
				hosts[instance_count]=chosen_host['host']
				instance_count+=1
			selected_hosts.append(hosts)
		'''
		algorithm = config.algos[algo_chosen]
                chosen_hosts = algorithm(self.hosts,req)
		
		print " SELECTED HOSTS : " + str(chosen_hosts)
		return chosen_hosts
		
					
	def select_destinations(self,req,algo_chosen):

		#flavor = req['flavor']
		#instance_count = req['instance_count']
		"""
			format = host
					 running vms
					 total vcpus
					 total memory
					 total disk space
					 vcpus used
					 memory used
					 disk space used
					 memory free
					 disk free
		"""          
		
		
		filtered_hosts = self.get_filtered_hosts(self.hosts,req)
		if not filtered_hosts:
			print('No Host Passed')
			exit()
		
		algorithm = config.algos[algo_chosen]
		chosen_hosts = algorithm(self.hosts,req)
		
		return chosen_hosts

	def get_filtered_hosts(self,hosts,req):


		req_cpu = config.flavors[req['flavor']][2]
		req_ram = config.flavors[req['flavor']][0]

		host_passes=[]	
		for host in hosts:
			free_vcpus = host['free_vcpus']
			free_ram = host['free_ram']

			if(req_cpu <= free_vcpus and req_ram <=	 free_ram):
				print(host)
				host_passes.append(host)

		return host_passes       			
