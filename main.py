def get_busy_times(busy):
    return busy['start']


def convert_to_minutes(time):
    return int(time[0:2]) * 60 + int(time[3:5])


def convert_to_time(minutes):
    hours = str(minutes // 60)
    minutes = str(minutes % 60)
    if minutes == '0':
        minutes = '00'

    return hours + ':' + minutes


busy = [
    {'start': '10:30',
     'stop': '10:50'
     },
    {'start': '18:40',
     'stop': '18:50'
     },
    {'start': '14:40',
     'stop': '15:50'
     },
    {'start': '16:40',
     'stop': '17:20'
     },
    {'start': '20:05',
     'stop': '20:20'
     }
]

free = []
start_time = 9 * 60
end_time = 21 * 60

busy.sort(key=get_busy_times)
print(busy)

for i in busy:
    while (start_time + 30) <= convert_to_minutes(i.get('start')) and start_time + 30 <= end_time:
        free.append({'start': convert_to_time(start_time), 'stop': convert_to_time(start_time + 30)})
        start_time += 30
    start_time = convert_to_minutes(i.get('stop'))

while start_time + 30 <= end_time:
    free.append({'start': convert_to_time(start_time), 'stop': convert_to_time(start_time + 30)})
    start_time += 30

print(free)
