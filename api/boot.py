import sys
sys.path.append('/root/SchedulingWrapper')
from spawn_instance import Spawn 
from Scheduler.scheduler import Scheduler

'''
Request Format
instance-name , image , flavor , instance_count
'''

print sys.argv
req={'name':sys.argv[1],'image':'"'+sys.argv[2]+'"','vcpu':1,'ram':512,'flavor':sys.argv[3],'count':int(sys.argv[4])}
algo='bestfit_core'

s = Scheduler()
chosen_host = s.schedule(req,algo)
print chosen_host['host']
Spawn(req,chosen_host['host'])
