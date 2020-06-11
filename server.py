from flask import Flask, render_template, request
import os
#from werkzeug import secure_filename
from pymysql import connect

app = Flask(__name__)

def dbconnect(sql):
    result = []
    db = connect(host='remotemysql.com', database='qTmJH8lRK0', user='qTmJH8lRK0', password='74MQEDNu42')
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    for i in cursor.fetchall():
        result.append(i)
    cursor.close()
    return result

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/tryit')
def form():
    return render_template('form.html')

@app.route('/faculty',methods = ['POST', 'GET'])
def faculty():
    if request.method == 'POST':
        res = request.form
        image = request.files['pic']
        print(image.filename)
        file = image.filename
        image.save(os.path.join(app.root_path, 'static/faculty/' + file))
        print(res)
        temp = 0
        try:
            print(res['optradio1'])
            temp = 1
        except:
            temp = 2
        print(temp)    
        name = res['name']
        designation = res['designation']
        college = res['collge']
        phone = res['phone']
        addr = res['address']
        email = res['email']
        bio = res['bio']
        interests = res['intrests'].split(',')
        work = res['work'].split(',')
        edu = res['edu'].split(',')
        teaching = res['teaching'].split(',')
        pub = res['publications'].split('|')
        print(name)
        print(designation)
        print(college)
        print(phone)
        print(addr)
        print(email)
        print(bio)
        print(interests)
        print(work)
        print(edu)
        print(teaching)
        print(pub)
        print(file)
        lenwork  = int((len(work))/2)
        lenedu = int((len(edu))/2)
        lenteach = int((len(teaching)))
        lenpub = int((len(pub)))
        sql = "select count(id) from faculty"
        res = dbconnect(sql)
        print(res)
        idf = res[0][0] + 1
        sql = "insert into faculty(id,name,designation,college,picture) values({0},'{1}','{2}','{3}','{4}')".format(idf,name, designation, college,file)
        res = dbconnect(sql)
    if temp == 1:
        return render_template('jk.html',name = name,phone = phone,addr = addr,email=email,bio = bio,interests = interests,work = work,edu = edu,teaching = teaching,pub = pub,file = file,lenwork = lenwork,lenedu = lenedu,lenteach = lenteach,lenpub = lenpub,designation = designation,college = college)
    else:
        return render_template('jk2.html',name = name,phone = phone,addr = addr,email=email,bio = bio,interests = interests,work = work,edu = edu,teaching = teaching,pub = pub,file = file,lenwork = lenwork,lenedu = lenedu,lenteach = lenteach,lenpub = lenpub,designation = designation,college = college)

@app.route('/clients')
def clients():
    sql = "select * from faculty"
    res = dbconnect(sql)
    print(res)
    return render_template('client.html',res=res)

@app.route('/contact')
def contact():
    return render_template('team.html')

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)