from subsetram_pruning import subsetram_pruning

import math
import operator
import ast
import json
def scheduler_glue(h,r):

	#print "In Scheduler scheduler_glue"
	r = r.replace('\'','"')
	h = h.replace('\'','"')
	
	requests = json.loads(r)
	#requests = ast.literal_eval(r)

	#requests = r.replace('u','')
	#print type(requests)
	
	h = json.loads(h)
	#h = ast.literal_eval(h)
	#hosts = h['hosts']
	hosts = h

	#print 'requests: '+str(requests)
	#print 'hosts:' + str(hosts)
	h1 = str(h)
	h1 = h1.replace('u','')


	#mapping = BestFit_Ram(hosts,requests)
	mapping = subsetram_pruning(hosts,requests)
	#mapping = ljf_ram(hosts,requests)
	#mapping = FirstFit_Ram(hosts,requests)
	print mapping	
	return str(mapping[0])

#print json_obj('{"q":1}')
