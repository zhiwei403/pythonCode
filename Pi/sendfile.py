import os 
import glob
import CameraID
#files = glob.glob('/tmp/image/*.png')

count = 1
while (count==1):
    files = glob.glob('/tmp/image/*.png')
    for image in files:
            if ( not os.path.isfile(image)):
                print("Error: %s file not found" %image)
            else:
                print("Sending file %s ..." % image)
                print CameraID.run()
                print os.remove(image)
