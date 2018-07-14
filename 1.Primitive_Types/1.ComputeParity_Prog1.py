#Compute Parity of a word

#The parity of a binary word is 1 if the number of 1s in the word is odd;
#it is 0 if the number of 1s in even

#Need to count the number of 1s in a Binary word

#Naive Solution (Time Complexity: O(n))
def naive_parity(x):
    '''
    i/p: x, an int
    o/p: 1, if number of 1s in x is odd
         0, otherwise
    '''
    flag = 0
    #while x is greater than 0
    while x:
        #if lowest bit of x is 1, then and_op becomes 1
        and_op = x & 1
        #flag becomes 1 if and_op is 1 and flag is 0 as it is using xor operation
        #Basically, xor_op is like a flag;
        xor_op = flag ^ and_op
        flag = xor_op
        #Shift x to right side so that we can read all the bits
        x = x >> 1

    #Remember
    #xor is like setting a flag
    #and is like counting 1's
    #shifting to consider other bits
    return flag


print(naive_parity(9))
