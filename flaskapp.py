from flask import Flask, render_template, request
from sqlalchemy import create_engine,text
app = Flask(__name__)
db_url = 'mysql+pymysql://root:1234@35.200.222.204:3306/FlaskDemo'
db_engine = create_engine(db_url)

@app.route('/',methods=['GET','POST'])

def home():
    status = ''
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone_number']
        print(name)
        print(phone)
        with db_engine.begin() as conn:
            conn.execute(text('INSERT INTO Contacts (name, phone_number) VALUES (:name,:phone_number);'),{'name':name,'phone_number':phone})
            status = 'Record saved successfully'
    return render_template('contactform.html',result={'status':status})

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)