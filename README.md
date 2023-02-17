# Тестовое задание Django + Stripe API бэкенд
***
~~~
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
Django Модель Item с полями (name, description, price) 
API с двумя методами:
    - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

Бонусные задачи выполненные: 
    1. Запуск используя Docker 
    2. Использование environment variables (python-decouple)
    3. Просмотр Django Моделей в Django Admin панели (реализован Inline)
    4. Запуск приложения на удаленном сервере, доступном для тестирования (ссылка на тест сервер ниже)
    5. Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order 
        c общей стоимостью всех Items 
~~~
***

### Шаги для запуска проекта локально с помощью Docker (.env.dev файл для запуска с тестовыми значениями в репозитории):

1. ```docker-compose up -d --build```
2. ```docker-compose exec web python manage.py migrate --noinput```
3. ```docker-compose exec web python manage.py createsuperuser```
4.  Добавить товары и заказы в админке (/admin)

### Протестировать можно по ссылке тестового сервера ```http:/194.67.112.94``` c помощью нижеуказанных URL

## URLS
#### GET /item/<int:pk>/  ---  [http:/194.67.112.94/item/1/](http:/194.67.112.94/item/1/)
#### GET /order/<int:pk>/  ---  [http:/194.67.112.94/order/1/](http:/194.67.112.94/order/1/)
~~~
HTML страница с простым описанием товара (/item) или заказа (/order) и кнопкой для перехода на stripe checkout форму
~~~
#### GET /buy/<int:pk>/  ---  [http:/194.67.112.94/buy/1/](http:/194.67.112.94/buy/1/)
#### GET /buy_order/<int:pk>/  ---  [http:/194.67.112.94/buy_order/1/](http:/194.67.112.94/buy_order/1/)
~~~
JSON response для получения session id конкретного товара (/item) или заказа (/order)
~~~
#### /admin/  ---  [http:/194.67.112.94/admin/](http:/194.67.112.94/admin/)
~~~
логин: admin
пароль: admin
~~~
