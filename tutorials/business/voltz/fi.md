---
name: Voltz
description: Kaikki yhdessä Lightning wallet yrityksellesi.
---

![cover](assets/cover.webp)



Idea Voltz-alustasta tuli ryhmältä bitcoin-käyttäjiä, jotka halusivat tarjota oman bitcoin wallet -palvelun. Tuloksena oli täydellinen infrastruktuuri bitcoinien hyväksymiseksi vähittäiskaupassa. Tässä opetusohjelmassa viemme sinut tutustumaan Voltziin ja alustan tarjoamiin bitcoin-integraatiomahdollisuuksiin.



## Voltzin käytön aloittaminen



Sen lisäksi, että Voltz on Lightning wallet, jonka avulla voit lähettää, vastaanottaa ja maksaa päivittäin, Voltz on täydellinen alusta, joka tarjoaa lukuisia laajennuksia bitcoinin integroimiseksi myyntipisteeksi tai markkinapaikaksi liiketoimintaasi.



Mene [Voltz]-alustalle (https://www.lnvoltz.xyz/en) ja luo tili klikkaamalla "Kokeile nyt" -painiketta.



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ On tärkeää, että asetat vahvan aakkosnumeerisen salasanan, joka lisää mahdollisuuksiasi brute-force-hyökkäyksiä vastaan, ja tarkistat, että olet todellakin Voltzin virallisella verkkosivustolla, kun täytät kirjautumistietosi, jotta suojaudut phishingiltä.



Voltzin käyttöliittymä on hyvin samanlainen kuin LnBits-alustan käyttöliittymä.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz on itse asiassa rakennettu LnBits-palvelimelle; tutustu opetusohjelmaamme, josta opit, miten voit asentaa omat LnBits-palvelimesi ja rakentaa ratkaisusi niiden päälle.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Alustan avulla voit hallita tehokkaasti useita salkkuja. Kun rekisteröidyt, sinulla on oletuksena automaattisesti Lightning-salkku. Voit kuitenkin lisätä muita salkkuja.



![wallets](assets/fr/03.webp)



### Siirrettävyys



Voltz ei rajoitu pelkästään verkkokäyttöliittymään: kohdassa **Mobile Access** voit yhdistää aktiivisen Voltz wallet:n sovelluksiin, kuten Zeus tai Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Tätä varten sinun on asennettava ja aktivoitava **LndHub**-laajennus alustalle.



![lndhub](assets/fr/04.webp)



Valitse aktiivinen Voltz-salkkusi ja skannaa asianmukainen QR-koodi sen mukaan, mitä oikeuksia haluat myöntää.




- Laskujen QR-koodin avulla voit vain lukea salkkuhistoriaasi ja generate:n uusia laskuja.
- Ylläpitäjän QR-koodin avulla voit tarkastella historiatietoja, generate-laskuja ja myös maksaa salamalaskut.



![qrs](assets/fr/05.webp)



Tässä opetusohjelmassa kytkemme Voltz wallet:n Blue Wallet-sovellukseen.



![connect](assets/fr/06.webp)



Kun salkkumme on yhdistetty, kaikki toiminnot synkronoidaan Blue Wallet:n ja Voltzin välillä. Kun esimerkiksi generate tekee laskun Blue Wallet:ssä, sillä on myös historia Voltzissa.



![sync](assets/fr/07.webp)



**Salkun määritys** -osiossa on minimiparametrit, kuten salkun nimen mukauttaminen ja valuutta, jolla haluat vastaanottaa maksut.



![config](assets/fr/08.webp)



### Laajennukset



Yksi Voltz-alustan erityispiirteistä on sen modulaarisuus, jonka ansiosta voit aktivoida tarvitsemasi laajennukset. Luettelo laajennuksista löytyy **Laajennukset** -valikosta.



![extensions](assets/fr/09.webp)



Näiden laajennusten joukossa on TPoS, myyntipisteen päätelaite, jota voit käyttää varaston pitämiseen ja maksujen keräämiseen asiakkailta.



![tpos](assets/fr/10.webp)



Myyntipäätteestä voit :




- Hanki verkkosivu, jonka voit jakaa asiakkaidesi ja kumppaneidesi kanssa;
- Tuotevaraston hallinta;
- Luo Lightning-laskuja;
- Käteismaksut Bolt-korteilla.



Laajennus on saatavana ilmaisena versiona ja maksullisena versiona, jossa on enemmän kehittyneitä ominaisuuksia. Voit luoda kassapäätteen napsauttamalla laajennuksen logon alla olevaa **Avaa**-painiketta ja napsauttamalla sitten **Uusi kassapiste**.



![new_tpos](assets/fr/11.webp)



Määrittele myyntipisteesi nimi ja liitä Voltz wallet sitten maksujen keräämistä varten päätelaitteeseen. Voit aktivoida juomarahat merkitsemällä **Activate gratuities** (Aktivoi juomarahat**) -valintaruudun. Aktivoi myös laskujen tulostusvaihtoehto, jos haluat antaa kuitit asiakkaillesi (tämä toiminto on vielä kehitteillä, joten siinä voi esiintyä toimintahäiriöitä).



Myyntipäätteessä on myös verokokoonpano, kun haluat soveltaa maasi veroa suoraan tuotteisiisi.



![tpos](assets/fr/12.webp)



Kun kassapäätteesi on luotu, voit lisätä siihen valmiiksi konfiguroituja tuotteita ja palveluita, jotta maksaminen ja kirjanpito sujuvat sinulle ja asiakkaillesi.



![product](assets/fr/13.webp)



Luo tuotteesi määrittelemällä niiden nimi, lisäämällä kuva ja asettamalla myyntihinta.  Voit luokitella tuotteesi helpompaa seurantaa varten. Voit soveltaa veroja suoraan tiettyyn tuotteeseen. Jos tuotteeseen ei ole sovellettu veroa, myyntipäätteen luomisvaiheessa määritetty vero sovelletaan automaattisesti.



![products](assets/fr/14.webp)



Voit tuoda tuoteluettelosi automaattisesti JSON-muodossa napsauttamalla **Tuonti/Vienti**-painiketta.



![exports](assets/fr/15.webp)



Pääset kassa-alueelle linkin kautta napsauttamalla **Uusi välilehti** -kuvaketta tai voit jakaa kassapalvelualustasi QR-koodin kautta asiakkaillesi napsauttamalla **QR-koodi** -kuvaketta.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Asiakkaasi voivat tutustua luetteloosi ja suorittaa maksunsa tästä käyttöliittymästä.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



Käytettävissä olevien laajennusten joukosta löydät myös työkaluja, kuten **Invoice**- ja **Payment Link**-laajennukset, joiden avulla voit kerätä generate-laskuja, joissa on tiettyjä tuotteita, jotta voit kerätä yksittäisiä maksuja ilman POS-päätteen kautta.



## Seuraa maksuja



Valikossa **Maksut** Voltz antaa sinulle yleiskatsauksen eri salkkuihin suoritetuista maksuista.


Voit seurata maksujasi :




- Tilanne.
- Merkintä: esimerkiksi **TPOS** myyntipisteen maksuja varten ja **lnhub** Zeus- ja Blue Wallet-lompakoiden mobiiliyhteyden kautta.
- Kokoelmasalkku.
- Saapuvien ja lähtevien maksujen kokonaismäärä.
- Tarkkaan määritelty ajanjakso.



![payments](assets/fr/22.webp)



## Lisää vaihtoehtoja



Voltz on myös infrastruktuuri, jolle voit rakentaa omia ratkaisuja. Osiossa **Laajennukset** on opas omien laajennusten kehittämiseen Voltzin ja LnBitsin ekosysteemissä.



![build](assets/fr/23.webp)



Jos haluat kehittää ratkaisuja ekosysteemin ulkopuolella, mutta käyttää silti niiden infrastruktuuria, löydät solmun **URL-osasta** API-avaimet ja dokumentointitiedot sekä esimerkin siitä, mitä voit tehdä näillä tiedoilla.



Voit luoda Lightning-laskuja sovelluksistasi Voltz wallet:n avulla, maksaa Lightning-laskuja, purkaa ja tarkistaa laskuja.



![keys](assets/fr/24.webp)



Nyt sinulla on hyvä käsitys Voltzista. Jos pidit tästä opetusohjelmasta, olemme varmoja, että opit lisää parhaista menetelmistä ja työkaluista, joilla voit integroida bitcoinin liiketoimintaasi kurssimme avulla: Bitcoin yrityksille.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a