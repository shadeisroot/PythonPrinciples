

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(d):
    count = 0
    for x in d.values():
        if x == 'online':
            count = count +1
    return(count)
online_count(statuses)