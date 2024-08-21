---
termi: STONEWALL
---

Erityinen Bitcoin-siirtotapa, jonka tavoitteena on lisätä käyttäjän yksityisyyttä maksun yhteydessä jäljittelemällä kahden henkilön välillä tapahtuvaa coinjoinia, olematta kuitenkaan sellainen. Todellisuudessa tämä siirto ei ole yhteistyöllinen. Käyttäjä voi rakentaa sen yksin, käyttäen vain omia UTXO:itaan syötteinä. Siksi voit luoda Stonewall-siirron mihin tahansa tilanteeseen, ilman tarvetta synkronoida toisen käyttäjän kanssa.

Stonewall-siirron toiminta on seuraava: siirron syötteenä lähettäjä käyttää 2 UTXO:ta, jotka kuuluvat hänelle. Siirto tuottaa sitten 4 tulostetta, joista 2 on täsmälleen samaa määrää. Kaksi muuta muodostavat vaihtorahan. Näistä kahdesta saman määrän tulosteesta vain toinen todellisuudessa menee maksun saajalle.

Näin ollen Stonewall-siirrossa on vain 2 roolia:
* Lähettäjä, joka suorittaa varsinaisen maksun;
* Saaja, joka saattaa olla tietämätön siirron erityisluonteesta ja yksinkertaisesti odottaa maksua lähettäjältä.

![](../../dictionnaire/assets/33.png)
Stonewall-siirtoja on saatavilla sekä Samourai Wallet -sovelluksessa että Sparrow Wallet -ohjelmistossa.

Stonewall-rakenne lisää paljon entropiaa siirtoon ja hämärtää ketjuanalyysin jälkiä. Ulkopuolelta tällainen siirto voidaan tulkita pienenä coinjoinina kahden henkilön välillä. Mutta todellisuudessa, aivan kuten Stonewall x2 -siirto, se on maksu. Tämä menetelmä siis luo epävarmuuksia ketjuanalyysiin tai jopa johtaa vääriin jälkiin. Vaikka ulkopuolinen tarkkailija onnistuisikin tunnistamaan Stonewall-siirron kaavan, hänellä ei ole kaikkea tietoa. Hän ei pysty määrittämään, kumpi kahdesta saman määrän UTXO:sta vastaa maksua. Lisäksi hän ei pysty määrittämään, tulevatko kaksi syötteen UTXO:ta kahdelta eri henkilöltä vai kuuluvatko ne yhdelle henkilölle, joka on yhdistänyt ne. Tämä viimeinen kohta johtuu siitä, että Stonewall x2 -siirrot noudattavat täsmälleen samaa kaavaa kuin Stonewall-siirrot. Ulkopuolelta ja ilman lisäkontekstitietoja on mahdotonta erottaa Stonewall-siirtoa Stonewall x2 -siirrosta. Kuitenkaan edelliset eivät ole yhteistyöllisiä siirtoja, kun taas jälkimmäiset ovat. Tämä lisää entisestään epäilyksiä tästä menosta.