# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # base case 1
    if len(sequence) == 1:
        return [sequence]
    # get smaller lists, all the way to 1 letter
    else:
        perm = []
        first_letter = sequence[0]
        sequence = sequence[1:]
        perm_list = get_permutations(sequence) # recursion to get lists
        
        # add first letter to different position of the lists created during iteration
        for p in perm_list:
            for n in range(0, len(p) + 1):
                new_comb = p[:n] + first_letter + p[n:]
                perm.append(new_comb)
        # first will return list of smaller combs, but in the end will get the final combs
        return list(set(perm))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
#    input1 = 'ab'
#    print('Input:', input1)
#    print('Expected Output:', ['ab', 'ba'])
#    print('Actual Output:', get_permutations(input1))
#    
#    input2 = 'aaa'
#    print('Input:', input2)
#    print('Expected Output:', ['aaa'])
#    print('Actual Output:', get_permutations(input2))
#    
#    input3 = 'abb'
#    print('Input:', input1)
#    print('Expected Output:', ['abb', 'bba', 'bab'])
#    print('Actual Output:', get_permutations(input3))
    
    print(get_permutations('aeiou'))


    
    
    
    
    
    
    
    
    
    
    
    
    
    

