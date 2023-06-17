Для запусков тестирования необходимо установить зависимые библиотеки

pip install -r requirements.txt

Запустить тесты

pytest test_API.py

Собрать Docker образ

docker build -t pytest_runner .

Запустить контейнер

docker run pytest_runner  
