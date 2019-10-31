from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import cv2
import tensorflow as tf
import os.path

BASE = os.path.dirname(os.path.abspath(__file__))

CATEGORIES = ["Fat", "Thin"]


def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


# def index(request):
#     print(request.GET['id'])
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    template = loader.get_template('scheduleGenarator\index.html')
    context = {
        'title': "helllldsdsllll",
        'cal': "calll",
    }
    return HttpResponse(template.render(context, request))


def process(request):
    model = tf.keras.models.load_model(os.path.join(BASE, "body-CNN.model"))
    template = loader.get_template('scheduleGenarator\schedule.html')
    imagePath = request.GET['imagePath']
    name = request.GET['name']
    # genderF = request.GET['genderF']
    # genderM = request.GET['genderM']
    height = request.GET['height']
    weight = request.GET['weight']
    bodyFat = request.GET['bodyFat']
    pressure = request.GET['pressure']

    print(name)
    print(height)
    print(weight)
    print(bodyFat)
    print(pressure)

    if (int(pressure) > 100):
        pressureCondition = 'HIGH'
    else:
        pressureCondition = 'LOW'

    data_folder = "D:\\project1\\ProjectFinal\\test_images\\"
    file_to_open = data_folder + imagePath
    print(file_to_open)
    prediction = model.predict([prepare(file_to_open)])
    # prediction = model.predict([prepare(data_folder + '11.jpg')])
    res = CATEGORIES[int(prediction[0][0])]

    if (res == 'Thin'):
        if (int(weight) < 45):
            context = {
                'bodyType': res,
                'name': name,
                'pressureCondition': pressureCondition,
                'running': "10 min",
                'pullover': "4reps 5 sets",
                'front': "6reps 3 sets",
                'back': "6reps 3 sets",
                'bench': "6reps 3 sets",
                'curl': "6reps 3 sets",
                'triceps': "6reps 3 sets",
                'situps': "20reps 3 set",
            }
        else:
            context = {
                'bodyType': res,
                'name': name,
                'pressureCondition': pressureCondition,
                'running': "15 min",
                'pullover': "6reps 4 sets",
                'front': "6reps 4 sets",
                'back': "6reps 4 sets",
                'bench': "8reps 4 sets",
                'curl': "8reps 3 sets",
                'triceps': "6reps 3 sets",
                'sitrunseups': "20reps 3 set",
            }
    else:
        if(int(weight)>100):
            context = {
                'bodyType': res,
                'name': name,
                'pressureCondition': pressureCondition,
                'running': "60 min",
                'pullover': "16rep 4 sets",
                'front': "12reps 4 sets",
                'back': "12reps 4 sets",
                'bench': "10reps 4 sets",
                'curl': "10reps 4 sets",
                'triceps': "12reps 3 sets",
                'situps': "40reps 4 set",
            }
        else:
            context = {
                'bodyType': res,
                'name': name,
                'pressureCondition': pressureCondition,
                'running': "45 min",
                'pullover': "12reps 4 sets",
                'front': "12reps 4 sets",
                'back': "12reps 4 sets",
                'bench': "10reps 4 sets",
                'curl': "8reps 4 sets",
                'triceps': "12reps 3 sets",
                'situps': "30reps 4 set",
            }

    return HttpResponse(template.render(context, request))
