f = open('std.py', 'r')

# read entire file
f.read()

# read one line
f.readline()

# for loop to read lines
for line in f:
    print line

# read all lines in a list 
list(f) 
f.readlines()

# write to file
f.write('something')

# get file object's current position in the file, measured in bytes from the beginning of the file
f.tell()

# over the position pointer
f.seek(offset, from_what)

# close the handler
f.close()
