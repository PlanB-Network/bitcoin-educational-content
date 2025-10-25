---
name: Lightning Watchtower
description: Watchtower mõistmine ja kasutamine Lightning-sõlmes
---
![cover](assets/cover.webp)



## Kuidas vahitornid töötavad?



Lightning Network ökosüsteemi oluline osa, _Watchtowers_ pakub kasutajate Lightning-kanalitele täiendavat kaitsetaset. Nende peamine ülesanne on jälgida kanali seisundit ja sekkuda, kui üks kanali pool püüab teist petta.



Kuidas saab Watchtower kindlaks teha, kas kanal on ohustatud? Ta saab kliendilt (üks kanali osapooltest) teavet, mis on vajalik rikkumise õigeks tuvastamiseks ja sellega tegelemiseks. See teave sisaldab andmeid kõige viimase tehingu kohta, kanali praegust seisundit ja karistustehingute loomiseks vajalikku Elementsi. Enne nende andmete edastamist Watchtower-le võib klient need konfidentsiaalsuse säilitamiseks krüpteerida. Seega, isegi kui Watchtower saab andmed kätte, ei saa ta neid dekrüpteerida enne, kui rikkumine on tegelikult toimunud. See krüpteerimismehhanism kaitseb kliendi eraelu puutumatust ja takistab Watchtower-l saada volitamata juurdepääsu tundlikule teabele.



Selles õpetuses vaatleme 3 võimalust, kuidas kasutada **Watchtower** :




- kõigepealt klassikaline toormeetod LND kaudu,
- seejärel teine lähenemine koos Eye of Satoshi-ga,
- ja lõpuks lihtsustatud Watchtower konfiguratsioon teie Lightning-sõlmes, mida majutab Umbrel.



## 1 - Watchtower või kliendi konfigureerimine LND kaudu



*See õpetus on võetud [ametlikust LND dokumentatsioonist](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Originaalversioonis võib olla tehtud mõningaid muudatusi



Alates versioonist v0.7.0 toetab `LND` privaatse altruistliku Watchtower täitmist `LND` täielikult integreeritud allsüsteemina. Watchtowerid pakuvad teist kaitseliini pahatahtlike või juhuslike rikkumisstsenaariumide vastu, kui kliendisõlm on rikkumise ajal võrguühenduseta või ei suuda reageerida, pakkudes suuremat turvalisust kanali rahaliste vahendite jaoks.



Erinevalt _tasuvastasest vaatetornist_, mis nõuab oma teenuse eest osa kanali rahalistest vahenditest, tagastab _altruistlik vaatetorn_ kõik ohvri rahalised vahendid (miinus On-Chain tasud) ilma komisjonitasu võtmata. Preemiavahitornid aktiveeritakse hilisemas versioonis; need on veel testimis- ja täiustamisfaasis.



Lisaks sellele saab "LND" nüüd konfigureerida nii, et see toimiks _valvetorni kliendina_, salvestades teiste altruistlike valvetornide krüpteeritud rikkumiste kõrvaldamise tehinguid (nn "õiglustehinguid"). Watchtower salvestab fikseeritud suurusega krüpteeritud blobs ning saab õiglustehingu dekrüpteerida ja avaldada alles pärast seda, kui rikkuja on edastanud Commitment tühistatud oleku. Klient ↔ Watchtower side krüpteeritakse ja autentitakse efemerentsete võtmepaaride abil, mis piirab Watchtower võimet jälgida oma kliente pikaajaliste volituste kaudu.



Pange tähele, et me oleme otsustanud kasutada selles versioonis piiratud hulka funktsioone, mis juba pakuvad olulist turvalisust LND kasutajatele. Paljud teised Watchtower-ga seotud funktsioonid on kas peaaegu valmis või juba kaugele arenenud; me jätkame nende tarnimist, kui me neid testime ja kui neid peetakse ohutuks.



märkus: esialgu salvestavad vaatetornid ainult tühistatud kohustuste väljundid `to_local` ja `to_remote`; HTLC väljundite salvestamine võetakse kasutusele tulevases versioonis, kuna protokolli saab laiendada, et lisada krüpteeritud blobs'ile täiendavaid allkirjaandmeid._



### Watchtower konfigureerimine



Watchtower seadistamiseks peavad käsurea kasutajad koostama valikulise `watchtowerrpc` allserveri, mis võimaldab Watchtower-ga suhtlemist gRPC või `lncli` kaudu. Avaldatud binaarsed versioonid sisaldavad vaikimisi `watchtowerrpc` allserverit.



Watchtower aktiveerimiseks on minimaalne konfiguratsioon `Watchtower.active=1`.



Watchtower konfiguratsiooniteavet saab kätte käsuga `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Watchtower konfiguratsioonivalikute täielik komplekt on saadaval käsuga `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Kuulamisliidesed



Vaikimisi kuulab Watchtower portaali `:9911`, mis vastab kõigi olemasolevate liideste portidele `9911`. Kasutajad saavad määrata oma kuulamise liidesed valikuga `--Watchtower.listen=`. Saate oma konfiguratsiooni kontrollida `lncli tower info` väljal `"listeners"`. Kui teil on probleeme Watchtower-ga ühenduse loomisega, veenduge, et `<port>` on avatud või et teie proxy on õigesti konfigureeritud aktiivsele Interface-le.



#### Välised IP-aadressid



Kasutajad võivad ka määrata Watchtower välise IP Address(es), kasutades `Watchtower.externalip=`, mis avalikustab Watchtower täieliku URI (pubkey@host:port) RPC või `lncli tower info` kaudu:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URI-d saab klientidele edastada ühendamiseks ja kasutamiseks järgmise käsuga:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Kui Watchtower klientidel on vaja sellele kaugjuurdepääsu, siis veenduge, et :




- Avage port 9911 (või port, mis on määratletud `Watchtower.listen` kaudu).
- Kasutage proxy't, et suunata liiklus avatud pordist Watchtower kuulavasse Address-sse.



#### Tori varjatud teenused



Watchtowerid toetavad Tor'i peidetud teenuseid ja võivad automaatselt generate käivitamisel kasutada järgmisi valikuid:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Seejärel ilmub .onion Address väljale "uris" päringu "lncli tower info" ajal:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



märkus: Watchtower avalik võti erineb LND sõlme avalikust võtmest. Hetkel toimib see "Soft valgeloendina", kuna kliendid peavad teadma Watchtower avalikku võtit, et kasutada seda varukoopiana, kuni täiustatud valgeloendimehhanismide valmimiseni. Me EI soovita seda avalikku võtit avalikult avaldada, välja arvatud juhul, kui olete valmis oma Watchtower kogu internetile avalikustama._



#### Watchtower andmebaasi kataloog



Watchtower andmebaasi saab teisaldada, kasutades valikut `Watchtower.towerdir=`. Pange tähele, et valitud teele lisatakse järelliide `/Bitcoin/Mainnet/Watchtower.db`, et isoleerida andmebaasid stringi järgi. Seega, kui määrata `Watchtower.towerdir=/path/to/towerdir`, siis tekib andmebaas aadressil `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Linuxi all asub näiteks Watchtower vaikimisi andmebaas aadressil :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Watchtower kliendi konfigureerimine



Watchtower kliendi konfigureerimiseks on vaja kahte elementi:





- Aktiveerige Watchtower klient valikuga `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- Aktiivse Watchtower URI.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Selliselt saab konfigureerida mitu vaatetorni.



#### Õigustehingute tasumäärad



Kasutajad saavad valikuliselt määrata õiglustehingute tasu määra valikuga `wtclient.sweep-fee-rate`, mis võtab vastu väärtusi sat/bait. Vaikeväärtus on 10 sat/bait, kuid tipptasude ajal on võimalik püüda suuremaid määrasid, et saavutada kõrgemat prioriteetsust. `sweep-fee-rate` muutmine kehtib kõigi uute uuenduste puhul pärast daemon taaskäivitamist.



#### Järelevalve



Käsuga `lncli wtclient` saavad kasutajad nüüd otse Watchtower kliendiga suhelda, et saada või muuta teavet kõigi registreeritud vaatetornide kohta.



Näiteks saate `lncli wtclient tower` abil teada, kui palju sessioone on praegu läbi räägitud eespool lisatud Watchtower-ga ja kas seda kasutatakse varukoopiate tegemiseks tänu väljale `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Watchtower seansside kohta teabe saamiseks kasutage valikut `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Kõik Watchtower kliendi konfiguratsioonivõimalused on saadaval käsuga `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Oma Eye of Satoshi paigaldamine



*See õpetus on osaliselt välja võetud [Summer of Bitcoin Blogi](https://blog.summerofbitcoin.org/) artiklist. Originaalversioonis on tehtud muudatusi*



Satoshi silm ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) on Watchtower välk, mis ei kuulu hoiule, vastab [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). See koosneb kahest põhikomponendist:





- teos**: sisaldab käsurea Interface (CLI) ja Watchtower olulisi serverifunktsioone. Selle _crate_ kompileerimisel saadakse kaks binaarkoodi - **teosd** ja **teos-CLI**.





- teos-common**: sisaldab jagatud serveripoolset ja kliendipoolset funktsionaalsust (kasulik kliendi loomiseks).



Watchtower korrektseks käivitamiseks peate enne Watchtower käivitamist käsuga **teosd** käivitama **bitcoind**. Enne nende kahe käsu käivitamist tuleb konfigureerida fail **Bitcoin.conf**. Seda saab teha järgmiselt:





- Installige Bitcoin core lähtekoodist või laadige see alla. Pärast allalaadimist asetage fail **Bitcoin.conf** Bitcoin core kasutajakataloogi. Lisateavet selle kohta, kuhu faili paigutada, leiate sellelt lingilt, sest see sõltub kasutatavast operatsioonisüsteemist.





- Kui asukoht on kindlaks määratud, lisage järgmised valikud:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: RPC taotluste puhul





- rpcuser** ja **rpcpassword**: RPC klientide autentimine serverile





- regtest**: ei ole vajalik, kuid kasulik, kui plaanite arendustegevust.



**rpcuser** ja **rpcpassword** väärtused valite ise. Need tuleb kirjutada ilma jutumärkideta. Näiteks:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Kui nüüd käivitate **bitcoind**, peaks sõlmpunkt käivituma.





- Watchtower osa jaoks peate esmalt installima **teos** lähtekoodist. Järgige sellel lingil toodud juhiseid.





- Kui olete oma süsteemi edukalt **teos** installeerinud ja testid läbi viinud, võite minna edasi viimase sammu juurde: **teos.toml** faili seadistamine teose kasutajakataloogis. See fail tuleks paigutada kausta nimega **.teos** (pange tähele punkti) teie kodukataloogi alla. Näiteks **/home//.teos** Linuxi all. Kui asukoht on leitud, looge fail **teos.toml** ja seadke need valikud vastavalt **bitcoind** tehtud muudatustele:



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Pange tähele, et siin tuleb kasutajanimi ja parool kirjutada **kinnitusmärkide sees**. Kasutades eelmist näidet :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Kui see on tehtud, peaksite olema valmis Watchtower käivitamiseks. Kuna me kasutame **regtest**, siis on tõenäoline, et meie Bitcoin testvõrgus ei kaevandatud plokke, kui Watchtower esimest korda ühendati (kui see juhtus, siis on midagi valesti). Watchtower loob sisemise vahemälu viimasest 100 plokist **bitcoind**; seega võib esimesel käivitamisel ilmneda järgmine viga:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Kuna me kasutame **regtest**, saame Miner blokeerida, andes RPC käsu, ilma et peaksime ootama 10-minutilist keskmist viivitust, mida on näha teistes võrkudes (näiteks Mainnet või Testnet). Vt **bitcoin-cli** abi, et saada üksikasjad Miner blokeerimise kohta.



![Image](assets/fr/01.webp)



See on kõik: te olete Watchtower edukalt käivitanud. Palju õnne. 🎉




## 3 - Watchtower konfigureerimine Umbrelil



Umbrelil on Watchtower-ga ühendamine teie välgumihkliksõlme kaitsmiseks äärmiselt lihtne, sest kõik toimub graafilise Interface kaudu. Pärast kaugühendamist oma sõlme avage rakendus "**Lightning Node**".



![Image](assets/fr/02.webp)



Klõpsake Interface paremal ülaosas olevatel kolmel väikesel punktil, seejärel valige "**täiustatud seaded**".



![Image](assets/fr/03.webp)



Menüüs "**Watchtower**" on saadaval kaks valikut:





- Watchtower teenus**: see valik võimaldab teil kasutada Watchtower, st teenust, mis jälgib teiste sõlmede kanaleid, et avastada pettusekatsed. Rikkumise korral avaldab teie Watchtower tehingu Blockchain-s, võimaldades kasutajatel oma lukustatud raha tagasi saada. Pärast aktiveerimist ilmub teie Watchtower URI ja seda saab edastada teistele sõlmedele, et nad saaksid selle lisada oma Watchtower kliendile;





- Watchtower Client**: see valik võimaldab teil ühendada väliseid vaatetorne, et kaitsta oma kanaleid. Kui see on aktiveeritud, saate lisada Watchtower teenuseid, millele teie sõlmpunkt edastab vajalikku teavet oma kanalite kohta. Need vaatetornid jälgivad seejärel nende seisundit ja sekkuvad pettusekatse korral.



Teie jaoks on loomulikult esmatähtis aktiveerida *Watchtower klient*, et kaitsta oma sõlme, kuid ma soovitan teil aktiveerida ka *Watchtower teenus*, et aidata kaasa teiste kasutajate turvalisusele.



![Image](assets/fr/04.webp)



Seejärel klõpsake nupule Green "**Save and Restart Node**". Teie LND käivitub uuesti.



Samast menüüst leiate ka oma Watchtower teenuse URI, kui olete selle aktiveerinud. Võite lisada ka välise Watchtower URI, et kaitsta oma kanaleid. Kinnitamiseks klõpsake "**ADD**".



![Image](assets/fr/05.webp)



Internetis on saadaval mitu Watchtowerit. Näiteks [LN+ ja Voltage pakuvad altruistlikku Watchtower](https://lightningnetwork.plus/Watchtower), millega saab ühendada:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Teine võimalus on Exchange oma Watchtower URI koos oma bitcoini kaaslastega, nii et igaüks kaitseb teise sõlme.



Samuti soovitan teil luua mitu vahitorni, et vähendada riske juhul, kui üks neist muutub kättesaamatuks.



Lõpuks saate reguleerida parameetrit "**Watchtower kliendi pühkimistasu määr**". See määrab maksimaalse tasu määra, mida olete nõus maksma Watchtower eetrisse kantud karistusmaksete tehingu eest. Veenduge, et määrate piisavalt kõrge väärtuse, mis on kohandatud teie kanalites lukustatud summadele.