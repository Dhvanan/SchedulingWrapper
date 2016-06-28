import sys
sys.path.append('/home/dhvanan/IISc/WORK/SchedulingWrapper')
from Scheduler.Algorithms import *
flavors={'m1.tiny':[512,1,1],'m1.small':[2048,20,1],'m1.medium':[4096,40,2],'m1.large':[8192,80,4],'m1.xlarge':[16384,160,8],'custom_1':[256,1,1],'custom_2':[1024,1,1],'custom_3':[1024,1,2],'custom_4':[2048,1,2],'custom_5':[1024,20,3],'custom_6':[4096,1,1],'custom_7':[2048,1,1]}
#algos = {'randomfit':randomfit.RandomFit,'bestfit_core':bestfit_core.BestFit_Core,'bestfit_ram':bestfit_ram.BestFit_Ram,'subsetcore':subsetcore.subsetcore,'subsetram':subsetram.subsetram}
algos = {'randomfit':randomfit.RandomFit,'bestfit_core':bestfit_core.BestFit_Core}