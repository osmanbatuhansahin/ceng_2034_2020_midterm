import os
import requests
import threading
import platform

b = os.getpid()
print("Process ID is: ", b)

d = os.getloadavg()
c = platform.system()
print("running os is: ", c)
if (c == "Linux"):
	print("loadavg values are: ", d)
else:
	print("running os is not linux you can not print loadavg")

a = os.cpu_count()
print("Cpu core count value is: ", a)

liste = list(os.getloadavg())

print("5 minute loadavg is ", liste[2])

if (a - liste[1] < 1):
	exit()
else:
	print("5 minute loadavg is not near to cpu core count value")


def url_define(url_list):

	url = requests.get(url_list)
	url.status_code
	
	print("Url status code: ", url.status_code)
	print("url is: ", url_list) 
	if (url.status_code < 300):
		print("correct")
	else:
		print("incorrect")

arr = ["https://api.github.com", "http://bilgisayar.mu.edu.tr/", "https://www.python.org/", "http://akrepnalan.com/ceng2034", "https://github.com/caesarsalad/wow​"]


thread1 = threading.Thread(target=url_define,args=(arr[0],))
thread2 = threading.Thread(target=url_define,args=(arr[1],))
thread3 = threading.Thread(target=url_define,args=(arr[2],))
thread4 = threading.Thread(target=url_define,args=(arr[3],))
thread5 = threading.Thread(target=url_define,args=(arr[4],))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()


























