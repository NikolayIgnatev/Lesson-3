import os
import smtplib
from dotenv import load_dotenv


load_dotenv()
email_from = "Nikolay12090@mail.ru"
email_to = "Nikolay12090@mail.ru"
name = "Николай"
friend_name = "Петр"
devman_link = "https://dvmn.org/referrals/JTphOoDMoLLWqJ1cB41YyfQioPOJ2Uj3h2FUDQK1/"
message = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
message = message.replace ('%friend_name%',friend_name)
message = message.replace ('%my_name%',name)
message = message.replace ('%website%',devman_link)
letter = """From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

{message}
""".format(email_from = email_from, email_to = email_to, message  = message)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login("Nikolay12090@mail.ru","jCV9jXhrtGpS4H4fS402")
server.sendmail(email_from, email_to, letter)
server.quit()

password = os.getenv("password")
login = os.getenv("login")
