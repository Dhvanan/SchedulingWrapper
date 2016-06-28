#import config
ram_allocation_ratio = 1

def subsetram(hosts,req):
	'''
	input: 	hosts list with each host as a dictionary
			req dict: {vm-default:[{},{}],vm-custom:[{},{}]} 

	output:	VM:Host Mapping		
	'''
	print "Hosts : "+ str(hosts)	
	mapping=[]	
	print("In Subset Ram")
	n=0
	for vm_type in req:
		print vm_type
		for request in req[vm_type]:
			n+=1	
	print n


	hosts = sorted(hosts,key=lambda k: k['free_vcpus'])
	host_list ={}
	for host in hosts:
		host_list[host['host']] = int(host['free_ram'] * ram_allocation_ratio)

	requests=[]
	i=0
	for vm_type in req:
		hosts_dict = {}
		for request in req[vm_type]:
			#ram_req = config.flavors[request['flavor']][0]
			ram_req = request['ram']
			#core_req = flavors[request['flavor']][2]
			requests.append(ram_req)
		
		#requests = [2,1,1,1,2]
		#n=5
		print requests
		
		for host in host_list:
			cap = host_list[host]
			print(host,' Capacity:',cap)

			w=list(range(0,n+1))
			w.reverse()

			#print "w:" + str(w)


			results={}
			weights=[]
			keep={}
			def sub(i,s):
				if (i,s) in results: return results[i,s]

				if(s<=0 or i==n):
					results[i,s]=0
					keep[i,s]=0
					return results[i,s]
				else:
					if(s-requests[i]>=0):
						val1=sub(i+1,s)
						val2=sub(i+1,s-requests[i])+requests[i]
						#print "i:"+str(i)+"	s:"+str(s)
						#print val1,val2
						val=max(val1,val2)

						if(val==sub(i+1,s)):
							keep[i,s]=0
						else:
							keep[i,s]=1	
					else:
						val=sub(i+1,s)
						keep[i,j]=0

					return val



			for i in w:
				for j in range(0,cap+1):

					results[i,j]=sub(i,j)
					#print('i:',i,'j:',j,'results:',results[i,j])
			ans=results[0,cap]
			print(ans)

			k=cap
			for i in range(0,n+1):
				if(keep[i,k]==1):
					hosts_dict[i]=host
					print requests[i]
					#mapping.append([req[vm_type][i],host])
					k=k-requests[i]
					requests[i]=0
		mapping.append(hosts_dict)
	return mapping			
