'''
Created on Apr 1, 2017

@author: Phanithi
'''

class Statements (object):
    

    
    def __init__(self):
        pass


    def runStatementSol(self):
        
       
        #Use for, split(), and if to create a Statement that will print out words that start with 's':
        st = 'Print only the words that start with s in this sentence'
        
        for word in st.split(' '):
            if(word.startswith('s')):
                print(word)
        
        # Use range() to print all the even numbers from 0 to 10.
        print(list(range(0,11,2)))
        
        
        #Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
        lst = [num for num in range(1, 51) if (num % 3 == 0)]  #Note that there is : in for loop
        print(lst)
        
        
        #Go through the string below and if the length of a word is even print "even!"
        st = 'Print every word in this sentence that has an even number of letters'
        for word in st.split(): 
            if len(word)%2 ==0: print(word+" : Even!")
        
        
        #Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
        # and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".    
        for num in range(1, 101):
            if(num % 3 == 0 and num % 5 == 0): print(str(num)+' : FizzBuzz')
            elif (num % 5 == 0): print(str(num)+' : Buzz')
            elif (num % 3 == 0): print(str(num)+' : Fizz')
            
         
        #Use List Comprehension to create a list of the first letters of every word in the string below:
        st = 'Create a list of the first letters of every word in this string'
        lst = [letter[0] for letter in st.split()]
        print(lst)    
            
x = int(input("Enter 10 to proceed : "))
if(x==10):
    stm = Statements()        
    stm.runStatementSol()
else:
    print('Please enter 10!')
    