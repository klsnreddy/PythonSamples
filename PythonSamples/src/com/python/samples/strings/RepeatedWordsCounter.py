'''
Created on Apr 15, 2017

@author: Phanithi
'''

s = "Hello Nagaraju Hello Phanithi"

#simple way to count words
print(s.count('Hello'))

#Using dictionary
def countRepeatedWords(s, word):
    print(s)
    s = str(s)
    
    if len(s) == 0: return 0
    d = {}
    
    for wrd in s.split(' '):
        if d.__contains__(wrd):
            d[wrd] = d[wrd]+1 
            
        else:
            d[wrd] = 1
            
    # Printing dictionary..
    for key in d.keys():
        print('Key - '+str(key) + ': Count - '+str(d[key]))   
    
    count = 0 
    if d.__contains__(word): 
        count = d[word]
        
    return count

print(countRepeatedWords(s, 'Hello1'))