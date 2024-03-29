def switch_gravity(lst):
    ln = len(lst)
    sl = len(lst[0])
    for i in range(0, sl):
        k = []
        for j in range(0, ln):
            k.append(lst[j][i])
        k.sort(reverse=True)
        for j in range(0, ln):
            lst[j][i] = k[j]
    return lst

print(switch_gravity([
    ["-", "#", "#", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"]
]
), [
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],
    ["-", "#", "#", "-"]
])


print(switch_gravity([
    ["-", "#", "#", "-"],
    ["-", "-", "#", "-"],
    ["-", "-", "-", "-"],
]
), [
    ["-", "-", "-", "-"],
    ["-", "-", "#", "-"],
    ["-", "#", "#", "-"]
])


print(switch_gravity([
    ["-", "#", "#", "#", "#", "-"],
    ["#", "-", "-", "#", "#", "-"],
    ["-", "#", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"]
]
), [
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "#", "-", "#", "#", "-"],
    ["#", "#", "#", "#", "#", "-"]
])

print(switch_gravity([
    ["-", "#", "#", "#", "#", "-"],
    ["#", "-", "-", "#", "#", "-"],
    ["-", "#", "-", "-", "-", "-"],
    ["-", "#", "-", "#", "-", "-"]
]
), [
    ["-", "-", "-", "-", "-", "-"],
    ["-", "#", "-", "#", "-", "-"],
    ["-", "#", "-", "#", "#", "-"],
    ["#", "#", "#", "#", "#", "-"]
])

print(switch_gravity([
    ["-", "#", "#", "-"],
    ["-", "-", "#", "-"],
    ["#", "#", "-", "-"],
]
), [
    ["-", "-", "-", "-"],
    ["-", "#", "#", "-"],
    ["#", "#", "#", "-"]
])

print(switch_gravity([
    ["#"],
    ["-"],
    ["#"],
    ["-"]
]
), [
    ["-"],
    ["-"],
    ["#"],
    ["#"]
])

print(switch_gravity([
    ["#"],
    ["#"],
    ["#"],
    ["#"]
]
), [
    ["#"],
    ["#"],
    ["#"],
    ["#"]
])