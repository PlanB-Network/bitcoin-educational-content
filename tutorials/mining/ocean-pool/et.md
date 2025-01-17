---
name: Ocean Mining
description: Sissejuhatus Ookeani Kaevandamisse
---

![signup](assets/cover.webp)

**Mai 2024**

Ookeani Kaevandamine on üsna ainulaadne kaevandusbassein. Siin ei nõuta kontosid, e-posti aadresse ega paroole. Nagu Bitcoin, on kõik läbipaistev, pseudonüümne ja kaastöötajad saavad valida nelja erineva ploki malli vahel.

### Kompensatsioonisüsteem

Ookeani kompensatsioonisüsteemi nimetatakse TIDES, "Läbipaistev Indeks Erinevatest Laiendatud Osaühikutest". See süsteem registreerib kaevurite poolt pakutava töö, mida tuntakse kui "osaühikuid". Bassein arvutab iga kaastöötaja "osaühikute" protsendi, seejärel lisab nende Bitcoin aadressi basseini ploki malli kui selle protsendi ploki auhinna saaja.

Ploki malli uuendatakse umbes iga 10 sekundi järel, et arvestada kõige kasumlikumate uute tehingutega ja vajadusel muuta ploki auhinna jaotust.

![signup](assets/rem.webp)

Pole oluline, kas teie masinad on uue ploki kaevandamise ajal ühendatud või mitte. Juba esitatud tööd hoitakse järgmise kaheksa basseini poolt leitud ploki jaoks.

Töö hoidmine kaheksa ploki jaoks, mitte loendurite nullimine iga uue kaevandatud plokiga, tähendab, et teie kompensatsioon on 100% ainult siis, kui bassein on leidnud kaheksa plokki pärast teie panustamise alustamist. See tähendab ka, et te jätkate kompensatsiooni saamist kaheksa ploki jooksul, kui lõpetate basseini panustamise.

See mehhanism silub kompensatsiooni ja heidutab "basseini hüppamist", mis hõlmab basseinide regulaarset vahetamist sõltuvalt sellest, milline neist tõenäoliselt järgmise ploki leiab.

### Väljamaksed

Ookeani Kaevandamise toimimine võimaldab selle kaastöötajatel taastada "puhtad" bitcoini, mis tähendab otse ploki auhinnast väljastatud bitcoine.

Erinevalt enamikust teistest basseinidest ei saa Ookean äsja kaevandatud bitcoine; kaastöötajate aadressid integreeritakse otse ploki malli.

Praegu on puhtast bitcoinist tõeliselt kasu saamiseks minimaalne summa 1,048,576 satsi. Iga basseini poolt kaevandatud plokiga peab teie "osaühikute" osakaal andma teile rohkem kui 1,048,576 satsi, et need makstaks teile otse ploki auhinnast.
Vastasel juhul hoitakse teie satsid Ookeanis, kuni teie kogu auhinnad ületavad selle summa.

Kõik Ookeani poolt ajutiselt hoitavad bitcoini on sellel aadressil: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, kõik on kontrollitav TimeChain'is.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
Samuti on võimalik oma satsid välja võtta Lightningu kaudu, kasutades BOLT12. Vaatame, kuidas seda seadistada.

### Basseini Tasud

Tasud jäävad vahemikku 0% kuni 2% sõltuvalt valitud ploki mallist.

## Ookeani Läbipaistvus

### Kaastöötaja Andmed

![signup](assets/1.webp)

Kogu teave basseini kohta on läbipaistev, sealhulgas kõik kasutajaandmed. Selle punkti mõistmiseks vaatame näidet:

[Ookeani armatuurlaual](https://ocean.xyz/dashboard) on teil mitmeid teavitusi nagu hashrate viimase kuue kuu jooksul, basseini osalejate arv, kaevandatud bitcoinide koguarv jne.

Keskendume "Kaastöötajate" sektsioonile. Näete kõigi kaastöötajate nimekirja koos nende keskmise hashrate'iga viimase kolme tunni jooksul, samuti protsendi **"osaühikute"** ja **"hashi"** kohta ülejäänud basseini suhtes.
**"Akciose %"** on töö protsent, mida panustaja on andnud viimase kaheksa ploki jooksul võrreldes ülejäänud basseiniga.
**"Hash %"** on keskmise hashimiskiiruse protsent, mida panustaja on andnud viimase kolme tunni jooksul võrreldes ülejäänud basseiniga.

![signup](assets/2.webp)

Märkate, et "Panustajad" on tuvastatud Bitcoin'i aadressiga. Võite klõpsata ükskõik millisele neist aadressidest, et saada rohkem üksikasju.

Kui võtame esimese, selle, millel on kõrgeim hashimiskiirus [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), näete kõiki üksikasju selle kasutaja kohta: hashimiskiirus, kaevandatud bitcoinide arv, millise plokiga ja isegi iga nende masina (ASICs) üksikasjad. Siiski jäävad nad anonüümseks, nagu Bitcoin'is.

### Ploki Mall

Armatuurlaua ülemises vasakus nurgas on teil "Järgmine plokk". Sellel lehel on neli erinevat ploki malli. Ocean võimaldab igal panustajal valida ploki malli, mida nad soovivad toetada. See ei mõjuta otseselt teie kompensatsiooni. Kui bassein kaevandab ploki, kompenseeritakse kõiki panustajaid sõltumata valitud mallist. See lihtsalt võimaldab kõigil "hääletada" endale sobiva ploki malli poolt.

![signup](assets/3.webp)

**CORE:** Tasu 2%, see on klassikaline Bitcoin Core mall ilma filtrita, nagu nende lehel kirjas "Sisaldab tehinguid ja enamikku spämmist"

**CORE+ANTISPAM:** Tasu 0%, Bitcoin Core filtriga teatud tehingute vastu nagu Ordinals "Sisaldab tehinguid ja piirab spämmi"

**OCEAN:** Tasu 0%, Bitcoin Knot "Sisaldab ainult tehinguid ja mõistlikult väikeseid andmeid"

**DATA-FREE:** Tasu 0%, Bitcoin Knot "Sisaldab ainult tehinguid ilma igasuguste suvaliste andmeteta"

### Erinevus Bitcoin Core ja Bitcoin Knot vahel
Bitcoin Core on tarkvara, mis võimaldab umbes 99% maailma Bitcoin'i sõlmedest töötada. Bitcoin on protokoll, mis tähendab, et nagu Internetis, kus on mitu brauserit, võib samal TimeChain'il koos eksisteerida mitu erinevat tarkvaraprogrammi. Siiski, ühilduvuse murest ja vigade riski piiramiseks, mis jätaksid TimeChain'ile kustutamatud jäljed, töötavad peaaegu kõik Bitcoin'i arendajad Bitcoin Core'is. Bitcoin Knots on Bitcoin Core'i haru, mis tähendab, et see jagab enamikku nende koodist, piirates oluliselt vigade riski. See haru loodi Luke Dashjr poolt, kes soovis rakendada Bitcoin Core'ist rangemaid reegleid ilma kõva haruta. Nüüd eksisteerivad Bitcoin Core ja Bitcoin Knots tänu Nakamoto konsensusele.

## Töötaja Lisamine

Töötaja lisamiseks alustage oma ploki malli valimisest. See valik määrab basseini URL-i, mille sisestate oma kaevurisse (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Järgmisena kasutaja väljale sisestage Bitcoin'i aadress, mille olete ise loonud. Siin on nimekiri ühilduvatest aadressitüüpidest:
- **P2PKH** (Algne aadressitüüp. Algab “1”-ga)
- **P2SH** (Mitme allkirjaga või P2SH-Segwit. Algab "3"-ga) - **Bech32** (Segwit. Algab "bc"-ga.)
- **Bech32m** (Taproot. Algab "bc"-ga. Pikem kui Bech32.)

Kui teil on mitu kaevurit, võite sisestada kõigile neile sama aadressi, nii et nende hashimiskiirused on kombineeritud ja kuvatakse nagu üks kaevur. Samuti võite neid eristada, lisades igale kaevurile eristuva nime. Selleks lisage lihtsalt ".workername" pärast Bitcoin'i aadressi.

Lõpuks, paroolivälja jaoks kasutage `x`.

**Näide:**
Kui valite **OCEAN** malli, on teie Bitcoin'i aadress `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` ja soovite oma kaevurile nimeks panna “Brrrr”, siis peate oma kaevuri liideses sisestama järgmise info:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **KASUTAJA**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **PAROOL**: `x`

Mõne minuti pärast kaevandamise alustamist näete oma andmeid Ocean'i saidil, otsides oma aadressi.

### Töölaud Ülevaade
- **Osalused Tasu Aknas**: See andmed näitavad osaluste arvu, tööd, mille olete basseinile saatnud viimase 8 poolt kaevandatud ploki aknas.
- **Hinnangulised Tasud Aknas**: Hinnang selle kohta, mitu satsi teenite juba tehtud tööga. See ei arvesta tehingutasusid, vaid ainult coinbase'i, uusi bitcoine, mida võrk väljastab.
- **Hinnangulised Sissetulekud Järgmises Plokis**: Hinnang selle kohta, mitu satsi teenitakse, kui plokk kaevandatakse praegu. Pidage meeles, kui see väärtus on väiksem kui 1,048,576 satsi, ei saa te satsid otse oma aadressile. Need saadetakse Ocean'i aadressile, kuni teie teenistus ületab selle läve.

Allpool on graafik, mis kuvab teie hashimiskiiruse ajalugu kuni 6 kuud.

![signup](assets/4.webp)

Siin on teie keskmine hashimiskiirus erinevatel ajaskaaladel, alates 60s kuni 24h, samuti basseini poolt kaevandatud plokkide ajalugu, millele olete panustanud ja mille eest olete tasu saanud.

![signup](assets/5.webp)

Teil on võimalus eksportida selle ajaloo CSV-fail **Laadi CSV alla** nupuga.

![signup](assets/6.webp)

Järgmises jaotises on nimekiri kõigist kaevuritest, kes on selle aadressiga basseiniga ühendatud. Teil on muidugi nende individuaalne hashimiskiirus, aga ka satside arv, mille nad on oma töö eest individuaalselt saanud.

![signup](assets/7.webp)

Võite klõpsata mis tahes kaevuri **Hüüdnime** peal. Siis näete kogu just nähtud teavet, kuid spetsiaalselt selle kaevuri kohta.

Ja lehe allosas on mõned lisateave, kus näete oma aadressi maksete ajalugu, satsid, mida olete kaevandanud, kuid mida teile veel makstud ei ole, ja kokku kaevandatud satsid.

![signup](assets/8.webp)

Siin näete, et **Hinnanguline Aeg Minimaalse Väljamakse Saamiseni** kastis on kirjutatud Lightning, kuna oleme seadistanud BOLT12 pakkumise.

### Lightning Väljamaksete Seadistamine
Nagu te mõistate, on Ocean'i eesmärk maksimeerida läbipaistvust ja minimeerida hoiustamist (teie satside hoidmist teie nimel).
Seetõttu on Lightningi väljamaksete jaoks vajalik kasutada **BOLT12 pakkumisi**. See on uus makseviis Lightning võrgus, mis hakkab ilmuma 2024. aastal ja võimaldab mitmeid asju:
- See on korduvkasutatav makselink, mis võimaldab automaatseid makseid ja, erinevalt Lightningi aadressist, on BOLT12 mittehoiduv.
- See on samuti makseviis, mis annab tõendi makse sooritamise kohta, mida LNURLide puhul ei ole.
- Väga oluline, seda saab kasutada koos Bitcoin'i allkirjaga, et tõestada, et olete nii BTC aadressi kui ka BOLT12 pakkumise omanik.
Tänase seisuga (mai 2024) on vähe lahendusi selle meetodi kasutamiseks. Selles näites kasutame Start9 serverit koos Core Lightninguga. Kui teised tööriistad, näiteks Phoenix Wallet, on integreerinud BOLT12 pakkumised, jääb see õpetus rakendatavaks. Veenduge, et teil on avatud kanalid sissetuleva likviidsusega, vastasel juhul maksed ei toimi.

Alustage, minnes Ocean'i veebilehele, sisestades oma BTC aadressi, seejärel klõpsake vahekaardil **Configuration**.

![signup](assets/9.webp)

Kopeerime **Description** teksti, siin:
`OCEAN Väljamaksed bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Nüüd minge oma Core Lightningi liidesesse oma Start9 serveris (või ükskõik millises rahakotis, mis suudab pakkuda BOLT12 pakkumist).

![signup](assets/10.webp)

Klõpsake **Receive**.

Valige **Offer**, seejärel kleepige eelnevalt kopeeritud tekst **Description** väljale ja jätke **Amount** väli tühjaks.

![signup](assets/11.webp)

Klõpsake **Generate Offer**.

![signup](assets/12.webp)

Olete genereerinud korduvkasutatava ja püsiva makselingi, mis ei vaja keskserverit, nagu on Lightningi aadresside puhul. Kopeerige link ja seejärel naaske Ocean'i lehele.

**Lightning BOLT12 Offer** väljal kleepige makselink ja jätke **Block Height** väli vaikimisi väärtusele. Klõpsake **GENERATE**.

![signup](assets/13.webp)

Selleks, et Ocean saaks tagada, et see makselink on tõepoolest teie oma ilma kontosüsteemi kasutamata, peate allkirjastama just genereeritud sõnumi oma privaatvõtmega, mis vastab teie kasutatavale Bitcoin'i aadressile. Paljud lahendused on olemas sõnumi allkirjastamiseks oma privaatvõtmega. Selles õpetuses võtame näiteks BlueWalleti, kuid meetod on sama kõigi rahakottide puhul.

![signup](assets/14.webp)

Eeldades, et teie privaatvõti on BlueWalletis (võite teha sama riistvara rahakotiga), klõpsake vastaval rahakotil.

![signup](assets/15.webp)

Seejärel **…** üleval paremal.

![signup](assets/15bis.webp)

Ja **Sign/Verify Message**.

![signup](assets/16.webp)

Selles aknas on teil kolm välja: **Address**, **Signature** ja **Message**.

**Address** väljal sisestage oma Bitcoin'i aadress. Kui me naaseme meie näite juurde, on see aadress: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Jätke **Signature** väli tühjaks.
Ja kopeerige genereeritud sõnum väljale **Message** Ocean'i lehel: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Klõpsake **Sign**.

See genereerib krüptograafilise allkirja, mis tõestab, et olete aadressi `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` omanik, ja see allkiri on unikaalne tänu Ocean'i poolt pakutud sõnumile, mis on genereeritud BOLT12 makselingi abil.

![signup](assets/17.webp)

Kopeerige allkiri ja kleepige see Ocean'i lehele, seejärel klõpsake **CONFIRM**.

![signup](assets/18.webp)

Te peaksite nägema kinnitussõnumit.

![signup](assets/19.webp)

Nüüd minge vahekaardile **My Stats**. Ülaosas kuvatakse lisateavet koos BOLT12 makselingiga, mille te varem Core Lightninguga Start9-s genereerisite.

![signup](assets/20.webp)