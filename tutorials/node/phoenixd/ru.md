---
name: Phoenixd
description: Развертывание собственного минимального узла Lightning с помощью Phoenixd
---

![cover](assets/cover.webp)



Финансовая автономия также означает контроль над инфраструктурой Lightning. Для разработчиков и компаний, желающих интегрировать Bitcoin Lightning в свои приложения, **Phoenixd** представляет собой идеальное решение: минималистичный, специализированный узел Lightning с автоматическим управлением ликвидностью.



Phoenixd - это сервер Lightning, разработанный компанией ACINQ и предназначенный специально для отправки и получения платежей Lightning через HTTP API. В отличие от полнофункциональных реализаций, таких как LND или Core Lightning, Phoenixd абстрагирует всю сложность управления каналами, сохраняя при этом самозащиту ваших средств.



В этом руководстве мы рассмотрим, как установить, настроить и использовать Phoenixd для разработки приложений Lightning с самостоятельной инфраструктурой и простым в использовании API.



## Что такое Phoenixd?



Phoenixd - это минимальная специализированная нода Lightning, разработанная компанией ACINQ. Это решение, предназначенное для разработчиков и предприятий, желающих интегрировать Lightning в свои приложения без сложностей управления Full node.



### Принцип работы



**Phoenixd - это минимальный узел Lightning, который использует ACINQ в качестве LSP (Lightning Service Provider) для автоматической ликвидности. Когда вы получаете платежи Lightning, он автоматически открывает каналы с узлами ACINQ для выделения необходимой входящей мощности. Эта ликвидность "на лету" возникает мгновенно, но оплачивается ровно **1% + комиссия Mining** от полученной суммы.



**Автоматизированное управление:** Система управляет тремя ключевыми Elements:




- Каналы Lightning**: Открывайте, закрывайте и управляйте ими автоматически по мере необходимости
- Входящая/исходящая ликвидность**: Автоматическое обеспечение за счет сращивания и открытия каналов
- Комиссионный кредит** : Небольшие платежи, недостаточные для обоснования канала, сохраняются в качестве резерва для будущих платежей



### Преимущества Phoenixd



**Вы сами контролируете свои приватные ключи (12-словные seed) и средства. Phoenixd генерирует ваши Wallet локально, никогда не предоставляя ключи в общий доступ.



**Личная инфраструктура:** Phoenixd работает на вашем сервере, предоставляя вам доступ к подробным журналам, настройке и управлению API. Вы больше не зависите от сторонних сервисов для получения доступа к своим средствам.



**Интегрированный API:** Phoenixd имеет HTTP API для интеграции с другими сервисами, встроенной поддержки LNURL и разработки собственных приложений.



**Простота интеграции:** Благодаря простому REST API Phoenixd можно интегрировать в любое приложение или сервис, требующий платежей Lightning.



**Важное примечание:** Автоматическая ликвидность по-прежнему поступает от ACINQ как LSP (Lightning Service Provider). Phoenixd использует тот же механизм, что и Phoenix mobile для автоматического управления каналами.



## Установка Phoenixd



### Пререквизиты



Для работы Phoenixd требуется среда Linux (рекомендуется Ubuntu/Debian), а также базовые навыки работы с командной строкой. Для оптимальной производительности вам понадобится :





- Сервер Linux**: VPS или локальная машина со стабильным соединением
- OpenJDK 21** : Среда выполнения Java
- Стабильное подключение к Интернету**: Для синхронизации с Lightning Network
- Доменное имя** (необязательно) : Для безопасного HTTPS-доступа к API



### Загрузка и установка



**1. Скачать Phoenixd**



Перейдите на страницу [GitHub releases](https://github.com/ACINQ/phoenixd/releases) и загрузите последнюю версию для вашей архитектуры:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Первый запуск



Запустите Phoenixd для инициализации:



```bash
./phoenixd
```



При первом запуске вам будет предложено подтвердить два важных шага, набрав "I understand":



**Сообщение 1 - Резервное копирование:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Сохраните эти 12 слов** - это единственная гарантия вашего выздоровления.



**Сообщение 2 - Автоматическая ликвидность:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Введите `I understand` для каждого подтверждения.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd запускается в первый раз: резервные подтверждения и автоматическая ликвидность*



**3. Конфигурация в процессе эксплуатации** (только на французском языке)



Для непрерывной работы создайте systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Сервис Phoenixd активен и работает через systemd и `автоликвидность` на 2m sat*



## Конфигурация и безопасность



### Файл конфигурации



Phoenixd автоматически создает файл `~/.phoenix/phoenix.conf` с необходимыми параметрами:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



** Ключевые параметры:*




- `Автоликвидность`: Размер автоматически открываемых каналов (по умолчанию: 2M Sats)
- http-password`: Пароль администратора для API (создание Invoice и отправка платежей)
- http-password-limited-access`: Ограниченный пароль (только для создания Invoice)



### Безопасный доступ с помощью HTTPS



По умолчанию доступ к API Phoenixd осуществляется только по локальному HTTP (`http://127.0.0.1:9740`). Чтобы использовать ваш узел извне (мобильные приложения, другие серверы, веб-интеграции), необходимо настроить безопасный HTTPS-доступ.



** Принцип обратного прокси:*


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** действует как **обратный прокси**: он принимает HTTPS-запросы из Интернета на порт 443, перенаправляет их на локальный порт Phoenixd (порт 9740), а затем отправляет зашифрованные ответы обратно клиенту.



**Сертификат SSL/TLS** - это цифровой файл, который :




- Удостоверение личности вашего сервера** (предотвращает атаки типа "человек посередине")
- Включает шифрование HTTPS**: все данные, включая пароли API, шифруются во время транспортировки
- Выдается бесплатно** компанией Let's Encrypt с помощью инструмента certbot



Эта конфигурация позволяет :




- Безопасный доступ к API из Интернета**
- Шифруйте пароли API** во время транспортировки (чтобы предотвратить их передачу открытым текстом)
- Интеграция Phoenixd** во внешние приложения, требующие HTTPS
- Соответствие стандартам безопасности** для финансовых API



Настройте этот обратный прокси-сервер HTTPS с помощью nginx:



**1. Конфигурация Nginx**



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. SSL** сертификат



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Функциональный тест



Убедитесь, что Phoenixd работает правильно:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Эти команды должны возвращать JSON-информацию о статусе и балансе узла (изначально пустую).



![Commandes CLI](assets/fr/03.webp)



*Команды Getinfo и getbalance для проверки состояния узла*



## Использование API



### Первый тест приема



**1. Создайте молнию** Invoice



Используйте API для создания своего первого Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Понимание механизма автоматической ликвидности



**Основной принцип:** Когда вы получаете платеж Lightning, Phoenixd иногда приходится открывать новый канал для его получения. За открытие канала взимается комиссия, которая **автоматически вычитается** из полученной суммы.



**Конкретный пример со 100 000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Первый приемочный тест: Получено 100 тыс. Sats, окончательный баланс Sats 75.561 после вычета расходов на ликвидность*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Расчет платы:**




- Плата за обслуживание**: 1% от пропускной способности канала (2 115 000 ГВт-15) = 21 150 ГВт-15
- Сборы Mining**: ~3,289 Sats (за транзакцию On-Chain)
- Всего**: 24 439 Sats автоматически вычитается



**Проверка работы с командами CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Окончательный баланс после оплаты: 257 Sats, оставшийся после отгрузки Молнии*



**Кредит платы за небольшие платежи:** Если вы получаете слишком маленькие платежи, чтобы оправдать открытие канала (< примерно 25k Sats), они сохраняются в невозвратном "кредите платы". Этот кредит будет использован для оплаты будущих платежей за канал, когда вы получите достаточную сумму.



**2. Следите за открытием канала**



Просмотрите журналы Phoenixd:



```bash
journalctl -u phoenixd -f
```



Вы увидите открытие канала и автоматическое списание комиссии за ликвидность. Комиссии варьируются в зависимости от условий Mempool Bitcoin, но всегда включают 1% сервисного сбора плюс текущую комиссию Mining.



**3. Проверьте канал**



```bash
./phoenix-cli listchannels
```



Эта команда отображает активные каналы с указанием их статуса и баланса.



### Полные операции с API



Phoenixd предоставляет REST API на порту 9740, позволяя :



**Основные операции:*


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Важно о стоимости:*




- Получение**: 1% + комиссия Mining за автоматическую ликвидность
- Доставка**: 0.4% маршрутный сбор на Lightning Network



**Webhooks:** Webhooks позволяют Phoenixd **автоматически уведомлять** ваши приложения о наступлении какого-либо события (получен платеж, оплачен Invoice, открыт канал и т.д.). Вместо того чтобы постоянно запрашивать у Phoenixd обновления, ваше приложение получает мгновенное HTTP-уведомление.



**Ваш интернет-магазин автоматически получает уведомление, когда клиент оплачивает заказ, что позволяет мгновенно подтвердить транзакцию.



Конфигурация в файле `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Расширенные приложения



### Интеграции LNURL



Phoenixd поддерживает протоколы LNURL для расширенной интеграции:



**LNURL-Pay:** Оплата услуг, совместимых с LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Получение средств из служб LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Аутентификация через Lightning для доступа к сервисам


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Интеграция с LNbits



LNbits может использовать Phoenixd в качестве источника финансирования, согласно [официальной документации](https://docs.lnbits.org/guide/wallets.html):



*конфигурация *LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Эта интеграция позволяет создавать субаккаунты LNbits на узле Phoenixd, обеспечивая веб-интерфейс Interface для управления несколькими кошельками Lightning.



### Пользовательские приложения



Благодаря обширному REST API вы можете разрабатывать :



** Электронная коммерция:** Прямая интеграция платежей Lightning в ваш магазин


** Услуги по пожертвованиям:** Системы пожертвований со счетами и автоматическими веб-крючками


**Боты для социальных сетей:** Боты для Telegram/Discord с функциями подсказок


**Paywall Lightning:** Премиум-контент доступен за плату Lightning



## Безопасность и передовой опыт



### Защита доступа



**ПаролиAPI:** Автоматически сгенерированные пароли - это ключи к вашей сокровищнице Lightning. Никогда не сообщайте их и меняйте, если сомневаетесь.



**Брандмауэр:** Никогда не оставляйте порт 9740 открытым непосредственно для выхода в Интернет. Всегда используйте nginx с HTTPS.



**Усиленная аутентификация:** Рассмотрите возможность использования VPN или Tailscale для ограничения доступа к вашему серверу только авторизованными устройствами.



### Основные резервные копии



**Восстановление seed:** Сохраните свои 12 слов в безопасном месте, вне сервера. Это единственная гарантия восстановления.



*каталог ~/.phoenix:** Регулярно создавайте резервные копии этой папки (после выключения Phoenixd), чтобы сохранить состояние канала и ускорить восстановление.



**Коды восстановления сервисов:** Также сохраните резервные коды для всех сервисов, в которых вы активировали 2FA с помощью Phoenix.



### Мониторинг и обслуживание



**Мониторинг журналов:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Обновления:** Следите за новыми версиями на [GitHub releases](https://github.com/ACINQ/phoenixd/releases). Обновление выполняется просто: замените бинарник и перезапустите сервис.



## Сравнение с альтернативами



### Phoenixd против Phoenix standard



**Феникс стандарт (мобильный) :**




- ✅ Немедленная установка, полная настройка
- ✅ Мобильный интуитивно понятный Interface
- ✅ То же автосохранение, что и в Phoenixd
- ❌ Отсутствие API для разработчиков
- ❌ Нет доступа к подробным журналам



**Phoenixd (сервер) :**




- ✅ HTTP API для интеграций
- ✅ Полный доступ к журналам
- ✅ Личная инфраструктура
- ❌ Требуются технические навыки
- ❌ Требуется обслуживание сервера



**Оба используют ACINQ в качестве LSP для автоматической ликвидности.



### Фениксд против LND/Ядро Молнии



**LND/Core Lightning :**




- ✅ Полный контроль, полный протокол Lightning
- ✅ Крупное сообщество, зрелая экосистема
- ❌ Сложное ручное управление ликвидностью
- ❌ Большая кривая обучения



**Phoenixd :**




- ✅ Автоматическое управление ликвидностью (как у Phoenix mobile)
- ✅ API для разработчиков
- ✅ Упрощенная конфигурация
- ❌ Использует ACINQ в качестве LSP (без независимой маршрутизации)
- ❌ Менее гибкие, чем полные узлы



## Решение общих проблем



### Проблемы с доступом к API



*ошибка *Authentication failed":**


1. Проверьте пароль в файле `~/.phoenix/phoenix.conf`


2. Проверка формата аутентификации `-u:password`


3. Убедитесь, что Phoenixd запущен (`./phoenix-CLI getinfo`)



** Таймауты соединения:**




- Убедитесь, что Phoenixd прослушивает правильный порт (9740)
- Протестируйте локальный доступ перед настройкой HTTPS
- Проверьте журналы: `journalctl -u phoenixd -f`



### Проблемы с ликвидностью



**Платежи не поступают :**


1. Убедитесь, что сумма превышает минимальный порог (~30k Sats)


2. Обратитесь к журналам, чтобы выявить ошибки канала


3. При необходимости перезапустите Phoenixd



**Остаток в "расходном кредите":**


Небольшие платежи хранятся в качестве резерва. Получите более крупную сумму, чтобы открыть канал и высвободить эти средства.



## Заключение



Phoenixd представляет собой отличный компромисс между простотой использования и техническим суверенитетом для разработчиков. Он предлагает простой, но мощный API Lightning с автоматическим управлением ликвидностью, устраняя сложность традиционных узлов Lightning.



Это решение особенно хорошо подходит для разработчиков и компаний, желающих :




- Интегрируйте Bitcoin Lightning в свои приложения
- Избегайте сложностей, связанных с управлением каналами Lightning
- Преимущество самостоятельной инфраструктуры
- Простой и надежный API



С помощью Phoenixd вы создаете собственную частную инфраструктуру Lightning с современным REST API и автоматическим управлением техническими аспектами. Это идеальное решение для демократизации интеграции Lightning в ваших проектах.



## Полезные ресурсы



### Официальная документация




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Исходный код и релизы
- Сайт Phoenix Server**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Полная документация
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Часто задаваемые вопросы



### Поддержка сообщества




- Проблемы GitHub** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Техническая поддержка
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Новости и объявления