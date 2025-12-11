---
name: BIP47 - PayNym
description: Käytä uudelleenkäytettävää maksukoodia Ashigarussa
---
![cover](assets/cover.webp)



Pahin yksityisyysvirhe, jonka Bitcoin:ssä voi tehdä, on osoitteiden uudelleenkäyttö. Aina kun samaan osoitteeseen maksetaan useita maksuja, nämä maksutapahtumat yhdistetään toisiinsa, jolloin maailma saa kartan tapahtumistasi. Siksi on erittäin suositeltavaa, että käytät generate:ssa aina yksilöllistä osoitetta jokaista kuittia varten. Joissakin Bitcoin-sovelluksissa tämä ei kuitenkaan ole yksinkertainen asia.



Justus Ranvierin vuonna 2015 ehdottama BIP47 tarjoaa tyylikkään vastauksen tähän ongelmaan. Siinä otetaan käyttöön **kierrätettävän maksukoodin** käsite: yksilöllinen tunniste, jonka avulla voidaan vastaanottaa lähes rajaton määrä bitcoin-maksuja ketjussa ilman, että osoitetta tarvitsee koskaan käyttää uudelleen. ECDH-vaihtoon (*Diffie-Hellman on elliptic curves*) perustuvan kryptografisen mekanismin ansiosta jokainen maksu samalle koodille johtaa tyhjään osoitteeseen, joka vastaa lähettäjän ja vastaanottajan välistä suhdetta.



![Image](assets/fr/01.webp)



Tämä BIP47-periaate on toteutettu erityisesti **PayNym**-järjestelmässä, joka on alun perin Samourai Wallet:n kehittämä ja nyt Ashigarun käyttöön ottama järjestelmä. Tässä oppaassa tarkastelemme, miten voit aktivoida PayNymin, vaihtaa maksukoodeja kirjeenvaihtajan kanssa ja suorittaa maksutapahtumia ilman osoitteen uudelleenkäyttöä.



En käsittele tässä BIP47:n yksityiskohtaista toimintaa. Jos haluat syventyä aiheeseen, katso BTC 204 -koulutuskurssini luku 6.6.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Edellytykset



Tämän ohjeen seuraamiseen tarvitset vain wallet:n Ashigaru-sovelluksessa. Jos et tiedä, miten ladata, tarkistaa, asentaa sovellus tai luoda wallet, suosittelen, että tutustut ensin tähän opetusohjelmaan:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Pyydä PayNym



Ensimmäinen vaihe on PayNymin hakeminen. Tämä toimenpide on tehtävä vain kerran wallet:ää kohden. Se yhdistää seed:stä (`PM...`) saadun BIP47-maksukoodin ja PayNym-toteutukselle ominaisen yksilöllisen tunnisteen. Tämän lyhyemmän ja luettavamman tunnisteen voi sitten lähettää kirjeenvaihtajillesi vaihtojen helpottamiseksi ilman, että sinun tarvitsee jakaa pitkää ja täydellistä BIP47-koodia.



Napsauta PayNym-kuvaasi käyttöliittymän vasemmassa yläkulmassa ja sitten maksukoodia `PM...`.



![Image](assets/fr/02.webp)



Napsauta sitten kolmea pientä pistettä oikeassa yläkulmassa ja valitse `Claim PayNym`.



![Image](assets/fr/03.webp)



Vahvista klikkaamalla `CLAIM YOUR PAYNYM` -painiketta.



![Image](assets/fr/04.webp)



Päivitä sivu: PayNym-tunnuksesi näkyy nyt kuvasi alapuolella, aivan BIP47-maksukoodisi yläpuolella.



![Image](assets/fr/05.webp)



PayNym on nyt aktiivinen ja valmis käytettäväksi ensimmäisiin BIP47-tapahtumiin.



## Yhdistä yhteyshenkilön kanssa



PayNymin välillä on kahdenlaisia yhteyksiä: **seuraa** ja **liitä**. `seuraa`-toiminto on täysin maksuton. Se luo yhteyden kahden PayNymin välille Sorobanin kautta, joka on Samourai-tiimin kehittämä ja Ashigarun käyttöön ottama Tor-pohjainen salattu viestintäprotokolla. Tämän linkin avulla kaksi toisiaan seuraavaa käyttäjää voi vaihtaa tietoja yksityisesti, erityisesti koordinoidakseen yhteistoiminnallisia tapahtumia, kuten Stowaway tai StonewallX2, joita tarkastelemme toisessa opetusohjelmassa. Tämä vaihe on PayNymille ominainen, eikä se kuulu BIP47-protokollaan.



![Image](assets/fr/06.webp)



Yhteyden muodostaminen (`connect`) puolestaan edellyttää on-chain-tapahtumaa. Se koostuu ilmoitustapahtuman suorittamisesta BIP47:ssä määritellyllä tavalla. Tämä Bitcoin-tapahtuma sisältää metatietoja OP_RETURN-tulosteessa, joka luo salatun viestintäkanavan maksajan ja vastaanottajan välille. Tästä kanavasta maksaja voi generate-käytössä antaa kullekin maksulle yksilölliset vastaanottajaosoitteet, ja vastaanottajalle ilmoitetaan näistä maksuista, ja hän voi generate-käytössä käyttää osoitteisiin liittyviä yksityisiä avaimia, jotta hän voi käyttää nämä varat myöhemmin.



Ilmoitustapahtumasta aiheutuu kustannuksia: mining-maksu ja 546 sats, joka lähetetään vastaanottajan ilmoitusosoitteeseen yhteyden merkiksi. Kun yhteys on muodostettu, BIP47:n kautta voidaan suorittaa lähes rajattomasti maksuja.



Pähkinänkuoressa:




- follow": ilmainen, luo salattua viestintää Sorobanin kautta, hyödyllinen Ashigarun yhteistyövälineille;
- `Connect`: maksullinen, suorittaa BIP47-ilmoitustapahtuman maksajan ja vastaanottajan välisen kanavan aktivoimiseksi.



Jos haluat olla vuorovaikutuksessa PayNymin kanssa, sinun on ensin *seurattava* sitä. Tämä on ensimmäinen vaihe ennen BIP47-yhteyden muodostamista. Oletetaan, että haluat lähettää toistuvia maksuja PayNymille `+instinctiveoffer10`.



Mene PayNym-sivullesi Ashigarussa ja napsauta sitten käyttöliittymän oikeassa alareunassa olevaa `+`-painiketta.



![Image](assets/fr/07.webp)



Voit sitten joko liittää vastaanottajan koko maksukoodin tai skannata hänen QR-koodinsa.



![Image](assets/fr/08.webp)



Jos sinulla on vain hänen PayNym-tunnuksensa, mene osoitteeseen [Paynym.rs](https://paynym.rs/) ja etsi hänen maksukoodiinsa liittyvä QR-koodi.



![Image](assets/fr/09.webp)



Kun olet skannannut QR-koodin, napsauta SEURAA-painiketta seurataksesi PayNymiä.



![Image](assets/fr/10.webp)



SEURAAVA-toiminto riittää yhteistoiminnallisiin tapahtumiin (*cahoots*). BIP47-maksujen lähettämistä varten sinun on kuitenkin luotava yhteys: napsauta `CONNECT` (Yhteys) ilmoitustapahtuman suorittamiseksi.



![Image](assets/fr/11.webp)



Ilmoitustapahtuma lähetetään sitten verkossa. Odota, että se on saanut vähintään yhden vahvistuksen, ennen kuin teet ensimmäisen maksun.



![Image](assets/fr/12.webp)



## Tee BIP47-maksu



Olet nyt yhteydessä vastaanottajaan ja voit lähettää maksun yksilölliseen osoitteeseen, joka on luotu automaattisesti BIP47-protokollan avulla, ilman, että vastaanottajan kanssa tarvitsee vaihtaa tietoja etukäteen.



Klikkaa PayNymin pääsivulta sitä yhteyshenkilöä, jolle haluat lähettää maksun.



![Image](assets/fr/13.webp)



Napsauta käyttöliittymän oikeassa yläkulmassa olevaa nuolikuvaketta.



![Image](assets/fr/14.webp)



Kirjoita lähetettävä summa. Vastaanottajan osoitetta ei tarvitse syöttää: se saadaan automaattisesti BIP47-protokollan avulla.



![Image](assets/fr/15.webp)



Tarkista huolellisesti tapahtuman tiedot, mukaan lukien maksut, ja allekirjoita ja lähetä tapahtuma vetämällä näytön alareunassa olevaa vihreää nuolta.



![Image](assets/fr/16.webp)



Tapahtuma on lähetetty.



![Image](assets/fr/17.webp)



Tässä esimerkissä maksu suoritettiin toiselle PayNym-lompakolleni. Näin ollen näen, että se on saapunut toiseen Ashigaru wallet:een ilman, että mitään osoitetta olisi vaihdettu manuaalisesti: käytettiin vain PayNym-tunnusta.



![Image](assets/fr/18.webp)



Osaat nyt käyttää BIP47-maksukoodeja Ashigaru-sovelluksen PayNym-toteutuksen ansiosta. Voit nyt jakaa tämän maksukoodin kenelle tahansa, joka haluaa lähettää sinulle maksuja (erityisesti toistuvia maksuja). Voit myös julkaista PayNym-tunnuksesi verkkosivustollasi tai sosiaalisissa verkostoissa saadaksesi lahjoituksia.



Jos haluat syventää tietämystäsi tästä protokollasta, ymmärtää yksityiskohtaisesti, miten se toimii, ja ymmärtää sen vaikutukset luottamuksellisuuteen, suosittelen lämpimästi, että osallistut BTC 204 -kurssilleni:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c