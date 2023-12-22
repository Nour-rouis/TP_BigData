import sys

sentiment_neg=["nul", "insatisfait","bof", "incompétents"]
sentiment_pos=["satisfait", "super", "excellent"]
for line in sys.stdin:
    sent_neg_find=[]
    sent_pos_find=[]
    #remove leading and trailing whitespace 
    line = line.strip()
    # split the line into words
    words = line.split()
    #increase counters
    for word in words :
    
        if(word in sentiment_neg):
            sent_neg_find.append("insatisfait")
        elif(word in sentiment_pos):
            sent_pos_find.append("satisfait")
    if(len(sent_neg_find)==len(sent_pos_find)):
        print("{}\t1".format("inconcluant"))
    elif (len(sent_neg_find)<len(sent_pos_find)):
        print("{}\t1".format("satisfait"))
    elif(len(sent_neg_find)>len(sent_pos_find)):
        print("{}\t1".format("insatisfait"))