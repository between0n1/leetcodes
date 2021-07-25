def minimumSwaps(arr):
    """
    intuition:
    from left to right, when we find i != elem, we try to find the smallest number in range(i+1,len(arr))
    and we will call the above range as "right portion of the array"
    we swap elem with smallest number from right portion.
    repeat this until we reach end of array.

    However, even though above approach results in correct answer, its time complexity is O(n^2) since we have two for loops.
    Therefore, we will create another array called a whose index indicates
    orig array's value, and a[value] = value's index in original array
    so that we can find smallest number's index with O(1) complexity.
    for example :
    arr = [0,2,4,1,3,5]
    a = [ index of 0 in orig array, index of 1 in orig array, index of 2 in orig array, ...... ]
    a[4] = 2 because the number 4 is located at position 2 in original array.

    while moving from left to right,
    if we find an element in correct position, we have to move to next smallest element
    so, aPtr += 1.
    else we find an element in incorrect position, we swap it with smallest element
    and update the element's (not smallest one) index in the array a to the point where the element will be moved
    """

    count = 0  # count swap
    arr = [i - 1 for i in arr]  # orig arr's smallest elem is 1 so I wanted to make it more intutive by doing i - 1
    a = [0 for i in range(len(arr))]
    for i, val in enumerate(arr):
        a[val] = i  # a[val] = val's index in orig array
        # since orig array is continuous (there is no gap between numbers)
        # this array's index indicates orig array's value in ascending order
        #
    aIndex = 0  # index for array a
    for i, val in enumerate(arr):
        if i != val:  # if current element is not in correct position
            a[val] = a[aIndex]  # we swap val's position in next line so we have to change array a
            arr[i], arr[a[aIndex]] = arr[a[aIndex]], arr[i]  # swap.
            count += 1  # a[aIndex] positined at the right position and arr[0: (aIndex == val)(inclusive)] is sorted since we found the smallest element to be at the right position
        aIndex += 1  # we find next smallest element
    print(arr)
    return count