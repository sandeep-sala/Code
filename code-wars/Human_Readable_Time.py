from  datetime import timedelta
def make_readable(s):
    a = str(timedelta(seconds=s))
    p = str(timedelta(seconds=s)).split(":")
    if len(a.split(",")) > 1:
        a = a.split(",")[0].replace("days","").replace("day","").strip()
        a = int(a)*24 + int(p[0].split(",")[1].strip())
        return '{:02}:{:02}:{:02}'.format(int(a), int(p[1]), int(p[2]))
    return '{:02}:{:02}:{:02}'.format(int(p[0]), int(p[1]), int(p[2]))


print(make_readable(0), "00:00:00")
print(make_readable(5), "00:00:05")
print(make_readable(60), "00:01:00")
print(make_readable(86399), "23:59:59")
print(make_readable(359999), "99:59:59")