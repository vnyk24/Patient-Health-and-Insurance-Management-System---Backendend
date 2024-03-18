from django.shortcuts import render
import pyrebase


config = {
  "apiKey": "AIzaSyA5sXeXvH-gq7B3qrTXII6nLN5-dAkwOo8",
  "authDomain": "group20-backend.firebaseapp.com",
  "projectId": "group20-backend",
  "storageBucket": "group20-backend.appspot.com",
  "messagingSenderId": "14221723934",
  "appId": "1:14221723934:web:5c0f8ec1e889dd17ffa10f",
  "measurementId": "G-L4HBX84CNL",
  "databaseURL": "firebase",
}
firebase = pyrebase.initialize_app(config)

auth  = firebase.auth()

def signIn(request):
    return render(request,"signIn.html")

def postSign(request):
    return render(request,"home.html")


