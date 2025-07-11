import random, time

def random_delay(min_d=0.3, max_d=1.5):
    time.sleep(random.uniform(min_d, max_d))
