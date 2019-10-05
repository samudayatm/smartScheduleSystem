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
    data_folder = "D:\\project1\\ProjectFinal\\test_images\\"
    file_to_open = data_folder + imagePath
    print(file_to_open)
    prediction = model.predict([prepare(file_to_open)])
    # prediction = model.predict([prepare(data_folder + '11.jpg')])
    res = CATEGORIES[int(prediction[0][0])]

    context = {
        'status': res,
    }
    return HttpResponse(template.render(context, request))
