def fix_the_meerkat(arr):
    return [arr[2],arr[1],arr[0]]


print(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
print(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
print(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
print(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
print(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])