#Импорт
from flask import Flask, render_template, request

app = Flask(__name__)


#Ссылки страниц
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dangers_main')
def dangers_main():
    return render_template('dangers_main.html')

@app.route('/dangers_1')
def dangers_1():
    return render_template('dangers1.html')

@app.route('/dangers_2')
def dangers_2():
    return render_template('dangers2.html')

@app.route('/dangers_3')
def dangers_3():
    return render_template('dangers3.html')

@app.route('/forecast')
def forecast():
    return render_template('forecast.html')

@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    
    #name = request.form['name']
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('feedback')
    with open('form.txt', 'a',) as f:
                f.write(name + '/n')
                f.write(email + '/n')
                f.write(feedback + '/n')
    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                           name=name,
                           email=email,
                           feedback=feedback
                           )
app.run(debug=True)