---
name: Координатор на Coinjoin - WabiSabi
description: Как да настроите и стартирате координатор за обединяване на монети, следвайки протокола WabiSabi (използван в Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Въведение 👋


В това експертно ръководство ще ви помогнем да създадете координатор на coinjoin, по същество сървър, който обединява хора, които искат да спестят от таксите за транзакции или да увеличат поверителността на веригата си в съвместни транзакции. Тъй като вече няма управляван от компанията координатор, включен в пакета на Wasabi Wallet, потребителите трябва да намерят и изберат свой собствен предпочитан сървър за координатори. Появиха се само няколко координатора, които поискаха 0% такса за координация, така че разработчиците на Wasabi Wallet работят усилено, за да направят възможно най-лесно започването на управлението на собствен координатор на общността (на хардуер, малък като Raspberry Pi5!). Активните в момента координатори, които искат 0% такса за координация, могат да бъдат намерени на [LiquiSabi](https://liquisabi.com) и по-важното на [nostr](https://github.com/Kukks/WasabiNostr).


## Изисквания 🫴



- VPS (хостван възел) или компютър/сървър (самостоятелно хостван възел)
- Орязан/пълен възел на ядрото на Bitcoin (тестван с версия 29.0)


По избор:


- (под)домейн, който препраща трафика към възела (напр. coinjoin.[yourdomain].io)


Препоръчително е да имате известен опит с командни редове и bash, тъй като не всички стъпки могат да бъдат автоматизирани.


Препоръчително е да разполагате със система с:


- 4 ядра
- 16 GB RAM
- 2 TB SSD или NVMe (за пълен възел) / 128 GB SSD (за възел pruned)


Такива изисквания могат да бъдат осигурени от Raspberry Pi 5 само за 120 $, с изключение на съхранението, което струва около 100 $ за 2TB NVMe стик.


Евтините VPS обикновено се предлагат само с 1 ядро и 4 GB RAM, което според мен е твърде малко, за да се синхронизира и провери целият биткойн blockchain с височина на блока 911817.


От гледна точка на съхранението един пълен възел се нуждае от минимум 2 TB дисково хранилище, за предпочитане тип SSD или NVMe. При орязване на blockchain е допустимо използването на много по-малък диск за съхранение (например 128GB SSD).


Ако възнамерявате да използвате координатор за големи (над 300 входни данни) съвместни операции, препоръчваме да изберете система с по-бързи/нови ядра с по-висока производителност за всички проверки на подписите.


## Инсталация 🛠️


На възела искаме да изтеглим и инсталираме последната издадена версия на Wasabi Wallet, която включва бекенд и координатор като самостоятелни изпълними файлове до wallet.


Намерете най-новата версия: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) и проверете PGP подписа на версията с ключовете: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Детайлите по внедряването се различават в зависимост от хардуера (процесорна архитектура) и избора на операционна система.По-долу са дадени различни детайли за Raspberry Pi (ARM-64) с Debian-базиран RaspiBlitz като отправна точка. Пропуснете напред за разгръщане на операционна система Ubuntu (X86-64) с помощта на Nix.


Намерете инструкциите за инсталиране тук: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Разгръщане на RaspiBlitz/Debian


За възли RaspiBlitz (тествани с версия 1.11) може да се използва разгръщане script, изградено от изходен код: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Лесно внедряване


За минимално внедряване просто трябва да разархивирате изпълнимите файлове за вашата платформа в една папка.

Примерни кодове от командния ред за Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Това трябва да доведе до следното съобщение за валиден подпис:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


И можете да продължите да инсталирате изтегления пакет:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Конфигурация 🧾


Преди да стартирате координатора, трябва да редактирате файла Config.json с вашия:


- Bitcoin RPC пълномощия
- Предпочитани параметри на кръга
- Разширен публичен ключ на координатора (създаване на нов SegWit wallet за получаване на събрания прах)

**Предупреждение**: Taproot wallet ще доведат до неизползваеми UTXO! Използвайте роден Segwit wallet тук.


- Разрешени типове входни и изходни адреси
- Конфигурация на анонсатора за публикуване през nostr (име, описание, Uri, минимални входове, nostr relay, nostr private key)


Можете да стартирате координатора, достъпен само чрез адреса .onion, или да използвате свой потребителски домейн в clearnet.


Намерете или създайте файла с конфигурацията по този път:


`~/.walletwasabi/coordinator/Config.json`


Редактирайте го с командата:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Вижте този пример Config.json:


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

### Конфигурация на Tor 🧅


За да попълните своя OnionServicePrivateKey, вероятно първо трябва да генерирате такъв.


Wasabi Wallet ще генерира частен ключ за вас, ако го стартирате за първи път с ```"PublishAsOnionService": true,```, зададен във файла Config.json.


Изпълнете координатора веднъж с командата:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


За да видите адреса на скритата услуга на Onion, проверете логовете на координатора с:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


и ще намерите нещо подобно:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Дългият URL адрес, завършващ на .onion, е вашият скрит адрес на услугата или CoordinatorUri.


Или проверете отново конфигурационния файл на координатора с:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Това трябва да се попълни автоматично.


## Бягане ⚡


След като всички параметри на конфигурацията са зададени, можете да стартирате услугата на координатора и да започнете да обявявате първия кръг 🕶️


Просто стартирайте координатора с командата:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Можете да следите текущия кръг и броя на регистрираните UTXO/монети, като проверите (в браузъра Tor за .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### По избор: отстраняване на грешки в сървъра на координатора


Можете да следите за евентуални проблеми или грешки в регистрационния файл на адрес ```~/.walletwasabi/backend/Logs.txt```


Типичните проблеми включват проблеми с връзката с RPC, което трябва да бъде разрешено в ```~/.bitcoin/bitcoin.conf``` с:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### По избор: Стартиране на бекенд сървъра


Заедно с координатора можете да осигурите и бекенд сървър за потребителите, които нямат собствен биткойн възел, към който да се свържат за оценка на таксите и блокфилтри.


Стартирайте тази услуга с командата:


```
wbackend
```


## Покана на потребители на Wasabi към вашия координатор 🫂


За да могат други потребители да открият услугата ви, можете да разчитате на анонса на nostr или да споделите магическа връзка с вашия домейн (clearnet) или скрита услуга (.onion link) и кръгли параметри по следния начин:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Когато потребителят копира магическата връзка и отвори своя Wasabi Wallet, софтуерът автоматично ще покаже диалоговия прозорец на координатора с вашия домейн и параметри.


![detected](assets/en/02.webp)


💚🍣 Поздравления за децентрализацията на поверителността на биткойн 🕶️


Не забравяйте обучението си [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet е само за защита 🛡️