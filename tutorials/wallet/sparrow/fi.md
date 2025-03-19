---
name: Varpunen Wallet
description: Sparrow Wallet:n asentaminen, konfigurointi ja käyttö
---
![cover](assets/cover.webp)

Sparrow Wallet on Craig Rawin kehittämä Bitcoin-salkunhallintaohjelmisto. Tämä avoimen lähdekoodin ohjelmisto on bitcoin-käyttäjien arvostama sen monien ominaisuuksien ja intuitiivisen Interface:n vuoksi.

Sparrow'ta voi käyttää kahdella tavalla:


- Kuten Hot Wallet, jossa yksityiset avaimesi on tallennettu tietokoneellesi.
- Cold:n Wallet:n hallinnoijana, kun yksityisiä avaimia säilytetään Hardware Wallet:ssä. Tässä tilassa Sparrow käsittelee vain julkisia Wallet-tietoja, seuraa varoja, luo osoitteita ja luo tapahtumia, mutta Hardware Wallet:n allekirjoitus vaaditaan, jotta nämä tapahtumat olisivat voimassa. Se voi siis korvata Ledger Liven tai Trezor Suiten kaltaiset sovellukset.

Sparrow tukee yhden ja usean allekirjoituksen lompakoita ja mahdollistaa useiden lompakoiden sujuvan hallinnan. Voit esimerkiksi hallita samanaikaisesti yhtä Wallet:ta, joka on liitetty Ledger:een, toista Trezoriin ja myös Hot Wallet:ta.

Ohjelmisto tarjoaa myös kehittyneitä kolikonvalvontaominaisuuksia, joiden avulla voit valita tarkasti, mitä UTXO-yksiköitä käytät transaktioissasi luottamuksellisuuden optimoimiseksi.

Yhteyden osalta Sparrow antaa sinun muodostaa yhteyden omaan Bitcoin-solmuun joko etänä Electrum-palvelimen kautta tai Bitcoin Core -palvelimella. On myös mahdollista käyttää julkista solmua, jos sinulla ei vielä ole omaa solmua. Etäyhteydet muodostetaan Torin kautta.

## Asenna Sparrow Wallet

Siirry [Sparrow Wallet:n viralliselle lataussivulle] (https://sparrowwallet.com/download/) ja valitse käyttöjärjestelmääsi vastaava ohjelmistoversio.

![Image](assets/fr/01.webp)

On tärkeää tarkistaa ohjelmiston eheys ja aitous ennen sen asentamista. Jos et tiedä, miten tämä tehdään, löydät täydellisen ohjeen täältä :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Kun Sparrow on asennettu, voit ohittaa ensimmäiset selittävät näytöt ja siirtyä suoraan yhteydenhallintanäyttöön.

![Image](assets/fr/02.webp)

## Yhteyden muodostaminen Bitcoin-verkkoon

Jotta Sparrow voi olla yhteydessä Bitcoin-verkkoon ja lähettää tapahtumia, sen on oltava yhteydessä Bitcoin-solmuun. Yhteys voidaan muodostaa kolmella eri tavalla:


- 🟡 Julkisen solmun käyttäminen, eli yhteyden muodostaminen kolmannen osapuolen solmuun, joka sallii tällaiset yhteydet. Jos sinulla ei ole omaa Bitcoin-solmua, tämän vaihtoehdon avulla pääset nopeasti alkuun Sparrow'n kanssa. Solmu, johon muodostat yhteyden, näkee kuitenkin kaikki tapahtumasi, mikä voi vaarantaa luottamuksellisuutesi. Avainten hallinta on tärkeää, mutta oma solmu on vielä parempi. Käytä tätä vaihtoehtoa siis vain, jos olet vasta aloittamassa ja olet tietoinen yksityisyyteesi kohdistuvista riskeistä.
- 🟢 Yhteyden muodostaminen Bitcoin Core -solmuun. Jos sinulla on oma Bitcoin Core -solmu, voit liittää sen Sparrow Wallet:een joko paikallisesti, jos Bitcoin Core on asennettu samaan koneeseen, tai etänä.
- 🔵 Yhteys Electrum-palvelimen kautta. Jos Bitcoin-solmusi on varustettu Electrilla, kuten esimerkiksi Umbrelin tai Start9:n kaltaisissa node-in-a-box -ratkaisuissa, voit muodostaa siihen yhteyden etänä Sparrow'sta.

**On suositeltavaa käyttää Electrs- tai Bitcoin Core -yhteyttä omassa solmussasi, jotta vähennät tarvetta luottaa kolmanteen osapuoleen ja optimoit luottamuksellisuuden**

### Yhteys julkiseen solmuun 🟡

Yhteyden muodostaminen julkiseen solmuun on hyvin yksinkertaista. Napsauta "*Julkinen palvelin*"-välilehteä.

![Image](assets/fr/03.webp)

Valitse solmu avattavasta luettelosta.

![Image](assets/fr/04.webp)

Napsauta sitten "*Testiyhteys*".

![Image](assets/fr/05.webp)

Kun yhteys on muodostettu, Sparrow Wallet näyttää keltaisen rastin Interface:n oikeassa alakulmassa osoituksena siitä, että olet yhteydessä julkiseen solmuun.

![Image](assets/fr/06.webp)

### Kytkeminen Bitcoin-ytimeen 🟢

Toinen tapa muodostaa yhteys Bitcoin-solmuun on yhdistää Sparrow Bitcoin Coreen. Jos Bitcoin Core on asennettu samaan koneeseen, todennus tapahtuu evästetiedoston avulla. Jos Bitcoin Core on etäkoneessa, sinun on käytettävä salasanaa, joka on määritelty `Bitcoin.conf`-tiedostossa.

Huomaa, että jos käytät karsittua Bitcoin Core-solmua, et voi palauttaa Wallet:ää, joka sisältää tapahtumia, jotka edeltävät paikallisesti tallennettuja lohkoja. Sparrow'lla luodun uuden Wallet:n kohdalla tämä ei kuitenkaan ole ongelma: uudet tapahtumat näkyvät, vaikka solmu olisi karsittu.

Bitcoin Core -solmun konfiguroimiseksi voit tutustua johonkin seuraavista ohjeista käyttöjärjestelmästäsi riippuen:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
Siirry Sparrow'ssa välilehdelle "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**With Bitcoin Core local:**

Jos Bitcoin Core on asennettu tietokoneellesi, etsi Bitcoin.conf-tiedosto ohjelmistotiedostojen joukosta. Jos tätä tiedostoa ei ole olemassa, voit luoda sen. Avaa se tekstieditorilla ja lisää seuraava rivi:

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