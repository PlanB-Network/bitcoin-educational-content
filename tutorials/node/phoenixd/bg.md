---
name: Phoenixd
description: Внедряване на собствен минималистичен възел Lightning с Phoenixd
---

![cover](assets/cover.webp)



Финансовата автономност означава също така да контролирате инфраструктурата си за светкавици. За разработчиците и компаниите, които желаят да интегрират Bitcoin Lightning в своите приложения, **Phoenixd** представлява идеалното решение: минималистичен, специализиран Lightning възел с автоматично управление на ликвидността.



Phoenixd е Lightning сървър, разработен от ACINQ, специално за изпращане и получаване на Lightning плащания чрез HTTP API. За разлика от пълнофункционалните имплементации, като LND или Core Lightning, Phoenixd абстрахира цялата сложност на управлението на каналите, като същевременно запазва самостоятелната защита на вашите средства.



В този урок ще разгледаме как да инсталираме, конфигурираме и използваме Phoenixd за разработване на приложения Lightning със самостоятелно хоствана инфраструктура и лесен за използване API.



## Какво е Phoenixd?



Phoenixd е минимален, специализиран възел Lightning, разработен от ACINQ. Това е решение, предназначено за разработчици и предприятия, които желаят да интегрират Lightning в своите приложения без сложността на управлението на full node.



### Принцип на работа



**Phoenixd е минимален възел на Lightning, който използва ACINQ като LSP (Lightning Service Provider) за автоматична ликвидност. Когато получавате Lightning плащания, той автоматично отваря канали с възли ACINQ, за да разпредели необходимия входящ капацитет. Тази ликвидност "в движение" е мигновена, но се таксува точно **1% + mining такси** от получената сума.



**Автоматизирано управление:** Системата управлява три основни елемента:




- Светкавични канали**: Отваряйте, затваряйте и управлявайте автоматично, когато е необходимо
- Входяща/изходяща ликвидност**: Автоматично осигуряване чрез сливане и отваряне на канали
- Кредит за такса** : Малките плащания, които не са достатъчни, за да оправдаят канала, се съхраняват като провизия за бъдещи такси



### Ползи от Phoenixd



** Вие контролирате частните си ключове (12 думи seed) и средствата. Phoenixd генерира вашите wallet локално, без да споделя ключовете ви.



**Лична инфраструктура:** Phoenixd работи на вашия сървър, като ви дава достъп до подробни регистри, конфигурация и контрол на API. Вече не сте зависими от услуга на трета страна за достъп до вашите средства.



**Интегриран API:** Phoenixd разполага с HTTP API за интегриране с други услуги, поддръжка на LNURL и разработване на персонализирани приложения.



**Лесна интеграция:** Благодарение на простия си REST API Phoenixd може да бъде интегриран във всяко приложение или услуга, които изискват плащания Lightning.



**Важна бележка:** Автоматичната ликвидност все още идва от ACINQ като LSP (Lightning Service Provider). Phoenixd използва същия механизъм като Phoenix mobile за автоматично управление на каналите.



## Инсталиране на Phoenixd



### Предварителни условия



Phoenixd изисква среда на Linux (препоръчително Ubuntu/Debian) с някои основни умения за работа с команден ред. За оптимална производителност ще ви е необходим :





- Сървър на Linux**: VPS или локална машина със стабилна връзка
- OpenJDK 21** : Среда за изпълнение на Java
- Стабилна интернет връзка**: За синхронизиране с мрежата Lightning
- Име на домейн** (по избор) : За защитен HTTPS достъп до API



### Изтегляне и инсталиране



**1. Изтегляне на Phoenixd**



Отидете на страницата [GitHub releases](https://github.com/ACINQ/phoenixd/releases) и изтеглете най-новата версия за вашата архитектура:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Първо стартиране



Стартирайте Phoenixd за инициализация:



```bash
./phoenixd
```



При първото стартиране ще бъдете помолени да потвърдите две важни стъпки, като напишете "Разбирам" :



**Съобщение 1 - Резервно копие:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Запазете тези 12 думи** - това е единствената гаранция за възстановяване.



**Съобщение 2 - Автоматична ликвидност:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



За всяко потвърждение въведете `Разбирам`.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd стартира за първи път: резервни потвърждения и автоматична ликвидност*



**3. Конфигурация в експлоатация** (само на френски език)



За непрекъсната работа създайте systemd :



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



*Услугата Phoenixd е активна и функционира чрез systemd и `автоликвидност` при 2m sat*



## Конфигуриране и сигурност



### Конфигурационен файл



Phoenixd автоматично създава `~/.phoenix/phoenix.conf` с основните параметри:



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



**Ключови параметри:**




- `автоликвидност`: Размер на автоматично отворените канали (по подразбиране: 2M Sats)
- http-password`: Парола на администратора за API (създаване на фактури и изпращане на плащания)
- http-password-limited-access`: Ограничена парола (само за създаване на фактури)



### Сигурен достъп с HTTPS



По подразбиране Phoenixd API е достъпен само чрез локален HTTP (`http://127.0.0.1:9740`). За да използвате възела си отвън (мобилни приложения, други сървъри, уеб интеграции), трябва да конфигурирате сигурен HTTPS достъп.



**Принцип на обратното пълномощно:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** действа като **обратен прокси**: той слуша HTTPS заявки от интернет на порт 443, пренасочва ги към Phoenixd локално (порт 9740), след което изпраща криптирани отговори обратно на клиента.



**Сертификатът SSL/TLS** е цифров файл, който :




- Доказване на самоличността на сървъра** (предотвратява атаки от типа "човек по средата")
- Активира HTTPS** криптиране: всички данни, включително паролите ви за API, се криптират по време на транспортирането
- Издава се безплатно** от Let's Encrypt чрез инструмента certbot



Тази конфигурация ви позволява да :




- Сигурен достъп до API от интернет**
- Криптиране на паролите API** по време на транспортиране (за да се предотврати предаването им в свободен текст)
- Интегриране на Phoenixd** във външни приложения, изискващи HTTPS
- Съответствие със стандартите за сигурност** за финансовите API



Конфигуриране на този HTTPS обратен прокси сървър с nginx :



**1. Конфигурация на Nginx**



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



### Функционален тест



Проверете дали Phoenixd работи правилно:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Тези команди трябва да връщат JSON информация за състоянието и баланса на възела (първоначално празна).



![Commandes CLI](assets/fr/03.webp)



*Команди Getinfo и Getbalance за проверка на състоянието на възлите*



## Използване на API



### Първи тест за приемане



**1. Създаване на фактура Lightning**



Използвайте API, за да създадете първата си фактура:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Разбиране на механизма за автоматична ликвидност



**Фундаментален принцип:** Когато получавате плащане от Lightning, Phoenixd понякога трябва да отвори нов канал, за да може да го получи. Това отваряне на канал струва такса, която **автоматично се приспада** от получената сума.



**Конкретен пример със 100 000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Първи тест за приемане: Sats 100 хил., получен, окончателен баланс на Sats 75 561 след приспадане на разходите за ликвидност*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Изчисляване на таксата:**




- Такса за обслужване**: 1% от капацитета на канала (2,115,000 Sats) = 21,150 Sats
- Такси Mining**: ~3,289 Sats (за транзакция On-Chain)
- Общо**: 24,439 Sats се приспада автоматично



**Проверка с команди CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Окончателно салдо след изпращане на плащането: 257 Sats, оставащи след изпращането на Lightning*



**Кредит за такси за малки плащания:** Ако получавате плащания, които са твърде малки, за да оправдаят откриването на канал (< около 25 хил. Sats), те се съхраняват в невъзвръщаем "кредит за такси". Този кредит ще се използва за плащане на бъдещи такси за канал, когато получите достатъчна сума.



**2. Следвайте отварянето на канала**



Гледайте дневниците на Phoenixd:



```bash
journalctl -u phoenixd -f
```



Ще видите отварянето на канала и автоматичното приспадане на таксите за ликвидност. Таксите варират в зависимост от условията на Mempool Bitcoin, но винаги включват 1% такса за обслужване плюс текущата такса mining.



**3. Проверка на канала**



```bash
./phoenix-cli listchannels
```



Тази команда показва активните ви канали с тяхното състояние и баланс.



### Завършване на операциите по API



Phoenixd разкрива REST API на порт 9740, който позволява :



**Основни операции:**


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



**Важни за разходите:**




- Разписка**: 1% + такса mining за автоматична ликвидност
- Доставка**: 0.4% такса за маршрутизиране в мрежата на Lightning



**Webhooks:** Webhooks позволяват на Phoenixd **автоматично да уведомява** приложенията ви при настъпване на събитие (получено плащане, платена фактура, отворен канал и т.н.). Вместо постоянно да питате Phoenixd за актуализации, вашето приложение получава незабавно HTTP известие.



**Вашият онлайн магазин автоматично получава известие, когато клиент плати за поръчка, което позволява незабавно потвърждаване на транзакцията.



Конфигурация в `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Разширени приложения



### Интеграции на LNURL



Phoenixd естествено поддържа протоколи LNURL за разширена интеграция:



**LNURL-Pay:** Плащайте за съвместими с LNURL услуги


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Извличане на средства от услуги LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Удостоверяване чрез Lightning за достъп до услуги


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Интеграция с LNbits



LNbits може да използва Phoenixd като източник на финансиране съгласно своята [официална документация](https://docs.lnbits.org/guide/wallets.html):



**Конфигурация LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Тази интеграция ви позволява да създавате LNbits подсметки, захранвани от вашия възел Phoenixd, като предоставяте уеб-базиран Interface за управление на множество портфейли Lightning.



### Персонализирани приложения



Благодарение на изчерпателния REST API можете да разработвате :



**Електронна търговия:** Директна интеграция на плащанията Lightning в магазина ви


**Услуги за дарения:** Системи за дарения с фактури и автоматични уеб куки


**Боти за социални мрежи:** Telegram/Discord ботове с функции за съвети


**Paywall Lightning:** Премиум съдържание срещу такса Lightning



## Безопасност и най-добри практики



### Защита на достъпа



**API пароли:** Автоматично генерираните пароли са ключът към вашата съкровищница на Lightning. Никога не ги споделяйте и ги сменяйте, ако се съмнявате.



**Защитна стена:** Никога не оставяйте порт 9740 отворен директно към интернет. Винаги използвайте nginx с HTTPS.



**Усъвършенствано удостоверяване:** Помислете за VPN или Tailscale, за да ограничите достъпа до сървъра си само до оторизирани устройства.



### Основни резервни копия



**Възстановяване на seed:** Запазете 12-те си думи на сигурно място, извън сървъра. Това е единствената ви гаранция за възстановяване.



*директория ~/.phoenix:** Създавайте редовно резервно копие на тази папка (след като Phoenixd е бил изключен), за да запазите състоянието на канала и да ускорите възстановяването.



**Кодове за възстановяване на услуги:** Запазете и резервни кодове за всички услуги, в които сте активирали 2FA с вашия Phoenix.



### Мониторинг и поддръжка



**Дневник за наблюдение:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Актуализации:** Следете [GitHub releases](https://github.com/ACINQ/phoenixd/releases) за нови версии. Актуализацията е толкова проста, колкото да замените двоичната програма и да рестартирате услугата.



## Сравнение с алтернативи



### Phoenixd срещу стандарт Phoenix



**Phoenix стандарт (мобилен) :**




- ✅ Незабавна инсталация, нулева конфигурация
- ✅ Interface мобилен интуитивен
- ✅ Същото автоматично запазване като Phoenixd
- ❌ Без API за разработчици
- ❌ Няма достъп до подробни дневници



**Phoenixd (сървър) :**




- ✅ HTTP API за интеграции
- ✅ Пълен достъп до дневниците
- ✅ Лична инфраструктура
- ❌ Изискват се технически умения
- ❌ Необходима е поддръжка на сървъра



**И двете използват ACINQ като LSP за автоматична ликвидност.



### Phoenixd срещу LND/Core Lightning



**LND/Core Lightning :**




- ✅ Пълен контрол, пълен протокол Lightning
- ✅ Голяма общност, зряла екосистема
- ❌ Комплексно ръчно управление на ликвидността
- ❌ Голяма крива на обучение



**Phoenixd :**




- ✅ Автоматично управление на ликвидността (като Phoenix mobile)
- ✅ API за разработчици
- ✅ Опростена конфигурация
- ❌ Използва ACINQ като LSP (без самостоятелно маршрутизиране)
- ❌ По-малко гъвкави от пълните възли



## Решаване на често срещани проблеми



### Проблеми с достъпа до API



**Аутентикацията се провали" грешка:**


1. Проверете паролата във файла `~/.phoenix/phoenix.conf`


2. Проверка на формата за удостоверяване `-u:password`


3. Уверете се, че Phoenixd работи (`./phoenix-CLI getinfo`)



** Време за прекъсване на връзката:**




- Проверете дали Phoenixd слуша на правилния порт (9740)
- Тестване на локалния достъп, преди да конфигурирате HTTPS
- Проверете дневниците: `journalctl -u phoenixd -f`



### Проблеми с ликвидността



**Плащанията не пристигат :**


1. Проверете дали сумата надвишава минималния праг (~30 хил. Sats)


2. Преглед на дневниците за идентифициране на грешки в канала


3. Рестартирайте Phoenixd, ако е необходимо



**Баланс в "кредит за разходи":**


Малките плащания се съхраняват като провизия. Получете по-голяма сума, за да задействате отварянето на канала и да освободите тези средства.



## Заключение



Phoenixd представлява отличен компромис между лекота на използване и техническа независимост за разработчиците. Той предлага прост, но мощен Lightning API с автоматично управление на ликвидността, като елиминира сложността на традиционните Lightning възли.



Това решение е особено подходящо за разработчици и компании, които желаят да :




- Интегриране на Bitcoin Lightning във вашите приложения
- Избягване на сложността на управлението на каналите на Lightning
- Възползвайте се от самостоятелно хоствана инфраструктура
- Прост и надежден API



С Phoenixd изграждате своя собствена частна инфраструктура на Lightning с модерен REST API и автоматично управление на техническите аспекти. Това е идеалното решение за демократизиране на интеграцията на Lightning във вашите проекти.



## Полезни ресурси



### Официална документация




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Изходен код и версии
- Сайт Phoenix Server**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Пълна документация
- Често задавани въпроси Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Често задавани въпроси



### Подкрепа от Общността




- Проблеми в GitHub** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Техническа поддръжка
- ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Новини и съобщения