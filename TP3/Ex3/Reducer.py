  #!/usr/bin/env python
# coding: utf-8


#!/usr/bin/env python 
import sys 
#Initialize variables 
current_word = None 
current_count = 0
word = None 
#Iterate through input lines, which are sorted by key (word) in ascending order 
for line in sys.stdin:
    #remove leading and trailing whitespace 
    line = line.strip()
    #split the key (word) and value (count) by a tab character 
    word, count = line.split('\t',1)
    #convert the count to an integer 
    try :
        count =  int(count)
    except ValueError:
        #if the conversion fails, skip this line
        continue
    #if the current word is the same as the previous word, increment the count
    if current_word == word:
        current_count +=count 
    else:
        #if the word changes, print the result for the previous word 
        if current_word :
            print('{}\t{}'.format(current_word,current_count))
        #Reset the variables for the new word .
        current_word = word 
        current_count = count 
#print the result for the last word 
if current_word == word :
    print('{}\t{}'.format(current_word,current_count))
