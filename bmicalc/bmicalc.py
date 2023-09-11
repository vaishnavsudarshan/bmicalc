from .bmitables import percentiles, boys_percentiles, girls_percentiles
def calc_bmi(weight, height):
    x = height ** 2
    y = weight / x
    z = y * 703
    return z

def calc_weight(bmi, height):
    x = height ** 2
    y = bmi * x
    z = y / 703
    return z

def calc_percentile(bmi, gender, age):
    if gender == "boy":
        table = boys_percentiles
    else:
        table = girls_percentiles
    for i in range(1, len(table)):
        if table[i][0] <= age < table[i+1][0]:
            row = table[i]
            break
    for i in range(1, len(row)):
        if row[i-1] <= bmi < row[i]:
            break
    y1 = percentiles[i-1]
    y2 = percentiles[i]
    x1 = row[i-1]
    x2 = row[i]
    m = (y2-y1)/(x2-x1)
    y = m*(bmi-x1)+y1
    return y

def calc_bmi_from_percentile(gender, age, percentile):
    '''
    '''
    if gender == "boy":
        table = boys_percentiles
    else:
        table = girls_percentiles
    for i in range(1, len(table)):
        if table[i][0] <= age < table[i+1][0]:
            row = table[i]
            break
    for i in range(1, len(percentiles)):
        if percentiles[i-1] <= percentile < percentiles[i]:
            break
    y1 = row[i]
    y2 = row[i+1]
    x1 = percentiles[i]
    x2 = percentiles[i+1]
    m = (y2-y1)/(x2-x1)
    y = m*(percentile-x1)+y1   
    return y

