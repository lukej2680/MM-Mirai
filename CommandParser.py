def getAlarmDays(string):
    days = ['monday', 'tuesday', 'wednsday', 'thursday', 'friday', 'saturday', 'sunday']
    results = []

    for day in days:
        if day in string:
            results.append(day)

    return results


def getAlarmTime(string):
    for word in string:
        if word[0].isdigit():
            time = word

    return None