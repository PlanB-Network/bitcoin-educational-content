---
term: STONEWALL X2

---
Erityinen Bitcoin-tapahtuman muoto, jonka tarkoituksena on lisätä käyttäjän yksityisyyttä kulutuksen aikana tekemällä yhteistyötä kolmannen osapuolen kanssa, joka ei ole osallisena kulutuksessa. Tämä menetelmä simuloi kahden osallistujan välistä minicoin-liittymää, kun maksu suoritetaan kolmannelle osapuolelle. Stonewall x2 -tapahtumat ovat käytettävissä sekä Samourai Wallet -sovelluksessa että Sparrow Wallet -ohjelmistossa (molemmat ovat yhteentoimivia).

Sen toiminta on suhteellisen yksinkertaista: se käyttää maksun suorittamiseen hallussamme olevaa UTXO:ta ja pyytää apua kolmannelta osapuolelta, joka myös osallistuu maksuun omistamallaan UTXO:lla. Tapahtuma päättyy neljään lähtöön: kaksi niistä on yhtä suuria, joista toinen on tarkoitettu maksun vastaanottajan osoitteeseen ja toinen yhteistyökumppanin osoitteeseen. Kolmas UTXO lähetetään takaisin toiseen yhteistyökumppanin osoitteeseen, jolloin tämä voi saada takaisin alkuperäisen summan (neutraali toimenpide hänelle, miinus louhintamaksut), ja viimeinen UTXO palautuu omistamaamme osoitteeseen, joka muodostaa maksun muutoksen. Stonewall x2 -tapahtumissa määritellään siis kolme eri roolia:


- Lähettäjä, joka suorittaa maksun;
- Yhteistyökumppani, joka tarjoaa bitcoineja parantaakseen transaktion yleistä anonymiteettiä ja saadakseen samalla kaikki varansa takaisin lopussa;
- Vastaanottaja, joka ei välttämättä tiedä tapahtuman erityisluonnetta ja odottaa vain maksua lähettäjältä.

![](../../dictionnaire/assets/3.webp)

Stonewall x2 -rakenne lisää paljon entropiaa kauppaan ja sekoittaa ketjuanalyysin jäljet. Ulkopuolelta katsottuna tällainen transaktio voidaan tulkita pieneksi kolikkoyhteydeksi kahden henkilön välillä. Todellisuudessa kyseessä on kuitenkin maksu. Tämä menetelmä tuottaa siis epävarmuutta ketjuanalyysiin tai johtaa jopa vääriin jälkiin. Vaikka ulkopuolinen tarkkailija onnistuisi tunnistamaan Stonewall x2 -tapahtuman mallin, hänellä ei ole kaikkea tietoa. Hän ei pysty päättelemään, kumpi kahdesta samansuuruisesta UTXO:sta vastaa maksua. Hän ei myöskään voi tietää, kuka maksun suoritti. Lopuksi he eivät voi selvittää, ovatko kaksi UTXO-tuloa peräisin kahdelta eri henkilöltä vai kuuluvatko ne yhdelle henkilölle, joka on yhdistänyt ne. Tämä viimeinen seikka johtuu siitä, että klassiset Stonewall-tapahtumat noudattavat täsmälleen samaa kaavaa kuin Stonewall x2 -tapahtumat. Ulkopuolelta käsin ja ilman lisätietoja asiayhteydestä on mahdotonta erottaa Stonewall-tapahtumaa Stonewall x2 -tapahtumasta. Ensin mainitut eivät kuitenkaan ole yhteistyöhön perustuvia liiketoimia, kun taas jälkimmäiset ovat. Tämä lisää entisestään epäilyksiä menojen suhteen.