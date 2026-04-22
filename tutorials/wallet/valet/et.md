---
name: Valet Bitcoin
description: Valet toob teie taskusse mittehooldatava välgumissõlme
---

![cover_valet](assets/cover.webp)



## Sissejuhatus


Valet on kergekaaluline, isekasutatav Bitcoin ja Lightning wallet, mis pakub algajatele lihtsat ja mugavat sisseelamisprotsessi. See on spetsiaalselt kohandatud Bitcoin kogukondade ja ringmajanduse teenindamiseks, eriti kaugetes piirkondades.


See on **Simple Bitcoin Wallet (SBW)** fork, millel on täiustatud Hosted Lightning kanali funktsioon nimega **Fiat Channels**, mis on loodud selleks, et igaüks saaks Lightning-makseid vastu võtta ilma volatiilsusriskideta.


Valet on praegu saadaval ainult Androidi seadmetele ning seda saab alla laadida ja paigaldada mitmest avatud rakenduste poest. Arendajate privaatsuse ja KYC-ga seotud probleemide tõttu ei ole Valet siiski **sisaldatud** Google Play Store'is**.



## Laadige alla ja paigaldage Valet


Valet saab APK-failina alla laadida Standard Sats' GitHubi lehelt. [Standard Sats](https://standardsats.github.io/) on ettevõte, mis arendas Valet.


👉 Valeti allalaadimiseks külastage Standard Sats [GitHubi lehekülge](https://github.com/standardsats/valet/releases) ja otsige üles **uuim** versioon (see on sageli kõige ülemine).


👉 Mine **Assets** ja klõpsa failil, millel on ainult **.apk** laiendus. Teie allalaadimine algab automaatselt.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Kui allalaadimine on lõppenud, minge oma seadme **Failihaldurisse** > **Laetud** ja valige Valet apk-fail.


![Select_valet_apk](assets/en/002.webp)


👉 Paigaldage see ja mõne sekundi pärast on teie rakendus valmis ning ilmub teie avakuvale.


![valet_icon_on_homescreen](assets/en/003.webp)


Alternatiivina saate Valet alla laadida ka **F-Droid** rakenduste poest. Kui teil ei ole F-Droid rakendust oma seadmes, saate selle alla laadida ja installida [siit](https://f-droid.org/en/).


👉 Avage oma avakuval F-Droid ja otsige **Valet**. Valige kahest ilmuvast valikust esimene valik, millel on **lilla ja valge ikoon**, ja klõpsake **Laadi alla**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Pärast allalaadimist klõpsake **Install** ja järgige ekraanil kuvatavaid juhiseid. Kui installimine on lõpetatud, saate käivitada Valet'i F-Droid-st, klõpsates **Open**, või käivitada selle oma seadme avakuvalt.



## Bitcoin Wallet loomine


Bitcoin wallet saate Valetis seadistada kahe lihtsa sammuga.


👉 Käivitage Valet seadme avakuvalt või F-Droid rakendusest. Ilmub wallet häälestusekraan, millel on kaks võimalust: **Loo uus Wallet** ja **Vaimalda olemasolev Wallet**.


👉 Valige **Loo uus Wallet** ja kohe luuakse uus wallet ning teid suunatakse edasi kodulehele.


![set_up_a\_new_wallet](assets/en/006.webp)



## Varundage oma seemnefraasi


👉 wallet avalehel klõpsake **Green kaardil**, millel on kiri **"Koputage, et salvestada wallet taastamise fraas, juhul kui te kunagi kaotate või asendate oma seadme".**


![seed_phrase_green_card](assets/en/007.webp)


👉 Kuvatakse 12 ingliskeelset sõna. Kirjuta need paberile, järjekorras 1 kuni 12, ja hoia neid alles.


![the_seed_phrase](assets/en/008.webp)


### Tähelepanu ⚠️:


Pöörake tähelepanu järgmistele elementidele:


- Nagu te juba teate, on Valet isehooldus wallet, seega on teie seed fraas ainus juurdepääs teie Wallet taastamiseks.
- Kui te kunagi kaotate oma seed fraasi, ei saa te **ei kunagi** juurdepääsu oma wallet-le.
- Kui keegi saab teie seed fraasi, võib ta pöördumatult varastada kõik teie Bitcoin-d.


Seega peate oma 12-sõnalise seed fraasi üles kirjutama ja seda turvalises kohas hoidma. Te ei tohiks kunagi teha ekraanipilti, salvestada seda e-kirjas eelnõuna ega salvestada seda mis tahes elektroonilises seadmes, mis on kunagi internetti ühendatud.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Bitcoin vastuvõtmine ja saatmine Valetiga


Valet on isekasutatav wallet, millel on nii on-chain kui ka Lightning Bitcoin võimekus. See tähendab, et te võite saada ja saata Bitcoin Valetist välja kas **On-chain** või **Lightning Network** kaudu.


Kuid selleks, et saaksite Lightning'i kaudu Bitcoin vastu võtta või saata, peate looma Lightning-kanali, kasutades oma on-chain Bitcoin-d Liquidity'ina. Või võite osta müüjatelt mõne Lightning-kanali likviidsuse.



## Kettasuunalise Bitcoin Address genereerimine


Bitcoin vastuvõtmiseks on-chain kaudu peate looma Bitcoin aadressi.


👉 wallet avalehel näete **Oranžit** ja **lillat kaarti**, mis kannavad vastavalt tähiseid **Bitcoin** ja **Valguse**.


👉 Klõpsake oranžil kaardil, millel on tähis **Bitcoin**. Teid suunatakse ümber ekraanile, kus kuvatakse Bitcoin aadress.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Saate aadressi **kopeerida** ja saata selle isikule, kes teile Bitcoin saadab, või klõpsata nupule **jaotada**, et saata QR-kood isikule sotsiaalmeedia või muude suhtluskanalite kaudu.


👉 Samuti saate klõpsata nupule **Muuda**, et määrata sellele aadressile saadetavate Bitcoin-de arvu.


**Väljaanne:** Nagu arve puhul, on redigeerimisfunktsioon kasulik stsenaariumide puhul, kus te soovite saada konkreetsele aadressile teatud summa Bitcoini, kuid see ei tähenda, et aadressile ei saa saata suuremaid või väiksemaid summasid.


👉Klikkige **Muute värskeid aadresse**, et luua uusi juhuslikke aadresse.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 on-chain Bitcoin aadressi saate genereerida ka wallet avalehel altpoolt nupule **Võta** klõpsates. Seejärel valige **Vasta bitcoini aadressile** ja jätkake sama protsessi ülalpool.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Bitcoin saatmine on-chaini kaudu


Bitcoin saatmine Valet wallet-st on-chain kaudu on lihtne ülesanne.


👉 wallet avalehel klõpsake altpoolt nuppu **Saatmine**, sisestage Bitcoin aadress või klõpsake aadressi QR-koodi skaneerimiseks nuppu **Skaneerimine** ja seejärel klõpsake nuppu **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Sisestage Bitcoin summa, mida soovite saata. Saate käsitsi sisestada summa Sats või Fiat-valuutas või võite klõpsata **Max**, et kasutada kogu oma on-chain saldot.


👉 Samuti saate kohandada tehingu eest makstavaid tasusid, klõpsates väikesel rohelisel kastil, millel on märge **tasu**, ja seejärel libistades valget punkti paremale või vasakule, et vastavalt suurendada või vähendada tasusid. Tehingu saatmiseks klõpsake **Ok**.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Lightning Network kanali seadistamine


Nagu eespool mainitud, on Valet isekasutatav Bitcoin ja Lightning wallet; seega, et saaksite saata ja vastu võtta Bitcoin läbi Lightning-võrgu, peate kõigepealt seadistama Lightning-kanali, järgides järgmisi samme:


👉 Klõpsake avakuval **lillat värvi kaardil**, millel on kirjas **Valgustus**. Teid suunatakse lehele, kus on järgmised valikud:



- Skaneeri sõlme QR
- Ostmine aadressil LNBIG.COM
- Ostmine aadressil BITREFILL.COM
- Taotlus LN graafi resünkroonimiseks.


Kui valite **Ostan lnbig.com** või **Ostan bitrefill.com**, suunatakse teid nende ettevõtete veebisaitidele, kus saate osta mitme mahuga sissetulevat likviidsust. Ignoreerige esialgu viimast valikut **Küsige LN graafiku resünkroniseerimist**.


Seega on meie valikuks siinkohal **Scan a Node QR**. Siinkohal peate olema otsustanud ja saanud selle sõlme **QR-koodi**, millele soovite kanali avada. Võite avada kanaleid mis tahes valitud avalikku sõlme. Vaadake välja [1ML](https://1ml.com/) või [Amboss](https://amboss.space/), valige ükskõik milline avalik sõlmpunkt ja skaneerige valitud sõlme vastav QR-kood.


![channel_opening_options](assets/en/016.webp)


👉 Teid suunatakse automaatselt järgmisele lehele, kus peate nüüd oma kanalit rahastama. Jällegi, enesekohane Lightning-võrgu kasutamine eeldab, et kasutate kanali rahastamiseks oma Bitcoin-d. See tähendab, et teil peab olema Bitcoins on-chain wallet, millega Lightning-kanalit rahastada. Palun lugege seda artiklit [Hacken](https://hacken.io/discover/lightning-network/), lugege rohkem Lightning-võrgustiku kohta.


![fund_channel](assets/en/017.webp)


👉 Sisestage **summa** Bitcoin, millega soovite kanalit rahastada, või klõpsake **Max**, et kasutada kogu oma on-chain Bitcoin saldo. Te võite kohandada **tasu** või jätta vaikimisi seadistatud tasu ja klõpsata nuppu **Ok**.


**Väljaandmine:** Summa, millega te kanalit rahastate, on teie uue kanali läbilaskevõime (st Sats kogumaht, mida saab sellesse kanalisse ja sellest kanalist läbi viia)


Samuti on oluline, et kasutate kanali avamisel rahastamissummana üle **100 000 Sats**. Seda seetõttu, et paljud Lightning-sõlmed nõuavad kanali avamiseks vähemalt 100 000 Sats mahutavust. Seega, et vältida katsetusi ja vigu, kasutage lihtsalt sellest vahemikust suuremaid summasid.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 Sel hetkel, kui te vaatate oma wallet kodulehte, näete, et teie rahastamissumma on nüüd üle viidud **Bitcoin kaardilt** **Lightning-kaardile**. Teie tehinguajaloos näete, et rahastamistehingut töödeldakse.


![channel_funding_processing](assets/en/020.webp)


👉 Kui klõpsate Lightning-kaardil, näete teavet, mis näitab, et teie Lightning-kanal on avatud. Samuti näete oma tehingute nimekirjas **kanali rahastamistehingut**. Oodake, kuni teie rahastamistehing kinnitatakse blockchain ja teie Lightning-kanal on valmis.


![channel_opening](assets/en/021.webp)


👉 Niipea kui rahastamistehing on kinnitatud, klõpsake oma avalehel **Välgukaardil** ja te näete oma välgukanali kohta järgmist teavet:



- PUNKTIDEGA SEPAREERITUD NUMBRID:** Need on sõlmede IP-aadressid. (vastavalt IPV4 ja IPV6)
- VÕIMALUS:** See on Sats kogumaht, mida saab selle kanali kaudu saata ja vastu võtta
- CAN SEND:** See on kogus Sats, mida saate praegu välja saata. Märkate, et see on peaaegu sama arv kui **Kapatsiteet**. See tuleneb sellest, et te ei ole veel ühtegi makset selle kanali kaudu välja saatnud.
- CAN RECEIVE:** See on arv Sats, mida saate hetkel sellele kanalile vastu võtta. (See on hetkel vähe või mitte midagi, sest selleks, et te saaksite vastu võtta, peate kõigepealt saatma välja mõned Sats, et luua sissetulev Liquidity)
- TAGASTATAV:** See näitab summat, mis makstakse teie on-chain aadressile tagasi, kui te sulgete oma kanali. Seda nimetatakse ka teie **Kanali kohalikuks saldoks**. Pange tähele, et see on veidi väiksem kui kanali maht, ja seda seetõttu, et kanali sulgemisel peate blockchain-l sulgemistehingu avaldamiseks maksma tasu, nagu te tegite ka kanali rahastamisel. Seega on süsteem maha arvanud ligikaudselt väikseima summa, mida te maksate)
- VÄLJAKUTSE:** Kui keegi saadab sinu kanalile sats või kui sa üritad kellelegi sats saata ja mis tahes põhjusel on tehing hilinenud, siis kuvatakse seda sageli selles väljal.


![channel_info](assets/en/022.webp)


## Sats saatmine teie kanali kaudu


Sats saatmine Lightning Network kaudu on lihtne ülesanne.


👉 Vajutage avalehel allosas **Saatke** ja **liidestage** Lightning-arve (peate olema selle kopeerinud) ettenähtud väljale või vajutage **Scan**, et skannida Lightning-arve QR-koodi.


![click_send_or_scan](assets/en/023.webp)


Enamik Lightning arveid on varustatud eelnevalt sisestatud summaga, mis tuleb tasuda. Kuid mõnel juhul võib tegemist olla avatud arvega, kus peate summa ise sisestama.


👉 Sisestage summa **Dollarites** või **Sats** või klõpsake **Max**, et kasutada kogu oma välkekanali saldo, ja seejärel klõpsake **Ok**. Niipea, kui hea tee on leitud, saadetakse teie makse ja see viiakse lõpule mõne sekundi jooksul. Hoidke silm pealehel, et näha, kas makse on lõpule viidud. See saab rohelise märkeruudu, kui see on lõpule viidud.


![enter_the_amount](assets/en/024.webp)


## Sats vastuvõtmine teie kanali kaudu


Maksete vastuvõtmine teie Lightning-kanalis sõltub suuresti sellest, kas teil on sissetulev Liquidity või mitte. Pärast kanali avamist ei saa te makseid vastu võtta enne, kui olete vähemalt saatnud mõne Sats, et **luua sissetulev likviidsus** kanaliühenduse teises otsas. Selleks, et kinnitada, kas saate Sats vastu võtta ja kui palju Sats saate vastu võtta, kontrollige oma kanali teabes välja **võib vastu võtta**. See näitab, kui palju Sats te igal ajahetkel saate.


Oletame, et olete saatnud oma kanalist välja Sats, teil on nüüd sissetulev likviidsus ja te saate Sats vastu võtta.


Lightning-kanalis vastuvõtmiseks peate looma arve. Erinevalt Bitcoin on-chain, mis kasutab aadresse, kasutab Lightning-võrk arveid. Valetis on arve genereerimiseks kaks teed.


#### VÕIMALUS 1


👉 Klõpsake avalehel allosas **Vastuvõtmine**, valige **Vastuvõtmine välkarvele**. Täitke arvele laekuv summa ja klõpsake **Ok**. Kopeerige arve või jagage QR-koodi maksjaga.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### VÕIMALUS 2


👉 Klõpsake oma wallet avalehel lillat värvi Lightning-kaardil. Koputage kuskil oma kanalil ja ekraanile ilmub valikute nimekiri. Valige **Kanalile vastuvõtmine** ja sisestage summa, mida saate (kas Sats või dollarites). Samuti näete arve täitmisel, kui palju Sats saate vastu võtta (sissetulev maht). Klõpsake **Ok** ja kopeerige arve või jagage QR-koodi maksjaga.


![receive_to_channel](assets/en/028.webp)


**Valve:** Esimene valik on universaalne valik, mis tähendab, et kui teil on rohkem kui üks aktiivne kanal ja te kasutate esimest valikut, valib süsteem automaatselt ühe teie kanalitest Sats vastuvõtmiseks.


Seega on antud stsenaariumi puhul parim kasutada teist võimalust, kui soovite saada Sats konkreetsele kanalile.


### Teie kanali hüpikakende valikute selgitamine


Kui koputate oma kanalile, kuvatakse järgmised valikuväljad:


![channel_pop_ups](assets/en/029.webp)


**LIGHTNING KANALI DETAILIDE JAGAMINE:** See võimaldab teil jagada oma kanali andmeid, nagu näiteks kaugkeskuse ID, kohaliku kanali ID, rahastamistehing, loomise kuupäev jne.


**SULGE KANAL WALLETILE:** Saate oma välgukanali sulgeda, millal iganes soovite. Oma kanali sulgemiseks kontrollib süsteem Bitcoin saldot, mis on teie enda poolel (mäletage **"Saab saata "** välja, mida nimetatakse ka teie kohalikuks saldoks), ja saadab selle teile tagasi. Valetis saate valida, kuhu soovite, et Bitcoin saadetakse kanali sulgemisel. Nii et **Sulgege kanal wallet** on üks teie kahest valikust.


👉 Klõpsake seda valikut ja valige **Bitcoin**. Alustatakse kanali sulgemist ja teie kanali Bitcoin saldo saadetakse tagasi teie wallet on-chain aadressile.


![close_channel_to_wallet](assets/en/030.webp)


**KANALI SULGE ADDRESS:** See on teine võimalus kanali sulgemiseks. Kui te valite selle valiku, palutakse teil sisestada wallet aadress, millele saadetakse teie kanali Bitcoin saldo. Pange tähele, et selle valiku puhul saate skannida ainult selle Bitcoin aadressi QR-koodi, kuhu soovite kanali sulgeda. Praegu puudub võimalus aadressi käsitsi sisestamiseks.


👉 Klõpsake seda valikut, skannige Bitcoin aadressi ja klõpsake **Ok**. Kanali sulgemine algab ja teie Lightning Bitcoin saldo saadetakse skaneeritud aadressile.


![scan_address_and_Ok](assets/en/031.webp)


**KANALILE KASUTAMINE:** See on sama, mis arve genereerimine, kuid mõnel juhul võib teil olla rohkem kui üks kanal, sealhulgas Fiat-kanalid (ainulaadne Lightning-kanal, mis on saadaval Valet wallet-s). Seega, kui teil on avatud mitu kanalit, tagab see valik, et saate makse konkreetsele kanalile.


**TÄITA MUUDEST KANALIST:** See valik on funktsioon, mis võimaldab teil täita ühte kanalit teistest olemasolevatest kanalitest. Näiteks kui teil on 2 erinevat Lightning-kanalit (A ja B) ja Bitcoin saldo kanalil A on tühi, saate selle valikuga hõlpsasti ja automaatselt kanali A saldot kanalilt B täiendada.


**Es on ka see võimalus, millega saate makse saamiseks koostada arve, kuid kui kasutate seda võimalust, maksab saatja otse teile. See tähendab, et makse ei hüppa läbi erinevate sõlmede, enne kui see jõuab sinuni, nagu tavaline Lightning-makse. Seega sisuliselt teab saatja, et see olete teie, kellele ta maksis, teab teie kanali ID-d jne. Seda võimalust saab sageli kasutada siis, kui saate makse allikalt, mida usaldate, ja teil ei ole vaja säilitada oma privaatsust.


## Hostitud ja Fiat-kanalid


Nagu paljud teised Bitcoin wallet, on ka Valet lihtne ja kerge Bitcoin ja Lightning wallet. Kuid sellel on ainulaadne Lightning funktsioon, mis eristab seda enamikust teistest Bitcoin wallet-dest. See funktsioon kannab nime **Hosted and Fiat Channels**.


Fiat-kanalid on Lightningi rakendamise tüüp, mis võimaldab Lightning-võrgustiku lihtsat kasutuselevõttu ja kasutamist. See on hoiulahendus, mis võimaldab täielikku anonüümsust, nagu tavalise Lightning-kanali puhul. Fiat-kanalite tehnoloogia võimaldab Lightning-võrgus luua ka Bitcoin tuletisinstrumente. Näiteks saavad kaupmehed Fiat-kanalite abil võtta vastu stabiilse väärtusega Bitcoin makseid, muretsemata Bitcoin volatiilsuse pärast.


Fiat-kanalite praegune rakendamine Valetis võimaldab luua stabiilseid sünteetilisi Fiat-valuutasid, mille tagatiseks on Sats. See kasutab vastuvõtja-kliendi suhet, kus vastuvõtja on mis tahes Lightning-sõlm, mis pakub seda teenust, ja klient on Valeti kasutaja. Tegemist on hoiulahendusega, sest kõik Sats on Hosti poolel; siiski toimub arve loomine, tori marsruutimine ja eelpildi loomine endiselt kliendi poolel, nagu tavalise Lightning-kanali puhul.


Fiat-kanali avamine toimub samamoodi nagu Lightning-kanali avamine. Ainus oluline erinevus on see, et sellisel juhul ei pea klient (Valet kasutaja) siduma likviidsust on-chain, et luua kanali võimsust. Host määrab kanali mahu ja suunab kõik kliendi jaoks tehtavad maksed.


👉 Fiat-kanali avamiseks klõpsake lillat värvi **Välgukaardil** oma wallet avalehel. Valige **Scan Node QR** (Siinkohal peate olema tuvastanud Hosti, millele soovite kanali avada, ja saanud sõlme QR-koodi. Näide Host-sõlme kohta, millele saate avada Fiat-kanali, on SATM-sõlm Standard Sats poolt)


**Attepanek:** On oluline märkida, et igaüks võib olla saatejuht. Kõik, mida te vajate, on Lightning-sõlme käivitamine koos **Fiat-kanali pluginaga** ja **Hedging-teenusega**. Fiat-kanalid on avatud lähtekoodiga projekt, mille on koostanud *Standard Sats*. Lugege selle kohta lähemalt [siin](https://github.com/standardsats/fiat-channels-rfc) ja [siin](https://standardsats.github.io/).


SATM-sõlme QR allpool:


![SATM_node_QR](assets/en/032.webp)


👉 Kui olete skaneerinud sõlme QR-koodi, klõpsake **Taotle USD fiat-kanalit** või **Taotle EUR fiat-kanalit** (See on fiat-denominaal, milles teie Fiat-saldod noteeritakse). Praegu valige USD ja klõpsake **OK**. Kanal avatakse automaatselt ja saate kohe alustada Sats vastuvõtmist. Näete, see on nii lihtne!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Mine oma wallet kodulehele, seal näed **helerohelist** kaarti, millel on kirjas **USD**, see on sinu **Fiat-kanal**.


![fiat_channel_card](assets/en/035.webp)


**Attentsioon:** Kui saate Sats Fiat-kanalil, siis on teie saadud Sats fiat-väärtus fikseeritud stabiilse saldona, samas kui Sats maht ujub koos Bitcoin hinnaga. See lahendus on mõeldud peamiselt kaupmeestele, kes soovivad Sats maksmiseks vastu võtta, kuid ei soovi silmitsi seista Bitcoin volatiilsusega seotud probleemidega. See aitab neil säilitada alati stabiilse väärtuse, kuid samas saavad nad teha tehinguid Lightning-võrgus, nautides Bitcoin globaalset levikut ja kiiret arveldamist Lightning Network vahetusvahendina.


Kui teie Fiat-kanal luuakse, näete järgmisi väärtusvälju ja nende tähendust:


![fiat_channel_info](assets/en/036.webp)



- PUNKTIDEGA SEPAREERITUD NUMBRID:** Need on sõlmede IP-aadressid. (vastavalt IPV4 ja IPV6)
- SERVERI HINNAGA:** See on Bitcoin turuhind, millega host pakub teile teenuseid. See erineb sageli veidi valdavast turuhinnast, sest Host võib lisada väikese lisatasu. Selle määra määramine on täielikult vastuvõtja otsustada; seega võib see ka vastuvõtjal erineda.
- FIAT SALDO:** See on lukustatud stabiilne fiatväärtus iga satelliidi kohta, mida saate sellel kanalil. Pidage meeles, et nagu eespool selgitatud, iga kord, kui saate Sats oma Fiat-kanalile, lukustatakse Sats fiat-väärtus vastuvõtu ajal kohe sünteetilise stabiilse fiat-väärtusena sellesse väljale. Teie **Fiat saldo** väärtus ei kõigu Bitcoin turuhinnaga. Kui soovite teha makseid sellest kanalist, saate saata ainult selle Fiat-saldo Sats ekvivalendi. Seega mõelge sellele kui digitaalsele fiat-valuutale, mille taga on Sats.
- VÕIMALUS:** See on Sats kogumaht, mida saab selle kanali kaudu saata ja vastu võtta. (Selle määrab ka vastuvõtja. Ja erinevalt tavalisest Lightning-kanalist saab seda võimsust vastavalt vajadusele reguleerida Hosti poolt)
- VÕIB SAADA:** See on Sats maht, mida saate igas punktis saata, lähtudes teie fiat-saldost. See on täiesti erinev sellest, mis teil on tavalises Lightning-kanalis, sest see väärtus ujub koos Bitcoin hinnaga. Seega on see, mida te siin näete, teie Fiat-saldo Sats väärtus igal ajahetkel, mis põhineb **Serveri kursil**.
- CAN RECEIVE:** See on arv Sats, mida saate hetkel sellele kanalile vastu võtta. Pärast kanali loomist peaks see väärtus olema sama, mis kanali läbilaskevõime.
- VÄLJAKUTSE:** Kui keegi saadab sinu kanalile sats või kui sa üritad saata kellelegi sats ja mis tahes põhjusel on tehing hilinenud, siis kuvatakse seda sageli sellel väljal.


Siin on olulised asjad, mida tuleb Fiat'i kanalite kohta tähele panna:



- Erinevalt tavalisest Lightning-kanalist saate fiat-kanali avamisel kohe alustada Sats vastuvõtmist, kuid te ei saa saata. Saate Sats välja saata alles siis, kui olete Sats vastu võtnud.
- Igal ajal on vara, mis saadetakse ja millest saadetakse, Sats. *Fiat Saldo* on lihtsalt sünteetiline IOU esindus Bitcoin väärtusest, mis on saadud igal ajahetkel. Seega ei ole see token loomine ega uus krüptoraha.
- Fiat-kanal on kasulik peamiselt kaupmeestele/ettevõtetele, kes on Bitcoin maksete vastuvõtmise suhtes skeptilised volatiilsusega seotud probleemide tõttu. See võib olla kasulik ka ettevõtetele, kes soovivad maksta oma töötajatele palka Bitcoin-s, ilma et nad peaksid kandma Bitcoin volatiilsuse tagajärgi, mis võivad muuta nende palgakapitali ebastabiilseks. See võib olla kasulik ka üksikisikutele, kes elavad piirkonnas, kus Bitcoin kasutatakse valdavalt, kuid kellel on fikseeritud elamiskulud.
- Pange tähele, et puudub väli, millel on märge **KASUTATAV**. See tuleneb sellest, et tehniliselt ei saa Fiat-kanalit sulgeda. Te võite lõpetada Fiat-kanali kasutamise ainult selle saldo tühjendamisega oma tavalisse Lightning-kanalisse.


### Teie Fiat Channel Pop-Up valikud selgitavad


Kui koputate oma Fiat Lightning kanalile, kuvatakse järgmised väljad:


![fiat_channel_pop_up](assets/en/037.webp)


**HOSTED CHANNEL DETAILS SHARE:** See võimaldab teil jagada oma Fiat-kanali andmeid, näiteks kaugkeskuse ID, kohaliku kanali ID, loomise kuupäev jne.


**KANALI SEISUKORD:** See võimaldab eksportida kanali seisukorda igal hetkel. See on tavaliselt kasulik kanali vigade parandamisel ja Host võib paluda seda jagada, kui selleks on vajadus.


**KANALITE SALDODEERIMINE:** Nagu varem mainitud, ei saa tehniliselt Fiat-kanalit sulgeda, kuid saate oma kanali saldo tühjendada olemasolevasse tavalisse Lightning-kanalisse. See liigutab automaatselt teie Fiat'i saldoga samaväärse Sat'i saldo teie tavalisse Lightning-kanalisse.


**KANALILE TAGASI:** See on sama asi, mis arve genereerimine, kuid mõnel juhul võib kasutajal olla rohkem kui üks Fiat-kanal erinevate Hostidega, sealhulgas tavalised Lightning-kanalid. Seega, kui kasutajal on avatud mitu kanalit, tagab see valik, et ta saab makse konkreetsesse kanalisse.


**TÄITA MUUDEST KANALIDEST:** See valik on funktsioon, mis võimaldab kasutajal täita ühte kanalit teistest olemasolevatest kanalitest. Nii et selle valikuga saate oma Fiat-kanali uuesti täita tavalisest kanalist või teistest olemasolevatest Fiat-kanalitest, täpselt samamoodi, nagu te saaksite tühjendada.


**Es on ka see võimalus, millega saate makse saamiseks koostada arve, kuid kui kasutate seda võimalust, maksab saatja otse teile. See tähendab, et makse ei hüppa läbi erinevate sõlmede, enne kui see jõuab teieni. Seega sisuliselt teab saatja, et see olete teie, kellele ta maksis, teab teie kanali ID-d jne. Seda võimalust saab sageli kasutada, kui saate makse allikalt, mida usaldate, ja teil ei ole vaja säilitada oma privaatsust.


## Valet seaded:


Nagu igal teiselgi rakendusel, on ka Valetil rakendussätted, mida saate kohandada vastavalt oma maitsele. Seadete lehele pääseb avakuvalt ekraanilt.


👉 Avakuval klõpsake seadete avamiseks ekraani paremas ülemises nurgas asuval ikoonil **Gear**. Allpool on esitatud seadete sektsioonis olevad komponendid.


![settings_icon](assets/en/038.webp)


**LOKALISTE KANALITE TAGASIVÕTMINE ON LÜLGITATUD:** Kui see on muidu **väljalülitatud,** siis peaksite selle lubama, sest see on ainus võimalus taastada oma tavalised Lightning-kanalid, kui te eemaldate ja installeerite Valet'i uuesti. Selgitame seda hiljem. Nii et klõpsake sellel ja andke Valetile luba oma **meediasalvestusele**, sest sinna salvestatakse varukoopiafail.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**KOOLISTE VARUTAMINE:** Niikaua kui olete andnud Valetile loa oma salvestusruumi kasutamiseks, määratakse see väli automaatselt kohalike varukoopiate salvestamiseks teie **Downloadid** kausta. Kuid te saate seda muuta, klõpsates siin ja valides mis tahes enda valitud kausta.


**HALDAMINE KETTAKIRI** See on natuke tehniline ja te ei pea sellega vaeva nägema, kui te ei ole piisavalt kogenud. Siin on vaikimisi seadistus lihtsalt hea.


**ADD HARDWARE WALLET:** Te ei peaks ka selle pärast vaeva nägema, kui teil ei ole riistvara wallet, mida soovite ühendada ja jälgida. Selle seadistusega saate skaneerida ja ühendada oma riistvara wallet, näiteks Trezori või Cold kaardi, ning jälgida selle tegevust. See on ainult jälgimisfunktsioon, mis tähendab, et te ei saa siit teha tehinguid riistvara wallet-ga. Te saate ainult jälgida ja jälgida wallet tegevust, saldot jne.


**SET CUSTOM ELECTRUM NODE:** See on samuti tehniline ja kui te ei ole piisavalt teadlik, ei peaks te sellega vaeva nägema. Vaikimisi seade on piisavalt hea.


**BITCOIN UNITS:** See on see, kuidas soovite, et teie Bitcoin saldo kuvatakse. Esimene valik näitab teie saldot Satoshi ühikutes, nt 1,000,000 Sats, teine valik näitab seda BTC kümnendkohtades, nt 0.01BTC


**KASUTA PIN-AUTENTIKATSIOON** Kui te märgistate selle kasti, siis peate seadistama PIN-koodi või sõrmejälje, mille peate sisestama oma wallet-sse sisselogimiseks ja tehingute autentimiseks.


**KASUTA TOR ÜHENDUST:** Kui märgistate selle kasti, suunatakse teie tehingud Tor-võrgu kaudu. See lisab täiendavat privaatsust, kuid võib põhjustada viivitusi maksete läbilaskevõimes, eriti välkmaksete puhul.


**VIEW BIP39 RECOVERY PHRASE:** Siin saate juurdepääsu oma 12-sõnalisele seed fraasile varundamiseks. Seega kui te ei ole seda varem üles kirjutanud või te ei leia, kuhu te selle üles kirjutasite, siis kui teil on endiselt juurdepääs oma Wallet-le, saate selle siit kopeerida.


**KASUTAMISTATISTIKA:** See näitab teile kokkuvõtet kõigist teie tehingutest ja tegevustest alates wallet loomisest


![usage_stats](assets/en/041.webp)


## Wallet taastamine


Valet on wallet mittekasutatav, seega kui kaotate oma seadme või eemaldate wallet rakenduse, peate wallet taastamise tegema, et saada tagasi oma Bitcoin ja Lightning-kanalid. Selle õpetuse alguses mainisime, kui oluline on kirjutada üles oma **12-sõnaline seed lause**, sest see on wallet taastamise võti. Klienditeenindajad ei saa teid aidata oma wallet tagasi saada.


Valet wallet taastamiseks on vaja kahte olulist tööriista, sõltuvalt sellest, kas teil oli aktiivne Lightning-kanal või mitte. Kasutajale, kellel ei olnud aktiivset tavalist Lightning-kanalit, on vaja vaid oma **12-sõnalist seed fraasi**, järgides alljärgnevaid lihtsaid samme:


👉 Paigaldage uus Valet rakendus ja käivitage/käivitage rakendus.


👉 Valige **Vaimaldage olemasolev Wallet**


![restore_existing_wallet](assets/en/042.webp)


👉 Valige **Välistuslause ainult**.


![select_recovery_phrase](assets/en/043.webp)


👉 Sisestage oma 12-sõnaline taastumisfraas ja klõpsake **OK**.


![input_12_words](assets/en/044.webp)


Teie wallet taastatakse. Sellisel juhul taastatakse ainult teie on-chain Bitcoin saldo.


Kui teil oli aga aktiivne tavaline välgukanal ja te taastate oma wallet ainult taastamise fraasiga, suletakse teie välgukanal sunniviisiliselt ja kõik Bitcoin saldod saadetakse automaatselt teie on-chain saldole.


Teine võimalus taastada oma Valet wallet, eriti kui teil oli enne Valeti desinstalleerimist avatud tavaline Lightning-kanal, on **kasutada seadmesse salvestatud kohalikku varukoopiafaili koos oma 12-sõnalise seed fraasiga**. Kui te kasutate neid kahte, taastatakse teie Lightning-kanali olek, seega ei suleta teie Lightning-kanalit sunniviisiliselt.


Siin on sammud:


👉 Paigaldage uus Valet rakendus ja käivitage/käivitage rakendus.


👉 Valige **Vaimalda olemasolev Wallet**.


👉 Valige **Backup + Recovery fraas**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Valige telefoni failihaldurist varundatud fail. (See on vaikimisi alati salvestatud teie **Downloadid** kausta)


![local_backup_file_in_download_folder](assets/en/046.webp)


Kui õige varukoopiafail on valitud, ilmub ekraanile kinnitus, et **"Varukoopiafail on olemas "**, ning seejärel palutakse teil sisestada 12-sõnaline seed fraas.


![enter_12_words](assets/en/047.webp)


👉 Sisestage oma 12-sõnaline taastamisfraas ja klõpsake **OK**. Teid suunatakse wallet kodulehele.


👉 Oodake, kuni Bitcoin võrgu sünkroniseerimine (**SYNC**) ja Lightning-sõlme sünkroniseerimine (**LN Sync**) on lõpule viidud, ja teie wallet on täielikult taastunud, sealhulgas teie Lightning-kanalid.


![LN_sync](assets/en/048.webp)


## Kokkuvõte


Valet on põnev wallet lahendus, mille funktsioonid muudavad selle sobivaks uute kasutajate sisseelamiseks. Sellel on ka Fiat-kanal, mitte just uus tehnoloogia, mis tagab fiat-ettevõtete integreerimise Bitcoin standardiga.


Lae Valet alla juba täna ja proovi seda!!! 🧡