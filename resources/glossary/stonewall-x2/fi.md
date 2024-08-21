---
termi: STONEWALL X2
---

Erityinen Bitcoin-siirtotapa, jonka tavoitteena on lisätä käyttäjän yksityisyyttä maksun yhteydessä yhteistyössä kolmannen osapuolen kanssa, joka ei ole mukana menossa. Tämä menetelmä simuloii mini-coinjoinia kahden osallistujan välillä samalla, kun tehdään maksu kolmannelle osapuolelle. Stonewall x2 -siirrot ovat saatavilla sekä Samourai Wallet -sovelluksessa että Sparrow Wallet -ohjelmistossa (molemmat ovat yhteensopivia).

Sen toiminta on suhteellisen yksinkertaista: se käyttää meidän hallussamme olevaa UTXO:a maksun tekemiseen ja pyytää apua kolmannelta osapuolelta, joka myös osallistuu omalla UTXO:llaan. Siirto päättyy neljään lähtöön: kaksi niistä ovat samansuuruisia, toinen on tarkoitettu maksunsaajan osoitteeseen, toinen yhteistyökumppanin osoitteeseen. Kolmas UTXO lähetetään takaisin toiseen yhteistyökumppanin osoitteeseen, jolloin he voivat palauttaa alkuperäisen summan (neutraali toimenpide heille, miinus louhintamaksut), ja viimeinen UTXO palautuu osoitteeseemme, joka muodostaa maksun vaihtorahan. Näin määritellään kolme eri roolia Stonewall x2 -siirroissa:
* Lähettäjä, joka suorittaa varsinaisen maksun;
* Yhteistyökumppani, joka tarjoaa bitcoineja parantaakseen siirron kokonaisanonyymiyttä, samalla täysin palauttaen varansa lopussa;
* Vastaanottaja, joka voi olla tietämätön siirron erityisluonteesta ja yksinkertaisesti odottaa maksua lähettäjältä.

![](../../dictionnaire/assets/3.png)

Stonewall x2 -rakenne lisää paljon entropiaa siirtoon ja sekoittaa ketjuanalyysin jälkiä. Ulkopuolelta tällainen siirto voidaan tulkita pienenä coinjoinina kahden ihmisen välillä. Mutta todellisuudessa se on maksu. Tämä menetelmä siis luo epävarmuuksia ketjuanalyysiin tai jopa johtaa vääriin jälkiin. Vaikka ulkopuolinen tarkkailija onnistuisikin tunnistamaan Stonewall x2 -siirron kaavan, heillä ei ole kaikkea tietoa. He eivät pysty määrittämään, kumpi kahdesta samansuuruisesta UTXO:sta vastaa maksua. Lisäksi he eivät voi tietää, kuka suoritti maksun. Lopuksi he eivät voi määrittää, tulevatko kaksi syöttö-UTXO:a kahdelta eri ihmiseltä vai kuuluvatko ne yhdelle henkilölle, joka yhdisti ne. Tämä viimeinen kohta johtuu siitä, että klassiset Stonewall-siirrot noudattavat täsmälleen samaa kaavaa kuin Stonewall x2 -siirrot. Ulkopuolelta ja ilman lisätietoja kontekstista on mahdotonta erottaa Stonewall-siirtoa Stonewall x2 -siirrosta. Kuitenkin edelliset eivät ole yhteistyösiirtoja, kun taas jälkimmäiset ovat. Tämä lisää vielä enemmän epävarmuutta menosta.