from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import mysql.connector
from django.http import HttpResponseRedirect

def index(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="sss"
    )

    mycursor = mydb.cursor()
    print(mydb)

    imagePath = request.GET['imagePath']
    name = request.GET['name']
    nic = request.GET['nic']
    gender = request.GET['gender']
    height = request.GET['height']
    weight = request.GET['weight']
    bodyFat = request.GET['bodyFat']
    pressure = request.GET['pressure']
    phoneNum = request.GET['phoneNum']
    email = request.GET['email']

    sql = "INSERT INTO `biodata` (`nic`, `name`, `gender`, `height`, `email`, `phone`,`weight`,`bodyFat`,`pressure`,`imagePath`)  VALUES (%s,%s, %s,%s, %s,%s, %s, %s,%s, %s)"
    val = (nic,name,gender,height,email,phoneNum,weight,bodyFat,pressure,imagePath)
    mycursor.execute(sql, val)

    mydb.commit()
    return HttpResponseRedirect("/schedule");