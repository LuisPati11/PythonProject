from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'task4', 'templates')

app=Flask(__name__, template_folder = template_dir)

@app.route('/')
def home():
    search_keyword = request.args.get('search')
    cursor = db.database.cursor()
    if search_keyword:
        cursor.execute("SELECT * FROM salaries WHERE employer_name LIKE %s", ('%' + search_keyword + '%',))
    else:
        cursor.execute("SELECT * FROM salaries")
    
    myresult=cursor.fetchall()

    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
          
    return render_template('index.html', data=insertObject)

@app.route('/job',methods=['POST'])
def addJob():
    employer_name = request.form['employer_name']
    location_name = request.form['location_name']
    job_title = request.form['job_title']
    annual_base_pay = request.form['annual_base_pay']

    if employer_name and location_name and job_title and annual_base_pay:
        cursor= db.database.cursor()
        sql= "INSERT INTO salaries (employer_name, location_name, job_title, annual_base_pay) VALUES (%s, %s, %s, %s)"
        data= (employer_name, location_name, job_title, annual_base_pay)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM salaries WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    employer_name = request.form['employer_name']
    location_name = request.form['location_name']
    job_title = request.form['job_title']
    annual_base_pay = request.form['annual_base_pay']

    if employer_name and location_name and job_title and annual_base_pay:
        cursor = db.database.cursor()
        sql = "UPDATE salaries SET employer_name = %s, location_name = %s, job_title = %s, annual_base_pay = %s WHERE id = %s"
        data = (employer_name, location_name, job_title,annual_base_pay, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True,port=4000)
