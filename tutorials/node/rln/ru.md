---
name: Узел RGB Lightning
description: Как запустить RGB-совместимый узел Lightning с помощью RLN?
---
![cover](assets/cover.webp)

В этом пошаговом руководстве вы узнаете, как настроить ноду Lightning RGB в среде Regtest. Мы увидим, как создавать токены RGB и распространять их в каналах.

## Проект RLN

Команда Bitfinex RGB работает с 2022 года над обогащением экосистемы RGB путем разработки полного технологического стека. Вместо того чтобы стремиться к созданию отдельного коммерческого продукта, ее усилия направлены на создание программных кирпичиков с открытым исходным кодом, внесение вклада в спецификации протокола RGB и создание эталонов реализации.

Среди заметных вкладов Bitfinex в экосистему RGB - [библиотека *RGBlib*](https://github.com/RGB-Tools/rgb-lib), написанная на Rust и доступная через связки на Kotlin и Python, которая значительно упрощает разработку приложений RGB, инкапсулируя сложные механизмы валидации и взаимодействия.

Команда Bitfinex также разработала мобильный кошелек RGB под названием "[*Iris Wallet*](https://iriswallet.com/)", доступный на Android. Этот кошелек интегрирует использование прокси-сервера RGB для простого управления обменом данными вне цепочки (*консигнациями*) для *Client-side Validation* на RGB.

Bitfinex также разработала проект `rgb-lightning-node` (RLN). Это демон Rust, основанный на форке `rust-lightning` (LDK), модифицированный для учета наличия RGB-активов в канале. При открытии канала можно указать наличие RGB-токенов, и при каждом обновлении состояния канала создается переход состояния, отражающий распределение токенов в Lightning-выходах. Это позволяет :


- Откройте каналы Lightning в USDT, например;
- Маршрутизация этих токенов по сети при условии, что маршруты маршрутизации обладают достаточной ликвидностью;
- Используйте логику наказаний и блокировки времени Lightning без изменений: просто закрепите RGB-переход в дополнительном выходе транзакции обязательств.

Код RLN все еще находится на стадии альфа-версии: мы рекомендуем использовать его только в **regtest** или в **testnet**.

## Напоминание о протоколе RGB

RGB - это протокол, который работает поверх Bitcoin и эмулирует функциональность смарт-контрактов и управление цифровыми активами, не перегружая блокчейн, на котором он основан. В отличие от обычных внутрицепочечных смарт-контрактов (как, например, в Ethereum), RGB опирается на систему "*Client-side validation*": большинство данных и истории состояний обмениваются и хранятся исключительно самими участниками, тогда как в блокчейне Bitcoin хранятся лишь небольшие криптографические обязательства (через такие механизмы, как *Tapret* или *Opret*). Таким образом, в протоколе RGB блокчейн Биткойна служит только сервером таймстампинга и системой защиты от двойных трат.

Контракт RGB по своей структуре напоминает эволюционную машину состояний. Он начинается с Генезиса, определяющего начальное состояние (описывающего, например, поставку, тикер или другие метаданные) в соответствии со строго типизированной и скомпилированной Схемой. Затем для изменения или расширения этого состояния применяются Переходы состояния и, при необходимости, Расширения состояния. Каждая операция, будь то передача взаимозаменяемых активов (RGB20) или создание уникальных активов (RGB21), включает в себя *Пломбы однократного использования*. Они связывают Bitcoin UTXO с внецепочечными состояниями и предотвращают двойные траты, обеспечивая конфиденциальность и масштабируемость.

Чтобы узнать больше о том, как работает протокол RGB, я рекомендую вам пройти этот полный курс обучения:

https://planb.network/courses/csv402
## RGB-совместимый узел Lightning

Чтобы скомпилировать и установить бинарный файл `rgb-lightning-node`, мы начнем с клонирования репозитория и его подмодулей, а затем запустим команду :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- Опция `--recurse-submodules` также клонирует необходимые суб-устройства (включая модифицированную версию `rust-lightning`);
- Опция `--shallow-submodules` ограничивает глубину клона для ускорения загрузки, но при этом предоставляет доступ к основным коммитам.

Из корня проекта выполните следующую команду для компиляции и установки двоичного файла :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` гарантирует, что версия зависимостей будет соблюдена;
- `--debug` не является обязательным, но может помочь вам сосредоточиться (вы можете использовать `--release`, если хотите) ;
- `--path .` указывает `cargo install` на установку из текущего каталога.

По завершении этой команды в каталоге `$CARGO_HOME/bin/` будет доступен исполняемый файл `rgb-lightning-node`. Убедитесь, что этот путь находится в вашем `$PATH`, чтобы вы могли вызывать команду из любой директории.

## Пререквизиты

Для работы демону `rgb-lightning-node` необходимо наличие и конфигурация :


- Узел `bitcoind`**

Каждый экземпляр RLN должен будет взаимодействовать с `bitcoind` для трансляции и мониторинга своих транзакций на цепи. Демону необходимо предоставить аутентификацию (логин/пароль) и URL (хост/порт).


- Индексатор** (Electrum или Esplora)

Демон должен уметь выводить список и изучать транзакции на цепи, в частности, находить UTXO, на котором был привязан актив. Вам нужно будет указать URL вашего сервера Electrum или Esplora.


- Прокси RGB**

Прокси-сервер - это компонент (необязательный, но настоятельно рекомендуемый) для упрощения обмена RGB *согласованиями* между пирами Lightning. Опять же, необходимо указать URL.

Идентификаторы и URL вводятся, когда демон *разблокирован* через API.

## Запуск регтеста

Для простого использования есть скрипт `regtest.sh`, который автоматически запускает через Docker набор сервисов: `bitcoind`, `electrs` (индексатор), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

Это позволяет запустить локальную, изолированную, предварительно настроенную среду. Она создает и уничтожает контейнеры и каталоги данных при каждой перезагрузке. Мы начнем с запуска файла :

```bash
./regtest.sh start
```

Этот скрипт будет :


- Создайте каталог `docker/` для хранения файлов ;
- Запустите `bitcoind` в regtest, а также индексатор `electrs` и `rgb-proxy-server`;
- Подождите, пока все будет готово к использованию.

![RLN](assets/fr/04.webp)

Далее мы запустим несколько узлов RLN. В отдельных оболочках запустите, например, (для запуска 3 узлов RLN) :

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


- Параметр `--network regtest` указывает на использование конфигурации regtest;
- `--daemon-listening-port` указывает, на каком REST-порту узел Lightning будет прослушивать вызовы API (JSON);
- `--ldk-peer-listening-port` указывает, на каком порту Lightning p2p слушать;
- `dataldk0/`, `dataldk1/` - это пути к каталогам хранилищ (каждый узел хранит свою информацию отдельно).

Теперь вы можете выполнять команды на узлах RLN через браузер, благодаря API. В частности, здесь вы можете *разблокировать* демонов. Просто откройте браузер на том же компьютере, что и ваши узлы, и введите URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Чтобы узел мог открыть канал, он должен сначала иметь биткоины на адресе, сгенерированном с помощью следующей команды (например, для узла n°1):

```bash
curl -X POST http://localhost:3001/address
```

В ответе вы найдете адрес.

![RLN](assets/fr/06.webp)

На `bitcoind` Regtest мы собираемся добыть несколько биткоинов. Выполнить

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Отправьте средства на адрес узла, указанный выше:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Затем заминируйте блок, чтобы подтвердить транзакцию:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Запуск тестовой сети (без Docker)

Если вы хотите протестировать более реалистичный сценарий, вы можете запустить узлы RLN не в Regtest, а в Testnet, указав на публичные службы или службы, которые вы контролируете:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

По умолчанию, если конфигурация не найдена, демон попытается использовать файл :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

С логином :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

Вы также можете настроить эти элементы с помощью API `init`/`unlock`.

## Выпуск токена RGB

Чтобы выпустить токен, мы начнем с создания "цветных" UTXO:

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

Вы, конечно, можете адаптировать заказ. Чтобы подтвердить сделку, мы высылаем вам сообщение с текстом :

```bash
./regtest.sh mine 1
```

Теперь мы можем создать актив RGB. Команда будет зависеть от типа актива, который вы хотите создать, и его параметров. Здесь я создаю токен NIA (*Non Inflatable Asset*) под названием "PBN" с запасом в 1000 единиц. Параметр `precision` позволяет определить делимость единиц.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

В ответе указывается идентификатор вновь созданного актива. Не забудьте записать этот идентификатор. В моем случае это :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

Затем вы можете передать его в цепь или распределить в канале Lightning. Именно этим мы и займемся в следующем разделе.

## Открытие канала и передача актива RGB

Сначала вы должны подключить свой узел к аналогу в сети Lightning с помощью команды `/connectpeer`. В моем примере я контролирую оба узла. Поэтому я получу открытый ключ второго узла Lightning с помощью этой команды:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Команда возвращает открытый ключ моего узла n°2:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Далее мы откроем канал, указав соответствующий актив (`PBN`). Команда `/openchannel` позволяет задать размер канала в сатоши и выбрать включение актива RGB. Это зависит от того, что вы хотите создать, но в моем случае команда выглядит так: :

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

Узнайте больше здесь:


- `peer_pubkey_and_opt_addr`: Идентификатор пира, к которому мы хотим подключиться (открытый ключ, найденный ранее);
- `capacity_sat`: Общая емкость канала в сатоши ;
- `push_msat`: Сумма в миллисатоши, первоначально передаваемая пиру при открытии канала (здесь я сразу передаю 10 000 сат, чтобы он мог сделать RGB-передачу позже);
- `asset_amount`: Количество RGB-активов, которые будут переданы каналу;
- `asset_id` : Уникальный идентификатор актива RGB, задействованного в канале;
- `public`: Указывает, должен ли канал быть общедоступным для маршрутизации в сети.

![RLN](assets/fr/14.webp)

Для подтверждения транзакции добывается 6 блоков:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

Канал Lightning теперь открыт и также содержит 500 токенов `PBN` на стороне узла n°1. Если узел n°2 хочет получить токены `PBN`, он должен сгенерировать счет-фактуру. Вот как это сделать:

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


- `amt_msat`: Сумма счета в миллисатоши (минимум 3000 сат) ;
- `expiry_sec`: время истечения срока действия счета-фактуры в секундах ;
- `asset_id`: идентификатор актива RGB, связанного со счетом-фактурой;
- `asset_amount`: Сумма актива RGB, который будет передан с этим счетом-фактурой.

В ответ вы получите счет в формате RGB:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Теперь мы оплатим этот счет с первого узла, на котором хранится необходимая наличность с токеном `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Оплата была произведена. Это можно проверить, выполнив команду :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Вот как развернуть узел Lightning, модифицированный для переноса RGB-активов. Эта демонстрация основана на :


- Среда regtest (через `./regtest.sh`) или testnet ;
- Узел Lightning (`rgb-lightning-node`), основанный на `bitcoind`, индексаторе и `rgb-proxy-server`;
- Серия JSON REST API для открытия/закрытия каналов, выпуска токенов, передачи активов через Lightning и т. д.

Благодаря этому процессу:


- Транзакции молниеносного взаимодействия включают дополнительный выход (OP_RETURN или Taproot) с привязкой RGB-перехода;
- Переводы осуществляются точно так же, как и традиционные платежи Lightning, но с добавлением токена RGB;
- Несколько узлов RLN могут быть связаны для маршрутизации и экспериментов с платежами между несколькими узлами при условии достаточной ликвидности как биткоинов, так и активов RGB на пути.

Если вы нашли этот урок полезным, я буду очень благодарен, если вы поставите ниже "зеленый палец". Пожалуйста, не стесняйтесь поделиться этой статьей в своих социальных сетях. Большое спасибо!

Я также рекомендую этот учебник, в котором я объясняю, как использовать инструмент RGB CLI, разработанный ассоциацией LNP/BP, для создания контракта RGB:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4