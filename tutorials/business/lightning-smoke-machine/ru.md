---
name: Lightning Smoke Machine
description: Запуск дымовой машины с помощью платежа Lightning через ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Введение



Превращает классическую дымовую машину в устройство, оплачиваемое в Bitcoin через Lightning Network. Каждый платеж автоматически запускает струю дыма!





- Уровень: Intermediate
- Расчетное время: 2-3 часа
- Примеры использования: Мероприятия Bitcoin, художественные выступления, демонстрация молний, автоматизированные сценические эффекты



## Пререквизиты



### Знания





 - Основы электроники (проводка, реле)
 - Сварка (или использование соединителей Dupont)
 - Настройка сети (WiFi, WebSocket)



### Необходимые счета





- Сервер BTCPay: Функциональный экземпляр (самостоятельный или размещенный)
- Blink Wallet : Учетная запись + доступ API



### Доступ





- Доступ администратора к серверу BTCPay
- WiFi соединение для ESP32



## Необходимые материалы



### Оборудование - Электронные компоненты





- 1 Микроконтроллер - ESP32-WROOM-32


*ESP32-WROOM-32 - это компактный, недорогой микроконтроллер с WiFi/Bluetooth для подключения электронных устройств к Интернету и удаленного управления ими*



![ESP32](assets/fr/1.webp)





- 1 Релейный модуль - 5 В с оптопарой


*Реле - это как переключатель, которым ESP32 может управлять, чтобы включить или выключить дымовую машину*



![relay](assets/fr/2.webp)





- ~10 кабелей Dupont - мужской/мужской и мужской/женский



![dupont-cables](assets/fr/3.webp)





- 1 Источник питания для ESP32 - 5 В USB или литий-полимерный аккумулятор



![battery](assets/fr/4.webp)





- 1 кабель micro-USB - соединение между ESP32 и источником питания



![micro-usb-cables](assets/fr/5.webp)





- 1 туманная машина 220 В с пультом дистанционного управления на батарейках 12 В



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 бутылка жидкости, совместимой с вашей дымовой машиной



### Оборудование - Инструменты





- Паяльник + олово (если паяете)
- Отвертка
- Мультиметр (рекомендуется)



### Программное обеспечение





- Прошивка BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Веб-браузер, совместимый с WebSerial (Chrome/Edge/Brave)
- Сервер BTCPay Server настроен. Для получения дополнительной информации о создании экземпляра BTCPay Server посетите этот учебник: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Архитектура системы



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ - ПРОЧИТАЙТЕ ПЕРЕД ПРОДОЛЖЕНИЕМ** **⚠️**



В этом проекте используется туманная машина, подключенная к сети **220 В**. Неправильная эксплуатация может привести к **смертельному поражению электрическим током** или **пожару**.



**Не обсуждаемые правила:*



1. **ВСЕГДА отключайте дым-машину от сети**, прежде чем открывать пульт дистанционного управления или вмешиваться в проводку


2. **Извлеките батарею из пульта дистанционного управления** перед началом работы (риск короткого замыкания и повреждения компонентов)


3. **Убедитесь, что все соединения изолированы**, прежде чем снова что-то подключать


4. **Никогда не подключайте 220 В**, пока не закроете и не закрепите блок дистанционного управления



Если вы не умеете обращаться с такими вещами, возьмите с собой кого-нибудь, кто умеет это делать.



---

## ЧАСТЬ 1: Сборка оборудования



### Шаг 1: Подготовка пульта дистанционного управления



Цель: Подключите реле к кнопке ON/OFF на пульте дистанционного управления


1. Открыть пульт дистанционного управления




    - Идентификация кнопки включения/выключения
    - Открутите корпус, чтобы открыть пульт дистанционного управления


2. Найдите соединения




 - Найдите + и - клеммы
 - Проверьте целостность с помощью мультиметра (опционально)



![smoke-machine-remote](assets/fr/8.webp)



3. Проводка кнопок (пайка или разъемы)




    - Припаяйте черный провод к - клемме кнопки
    - Припаяйте красный кабель к общей клемме +



![smoke-machine-remote](assets/fr/9.webp)



### Шаг 2: Подключение к релейному модулю



**Напоминание: Терминология реле



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

** Проводка от пульта дистанционного управления к релейному модулю:**




- Черный провод от кнопки ON/OFF **→** NO (нормально разомкнутый)
- Красный провод (общий) **→** COM (общий)



**Логика:**


Когда ESP32 активирует реле, он соединяет COM и NO, что в точности соответствует нажатию кнопки пульта дистанционного управления.


Когда ESP32 отключает реле, COM и NO разделяются, что эквивалентно отпусканию кнопки.



![remote-relay](assets/fr/10.webp)



### Шаг 3: Подключение ESP32 к релейному модулю



** Схема подключения:*



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

** Проверка:*




- VCC и GND хорошо соединены (полярность)
- GPIO 21 используется для управляющего сигнала
- Отсутствие видимого короткого замыкания



![relay-esp32](assets/fr/11.webp)



**Контрольная точка аппаратуры**


Перед переключением на программное обеспечение проверьте :




- Правильно подключенный пульт дистанционного управления
- Релейный модуль, подключенный к ESP32
- Отсутствие оголенных проводов, касающихся других компонентов
- 220 В всегда отключено



![relay-esp32](assets/fr/12.webp)





---


## ЧАСТЬ 2: Конфигурация программного обеспечения



Мы будем использовать *Blink* в качестве примера, но *BTCPay Server* также предлагает *Strike, Breez и Boltz*, если вы предпочитаете другой вариант.



### Шаг 1: Плагины, установка *BitcoinSwitch* + *Blink



1 - Зайдите на свой экземпляр *BTCPay Server* под учетной записью администратора



2 - Создайте свою первую слепую



3 - На левой стороне *BTCPay Server* прокрутите страницу в самый низ и перейдите к разделу *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Мы собираемся установить плагины *BitcoinSwitch*, а также *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Прокрутите список плагинов вниз и нажмите на *"Установить "* : *BitcoinSwitch и Blink* (или доступный wallet по вашему выбору)



![btcpay-plugins](assets/fr/15.webp)



6 - После завершения установки перезапустите *BTCPay Server* и подождите 1 минуту, пока экземпляр не перезапустится



![btcpay-plugins](assets/fr/16.webp)



7 - Когда вы вернетесь в *"Управление плагинами "*, проверьте, что оба плагина были установлены



![btcpay-plugins](assets/fr/17.webp)



### Шаг 2: Бэкэнд: *Сервер BTCPay + конфигурация Blink*



**1 - Создание wallet *Blink***




- Посетите https://www.blink.sv
- Создайте свою учетную запись. Обратитесь к учебнику :



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Сгенерируйте ключ API *Blink***




- Зайдите в интерфейс API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** и войдите в систему под той же учетной записью, которую вы использовали для создания wallet *Blink*



![blink-api](assets/fr/18.webp)





   - После подключения перейдите на вкладку *API Keys*



![blink-api](assets/fr/19.webp)





   - Нажмите на *" + "* в правом верхнем углу, чтобы получить доступ к конфигурации ключа API



![blink-api](assets/fr/20.webp)





   - Дайте ключу API имя и оставьте настройки по умолчанию. Затем, на третьем шаге, запишите свой ключ API - вы увидите его только один раз: `blink_mZ5KxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - После создания он должен появиться в списке активных ключей API.



![blink-api](assets/fr/22.webp)



**3 - Подключите *Blink* к *BTCPay Server***




- Откройте свой *сервер BTCPay*
- Перейдите по ссылке : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Нажмите на *Использовать пользовательский узел*
- Вставьте следующую строку подключения:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Важно** :




- Не изменяйте первую часть: `type=blink;server=https://api.blink.sv/graphql`;
- Заменяйте только :
    - api-key= *по вашему ключу API Blink*
    - wallet-id= *по вашему идентификатору wallet Blink*
- Затем нажмите *Тестировать соединение*, затем *Сохранить*



![btcpay-server](assets/fr/24.webp)





 - Убедитесь, что соединение установлено (зеленый цвет)



![btcpay-server](assets/fr/25.webp)



**4 - Создание торговой точки (PoS)**




- В BTCPay Server перейдите на вкладку *Плагины* и нажмите на *Точка продажи*



![btcpay-server](assets/fr/26.webp)





- Дайте вашей PoS имя и нажмите на кнопку *Создать*



![btcpay-server](assets/fr/27.webp)





- Конфигурация PoS :
    - Выберите стиль торговой точки = *Печатная витрина*
    - Валюта = *SATS*
    - Нажмите на *Сохранить*



![btcpay-server](assets/fr/28.webp)





- Конфигурация продукта :
    - Удалите все продукты по умолчанию
    - Затем нажмите на кнопку *Добавить элемент*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Настройте продукт:
    - Название : *дымовая машина*
    - Цена : *10 sats*
    - Bitcoin Переключатель GPIO : 21
    - Bitcoin Продолжительность переключения (в миллисекундах) : 5000
    - Нажмите *Закрыть*, а затем *Сохранить*, чтобы сохранить новый продукт



![btcpay-server](assets/fr/31.webp)



### Шаг 3: Прошивка: Прошивка ESP32



**1 - Перейти на сайт флэш-памяти




- Перейти к : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash прошивка BitcoinSwitch**




- Подключите ESP32 к компьютеру с помощью кабеля USB/Micro-USB
- Затем нажмите *Подключиться к устройству*
- Откроется окно, выберите USB-порт на вашем ESP32, затем нажмите *Подключить*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- После подключения ESP32 мы прошьем прошивку BitcoinSwitch. В разделе *T-Display* нажмите на *Upload Firmware* для последней доступной версии (в настоящее время: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Дождитесь загрузки, процесс будет завершен, когда в журнале появится сообщение *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Отключите ESP32 от сети



**3 - Проверка установки прошивки BitcoinSwitch




- Перезагрузить страницу: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Подключите ESP32 к компьютеру с помощью кабеля USB/Micro-USB
- Затем нажмите *Подключиться к устройству
- Выберите порт USB на вашем ESP32, затем нажмите *Подключить*, как описано выше
- После подключения нажмите кнопку **RESET** на ESP32
- Проверьте в журналах, что последние строки показывают :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Это нормально, это означает, что конфигурации еще нет, но прошивка уже установлена)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Генерация URL-адреса WebSocket LNURL**



Ожидаемый окончательный формат:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Шаги генерации :




- Откройте свой экземпляр сервераBTCPay, затем перейдите к PoS, который мы создали позже.
- Затем нажмите "Просмотр", чтобы открыть PoS в браузере



![btcpay-server-https](assets/fr/37.webp)





- Скопируйте URL-адрес страницы, например :



![btcpay-server-https](assets/fr/38.webp)



Давайте распакуем этот URL:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → домен вашего экземпляра сервера BTCPay Server
- `46XXXXXXXXXXXXXXXXXXXXwFB` → ваш уникальный идентификатор PoS
- `/pos` → указывает на торговую точку



Преобразуйте его:




- Замените `https://` на `wss://`
- Добавьте `/bitcoinswitch` в конце



Результат:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Сохраните этот URL для будущей настройки, так как он позволит вашему ESP32 общаться с сервером BTCPay в режиме реального времени. Протокол WebSocket (`wss://`) устанавливает постоянное соединение между ними: как только платеж Lightning подтверждается на вашем PoS, BTCPay мгновенно отправляет информацию на ESP32, который затем может запустить вашу дым-машину.



**5 - Настройка WiFi и WebSocket




- Возврат к странице: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) с подключенным ESP32
- Перейдите в раздел *Конфигурация устройства* → *Настройки Wi-Fi*



Информировать :




- WiFi SSID: название вашей сети WiFi
- Пароль WiFi: ваш пароль WiFi



![bitcoinswitch-lnbits](assets/fr/39.webp)





- В разделе *LNbits Device URL* вставьте URL WebSocket, созданный на предыдущем шаге
- Нажмите на *Загрузить конфигурацию*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Дождитесь завершения загрузки; в журнале должны отобразиться параметры, которые вы только что ввели (SSID, пароль и URL WebSocket)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Подождите, пока ESP32 установит соединение WebSocket. Вы должны увидеть :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Теперь вы можете отключить ESP32



---
## Программное обеспечение Checkpoint



Перед окончательным испытанием проверьте :





- Blink подключился к BTCPay
- PoS, созданный как минимум из 1 предмета
- ESP32, прошитый с помощью BitcoinSwitch
- Настройка WiFi на ESP32
- Правильный URL-адрес WebSocket
- Журналы ESP32 без ошибок



---

## Тестирование и отладка



### Завершите финальный тест



1. Подключите дымогенератор (220 В) и включите его


2. Питание ESP32 (от батареи или USB)


3. Откройте свой PoS BTCPay в браузере


4. Сканировать элемент "Дымовая машина"


5. Оплатить wallet Lightning (Blink или другой wallet)


6. Наблюдайте:




 - Реле щелкает (раздается звуковой сигнал и загорается светодиод реле)
 - Дымовая машина активирована
 - Дым!



### Проблемы и решения, связанные со справедливостью



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Ресурсы



### Полезные ссылки





- Прошивка BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Документация по серверу BTCPay : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- Распиновка ESP32 : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Сообщество и поддержка





- Сервер BTCPay** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Официальный Mattermost
- Сервер BTCPay Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Официальный Telegram, активное сообщество
- BitcoinSwitch (ошибки в прошивке)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Исходный код





- Исходный код прошивки BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Складывайте sats, делайте дым, веселитесь, оставайтесь скромными! **⚡**