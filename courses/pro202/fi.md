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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Bitcoin:n täytäntöönpanon matematiikka

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptisen käyrän salaus

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin-transaktioiden sisäiset toiminnot

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Tapahtumien analysointi ja ECDSA-allekirjoitukset

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skriptien ja tapahtumien validointi

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Tapahtumien rakenne ja Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Verkon sisäiset rakenteet

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin-lohkot ja Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Verkkoviestintä ja Merkle-puut

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Kehittynyt solmuviestintä ja erotettu todistaja

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Viimeinen jakso


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Arvostelut & arvostelut


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Päätelmä


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
