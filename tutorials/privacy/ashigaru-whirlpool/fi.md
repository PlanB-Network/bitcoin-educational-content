---
name: Ashigaru - Whirlpool Coinjoin
description: Miten teen kolikkoliitoksia Ashigaru-sovelluksessa?
---

![cover](assets/cover.webp)



"*Bitcoin wallet kaduille*"



Tässä opetusohjelmassa opit, mitä coinjoin on ja miten se tehdään Ashigaru Terminal -sovelluksella ja Whirlpool-toteutuksella, joka on Samourai Wallet:sta peritty coinjoin-protokolla.



## Miten Whirlpool:n koliittimet toimivat



Tässä opetusohjelmassa en palaa coinjoinin käsitteeseen, sen hyödyllisyyteen tai Whirlpool:n teoreettiseen toimintaan, sillä nämä aiheet on jo selitetty yksityiskohtaisesti Plan ₿ Academyn BTC 204 -koulutuskurssin osassa 5. Jos et vielä hallitse Whirlpool:n toimintaa tai coinjoinin periaatetta, suosittelen, että tutustut tähän osaan 5 ennen kuin jatkat :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Seuraavassa on kuitenkin muutama nopea tieto ja luku, jotka voivat olla hyödyllisiä.



Whirlpool-yhteensopivissa salkuissa käytetään 4 erillistä tiliä coinjoin-prosessin tarpeiden täyttämiseksi:




- **Talletustili**, joka on tunnistettu indeksillä `0'` ;
- **Pahan pankin** (tai *toksisen valuutan*) tili, joka on merkitty indeksillä `2,147,483,644'` ;
- Tilin **Premix**, jonka tunnus on "2 147 483 645" ;
- **Postmix**-tili, jonka tunnus on "2 147 483 646".



Ashigarussa on marraskuussa 2025 saatavilla kaksi allasnimikettä (tämä luettelo todennäköisesti muuttuu tulevina kuukausina: muista siis tarkistaa arvot lukiessasi):




- 0.25 BTC`, ja osallistumismaksu on `0.0125 BTC`;
- 0.025 BTC, ja osallistumismaksu on 0,00125 BTC.



Jokaisessa sekoitussyklissä voi olla 5-10 UTXO:ta tulossa ja lähdössä.



![Image](assets/fr/01.webp)



## Ohjelmistovaatimukset



Whirlpool:llä tehtäviin rinnakkaisliitoksiin tarvitaan kolme erillistä ohjelmaa:





- Ashigaru Terminal**, jonka avulla voit hallita kolikkoliitoksiasi suoraan tietokoneeltasi;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, älypuhelimesi sovellus, jolla voit käyttää bitcoineja *postmixissä* mistä tahansa;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, Bitcoin-solmutoteutus, joka takaa sinulle suvereenin yhteyden verkkoon ilman riippuvuutta kolmannen osapuolen palvelimesta.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Asenna kukin näistä työkaluista seuraamalla niiden opetusohjelmia, minkä jälkeen voit aloittaa ensimmäisten coinjoinejen tekemisen.



## Vastaanottaa bitcoineja



Kun olet luonut salkkusi, aloitat yhdellä tilillä, joka on merkitty indeksillä "0". Tämä on `Talletustili`. Lähetät tälle tilille coinjoineihin tarkoitettuja bitcoineja. Voit vastaanottaa niitä joko Ashigaru-sovelluksen kautta (ks. osa 5 erityisestä opetusohjelmasta) tai Ashigaru-päätteellä (josta kerrotaan tarkemmin myös erillisen opetusohjelman osassa 5).



Kun talletustililläsi on vähintään pienimpään pooliin osallistumiseen tarvittava summa (lisättynä palvelumaksuilla ja mining-kustannusten kattamiseen vaadittavalla vähimmäismäärällä), olet valmis aloittamaan ensimmäiset kolikkoyhteytesi.



![Image](assets/fr/02.webp)



## Tee Tx0



Kun varat ovat saapuneet talletustilillesi ja transaktio on vahvistettu, voit aloittaa kolikkojäsenyysprosessin. Avaa tätä varten Ashigaru-päätteellä "Lompakot"-valikko ja valitse sitten wallet. Jos wallet:si on lukittu, ohjelma pyytää sinua antamaan salasanasi ja passphrase:n.



![Image](assets/fr/03.webp)



Valitse sitten "Talletus"-tili.



![Image](assets/fr/04.webp)



Siirry `UTXOs`-valikkoon.



![Image](assets/fr/05.webp)



Täällä näet luettelon kaikista UTXO:ista talletustililläsi. Valitse ne, jotka haluat lähettää coinjoin-sykleissä.



Luottamuksellisuuden lisäämiseksi ja *Common Input Ownership Heuristic (CIOH)*:n välttämiseksi suositellaan, että Whirlpool:ssä käytetään vain yhtä UTXO:tä kutakin tuloa kohti (yksityiskohtainen selitys tästä periaatteesta on BTC 204:ssä).



Paina näppäimistön `ENTER`-näppäintä valitaksesi UTXO:n. Tähti `(*)` ilmestyy sen viereen merkiksi, että se on valittu.



![Image](assets/fr/06.webp)



Napsauta sitten `Mix Selected`-painiketta.



![Image](assets/fr/07.webp)



Jos UTXO on riittävän suuri osallistuakseen jompaankumpaan käytettävissä olevaan pooliin, voit valita kohdepoolin nuolinäppäimillä. Tällä sivulla näet Tx0:n tiedot:




- pooliin tulevien UTXO:iden määrä;
- eri maksut (palvelumaksut ja mining-maksut) ;
- *toksisen muutoksen* määrä.



Tarkista tiedot huolellisesti ja klikkaa sitten `Broadcast` lähettääksesi Tx0:n.



![Image](assets/fr/08.webp)



Tämän jälkeen Ashigaru näyttää Tx0:n TXID:n ja vahvistaa, että transaktio on lähetetty verkkoon.



![Image](assets/fr/09.webp)



## Yhteenliittämisen tekeminen



Kun Tx0 on lähetetty, palaa talletustilisi etusivulle, valitse "Tilit" ja valitse "Premix"-tili.



![Image](assets/fr/10.webp)



Valikossa `UTXOs` näet eri tasoitetut osat, jotka ovat valmiina coinjoin-sykleihin. Heti kun Tx0 on vahvistettu, Ashigaru Terminal aloittaa automaattisesti ensimmäisen sekoitussyklinsä.



![Image](assets/fr/11.webp)



Kun Tx0 on vahvistettu, Ashigaru Terminal luo ja lähettää ensimmäisen coinjoin-transaktion automaattisesti. Siirtymällä osoitteeseen `Tilit > Postmix > UTXOs` voit tarkastella tasoitettuja UTXOsi, jotka odottavat ensimmäisen syklin vahvistusta.



![Image](assets/fr/12.webp)



Voit nyt jättää Ashigaru Terminalin toimimaan taustalla: se jatkaa automaattisesti kappaleidesi miksaamista ja remixaamista.



## Yhteenliitosten viimeistely



Nyt voit antaa kolikoidesi remixata itsensä automaattisesti. Whirlpool-malli tarkoittaa, että remixauksesta ei peritä lisämaksuja: ei palvelumaksuja, ei mining-maksuja. Joten kolikoidesi antaminen osallistua useampiin sekoitussykleihin voi vain hyödyttää luottamuksellisuuttasi.



Jos haluat ymmärtää paremmin tätä mekanismia ja sitä, kuinka monta sykliä kannattaa odottaa, suosittelen lukemaan tämän artikkelin:



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Jos haluat nähdä, kuinka monta remixiä kukin kappaleesi on tehnyt, avaa Postmix-tilin `UTXOs`-valikko.



![Image](assets/fr/13.webp)



Voit käyttää sekakolikkosi Ashigaru-sovelluksessa, joka käyttää samaa wallet:ta kuin Ashigaru Terminal -ohjelmisto. Avautumisen yhteydessä näkyvä wallet vastaa "Talletus"-tiliäsi. Pääset "Postmix"-tilille, joka sisältää sekoitetut UTXO:t, napsauttamalla oikeassa yläkulmassa olevaa Whirlpool-symbolia.



![Image](assets/fr/14.webp)



Tällä tilillä näet kaikki kolikkosi tällä hetkellä sekoitettuna. Jos haluat käyttää ne, paina näytön oikeassa alareunassa olevaa "+"-symbolia ja valitse sitten "Lähetä".



![Image](assets/fr/15.webp)



Täytä maksutapahtuman tiedot: vastaanottajan osoite, lähetettävä summa ja halutessasi voit valita erityisen maksutapahtumarakenteen luottamuksellisuuden lisäämiseksi (katso vastaavat opetusohjelmat).



![Image](assets/fr/16.webp)



Tarkista tapahtuman tiedot huolellisesti ja vahvista lähetys vetämällä näytön alareunassa olevaa nuolta.



![Image](assets/fr/17.webp)



Tapahtumasi on allekirjoitettu ja lähetetty Bitcoin-verkkoon.



![Image](assets/fr/18.webp)



## Kuluta Doxxic Change



Muista: Whirlpool:n malli perustuu nappuloiden tasaamiseen Tx0:ssa, ennen kuin ne tulevat altaisiin. Juuri tämä mekanismi rikkoo UTXO:n seurannan. Mielestäni tämä on tehokkain coinjoin-malli, mutta siinä on yksi haittapuoli: se tuottaa *vaihtoa*, joka ei mene coinjoin-prosessin läpi.



Tämä muutos vastaa kullekin Tx0:lle luotua UTXO:tä. Se on eristetty erityiselle tilille, jonka nimi on ohjelmasta riippuen `Doxxic Change` tai `Bad Bank`, jotta sitä ei käytettäisi muiden UTXO:iden kanssa. Tämä on erittäin tärkeää, koska näitä UTXO:ita ei ole sekoitettu: niiden jäljitettävyyslinkit säilyvät koskemattomina, ja ne voivat vaarantaa luottamuksellisuutesi luomalla yhteyden sinun ja kolikkoyhdistämistoimintasi välille. Käsittele niitä siis varovasti, äläkä koskaan käytä niitä muiden UTXO:iden** kanssa, olipa niitä sitten sekoitettu tai ei. Jos yhdistät myrkyllisen UTXO:n ja UTXO:n sekoitetun UTXO:n, kaikki coinjoiningista saamasi yksityisyydensuojan edut menevät hukkaan.



Tällä hetkellä Ashigaru ei tarjoa suoraa pääsyä tälle `Doxxic Change`-tilille (ainakaan minä en ole löytänyt sitä). Tämä ominaisuus lisätään todennäköisesti tulevassa päivityksessä. Sillä välin ainoa tapa saada nämä varat takaisin on tuoda seed Sparrow Wallet:een. Jälkimmäinen tunnistaa yleensä automaattisesti, että kyseessä on wallet, jota käytetään Whirlpool:n kanssa, ja antaa sinulle pääsyn kaikkiin neljään tiliin, myös `Doxxic Change` -tiliin. Voit sitten käyttää nämä UTXO:t kuten tavalliset bitcoinit Sparrow:stä.



Seuraavassa on useita mahdollisia strategioita, joilla voit hallita valuuttasi UTXO:ta coinjoinsista vaarantamatta yksityisyyttäsi:





- Sekoittaminen pienempiin altaisiin:** Jos myrkyllinen UTXO on tarpeeksi suuri liittyäkseen pienempään altaaseen, tämä on yleensä paras vaihtoehto. Ole kuitenkin varovainen, ettet koskaan yhdistä useita myrkyllisiä UTXO:ita tämän saavuttamiseksi, sillä tämä luo yhteyden eri merkintöjen välille Whirlpool:ssä.





- Merkitse ne käyttökelvottomiksi:** Toinen varovainen tapa on yksinkertaisesti pitää ne sellaisenaan erillisellä tilillään ja jättää ne koskematta. Näin estät sinua käyttämästä niitä vahingossa. Jos bitcoinien arvo nousee, uusia, niiden kokoon sopivia pooleja voidaan avata.





- Tee lahjoituksia:** Voit halutessasi muuttaa nämä myrkylliset UTXO:t lahjoituksiksi Bitcoin-kehittäjille, avoimen lähdekoodin projekteille tai yhdistyksille, jotka hyväksyvät BTC:tä. Näin voit hävittää ne hyödyllisesti ja tukea samalla ekosysteemiä.





- Osta prepaid-lahjakortteja tai Visa-kortteja:** Alustojen, kuten [Bitrefill](https://www.bitrefill.com/), avulla voit vaihtaa bitcoinisi lahjakortteihin tai uudelleenladattaviin Visa-kortteihin, joita voit käyttää kaupoissa. Tämä voi olla yksinkertainen ja huomaamaton tapa käyttää myrkyllisiä UTXO-rahojasi.





- Vaihda ne Moneroon:** Samourai Wallet tarjosi aiemmin BTC/XMR-atomivaihtopalvelua, joka on nyt lakkautettu. Jos samanlainen palvelu on olemassa (itse en tiedä sellaisesta), se on erinomainen ratkaisu näiden UTXO:iden eristämiseen, niiden muuntamiseen Moneroksi ja sitten lopulta niiden lähettämiseen takaisin Bitcoin:lle. Tämä menetelmä oli kuitenkin kallis ja riippuvainen käytettävissä olevasta likviditeetistä.





- Siirrä ne Lightning Network:een:** Näiden UTXO:iden siirtäminen Lightning Network:een alennettujen transaktiomaksujen saamiseksi on mahdollisesti mielenkiintoinen vaihtoehto. Tämä menetelmä voi kuitenkin paljastaa tiettyjä tietoja Lightningin käytöstä riippuen, joten sitä on käytettävä varoen.



## Miten voin saada tietoa coinjoin-syklien laadusta?



Jotta rinnakkaisliitos olisi todella tehokas, sen on oltava hyvin yhdenmukainen tulo- ja lähtömäärien välillä. Tämä yhdenmukaisuus lisää ulkopuolisen tarkkailijan tulkintamahdollisuuksien määrää, mikä puolestaan lisää epävarmuutta liiketoimesta. Epävarmuuden mittaamiseen käytetään tapahtumaan sovellettua entropian käsitettä. Whirlpool-malli on tunnustettu yhdeksi tehokkaimmista tässä suhteessa, koska se takaa erinomaisen homogeenisuuden osallistujien välillä. Jos haluat tutustua syvällisemmin tähän periaatteeseen, suosittelen tutustumaan BTC 204 -koulutuskurssin osan 5 viimeiseen lukuun.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Useiden kolikon yhdistämissyklien suorituskykyä mitataan niiden joukkojen koon perusteella, joihin kolikko on piilotettu. Nämä joukot määrittelevät niin sanotut *anonsets*. Niitä on kahta tyyppiä: ensimmäinen mittaa luottamuksellisuutta retrospektiivisen analyysin edessä (nykyhetkestä menneisyyteen), ja toinen mittaa prospektiivisen analyysin kestävyyttä (menneisyydestä nykyhetkeen). Näiden kahden indikaattorin täydellisen selityksen saat seuraavasta opetusohjelmasta (tai jälleen kerran BTC 204 -koulutuskurssista):



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Miten hallita postmixiä?



Kun olet suorittanut useita coinjoin-syklejä, paras strategia on pitää UTXO:t "Postmix"-tilillä ja antaa niiden sekoittua loputtomiin, kunnes ne todella tarvitsee käyttää.



Jotkut käyttäjät haluavat siirtää sekoitetut bitcoinit wallet-laitteistolla suojattuun wallet-laitteistoon. Tämä vaihtoehto on mahdollinen, mutta vaatii tiettyä tarkkuutta, jotta coinjoinsilla hankittu luottamuksellisuus ei vaarannu.



UTXO:iden yhdistäminen on yleisin virhe. On tärkeää, ettei sekoitettuja UTXO:ita koskaan yhdistetä sekoittamattomiin UTXO:ita samassa tapahtumassa, sillä muuten on vaarana, että *Common Input Ownership Heuristic (CIOH)* käynnistyy. Tämä edellyttää UTXO:iden tiukkaa hallintaa, erityisesti selkeää ja tarkkaa merkintää. Yleisesti ottaen UTXO:iden yhdistäminen on huono käytäntö, joka johtaa usein luottamuksellisuuden menettämiseen, jos se on huonosti hoidettu.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Sinun tulisi myös olla varovainen UTXO-sekoitusten yhdistämisessä. Rajoitettuja konsolidointeja voidaan harkita, jos UTXO:iden anonesiot ovat merkittäviä, mutta ne vähentävät väistämättä luottamuksellisuuden tasoa. Vältä massiivisia tai hätäisiä konsolidointeja, jotka tehdään ennen riittävän montaa uudelleensekoitusta, sillä ne voivat luoda päätelmäyhteyksiä sekoitusta edeltävien ja sen jälkeisten kappaleiden välille. Epäselvissä tapauksissa on parasta olla konsolidoimatta postmix UTXO:ita ja siirtää ne yksi kerrallaan wallet-laitteistoon ja luoda joka kerta uusi tyhjä vastaanotto-osoite. Älä unohda merkitä jokaista siirrettyä UTXO:tä.



Emme suosittele siirtämään postmix UTXO:ita salkkuihin vähemmistöskriptien avulla. Jos esimerkiksi osallistuit Whirlpool:een multi-sig:n salkusta `P2WSH:ssa`, vain harvat teistä jakavat tämäntyyppisen skriptin. Lähettämällä postmix UTXO:t tämäntyyppisiin skripteihin vähennät huomattavasti anonymiteettiäsi. Skriptityypin lisäksi muut erityiset wallet-sormenjäljet voivat vaarantaa luottamuksellisuutesi, joten parasta on käyttää ne Ashigaru-sovelluksesta.



Lopuksi, kuten kaikissa Bitcoin-tapahtumissa, älä koskaan käytä vastaanottavaa osoitetta uudelleen. Jokainen maksu on lähetettävä uuteen, ainutlaatuiseen, tyhjään osoitteeseen.



Yksinkertaisin ja turvallisin tapa on antaa sekoitettujen UTXO:iden levätä "Postmix"-tilillään, antaa niiden remixata luonnollisesti ja käyttää niitä vain tarvittaessa Ashigarusta.



Ashigarun ja Sparrow:n lompakoissa on lisäsuojatoimintoja lohkoketjuanalyysiin liittyviä yleisimpiä virheitä vastaan, mikä auttaa sinua säilyttämään transaktioiden luottamuksellisuuden.