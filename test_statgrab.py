import statgrab as stg

    sg_get_cpu_percents() #Give information about CPU load in percents
    sg_get_cpu_stats()	#Same than cpu_percents but give also the timestamp
    sg_get_cpu_stats_diff() #Return the difference in values with the previous cpu_percents/stats
    sg_get_disk_io_stats() #Give in bytes input ouput of each disks
    sg_get_disk_io_stats_diff() #Give the difference with the previous io_stats
    sg_get_error()
    sg_get_error_arg()
    sg_get_error_errno()
    sg_get_fs_stats() #Return infos about filesystem (bugged), free_blocks, total ..
    sg_get_host_info() #Return basically the same than uname -a
    sg_get_load_stats() #Return the average since 1 minute, 5 minutes and 15 minutes
    sg_get_mem_stats() #Return total, free, cache and used of the RAM
    sg_get_network_iface_stats() #Retur network interfaces and theirs status
    sg_get_network_io_stats() #Return input ouput in bytes on each interfaces (and errors..)
    sg_get_network_io_stats_diff() #Return the difference with the last io_stats()
    sg_get_page_stats()
    sg_get_page_stats_diff()
    sg_get_process_count() #Return informations about processes
    sg_get_process_stats() #Return informations about all process
    sg_get_swap_stats() #Same as mem_stats but not with cache
    sg_get_user_stats() # ?

if not stg.sg_init():
  sys.exit(1)

res = stg.sg_get_cpu_percents()
#The problem is the object returned is a Result class you can loop trough items knowing
#in advance all the keys. ex:

for k in ('kernel','iowait','idle','swap','nice','user'): #time_taken ..
  print k,": ",res[k],"%"
'''
kernel :  0.531929373741 %
iowait :  0.00408129952848 %
idle :  97.5757064819 %
swap :  0.0 %
nice :  0.0 %
user :  1.8923625946 %
'''
  
#OR you can convert Result class to dictionnary
import ast
dic = ast.literal_eval(str(res))

for (k,v) in dic.items():
  print k,": ",v,"%"
  
  
for disk in stg.sg_get_disk_io_stats():
  print disk['disk_name'],"\tRead: ",disk['read_bytes']/1000,"KB\t\tWrite: ",disk['write_bytes']/1000,"KB"
'''
sda 	Read:  814150 KB		Write:  1347350 KB
sdb 	Read:  11636 KB		Write:  0 KB
'''

res = stg.sg_get_host_info()
for (k,v) in ast.literal_eval(str(res)).items():
  print k,": ",v
'''
uptime :  11135
os_name :  Linux
os_version :  #1 SMP Fri Apr 6 05:01:55 UTC 2012
hostname :  Cyborg
platform :  x86_64
os_release :  3.2.0-2-amd64
'''

print "Memory (RAM)"
res = stg.sg_get_mem_stats()
for (k,v) in ast.literal_eval(str(res)).items():
  print k, v / 1000000,"MB"
'''
total 8372 MB
cache 1769 MB
used 4549 MB
free 3822 MB
'''
#This is exactly the same with swap, and user but not with cache attribute

for iface in stg.sg_get_network_iface_stats():
  print iface['interface_name']+":", "up" if iface["up"] == 1 else "down"
'''
lo: up
wlan0: up
eth0: up
'''

for iface in stg.sg_get_network_io_stats():
  print iface['interface_name']+": Input:",iface['ipackets'] / 1000,'Kb\tOutput:',iface['opackets'] / 1000,"Kb"
'''
lo: Input: 0 Kb	Output: 0 Kb
wlan0: Input: 794 Kb	Output: 554 Kb
eth0: Input: 0 Kb	Output: 0 Kb
'''

res = stg.sg_get_process_count()
for (k,v) in ast.literal_eval(str(res)).items():
  print k,v
'''
zombie 0
running 2
total 175
stopped 1
sleeping 172
'''

res = stg.sg_get_process_stats()
print "Number Processes:",len(res)
print "CPU\tUID\tGID\tPID\tName"
for p in res:
  print round(p['cpu_percent'],2),"\t",p['uid'],"\t",p['gid'],'\t',p['pid'],'\t',p['process_name']
'''
CPU	UID	GID	PID	Name 
0.01 	0 	0 	1 	init
0.0 	0 	0 	2 	kthreadd
0.0 	0 	0 	3 	ksoftirqd/0
0.0 	0 	0 	6 	migration/0
0.0 	0 	0 	7 	watchdog/0
0.0 	0 	0 	8 	migration/1
...
'''