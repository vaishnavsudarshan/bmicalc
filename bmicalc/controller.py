'''
Controllers for BMI forms
'''
from browser import document
import bmicalc.bmicalc


def update_bmi(_):
    '''
    Update BMI and BMI percentile when weight changes
    '''
    gender = document['gender'].value
    age = float(document['age'].value)
    weight = float(document['weight'].value)
    height = float(document['height'].value)
    bmi = bmicalc.bmicalc.calc_bmi(weight, height)
    bmi_percentile = bmicalc.bmicalc.calc_percentile(bmi, gender, age)
    document['bmi'].value = f'{bmi:0.2f}'
    document['bmi-percentile'].value = f'{bmi_percentile:0.2f}'


def update_weight_from_bmi(_):
    '''
    Update weight when BMI changes
    '''
    gender = document['gender'].value
    age = float(document['age'].value)
    height = float(document['height'].value)
    bmi = float(document['bmi'].value)
    weight = bmicalc.bmicalc.calc_weight(bmi, height)
    bmi_percentile = bmicalc.bmicalc.calc_percentile(bmi, gender, age)
    document['weight'].value = f'{weight:0.2f}'
    document['bmi-percentile'].value = f'{bmi_percentile:0.2f}'


def update_weight_from_bmi_pct(_):
    '''
    Update weight when BMI changes
    '''
    gender = document['gender'].value
    age = float(document['age'].value)
    height = float(document['height'].value)
    bmi_percentile = float(document['bmi-percentile'].value)
    bmi = bmicalc.bmicalc.calc_bmi_from_percentile(gender, age, bmi_percentile)
    weight = bmicalc.bmicalc.calc_weight(bmi, height)

    document['weight'].value = f'{weight:0.2f}'
    document['bmi'].value = f'{bmi:0.2f}'
