import os
import sys

import capture
import detect

if __name__ == '__main__' :
    source_datapath=sys.argv[1]
    capture.save_video_to_image(source_datapath)
    datapath=os.path.join(source_datapath,'output')
    detect.run(source=datapath)
