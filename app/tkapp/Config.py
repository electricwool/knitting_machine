import os

class Config:
    def __init__(self):
        self.imgdir = "img";
        if os.sys.platform == 'win32':
            self.device = "com34"
#            self.datFile = './'
            self.datFile = './'
            self.simulateEmulator = True
        else:
            self.device = "/dev/ttyUSB0"
