#import ftprun
#import ftp
import test
def cam_name(cam_name):
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
 
  return cpuserial
def run():
  myserial = cam_name(cam_name)
  #print c.take_photo()
  print myserial
  #print ftprun.ftprun(cam_name)
  #print ftp.ftphttp(cam_name)
  print test.ftphttp(cam_name)
