Cloud Scheduling Algorithms for Big Data Workloads

Code:
Scheduling Wrapper

To start the api, go to SchedulingWrapper/api and run the api_interface.py, this will start the API service to listen for any workload submission.

To submit a workload, go to SchedulingWrapper/workloads and run wl_glue.py, this will submit the workload to the API that will then schedule and submit it to OpenStack and CloudSim.

To delete all the created VM's, run delete.py in SchedulingWrapper/workloads. 