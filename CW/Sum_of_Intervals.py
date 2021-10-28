def sum_of_intervals(intervals):
    num = {}
    for i in intervals:
        for j in range(i[0],i[1]):
            num[j] = j
    return len(num)


# function sumIntervals(intervals){
#   var numbers = {};
#   intervals.forEach(function(x) {
#     for (var i = x[0]; i < x[1]; i++) {
#       numbers[i] = i;
#     }
#   });
#   return Object.keys(numbers).length;
# }