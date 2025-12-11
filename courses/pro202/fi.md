---
name: Ohjelmointi Bitcoin
goal: Rakenna täydellinen Bitcoin-kirjasto tyhjästä ja ymmärrä Bitcoin:n kryptografisia perusteita
objectives: 

 - Toteuta äärellisten kenttien aritmetiikkaa ja elliptisten käyrien operaatioita Pythonissa
 - Bitcoin-transaktioiden rakentaminen ja jäsentäminen ohjelmallisesti
 - Luo Testnet-osoitteita ja lähetä transaktioita verkossa
 - Bitcoin:n turvallisuusmallin perustana olevien matemaattisten perusteiden hallitseminen

---
# Matka Bitcoin:n käsikirjoituksiin ja ohjelmiin


Tämä intensiivinen kaksipäiväinen kurssi, jonka opettajana toimii Jimmy Song, vie sinut syvälle Bitcoin:n teknisiin perusteisiin rakentamalla täydellisen Bitcoin-kirjaston alusta alkaen. Aloitat äärellisten kenttien ja elliptisten käyrien keskeisestä matematiikasta ja etenet transaktioiden jäsentämisen, skriptien suorittamisen ja verkkokommunikoinnin kautta. Käytännönläheisten koodausharjoitusten avulla Jupyterin muistikirjoissa luot oman Testnet Address:n, rakennat transaktioita manuaalisesti ja lähetät ne suoraan verkkoon - ja samalla saat syvällisen ymmärryksen kryptografisista periaatteista, jotka tekevät Bitcoin:sta turvallisen ja Trustless:sta turvallisen.


Nauti löydöstäsi!


+++

# Johdanto

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Kurssin yleiskatsaus

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Tervetuloa kurssille PRO 202 _**Programming Bitcoin**_, intensiiviselle matkalle, joka vie sinut äärellisten kenttien aritmetiikasta aina todellisten tapahtumien rakentamiseen ja lähettämiseen Bitcoinin testiverkossa.

Tällä kurssilla rakennat vaiheittain Bitcoin-kirjaston Pythonissa samalla kun hankit kryptografiset, protokolla- ja ohjelmisto-osaamisen, jota tarvitaan Bitcoinin turvallisuuden ja sisäisen toiminnan täsmälliseen ymmärtämiseen. PRO 202 -lähestymistapa on täysin käytännönläheinen: jokainen käsite toteutetaan välittömästi Jupyter-muistikirjoissa, varmistaen, että teoria ja koodi vahvistavat toisiaan.

### Bitcoini keskeiset matemaattiset käsitteet

Tämä ensimmäinen osio luo välttämättömän matemaattisen perustan. Toteutat äärellisten kenttien aritmetiikan ja elliptisten käyrien operaatiot (ryhmälaki, yhteenlasku, kaksinkertaistus, skalaaritulo...) — ECDSA:n edellytykset. Tavoite on kaksitahoinen: ymmärtää algebraattinen rakenne, joka mahdollistaa kryptografiset allekirjoitukset, ja rakentaa luotettavia Python-työkaluja niiden käsittelyyn.

Tämän jälkeen muodollistat ECDSA:n komponentit: avaimen generoinnin, pisteiden muotoilun, hashauksen, allekirjoituksen luomisen ja tarkistamisen. Tämä osio yhdistää teorian suoraan käytäntöön ja korostaa toteutuksen yksityiskohtia sekä taustalla olevan turvallisuusmallin luotettavuutta.

### Bitcoin-siirron sisäinen toiminta

Toisessa osassa puret auki Bitcoin-siirron rakenteen: UTXO:t, syötteet/tulosteet, sekvenssit, skriptit, koodaukset ja paljon muuta. Kirjoitat koodia rakentaaksesi, allekirjoittaaksesi ja tarkistaaksesi siirtoja, saadaksesi tarkan käsityksen siitä, mitä hash sitouttaa ja miksi.

Seuraavaksi toteutat minimaalisen _Script_-suorittimen, tarkastelet keskeisiä opkoodeja ja validoit kulutuspolut. Tavoitteena on, että pystyt auditoimaan transaktioiden käyttäytymistä, diagnosoimaan validointivirheitä ja arvioimaan kulutuskäytäntöjen turvallisuutta.

### Bitcoin-verkon sisäinen toiminta

Kolmannessa osassa sijoitat transaktion laajempaan järjestelmään: lohkorakenne, otsikot, vaikeustaso ja Proof-of-Work-mekanismi. Käsittelet protokollaviestejä, lohko-otsikoita ja Merkle-puita.

Lopuksi tutkit vertaisverkkojen solmujen välistä viestintää, viestien optimointia ja SegWitin käyttöönottoa.

Kuten kaikilla Plan ₿ Academy -kursseilla, myös lopussa on arviointi, joka on suunniteltu vahvistamaan ymmärrystäsi. Oletko valmis paljastamaan Bitcoinin sisäisen toiminnan ja kirjoittamaan sen taustalla olevan koodin? Aloitetaan!

# Bitcoin:n keskeiset matemaattiset käsitteet

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Bitcoin:n täytäntöönpanon matematiikka

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptisen käyrän salaus

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin-transaktioiden sisäiset toiminnot

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Tapahtumien analysointi ja ECDSA-allekirjoitukset

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skriptien ja tapahtumien validointi

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Tapahtumien rakenne ja Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Verkon sisäiset rakenteet

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin-lohkot ja Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Verkkoviestintä ja Merkle-puut

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Kehittynyt solmuviestintä ja erotettu todistaja

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Viimeinen jakso


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Arvostelut & arvostelut


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Päätelmä


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
