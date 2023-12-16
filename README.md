## Запуск проекта 

 - Склонируйте репозиторий в папку проекта https://github.com/ArtyomBatmanov/Django-shop
 - Установите необходимые библиотеки командой "pip install -r requirements.txt"
 - Собрать пакет: в директории diploma-frontend выполнить команду python setup.py sdist
 - Перейти в директорию diploma-frontend/dist. Установить полученный пакет в виртуальное окружение: pip install diploma-frontend-0.6.tar.gz. 
 - Создайте миграции командой python manage.py makemigrations
 - Затем выполните команду python manage.py migrate
 - Установите фикстуры в базу данных командой python loaddata fixtures/fixtures.json
    Админ: 
        логин: admin
        пароль: admin
    Пользователь:
        логин: testuser
        пароль: 123456
 - В директории megano выполните команду python manage.py runserver
