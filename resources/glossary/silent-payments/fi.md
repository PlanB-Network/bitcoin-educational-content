---
termi: HILJAISEN MAKSUN
---

Menetelmä staattisten Bitcoin-osoitteiden käyttämiseen maksujen vastaanottamiseksi ilman osoitteen uudelleenkäyttöä, ilman vuorovaikutusta ja ilman näkyvää on-chain-linkkiä eri maksujen ja staattisen osoitteen välillä. Tämä tekniikka eliminoi tarpeen luoda uusia, käyttämättömiä vastaanotto-osoitteita jokaiselle transaktiolle, välttäen siten tavalliset vuorovaikutukset Bitcoinissa, joissa vastaanottajan on tarjottava uusi osoite maksajalle.

Hiljaisen maksun avulla maksaja käyttää vastaanottajan julkisia avaimia (kulutusjulkinen avain ja skannausjulkinen avain) ja oman yksityisen avaimensa summaa syötteenä luodakseen tuoreen osoitteen jokaiselle maksulle. Vain vastaanottaja, omilla yksityisillä avaimillaan, voi laskea yksityisen avaimen, joka vastaa tätä maksuosoitetta. ECDH (*Elliptic-Curve Diffie-Hellman*), kryptografinen avaintenvaihtoalgoritmi, käytetään yhteisen salaisuuden luomiseen, jota sitten käytetään vastaanotto-osoitteen ja yksityisen avaimen (vain vastaanottajan puolella) johdattamiseen. Jotta vastaanottajat voivat tunnistaa heille tarkoitetut Hiljaiset Maksut, heidän on skannattava lohkoketju ja tutkittava jokaista transaktiota, joka vastaa protokollan kriteerejä. Toisin kuin BIP47, joka käyttää ilmoitustransaktiota maksukanavan perustamiseen, Hiljainen Maksu poistaa tämän vaiheen, säästäen transaktion. Kompromissina on kuitenkin, että vastaanottajan on skannattava kaikki mahdolliset transaktiot määrittääkseen ECDH:n soveltamisen avulla, onko ne osoitettu heille.

Esimerkiksi Bobin staattinen osoite $B$ edustaa hänen skannausjulkisen avaimensa ja kulutusjulkisen avaimensa yhdistämistä:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Nämä avaimet johdetaan yksinkertaisesti seuraavasta polusta:

```text
skannaus : m / 352' / 0' / 0' / 1' / 0
kulutus : m / 352' / 0' / 0' / 0' / 0
```

Bob julkaisee tämän staattisen osoitteen. Alice hakee sen tehdäkseen Hiljaisen Maksun Bobille. Hän laskee Bobin maksuosoitteen $P_0$ tällä tavalla:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Missä:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

Jossa:
* $B_{\text{scan}}$: Bobin skannausjulkinen avain (staattinen osoite);
* $B_{\text{spend}}$: Bobin kulutusjulkinen avain (staattinen osoite);
* $A$: Syötteenä olevien julkisten avainten summa (tweak);
* $a$: Tweakin yksityinen avain, eli kaikkien `scriptPubKey`-käytössä olevien UTXOjen syötteinä käytettyjen avainparien summa;
* $\text{outpoint}_L$: Pienin leksikografisesti käytetty UTXO Alice'n transaktion syötteenä;
* $\text{ ‖ }$: Yhdistäminen (operandien yhdistäminen peräkkäin);
* $G$: Elliptisen käyrän `secp256k1` generaattoripiste;
* $\text{hash}$: SHA256-hajautusfunktio, joka on merkitty `BIP0352/SharedSecret`;
* $P_0$: Ensimmäinen julkinen avain / ainutlaatuinen osoite maksulle Bobille;
* $0$: Kokonaisluku, jota käytetään useiden ainutlaatuisten maksuosoitteiden luomiseen.

Bob skannaa lohkoketjun löytääkseen Hiljaisen Maksunsa tällä tavalla:
$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Jossa:
* $b_{\text{scan}}$: Bobin yksityinen skannausavain.

Jos hän löytää $P_0$:n osoitteena, joka sisältää hänelle osoitetun Hiljaisen Maksun, hän laskee $p_0$:n, yksityisen avaimen, joka mahdollistaa hänelle lähetettyjen varojen käyttämisen $P_0$:ssa:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Jossa:
* $b_{\text{spend}}$: Bobin yksityinen kulutusavain;
* $n$: elliptisen käyrän `secp256k1` järjestys.

Tämän perusversion lisäksi, etikettejä voidaan myös käyttää tuottamaan useita erilaisia staattisia osoitteita samasta perusstaattisesta osoitteesta, tavoitteena erottaa useita käyttötarkoituksia ilman, että skannauksen aikana vaadittava työmäärä kasvaa kohtuuttomasti.