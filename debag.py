import smtplib

import os

from dotenv import load_dotenv

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


advertisement = '''{0}

Привет, {1}! {2} приглашает тебя на сайт {3}!

{3} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {3}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {3}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

friend_name = 'Бро'

website = 'https://dvmn.org/profession-ref-program/kalyayo7/Cv1gt/'

my_name = 'Великолепный программист и продавец - Аким'

letter = '''From: paulinachipolino@yandex.ru
To: paulinachipolino@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";'''




email_from = 'paulinachipolino@yandex.ru'
email_to = 'paulinachipolino@yandex.ru'



server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(email_from, email_to, advertisement.format(letter, friend_name, my_name, website).encode("UTF-8"))
server.quit()




