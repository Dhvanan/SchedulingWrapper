import sys
sys.path.append('/home/dhvanan/IISc/WORK/SchedulingWrapper')
import MySQLdb
import config

def get_all_hosts():
	db = MySQLdb.connect("localhost","admin","admin","nova")

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# execute SQL query using execute() method.
	cursor.execute("select host,running_vms,vcpus,memory_mb,local_gb,vcpus_used,memory_mb_used,local_gb_used,free_ram_mb,free_disk_gb from compute_nodes;")

	# Fetch a single row using fetchone() method.
	data = cursor.fetchone()

	compute_nodes = []
	while(data):
		compute_node = {'host':data[0],'running_vms':data[1],'vcpus':data[2],'memory_mb':data[3],'local_gb':data[4],'vcpus_used':data[5],'free_vcpus':data[2]-data[5],'memory_mb_used':data[6],'local_gb_used':data[7],'free_ram':data[8],'free_disk_gb':data[9]}
		compute_nodes.append(compute_node)
		data = cursor.fetchone()

	# disconnect from server
	db.close()

	return compute_nodes

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