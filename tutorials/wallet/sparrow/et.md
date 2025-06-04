---
name: Varblane Wallet
description: Sparrow Wallet paigaldamine, konfigureerimine ja kasutamine
---
![cover](assets/cover.webp)

Sparrow Wallet on Craig Raw poolt välja töötatud isehaldatav Bitcoin portfellihaldusprogramm. Seda avatud lähtekoodiga tarkvara hindavad bitcoin'id oma paljude funktsioonide ja intuitiivse Interface eest.

Sparrow'd saab kasutada kahel viisil:


- Nagu Hot Wallet, kus teie isiklikud võtmed on salvestatud teie arvutisse.
- Cold Wallet haldurina, kus privaatvõtmeid hoitakse Hardware Wallet-l. Selles režiimis manipuleerib Sparrow ainult avalikku Wallet teavet, jälgib vahendeid, genereerib aadresse ja koostab tehinguid, kuid Hardware Wallet allkiri on vajalik, et need tehingud oleksid kehtivad. Seega võib see asendada selliseid rakendusi nagu Ledger Live või Trezor Suite.

Sparrow toetab ühe ja mitme allkirjaga rahakotte ning võimaldab mitme rahakoti sujuvat haldamist. Näiteks saate samaaegselt juhtida ühte Wallet, mis on ühendatud Ledger-ga, teist Trezoriga, ning samuti Hot Wallet.

Tarkvara pakub ka täiustatud mündikontrollifunktsioone, mis võimaldavad teil täpselt valida, milliseid UTXOsid teie tehingutes kasutada, et optimeerida oma konfidentsiaalsust.

Mis puutub ühendusse, siis Sparrow võimaldab teil ühendada oma Bitcoin sõlme kas eemalt Electrumi serveri kaudu või Bitcoin Core'i abil. Samuti on võimalik kasutada avalikku sõlme, kui teil ei ole veel oma sõlme. Kaugühendused toimuvad Tori kaudu.

## Paigaldage Sparrow Wallet

Mine [ametlikule Sparrow Wallet allalaadimislehele](https://sparrowwallet.com/download/) ja vali oma operatsioonisüsteemile vastav tarkvaraversioon.

![Image](assets/fr/01.webp)

Oluline on kontrollida tarkvara terviklikkust ja autentsust enne selle paigaldamist. Kui te ei tea, kuidas seda teha, leiate täieliku õpetuse siit :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Kui Sparrow on paigaldatud, võite jätta esialgsed selgitavad ekraanid vahele ja minna otse ühenduse haldamise ekraanile.

![Image](assets/fr/02.webp)

## Ühendamine Bitcoin võrguga

Bitcoin võrguga suhtlemiseks ja oma tehingute edastamiseks peab Sparrow olema ühendatud Bitcoin sõlme. Selle ühenduse loomiseks on kolm peamist võimalust:


- 🟡 Kasutades avalikku sõlme, st ühendudes kolmanda osapoole sõlme, mis lubab selliseid ühendusi. Kui sul ei ole oma Bitcoin sõlme, võimaldab see võimalus Sparrow'ga kiiresti alustada. Kuid sõlme, millega te ühendute, näeb kõiki teie tehinguid, mis võib ohustada teie konfidentsiaalsust. Kontroll oma võtmete üle on oluline, kuid oma sõlme omamine on veelgi parem. Seega kasutage seda võimalust ainult siis, kui te alles alustate, olles samas teadlik oma privaatsust ohustavatest riskidest.
- 🟢 Ühendamine Bitcoin tuumasõlmega. Kui teil on oma Bitcoin Core'i sõlmpunkt, saate selle ühendada Sparrow Wallet-ga kas lokaalselt, kui Bitcoin Core on paigaldatud samasse masinasse, või eemalt.
- 🔵 Ühendus Electrumi serveri kaudu. Kui teie Bitcoin-sõlm on varustatud Electrumiga, nagu näiteks node-in-a-box-lahenduste puhul, nagu Umbrel või Start9, siis saate sellega Sparrow'st eemalt ühendust luua.

**Võimalik on kasutada ühendust Electrs või Bitcoin Core'i kaudu oma sõlmes, et vähendada vajadust usaldada kolmandat osapoolt ja optimeerida oma konfidentsiaalsust**

### Ühenda avaliku sõlme 🟡

Avaliku sõlme ühendamine on väga lihtne. Klõpsake vahekaardil "*Public Server*".

![Image](assets/fr/03.webp)

Valige rippmenüüst sõlme.

![Image](assets/fr/04.webp)

Seejärel klõpsake nuppu "*Testiühendus*".

![Image](assets/fr/05.webp)

Pärast ühendamist kuvab Sparrow Wallet Interface paremas alumises nurgas kollase märkeruudu, mis näitab, et olete ühendatud avaliku sõlmpunktiga.

![Image](assets/fr/06.webp)

### Bitcoin tuumaga ühendamine 🟢

Teine meetod Bitcoin sõlme ühendamiseks on Sparrow'i ühendamine Bitcoin tuumaga. Kui Bitcoin Core on paigaldatud samasse masinasse, toimub autentimine küpsiste faili kaudu. Kui Bitcoin Core asub kaugemas masinas, tuleb kasutada parooli, mis on määratud failis `Bitcoin.conf`.

Pange tähele, et kui te kasutate kärbitud Bitcoin tuumasõlme, ei saa te taastada Wallet, mis sisaldab tehinguid, mis eelnevad lokaalselt salvestatud plokkidele. Sparrow'l loodud uue Wallet puhul ei ole see aga probleem: teie uued tehingud on nähtavad, isegi kui sõlme on kärbitud.

Bitcoin Core-sõlme konfigureerimiseks saate sõltuvalt teie operatsioonisüsteemist tutvuda ühega järgmistest juhendmaterjalidest:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
Mine Sparrow's vahekaardile "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**With Bitcoin Core local:**

Kui teie arvutisse on paigaldatud Bitcoin Core, otsige tarkvara failide hulgast üles fail "Bitcoin.conf". Kui seda faili ei ole olemas, saate selle luua. Avage see tekstiredaktoriga ja sisestage järgmine rida:

```ini
server=1
````
Sauvegardez ensuite vos modifications.
Vous pouvez également effectuer cette configuration via l'interface graphique de Bitcoin-QT en naviguant dans "*Settings*" > "*Options...*" et en activant l'option "*Enable RPC server*".
N'oubliez pas de redémarrer le logiciel après ces modifications.
![Image](assets/fr/08.webp)
Revenez ensuite à Sparrow Wallet et renseignez le chemin vers votre fichier de cookie, généralement situé dans le même dossier que le `bitcoin.conf`, selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
![Image](assets/fr/09.webp)
Laissez les autres paramètres par défaut, l'URL `127.0.0.1` et le port `8332`, puis cliquez sur "*Test Connection*".
![Image](assets/fr/10.webp)
La connexion est établie. Une coche verte apparaîtra en bas à droite pour indiquer que vous êtes connecté à un nœud Bitcoin Core.
![Image](assets/fr/11.webp)
**Avec Bitcoin Core à distance :**
Si Bitcoin Core est installé sur une autre machine connectée sur le même réseau, commencez par localiser le fichier `bitcoin.conf` parmi les fichiers du logiciel. Si ce fichier n'existe pas encore, vous pouvez le créer. Ouvrez ce fichier avec un éditeur de texte et ajoutez la ligne suivante :
```

server=1

```
Après avoir modifié le fichier, assurez-vous de l'enregistrer dans le dossier approprié selon votre système d'exploitation :
| **macOS**   | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin                     |
| **Linux**   | ~/.bitcoin                            |
Il est également possible de réaliser cette manipulation via l'interface graphique de Bitcoin-QT. Accédez au menu "*Settings*", puis "*Options...*", et activez l'option "*Enable RPC server*" en cochant la case correspondante. Si le fichier `bitcoin.conf` n'existe pas, vous pouvez le créer directement depuis cette interface en cliquant sur "*Open Configuration File*".
![Image](assets/fr/12.webp)
Trouvez l'adresse IP de la machine qui héberge Bitcoin Core dans votre réseau local. Pour cela, vous pouvez utiliser un outil tel que [Angry IP Scanner](https://angryip.org/). Supposons, pour l'exemple, que l'adresse IP de votre nœud soit `192.168.1.18`.
Dans le fichier `bitcoin.conf`, ajoutez les lignes suivantes, en configurant `rpcbind=192.168.1.18` pour correspondre à l'adresse IP de votre nœud.
```

[käsi]

rpcbind=127.0.0.0.1

rpcbind=192.168.1.18

rpcallowip=127.0.0.0.1

rpcallowip=192.168.1.0/24

```
![Image](assets/fr/13.webp)
Ajoutez également dans le fichier `bitcoin.conf` un identifiant et un mot de passe pour les connexions à distance. Assurez-vous de remplacer `loic` par votre nom d'utilisateur et `my_password` par un mot de passe fort :
```

rpcuser=loic

rpcpassword=my_password

```