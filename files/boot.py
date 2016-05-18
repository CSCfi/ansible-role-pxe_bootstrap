#!/usr/bin/python
import sys
import os
import socket
import json
sys.stderr = sys.stdout
print "Content-Type: text/plain"
print

try:
  # from the name, e.g. c1-3 take c1-3
  hostname = socket.gethostbyaddr(os.environ["REMOTE_ADDR"])[0].split(".")[0]

  os.remove("/var/www/provision/reinstall/" + hostname)
  with open('/var/www/provision/nodes/pxe_nodes.json') as f:
    j = json.load(f)
  nodesettings = j[hostname]

  serialport = 'ttyS0'
  if 'serialport' in nodesettings:
    serialport = nodesettings['serialport']

  print "#!ipxe"
  print "kernel http://" + nodesettings["kickstart_server_ip"] + "/ks/vmlinuz ks=http://" + nodesettings["kickstart_server_ip"] + "/ks/" + nodesettings["kickstart_profile"] + " edd=off ksdevice=bootif kssendmac console=" + serialport + ",115200 console=tty0 initrd=initrd.img"
  print "initrd http://" + nodesettings["kickstart_server_ip"] + "/ks/initrd.img"
  print "boot"

except:
   print "#!ipxe"
   print "exit"
