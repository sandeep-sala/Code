def flick_switch(lst):
    k, p = True, []
    for i in lst:
        if i == "flick":
            k = not k
        p.append(k)
    return p


print(flick_switch(['codewars', 'flick', 'code', 'wars']),
      [True, False, False, False])
print(flick_switch(['flick', 'chocolate', 'adventure', 'sunshine']), [
      False, False, False, False])
print(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']), [
      True, True, False, False, True])
print(flick_switch(['bicycle']), [True])
print(flick_switch([('john', 'smith', 'susan'), 'flick']), [True, False])
print(flick_switch(['flick', 'flick', 'flick', 'flick', 'flick']), [
      False, True, False, True, False])
print(flick_switch([]), [])
