import sys

def nospace(msg, car):
    out = u''
    ind = 0
    if len(msg) < 8*len(car):
        sys.exit(f"Message is {(len(car)*8)-len(msg)} characters too short")
    for l in car:
        for b in format('{0:08b}'.format(ord(l))):
            out += msg[ind]
            if b == '1': out += u'\u200b'
            ind += 1
    out += msg[ind:]
    return out

def findspace(msg):
    outstr = ''
    buf = []
    ind = 0
    while ind < len(msg)-1:
        if ord(msg[ind+1]) == 8203:
            buf.append('1')
            ind += 1
        else:
            buf.append('0')
        if len(buf) == 8:
            nchar = chr(int(''.join(buf), 2))
            if nchar =='\0':
                continue
            outstr += nchar
            buf = []
        ind+=1
    return outstr


usage = """Usage:
    python3 nospace.py <<file1>> [[file2]]

If one argument is provided, file1 will be decoded
If two arguments are provided, file2 will attempt to be encoded into file1"""

if len(sys.argv) not in [2,3]:
    print(usage)
    exit()
elif len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as message:
        print(findspace(message.read()))
elif len(sys.argv) == 3:
    with open(sys.argv[1], 'r') as carrier, open(sys.argv[2], 'r') as message:
        print(nospace(carrier.read(), message.read()))

