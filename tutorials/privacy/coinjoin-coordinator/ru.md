---
name: Координатор Coinjoin - WabiSabi
description: Как настроить и запустить координатор coinjoin, следуя протоколу WabiSabi (используется в Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Введение 👋


В этом руководстве мы поможем вам настроить координатор coinjoin - по сути, сервер, объединяющий людей, которые хотят сэкономить на комиссии за транзакции или повысить свою конфиденциальность в совместных транзакциях. Поскольку в комплекте с Wasabi Wallet больше нет координатора, управляемого компанией, пользователям приходится самим искать и выбирать подходящий им сервер-координатор. Лишь несколько координаторов предложили плату за координацию в размере 0%, поэтому разработчики Wasabi Wallet приложили все усилия, чтобы сделать управление собственным координатором сообщества как можно более простым (на таком маленьком оборудовании, как Raspberry Pi5!). В настоящее время активных координаторов, которые просят 0% за координацию, можно найти на [LiquiSabi](https://liquisabi.com) и, что более важно, на [nostr](https://github.com/Kukks/WasabiNostr).


## Требования 🫴



- VPS (хостируемый узел) или компьютер/сервер (самостоятельный узел)
- Обрезанный/полный узел ядра Bitcoin (проверено в версии 29.0)


Дополнительно:


- (Под)домен, перенаправляющий трафик на узел (например, coinjoin.[yourdomain].io)


Рекомендуется иметь некоторый опыт работы с подсказками командной строки и bash, поскольку не все шаги можно автоматизировать.


В аппаратном плане рекомендуется иметь систему с:


- 4 ядра
- 16 ГБ ОПЕРАТИВНОЙ ПАМЯТИ
- 2 ТБ SSD или NVMe (для полного узла) / 128 ГБ SSD (для узла pruned)


Такие требования может обеспечить Raspberry Pi 5 всего за 120 долларов, не считая хранилища, которое стоит около 100 долларов за NVMe-флешку на 2 ТБ.


Дешевые VPS обычно оснащаются только 1 ядром и 4 ГБ оперативной памяти, что, как я убедился, слишком мало для синхронизации и проверки всего биткоина blockchain на блокчейне 911817.


Для хранения данных полной ноде потребуется как минимум 2 ТБ дисковой памяти, предпочтительно SSD или NVMe. При обрезке blockchain допустимо использовать накопитель гораздо меньшего объема (например, SSD на 128 ГБ).


Если вы планируете использовать координатор для больших (300+ входных данных) коинджойнтов, рекомендуется выбрать систему с более быстрыми/новыми ядрами с более высокой производительностью для всех проверок подписей.


## Установка 🛠️


На узел мы хотим загрузить и установить последнюю выпущенную версию Wasabi Wallet, которая включает бэкенд и координатор в виде отдельных исполняемых файлов рядом с wallet.


Найдите последнюю версию: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) и проверьте PGP-подпись релиза с помощью ключей: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Детали развертывания зависят от аппаратного обеспечения (процессорной архитектуры) и выбора ОС. Ниже приведены различные детали для Raspberry Pi (ARM-64) с Debian на базе RaspiBlitz в качестве отправной точки. Перейдите к развертыванию ОС Ubuntu (X86-64) с помощью Nix.


Инструкции по установке можно найти здесь: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Развертывание RaspiBlitz/Debian


Для узлов RaspiBlitz (проверено в версии 1.11) можно использовать развертывание script, собранное из исходного кода: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Простота развертывания


Для минимального развертывания достаточно извлечь исполняемые файлы для вашей платформы в папку.

Примеры кодов командной строки для Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


В результате должно получиться следующее сообщение с правильной подписью:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


После этого можно приступать к установке загруженного пакета:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Конфигурация 🧾


Перед запуском координатора необходимо отредактировать файл Config.json:


- Bitcoin RPC учетные данные
- Предпочтительные параметры раунда
- Расширенный открытый ключ координатора (создайте новый SegWit wallet для приема собранной пыли)

**Предупреждение**: Taproot wallet приведут к появлению неизрасходованных UTXO! Используйте здесь нативные Segwit wallet.


- Разрешенные типы входных и выходных адресов
- Конфигурация диктора для публикации через nostr (имя, описание, Uri, минимальные входы, nostr relay, nostr private key)


Вы можете запустить координатор, доступный только через адрес .onion, или использовать свой собственный домен clearnet.


Найдите или создайте файл конфигурации по этому пути:


`~/.walletwasabi/coordinator/Config.json`


Отредактируйте его с помощью команды:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Смотрите этот пример Config.json:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Конфигурация Tor 🧅


Чтобы заполнить свой OnionServicePrivateKey, вам, скорее всего, придется сначала сгенерировать его.


Wasabi Wallet сгенерирует для вас приватный ключ, если вы запустите его в первый раз с ``PublishAsOnionService'': true,`` установленным в файле Config.json.


Запустите координатор один раз с помощью команды:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Чтобы узнать адрес скрытой службы Onion, проверьте журналы координатора с помощью:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


и вы найдете что-то вроде:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Длинный URL, заканчивающийся на .onion, - это адрес вашего скрытого сервиса или CoordinatorUri.


Или проверьте конфигурационный файл координатора еще раз:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Теперь они должны заполняться автоматически.


## Бег ⚡


После установки всех параметров конфигурации вы можете запустить службу координатора и начать анонсировать первый раунд 🕶️


Просто запустите координатор командой:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Вы можете следить за текущим раундом и количеством зарегистрированных UTXO's/монет, проверив (в браузере Tor для .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Дополнительно: отладка сервера координаторов


Вы можете отслеживать любые проблемы или ошибки в файле журнала по адресу ``~/.walletwasabi/backend/Logs.txt``


Типичные проблемы включают в себя проблемы с подключением RPC, это должно быть включено в ``~/.bitcoin/bitcoin.conf`` с помощью:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Необязательно: Запуск внутреннего сервера


Вместе с координатором вы также можете предоставить пользователям, у которых нет собственного узла биткоина, бэкэнд-сервер, к которому можно подключиться для оценки комиссии и блокчейн-фильтров.


Запустите эту службу с помощью команды:


```
wbackend
```


## Приглашение пользователей Wasabi к вашему координатору 🫂


Чтобы другие пользователи могли найти ваш сервис, вы можете положиться на диктора nostr или поделиться волшебной ссылкой с вашим доменом (clearnet) или скрытым сервисом (ссылка .onion) и круглыми параметрами, как здесь:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Когда пользователь скопирует волшебную ссылку и откроет свой Wasabi Wallet, программа автоматически покажет диалог координатора с вашим доменом и параметрами.


![detected](assets/en/02.webp)


💚🍣 Поздравляем с децентрализацией приватности биткоина 🕶️


Помните о своей подготовке [Васабика](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet только для защиты 🛡️