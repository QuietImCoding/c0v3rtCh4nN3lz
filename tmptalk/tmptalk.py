# Create / Remove file /tmp/DATA
# Create / Remove file /tmp/DSR - stable data
# Read DRD - check if receiver has read the data
import time, sys,os
from mozilla_flagger import Flagger

#Instantiate flagger class
flagger = Flagger()

def mod_data_file(bit:int):
    """Modulates the data file by setting flags

    bit -- the whether to set or unset the flag, one bit of the data"""
    if bit==1:
        flagger.set('dat')
    else:
        if flagger.check('dat'): flagger.unset('dat')
    
def send_msg(message:bytes):
    """Send the message via the tmp directory

    message -- the message to send"""
    msgbin = ''.join(['{0:08b}'.format(byt) for byt in message + b'\0'])

    for bit in msgbin:
        #print(os.listdir('/tmp'))
        if bit == '0': mod_data_file(0)
        else: mod_data_file(1)
        flagger.set('dsr')
        while not flagger.check('drd'):
            pass
        flagger.unset('drd')

def rcv_msg():
    """Receive the message via the tmp directory
    """
    outstring = ''
    bitbuf = []
    recvd = 0
    while '\0' not in outstring:
        while not flagger.check('dsr'):
            pass
        flagger.unset('dsr')
        
        bitbuf.append('1' if flagger.check('dat') else '0')

        if len(bitbuf) == 8:
            outstring += chr(int(''.join(bitbuf), 2))
            bitbuf = []
        recvd += 1
        
        flagger.set('drd')
        
    return outstring

# Unset all the flags before running
if flagger.check('dat'): flagger.unset('dat')
if flagger.check('drd'): flagger.unset('drd')
if flagger.check('dsr'): flagger.unset('dsr')

# Long usage string, maybe should put in another file
usage = """Usage:
    python3 tmptalk.py [[filename]]
    
If filename is provided, tmptalk will write the file via the tmp directory covert channel
Otherwise tmptalk will read from the covert channel
Always run the read functionality first!

Examples:
    python3 tmptalk.py - will start listening for data
    python3 tmptalk.py tmptalk.py - will write data to the channel
"""

# Deciding to print the usage string
if len(sys.argv) not in [1,2] or (len(sys.argv) == 2 and sys.argv[1] == '-h'):
    print(usage)
    exit()

# No args -> receive
if len(sys.argv) == 1:
    print(rcv_msg())
    # Clean up after receiving
    if flagger.check('dat'): flagger.unset('dat')
    if flagger.check('drd'): flagger.unset('drd')
    if flagger.check('dsr'): flagger.unset('dsr')
    exit()

# Args given -> send
try:
    with open(sys.argv[1], 'rb') as mycode:
        send_msg(mycode.read())
except FileNotFoundError as e:
    print("Invalid file path. Please try again")

