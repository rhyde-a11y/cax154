import math
import random
import platform

random_number = random.randint(1, 100)

sqrt_rectangle = math.sqrt(random_number)

os_name = platform.system()
py_ver = platform.python_version()

import requests
response = requests.get('https://api.github.com')