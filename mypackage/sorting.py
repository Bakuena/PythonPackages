def bubble_sort(items):

   count = 0

    for idx in range(len(items)-1):
        if items[idx] > items[idx + 1]:
            items[idx],items[idx + 1] = items[idx + 1],items[idx]
            count += 1

    if count == 0:
        return items
    else:
        return bubble_sort(items)
    '''Return array of items, sorted in ascending order'''

    
def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
