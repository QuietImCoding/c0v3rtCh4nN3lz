import os

class Flagger:

    def __init__(self):
        self.DAT_NAME = '/tmp/DATA'
        self.DSR_NAME = '/tmp/DSR'
        self.DRD_NAME = '/tmp/DRD'
        self.flags = {'dat':self.DAT_NAME,
                      'drd':self.DRD_NAME,
                      'dsr':self.DSR_NAME}
             
    def create_file(self, f:str):
        with open(f, 'w+') as fp:
            pass
    
    def check(self, flag:str):
        return os.path.exists(self.flags[flag])

    def unset(self, flag:str):
        os.remove(self.flags[flag])

    def set(self, flag:str):
        self.create_file(self.flags[flag])
