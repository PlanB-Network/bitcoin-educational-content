---
name: Jade - Electrum
description: Jaden tai Jade Plus -laitteen käyttäminen Electrum:n kanssa (työpöytä)
---

![cover](assets/cover.webp)



_Tämä opas on otettu [Bitcoin-työpajojen oppitunnilta](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Ohje on tehty Jade Classic -ohjelmalla, mutta toiminnot pätevät myös niille, joilla on Jade Plus.



Kun olet alustanut Jaden, voit aloittaa sen käytön ja valita wallet-näytön.



Jade on laite, jota voidaan käyttää useiden wallet:n tai liitännäissovellusten kanssa, kuten Blockstream ilmoittaa sivustollaan.



Tässä oppaassa näet vaiheet Electrum Wallet:n käyttämiseksi USB-kaapeliyhteyden kautta.



## Julkisen avaimen siirto



Ota ja käynnistä alustettu Jade. Heti kun kytket sen päälle, se näyttää tältä:




![img](assets/en/32.webp)



Jos valitset _Unlock Jade_, saat näkyviin valikon, jossa sinun on valittava, miten yhdistät laitteesi kumppanuussovellukseen.



Electrum:n kanssa voit liittää Jaden vain USB:n kautta, joten valitse tämä menetelmä.



Käynnistä Electrum, joka avaa ehdotuksen oletusarvoisesti viimeksi käytetyn wallet:n avaamiseksi.



Jos tämä on ensimmäinen kerta, kun yhdistät Jaden Electrum:een, valitse _Luo uusi lompakko_ ja sitten _Valmis_.



![img](assets/en/34.webp)



Nimi wallet.



![img](assets/en/35.webp)



Valitse Standard Wallet.



![img](assets/en/36.webp)



Avainsäilöä valittaessa on tärkeää valita _Käytä laitteistolaitetta_.



![img](assets/en/37.webp)



Electrum aloittaa laitteiston etsimisen.



![img](assets/en/38.webp)



Kun liität USB:n tietokoneeseen (USB C on jo kytketty Jadeen), wallet-laitteisto näkyy lukitustilassa. Jade avaa lukituksen syöttämällä asennuksen aikana asetetun kuusinumeroisen PIN-koodin.




![img](assets/en/39.webp)



Lukitsematon laitteisto, Electrum havaitsee Jaden. Jatka klikkaamalla _Next_.



![img](assets/en/40.webp)



Tässä vaiheessa Electrum pyytää sinua asettamaan käytäntöskriptin: valitse _Native Segwit_.



![img](assets/en/41.webp)



Julkisen avaimen siirtovaihe wallet:sta Jadesta Electrum:n näyttöön alkaa.



Kun julkisen avaimen vienti on valmis, prosessi on päättynyt.



Watch-only on valmis, ja Electrum ilmoittaa valmistumisesta seuraavassa näytössä.



![img](assets/en/42.webp)



wallet on todella luotu, ja voit alkaa tutkia sitä: näet _osoitteet_, _wallet-tiedot_ ja - mikä tärkeintä - näet oikeassa alakulmassa merkinnän siitä, että kyseessä on Blockstreamin laite. Blockstreamin logon vieressä oleva vihreä piste osoittaa, että laite on kytketty päälle ja että se on liitetty kunnolla lähiverkkoon.



![img](assets/en/43.webp)



## Tapahtumien vastaanottaminen ja kuluttaminen



Electrum:n _Receive_-valikosta generate "scriptPubKey" (osoite) varojen vastaanottamista varten. Aloita aina pienellä summalla ja tee vastaanotto- ja kulutustesti.



![img](assets/en/44.webp)



Kun olet saanut satssin, voit tarkistaa sen saapumisen _Historia_-valikosta.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Kun maksutapahtuma on vahvistettu, voit käyttää tämän UTXO:n ja suorittaa testin loppuun.



Kustannuksiin liittyy Jaden käyttäminen allekirjoittamiseen.



Mene Electrum:n _Send_-valikkoon, liitä scriptPubKey ja tarkista se hyvin.



![img](assets/en/47.webp)



Kun olet valmis, paina _Maksa_.



Tapahtumaikkuna avautuu, jossa on tärkeää asettaa oikeat tapahtumamaksut. Kun olet saanut kaikki asetukset valmiiksi, napsauta oikeassa alakulmassa olevaa _Preview_ (esikatselu) -painiketta.



![img](assets/en/48.webp)



Tapahtumaikkunassa näkyy joitakin tärkeitä tietoja, ennen kaikkea tila: `Unsigned`.



Tässä vaiheessa näet myös komennon _Sign_, jota napsauttamalla voit kiinnittää allekirjoituksen Jaden kanssa.



![img](assets/en/49.webp)



Nyt alkaa wallet-näytön ja laitteiston välinen viestintävaihe, jossa Electrum ilmoittaa, että sinun on noudatettava laitteiston ohjeita, joka on kytketty päälle ja valmis allekirjoittamaan.



![img](assets/en/50.webp)



**Ensin sinun on kuitenkin parasta tarkistaa, mitä olet allekirjoittamassa: kaikki juuri määrittämäsi tapahtuman parametrit näkyvät myös Jade**:ssä, ja voit tarkistaa ne kaikki.



![img](assets/en/51.webp)



Jatkaaksesi varmista, että asetat kursorin aina seuraaviin vaiheisiin vievään nuoleen "→", etkä koskaan "X"-nuolelle, ellet halua lopettaa toimintoa suorittamatta sitä loppuun.



Tarkastusosa päättyy maksun näyttöön. Tässä vaiheessa vahvistus vastaa allekirjoituksen antamista.



![img](assets/en/52.webp)



Jade käsittelee toimenpidettä hetken aikaa, ja kun se on valmis, se palaa aloitusvalikkoon.



![img](assets/en/53.webp)



Kun olet Electrum:ssä, näet tapahtuman tilan, joka on muuttunut "allekirjoittamattomasta" "allekirjoitetuksi", ja nyt on mahdollista levittää sitä klikkaamalla _Broadcast_.



![img](assets/en/54.webp)



Näin testattua wallet:aa voidaan käyttää turvalliseen varastointiin tarkoitetun UTXO:n vastaanottamiseen.



![img](assets/en/55.webp)



Tämä opas on esimerkki siitä, miten USB-liitännän kautta kytkettyä Jadea käytetään wallet-kelloon. Electrum on klassinen esimerkki, mutta saatat haluta muita wallet-ohjelmistoja. Jade vie julkisen avaimen moniin muihin lompakoihin: löydä samankaltaisia toimintoja, joista luet tässä oppaassa, opastaa sinua ja löytää, miten työllistää se suosikki companio-sovelluksesi.