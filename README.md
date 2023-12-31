# Описание решения

### 1. Запуск

В качестве обертки для модели я написал телеграм-бота (@tins_sirius_sns_bot) и создал простое web-приложение с помощью фреймворка ```streamlit```

***0) Для начала:***

   ```git clone https://github.com/elderberry17/tink-sirius-test.git```
    
   ```cd tink-sirius-test```

***1) Запуск бота:***
   
   ```docker build -t tink_sns_bot -f Dockerfile.bot .```
   
   ```docker run tink_sns_bot```

***2) Запуск веб-приложения:***

   ```docker build -t tink_sns_web -f Dockerfile.web .```
   
   ```docker run tink_sns_web```

### 2. Эксперименты
   
В процессе дообучения я использовал данный google colab:
https://clck.ru/35XhGD

Я пробовал дообучать модель на разных данных: переписках с друзьями, учебных чатах, чатах профессиональных коммьюнити.
В итоге я остановился на 3-х вариантах, в раз захостил несколько версий бота с помощью сервиса ```beget``` (https://beget.com/ru) и устроил тестирование с помощью друзей.

Результаты тестирования приведены в таблице ниже:

https://clck.ru/35Xh72

Я постарался выбрать самого достойного бота также учитывая статистику опроса подписчиков в своем небольшом телеграм-канале (сейчас он закрыт, так что данные дать не могу), мнение людей в среднем совпадало с точечным мнением трех тестировщиков)

Победила модель, обученная на данных известного чата о стажировках (https://t.me/sns_internships). В среднем она выдает наиболее осмысленные и интеллектуальные беседы.
