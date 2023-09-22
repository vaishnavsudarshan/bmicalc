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
    age = float(document['age-years'].value)*12 + float(document['age-months'].value)
    weight = float(document['weight-lb'].value) + float(document['weight-oz'].value)/16
    height = float(document['height-ft'].value)*12 + float(document['height-in'].value)
    bmi = bmicalc.bmicalc.calc_bmi(weight, height)
    bmi_percentile = bmicalc.bmicalc.calc_percentile(bmi, gender, age)
    document['bmi'].value = f'{bmi:0.2f}'
    document['bmi-percentile'].value = f'{bmi_percentile:0.2f}'


def update_weight_from_bmi(_):
    '''
    Update weight when BMI changes
    '''
    gender = document['gender'].value
    age = float(document['age-years'].value)*12 + float(document['age-months'].value)
    height = float(document['height-ft'].value)*12 + float(document['height-in'].value)
    bmi = float(document['bmi'].value)
    weight = bmicalc.bmicalc.calc_weight(bmi, height)
    bmi_percentile = bmicalc.bmicalc.calc_percentile(bmi, gender, age)
    weight_lb = int(weight)
    weight_oz = 16*(weight - weight_lb)
    document['weight-lb'].value = f'{weight_lb}'
    document['weight-oz'].value = f'{weight_oz:0.2f}'
    document['bmi-percentile'].value = f'{bmi_percentile:0.2f}'


def update_weight_from_bmi_pct(_):
    '''
    Update weight when BMI changes
    '''
    gender = document['gender'].value
    age = float(document['age-years'].value)*12 + float(document['age-months'].value)
    height = float(document['height-ft'].value)*12 + float(document['height-in'].value)
    bmi_percentile = float(document['bmi-percentile'].value)
    bmi = bmicalc.bmicalc.calc_bmi_from_percentile(gender, age, bmi_percentile)
    weight = bmicalc.bmicalc.calc_weight(bmi, height)
    weight_lb = int(weight)
    weight_oz = 16*(weight - weight_lb)

    document['weight-lb'].value = f'{weight_lb}'
    document['weight-oz'].value = f'{weight_oz:0.2f}'

    document['bmi'].value = f'{bmi:0.2f}'
