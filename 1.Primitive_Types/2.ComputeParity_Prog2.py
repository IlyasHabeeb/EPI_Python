#Compute Parity of a word

#The parity of a binary word is 1 if the number of 1s in the word is odd;
#it is 0 if the number of 1s in even

#Need to count the number of 1s in a Binary word

#Better Solution (Time Complexity: O(k) where k = #1's in the word)
def better_parity(x):
    '''
    i/p: x, an int
    o/p: 1, if number of 1s in x is odd
         0, otherwise
    '''
    #Initializing flag to be 0
    flag = 0

    #while x > 0 (loop repeats only {#1s in word} times)
    while x:

        #set flag to be 1 if flag = 0 and to be 0 if flag = 1
        flag = flag ^ 1
        #bit-fiddling trick
        x = x & x-1 #clears the lowest bit 1 (i.e., changes it to 0)

    return flag

print(better_parity(9))
