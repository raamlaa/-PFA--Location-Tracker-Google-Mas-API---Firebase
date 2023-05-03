import pyrebase
import serial
import pynmea2

firebaseConfig = {

    "apiKey": "AIzaSyBh84TqjYM2G6vT7Qc71WACE-f9pR4BOGQ",
    "authDomain": "pfa-project-f9a2b.firebaseapp.com",
    " databaseURL": "https://pfa-project-f9a2b-default-rtdb.firebaseio.com",
    " projectId": "pfa-project-f9a2b",
    "storageBucket": "pfa-project-f9a2b.appspot.com",
    " messagingSenderId": "343639216796",
    "appId": "1:343639216796:web:3546af136e784a39e9d359",
    " measurementId": "G-QGHJX77NZB"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()                # database

while True:
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()
    n_data = newdata.decode('latin-1')
    if n_data[0:6] == '$GPRMC':
        newmsg = pynmea2.parse(n_data)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
        print(gps)
        data = {"LAT": lat, "LNG": lng}
        db.update(data)
        print("Data sent")
