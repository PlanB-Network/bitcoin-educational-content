---
name: LN Markets
description: Bitcoin kauplemisplatvorm Lightning Network peal
---

![cover](assets/cover.webp)



LN Markets on esimene tõeliselt Lightning-native Bitcoin kauplemisplatvorm, mis võimaldab teil kaubelda finantsvõimendusega Bitcoin tuletisinstrumentidega otse oma wallet Lightningist, ilma KYC-i, kohese arvelduse ja minimaalse hoiustamisega. See 2020. aastal käivitatud süsteem kõrvaldab traditsiooniliste börside hõõrdumise: ei mingit identiteedi kontrollimist, ei blokeeritud hoiuseid, ei ootamist plokiahela kinnituste järele. Teie wallet Lightningist saab teie kauplemiskonto.



## Mis on LN Markets?



LN Markets pakub **Futuurid** (tähtajatuid lepinguid, mille finantsvõimendus on kuni 100×) ja **Optsioonid** (ostuoptsioonid, mille risk on piiratud makstud preemiaga). Platvorm toimib likviidsuse koondamise kihina, mis konsolideerib mitmeid kauplemiskohti optimaalse null-libisemisega täitmise tagamiseks. Teie vahendid on lukustatud ainult teie aktiivsete positsioonide täpseks ajaks, mitte päevadeks või nädalateks, nagu traditsioonilise hoiukonto puhul.



### Saadaval olevad kaubandustooted



**Futuurid (tähtajatu lepingud)**



Perpetual lepingud on futuurid, millel ei ole lõpptähtaega, mis võimaldab teil võimendusega spekuleerida Bitcoin hinnatrendiga. LN Markets pakub kahte marginaali haldamise režiimi:



**Isoleeritud režiim**: Igal positsioonil on oma spetsiaalne varu. Ainult sellele konkreetsele positsioonile eraldatud vahendid on ohus. Kui positsioon jõuab likvideerimishinnani, **liquidiseeritakse ainult see positsioon**, teie teisi positsioone ja ülejäänud saldot see ei mõjuta. Ideaalne riskide rangeks piiramiseks kaubanduse kohta.



**Ristirežiim (ristmarginaal)** : Marginaal jagatakse kõigi teie avatud positsioonide vahel. Teie kogu kontojääk on kõigi teie positsioonide tagatiseks. Kui positsioon läheb halvasti, kasutab süsteem kogu teie olemasolevat saldot, et vältida likvideerimist. **Risk**: Kui teie kogu saldo saab otsa, võidakse kõik teie positsioonid likvideerida samaaegselt. Soovitatav ainult kogenud kauplejatele, kes soovivad maksimeerida kapitali tõhusust.



**Positsioonide juhtimine** :





- Pikk positsioon**: panustate BTC/USD tõusule. Kui hind tõuseb, võidate, kui langeb, kaotate. **Näide**: Bitcoin 100 000 dollaril, avate Long positsiooni 10 000 sats ja 10× finantsvõimendusega. Kui Bitcoin tõuseb 105 000 dollarini (+5%), võidab teie positsioon 50% (5% × 10), st ~5 000 sats kasumit. Kui Bitcoin langeb 95 000 dollarini (-5%), kaotate 50%, st ~5 000 sats kahjumit.





- Lühike positsioon**: panustate BTC/USD langusele. Kui hind langeb, võidad; kui tõuseb, kaotad. **Näide**: Bitcoin 100 000 dollaril, avate lühikese positsiooni 10 000 sats ja 10× finantsvõimendusega. Kui Bitcoin langeb 95 000 dollarini (-5%), võidate 50%, st ~5000 sats. Kui Bitcoin tõuseb 105 000 dollarini (+5%), kaotate 50%.



Võimendus (kuni 100×) võimendab kasumit ja kahjumit proportsionaalselt. **rahastamismäärade** mehhanism (perioodilised tasud iga 8 tunni järel) tasakaalustab pikki ja lühikesi positsioone. Saate samaaegselt hallata kuni 100 futuuripositsiooni.



**Võimalused**



Optsioon on nagu **loteriipilet, mille kehtivusaeg lõpeb**. Te maksate preemiat, et panustada Bitcoin hinna suunda. **Suur eelis**: te ei saa kunagi kaotada rohkem kui makstud preemiat, likvideerimine ei ole võimalik.





- Ostuoptsioon (bullish bet)**: Te panustate, et Bitcoin tõuseb enne kehtivusaja lõppu üle täitmiskoha. Kui hind tõuseb, võidate, kui hind langeb, kaotate ainult preemia ulatuses.





- Müügioptsioon (karuteemaline panus)**: Te panustate, et Bitcoin langeb allapoole täitmispunkti. Kui hind langeb, võidate, kui hind tõuseb, kaotate ainult preemia ulatuses.





- Straddle (volatiilsuse panus)**: Te ostate üheaegselt ostu ja müügi. Sa võidad, kui Bitcoin teeb suure liikumise mis tahes suunas, sa kaotad mõlemad preemiad, kui hind jääb stabiilseks.



Piirang: 50 üheaegset positsiooni. Ideaalne finantsvõimendusega kauplemise alustamiseks ilma likvideerimise hirmuta.



**sats ↔ sUSD**: Konverteerige oma satoshid koheselt sünteetilisteks dollariteks (sUSD), et kaitsta end volatiilsuse eest, või vastupidi, et taastada Bitcoin riskipositsioon.



## Platvormile juurdepääs ja konto loomine



### Mine LN Markets juurde



Mine aadressile [lnmarkets.com](https://lnmarkets.com) ja klõpsa "Ava rakendus".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Looge oma konto



Tervitusekraan pakub mitmeid ühendamisviise:



![Méthodes de connexion](assets/fr/02.webp)



**Võimalikud valikud** :


1. **Registreerige Lightning wallet** (soovitatav) : LNURL-auth koos Phoenix, Breez, Zeus või BlueWalletiga


2. **Registreeri end e-posti teel**: klassikaline konto (piirab Lightning-kogemust)


3. **Alby** või **Ledger**: brauseri laiendused



### Ühendus Lightning'i kaudu (LNURL-auth)



Klõpsake nupule "Registreeru koos Lightning wallet-ga". Skaneerige oma wallet Lightningiga QR-kood:



![QR code LNURL-auth](assets/fr/03.webp)



Teie wallet allkirjastab automaatselt krüptograafilise taotluse ja teie konto luuakse koheselt, ilma e-posti või paroolita. Tugev turvalisus ja täielik anonüümsus.



### Esialgne konfiguratsioon



![Configuration post-connexion](assets/fr/04.webp)



**Kasutatavad parameetrid** :




- Kasutajanimi**: isikupärastage oma kasutajanimi
- Automaatne väljavõtmine**: aktiveerige automaatne väljavõtmine oma wallet-i pärast kauplemise lõpetamist
- Kahefaktoriline autentimine**: täiustatud turvalisus 2FA abil
- Dokumentatsioon**: juurdepääs ametlikele ressurssidele



## Interface tuur



LN Markets kasutajaliides on jaotatud mitmesse sektsiooni, mis on kättesaadavad külgmenüüst:



### Armatuurlaud



![Dashboard](assets/fr/06.webp)



Näitab teie tulemusi tootetüüpide kaupa (Futures Cross, Futures Isolated, Options) koos P&L, kaubeldavate mahtude ja teie isikliku Address Lightning (nt `pivi@lnmarkets.com`).



### Profiil



![Profil trader](assets/fr/07.webp)



Üksikasjalik statistika: tehingute arv, kaupleja tüüp (SCALPER jne), positsiooni keskmine kestus, Long/Short jaotus, võidu määr, keskmised (kogus, marginaal, finantsvõimendus) ja progressiivne tasustruktuur vastavalt mahule.



### Tehingud



![Historique des trades](assets/fr/08.webp)



Vahekaardil Trades kuvatakse teie positsioonide täielik ajalugu koos kõigi oluliste näitajatega: loomise kuupäev, suund (Long/Short), positsiooni suurus (kogus), kohustusliku marginaali, sisenemis- ja väljumishind, realiseeritud kasum/kahjum (P&L) ja kauplemiskulud. Saate filtreerida toote tüübi järgi (futuurid/optsioonid) ja eksportida oma andmeid välise analüüsi või raamatupidamise jaoks.



### Seaded



![Paramètres de la plateforme](assets/fr/05.webp)



Vahekaardil Seaded on kaks vahekaarti: **Konto** ja **Interface**.



**Konto** vahekaart:



Kontohaldus koos redigeeritavate väljadega :




- Kasutajanimi**: muutke oma kasutajanime (nt "pivi") nupu "Update" abil
- E-post**: lisa/muuda oma e-posti aadressi
- Deposit bitcoin address**: bitcoini aadress, mida saate kasutada on-chain vahendite deponeerimiseks.



**Kolme konfiguratsiooni lülitit** :




- Esineda edetabelites**: valige, kas soovite avalikes edetabelites esineda või mitte
- Taproot aadresside kasutamine**: Bitcoin aadresside kasutamine Taproot on-chain hoiuste/väljavõtete tegemiseks
- Automaatse väljavõtte lubamine**: aktiveerige automaatne väljavõtmine teie wallet Lightning'ile pärast kauplemise lõpetamist



**Kontole üleminek**: Jaotis, mis võimaldab teil oma Lightning-konto migreerida klassikalise e-posti/salasõna autentimise juurde.



**Session juhtimine**: "Tühjenda seanss ja kohalikud andmed" nuppu, et katkestada ühendus ja puhastada brauseri kohalikud andmed.



**Interface** vahekaart:



Kohandage kasutajakogemust seitsme lüliti abil:




- Korralduse kinnituse vahelejätmine**: deaktiveerib kinnituse modaali enne kaubanduse täitmist (kiire kauplemine)
- Show tooltips**: kuvab tööriistade näpunäiteid, kui viibida elementide kohal
- Privaatne režiim (maskeerib tundlikud andmed)**: maskeerib summad ja tundlikud andmed liideses (privaatsusrežiim)
- Näita neto PL profiilis**: näita puhaskasumit/kahjumit oma avalikus profiilis
- Kasutage ühikute ikoone**: kuvatakse rahaühikute (sats, $) ikoone
- Heliteadete sisselülitamine**: aktiveerige kauplemissündmuste heliteated
- Töölaua teavituste sisselülitamine**: operatsioonisüsteemi töölaua teavituste aktiveerimine



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin ja sünteetilised USD-saldod koos hoiuste, väljavõtete, ristülekannete, vahetustehingute, rahastamise ja on chain aadressi haldamise ajalooga.



### API



![API V3](assets/fr/10.webp)



LN Markets pakub täielikku API REST (V2 ja V3), et täielikult automatiseerida oma kauplemist skriptide või robotite abil. Saate luua API võtmed kohandatavate õigustega (ainult lugemiseks, kauplemiseks, väljavõtmiseks) otse liidesest. Ametlikud TypeScripti ja Pythoni SDK-d on lihtsaks integreerimiseks saadaval. Täielik API V3 dokumentatsioon on saadaval aadressil [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).



## Rahaliste vahendite esimene sissemakse



Klõpsake nupule "Deposit". Saadaval on kolm meetodit:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: skaneeri QR-kood oma wallet Lightningiga


2. **Invoice**: sisestage summa ja skannige seejärel välkarve


3. **On-Chain**: depoo Bitcoin on chain



## Kauplemine praktikas



### Trade Futures Long: panustamine ülespoole



Klõpsake juhtpaneelilt "Futures" ja seejärel "Isolated". Pika positsiooni avamiseks klõpsake **"Osta "**.



![Interface Futures Long](assets/fr/12.webp)



Klõpsake nupu "Osta" kõrval oleval **kalkulaatori** ikoonil, et kuvada positsioonikalkulaator:



![Calculateur de position Long](assets/fr/13.webp)



**Konkreetne näide** :




- Kogus**: $100 (positsiooni suurus)
- Kaubanduse marginaal**: 12.336 sats (kulukohustuslik marginaal)
- Võimendus**: 7.(iga 1% BTC muutus = 7,73% teie kapitalist)
- Sisenemishind** : $104,863.5
- Likvideerimine**: $92 852 (kriitiline automaatne likvideerimishind): $92 852 (kriitiline automaatne likvideerimishind)
- Väljumishind**: $ 110,000 (kasumi arvutamiseks)
- PL** : 4,492 sats (kasum, kui väljumine on 110 000 dollarit)



**Stsenaariumid** :




- Kasv +4,9%** (110 000 $) : +4 492 sats kasum (+36,4%)
- Neutraalne** (104 863 $) : -185 sats (ainult tasud)
- Alla -11,5%** (92 852 $): täielik likvideerimine (-100%)



Kauplemise kinnitamiseks klõpsake nupule "Osta". **Kaks võimalikku juhtumit** :





- Kui teie kontol on piisavalt likviidsust**, kuvatakse otse kinnitusmoodal (pilt allpool). Klõpsake "Jah", et kauplemine koheselt teostada.



![Confirmation trade Long](assets/fr/14.webp)





- Kui teil ei ole piisavalt sularaha**: selle asemel kuvatakse Lightning QR-kood. Skaneerige seda oma wallet Lightningiga, et maksta nõutav marginaal. Kauplemine avaneb automaatselt makse laekumisel



### Trade Futures Short: panustamine allapoole



Klõpsake **"Müüa "**, et avada lühike positsioon (võidate, kui hind langeb). Avage kalkulaator kalkulaatori ikooniga, et määrata oma positsioon:



![Calculateur de position Short](assets/fr/15.webp)



Kinnitamiseks klõpsake "Müüa". Mis puutub Longi, siis **kaks võimalikku juhtumit**:





- Kui teil on piisavalt sularaha**: otsekinnitusrežiim, klõpsake "Jah"
- Kui teil ei ole piisavalt sularaha**: kuvatakse Lightning QR-kood (pilt allpool). Skaneerige see oma wallet Lightningiga, et maksta nõutav marginaal:



![Paiement Lightning pour Short](assets/fr/16.webp)



Kui Lightning-makse on laekunud, avaneb teie lühike positsioon automaatselt. Seejärel saate seda hallata kauplemisliidesest.



#### Positsiooni sulgemine



Oma positsiooni (pikk või lühike) sulgemiseks klõpsake **väikest risti juhtimisliidese alumises paremas nurgas**:



![Interface de clôture](assets/fr/17.webp)



Kaubanduse lõpetamise kinnitamiseks kuvatakse kinnitusdialoog:



![Confirmation clôture](assets/fr/18.webp)



Modaal kuvab teie jooksva kasumiaruande (kasum või kahjum). Klõpsake sulgemiseks "Jah". Saldo lisatakse (kasum) või lahutatakse (kahjum) teie Wallet-st Lightning'i kaudu koheselt.



### Kaubandus Optsioonid Call: tingimuslik ostuõigus



Optsioonid pakuvad **riski, mis on piiratud** makstud preemiaga, ilma likvideerimise võimaluseta. Ostuoptsioon annab teile õiguse (mitte kohustuse) osta Bitcoin enne tähtaja lõppu täitmishinnaga. Erinevalt futuuridest ei saa te kunagi kaotada rohkem kui investeeritud preemiat.



Klõpsake juhtpaneelil nupule "Valikud", seejärel valige vahekaart "Kõne".



![Interface Options Call](assets/fr/19.webp)



Konfigureerige oma kauplemine järgmiste parameetritega:




- Kogus**: $100 (teie lepingu suurus)
- Kehtivusaeg** : 2025-11-15 (aegumiskuupäev)
- Streik**: $96,000 (sihttase)



Teised väljad arvutatakse automaatselt:




- Marginaal**: 1.045 sats (makstav lisatasu, teie investeering)
- Tasuvus**: $96,923 (hind, et saada oma panus tagasi)
- Delta**: 40 (Bitcoin hinnatundlikkus)



**Kuidas arvutada oma võitu?**



Teie kasum sõltub Bitcoin hinnast tähtaja lõppemisel. Valem: **(BTC hind - Strike) × Contract suurus - makstud preemia**.



**Konkreetsed näited** :





- Bitcoin hinnaga 96 000 dollarit** (praegune hind) : **Kahjum: -1,045 sats** (kaotate preemia)





- Bitcoin hinnaga 97 000 dollarit**: (97 000 - 96 000) × 0,00105 BTC = 1,05 $. Ümberarvestatud sats ≈ 2,175 sats. **Kasum: 2,175 - 1,045 = +1,130 sats** (+108% kasum)





- Bitcoin hinnaga 98 000 $**: sisemine väärtus = 2000 $ ≈ 3 224 sats. **Kasum: +2,179 sats** (+208% kasum)





- Bitcoin hinnaga 100 000 dollarit**: sisemine väärtus = 4000 dollarit ≈ 5,263 sats. **Kasum: +4,218 sats** (+403% kasum)





- Bitcoin alla 96 000 dollari**: Optsioon aegub väärtusetult. ** Piiratud kahjum: -1,045 sats**, likvideerimine ei ole võimalik



Klõpsake nuppu "Osta kõne". Ilmub kinnitusdialoog:



![Confirmation Call option](assets/fr/20.webp)



Kinnitamiseks klõpsake uuesti nuppu "Osta kõne". Valik ilmub "Running Options" (jooksvad valikud). Aegumisel arvutab LN Markets automaatselt sisemise väärtuse ja korrigeerib teie kasumit/kahjumit.



**Märkus müügioptsioonide kohta** : Toiming on identne ostuoperatsiooniga, kuid vastupidine. Müügioptsiooniga panustate Bitcoin hinna **langusele**. Kui Bitcoin langeb allapoole teie riski, võidate; kui see jääb kõrgemale, kaotate ainult makstud preemia. Kasumi arvutamine järgib sama loogikat: **(Strike - BTC hind) × Contract suurus - makstud preemia**.



### Välgafondi väljavõtmine



Klõpsake nuppu "Taganemine":



![Modal de retrait](assets/fr/21.webp)



**Metoodika** : LNURL, Invoice, Lightning Address, On-Chain.



**Invoice menetlus** :


1. Lightning arve genereerimine wallet-st


2. Koopia arve (algab sõnaga `lnbc...`)


3. Sisestage see LN Markets väljale


4. Kinnitage tagasivõtmine


5. Teie wallet krediteeritakse 1-3 sekundiga



Ei mingeid välkkiirendustasusid, ainult minimaalsed marsruutimiskulud (praktikas <0,1%).



## Riskid ja parimad tavad



** Peamised riskid** :




- Täielik likvideerimine**: kõrge finantsvõimendus võib hävitada 100% marginaalist minutitega
- Eksperimentaalteenus**: alfa-faas, tehnoloogiline ebakindlus
- Vastaspoole risk**: platvorm jääb üheks vastaspooleks



**Parimaid tavasid** :



1. **Kapitali juhtimine**: võtke vastu teie profiilile kohandatud riskijuhtimisstrateegia. Näiteks: eraldage 5% oma koguvaradest finantsvõimendusega kauplemisele, seejärel riskige maksimaalselt 1% sellest kapitalist ühe tehingu kohta (nt: 1 BTC vara → 5M sats kauplemiseks → 50k sats maksimaalne risk positsiooni kohta)



2. **Süstemaatiline stop-loss**: konfigureerige stop-lossid, et piirata oma kahjumit kaubanduse kohta. Näiteks 1% riskireegli puhul moodustavad isegi 10 järjestikust kaotavat tehingut ainult 10% teie kauplemiskapitalist



3. **Alustage väikeselt**: katsetage esmalt mõne tuhande satelliidiga, et mõista mehhanisme enne kapitali juhtimise strateegia rakendamist



4. **Regulaarne kasumi väljavõtmine**: kindlustage oma kasum oma peamises wallet, jättes platvormile ainult aktiivse kauplemiskapitali



5. **Vahtuge finantsvõimenduse eest**: vältige finantsvõimendust >20×, kui te ei ole täielikult teadlik likvideerimisriskidest



**Kulud**: ei ole Lightning deposiit/väljavõtutasusid, spread ~0,1% kauplemiskoha kohta (langeb kuni 0,06% sõltuvalt mahust).



## Eelised ja piirangud



**Eelised** :




- Mittekohustuslik (kogu kontroll, v.a kauplemisperioodid)
- KYC-vaba (anonüümsus Lightning/Nostr kaudu)
- Kohesed arveldused (hoiused/väljavõtmised sekundite jooksul)
- Zero-slippage täitmine koos likviidsuse koondamisega
- API avalik ja Nostr toetus



**Piirangud** :




- Teenuse alfa (võimalikud arengud)
- Madalam likviidsus kui Binance/Deribit
- USA elanikele keelatud



## Kokkuvõte



LN Markets kehastab Bitcoin kauplemise olulist arengut, integreerides Lightning Network, et anda kontroll tagasi kasutajatele. Asjatundlikele bitcoin'ile, kes soovivad spekuleerida ilma oma suveräänsust ohustamata, on see ainulaadne alternatiiv traditsioonilistele tsentraliseeritud börsidele.



Platvorm areneb edasi, arendamisel on USDT lineaarsed futuurid ja mittekaubanduslik kauplemine Discreet Log Contracts (DLC) kaudu. Rakendades häid riskijuhtimise tavasid (väikesed summad, stop-loss, regulaarsed väljavõtmised), saab LN Markets võimsaks vahendiks Bitcoin võimenduse vastutustundlikuks uurimiseks.



Alustage väikselt, katsetage mõne tuhande satelliidiga ja uurige järk-järgult seda uut Lightning Network piiri. Head suveräänset kauplemist ⚡️!



## Ressursid





- [LN Markets ametlik kodulehekülg](https://lnmarkets.com)
- [Dokumentatsioon](https://docs.lnmarkets.com)