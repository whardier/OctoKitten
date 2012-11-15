#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__name__ = "octokitten"
__author__ = 'Shane R. Spencer'
__email__ = "shane@bogomip.com"
__license__ = 'MIT'
__copyright__ = '2012 Shane R. Spencer'
__version__ = '0.0.1'
__status__ = "Prototype"
__description__ = "Squid filter to replace images with images from http://placekitten.com/"

import sys
import syslog
import urllib2
import urlparse

from cStringIO import StringIO

from PIL import Image

def run():

    syslog.openlog(logoption=syslog.LOG_PID)
    syslog.syslog('Processing started')

    while True:
        line = sys.stdin.readline().strip()    
        url = line.split(' ', 1)[0]    
        spliturl = urlparse.urlparse(url)

        if " GET" in line:
            if spliturl.scheme == 'http':    
                lpath = spliturl.path.lower()
                if lpath[-4:] in ('.png', '.jpg', '.gif'):
                    response = urllib2.urlopen(url)
                    if response.code == 200:                    
                        image = StringIO(response.read())

                        try:
                            pilimage = Image.open(image)
                            width, height = pilimage.size
                        except:
                            width = 0
                            height = 0

                        if width and height:
                            newurl = 'http://placekitten.com/%d/%d' % (width, height)
                            syslog.syslog(newurl)
                            sys.stdout.write('302:%s\n' % newurl)
                            sys.stdout.flush()
                            continue
                            
        sys.stdout.write('\n')
        sys.stdout.flush()

if __name__ == "__main__":
    run()
