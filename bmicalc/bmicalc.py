'''
The model
'''
# pylint: disable-msg=C0103

from .bmitables import percentiles, boys_percentiles, girls_percentiles

def calc_bmi(weight, height):
    '''
    Calculate BMI given weight (lb) and height (inches)
    '''
    x = height ** 2
    y = weight / x
    z = y * 703
    return z

def calc_weight(bmi, height):
    '''
    Calculate weight (lb) given BMI and height (inches)
    '''
    x = height ** 2
    y = bmi * x
    z = y / 703
    return z

def calc_percentile(bmi, gender, age):
    '''
    Calculate percentile given BMI, Gender and Age (months)
    '''
    if gender == "boy":
        table = boys_percentiles
    else:
        table = girls_percentiles
    print(f'Age in months = {age=}')
    for i in range(len(table)-1):
        if table[i][0] <= age < table[i+1][0]:
            row = table[i]
            break
    print(f'Age = {row[:10]}, {bmi=}')
    if bmi < row[1]:
        y = percentiles[1] * bmi / row[1]
        return y

    if bmi > row[-1]:
        y = (2.99*bmi - 99.99*row[-1] + 3880)/(40-row[-1])
        return y
    

    for i in range(1, len(row)-1):
        if row[i] <= bmi < row[i+1]:
            print(f'{row[i]=}, {bmi=}, {row[i+1]=}')
            break
    print(f'{i=}')
    y1 = percentiles[i]
    y2 = percentiles[i+1]
    x1 = row[i]
    x2 = row[i+1]
    print(f'{x1=}, {x2=}, {y1=}, {y2=}')

    m = (y2-y1)/(x2-x1)
    y = m*(bmi-x1)+y1
 
    print(f'BMI Percentile, {y=}')
    return y

def calc_bmi_from_percentile(gender, age, percentile):
    '''
    Calculate BMI given percentile, gender and age (months)
    '''
    if gender == "boy":
        table = boys_percentiles
    else:
        table = girls_percentiles
    for i in range(len(table)-1):
        if table[i][0] <= age < table[i+1][0]:
            row = table[i]
            break
    if 0 <= percentile < percentiles[1]:
        y = percentile*row[1]/percentiles[1]
        return y

    if percentile >= percentiles[-1]:
        y1 = row[-2]
        y2 = row[-1]
        x1 = percentiles[-2]
        x2 = percentiles[-1]
        m = (y2-y1)/(x2-x1)
        y = m*(percentile-x1)+y1
        return y

    for i in range(1, len(percentiles)-1):
        if percentiles[i] <= percentile < percentiles[i+1]:
            break
            
    y1 = row[i]
    y2 = row[i+1]
    x1 = percentiles[i]
    x2 = percentiles[i+1]
    m = (y2-y1)/(x2-x1)
    y = m*(percentile-x1)+y1
    return y

def get_bmi_percentiles(gender):
    months = []
    bmi_percentiles = []
    for _ in range(len(percentiles)-1):
        bmi_percentiles.append([])

    if gender == "boy":
        for bmi_list in boys_percentiles:
            for col, bmi in enumerate(bmi_list):
                if col == 0:
                    months.append(bmi)
                else:
                    bmi_percentiles[col-1].append(bmi)
    else:
        for bmi_list in boys_percentiles:
            for col, bmi in enumerate(bmi_list):
                if col == 0:
                    months.append(bmi)
                else:
                    bmi_percentiles[col-1].append(bmi)

    return months, percentiles[1:], bmi_percentiles


