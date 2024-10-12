intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key = lambda i:i[0])

start = intervals[0][0]
end = intervals[0][1]

output = intervals[0]
final = []

for i in range(1,len(intervals)):
    if intervals[i][0] < end:
        final.append([start,max(end,intervals[i][1])])
    else:
        final.append([intervals[i][0],intervals[i][1]])

print(final)