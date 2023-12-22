import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # split the line into timestamp and URL
    timestamp, url = line.split(' ', 1)
    
    # emit URL and count 1 as a key-value pair
    print("{}\t{}".format(url, 1))
