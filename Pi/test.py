import ftplib
import hashlib
import httplib
import pytz
from datetime import datetime
import urllib
from pytz import timezone
import os.path, time
import glob

def ftphttp(cam_name):
   
 for image in glob.glob(os.path.join('/tmp/image/*.png')):
    
   ts = os.path.getmtime(image)
   dt = datetime.fromtimestamp(ts, pytz.utc)
   timeZone= timezone('Asia/Singapore')
   localtime = dt.astimezone(timeZone).isoformat()
   camid = cam_name(cam_name)
   tscam = localtime + camid
   ftp = ftplib.FTP('10.217.139.111','kevin403','S$ip1234')
   ftp.cwd('/var/www/html/image')

    
   m=hashlib.md5()
   m.update(tscam)
   dd=m.hexdigest()
   with open(image, 'rb') as file:
      ftp.storbinary('STOR '+dd+ '.png', file)
   print "Storing ", image
   
   x = httplib.HTTPConnection('10.217.139.111', 8086)
   x.connect()
   f = {'ts' : localtime}
   x.request('GET','/camera/store?fn='+dd+'&'+urllib.urlencode(f)+'&cam='+cam_name(cam_name))
   y = x.getresponse()
   z=y.read()
   x.close()
   ftp.quit()
'''
   with open(image, 'rb') as file:
     ftp.storbinary('STOR '+dd+ '.png', file)
   print "Storing ", image
'''

