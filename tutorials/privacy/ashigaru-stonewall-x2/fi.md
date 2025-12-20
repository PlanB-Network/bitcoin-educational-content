---
name: Ashigaru - Stonewall x2
description: Stonewall x2 -tapahtumien ymmärtäminen ja käyttäminen Ashigarussa
---
![cover stonewall x2](assets/cover.webp)



> *Tee jokaisesta rahankäytöstä coinjoin

## Mikä on Stonewall x2 -tapahtuma?



Stonewall x2 on erityinen Bitcoin-tapahtuman muoto, jonka tarkoituksena on lisätä käyttäjän luottamuksellisuutta menojen yhteydessä tekemällä yhteistyötä kolmannen osapuolen kanssa, joka ei ole osallisena menoissa. Tämä menetelmä simuloi kahden osallistujan välistä minikolikkoliitosta, kun maksu suoritetaan kolmannelle osapuolelle. Stonewall x2 -tapahtumat ovat saatavilla Ashigaru-sovelluksessa, joka on Samourai Wallet:n (tämän tapahtumatyypin luomisen takana oleva tiimi) fork.



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Toiminta on suhteellisen yksinkertaista: maksat maksun hallussasi olevalla UTXO:llä ja käytät apuna kolmatta osapuolta, joka myös osallistuu maksuun omalla UTXO:llä. Maksutapahtumasta syntyy neljä tulostetta: kaksi yhtä suurta, joista toinen on tarkoitettu maksun saajan osoitteeseen ja toinen yhteistyökumppanin osoitteeseen. Kolmas UTXO palautetaan toiseen yhteistyökumppanin osoitteeseen, jolloin tämä voi saada takaisin alkuperäisen summan (mikä on hänelle neutraali toimenpide, kun otetaan huomioon mining-kustannukset), ja viimeinen UTXO palautetaan meille kuuluvaan osoitteeseen, mikä muodostaa maksun vaihdon.



Stonewall x2 -tapahtumissa määritellään siis kolme erilaista roolia:




- Liikkeeseenlaskija, joka suorittaa varsinaisen maksun ;
- Yhteistyökumppani, joka asettaa bitcoinit saataville parantaakseen transaktion anonymiteettiä ja saa lopussa takaisin kaikki varansa (neutraali toiminta hänelle, kun otetaan huomioon mining-kustannukset);
- Vastaanottaja, joka ei välttämättä tiedä tapahtuman erityisluonnetta ja odottaa yksinkertaisesti maksua lähettäjältä.



Otetaanpa esimerkki. Alice on leipomossa ostamassa patonkia, joka maksaa 4 000 sats. Hän haluaa maksaa bitcoineilla ja pitää maksunsa luottamuksellisena. Niinpä hän kutsuu ystävänsä Bob:n, joka auttaa häntä tässä.



![image](assets/fr/01.webp)



Analysoimalla tätä liiketapahtumaa voidaan todeta, että leipuri sai patongista maksuna 4 000 sats. Alice käytti 10 000 sats` panoksena ja sai takaisin 6 000 sats` tuotoksena, jolloin nettosaldo oli 4 000 sats`, mikä vastaa patongin hintaa. Bob toimitti 15 000 sats` tuotantopanoksena ja sai kaksi tuotosta: 4 000 sats` ja 11 000 sats`, jolloin saldo oli 0`.



Tässä esimerkissä olen tarkoituksella jättänyt mining-maksut huomiotta, jotta se olisi helpommin ymmärrettävissä. Todellisuudessa maksutapahtumamaksut jaetaan tasan maksun myöntäjän ja yhteistyökumppanin kesken.



## Mitä eroa on Stonewallilla ja Stonewall x2:lla?



StonewallX2-tapahtuma toimii täsmälleen samalla tavalla kuin Stonewall-tapahtuma, paitsi että ensin mainittu on yhteistoiminnallinen ja jälkimmäinen ei. Kuten olemme nähneet, StonewallX2-tapahtumaan osallistuu kolmas osapuoli, joka on maksun ulkopuolinen ja joka antaa bitcoinejaan saataville parantaakseen tapahtuman luottamuksellisuutta. Klassisessa Stonewall-tapahtumassa lähettäjä on yhteistyökumppanin roolissa.



Palataanpa esimerkkiin Alice:sta leipomossa. Jos hän ei olisi löytänyt jotakuta Bob:n kaltaista henkilöä, joka olisi seurannut häntä hänen tuhlauskierroksellaan, hän olisi voinut tehdä Stonewallin yksin. Näin hän olisi saanut kaksi UTXO:ta matkalla sisään ja kolme matkalla ulos.



![image](assets/fr/02.webp)




Ulkopuolisen näkökulmasta liiketoimi olisi pysynyt samana.



![image](assets/fr/05.webp)



Logiikan pitäisi siis olla seuraava, kun haluat käyttää Ashigaru-työkalua:




- Jos kauppias ei tue Payjoin Stowaway -palvelua, voit tehdä maksutapahtuman yhteistyössä toisen henkilön kanssa maksun ulkopuolella Stonewall x2 -palvelun ansiosta;
- Jos et löydä ketään, joka tekisi Stonewall x2 -tapahtuman, voit tehdä pelkän Stonewall-tapahtuman, joka jäljittelee Stonewall x2 -tapahtuman käyttäytymistä.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Mitä hyötyä Stonewall x2 -kaupasta on?



Stonewall x2 -rakenne lisää valtavasti entropiaa transaktioon, mikä sekoittaa ketjuanalyysin. Ulkopuolelta katsottuna tällainen transaktio voitaisiin tulkita pieneksi Coinjoiniksi kahden henkilön välillä. Todellisuudessa kyseessä on kuitenkin maksu. Tämä menetelmä aiheuttaa siis epävarmuutta ketjuanalyysiin tai johtaa jopa vääriin johtolankoihin.



Otetaan esimerkiksi Alice, Bob ja Boulanger. Lohkoketjussa tapahtuma näyttäisi seuraavalta:



![image](assets/fr/03.webp)



Ulkopuolinen tarkkailija, joka luottaa tavalliseen ketjuanalyysin heuristiikkaan, saattaa virheellisesti päätellä, että "*Alice ja Bob ovat tehneet pienen coinjoinin, jossa kumpikin on saanut yhden UTXO:n sisään ja kumpikin kaksi UTXO:ta ulos*".



![image](assets/fr/04.webp)



Tämä tulkinta on virheellinen, koska kuten tiedätte, UTXO lähetettiin Boulangeriin, Alice:ssa on vain yksi vaihtolähtö ja Bob:ssa kaksi.



![image](assets/fr/01.webp)



Vaikka ulkopuolinen tarkkailija onnistuisikin tunnistamaan Stonewall x2 -tapahtuman isän, hänellä ei ole kaikkea tietoa. Hän ei pysty päättelemään, kumpi kahdesta samansuuruisesta UTXO:sta vastaa maksua. Hän ei myöskään pysty päättelemään, onko maksun suorittanut Alice vai Bob. Hän ei myöskään pysty päättelemään, ovatko kaksi kirjattua UTXO:ta peräisin kahdelta eri henkilöltä vai kuuluvatko ne yhdelle henkilölle, joka on yhdistänyt ne. Tämä viimeinen seikka johtuu siitä, että edellä käsitellyt klassiset Stonewall-tapahtumat noudattavat täsmälleen samaa paternea kuin Stonewall x2 -tapahtumat. Ulkopuolelta katsottuna ja ilman kontekstiin liittyvää lisätietoa on mahdotonta erottaa Stonewall-tapahtumaa Stonewall x2 -tapahtumasta. Ensin mainitut eivät ole yhteistyöhön perustuvia liiketoimia, kun taas jälkimmäiset ovat. Tämä lisää entisestään epäilyksiä kustannusten osalta.



![image](assets/fr/05.webp)




## Miten voin luoda yhteyden Paynymien välille?



Kuten muissakin Ashigarun (*Cahoots*) yhteistoiminnallisissa transaktioissa, Stonewall x2:ssa vaihdetaan osittain allekirjoitettuja transaktioita lähettäjän ja yhteistyökumppanin välillä. Tämä vaihto voidaan suorittaa manuaalisesti, jos olet fyysisesti läsnä yhteistyökumppanisi kanssa, tai automaattisesti Soroban-viestintäprotokollan avulla.



Jos valitset toisen vaihtoehdon, sinun on luotava yhteys Paynymien välille ennen kuin voit suorittaa Stonewall x2:n. Tätä varten sinun Paynymisi on "*seurattava*" yhteistyökumppanisi Paynymiä ja päinvastoin. Jos haluat tietää, miten tämä tehdään, voit seurata tämän toisen ohjeen alkua:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Miten teen Stonewall x2 -tapahtuman Ashigarussa?



Voit suorittaa Stonewall x2 -tapahtuman napsauttamalla Paynym-kuvasi kuvaa näytön vasemmassa yläkulmassa ja avaamalla sitten "Yhteistyö"-valikon. Tapahtumaan kanssasi osallistuvan henkilön on tehtävä samoin, ellette vaihda QR-koodeja henkilökohtaisesti.



![Image](assets/fr/06.webp)



Sinulla on kaksi vaihtoehtoa: valitse "Aloita", jos olet maksun lähettäjä, tai "Osallistu", jos olet tapahtumaan osallistuva henkilö, mutta et ole maksaja etkä varsinainen vastaanottaja.



![Image](assets/fr/07.webp)



Jos sinulla on yhteistyökumppanin rooli, menettely on hyvin yksinkertainen. Soroban-verkon kautta tapahtuvaa etäyhteistyötä varten klikkaa `Osallistu`, valitse tili, jota haluat käyttää, ja paina sitten `LISTEN FOR CAHOOTS REQUESTS` odottaaksesi maksajan lähettämää pyyntöä.



![Image](assets/fr/08.webp)



Jos taas haluat tehdä henkilökohtaista yhteistyötä QR-koodin skannauksen avulla, siirry wallet:n etusivulle, paina näytön yläreunassa olevaa QR-koodi-kuvaketta ja skannaa sitten maksutapahtuman aloittavan maksajan antama QR-koodi.



![Image](assets/fr/09.webp)



Jos olet maksajan roolissa, eli olet se, joka aloittaa tapahtuman, siirry "Yhteistyö"-valikkoon ja valitse sitten "Aloita".



![Image](assets/fr/10.webp)



Koska haluamme suorittaa Stonewall x2:n, valitse tämä vaihtoehto tapahtumatyypiksi.



![Image](assets/fr/11.webp)



Tämän jälkeen voit valita joko online-yhteistyön (*Cahoots* *Sorobanin* kautta) tai kasvokkain tapahtuvan yhteistyön QR-koodien vaihdon avulla.



![Image](assets/fr/12.webp)



### Cahoots verkossa



Jos olet valinnut vaihtoehdon "Online", valitse yhteistyökumppanisi seuraamistasi Paynyms-ohjelmista.



![Image](assets/fr/13.webp)



Napsauta `Set up transaction` ja valitse sitten tili, jolta haluat tehdä menon.



![Image](assets/fr/14.webp)



Kirjoita seuraavalla sivulla tapahtuman tiedot: maksun todellisen vastaanottajan osoite, lähetettävä summa ja veloitusmaksu. Napsauta sitten `Katsele maksutapahtuman asetuksia`.



![Image](assets/fr/15.webp)



Tarkista tiedot huolellisesti, varmista, että yhteistyökumppanisi kuuntelee *Cahoots*-pyyntöjä, ja napsauta sitten vihreää `BEGIN TRANSACTION` -painiketta aloittaaksesi PSBT:iden vaihdon Sorobanin kautta.



![Image](assets/fr/16.webp)



Odota, kunnes molemmat osallistujat ovat allekirjoittaneet tapahtuman, ja lähetä se sitten Bitcoin-verkkoon.



![Image](assets/fr/17.webp)



### Henkilökohtaiset keskustelut



Jos haluat suorittaa vaihdon henkilökohtaisesti, valitse tapahtumatyyppi "STONEWALL X2" ja valitse sitten vaihtoehto "Henkilökohtaisesti / manuaalisesti".



![Image](assets/fr/18.webp)



Napsauta `Set up transaction` ja valitse sitten tili, jolta haluat tehdä menon.



![Image](assets/fr/19.webp)



Kirjoita seuraavalla sivulla tapahtuman tiedot: maksun todellisen vastaanottajan osoite, lähetettävä summa ja veloitusmaksu. Napsauta sitten `Katsele maksutapahtuman asetuksia`.



![Image](assets/fr/20.webp)



Tarkista tiedot ja paina sitten vihreää `BEGIN TRANSACTION` -painiketta aloittaaksesi PSBT:iden vaihtamisen QR-koodin skannauksen avulla.



![Image](assets/fr/21.webp)



Vaihto tapahtuu skannaamalla vuorotellen yhteistyökumppanin kanssa: napsauta `NÄYTÄ QR-KOODI` näyttääksesi QR-koodisi yhteistyökumppanillesi, joka skannaa sen. Tämän jälkeen hän napsauttaa `NÄYTÄ QR-KOODI` näyttääksesi omansa, ja sinä skannaat sen `LAUNCH QR Scanner` -ohjelmalla. Toista tätä prosessia, kunnes kaikki viisi vaihtovaihetta on suoritettu.



![Image](assets/fr/22.webp)



Kun kaikki vaihdot on suoritettu, tarkista tapahtuman tiedot ja vapauta se vetämällä näytön alareunassa olevaa vihreää nuolta.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Sen rakenne on seuraava:



![Image](assets/fr/24.webp)



*Luotto: [mempool.space](https://mempool.space/)*



Voimme havaita kaksi panosta omasta salkustani, "91,869 sats" ja "64,823 sats", kun taas kaksi muuta panosta tulevat yhteistyökumppanini wallet:stä. Tuotospuolella yksi UTXO, 100 000 sats, lähetetään varsinaiselle maksunsaajalle, ja kaksi UTXO:ta, 100 000 sats ja 159 578 sats, palautetaan yhteistyökumppanini salkkuun. Hänelle operaatio on neutraali, koska hän saa takaisin kaikki panokseen sijoittamansa varat (lukuun ottamatta mining-kustannuksia, joihin hän osallistui). Lopuksi saan vaihdossa UTXO 56 270 sats`, joka vastaa kokonaispanokseni ja vastaanottajalle lähetetyn 100 000 sats`:n maksun välistä erotusta.



Voin luonnollisesti kuvata tämän rakenteen, koska olen rakentanut tapahtuman itse. Ulkopuolisen tarkkailijan on kuitenkin yleensä mahdotonta määrittää, mitkä UTXO:t kuuluvat millekin osallistujalle joko tuloissa tai lähdöissä.



Jos haluat syventää tietämystäsi onchain-yksityisyyden hallinnasta Bitcoin:ssa, suosittelen, että osallistut BTC 204 -koulutukseeni Plan ₿ Academyssa:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c