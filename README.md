# Django Celery

Простое джанго веб приложение для тестирования асинхронных задач.

Приложение построено на Django 4 + Docker, Celery, Redis, Flower

1. На http://localhost:8000 выводится форма для отправки email-а. 

![Screenshot_1](/screenshots/Screenshot_1.png)

2. После отправки - страница "Спасибо".

![Screenshot_2](/screenshots/Screenshot_2.png)

3. Отправка самого письма происходит в асинхронной задаче.

![Screenshot_3](/screenshots/Screenshot_3.png)

4. В приложении Flower наблюдаем отработанную задачу.

![Screenshot_4](/screenshots/Screenshot_4.png)
