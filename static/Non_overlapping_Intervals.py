
def eraseOverlapIntervals(intervals):
    count = 0
    if len(intervals) < 2:
        return count
    intervals.sort(key = lambda x: x[1]) 
    temp = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0] >= temp:
            temp = intervals[i][1]
        else:
            count += 1

    return count


intervals = [[1,2], [2,3], [1,3]]

print (eraseOverlapIntervals(intervals))
