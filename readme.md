1. Убедитесь, что на машине установлен Python и pip. В терминале введите:

    python --version
    pip --version

Если не установлены, скачать и установить с https://www.python.org/downloads/


2. Скачайте проект 

    cd путь/к/папке/с/проектами
    git clone https://github.com/nestor-alexxx/gen-csv-upload-to-db.git


3. Перейдите в каталог проекта, создайте виртуальное окружение и активируйте его:

    cd путь/к/проекту
    python -m venv venv
    .\venv\Scripts\activate


4. Установите зависимости из файла requirements.txt:

    pip install -r requirements.txt


5. Откройте планировщик задач и нажмите "Создать задачу". Дайте любое удобное имя, добавьте триггер с параметром "Еженедельно", выделив все дни, кроме воскресенья, установив подходящее время. Затем добавьте действие, выбрав файл "data-generator.py". Сохраните. 
Аналогично сделайте для файла "upload-to-db.py". Время установите спустя не менее нескольких минут после выполнения файла "data-generator.py".