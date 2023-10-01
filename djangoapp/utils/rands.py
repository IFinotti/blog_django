
import string
from random import SystemRandom


def random_letters(k=5):
    return SystemRandom().choices(
        string.ascii_letters + string.digits, k=k
    )