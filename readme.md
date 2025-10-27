# REST API для электронной библиотеки

## Установка
1. \`python -m venv venv\`
2. Активируйте venv
3. \`pip install -r requirements.txt\`
4. \`python manage.py migrate\`
5. \`python manage.py createsuperuser\`
6. \`python manage.py runserver\`

## Эндпоинты
- \`GET /api/authors/\`
- \`GET /api/books/\`
- \`POST /api/books/create/\` (только админ)