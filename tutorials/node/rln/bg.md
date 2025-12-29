---
name: RGB Lightning Node
description: Как да стартирам възел Lightning, съвместим с RGB, с RLN?
---
![cover](assets/cover.webp)


В този урок стъпка по стъпка ще научите как да настроите възел Lightning RGB в среда на Regtest. Ще видим как да създадем RGB токени и да ги разпространяваме в канали.


## Проектът RLN


Екипът на Bitfinex RGB работи от 2022 г. насам, за да обогати екосистемата на RGB, като разработи цялостен технологичен стек. Вместо да се стреми към един-единствен търговски продукт, неговите усилия са насочени към предоставяне на софтуерни тухли с отворен код, принос към спецификациите на протокола RGB и създаване на референции за изпълнение.


Сред забележителните приноси на Bitfinex към екосистемата на RGB е [библиотеката *RGBlib*](https://github.com/RGB-Tools/rgb-lib), написана на Rust и достъпна чрез връзки в Kotlin и Python, която значително опростява разработването на приложения за RGB, като капсулира сложни механизми за валидиране и ангажиране.


Екипът на Bitfinex е разработил и мобилен RGB wallet, наречен "[*Iris Wallet*](https://iriswallet.com/)", достъпен за Android. Този wallet интегрира използването на прокси сървър на RGB за лесно управление на обмена на данни (*консигнации*) на off-chain за *Client-side Validation* на RGB.


Bitfinex разработи и проекта "Rgb-lightning-node" (RLN). Това е ГВ-16 ГВ-15, базиран на ГВ-17 на `ръждиво-просветлителния` (ЛДК), модифициран така, че да отчита наличието на ГВ-18 активи в канала. Когато се отваря канал, може да се посочи наличието на токени RGB и при всяко актуализиране на състоянието на канала се създава преход в състояние, който отразява разпределението на токените в изходите на Светкавицата. Това позволява :




- Отворете каналите на Lightning в USDT, например;
- Маршрутизирайте тези токени в мрежата, при условие че маршрутите имат достатъчна ликвидност;
- Използвайте логиката за наказание и времеви блокаж на Lightning без модификация: просто закрепете прехода RGB в допълнителен изход на commitment transaction.


Кодът на RLN все още е в алфа-стадий: препоръчваме да го използвате само в **regtest** или в **testnet**.


## Напомняне на протокола RGB


RGB е протокол, който работи върху Bitcoin и емулира функционалността на интелигентните договори и управлението на цифрови активи, без да претоварва блокчейна, на който е базиран. За разлика от конвенционалните интелигентни договори на on-chain (като на Ethereum, например), RGB разчита на системата "*Client-side validation*": по-голямата част от данните и историите на състоянието се обменят и съхраняват изключително от участващите участници, докато блокчейнът на Bitcoin е домакин само на малки криптографски ангажименти (чрез механизми като *Tapret* или *Opret*). Следователно в протокола RGB блокчейнът Bitcoin служи само като сървър за маркиране на времето и система за защита на double-spending.


Договорът RGB е структуриран като еволюционна държавна машина. Той започва с Genesis, който дефинира началното състояние (описвайки например доставката, тикера или други метаданни) в съответствие със строго типизиран и компилиран Schema. След това се прилагат преходи на състояния и, ако е необходимо, разширения на състояния, за да се модифицира или разшири това състояние. Всяка операция, независимо дали става дума за прехвърляне на заменяеми активи (RGB20) или за създаване на уникални активи (RGB21), включва *Печати за еднократна употреба*. Те свързват Bitcoin UTXOs със състояния off-chain и предотвратяват двойното изразходване, като същевременно осигуряват поверителност и мащабируемост.


За да научите повече за това как работи протоколът RGB, ви препоръчвам да преминете този цялостен курс на обучение:


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## Инсталиране на възел Lightning, съвместим с RGB


За да компилираме и инсталираме бинарния модул `rgb-lightning-node`, започваме с клониране на хранилището и неговите подмодули, след което стартираме :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- Опцията `--recurse-submodules` също клонира необходимите подустройства (включително модифицираната версия на `rust-lightning`);
- Опцията `--shallow-submodules` ограничава дълбочината на клонинга, за да ускори изтеглянето, като същевременно осигурява достъп до основните предавания.


От корена на проекта изпълнете следната команда, за да компилирате и инсталирате двоичния файл :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` гарантира, че версията на зависимостите се спазва;
- `--debug` не е задължително, но може да ви помогне да се съсредоточите (ако предпочитате, можете да използвате `--release`) ;
- `--path .` казва на `cargo install` да инсталира от текущата директория.


В края на изпълнението на тази команда във вашия `$CARGO_HOME/bin/` ще бъде наличен изпълним файл `rgb-lightning-node`. Уверете се, че този път е във вашия `$PATH`, за да можете да извикате командата от всяка директория.


## Предварителни условия


За да функционира, `rgb-lightning-node` daemon се нуждае от наличието и конфигурацията на :




- Взел **`bitcoind`**


Всеки екземпляр на RLN ще трябва да комуникира с `bitcoind`, за да излъчва и наблюдава своите транзакции on-chain. На daemon ще трябва да се предостави удостоверяване на автентичността (потребителско име/парола) и URL адрес (хост/порт).




- **индексатор** (Electrum или Esplora)


ГС-41 трябва да може да изброява и проучва транзакциите в ГС-40, по-специално да намира ГС-42, върху която е закотвен даден актив. Ще трябва да посочите URL адреса на вашия Electrum сървър или Esplora.




- Пълномощно **RGB**


Прокси сървърът е компонент (незадължителен, но силно препоръчителен) за опростяване на обмена на RGB *консигнации* между равнопоставени потребители на Lightning. Отново трябва да се посочи URL адрес.


Идентификаторите и URL адресите се въвеждат, когато daemon е *отключен* чрез API.


## Стартиране на Regtest


За проста употреба има скрипт `regtest.sh`, който автоматично стартира набор от услуги чрез Docker: `bitcoind`, `electrs` (индексер), `rgb-proxy-server`.


![RLN](assets/fr/03.webp)


Това ви позволява да стартирате локална, изолирана и предварително конфигурирана среда. Тя създава и унищожава контейнери и директории с данни при всяко рестартиране. Ще започнем със стартирането на :


```bash
./regtest.sh start
```


Този скрипт ще :




- Създаване на директория `docker/` за съхранение на ;
- Стартирайте `bitcoind` в regtest, както и индексатора `electrs` и `rgb-proxy-server` ;
- Изчакайте, докато всичко е готово за употреба.


![RLN](assets/fr/04.webp)


След това ще стартираме няколко RLN възела. В отделни черупки стартирайте, например (за да стартирате 3 RLN възела) :


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- Параметърът `--network regtest` указва използването на конфигурацията regtest;
- `--daemon-listening-port` указва на кой REST порт възелът Lightning ще слуша за повиквания API (JSON);
- `--ldk-peer-listening-port` задава на кой порт на Lightning p2p да се слуша;
- `dataldk0/`, `dataldk1/` са пътищата до директориите за съхранение (всеки възел съхранява информацията си отделно).


Благодарение на API вече можете да изпълнявате команди на вашите RLN възли от браузъра си. По-специално, това е мястото, където можете да *отключвате* демони. Просто отворете браузър на същия компютър, на който са вашите възли, и въведете URL адреса :


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


За да може даден възел да отвори канал, той трябва първо да има биткойни на адрес, генериран със следната команда (например за възел № 1):


```bash
curl -X POST http://localhost:3001/address
```


Отговорът ще ви даде адрес.


![RLN](assets/fr/06.webp)


На регтеста `bitcoind` ще добием няколко биткойна. Изпълнете :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


Изпратете средствата на адреса на възела, генериран по-горе:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


След това изкопайте блок, за да потвърдите транзакцията:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Стартиране на Testnet (без Docker)


Ако искате да тествате по-реалистичен сценарий, можете да стартирате RLN възли в Testnet, а не в Regtest, като ги насочите към публични услуги или услуги, които контролирате:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


По подразбиране, ако не бъде намерена конфигурация, daemon ще се опита да използва :




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`


С вход :




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


Можете също така да персонализирате тези елементи чрез `init`/`unlock` API.


## Издаване на RGB token


За да издадем token, ще започнем със създаването на "цветни" UTXO:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


Разбира се, можете да промените реда. За да потвърдите сделката, ние мина а :


```bash
./regtest.sh mine 1
```


Сега можем да създадем актив RGB. Командата ще зависи от типа на актива, който искате да създадете, и неговите параметри. Тук създавам NIA (*Ненадуваем актив*) token с име "Plan ₿ Academy" (Академия "План ₿") с доставка на 1000 единици. Параметърът `прецизност` ви позволява да определите делимостта на единиците.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "Plan ₿ Academy",
"name": "Plan ₿ Academy",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


Отговорът включва идентификатора на новосъздадения актив. Не забравяйте да отбележите този идентификатор. В моя случай той е :


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


След това можете да го прехвърлите on-chain или да го разпределите в канал за светкавици. Точно това ще направим в следващия раздел.


## Откриване на канал и прехвърляне на актив RGB


Първо трябва да свържете възела си с партньор в мрежата на Lightning, като използвате командата `/connectpeer`. В моя пример управлявам и двата възела. Така че ще извлека публичния ключ на втория си Lightning възел с тази команда:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Командата връща публичния ключ на моя възел № 2 :


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


След това ще отворим канала, като посочим съответния актив (`План ₿ Академия`). Командата `/openchannel` ви позволява да определите размера на канала в сатоши и да изберете да включите актива RGB. Това зависи от това какво искате да създадете, но в моя случай командата е :


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


Научете повече тук:




- `peer_pubkey_and_opt_addr`: Идентификатор на партньора, към който искаме да се свържем (публичният ключ, който намерихме по-рано);
- `capacity_sat`: Общ капацитет на канала в сатоши ;
- `push_msat`: Сума в милисатоши, първоначално прехвърлена на партньора при отваряне на канала (тук веднага прехвърлям 10 000 sats, за да може той да направи трансфер RGB по-късно) ;
- `asset_amount`: Сума на активите на RGB, които трябва да бъдат предоставени на канала ;
- `asset_id` : Уникален идентификатор на актива на RGB, включен в канала;
- `public`: Показва дали каналът трябва да бъде публичен за маршрутизиране в мрежата.


![RLN](assets/fr/14.webp)


За да се потвърди транзакцията, се добиват 6 блока:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Каналът за светкавици вече е отворен и също така съдържа 500 токена `Plan ₿ Academy` от страна на възел № 1. Ако възел № 2 желае да получи токени `Plan ₿ Academy`, той трябва да издаде фактура generate. Ето как да го направите:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


С :




- `amt_msat`: Invoice в милисатоши (минимум 3000 sats) ;
- `expiry_sec` : време на изтичане на Invoice в секунди ;
- `asset_id` : Идентификатор на актива RGB, свързан с фактурата ;
- `asset_amount`: Сума на актива RGB, който ще бъде прехвърлен с тази фактура.


В отговор ще получите фактура RGB:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


Сега ще платим тази фактура от първия възел, който разполага с необходимите парични средства в `Академия План ₿` token:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


Плащането е извършено. Това може да се провери, като се изпълни командата :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


Ето как да разгърнете възел Lightning, модифициран за пренасяне на средства RGB. Тази демонстрация се основава на :




- Среда regtest (чрез `./regtest.sh`) или testnet ;
- Възел Lightning (`rgb-lightning-node`), базиран на `bitcoind`, индексиращ модул и `rgb-proxy-server`;
- Серия от JSON REST API за отваряне/затваряне на канали, издаване на токени, прехвърляне на активи чрез Lightning и др.


Благодарение на този процес :




- Транзакциите за ангажиране на мълнии включват допълнителен изход (OP_RETURN или Taproot) с закрепване на преход RGB;
- Преводите се извършват точно по същия начин като традиционните светкавични плащания, но с добавяне на RGB token;
- Няколко RLN възела могат да бъдат свързани за маршрутизиране и експериментиране с плащания в няколко възела, при условие че по пътя има достатъчна ликвидност както в биткойни, така и в активи RGB.


Ако сте намерили този урок за полезен, ще ви бъда много благодарен, ако поставите зелен палец под него. Моля, не се колебайте да споделите тази статия във вашите социални мрежи. Благодаря ви много!


Препоръчвам и този друг урок, в който обяснявам как да използвате инструмента RGB CLI, разработен от асоциацията LNP/BP, за създаване на договор RGB:


https://planb.academy/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4