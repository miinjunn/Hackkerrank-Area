s1 = '07:05:45PM'
s2 = '12:45:00PM'
s3 = '12:45:00AM'


def timeConversion(s):
    times = s.split(':')
    if times[-1][2:] == 'PM':
        if times[0] == '12':
            times[0] = '12'
        else:
            times[0] = str(int(times[0]) + 12)
        times[-1] = times[-1][:2]
        return ':'.join(times)

    elif times[-1][2:] == 'AM':
        if times[0] == '12':
            times[0] = '00'
        times[-1] = times[-1][:2]
        return ':'.join(times)


print(timeConversion(s1))
print(timeConversion(s2))
print(timeConversion(s3))
