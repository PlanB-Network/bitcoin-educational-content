---
name: Ashigaru - Stonewall
description: Stonewall-tapahtumien ymmärtäminen ja käyttäminen Ashigarussa
---
![cover stonewall](assets/cover.webp)



> *Riko lohkoketjuanalyysin oletukset matemaattisesti todistettavilla epäilyksillä transaktioiden lähettäjän ja vastaanottajan välillä.*

## Mikä on Stonewall-tapahtuma?



Stonewall on erityinen Bitcoin-transaktiomuoto, joka on suunniteltu lisäämään käyttäjien luottamuksellisuutta rahankäytön yhteydessä jäljittelemällä kahden ihmisen välistä kolikkoyhteyttä ilman, että ne todellisuudessa ovat yksi. Itse asiassa tämä transaktio ei ole yhteistoiminnallinen. Käyttäjä voi rakentaa sen yksin käyttäen panoksena vain omistamiaan UTXO:ita. Voit siis luoda Stonewall-tapahtuman mihin tahansa tilaisuuteen ilman, että sinun tarvitsee synkronoitua toisen käyttäjän kanssa.



Stonewall-tapahtuma toimii seuraavasti: liikkeeseenlaskija käyttää tapahtuman syötteenä kahta UTXO:tä, jotka kuuluvat sille. Lähtöpuolella transaktio tuottaa 4 lähtöä, joista 2 on täsmälleen saman suuruisia. Loput 2 ovat valuuttaa. Kahdesta samansuuruisesta tuotoksesta vain toinen menee maksunsaajalle.



Stonewall-tapahtumassa on siis vain kaksi roolia:




- Liikkeeseenlaskija, joka suorittaa varsinaisen maksun ;
- Vastaanottaja, joka ei välttämättä tiedä tapahtuman erityisluonnetta ja odottaa yksinkertaisesti maksua lähettäjältä.



Otetaan esimerkki tämän tapahtumarakenteen ymmärtämiseksi. Alice on leipomossa ostamassa patonkia, joka maksaa 4 000 sats. Hän haluaa maksaa bitcoineilla säilyttäen samalla jonkinlaisen luottamuksellisuuden maksustaan. Niinpä hän päättää rakentaa maksua varten Stonewall-tapahtuman.



![image](assets/fr/01.webp)



Analysoimalla tätä liiketapahtumaa voidaan todeta, että leipuri on todellakin saanut 4 000 sats patongista. Alice käytti panoksina kahta UTXO:tä: toinen oli 10 000 sats ja toinen 15 000 sats. Tuotantopuolella se on saanut takaisin 3 UTXO:tä: yhden 4 000 sats:n, yhden 6 000 sats:n ja yhden 11 000 sats:n arvosta. Alice:n nettosaldo tästä liiketoimesta on siis - 4 000 sats`, mikä vastaa hyvin patongin hintaa.



Tässä esimerkissä olen tarkoituksella jättänyt mining-maksut huomiotta, jotta se olisi helpommin ymmärrettävissä. Todellisuudessa transaktiokulut jäävät kokonaan liikkeeseenlaskijan maksettaviksi.



## Mitä eroa on Stonewallilla ja Stonewall x2:lla?



Stonewall-tapahtuma toimii samalla tavalla kuin StonewallX2-tapahtuma, paitsi että jälkimmäinen edellyttää yhteistyötä, toisin kuin klassinen Stonewall-tapahtuma, mistä nimi "x2" johtuu. Tämä johtuu siitä, että Stonewall-transaktio suoritetaan ilman ulkopuolista yhteistyötä: lähettäjä voi suorittaa sen ilman toisen henkilön apua. Sen sijaan Stonewall x2 -tapahtumassa prosessiin liittyy ylimääräinen osallistuja, jota kutsutaan "yhteistyökumppaniksi". Hän osallistuu transaktioon omilla bitcoineillaan lähettäjän bitcoinien ohella ja ottaa lopussa haltuunsa koko summan (mining-kustannusten moduuli).



Palataanpa esimerkkiin Alice:n kanssa leipomossa. Jos hän olisi halunnut tehdä Stonewall x2 -tapahtuman, Alice:n olisi pitänyt tehdä yhteistyötä Bob:n (kolmannen osapuolen) kanssa, kun hän perusti tapahtuman. Kumpikin olisi tuonut UTXO:n. Bob olisi sitten saanut koko panoksensa takaisin. Leipuri olisi saanut maksun patongistaan samalla tavalla kuin Stonewall-kaupassa, kun taas Alice olisi saanut takaisin alkuperäisen saldonsa, josta olisi vähennetty patongin hinta.



![image](assets/fr/02.webp)



Ulkopuolisen näkökulmasta liiketoimi olisi pysynyt täsmälleen samana.



![image](assets/fr/03.webp)



Yhteenvetona voidaan todeta, että Stonewallin ja Stonewall x2:n liiketoimet ovat rakenteeltaan samanlaisia. Näiden kahden liiketoimen erona on niiden yhteistoiminnallinen tai ei-yhteistoiminnallinen luonne. Stonewall-tapahtuma kehitetään yksilöllisesti, eikä siihen tarvita yhteistyötä. Stonewall x2 -tapahtuma sen sijaan perustuu kahden henkilön väliseen yhteistyöhön.



[**-> Lisätietoja Stonewall-tapahtumista x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Mitä hyötyä Stonewall-kaupasta on?



Stonewall-rakenne lisää liiketoimiin valtavasti entropiaa, mikä hämärtää ketjuanalyysin rajoja. Ulkopuolelta katsottuna tällainen transaktio voidaan tulkita pieneksi kolikkoyhteydeksi kahden ihmisen välillä. Todellisuudessa se on kuitenkin Stonewall x2 -tapahtuman tavoin maksu. Tämä menetelmä aiheuttaa siis epävarmuutta ketjuanalyysissä tai johtaa jopa vääriin johtolankoihin.



Otetaan esimerkiksi Alice leipomossa. Lohkoketjussa tapahtuma näyttäisi seuraavalta:



![image](assets/fr/04.webp)



Ulkopuolinen tarkkailija, joka luottaa tavalliseen ketjuanalyysin heuristiikkaan, saattaa virheellisesti päätellä, että "**kaksi ihmistä on tehnyt pienen coinjoinin, jossa kummallakin on syötteenä yksi UTXO ja tuloksena kaksi UTXO:ta**".



![image](assets/fr/05.webp)



Tämä tulkinta on epätarkka, sillä kuten tiedätte, yksi UTXO lähetettiin leipurille, kaksi saapuvaa UTXO:ta tuli Alicelta, ja hän sai takaisin kolme vaihtokurssitulosta.



![image](assets/fr/01.webp)



Vaikka ulkopuolinen tarkkailija onnistuisikin tunnistamaan Stonewall-tapahtuman isän, hänellä ei ole kaikkea tietoa. Hän ei pysty päättelemään, kumpi kahdesta samansuuruisesta UTXO:sta vastaa maksua. Hän ei myöskään pysty päättelemään, ovatko kaksi kirjattua UTXO:ta peräisin kahdelta eri henkilöltä vai kuuluvatko ne yhdelle henkilölle, joka on yhdistänyt ne. Tämä viimeinen seikka johtuu siitä, että edellä mainitut Stonewall x2 -tapahtumat noudattavat täsmälleen samaa kaavaa kuin Stonewall-tapahtumat. Ulkopuolelta katsottuna ja ilman lisätietoja asiayhteydestä on mahdotonta erottaa Stonewall-tapahtumaa ja Stonewall x2 -tapahtumaa toisistaan. Ensin mainitut eivät ole yhteistyöhön perustuvia liiketoimia, kun taas jälkimmäiset ovat. Tämä lisää entisestään epäilyksiä kustannusten osalta.



![image](assets/fr/03.webp)



## Miten teen Stonewall-tapahtuman Ashigarussa?



Alun perin Samourain Wallet-tiimin kehittämä Stonewall-tapahtumat on otettu haltuun Ashigaru-sovelluksella, joka on alkuperäisen wallet:n fork, joka luotiin Samourain kehittäjien pidätyksen jälkeen. Sinun on asennettava Ashigaru ja luotava wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Toisin kuin Stowaway- tai Stonewall x2 (*cahoots*) -tapahtumat, Stonewall-tapahtumat eivät edellytä Paynymsin käyttöä. Ne voidaan suorittaa suoraan ilman edeltävää valmistelua tai yhteistyötä toisen käyttäjän kanssa.



Itse asiassa et oikeastaan tarvitse opetusta Stonewall-tapahtumien tekemiseen, sillä Ashigaru luo ne automaattisesti aina kun kulutat rahaa, kun wallet:ssäsi on tarpeeksi UTXO:ta.



Napsauta näytön oikeassa alareunassa olevaa "+"-painiketta ja valitse sitten "Lähetä".



![Image](assets/fr/06.webp)



Valitse tili, jolta haluat tehdä menon.



![Image](assets/fr/07.webp)



Syötä sitten tapahtuman tiedot: vastaanottajan osoite ja lähetettävä summa ja vahvista painamalla nuolinäppäintä.



![Image](assets/fr/08.webp)



Tässä voit tietysti mukauttaa oletusarvoista transaktiomaksua markkinaolosuhteiden mukaan. Tämän sivun mielenkiintoisin elementti on kuitenkin tapahtumatyyppi. Huomaat, että Ashigaru on automaattisesti valinnut `STONEWALL`. Klikkaa `PREVIEW`-painiketta saadaksesi lisätietoja.



![Image](assets/fr/09.webp)



Näette, että transaktio on todellakin Stonewall-tyyppinen: se koostuu kahdesta samansuuruisesta panoksesta, kahdesta samansuuruisesta tuotoksesta sekä vaihtotuloksista ja minun tapauksessani ylimääräisestä panoksesta maksusumman täyttämiseksi.



![Image](assets/fr/10.webp)



Jos et halua tehdä Stonewall-tapahtumaa, vaan haluat mieluummin tavanomaisen maksun, napsauta näytön oikeassa yläkulmassa olevaa kynäkuvaketta ja valitse sitten `Simple` eikä `STONEWALL`.



![Image](assets/fr/11.webp)



Kun olet tarkistanut kaikki tiedot, vedä näytön alareunassa olevaa vihreää nuolta allekirjoittaaksesi ja vapauttaaksesi tapahtuman.



![Image](assets/fr/12.webp)



Tiedät nyt, miten Stonewall-tapahtuma toteutetaan, ja mikä tärkeintä, miten se toimii. Jos haluat lisätietoja, katso Ashigaru Terminal -oppaastani, jossa selitetään, miten kolikkoyhteyksiä tehdään Whirlpool:n kautta.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add