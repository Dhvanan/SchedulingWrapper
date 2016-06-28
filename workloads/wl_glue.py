import urllib2

proxy_handler = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_handler)

#data = '{"vm-default":[{"name" : "my-vm-small","description":"VM","image":"cirros image","flavor":"custom_1","instance_count":1,"host-affinity" : "packed"},{"name":"test2","description":"test instance","flavor":"m1.tiny","image":"cirros image","instance_count":1,"host-affinity":"packed"}]}'
#data = '{"vm-default":[{"name" : "VM1","description":"VM","image":"cirros image","flavor":"custom_4","instance_count":1,"host-affinity" : "packed"},{"name":"VM2","description":"test instance","flavor":"custom_2","image":"cirros image","instance_count":1,"host-affinity":"packed"},{"name":"VM3","description":"test instance","flavor":"custom_4","image":"cirros image","instance_count":1,"host-affinity":"packed"},{"name":"VM4","description":"test instance","flavor":"custom_5","image":"cirros image","instance_count":1,"host-affinity":"packed"}]}'
#data = '{"vm-default":[{"name" : "VM1","description":"VM","image":"cirros image","flavor":"custom_2","instance_count":1,"host-affinity" : "packed"},{"name":"VM2","description":"test instance","flavor":"m1.medium","image":"cirros image","instance_count":1,"host-affinity":"packed"},{"name":"VM3","description":"test instance","flavor":"m1.small","image":"cirros image","instance_count":1,"host-affinity":"packed"}]}'
data = '{"vm-default":[{"name" : "VM1","description":"VM","image":"cirros image","flavor":"custom_2","instance_count":1,"host-affinity" : "packed"},{"name":"VM2","description":"test instance","flavor":"custom_2","image":"cirros image","instance_count":1,"host-affinity":"packed"},{"name":"VM3","description":"test instance","flavor":"custom_2","image":"cirros image","instance_count":1,"host-affinity":"packed"},{"name":"VM4","description":"test instance","flavor":"custom_7","image":"cirros image","instance_count":1,"host-affinity":"packed"},{"name":"VM5","description":"test instance","flavor":"custom_6","image":"cirros image","instance_count":1,"host-affinity":"packed"},{"name":"VM6","description":"test instance","flavor":"custom_6","image":"cirros image","instance_count":1,"host-affinity":"packed"},{"name":"VM7","description":"test instance","flavor":"custom_2","image":"cirros image","instance_count":1,"host-affinity":"packed"}]}'
url="http://localhost:5001/todo/api/v1.0/tasks"
req = urllib2.Request(url,data,{'Content-Type': 'application/json'})
	
res = opener.open(req)
for i in res:
	print i
