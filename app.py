import os
from flask import Flask, render_template

app = Flask(__name__)

def index():
    return render_template('index.html')

def downloadMem():
    return render_template('MemDownload.html')

def downloadFarm():
    return render_template('farmdowload.html')

def ArticleCuwd():
    return render_template('abadonedProject.html')

def downloadTefteli():
    return render_template('tefteliDownload.html')

def downloadSnake():
    return render_template('BountyhunterDownload.html')

def downloadBoat3d():
    return render_template('Boat3dDownload.html')

def downloadAnalytic():
    return render_template('AnalyticDwonload.html')


folder = os.getcwd() # запам'ятали поточну робочу папку
# Створюємо об'єкт веб-програми:
app = Flask(__name__, template_folder=folder, static_folder=folder) # перший параметр - ім'я модуля
                            # параметр з ім'ям static_folder визначає ім'я папки, що містить статичні файли
                            # параметр з ім'ям template_folder визначає ім'я папки, що містить шаблони



# Маршруты
app.add_url_rule('/', 'index', index)
app.add_url_rule('/index.html', 'index', index)
app.add_url_rule('/download', 'downloadMem', downloadMem)
app.add_url_rule('/download2', 'farmdownload', downloadFarm)
app.add_url_rule('/article', 'abadonedProject', ArticleCuwd)
app.add_url_rule('/download3', 'tefteliDownload', downloadTefteli)
app.add_url_rule('/download4', 'BountyhunterDownload', downloadSnake)
app.add_url_rule('/download5', 'Boat3dDownload', downloadBoat3d)
app.add_url_rule('/download6', 'AnalyticDwonload', downloadAnalytic)

if __name__ == '__main__':
    app.run(debug=True)

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)
