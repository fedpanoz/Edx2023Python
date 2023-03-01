def oddTuples(aTup):
    if len(aTup) > 0:

        newTup = (aTup[0],)
        for i in range(1, len(aTup)):
            if i % 2 == 0:
                newTup += (aTup[i],)
        return newTup
    else:
        newTup = ()
        return newTup
print(oddTuples(()))
