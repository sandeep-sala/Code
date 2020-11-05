def sequence_sum(begin_number, end_number, step, s = 0):
    if begin_number > end_number: return 0
    if s == 0 :  s = begin_number
    if begin_number != end_number:
        begin_number += step
        if begin_number <= end_number:
            s += begin_number
            return sequence_sum(begin_number, end_number, step, s)
    return s








print(sequence_sum(2, 6, 2), 12)
print(sequence_sum(1, 5, 1), 15)
print(sequence_sum(1, 5, 3), 5)
print(sequence_sum(0, 15, 3), 45)
print(sequence_sum(16, 15, 3), 0)
print(sequence_sum(2, 24, 22), 26)
print(sequence_sum(2, 2, 2), 2)
print(sequence_sum(2, 2, 1), 2)
print(sequence_sum(1, 15, 3), 35)
print(sequence_sum(15, 1, 3), 0)