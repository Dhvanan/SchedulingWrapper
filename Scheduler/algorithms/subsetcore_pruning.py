import copy
import operator
import time
#import config
cores_allocation_ratio = 1

'''
*	Subset fit for RAM (Pruning host list)
*	author Dhvanan Shah
*	version 2.0
'''
#Global Variables
length_cores = {32: 1, 128: 3967, 64: 52, 256: 6673, 16: 4, 512: 1789}
start_index = {32: 4, 128: 57, 64: 5, 256: 4024, 16: 0, 512: 10697}
iter_count=0
iter_count_1=0

def write_to_file(hostlist,filename):
	with open(filename,'w') as f:
		for host in hostlist:
			host_id = host['host']
			cores = host['free_vcpus']
			f.write(str(host_id)+','+str(cores)+'\n')

def prune_hostlist(hosts,req):
	'''
	Prune the hostlist for more efficient computation
	'''
	total_cores = 0
	for r in req:
		total_cores += r['cores']
	request_min = min([request['cores'] for request in req])
	
	cores_list = [host['free_vcpus'] for host in hosts]
	hosts_max = max(cores_list)
	max_index = cores_list.index(max(cores_list))
	hosts_min = min(cores_list)
	min_index = cores_list.index(min(cores_list))
	cores_sorted_list = list(set(cores_list))
	cores_sorted_list.sort()

	print "\n"+"total_cores:"+str(total_cores)
	print "host_max:"+str(hosts_max)

	# Removing all hosts that cannot handle min request 
	if(request_min > hosts_min):
		for host in hosts:
			if host['free_vcpus'] < request_min:
				hosts.remove(host)			
	#print "Len of hosts after removing min: "+str(len(hosts))

	pruned_hostlist = []
	end_index = 0			

	global start_index
	# Removing all hosts more than required
	if(total_cores > hosts_max):
		print cores_sorted_list
		for cores_val in cores_sorted_list:
			if(cores_val>hosts_max):
				break
			print cores_val	
			add_index = min(int(float(total_cores)/cores_val),length_cores[cores_val]-1)
			end_index = start_index[cores_val] + add_index
			extend_list = hosts[start_index[cores_val]:end_index+1]
			pruned_hostlist.extend(extend_list)
	
	else:
		end_index = max_index													#Wrong ,  dont go to the max_index
		pruned_hostlist = hosts[:end_index+1]			
	print "Pruned Host List Length: "+str(len(pruned_hostlist))
	#print cores_list[:end_index+1]
	return pruned_hostlist

def subsetcore_pruning(hosts,req):
	'''
	input: 	hosts list with each host as a dictionary
			req dict: {vm-default:[{},{}],vm-custom:[{},{}]} 

	output:	VM:Host Mapping		
	'''

	mapping=[]	
	n = len(req['vm-default'])
	for host in hosts:
		host['free_vcpus'] = int(host['free_vcpus']/100 * cores_allocation_ratio)


	#Call Hosts Pruning here
	#pruned_host_list = prune_hostlist(hosts,req['vm-default'])
	pruned_host_list = hosts
	filename = '/home/dhvanan/IISc/WORK/BenchmarkingAlgorithms/mapping/Host_List/hosts_'+str(n)+'.csv'
	write_to_file(pruned_host_list,filename)

	print [host['free_vcpus'] for host in pruned_host_list]

	host_list ={}
	for host in pruned_host_list:
		host_list[host['host']] = host['free_vcpus']

	
	sorted_host_list = sorted(host_list.items(), key = operator.itemgetter(1))

	requests=[]
	i=0
	for vm_type in req:
		hosts_dict = {}
		req_list=[]
		for request in req[vm_type]:
			#print request
			name = request['name']
			cores_req = request['cores']
			requests.append(cores_req)
			req_list.append([name,cores_req])

		#print requests	
		global iter_count_1	
		for host in sorted_host_list:
			cap = host[1]
			
			w=list(range(len(req_list)))
			w.reverse()
			results={}
			weights=[]
			keep={}
			
			def sub(i,s):
				global iter_count
				iter_count+=1
				#print 'i:'+str(i)
				if(s<=0 and i<len(req_list)):
					results[req_list[i][0],s]=0
					keep[req_list[i][0],s]=0
					return results[req_list[i][0],s]
				if(i==len(req_list)):
					results[i,s]=0
					keep[i,s]=0
					return results[i,s]	
				if (req_list[i][0],s) in results: return results[req_list[i][0],s]

				else:
					if(s-req_list[i][1]>=0):
						val1=sub(i+1,s)
						val2=sub(i+1,s-req_list[i][1])+req_list[i][1]
						val=max(val1,val2)

						if(val==val1):
							keep[req_list[i][0],s]=0
						else:
							keep[req_list[i][0],s]=1	
					else:
						val=sub(i+1,s)
						keep[req_list[i][0],s]=0

					return val
			#print "REQ_LIST : "+str(req_list)
			#print "w:"+str(w)
			break_loop = False
			req_chosen = []
			for i in w:												# W is "requests"
				req_chosen.append(i)
				for j in range(0,cap+1):
					results[req_list[i][0],j]=sub(i,j)
					if(results[req_list[i][0],j] == cap):
						#print "Found the VM's for hosts : "+str(results[req_list[i][0],j])
						ans = results[req_list[i][0],j]
						break_loop = True
				if(break_loop == True):
					#print "ANS : "+str(ans)
					break
			
			iter_count_1 += len(w)*cap
			#print "iter_time : "+str(en_time - st_time)
			#print "iter_count : "+str(len(w)*cap)+'\n'
			
			req_chosen.sort()
			k=cap
			host_cores = []
			#print "KEEP : "+str(keep)
			for i in req_chosen:
				if(keep[req_list[i][0],k]==1):
					hosts_dict[req_list[i][0]]=host[0]
					host_cores.append(host[1])
					k=k-req_list[i][1]
					req_list[i][1]=0
				if(k==0):
					break

			req_list_dup = copy.deepcopy(req_list)
			
			for i in req_list_dup:
				if(i[1]==0):
					req_list.remove(i)		

			#print hosts_dict		
			#print "Requests selected: "+str(len(hosts_dict))
			if(len(hosts_dict) == n):
				break

		mapping.append(hosts_dict)
		print "iter_count :"+str(iter_count)
		print "iter_count_1 :"+str(iter_count_1)

	return mapping
	
