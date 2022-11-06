def format_duration(seconds):
    if seconds == 0:
        return 'now'
    years = seconds // 31536000
    days = ((seconds % 31536000) // 86400)
    hours = (((seconds % 31536000) % 86400) // 3600)
    minu = ((((seconds % 31536000) % 86400) % 3600) // 60)
    sec = (((seconds % 31536000) % 86400) % 3600) % 60
    k = []
    if years > 0:
        k.append(f'{years} { "year" if years == 1 else "years"}')
    if days > 0:
        k.append(f'{days} { "day" if days == 1 else "days"}')
    if hours > 0:
        k.append(f'{hours} { "hour" if hours == 1 else "hours"}')
    if minu > 0:
        k.append(f'{minu} { "minute" if minu == 1 else "minutes"}')
    if sec > 0:
        k.append(f'{sec} { "second" if sec == 1 else "seconds"}')

    j = len(k)

    if j == 1:
        return k[0]
    elif j == 2:
        return " and ".join(k)
    elif j > 2:
        return ", ".join(k[:-2])+", "+" and ".join(k[-2:])


print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds")
