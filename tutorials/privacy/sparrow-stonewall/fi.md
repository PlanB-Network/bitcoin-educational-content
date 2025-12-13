---
name: Sparrow Wallet - Stonewall
description: Stonewall-tapahtumien ymmärtäminen ja käyttö Sparrow:ssa
---

![cover](assets/cover.webp)




> *Riko lohkoketjuanalyysin oletukset matemaattisesti todistettavilla epäilyksillä transaktioiden lähettäjän ja vastaanottajan välillä.*

## Mikä on Stonewall-tapahtuma?



Stonewall on erityinen Bitcoin-transaktiomuoto, joka on suunniteltu lisäämään käyttäjien luottamuksellisuutta rahankäytön yhteydessä jäljittelemällä kahden ihmisen välistä kolikkoyhteyttä ilman, että ne todellisuudessa ovat yksi. Itse asiassa tämä transaktio ei ole yhteistoiminnallinen. Käyttäjä voi rakentaa sen yksin käyttäen syötteenä vain hänelle kuuluvia UTXO:ita. Voit siis luoda Stonewall-tapahtuman mihin tahansa tilaisuuteen ilman, että sinun tarvitsee synkronoitua toisen käyttäjän kanssa.



Stonewall-tapahtuma toimii seuraavasti: liikkeeseenlaskija käyttää tapahtuman syötteenä kahta sille kuuluvaa UTXO:ää. Lähtöpuolella transaktio tuottaa 4 lähtöä, joista 2 on täsmälleen samanarvoisia. Muut 2 ovat valuuttaa. Kahdesta samansuuruisesta tuotoksesta vain toinen menee maksunsaajalle.



Stonewall-tapahtumassa on siis vain kaksi roolia:




- Liikkeeseenlaskija, joka suorittaa varsinaisen maksun ;
- Vastaanottaja, joka ei välttämättä tiedä tapahtuman erityisluonnetta ja odottaa yksinkertaisesti maksua lähettäjältä.



Otetaan esimerkki tämän tapahtumarakenteen ymmärtämiseksi. Alice on leipomossa ostamassa patonkia, joka maksaa 4 000 sats.". Hän haluaa maksaa bitcoineilla säilyttäen kuitenkin jonkinlaisen luottamuksellisuuden maksunsa suhteen. Niinpä hän päättää rakentaa maksua varten Stonewall-tapahtuman.



![image](assets/fr/01.webp)



Analysoimalla tätä liiketapahtumaa voidaan todeta, että leipuri on todellakin saanut 4 000 sats patongista. Alice käytti syötteenä kahta UTXO:ta: toinen oli 10 000 sats ja toinen 15 000 sats. Tuotoksena se on saanut 3 UTXO:a: yksi 4 000 sats, yksi 6 000 sats ja yksi 11 000 sats. Alice:n nettosaldo tästä liiketoimesta on siis - 4 000 sats`, mikä vastaa hyvin patongin hintaa.



Tässä esimerkissä olen tarkoituksella jättänyt mining-maksut huomiotta, jotta se olisi helpommin ymmärrettävissä. Todellisuudessa transaktiokulut jäävät kokonaan liikkeeseenlaskijan maksettaviksi.



## Mitä eroa on Stonewallilla ja Stonewall x2:lla?



Stonewall-transaktio toimii samalla tavalla kuin StonewallX2-transaktio, paitsi että jälkimmäinen vaatii yhteistyötä, toisin kuin klassinen Stonewall-transaktio, mistä nimi "x2" johtuu. Tämä johtuu siitä, että Stonewall-transaktio suoritetaan ilman ulkopuolista yhteistyötä: lähettäjä voi suorittaa sen ilman toisen henkilön apua. Sen sijaan Stonewall x2 -tapahtumassa prosessiin liittyy ylimääräinen osallistuja, jota kutsutaan "yhteistyökumppaniksi". Hän osallistuu transaktioon omilla bitcoineillaan lähettäjän bitcoinien ohella ja saa lopussa koko summan (miinus mining-kustannukset).



Palataanpa esimerkkiin Alice:sta leipomossa. Jos hän olisi halunnut tehdä Stonewall x2 -tapahtuman, Alice:n olisi pitänyt tehdä yhteistyötä Bob:n (kolmannen osapuolen) kanssa, kun hän perusti tapahtuman. Molemmat olisivat tuoneet UTXO:n. Bob olisi sitten saanut koko panoksensa poistumisen yhteydessä. Leipuri olisi saanut maksun patongistaan samalla tavalla kuin Stonewall-kaupassa, kun taas Alice olisi saanut takaisin alkuperäisen saldonsa, josta olisi vähennetty patongin hinta.



![image](assets/fr/02.webp)



Ulkopuolisen näkökulmasta liiketoimi olisi pysynyt täsmälleen samana.



![image](assets/fr/03.webp)



Yhteenvetona voidaan todeta, että Stonewallin ja Stonewall x2:n liiketoimet ovat rakenteeltaan samanlaisia. Näiden kahden liiketoimen erona on niiden yhteistoiminnallinen tai ei-yhteistoiminnallinen luonne. Stonewall-tapahtuma kehitetään yksilöllisesti, eikä siihen tarvita yhteistyötä. Stonewall x2 -tapahtuma sen sijaan perustuu kahden henkilön väliseen yhteistyöhön.



[**-> Lisätietoja Stonewall-tapahtumista x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Mitä hyötyä Stonewall-kaupasta on?



Stonewall-rakenne lisää liiketoimiin valtavasti entropiaa, mikä hämärtää ketjuanalyysin rajoja. Ulkopuolelta katsottuna tällainen transaktio voidaan tulkita pieneksi kolikkoyhteydeksi kahden ihmisen välillä. Todellisuudessa se on kuitenkin Stonewall x2 -tapahtuman tavoin maksu. Menetelmä aiheuttaa siis epävarmuutta ketjuanalyysissä tai johtaa jopa vääriin johtolankoihin.



Otetaan esimerkiksi Alice leipomossa. Lohkoketjussa tapahtuma näyttäisi seuraavalta:



![image](assets/fr/04.webp)



Ulkopuolinen tarkkailija, joka luottaa tavalliseen ketjuanalyysin heuristiikkaan, saattaa virheellisesti päätellä, että "*kaksi ihmistä on tehnyt pienen coinjoinin, jossa kummallakin on yksi UTXO syötteenä ja kaksi UTXO:ta tuotoksena*".



![image](assets/fr/05.webp)



Tämä tulkinta on epätarkka, koska kuten tiedätte, yksi UTXO lähetettiin leipurille, kaksi saapuvaa UTXO:ta tuli Alicelta, ja hän sai takaisin kolme vaihtotulosta.



![image](assets/fr/01.webp)



Vaikka ulkopuolinen tarkkailija onnistuisikin tunnistamaan Stonewall-tapahtuman isän, hänellä ei ole kaikkea tietoa. Hän ei pysty päättelemään, kumpi kahdesta samansuuruisesta UTXO:sta vastaa maksua. Hän ei myöskään pysty päättelemään, ovatko kaksi UTXO-merkintää peräisin kahdelta eri henkilöltä vai kuuluvatko ne yhdelle henkilölle, joka on yhdistänyt ne. Tämä viimeinen seikka johtuu siitä, että edellä mainitut Stonewall x2 -tapahtumat noudattavat täsmälleen samaa kaavaa kuin Stonewall-tapahtumat. Ulkopuolelta katsottuna ja ilman lisätietoja asiayhteydestä on mahdotonta erottaa Stonewall-tapahtumaa ja Stonewall x2 -tapahtumaa toisistaan. Ensin mainitut eivät ole yhteistyöhön perustuvia liiketoimia, kun taas jälkimmäiset ovat. Tämä lisää entisestään epäilyksiä kustannusten osalta.



![image](assets/fr/03.webp)



## Miten teen Stonewall-tapahtuman Sparrow:ssä?



Samurai Wallet -tiimin alun perin kehittämät Stonewall-tapahtumat otettiin haltuun Ashigaru-sovelluksella, joka on fork alkuperäisestä salkusta, joka luotiin samurai-kehittäjien pidätyksen jälkeen, ja myös Sparrow Wallet:lla.



Sinun on asennettava Sparrow ja luotava :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Toisin kuin Stowaway- tai Stonewall x2 (*cahoots*) -tapahtumat, Stonewall-tapahtumat eivät edellytä Paynymsin käyttöä. Ne voidaan suorittaa suoraan, ilman erityisiä valmisteluja tai yhteistyötä toisen käyttäjän kanssa.



Stonewall-tapahtuman suorittaminen Sparrow:llä on hyvin yksinkertaista: aloita luomalla tapahtuma tavalliseen tapaan joko `Lähetys`-valikosta tai `UTXOs`-valikosta, jos haluat käyttää *Coin-ohjausta*.



![Image](assets/fr/06.webp)



Syötä sitten tapahtuman tiedot: vastaanottajan osoite, etiketti, lähetettävä summa ja kulujen määrä tai osuus markkinaolosuhteiden mukaan.



![Image](assets/fr/07.webp)



Ennen vahvistamista voit valita Stonewall-rakenteen. Korvaa käyttöliittymän alaosassa `Efficiency` sanalla `Privacy`. Jos tätä vaihtoehtoa ei näy, se tarkoittaa, että salkussasi ei ole riittävästi UTXO:ta tämäntyyppisen transaktion rakentamiseen.



![Image](assets/fr/08.webp)



Kun olet valinnut `Privacy`-vaihtoehdon, huomaat, että transaktion rakenne muuttuu täysin: siitä tulee Stonewall-transaktio, joka kuluttaa useita UTXO:itasi panoksina ja tuottaa kaksi samansuuruista tuotosta, joista toinen vastaa varsinaista maksua `100,000 sats` vaihtotulosten lisäksi.



![Image](assets/fr/09.webp)



Jos kaikki on oikein, napsauta `Create Transaction`.



Tämän jälkeen voit tarkistaa tapahtuman tiedot vielä kerran ja napsauttaa "Viimeistele tapahtuma allekirjoitusta varten".



![Image](assets/fr/10.webp)



Allekirjoita transaktio salkullesi ominaista menetelmää käyttäen ja lähetä se Bitcoin-verkkoon vahvistusta odottaen klikkaamalla `Broadcast Transaction`.



![Image](assets/fr/11.webp)



Tiedät nyt, miten Stonewall-tapahtuma toimii Sparrow Wallet:ssä ja miten sellainen luodaan. Syventääksesi näiden työkalujen hallintaa, jotka on suunniteltu vahvistamaan onchain-luottamuksellisuuttasi, kutsun sinut seuraamaan BTC 204 -koulutustani Plan ₿ Academyssa :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c