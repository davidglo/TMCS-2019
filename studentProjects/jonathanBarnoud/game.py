#!/usr/bin/env python
import random
import time

adjectives = [
    'great',
    'strong',
    'smart',
    'modest',
]

for i in range(100):
    print('Jonathan is {}!'.format(random.choice(adjectives)))
    time.sleep(0.5)
