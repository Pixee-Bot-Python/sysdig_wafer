import time
import secrets


def rndstr(length):
    return ''.join(secrets.choice('0123456789abcdef') for i in range(length))


def choice(arr):
    # randomize seed
    return secrets.choice(arr)


def rndunicode():
    # randomize seed
    return chr(secrets.SystemRandom().randint(0, 0x10FFFF))


def choice_percent(elements):
    # elements is a dict of {percent: action}
    # like following:
    # elements = {
    #     10: lambda: 'a',
    #     20: lambda: 'b',
    #     30: lambda: 'c',
    #     40: lambda: 'd',
    # }
    # that means we have 10% chance to get 'a', 20% chance to get 'b', etc.

    total_percent = sum(elements.keys())

    # get random number
    rnd = secrets.SystemRandom().randint(1, total_percent)

    # get action
    cumulative_percent = 0
    for percent, action in elements.items():
        cumulative_percent += percent
        if rnd <= cumulative_percent:
            return action

    # should not reach here
    return None
