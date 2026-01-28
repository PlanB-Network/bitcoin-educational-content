---
name: SAFU Ninja
description: Tallenna seed SAFU Ninja -menetelmällä
---

![cover](assets/cover.webp)


## 1. Johdanto



**Ninja SAFU** -menetelmä on **DIY (tee se itse)** -ratkaisu, jonka avulla voit luoda **kestävän, turvallisen ja huomaamattoman** varmuuskopion **seed-lausekkeestasi** (12- tai 24-sanaisesta Mnemonic-lausekkeesta, joka on määritelty **BIP-39**-standardissa). Tämä lauseke on välttämätön Bitcoin Wallet:n tai minkä tahansa muun yhteensopivan Wallet:n palauttamiseksi.



Sen sijaan, että kirjoittaisit sanasi paperille - yksinkertainen mutta haavoittuva menetelmä - kaiverretaan ne **ruostumattomasta teräksestä valmistettuihin aluslevyihin**, jotka on koottu **Bolt:een**. Tuloksena on pienikokoinen, palo-, korroosio-, vesi- ja iskunkestävä varmuuskopio. Toisin kuin paperi, joka voi tuhoutua liekkien, kosteuden tai ajan vaikutuksesta, ruostumaton teräs takaa pitkäaikaisen säilyvyyden jopa äärimmäisissä olosuhteissa (jopa 1300 °C tai 20 tonnin paine).



Ninja SAFU -lähestymistavalla on useita etuja:





- **Luottamuksellisuus**: Et ole ostamassa tuotetta, jonka on todettu olevan tarkoitettu kryptovaluutan varmuuskopiointiin. Komponentit ovat vakiokomponentteja (aluslevyt, pultit, metallikotelo), joita on saatavilla rautakaupoista, mikä vähentää kohdentamisriskiä, jos tietovuoto tulee erikoistuneelta myyjältä.





- **Edullisuus**: Tämä ratkaisu maksaa **15-140 euroa**, riippuen jo käytössäsi olevista työkaluista.





- **Luotettavuus**: [Jameson Lopp](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/), jotka ovat testanneet menetelmää tiukoissa rasituskokeissa (äärimmäinen kuumuus, korroosio, mekaaninen paine).



Tämä vaiheittainen opas näyttää sinulle, miten voit tehdä oman Ninja SAFU -varmistuskopiosi ja suojata bitcoinisi paremmin häviämiseltä tai tuhoutumiselta. Jos haluat lisätietoja seed-lauseen varmuuskopioinnista ja suojaamisesta, tutustu liitteisiin.




## 2. Laitteisto



Ninja SAFU -varmuuskopion luomiseen tarvitset seuraavat komponentit, joita kaikkia on saatavana laitekaupoista tai verkosta.



### 2.1 Tarvittavat materiaalit





- Ruostumattomasta teräksestä valmistetut aluslevyt (suositellaan M8):
- **Materiaali**: Ruostumaton teräs (esim. 304 tai V4A korroosionkestävyyden lisäämiseksi)
- **Koko**: M8 (sisähalkaisija 8 mm, ulkohalkaisija ~24 mm). M6 aluslevyt ovat liian pieniä ja vaikeita kaivertaa.
- **Määrä**: 12 tai 24 aluslevyä vakiolauseeseen seed, lisäksi valinnaisia aluslevyjä (ks. kohta 3.4) ja noin kymmenen aluslevyä testejä tai virheitä varten.





- **Ruostumaton teräs Bolt ja mutteri (M8)**:
- **Tekniset tiedot**: Riippuen aluslevyjen määrästä ja paksuudesta, halkaisija 8 mm. Siipimutteri helpottaa avaamista ilman työkaluja, mutta myös yksinkertaista mutteria voidaan käyttää.



![image](assets/fr/03.webp)





- **Kirjain- ja numerolävistyssarja (3 mm tai 6 mm)**:
- **Tekniset tiedot**: 6 mm korkeat merkit helpottavat luettavuutta, ja ne voivat olla suositeltavampia, jos osa kirjaimista on heikentynyt. Valitse tukeva sarja toistuvaa käyttöä varten.



![image](assets/fr/04.webp)





- **Vasara vai leka**:
    - Riittävän ja tarkan leimausvoiman saamiseksi on suositeltavaa käyttää lekalevyjä





- **Alasin tai tukeva pinta**:
 - Paksu Hard-pinta (esim. 1 kg:n painoinen alasin tai 10 cm:n kiveys) iskujen vaimentamiseksi.



Jos et halua investoida lävistinsarjaan, voit myös kaivertaa aluslevyt kaiverruskynällä. Tämä ratkaisu on usein edullisempi, mutta vaatii suurempaa huolellisuutta tyydyttävän lopputuloksen saamiseksi.



### 2.2 Valinnaiset työkalut





- **Leimauslaite**: Pitää aluslevyä ja ohjaa stanssia, mikä mahdollistaa tarkan ja puhtaan leimauksen, paremman suuntauksen ja kirjainten tasaisen välyksen



![image](assets/fr/05.webp)





- **Tiivistyslaitteet**: Sinetöity pussi tai sinetöintiliuska



![image](assets/fr/06.webp)





- **Hermeettisesti suljettu säiliö**: Aluslevypalojen säilyttämistä varten



![image](assets/fr/07.webp)


### 2.3 Turvallisuus





- Suositellaan **käsineitä** ja **suojalaseja**.
- **Putkiavain**, johon lyönti liu'utetaan, niin että lyöntiä pidetään kiinni putkiavaimella eikä sormilla.



### 2.4 Määrät ja arvioidut kustannukset





- **Määrä 24 sanan varmuuskopiota varten**: 1 Bolt, 1 siipimutteri, 1 lyöntisarja, 1 vasara/massetti, 1 alasin/tuki.





- **Kokonaiskustannukset**:
 - Aluslevyt ja pultit/mutterit: ~ 15 EUR
 - Lyöntisarja: ~ 45 EUR
 - Suojakotelo: ~ EUR
 - Kaikkien lisävarusteiden kanssa: ~ 140 EUR





- Katso lisäyksessä esimerkkilaitteita.




## 3. Vaiheittaiset ohjeet



1. ** Valmistautuminen:**




 - Yksityinen sijainti, ei kameroita (ei myöskään älypuhelimia)
 - Tukeva, iskuja vaimentava pinta
 - Käsineet ja suojalasit
 - Puhdista kaikki rasva ja lika pesukoneista
 - Harjoittelu testialuslevyillä


2. **Polttakaa Mnemonic-sanat** :




    - Kaiverra koko sana yhdelle puolelle. Älä rajoitu vain neljään ensimmäiseen kirjaimeen, jos neljäs kirjain vahingoittuu.
    - Lyö vasaralla lujasti ja pidä lyönti kiinni putkiavaimella


3. **Aluslevyjen lukumäärä** :




    - Kaiverra samalle puolelle sana position number, joka on välttämätön, jos aluslevyt irtoavat.


4. **Tallennustiedot** (valinnainen ja suositeltava) :




    - Kaiverretaan tarpeeton sana kiekon toiselle puolelle
    - Kaiverretaan Wallet-tunnus ylimääräiseen aluslevyyn
    - Kaiverra käyttämäsi tilin johdannaispolku ylimääräiseen aluslevyyn. Löydät tämän tiedon salkkuohjelmistosi asetuksista. Esimerkiksi tavallisessa Taproot-salkussa oletusarvoinen johdannaispolku on: `m / 86' / 0' / 0' /`
    - Kirjoita PIN-koodi, jolla avaat Hardware Wallet:n lukituksen, tai PIN-koodi, jos käytät COLDCARD-korttia.


5. **Älä polta passphrase :**




 - Jos käytät passphrase:a, varmista, ettet kirjoita sitä samalle kortille kuin Mnemonic:tä. passphrase on suunniteltu suojaamaan Wallet-korttiasi siinä tapauksessa, että Mnemonic varastetaan. Lisätietoja on liitteessä.


6. ** Tarkista luettavuus** :




    - Varmista, että jokainen sana ja numero on selkeä ja luettavissa.


7. **Kokoa aluslevyt** :




    - Kierrä aluslevyt Bolt:een numeroiden mukaisessa järjestyksessä.
    - Valinnainen: lisää päätyihin tyhjät aluslevyt.
    - Ruuvaa siipimutteri kiinni akun kiinnittämiseksi.
    - Kiristä tiukasti parantaaksesi suojaa vettä, tulta ja mekaanista rasitusta vastaan.


8. **Testi varmuuskopio** :




    - Yritä palauttaa salkku uudesta varmuuskopiosta
- **Varmuuskopion sinetöinti** (valinnainen ja suositeltava) :
 - Sinetöityinä nauhoina tai sinetöidyissä pusseissa.
 - Jos käytät pussia, merkitse muistiin sen yksilöllinen tunnistenumero, jotta voit tarkistaa, että kyseessä on oikea pussi eikä alkuperäisen pussin korvaava houkutuslintu.




## 4. Varastointi



### 4.1 Valitse sopiva paikka



Säilytä varmuuskopiot **huomaamattomassa paikassa**, joka on poissa näkyvistä ja johon pääsee säännöllisesti tarkistamaan ne. Valitse **tulenkestävä ja vesitiivis säilytyspaikka**, kotona tai **yksinomaisessa valvonnassasi** olevassa paikassa.



Vältä paikkoja, joissa olet riippuvainen kolmannesta osapuolesta (pankkikaappi, notaari): menetät itsenäisen pääsyn varoihisi, mikä on vastoin Bitcoin:n suvereniteettiperiaatteita.



Älä koskaan paljasta, että käytät Ninja SAFU -menetelmän kaltaista menetelmää. Vaitiolovelvollisuus on jo itsessään Layer-turvaa.



### 4.2 Redundanssi



Luo tarvittaessa **monia kopioita** ja säilytä niitä **eri maantieteellisissä paikoissa**.


Vaikka laitteeseen valitut materiaalit olisivat veden- ja palonkestäviä, et pääse käsiksi laitteeseen, jos se on haudattu kuutiometrien raunioiden alle kotonasi, ja sitä on hyvin vaikea, ellei jopa mahdoton, saada takaisin.




## 5. Seuranta ja ylläpito



Vaikka varmuuskopio olisi hyvin säilytetty, se on **tarkastettava säännöllisesti**:





- Tarkasta varmuuskopio **kerran tai kaksi kertaa vuodessa**.
- Jos **kaiverrukset heikkenevät**, luo uusi varmuuskopio, **testaa se** ja **hävitä vanha kopio** huolellisesti.
- Jos varmuuskopio on suljetussa pussissa :
 - Tarkista kirjautumisesi
 - Tarkista sen eheys
 - Avaa kirjekuori säännöllisesti tarkistaaksesi kaiverrusten kunnon, ja jos kaikki on kunnossa, laita varmuuskopio uuteen taskuun




**PYSY TURVASSA!**


![image](assets/fr/08.webp)




## LIITTEET



### A.1 Tallenna palautuslauseesi



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### A.2 passphrase:n BIP39:n ymmärtäminen



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

### A.3 Miten Bitcoin-salkut toimivat



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### A.4 Ninja SAFU -menetelmän luokittelu



Jameson Loppin mukaan:





- [Kertomus](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/) Ninja SAFU -menetelmästä





- Vertailutaulukko [täydellinen](https://jlopp.github.io/metal-Bitcoin-storage-reviews/?ref=blog.lopp.net)





- Osittainen taulukko :


![image](assets/fr/09.webp)



### A.5 Esimerkki laitteistosta





- **Aluslevyt** varten
 - [Titan](https://pleb.style/fr-fr/products/disques-de-seed-supplementaires-titan-Wallet)
- **Aluslevyt + mutteri + suojakotelo** (aluslevyille)
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-premium-acier-steel-Wallet-backup?variant=50022696419664)
 - [TerraSteel](https://pleb.style/fr-fr/products/terrasteel-Wallet-plebstyle-acier-backup)
- Rei'ityssarja
 - [PlebStyle](https://pleb.style/fr/products/schlagstempelset-a-z-0-9-3mm)
- **Tyypittelyn perusta**
 - [PlebStyle](https://pleb.style/fr/products/schlagunterlage-10cm-x-10cm-x-1-5cm)
- **Napautuslaite** (opas)
 - [TerraSteel](https://pleb.style/fr-fr/products/zubehor-einschlag-vorrichtung?_pos=1&_sid=2767fd66f&_ss=r)
- Tiivistyslaite
 - [Suljettu pussi](https://pleb.style/fr/products/zubehor-5x-sicherheitstasche-tamper-evident)
 - [Tiivistysnauhat](https://pleb.style/fr/products/zubehor-5x-siegel-streifen-fur-dein-seed-backup)
- **Täydellinen** paketti
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-diy-kit-premium-seed-backup-steelwallet-plebstyle?pr_prod_strat=e5_desc&pr_rec_id=aa9f36359&pr_rec_pid=8728733155664&pr_ref_pid=8730877788496&pr_seq=uniform)
 - [TerraSteel](https://pleb.style/fr-fr/products/kopie-von-terrasteel-Wallet-starter-kit)



Huomautus: Linkit verkkokauppoihin on annettu vain tiedoksi.


Plan B:n ja edellä mainittujen myyjien ja valmistajien välillä ei ole kaupallista kumppanuutta.


Plan B ei ole vastuussa virheistä, hinnanvaihteluista tai tuotteiden laatuun tai toimitukseen liittyvistä ongelmista. **DYOR**




### A.6 Kuvien lähteet



https://pleb.style/fr/


https://x.com/lopp/status/1463155802345193475


https://bitcointalk.org/index.php?topic=5389446.0


https://x.com/econoalchemist/status/1329271981712289797


https://www.waivio.com/@themarkymark/create-your-own-metal-seed-key-backup - varmuuskopion luominen


https://github.com/minibolt-guide/minibolt/blob/main/bonus/Bitcoin/safu-ninja.md