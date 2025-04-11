---
term: STONEWALL

---
Erityinen Bitcoin-tapahtuman muoto, jonka tarkoituksena on lisätä käyttäjän yksityisyyttä rahankäytön aikana jäljittelemällä kahden ihmisen välistä kolikkoliitosta, mutta joka ei itse asiassa ole sellainen. Tämä transaktio ei todellakaan ole yhteistoiminnallinen. Käyttäjä voi rakentaa sen yksin, jolloin vain hänen omat UTXO:nsa ovat syötteinä. Voit siis luoda Stonewall-tapahtuman mihin tahansa tilaisuuteen ilman, että sinun tarvitsee synkronoitua toisen käyttäjän kanssa.

Stonewall-transaktio toimii seuraavasti: transaktion syötössä lähettäjä käyttää kahta itselleen kuuluvaa UTXO:ta. Tämän jälkeen transaktio tuottaa 4 ulostuloa, joista 2 on täsmälleen sama määrä. Loput 2 muodostavat muutoksen. Näistä kahdesta samansuuruisesta tuotoksesta vain toinen menee maksun vastaanottajalle.

Stonewall-tapahtumassa on siis vain kaksi roolia:


- Lähettäjä, joka suorittaa varsinaisen maksun;
- Vastaanottaja, joka ei välttämättä tiedä tapahtuman erityisluonnetta ja odottaa vain maksua lähettäjältä.

![](../../dictionnaire/assets/33.webp)

Stonewall-tapahtumat ovat käytettävissä sekä Samourai Wallet -sovelluksessa että Sparrow Wallet -ohjelmistossa.

Stonewall-rakenne lisää paljon entropiaa transaktioon ja peittää ketjuanalyysin jäljet. Ulkopuolelta katsottuna tällainen transaktio voidaan tulkita pieneksi kolikkoyhteydeksi kahden henkilön välillä. Todellisuudessa se on kuitenkin Stonewall x2 -tapahtuman tavoin maksu. Tämä menetelmä aiheuttaa siis epävarmuutta ketjuanalyysissä tai johtaa jopa vääriin jälkiin. Vaikka ulkopuolinen tarkkailija onnistuisikin tunnistamaan Stonewall-tapahtuman mallin, hänellä ei ole kaikkea tietoa. Hän ei pysty päättelemään, kumpi kahdesta samansuuruisesta UTXO:sta vastaa maksua. Hän ei myöskään pysty päättelemään, ovatko nämä kaksi UTXO:ta peräisin kahdelta eri henkilöltä vai kuuluvatko ne yhdelle henkilölle, joka on yhdistänyt ne. Viimeinen seikka johtuu siitä, että Stonewall x2 -tapahtumat noudattavat täsmälleen samaa kaavaa kuin Stonewall-tapahtumat. Ulkopuolelta käsin ja ilman lisätietoja asiayhteydestä on mahdotonta erottaa Stonewall-tapahtumaa Stonewall x2 -tapahtumasta. Ensin mainitut eivät kuitenkaan ole yhteistoiminnallisia liiketoimia, kun taas jälkimmäiset ovat. Tämä lisää entisestään epäilyksiä näiden menojen suhteen.