import re, os

class Flagger:

    def __init__(self):
        self.filere = r"mozi..a\..ol"
        self.flags = {'dat':4,
                      'drd':5,
                      'dsr':8}
        if self.locate_file() is None:
            with open('/tmp/mozilla.lol', 'w') as f:
                pass


    def locate_file(self):
        checkfiles = [re.findall(self.filere, f) for f in os.listdir('/tmp')]
	# Flatten 2d list - shamelessly stolen from coderwall.com
        flattened = [y for x in checkfiles for y in x]
        return flattened[0] if len(flattened) > 0 else None

    def check(self, flag:str):
        fname = self.locate_file()
        #print(fname[self.flags[flag]])
        return (fname[self.flags[flag]] == '1')

    def unset(self, flag:str):
        fname = self.locate_file()
        nfname = fname[:self.flags[flag]] + 'l' + fname[self.flags[flag]+1:]
        os.rename(f"/tmp/{fname}", f"/tmp/{nfname}")

    def set(self, flag:str):
        fname = self.locate_file()
        nfname = fname[:self.flags[flag]] + '1' + fname[self.flags[flag]+1:]
        os.rename(f"/tmp/{fname}", f"/tmp/{nfname}")
