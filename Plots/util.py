import matplotlib.pyplot as plt

files = ["/home/dhvanan/IISc/WORK/SchedulingWrapper/Plots/LJF/Requests-50k/hostTotalUtil.csv","/home/dhvanan/IISc/WORK/SchedulingWrapper/Plots/Best Fit/Requests-50k/hostTotalUtil-BestFit.csv","/home/dhvanan/IISc/WORK/SchedulingWrapper/Plots/Balanced Fit/Requests-50k/hostTotalUtil.csv"]

for i in files:
	f = open(i,"r")

	data = f.read()
	data=data.strip().split('\n')
	clock=[]
	ram=[]
	core=[]
	machines = []
	for i in range(len(data)):
		stat=data[i].split(',')
		
		clock.append(stat[0])
		machines.append(int(stat[1]))	

		ram.append(float(stat[2])*100)
		core.append(float(stat[3])*100)

	print()	
	print "Avg: "+str(sum(machines[61:6001])/len(machines[61:6001]))
	print "Max: "+str((max(machines)))
	#plt.plot(clock,machines)
	#plt.show()

	plt.xlim(0, 20000)
	plt.plot(clock,core,clock,ram)
	plt.show()


