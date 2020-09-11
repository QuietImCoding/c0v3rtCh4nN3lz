import re, sys

def spacebin(instr:str, mode:int):
    """Converts one letter to spaces / tabs or vice versa

    instr -- The string input, either one letter or a bunch of spaces and tabs
    mode -- 0 or 1 determines whether encoding or decoding
    """
    # Return nothing if less than 7 bits of whitespace to decode
    if mode == 0 and len(instr) != 7: return ''
    if mode == 0:
        # Convert spaces + tabs to 1 and 0, then cast to int, then cast to ascii
        return chr(int(''.join(['0' if l == ' ' else '1' for l in instr]),2))
    if mode == 1:
        # Format ascii to binary, then replace 0 with space and 1 with tab
        return '{0:07b}'.format(ord(instr)).replace('0',' ').replace('1','\t')

def decode_msg(msg:str):
    """Decode hidden message from string

    msg -- message with hidden data to decode
    """
    # Use regex to find all groups of whitespace with a newline after it,
    # Then decode them using spacebin and join them
    return ''.join([spacebin(a[:7],0) for a in re.findall(r'[\t ]{7}\n', msg)])

def encode_msg(msg:str, hid:str):
    """Encode hidden string in carrier string

    msg -- message to hide data in / carrier
    hid -- data to hide in msg
    """
    # Make sure that there are enough lines in the source file to hide message
    if msg.count('\n') < len(hid): sys.exit("Not enough lines in source!")
    lines = msg.split('\n')
    # Append data to ends of lines + join with newlines
    coded = '\n'.join([lines[i]+spacebin(hid[i],1) for i in range(len(hid))])
    # Add back the rest of the file 
    return coded+'\n'+'\n'.join(lines[len(hid)+1:])

usage = '''tabspace.py 1.0
Encodes text in the trailing whitespace of a file

USAGE:
    python3 tabspace.py <input file>
    python3 tabspace.py <carrier file> <hidden file>'''

# Make sure arg number makes sense
if len(sys.argv) not in [2, 3]:
    print(usage)
    exit()
# If 2 arguments, decode the file
elif len(sys.argv) == 2:
    with open(sys.argv[1]) as infile:
        fin = infile.read()
        print(decode_msg(fin), end='')
# If 3 arguments, encode second file in first file
elif len(sys.argv) == 3:
    with open(sys.argv[1]) as carrier, open(sys.argv[2]) as message:
        ctxt = carrier.read()
        msg = message.read()
        print(encode_msg(ctxt, msg), end='')
