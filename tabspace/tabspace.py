import re, sys

def spacebin(instr:str, mode:int):
    if mode == 0 and len(instr) != 7: return ''
    if mode == 0:
        return chr(int(''.join(['0' if l == ' ' else '1' for l in instr]),2))
    if mode == 1:
        return '{0:07b}'.format(ord(instr)).replace('0',' ').replace('1','\t')

def decode_msg(msg:str):
    return ''.join([spacebin(a[:7],0) for a in re.findall(r'[\t ]{7}\n', msg)])

def encode_msg(msg:str, hid:str):
    if msg.count('\n') < len(hid): sys.exit("Not enough lines in source!")
    lines = msg.split('\n')
    coded = '\n'.join([lines[i]+spacebin(hid[i],1) for i in range(len(hid))])
    return coded+'\n'+'\n'.join(lines[len(hid)+1:])

usage = '''tabspace.py 1.0
Encodes text in the trailing whitespace of a file

USAGE:
    python3 tabspace.py <input file>
    python3 tabspace.py <carrier file> <hidden file>'''

if len(sys.argv) not in [2, 3]:
    print(usage)
    exit()
elif len(sys.argv) == 2:
    with open(sys.argv[1]) as infile:
        fin = infile.read()
        print(decode_msg(fin), end='')
elif len(sys.argv) == 3:
    with open(sys.argv[1]) as carrier, open(sys.argv[2]) as message:
        ctxt = carrier.read()
        msg = message.read()
        print(encode_msg(ctxt, msg), end='')
