def BestFit_Core(hosts,req):

	min_core = hosts[0]['free_vcpus']
	selected_host = filtered_hosts[0]
	
	for host in filtered_hosts[1:]:
		
		if(host['free_vcpus'] < min_core):
			min_core = host['free_vcpus']
			selected_host = host

	return selected_host
