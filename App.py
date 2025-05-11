from flask import Flask, render_template, flash, request, session, send_file
from flask import render_template, redirect, url_for, request
import os
import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('Prediction.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Parkinsondb')

    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()

    return render_template('AdminHome.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['Password'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Parkinsondb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb")
            data = cur.fetchall()

            return render_template('AdminHome.html', data=data)
        else:
            flash("UserName or Password Incorrect!")

            return render_template('AdminLogin.html')


@app.route("/Prediction")
def Prediction():
    return render_template('Prediction.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']

        age = request.form['age']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        Password = request.form['Password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Parkinsondb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' ")
        data = cursor.fetchone()
        if data is None:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Parkinsondb')
            cursor = conn.cursor()
            cursor.execute(
                "insert into regtb values('','" + name + "','" + age + "','" + mobile + "','" + email + "','" + address + "','" +
                username + "','" + Password + "')")
            conn.commit()
            conn.close()
            return render_template('UserLogin.html')



        else:
            flash('Already Register Username')
            return render_template('NewUser.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['Password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Parkinsondb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')

        else:
            return render_template('Prediction.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        import tensorflow as tf
        import numpy as np
        import cv2
        from keras.preprocessing import image
        file = request.files['file']
        file.save('static/upload/Test.png')
        org1 = 'static/upload/Test.png'

        img1 = cv2.imread('static/upload/Test.png')

        dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
        # cv2.imshow("Nosie Removal", dst)
        noi = 'static/upload/noi.png'

        cv2.imwrite(noi, dst)

        import warnings
        warnings.filterwarnings('ignore')

        classifierLoad = tf.keras.models.load_model('pdmodel.h5')
        test_image = image.load_img('static/upload/Test.png', target_size=(200, 200))
        test_image = np.expand_dims(test_image, axis=0)
        result = classifierLoad.predict(test_image)
        print(result)

        ind = np.argmax(result)

        out = ''
        if ind == 0:
            print("Healthy")
            out = "Healthy"
            fer = "Nil"
        elif ind == 1:
            print("Parkinson")
            out = "Parkinson"
            fer = "The most common medication for Parkinson's disease, levodopa is converted into dopamine in the brain to treat symptoms like stiffness, tremors, and slowness of movement. Levodopa is often taken with carbidopa, which reduces side effects like nausea and vomiting."

        else:
            out = "Nil"
            fer = "Nil"

        return render_template('Result.html', result=out, org=org1, noi=noi, fer=fer)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
