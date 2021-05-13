#!/usr/bin/env python3
import os
import zipfile


filetocheck = input("What file are we checking today? ")
filetocheck = '/home/student/mywork/quickzippy/myarchive.zip'
print(zipfile.is_zipfile(filetocheck))
