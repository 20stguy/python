import psutil
import os


print("psutil.cpu_times", psutil.cpu_times()) # cpu정보는 항상 커진다. 시가을 돌릴 수 없기 때문
print("psutil.cpu_percent", psutil.cpu_percent(interval=1, percpu=True))
print("psutil.cpu_times_percent", psutil.cpu_times_percent())
print("psutil.cpu_times_percent", psutil.cpu_times_percent(interval=1, percpu=True))
print("psutil.cpu_count", psutil.cpu_count(logical=True)) # cpu코어 개수(logical = Hyper Threading)
print("psutil.cpu_count", psutil.cpu_count(logical=False))
print("psutil.stats", psutil.cpu_count())
print("psutil.stats", psutil.cpu_stats())
print("psutil.cpu_freq", psutil.cpu_freq())

# print("psutil.getloadavg", psutil.getloadavg())
# print("psutil.percentage representation", [x/psutil.cpu_count() * 100 for x in psutil.getloadavg()])

print("psutil.virtual_memory", psutil.virtual_memory()) # total physical memory
print("swap_memory", psutil.swap_memory())

print("disk_partitions", psutil.disk_partitions())
print("disk_usage", psutil.disk_usage("/"))
print("disk_usage with os", psutil.disk_usage(os.getcwd()))
print("disk_usage with os percent", psutil.disk_usage(os.getcwd())[3])
# print("disk_usage with os.fsencode", psutil.disk_usage(os.fsencode("ps_utils.py")))

# cpu %
# print("psutil.cpu_times_percent", psutil.cpu_times_percent())

# RAM %
# print("psutil.virtual_memory", psutil.virtual_memory()) # total physical memory

# Storage %
#
# Temperature
print("sensors_temperatures", psutil.sensors_temperatures())
