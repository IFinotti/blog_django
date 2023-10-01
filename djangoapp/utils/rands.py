import string
from random import SystemRandom
from django.utils.text import slugify

def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits, k=k
    ))

# print(random_letters())

def new_slugify(text, k=5):
    return slugify(text) + random_letters(k)