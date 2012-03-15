"""
binary_search.py
===
1. Write a function named search that takes two arguments, a *sorted* list and a value to search for
2. If the value is in the list, return the index of the value
3. If the value is not in the list, return -1
4. Do not use the index() function or in
5. Instead, implement binary search - read the first paragraph on wikipedia: 
	http://en.wikipedia.org/wiki/Binary_search_algorithm
6. See an example in action (enter a state name): 
	http://www.dave-reed.com/book/Chapter8/search.html
7. Don't hesitate to look up the pseudocode: 
	http://www.computingstudents.com/notes/computation_and_algorithms/binary_search.php

Some test output follows!

!!!!!!!!!!!!!!!!!


Call script with verbose option:






python binary_search_tested.py -v


"""
def search(sorted_list, value):
    """
        >>> search([7, 32, 65], 7)
        0
        >>> search([7, 32, 65], 32)
        1
        >>> search([7, 32, 65], 65)
        2
        >>> search([7, 32, 65], 2)
        -1
        >>> search([7, 32, 65], 8)
        -1
        
        >>> search([7, 32, 65, 65], 65)
        2
        
        >>> search([7, 32, 65, 70, 100], 65)
        2
        >>> search([7, 32, 65, 70, 100], 70)
        3
        
        >>> search([7, 32, 65, 70, 100, 102], 65)
        2
        >>> search([7, 32, 65, 70, 100, 102], 70)
        3
        
        >>> search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 9)
        8
        >>> search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 20)
        -1
    """    
    x=0
    last=len(sorted_list)
    first=0
    while x!=len(sorted_list):
        middle=(first+last)/2
        if value==sorted_list[middle]:
            return middle
        elif value>sorted_list[middle]:
            first=middle
        else: #value<sorted_list[middle]:
            last=middle
        x=x+1
    return -1
    
if __name__ == '__main__' :
    import doctest
    doctest.testmod()
