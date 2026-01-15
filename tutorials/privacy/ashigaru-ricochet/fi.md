---
name: Ashigaru - Ricochet
description: Ricochet-tapahtumien ymmärtäminen ja käyttö
---
![cover ricochet](assets/cover.webp)



> *Premium-työkalu, joka lisää ylimääräistä historiaa tapahtumiin. Poista mustat listat ja auta suojautumaan epäoikeudenmukaisilta kolmannen osapuolen tilien sulkemisilta.*

## Mikä on Ricochet?



Ricochet on tekniikka, joka koostuu useiden fiktiivisten transaktioiden suorittamisesta itseä kohti, jotta voidaan simuloida bitcoinin omistusoikeuden siirtoa. Tämä työkalu eroaa Ashigarun muista transaktioista (jotka on peritty Samurai Wallet:ltä) siinä, että se ei tarjoa prospektiivista anonymiteettiä, vaan pikemminkin eräänlaisen retrospektiivisen anonymiteetin. Itse asiassa Ricochet hämärtää ne erityispiirteet, jotka voivat vaarantaa Bitcoin-osan vaihdettavuuden.



Jos esimerkiksi teet coinjoinin, sekoituksesta tuleva osa tunnistetaan sellaiseksi. Ketjuanalyysityökalut pystyvät havaitsemaan coinjoin-tapahtumien osat ja antamaan niistä tuleville kappaleille merkinnän. Itse asiassa coinjoinilla pyritään katkaisemaan kolikon historialliset yhteydet, mutta sen kulku coinjoinien läpi pysyy havaittavana. Tämä ilmiö on verrattavissa tekstin salaamiseen: vaikka alkuperäistä tekstiä ei voi käyttää selvänä tekstinä, on helppo tunnistaa, että sitä on salattu.



Merkintä "coinjoined" voi vaikuttaa UTXO:n korvattavuuteen. Säännellyt yksiköt, kuten vaihtoportaat, voivat kieltäytyä hyväksymästä coinjoined UTXO:ta tai jopa vaatia sen omistajalta selityksiä, jolloin vaarana on, että tilisi suljetaan tai varasi jäädytetään. Joissakin tapauksissa foorumi voi jopa ilmoittaa käyttäytymisestäsi valtion viranomaisille.



Tässä kohtaa Ricochet-menetelmä astuu kuvaan. Kolikkoliitoksen jättämän jäljen häivyttämiseksi Ricochet suorittaa neljä peräkkäistä tapahtumaa, joissa käyttäjä siirtää varojaan itselleen eri osoitteisiin. Tämän transaktiosarjan jälkeen Ricochet-työkalu ohjaa bitcoinit lopulta lopulliseen määränpäähänsä, esimerkiksi vaihtoalustalle. Tarkoituksena on luoda etäisyyttä alkuperäisen coinjoin-transaktion ja lopullisen rahankäytön välille. Tällä tavoin lohkoketjuanalyysityökalut olettavat, että omistusoikeus on todennäköisesti siirtynyt coinjoinin jälkeen ja että sen vuoksi ei ole tarvetta ryhtyä toimenpiteisiin liikkeeseenlaskijaa vastaan.



![image](assets/fr/01.webp)



Ricochet-menetelmän kohdalla voisi kuvitella, että ketjuanalyysiohjelmisto syventäisi tarkasteluaan neljän pompun jälkeen. Näillä alustoilla on kuitenkin ongelma havaintokynnyksen optimoinnissa. Niiden on määriteltävä kynnysarvo hyppyjen lukumäärälle, jonka jälkeen ne hyväksyvät, että omistajanvaihdos on todennäköisesti tapahtunut ja että linkki aiempaan coinjoiniin olisi jätettävä huomiotta. Tämän kynnysarvon määrittäminen on kuitenkin riskialtista: jokainen havaittujen hyppyjen määrän kasvu lisää eksponentiaalisesti väärien positiivisten tulosten määrää, toisin sanoen henkilöitä, jotka on virheellisesti merkitty coinjoinin osallistujiksi, vaikka tosiasiassa operaation on suorittanut joku muu. Tämä skenaario on suuri riski näille yrityksille, sillä väärät positiiviset tulokset johtavat tyytymättömyyteen, joka voi ajaa asianomaiset asiakkaat kilpailemaan. Pitkällä aikavälillä liian kunnianhimoinen tunnistuskynnys johtaa siihen, että foorumi menettää enemmän asiakkaita kuin sen kilpailijat, mikä voi uhata sen elinkelpoisuutta. Sen vuoksi näiden alustojen on hankala lisätä havaittujen pomppujen määrää, ja 4 on usein riittävä määrä niiden analyysien vastapainoksi.



Näin ollen **Ricochetin yleisin käyttötapaus syntyy, kun on tarpeen salata aiempi osallistuminen coinjoiniin omistamallasi UTXO:lla.** Ihannetapauksessa on parasta välttää coinjoinin läpikäyneiden bitcoinien siirtämistä säännellyille yhteisöille. Jos muuta vaihtoehtoa ei kuitenkaan ole, erityisesti silloin, kun bitcoinit on kiireellisesti realisoitava valtion valuutassa, Ricochet tarjoaa tehokkaan ratkaisun.



## Miten Ricochet toimii Ashigarussa?



Ricochet on yksinkertaisesti menetelmä, jolla voi lähettää bitcoineja itselleen, ja sen keksivät alun perin Samurai Wallet:n kehittäjät. Ricochet on siis täysin mahdollista simuloida manuaalisesti ilman erikoistyökalua. Niille, jotka haluavat automatisoida prosessin ja nauttia samalla hiotummasta lopputuloksesta, Ashigaru-sovelluksen (joka on Samourai fork) kautta saatavilla oleva Ricochet-työkalu on kuitenkin hyvä ratkaisu.



Koska Ashigaru veloittaa palvelustaan, Ricochet maksaa 100 000 sats palvelumaksuna ja lisäksi mining-maksun. Sen käyttöä suositellaan siksi suurten summien siirtoihin.



Ashigaru-sovellus tarjoaa kaksi Ricochet-vaihtoehtoa:





- Vahvistettu Ricochet eli "porrastettu toimitus", jonka etuna on Ashigarun palvelumaksujen jakautuminen viidelle peräkkäiselle tapahtumalle. Tällä vaihtoehdolla varmistetaan myös, että jokainen transaktio lähetetään erillisenä ajankohtana ja kirjataan eri lohkoon, mikä jäljittelee mahdollisimman hyvin omistajanvaihdoksen käyttäytymistä. Vaikka tämä menetelmä on hitaampi, se on parempi niille, joilla ei ole kiire, sillä se maksimoi Ricochetin tehokkuuden vahvistamalla sen vastustuskykyä ketjuanalyysille;





- Klassinen Ricochet, joka on suunniteltu suorittamaan operaatio nopeasti ja lähettämään kaikki tapahtumat lyhennetyssä ajassa. Tämä menetelmä tarjoaa siis vähemmän luottamuksellisuutta ja vähemmän vastustuskykyä analyysille kuin vahvistettu menetelmä. Sitä tulisi käyttää vain kiireellisiin lähetyksiin.



## Miten tehdä Ricochet Ashigarulle?



Ashigarun rysäyksen tekeminen on hyvin yksinkertaista: aktivoi vain vastaava vaihtoehto, kun luot lähetystapahtuman. Klikkaa aluksi `+`-painiketta, sitten `Lähettää` ja valitse tili, jolta haluat lähettää varoja.



![Image](assets/fr/02.webp)



Täytä tapahtuman tiedot: lähetettävä summa ja vastaanottajan lopullinen osoite Ricochet-hyppyjen jälkeen. Valitse sitten "Ricochet"-vaihtoehto.



![Image](assets/fr/03.webp)



Tämän jälkeen voit valita teoriaosassa käsitellyn kahden Ricochet-tilan välillä: joko klassisen Ricochetin, jossa kaikki tapahtumat sisältyvät samaan lohkoon, tai porrastetun toimituksen, joka parantaa Ricochetin laatua pidemmän viiveen kustannuksella.



Kun olet tehnyt valintasi, vahvista valinta painamalla näytön alareunassa olevaa nuolta.



![Image](assets/fr/04.webp)



Seuraavalla näytöllä näet täydellisen yhteenvedon tapahtumastasi. Täällä voit myös säätää Ricochet-tapahtumien maksua markkinaolosuhteiden mukaan. Jos olet tyytyväinen kaikkeen, vedä vihreää nuolta allekirjoittaaksesi ja jakaaksesi Ricochet-tapahtumat.



![Image](assets/fr/05.webp)



Odota, kun eri hypyt suoritetaan automaattisesti.



![Image](assets/fr/06.webp)



Tapahtumasi on lähetetty onnistuneesti.



![Image](assets/fr/07.webp)



Olet nyt täysin perehtynyt Ashigaru-sovelluksen Ricochet-vaihtoehtoon. Jos haluat mennä pidemmälle, suosittelen sinua osallistumaan BTC 204 -koulutuskurssilleni, jossa opit yksityiskohtaisesti, miten voit vahvistaa ketjussa olevaa luottamuksellisuuttasi.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c