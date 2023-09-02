'''
Controllers for BMI forms
'''
from browser import document
import bmicalc.bmicalc



def update_bmi_weight(_):
    '''
    Update BMI and BMI percentile when weight changes
    '''
    gender =  document['gender'].value
    age = float(document['age'].value)
    weight = float(document['weight'].value)
    height = float(document['height'].value)
    bmi = bmicalc.bmicalc.calc_bmi(weight, height)
    bmi_percentile = bmicalc.bmicalc.calc_percentile(bmi, gender, age)
    document['bmi'].value = bmi
    document['bmi_percentile'].value = bmi_percentile


def update_weight_from_bmi(_):
    '''
    Update weight when BMI changes
    '''
    gender =  document['gender'].value
    age = float(document['age'].value)
    height = float(document['height'].value)
    bmi = float(document['bmi'].value)
    weight = bmicalc.bmicalc.calc_weight(bmi, height)
    bmi_percentile = bmicalc.bmicalc.calc_percentile(bmi, gender, age)
    document['weight'].value = weight
    document['bmi-percentile'].value = bmi_percentile

