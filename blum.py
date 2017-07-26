def select_median_of_medians_pivot(array, k):
    
    if len(array) <= 80:
        sorted(array)
        return array[k]
 

    subset_size = 7  
    subsets = []  
    num_medians = len(array) // subset_size
    if (len(array) % subset_size) > 0:
        num_medians += 1  
    for i in range(num_medians):
        beg = i * subset_size
        end = min(len(array), beg + subset_size)
        subset = array[beg:end]
        subsets.append(subset)
 

    medians = []  # list of medians
    for subset in subsets:
        median = select_median_of_medians_pivot(subset, len(subset)//2)
        medians.append(median)

    median_of_medians = select_median_of_medians_pivot(medians, len(medians)//2)
    pivot = median_of_medians 

    array_lt = []
    array_gt = []
    array_eq = []
    for item in array:
        if item < pivot:
            array_lt.append(item)
        elif item > pivot:
            array_gt.append(item)
        else:
            array_eq.append(item)
 
    
    if k < len(array_lt):
        return select_median_of_medians_pivot(array_lt, k)
    elif k < len(array_lt) + len(array_eq):
        return array_eq[0]
    else:
        normalized_k = k - (len(array_lt) + len(array_eq))
        return select_median_of_medians_pivot(array_gt, normalized_k)

def Filter(arr):
    k = (len(arr)*7)//10
    n=select_median_of_medians_pivot(arr, k)
    return n
