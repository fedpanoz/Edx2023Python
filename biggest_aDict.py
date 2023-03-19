def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if aDict == {}:
        return None
    else:
        max = 0
        for key in aDict:
            if len(aDict[key]) >= max:
                max = len(aDict[key])
                maxKey = key
        return maxKey