#!/usr/bin/python
import sys
import os
import socket
import json
import syslog
sys.stderr = sys.stdout
print "Content-Type: text/plain"
print

def pxe_abort():
  """Abort the PXE boot, continue with the next boot device in the BIOS boot order"""
  print "#!ipxe"
  print "exit"
  sys.exit(0)

try:
  # from the name, e.g. c1-3 take c1-3
  hostname = socket.gethostbyaddr(os.environ["REMOTE_ADDR"])[0].split(".")[0]

  try:
    os.remove("/var/www/provision/reinstall/" + hostname)
  except OSError as e:
    syslog.syslog(syslog.LOG_INFO, str(e))
    pxe_abort()

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

except Exception as e:
  syslog.syslog(syslog.LOG_ERR, str(e))
  pxe_abort()
