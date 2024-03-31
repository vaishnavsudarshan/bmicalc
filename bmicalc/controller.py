'''
Controllers for BMI forms
'''
from browser import document, window
import bmicalc.bmicalc
Plotly = window.Plotly

def update_bmi_classification(bmi_percentile):
    if bmi_percentile < 5:
        document['bmi-classification'].text = 'Underweight'
        document['bmi-classification'].attrs['class'] = 'input-group-text bg-danger text-white'
    elif 5 <= bmi_percentile < 85:
        document['bmi-classification'].text = 'Normal'
        document['bmi-classification'].attrs['class'] = 'input-group-text bg-light text-dark'
    elif 85 <= bmi_percentile < 95:
        document['bmi-classification'].text = 'Overweight'
        document['bmi-classification'].attrs['class'] = 'input-group-text bg-warning text-dark'
    else:
        document['bmi-classification'].text = 'Obese'
        document['bmi-classification'].attrs['class'] = 'input-group-text bg-danger text-white'

def update_growth_chart(age, bmi):
    print(f'Updating growth chart: {document["bmi-plot"]=}, {age=}, {bmi=}')
    Plotly.restyle("bmi-plot", {"x": [[age]], "y": [[bmi]]}, [0])


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
    update_bmi_classification(bmi_percentile)
    update_growth_chart(age, bmi)

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
    update_bmi_classification(bmi_percentile)
    update_growth_chart(age, bmi)


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
    update_bmi_classification(bmi_percentile)
    update_growth_chart(age, bmi)


def make_plot():
  months, percentiles, bmi_percentiles = bmicalc.bmicalc.get_bmi_percentiles(document['gender'].value)
  data = []
  for percentile, bmi_percentile in zip(percentiles, bmi_percentiles):
      data.append({"x": months, "y": bmi_percentile, "type": "scatter", "mode": "lines",  "name": "P %2d"%percentile})
  
  age = float(document['age-years'].value)*12 + float(document['age-months'].value)
  bmi = float(document['bmi'].value)
  data.append({"x": [age], "y": [bmi], "type": "scatter", "mode": "markers", "marker": {"size":15}, "name": "Your BMI"})

  layout = {"title": f"BMI distribution for {document['gender'].value}s", "xaxis": {"title": "Months"}, "yaxis": {"title": "BMI"}}
  Plotly.newPlot('bmi-plot', data[::-1], layout)

def redraw_plot(_):
    make_plot()
  