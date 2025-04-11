---
term: HILJAISET MAKSUT

---
Menetelmä staattisten Bitcoin-osoitteiden käyttämiseksi maksujen vastaanottamiseen ilman osoitteen uudelleenkäyttöä, ilman vuorovaikutusta ja ilman näkyvää ketjussa olevaa yhteyttä eri maksujen ja staattisen osoitteen välillä. Tämä tekniikka poistaa tarpeen luoda uusia, käyttämättömiä vastaanottoosoitteita jokaista maksutapahtumaa varten, jolloin vältetään Bitcoinissa tavanomaiset vuorovaikutustilanteet, joissa vastaanottajan on annettava maksajalle uusi osoite.

Hiljaisissa maksuissa maksaja käyttää vastaanottajan julkisia avaimia (julkinen avain ja julkinen skannausavain) ja omien yksityisten avaintensa summaa syöttötietoina luodakseen uuden osoitteen jokaista maksua varten. Ainoastaan vastaanottaja voi laskea tätä maksuosoitetta vastaavan yksityisen avaimen omien yksityisten avaintensa avulla. ECDH (*Elliptic-Curve Diffie-Hellman*) on salausalgoritmi, jota käytetään jaetun salaisuuden luomiseen, jonka perusteella saadaan vastaanottava osoite ja yksityinen avain (vain vastaanottajan puolella). Tunnistaakseen heille tarkoitetut Silent Payments -maksut vastaanottajien on skannattava lohkoketju ja tutkittava jokainen protokollan kriteerit täyttävä transaktio. Toisin kuin BIP47, joka käyttää ilmoitustapahtumaa maksukanavan luomiseen, Silent Payments poistaa tämän vaiheen ja säästää tapahtuman. Kompromissina on kuitenkin se, että vastaanottajan on skannattava kaikki mahdolliset transaktiot määrittääkseen ECDH:ta soveltamalla, onko ne osoitettu hänelle.

Esimerkiksi Bobin staattinen osoite $B$ edustaa hänen julkisen scan-avaimensa ja julkisen spend-avaimensa yhdistelmää:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Nämä avaimet johdetaan yksinkertaisesti seuraavasta polusta:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Tämän staattisen osoitteen on julkaissut Bob. Alice hakee sen tehdäkseen hiljaisen maksun Bobille. Hän laskee Bobin maksuosoitteen $P_0$ näin:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Missä:

$$ \text{inputHash} = \text{hash}(\text{outpoint}_ L \text{ ‖ } A) $$ $$

Kanssa:


- $B_{\text{scan}}$: Bobin julkinen skannausavain (staattinen osoite);
- $B_{\text{spend}}$: Bobin julkinen avain (staattinen osoite);
- $A$: Julkisten avainten summa syötteessä (tweak);
- $a$: Kaikkien avainparien summa, joita on käytetty `scriptPubKey`:ssä UTXO:ssa, joka on käytetty syötteenä Alicen transaktiossa;
- $\text{outpoint}_L$: Pienin UTXO (leksikografisesti), jota käytetään sisääntulona Alicen tapahtumassa;
- $\text{ ‖ }$: Konkatenaatio (operandien yhdistäminen peräkkäin);
- $G$: Elliptisen käyrän `secp256k1` generaattoripiste;
- $\text{hash}$: SHA256-hajausfunktio, joka on merkitty tunnisteella `BIP0352/SharedSecret`;
- $P_0$: Ensimmäinen julkinen avain / yksilöllinen osoite, josta maksetaan Bobille;
- $0$: Kokonaisluku, jota käytetään useiden yksilöllisten maksuosoitteiden luomiseen.

Bob skannaa lohkoketjua löytääkseen hiljaisen maksunsa tällä tavoin:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Kanssa:


- $b_{\text{scan}}$: Bobin yksityinen skannausavain.

Jos hän löytää $P_0$-osoitteen, joka sisältää hänelle osoitetun Hiljaisen maksun, hän laskee $p_0$:n, joka on yksityinen avain, jonka avulla hän voi käyttää Alicen $P_0$-osoitteeseen lähettämät varat:

$$ p_0 = (b_{\text{spend}}) + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Kanssa:


- $b_{\text{spend}}}$: Bobin yksityinen rahankäyttöavain;
- $n$: elliptisen käyrän `secp256k1` järjestys.

Tämän perusversion lisäksi tarroja voidaan käyttää myös luomaan samasta staattisesta perusosoitteesta useita erilaisia staattisia osoitteita, jolloin useat käyttötarkoitukset voidaan erottaa toisistaan ilman, että skannauksen vaatima työmäärä lisääntyy kohtuuttomasti.