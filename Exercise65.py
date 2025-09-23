#چند روزشه؟
from datetime import datetime

def day_calculator(dateStr):
    mainDate = "1999-01-14"
    mainDate = datetime.strptime(mainDate,'%Y-%m-%d').date()
    dateStr = datetime.strptime(dateStr,'%Y-%m-%d').date()
    if dateStr < mainDate:
        result = "Not yet born"
    else:
        result = (dateStr - mainDate).days
    return result
    
print(day_calculator('1118-10-13'))