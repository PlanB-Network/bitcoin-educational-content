---
name: BIP-85
description: Miten voin käyttää BIP-85:tä generate:n useiden siemenlauseiden muodostamiseen pää-seed:stä?
---
![cover](assets/cover.webp)



## 1. BIP-85:n ymmärtäminen



### 1.1 Mikä on BIP-85?



BIP-85 on edistynyt toiminto, jonka avulla voit luoda useita **seed-sekundäärilausekkeita** yhdestä **seed-päälausekkeesta**.



Kunkin seed-sekundäärilauseen avulla voidaan luoda täysin itsenäinen Bitcoin-salkku. Näitä salkkuja voidaan käyttää moniin eri tarkoituksiin: Hot Wallet matkapuhelimessa, salkku sukulaiselle, erillinen säästösalkku jne.



Kaikki seed-alalauseet ovat **matemaattisesti johdettuja**, mutta on **mahdotonta jäljittää alalauseesta takaisin seed-päälauseeseen**. Näin varmistetaan täydellinen erottelu kunkin salkun välillä.



Niin kauan kuin sinulla on pääsy seed-pääfraasiin (ja siihen liittyvään passphrase:aan, jos käytät sellaista), voit luoda minkä tahansa seed-sekundäärilauseen **identtisesti** ilman, että sinun tarvitsee tallentaa sitä erikseen.



### 1.2 Miksi käyttää BIP-85:tä?



BIP-85 on hyödyllinen, jos haluat :





- Luo useita itsenäisiä Bitcoin-salkkuja ilman useita varmuuskopioita
- Hallitse varoja eri käyttötarkoitusten mukaan (säästöt, menot, perhe, projektit)
- Turvatakuut sukulaisille ("Jim-setä" -toiminto)
- Poista salkku menettämättä pääsyä varoihisi
- Yksinkertaista tietoturvaa: vain yksi seed-avainlause suojaa



### 1.3 Etuja BIP-32:een verrattuna



BIP-32:n avulla yhtä ainoaa seed-lauseen osaa voidaan käyttää generate:n tilien ja osoitteiden täydelliseen Bitcoin-hierarkiaan käyttäen johdannaispolkuja (esimerkiksi: `m/44'/0'/0'/0'/0/0`). Kukin polku voi edustaa erillistä tiliä, mutta **kaikki pysyvät yhteydessä samaan seed-lauseeseen**. Jos siis tämä seed-lause vaarantuu, **kaikki johdetut tilit tulevat saataville**.



BIP-85:n avulla seed-päälausetta voidaan käyttää generate:n useisiin täysin itsenäisiin seed-sivulauseisiin: **jos yksi näistä toissijaisista siemenistä vaarantuu, hyökkääjä ei voi koskaan palata seed-päälauseeseen tai päästä käsiksi muihin salkkuihin**.


Tämä mahdollistaa riskien lokeroimisen:





- Voit käyttää toissijaista seed:a Hot Wallet:ää tai tilapäistä käyttöä varten ja hyväksyä suuremman altistuksen.
- Vaikka tämä Hot Wallet vaarantuisi, muut varasi, jotka on suojattu muilla toissijaisilla siemenillä tai säilytetty offline-tilassa, **pysyvät turvassa**.



Toisaalta sekä BIP-32:n että BIP-85:n osalta **kaikki rahastot ovat haavoittuvaisia**, jos pää-seed on vaarassa. Siksi on ratkaisevan tärkeää suojata se mahdollisimman korkealla turvallisuustasolla.



![image](assets/fr/02.webp)


## 2. BIP-85:n käytännön käyttötapaukset



BIP-85:n avulla voit luoda useita Bitcoin-salkkuja yhdestä seed-ydinlausekkeesta, joista jokaisella on oma seed-sekundaarilauseke. Seuraavassa on viisi käytännön käyttötapausta Bitcoin-varojen järjestämiseen ja turvaamiseen. Jokainen tapaus selittää, miksi BIP-85:n käyttö on käytännöllisempää kuin useiden tilien hallinta yhdellä seed-lauseella BIP-32:n avulla.



### 2.1 Epävarmasta salkusta aiheutuvan riskin rajoittaminen





- Skenaario**: Hot Wallet" Wallet (asennettu Internet-yhteydellä varustettuun laitteeseen) päivittäisiin tapahtumiin.
- Ratkaisu BIP-85**: Luodaan tälle salkulle omistettu seed-sekundäärilause.
- Etu BIP-32:een** verrattuna: Sinun ei tarvitse tuoda seed:n ensisijaista lausetta puhelimeesi, mikä vähentää hakkeroinnin riskiä. Vain seed:n toissijainen lauseke vaarantuu, mikä suojaa muita lompakoitasi. BIP-32:ssa sinun on käytettävä seed-päälausetta ja ohitusreittiä, jolloin kaikki varasi paljastuvat.



### 2.2 Luo salkku perheenjäsenelle





- Skenaario**: Bitcoin Wallet jollekin läheisellesi (esim. äidillesi), mutta voit palauttaa sen, jos hän kadottaa sen.
- Ratkaisu BIP-85**: seed:n toissijaisen lauseen luominen ja vain tämän lauseen jakaminen.
- Etu BIP-32:een** verrattuna: Tämä vaarantaa kaikki varasi ja vaikeuttaa läheisesi hallinnointia (haarautumispolkujen hallinnointi), tai sitten on luotava uusi seed-lause, joka tallennetaan seed-lauseen lisäksi.



### 2.3 Erillisten salkkujen hallinnan helpottaminen





- Skenaario**: Erittelet bitcoinisi eri tarkoituksiin (esim. pitkäaikaiset säästöt, muut kuin KYC-varat).
- Ratkaisu BIP-85**: Luodaan seed toissijaisia lauseita, jotka on omistettu kullekin tavoitteelle.
- Etu BIP-32:een** verrattuna: Tämä vaikeuttaa hallintaa kolmannen osapuolen salkuissa, koska se edellyttää johdannaispolkujen, kuten `m/44'/0'/0'/0'`, hallintaa. Lisäksi ei ole mahdollista määrittää erillistä tiliä laitekohtaisesti (esim. "säästöt Coldcardilla", "päivittäiset matkapuhelimella", "lomat Trezorilla"). BIP-85 määrittää jokaista tavoitetta kohden yksilöllisen seed-sekundäärilauseen, joka on helppo tunnistaa ja tuoda erikseen jokaiseen laitteeseen.



### 2.4 Väliaikaisen Wallet:n käyttäminen tapahtumia varten





- Skenaario**: Tarvitset tilapäisen salkun kertaluonteista transaktiota varten tai luottamuksellisuuden säilyttämiseksi (esim. varojen sekoittaminen, vuorovaikutus Exchange KYC:n kanssa jne.).
- Ratkaisu BIP-85**: seed:n toissijaisen lauseen luominen, sen käyttäminen transaktioon ja sen tuhoaminen tarvittaessa tietäen, että se voidaan luoda uudelleen.
- Etu BIP-32:een** verrattuna: BIP-32:ssa väliaikainen tili on riippuvainen seed:n päälausekkeesta, jolloin kaikki varasi ovat vaarassa, jos ne vaarantuvat.





## 3. Ennen kuin aloitat





- Laitteisto** (valinnainen)
 - Coldcard Mk4 tai Q1
 - MicroSD-kortti





- Perustiedot
 - Mnemonic-lausekkeiden ymmärtäminen (BIP-39): 12-24 sanan luettelo portfolion tallentamiseksi.
 - Tiedä, mikä Bitcoin Wallet on: ohjelmisto tai laite, jolla voit hallita bitcoinejasi, ja miten se palautetaan Mnemonic-lauseella.
 - Lisää resursseja liitteissä.





- Yhteensopiva** ohjelmisto
 - Sparrow wallet (tietokone, pelkkää valvontaa tai edistynyttä hallintaa varten)
 - Nunchuck (mobiili, useita allekirjoituksia varten)
 - BlueWallet (mobiili)
 - ...





- 3.4 Kylmäkortin** kokoonpano
 - Alusta 24 sanan seed-lause Coldcard-kortille.
 - Valinnainen: Lisää passphrase turvaamaan pääsy BIP-85:n haaroihin.
 - Aktivoi hyödylliset vaihtoehdot: NFC (vientiä varten), USB:n kytkeminen pois päältä akulla (turvallisuus).




## 4. Vaiheittainen opetusohjelma



Noudata seuraavia ohjeita, kun haluat luoda, käyttää ja hakea toissijaisen Mnemonic:n BIP-85:llä Coldcard-kortillasi.



### 4.1 generate a seed toissijainen lause



Luot seed-päälausekkeestasi seed:n toissijaisen lausekkeen.


Kytke Coldcard-kortti päälle ja syötä PIN-koodi.





- 1. Jos olet liittänyt passphrase:n seed:n päälaitteeseen:**
 - Siirry aloitusnäytöstä kohtaan "passphrase".
    - Valitse `Add Word` ja syötä salasanasi.
    - Paina `Apply`.
    - Tarkista Wallet:n tunnistetiedot: Wallet:n sormenjälki: Mene kohtaan `Advanced > View Identity` (Lisäasetukset > Näytä identiteetti).





- 2. Siirry BIP-85**-valikkoon
 - Siirry aloitusnäytöstä kohtaan "Lisäasetukset > Johdanto seed B85"
 - Lue varoitus ja vahvista.



ColdCard ilmoittaa, että luodut siemenet ovat matemaattisesti johdettu pää-seed:stä, mutta salauskieleltään täysin riippumattomia.


![image](assets/fr/03.webp)





- 3. Valitse muoto


Valitse seed-lauseen muoto: 12, 18 tai 24 sanaa. Tarkista sanojen määrä, jonka Wallet hyväksyy ja johon haluat tuoda seed-lauseen.


![image](assets/fr/04.webp)





- 4. Valitse indeksi
 - Syötä indeksi väliltä 0-9999.
 - Tämä indeksi on ratkaisevan tärkeä sekundaarisen seed:n uudistamiseksi myöhemmin. Säilytä se huolellisesti merkinnällä, kuten: "Indeksi 1 = Wallet mobile", "Indeksi 2 = perheprojekti", "Indeksi 4 = testisekoitus", ....
 - Jos kadotat sen, et menetä rahojasi, mutta sinun on testattava yhdistelmiä 0:sta 9999:ään löytääkseen ne.


![image](assets/fr/05.webp)





- 5. Huomautus tai vienti seed:n toissijainen lause**


ColdCard näyttää nyt uuden seed:n toissijaisen lauseen. Voit :




 - **Nota käsin**.
 - Lehdistö :
     - 1` tallentaa sen SD-kortille
     - `2` siirtääksesi "käytä tätä seed:ta "** tilaan ColdCardissa (hyödyllinen tapahtuman viemisessä tai allekirjoittamisessa)
     - 3` näyttääksesi **QR-koodin** (skannattava mobiilisovelluksella, kuten BlueWallet tai Nunchuck)
     - 4` lähettääksesi sen **NFC**:llä**



💡 Tässä vaiheessa sinulla on itsenäinen seed-lause, jota voidaan käyttää missä tahansa Wallet BIP39:ssä (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Toissijaisen seed:n käyttö



Voit nyt käyttää tätä johdettua seed:ää uuden salkun luomiseen :




- mobiilisovellus
- toinen Hardware Wallet
- gW-69-salkku



### 4.3 Kadonneen seed-sekundäärilauseen palauttaminen



Voit hakea toisen seed:n milloin tahansa toistamalla prosessin:


1. Käynnistä ColdCard uudelleen


2. Anna PIN-koodi


3. Syötä passphrase, jos se on määritelty


4. Siirry kohtaan `Advanced > Derive seed B85`


5. Valitse muoto (12/18/24 sanaa)


6. Syötä sama indeksi (esim. `1`)


7. Saat täsmälleen saman toissijaisen seed:n




## 5. Rajoitukset, riskit ja parhaat käytännöt



### 5.1 Riippuvuus seed-päälauseesta + passphrase:stä



BIP85:n käyttö perustuu täysin 24 sanan seed-päälauseeseen sekä passphrase:ään, jos olet käyttänyt sitä.




- Näistä kahdesta Elements:stä voidaan luoda kaikki seed:n toissijaiset lausekkeet.
- Ilman yhtä näistä kahdesta Elements:stä menetät pääsyn kaikkiin johdannaissalkkuihin.



### 5.2 Usean allekirjoituksen kokoonpanoon liittyvät riskit



Suosittelemme, että multi-sig-kokoonpanossa ei käytetä toissijaisia seed-lausekkeita, jotka on luotu samasta ensisijaisesta seed-lausekkeesta: jos laite tai ensisijainen seed-lauseke vaarantuu, hyökkääjä voi luoda uudelleen kaikki multi-sig-avaimet.



### 5.3 Ohjelmistojen yhteensopivuus



Kaikki sovellukset eivät suoraan tue BIP85-alkuperäämistä. BIP85:n avulla tuotetut siemenet ovat kuitenkin tavallisia BIP39-siemeniä (12, 18 tai 24 sanaa), joten niitä voidaan käyttää missä tahansa BIP39-yhteensopivassa portfoliossa.



### 5.4 BIP85-tilirekisteri



On suositeltavaa pitää ajan tasalla olevaa henkilökohtaista rekisteriä seed:n toissijaisista lausekkeista.




- Sen avulla voit nopeasti selvittää, mikä BIP85-indeksi vastaa mitä salkkua, ilman että sinun tarvitsee pitää seed:n toissijaisia lauseita.
- Tämän rekisterin olisi oltava minimalistinen, eikä siinä pitäisi olla nimenomaista mainintaa Bitcoin:sta, ja se olisi tallennettava erillään seed:n päärekisteristä. Muista mainita se perintösuunnitelmassasi.



Rekisteri voi sisältää :




- bIP85 käytetty indeksi (luku 0-9999)
- käyttö- tai viitenimi (esim. Hot Wallet, henkilökohtaiset säästöt, Wallet äidiltä)
- tarvittaessa Wallet:n sormenjälki ColdCardissa tapahtuvaa tarkistusta varten



### 5.5 Varmuuskopiointi



Varmuuskopioiden on sisällettävä :




- gW-91:n pääreitti
- gW-76 (jos käytetään)



Älä koskaan säilytä yhdessä:




- gW-93- ja passphrase-pääsarjat
- pää seed ja BIP85-tilirekisteri



Lisää resursseja liitteissä.




## LIITTEET



## A.1 Sanasto





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed-lause](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Tallenna palautuslauseesi



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 passphrase-rajatarkastusaseman39 ymmärtäminen



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Miten Bitcoin-salkut toimivat



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f