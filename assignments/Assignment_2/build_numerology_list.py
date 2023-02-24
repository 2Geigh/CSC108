def build_numerology_list(compatibility_data: list[str]) -> list:
    """
    Given `compatibility_data`, formatted as in NUM_COMPATIBILITY_DATA, return
    a list of lists with the following structure:

        [
            [n1, [all compatible nums for n1], [all incompatible nums for n1]],
            [n2, [all compatible nums for n2], [all incompatible nums for n2]],
            :
        ]

    Each inner compatibility list will be sorted in increasing order, and
    the overall list should be sorted by the n's.

    >>> test_list = ['1,2,YES', '1,1,YES', '1,4,NO']
    >>> build_numerology_list(test_list)
    [[1, [1, 2], [4]]]

    >>> test_list = ['3,1,NO', '1,3,YES']
    >>> build_numerology_list(test_list)
    [[1, [3], []], [3, [], [1]]]

    >>> test_list = ['1,1,YES', '1,2,YES', '2,3,YES', '3,1,YES','3,2,NO']
    >>> build_numerology_list(test_list)
    [[1, [1, 2], []], [2, [3], []], [3, [1], [2]]]

    >>> test_list = ['8,7,YES', '4,3,NO', '2,4,YES', '8,3,NO', '8,9,YES']
    >>> build_numerology_list(test_list)
    [[2, [4], []], [4, [], [3]], [8, [7, 9], [3]]]

    >>> test_list = ['8,7,YES', '4,3,NO', '3,4,YES', '8,4,YES', '8,3,NO', '8,9,YES', '22,4,YES']
    >>> build_numerology_list(test_list)
    [[3, [4], []], [4, [], [3]], [8, [4, 7, 9], [3]], [22, [4], []]]
    """


    final_return_list = []

    for data_set in compatibility_data:
        #setting index
        if data_set[0:2] == '11':
            index = '11'
        elif data_set[0:2] == '22':
            index = '22'
        else:
            index = data_set[0]

        #getting child
        if len(index) >= 2:
            child = data_set[3]
        else:
            child = data_set[2]

        list_to_append = [int(index)]
        if 'YES' in data_set:
            list_to_append.append([int(child)])
            list_to_append.append([])
        else:
            list_to_append.append([])
            list_to_append.append([int(child)])

        final_return_list.append(list_to_append)
        
    
    final_return_list.sort()

    
    
    """for i in range(0,len(final_return_list) - 2):
        if final_return_list[i][0] == final_return_list[i + 1][0]:
            final_return_list[i][1].extend(final_return_list[i+1][1])
            final_return_list[i][1].sort()            

            final_return_list[i][2].extend(final_return_list[i+1][2])
            final_return_list[i][2].sort()

            final_return_list.__delitem__(i+1)"""

    def multiple_sublist_same_index(list_of_lists: list[list], n:int) -> True:
        """PRECONDITION: Sublists within list_of_lists MUST have their first element be an integer, and the list_of_lists must be sorted in ascending order by first element.
        
        This function returns a boolean value depending on whether or not there are multlpe sublists of index n within list_of_lists
        
        >>> test_list = [[2, [4], []], [2, [], [3]], [8, [7, 9], [3]]]
        >>> multiple_sublist_same_index(test_list, 2)
        True

        >>> test_list = [[2, [4], []], [4, [], [3]], [8, [7, 9], [3]]]
        >>> multiple_sublist_same_index(test_list, 2)
        False
        
        >>> test_list = [[2, [4], []], [8, [7, 9], [3]]]
        >>> multiple_sublist_same_index(test_list, 9)
        False
        
        >>> test_list = [[1, [4], []], [1, [7, 9], [3]]]
        >>> multiple_sublist_same_index(test_list, 1)
        True
        
        >>> test_list = [[1, [4], []]]
        >>> multiple_sublist_same_index(test_list, 1)
        False
        """
        if len(list_of_lists) < 2:
                return False
        for sublist_A in list_of_lists:
                for sublist_B in list_of_lists:
                        if sublist_A != sublist_B and (n == sublist_A[0] and n == sublist_B[0]):
                                return True
        return False
        
    new_final_return_list = []    
    
    possible_indexes = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22)
    
    for n in possible_indexes:
        to_append = [n, [], []]
        
        #create a list called of_index_n of every sublist with index n
        of_index_n = []
        for sublist in final_return_list:
            if sublist[0] == n:
                of_index_n.append(sublist)
        #for every sublist in of_index_n, extend the second and third elements of to_append
        for sublist in of_index_n:
            to_append[1].extend(sublist[1])
            to_append[2].extend(sublist[2])

        new_final_return_list.append(to_append)
    
    new_new_final_return_list = []
    
    for sublist in new_final_return_list:
        if sublist[1] == [] and sublist[2] == []:
            continue
        else:
            new_new_final_return_list.append(sublist)
            
                

    return new_new_final_return_list

    # TODO: fill in the expected value for the last docstring example above

    # TODO: design and write the function body
    
print("\n")
print(build_numerology_list(['1,2,YES', '1,1,YES', '1,4,NO']))
print([[1, [1, 2], [4]]])
print("\n")

print(build_numerology_list(['3,1,NO', '1,3,YES']))
print([[1, [3], []], [3, [], [1]]])
print("\n")

print(build_numerology_list(['1,1,YES', '1,2,YES', '2,3,YES', '3,1,YES','3,2,NO']))
print([[1, [1, 2], []], [2, [3], []], [3, [1], [2]]])
print("\n")

print(build_numerology_list(['8,7,YES', '4,3,NO', '2,4,YES', '8,3,NO', '8,9,YES']))
print([[2, [4], []], [4, [], [3]], [8, [7, 9], [3]]])
print("\n")

print(build_numerology_list(['8,7,YES', '4,3,NO', '3,4,YES', '8,4,YES', '8,3,NO', '8,9,YES', '22,4,YES']))
print([[3, [4], []], [4, [], [3]], [8, [4, 7, 9], [3]], [22, [4], []]])
print("\n")