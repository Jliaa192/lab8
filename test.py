import re
from datetime import datetime
date_string = input()
def fod(date_string):
    a = r'^(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})$'
    match = re.match(a, date_string)
    if not match:
        return False
    day,month,year = map(int,match.groups())
    try:
        datetime(year=year, month=month, day=day)
        if 1600 <= year <= 9999:
            return True
        else:
            return False
    except ValueError:
        return False
print(fod(date_string))
