---
name: Blixt Wallet
description: Kuidas hakata kasutama võimsat LN sõlme oma mobiilis?
---
![cover](assets/cover.webp)


See juhend on pühendatud kõigile neile uutele kasutajatele, kes soovivad alustada Bitcoin Lightning Network (LN) kasutamist TASUTA AVATUD JUURDEGA, TÄIELIKULT MITTE KASUTAMATA.


Kasutades [Blixt Wallet](https://blixtwallet.com/), täielik LN sõlme oma mobiilis, kus iganes sa oled.


Kui te ei ole kunagi kasutanud Bitcoin Lightning Network, siis lugege enne alustamist [palun lugege seda lihtsat selgitusanaloogiat Lightning Network (LN) kohta](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## OLULISED ASPEKTID:



- Blixt on privaatsõlm, mitte marsruutimise sõlmpunkt! Pidage seda meeles : See tähendab, et kõik Blixtis olevad LN kanalid on LN graafi jaoks ette teatamata (nn privaatsed kanalid). See tähendab, et see sõlme ei tee teiste maksete marsruutimist läbi Blixt'i sõlme. See Blixt-sõlm EI ole marsruutimiseks, ma kordan. Peamiselt selleks, et saaksite hallata oma LN kanaleid ja teha oma LN makseid privaatselt, kui teil on vaja. See Blixt-sõlm peab olema online ja sünkroonitud AINULT ENNE, kui te kavatsete oma tehinguid teha. Seepärast näete üleval ikooni, mis näitab sünkroonimisstaatust. See võtab vaid mõne hetke, sõltuvalt sellest, kui kaua te seda offline'is hoiate.



- Blixt kasutab LND (aezeed) Wallet backendina, seega ärge proovige sinna importida teist tüüpi Bitcoin rahakotte. [Siin olete selgitanud Wallet Mnemonic seemnete tüüpe](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Ja siin on [ulatuslikum nimekiri kõikidest rahakoti tüüpidest](https://walletsrecovery.org/). Nii et kui teil oli varem LND sõlme, saate importida seed ja backup.kanaleid Blixt'i, [nagu selles juhendis on selgitatud](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Käesoleva juhendi lõpus on eraldi osa ["näpunäiteid ja nippe"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt olulised lingid - vt neid käesoleva juhendi lõpus, palun lisage need järjehoidjasse.


---

## Blixt - Esimene kontakt


Niisiis... Darthi ema otsustas hakata LN koos Blixtiga kasutama. Hard otsus, aga tark. Blixt on ainult tarkadele inimestele ja neile, kes tõesti tahavad rohkem õppida, sügavuti kasutada LN.


![blixt](assets/en/01.webp)


Darth hoiatab oma ema:


"*Mom, kui hakkate kasutama Blixt LN Node'i, peate kõigepealt teadma, mis on Lightning Network ja kuidas see töötab, vähemalt baastasemel. [Siin panin kokku lihtsa loetelu allikatest Lightning Network kohta](https://blixtwallet.github.io/faq#what-is-LN). Palun lugege neid kõigepealt läbi.*"


Darthi ema luges ressursse ja tegi esimese sammu: paigaldas Blixt'i oma uhiuusse Android-seadmesse. Blixt on saadaval ka iOS-i ja macOS-i (töölauaarvuti) jaoks. Aga need ei ole Darth's Mom jaoks... Sellest hoolimata on soovitatav kasutada uuemat Androidi versiooni, vähemalt 9 või 10 parema ühilduvuse ja kogemuse saamiseks. Täieliku LN sõlme käivitamine mobiilseadmes ei ole lihtne ülesanne ja võib võtta veidi ruumi (min 600MB) ja mälu.


Kui avate Blixt'i, saate "Tere tulemast" ekraanil mõned valikud:


![blixt](assets/en/02.webp)


Paremas ülemises nurgas näete 3 punkti, mis aktiveerivad menüü:



- "enable Tor" - kasutaja saab alustada Tori võrguga, eriti kui ta soovib taastada vana LND sõlme, mis töötas ainult Toriga.
- "Set Bitcoin node" - kui kasutaja soovib ühendada oma sõlme otse, et sünkroonida plokid läbi Neutrino, saab seda teha kohe tervitusekraanilt. See valik on hea ka juhul, kui teie internetiühendus või Tor ei ole vaikimisi Bitcoin sõlme (node.blixtwallet.com) ühendamiseks nii stabiilne.
- Varsti lisatakse keel sinna, nii et kasutaja saab alustada otse keeles, mis on mugav. Kui soovite aidata kaasa sellele avatud lähtekoodiga projektile tõlgetega teistesse keeltesse, [palun liituge siin](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### VARIANT A - Uue Wallet loomine


Kui valite "luua uus Wallet", suunatakse teid otse Blixt Wallet põhiekraanile.


See on teie "kokpit" ja ka "Main LN Wallet", nii et olge teadlik, see näitab teile ainult teie LN Wallet tasakaalu. Onchain Wallet kuvatakse eraldi (vt C).


![blixt](assets/en/03.webp)


A - Blixt blokeerib sünkroonimisindikaatori ikooni. See on LN sõlme jaoks kõige tähtsam: olla sünkroonitud võrguga. Kui see ikoon on veel seal töötav, tähendab, et teie sõlme EI OLE VALMIS! Nii et olge kannatlik, eriti esimese esialgse sünkroniseerimise puhul. See võib võtta kuni 6-8 minutit, sõltuvalt teie seadmest ja internetiühendusest.


Saate sellele klõpsata ja näha sünkroonimise staatust:


![blixt](assets/en/04.webp)


Samuti võite klõpsata nupule "Näita LND logi" (A), kui soovite näha ja lugeda LND logi tehnilisi üksikasju reaalajas. See on väga kasulik vigade kõrvaldamiseks ja LN tööpõhimõtete tundmaõppimiseks.


B - Siin saate juurdepääsu kõigile Blixt seaded, ja on palju! Blixt pakub palju rikkalikke funktsioone ja võimalusi, et hallata oma LN sõlme nagu profi. Kõik need valikud on üksikasjalikult selgitatud "[Blixt Features Page] (https://blixtwallet.github.io/features#blixt-options) - Options Menu".


C - Siin on menüü "Magic Drawer", [siin on ka üksikasjalik selgitus](https://blixtwallet.github.io/features#blixt-drawer). Siin on "Onchain Wallet" (B), Lightning Channels (C), Contacts, Channels status icon (A), Keysend (D).


![blixt](assets/en/05.webp)


D - on abimenüü, kus on lingid KKK/juhendite lehele, kontakteeruge arendajaga, Githubi lehele ja Telegrami tugirühmale.


E - märkige oma esimene BTC Address, kuhu saate oma esimese testimise Sats hoiustada. SEE ON VABATAHTLIK! Kui te hoiustate otse, et Address, avab LN kanali suunas Blixt Node. See tähendab, et näete oma hoiustatud Sats, läheb teise onchain tehing (tx), avamiseks, et LN kanal. Saate kontrollida, et Blixt onchain Wallet (vt punkt C), klõpsates üleval paremal TX menüüs.


![blixt](assets/en/06.webp)


Nagu näete Onchaini tehingute logis, on sammud väga üksikasjalikud, näidates, kuhu Sats läheb (hoiustamine, avatud, suletud kanal).


SOOVITUS:


Pärast mitmete olukordade katsetamist jõudsime järeldusele, et palju tõhusam on avada kanalid vahemikus 1 ja 5 M Sats. Väiksemad kanalid kipuvad kiiresti ammenduma ja maksavad suuremate kanalitega võrreldes suuremaid tasusid.


F - märkige oma peamine Lightning Wallet saldo. See EI ole teie kogu Blixt Wallet saldo, see kujutab endast ainult Sats, mis on teil Lightning kanalites, mis on saadaval saatmiseks. Nagu eespool märgitud, on Onchain Wallet eraldi. Pidage seda aspekti meeles. Onchain Wallet on eraldi olulisel põhjusel: seda kasutatakse peamiselt LN kanalite avamiseks/sulgemiseks.


Okei, nüüd on Darth's Mom paigutanud Sats sellesse Address-i, mis kuvatakse põhiekraanil. Seda tehes on soovitatav hoida oma Blixt rakendust mõnda aega online ja aktiivsena, kuni BTC tx võetakse kaevurite poolt esimesse plokki.


Pärast seda võib kuluda kuni 20-30 minutit, kuni see on täielikult kinnitatud ja kanal on avatud ning te näete seda Magic Drawer - Lightning Channels'is aktiivsena. Ka väike värviline punkt sahtli peal, kui see on Green, näitab, et teie LN kanal on võrgus ja valmis Sats saatmiseks LN kaudu.


Address ja kuvatav tervitussõnum kaovad. Nüüd ei ole enam vaja automaatset kanalit avada. Samuti saate selle valiku seadete menüüs deaktiveerida.


On aeg edasi liikuda, katsetada teisi funktsioone ja võimalusi LN kanalite avamiseks.


Nüüd avame teise kanali teise sõlme peeriga. Blixt community put togheter [nimekiri headest sõlmedest, mida Blixtiga kasutama hakata](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Protseduur LN kanali avamiseks Blixtis**


See on väga lihtne, selleks on vaja vaid mõningaid samme ja veidi kannatust:



- Sai [Blixt Community](https://github.com/hsjoberg/blixt-Wallet/issues/1033) kolleegide nimekirja
- Valige sõlme ja klõpsake selle nime pealkirja lingil, see avab selle Amboss'i lehe
- Klõpsake, et kuvada QR-koodi sõlme URI Address jaoks


![blixt](assets/en/07.webp)


Avage Blixt ja minge ülemisse sahtlisse - Lightning Channels ja vajutage nupule "+"


![blixt](assets/en/08.webp)


Nüüd klõpsake (A) kaamerale, et skaneerida QR-koodi Amboss'i lehelt ja sõlme andmed täidetakse. Lisage soovitud kanali Sats summa ja seejärel valige tx-tasu määr. Kiirema kinnituse saamiseks võite jätta selle automaatseks (B) või reguleerida seda käsitsi nuppu libistades. Te võite ka pikalt vajutada numbrit ja muuta seda nii, nagu soovite.


Ära pane vähem kui 1 sat/vbyte ! Tavaliselt on parem enne kanali avamist konsulteerida [Mempool tasud](https://Mempool.space/) ja valida sobiv tasu.


Valmis, nüüd klõpsa lihtsalt nupule "ava kanal" ja oota 3 kinnitust, mis tavaliselt võtab 30 min (1 plokk aprox iga 10min).


Kui see on kinnitatud, näete kanalit aktiivsena oma jaotises "Välgukanalid".


---

## Blixt - Teine kontakt


Okei, nüüd on meil LN kanal ainult OUTBOUND likviidsusega. See tähendab, et me saame ainult SAADA, me ei saa ikka veel Sats üle LN vastu võtta.


![blixt](assets/en/09.webp)


Miks? Kas sa lugesid alguses märgitud juhendeid? Ei? Mine tagasi ja loe neid. On väga oluline mõista, kuidas LN kanalid töötavad.


![blixt](assets/en/10.webp)


Nagu näete selles näites, ei ole esimese deposiidiga avatud kanalil liiga palju INBOUND likviidsust ("Võib saada"), kuid on palju OUTBOUND likviidsust ("Võib saata").


Millised on teie võimalused, kui soovite saada rohkem Sats kui LN?



- Kulutada mõned Sats olemasolevast kanalist. Jah, LN on Bitcoin maksevõrk, mida kasutatakse peamiselt selleks, et kulutada oma Sats kiiremini, odavamalt, privaatselt ja lihtsalt. LN ei ole hodling viis, selleks on teil onchain Wallet.



- Vahetage mõned Sats, tagasi oma ahelasse Wallet, kasutades allveelaeva vahetusteenust. Sel viisil te ei kuluta oma Sats, vaid annate selle tagasi oma Wallet-ile. Siin näete üksikasjalikult mõningaid meetodeid, [Blixt Guides Page](https://blixtwallet.github.io/guides).



- Avage INBOUND-kanal mis tahes LSP-teenuse pakkujalt. Siin on videodemonstratsioon selle kohta, kuidas kasutada LNBig LSP-d sissetuleva kanali avamiseks. See tähendab, et te maksate väikese tasu tühja kanali eest (teie poolt) ja saate sellesse kanalisse rohkem Sats. Kui olete kaupmees, kes saab rohkem kui kulutada, on see hea võimalus. Ka siis, kui te ostate Sats üle LN, kasutades Robosatsi või mõnda muud LN Exchange.



- Avage Dunderi kanal Blixt'i sõlme või mõne muu Dunderi LSP teenusepakkuja abil. Dunderi kanal on lihtne viis saada INBOUNDi likviidsust, kuid samal ajal hoiustate sellesse kanalisse ka Sats. On ka hea, sest see avab kanali [UTXO](https://en.Bitcoin.it/wiki/UTXO), mis ei ole teie Blixt Wallet. See lisab mõningast privaatsust. On ka hea, sest kui teil ei ole Sats onchain Wallet, et avada tavaline LN kanal, kuid teil on neid teise LN Wallet, saate lihtsalt maksta, et teine Wallet läbi LN avamine ja hoiustamine (teie poolt), et Dunder kanal. [Täpsemalt, kuidas Dunder töötab ja kuidas oma serverit juhtida siin](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Siin on Dunderi kanali avamise aktiveerimise sammud:



- Mine seadistustesse, aktiveeri jaotises "Eksperimendid" ruut "Dunder LSP lubamine".
- Kui olete seda teinud, minge tagasi jaotisse "Lightning Network" ja näete, et ilmus valik "Set Dunder LSP Server". Seal on vaikimisi määratud "https://dunder.blixtwallet.com", kuid te saate seda muuta mis tahes muu Dunder LSP teenusepakkuja Address abil. [Siin on Blixt community list](https://github.com/hsjoberg/blixt-Wallet/issues/1033) sõlmedega, mis võivad pakkuda Dudner LSP kanaleid teie Blixt'ile.
- Nüüd saate minna põhiekraanile ja klõpsata nupule "Receive". Seejärel järgige seda protseduuri [käesolevas juhendis selgitatud](https://blixtwallet.github.io/guides#guide-lsp).


OK, nii et pärast Dunderi kanali kinnitamist (võtab paar minutit) on teil lõpuks 2 LN kanalit: üks on algselt avatud autopiloodiga (kanal A) ja teine on avatud Dunderiga (kanal B), millel on rohkem sissetulevat likviidsust.


![blixt](assets/en/12.webp)


Hea, nüüd on teil hea minna, et saata ja vastu võtta piisavalt Sats üle LN !


ÕNNE Bitcoin VÄLK!


---

## Blixt - Kolmas kontakt


Pea meeles, et esimeses peatükis "Esimene kontakt" oli tervitusekraanil 2 valikut:


- [Valik A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Uue Wallet loomine
- Valik B - Wallet taastamine


Arutleme nüüd selle üle, kuidas taastada Blixt Wallet või mõni muu kokku kukkunud LND sõlme. See on veidi tehnilisem, kuid palun pöörake tähelepanu. Ei ole see Hard.


### VARIANT B - Wallet taastamine


Varem kirjutasin spetsiaalse juhendi [kuidas taastada kokkuvarisenud Umbrel-sõlme](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), kus ma mainisin ka meetodit, kuidas kasutada Blixt'i kiiret taastamisprotsessi, kasutades seed + channel.backup faili Umbrelist.


Kirjutasin ka juhendi, kuidas taastada oma Blixt-sõlme või migreerida oma Blixt teise seadmesse, [siin](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Kuid selgitame seda protsessi lihtsate sammudega. Nagu näete ülaltoodud pildil, on 2 asja, mida peaksite tegema, et taastada oma eelmine Blixt/LND sõlme:



- ülemine kast on see, kus sa pead täitma kõik 24 sõna oma seed-st (vana/surnud sõlme)
- all on kaks nupuvarianti, et sisestada/laadida kanali.backup-faili, mis on eelnevalt salvestatud teie vanast Blixt/LND sõlmest. See võib olla kohalikust failist (te laadite selle eelnevalt oma seadmesse üles) või võib olla Google drive / iCloudi kaugkasutatavast asukohast. Blixtil on see võimalus salvestada oma kanalite varukoopia otse Google'i / iCloudi kettale. Vaata lähemalt [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).


Siiski tuleb mainida, et kui teil ei olnud varem ühtegi avatud LN kanalit, ei ole vaja laadida üles ühtegi channels.backup faili. Lihtsalt sisestage 24 sõna seed ja vajutage taastamise nuppu.


Ärge unustage aktiveerida Tor, ülalt 3 punkti menüüst, nagu me selgitasime punktis A. See on siis, kui teil oli AINULT Tor peers ja te ei saanud ühendust üle clearneti (domeen/IP). Muidu ei ole vaja.


Teine kasulik funktsioon on määrata konkreetne Bitcoin sõlme sellest ülemisest menüüst. Vaikimisi sünkroonib see blokke node.blixtwallet.com (neutriinorežiim), kuid te võite määrata mis tahes muu Bitcoin sõlme, mis pakub neutriinosünkroonimist.


Nii et kui olete need valikud täitnud ja vajutanud taastamisnuppu, hakkab Blixt kõigepealt plokke Neutrino kaudu sünkroonima, nagu me selgitati peatükis "Esimene kontakt". Nii et olge kannatlik ja jälgige taastamisprotsessi põhiekraanil, klõpsates sünkroonimise ikoonil.


![blixt](assets/en/14.webp)


Nagu näete, näitab see, et Bitcoin plokid on 100% sünkroonitud (A) ja taastamisprotsess on käimas (B). See tähendab, et LN kanalid, mis teil varem olid, suletakse ja vahendid taastatakse teie Blixt onchain Wallet.


See protsess võtab aega! Seega palun olge kannatlik ja püüdke oma Blixt aktiivne ja online hoida. Esialgne sünkroonimine võib võtta kuni 6-8 minutit ja kanalite sulgemine kuni 10-15 minutit. Seega on parem, kui seade on hästi laetud.


Kui see protsess on alanud, saate kontrollida Magic Drawer - Lightning Channels, staatuse iga teie eelmise kanaleid,näitab, et on "ootel sulgeda" staatuses. Kui iga kanal on suletud, võite näha sulgemise tx onchain Wallet (vt Magic Drawer - Onchain), ja avada tx menüü logi.


![blixt](assets/en/15.webp)


Samuti on hea kontrollida ja lisada, kui ei ole olemas, oma varem oma vanas LN sõlmes olnud eakaaslased. Nii et minge menüüsse Settings, alla "Lightning Network" ja sisestage valik "Show Lightning Peers".


![blixt](assets/en/16.webp)


Selle sektsiooni sees näete, millised eakaaslased on teil sel hetkel ühendatud ja võite lisada veel, parem on lisada need, mis teil olid varem kanalid. Lihtsalt minge [Amboss page](https://amboss.space/), otsige oma eakaaslaste sõlmede aliase või nodeID ja skaneerige nende sõlme URI.


![blixt](assets/en/17.webp)


Nagu näete ülaltoodud pildil, on 3 aspekti:


A - esindab clearnet-sõlme Address URI (domeen/IP)


B - esindab Tor sibulasõlme Address URI (.onion)


C - on QR-kood, mida saate skannida oma Blixt-kaameraga või kopeerimisnupuga.


See sõlme Address URI peate lisama selle oma eakaaslaste nimekirja. Nii et olge teadlik ei piisa ainult sõlme aliasnimi või nodeID.


Nüüd saate minna Magic Drawer (ülemine vasakpoolne menüü) - Lightning Channels, ja näete, millise tähtajaga ploki kõrgusel raha tagastatakse teie onchain Address.


![blixt](assets/en/18.webp)


See plokk number 764272 on siis, kui vahendid on kasutatavad teie Bitcoin onchain Address. Ja see võib võtta kuni 144 plokki alates 1. kinnituse plokist kuni vabastatakse. [Nii et kontrollige, et Mempool] (https://Mempool.space/).


Ja see ongi kõik. Lihtsalt oodake kannatlikult, kuni kõik kanalid on suletud ja vahendid tagasi teie onchain Wallet-sse.


👉 **Salajane taastamismeetod :**


Blixt LND-sõlme taastamiseks on veel üks meetod, mille puhul ei pea isegi kanaleid sulgema. Aga on peidetud tavaliste noob-kasutajate eest, sest see meetod on AINULT neile, kes teavad, mida nad teevad.


Kui teil on vaja olemasolevat (töötavat) Blixt-sõlme teise uude seadmesse üle viia, ilma olemasolevaid LN kanaleid sulgemata, peate tegema järgmised toimingud:



- Oletame, et olete juba salvestanud Blixt Wallet seed (24 sõna aezeed)
- Mine vanas seadmes jaotisse "Settings" (Seaded) - jaotis "Debug - Compact LND database" (Kompaktne LND andmebaas). See samm on valikuline, kuid soovitatav, kui soovite väiksema suurusega faili channel.db. Tavaliselt on üsna suur, sõltuvalt teie sõlme aktiivsusest. See käivitab Blixt uuesti ja tihendab db-faili suurust.
- Pärast taaskäivitamist mine "Settings" (Seaded) ja muuda oma tavaline aliasnimi "Hampus" (Hampus). See aktiveerib varjatud valikud, mis on mõeldud ainult edasijõudnud kasutajatele.
- Minge alla "Debug" sektsiooni ja näete uut võimalust "Export channel.db faili". HOIATUS! Kui te seda eksporti teostate, lülitatakse olemasolev Blixt LN-sõlm selles vanas seadmes välja ja eksporditakse kogu sõlme andmebaas (channel.db), mis on valmis uude seadmesse importimiseks.
- See db-fail salvestatakse teie vanas seadmes määratud kausta (dokumendid või allalaadimised) ja sealt peate selle sellisena uude seadmesse üle viima. Te võite kasutada näiteks [LocalSend FOSS app](https://github.com/localsend/localsend), et faili otse seadmete vahel üle kanda.
- Sel hetkel peab teie vana Blixt jääma kinni. ÄRGE AVAGE SEDA UUESTI!
- Kui olete kanali.db faili uude seadmesse üle kandnud, käivitage Blixt'i uus paigaldus ja valige esimesel ekraanil "Restore Wallet".
- Nupule, kus on kirjas "Select SCB file", vajutage pikalt (MITTE lihtne klõps!) ja siis näete võimalust valida channel.db faili, kuhu salvestate selle lokaalselt uues seadmes. Kui te lihtsalt lihtsalt vajutate seda nuppu, siis kasutab see vaikimisi SCB-faili (koos sulgevate kanalitega), see ei tööta täieliku varukoopia live-kanalite puhul.
- Pange 24 sõna seed ja seejärel klõpsake "Restore"
- Te näete, et Blixt hakkab Neutrinoga sünkroonima. Saate vaadata ka sünkroonimisprotokolle.
- HOIDKE MEELES! Püüa hoida Blixt selles faasis kogu aeg avatud! Ärge laske tal magama minna ega sulgege rakenduse ekraani. See võib esialgset sünkroonimist häirida ja te peate seda uuesti tegema. Oodake kannatlikult, ei võta rohkem kui paar minutit.
- Kui esialgsed plokid on sünkroonitud, skaneerib see kiiresti teie varasemad Wallet-aadressid ja seejärel on teie kanalid taas võrgus, elus ja terved.
- Kahjuks ei ole (veel) võimalik taastada varasemat maksete ajalugu ja kontakte. Aga see ei ole niikuinii nii oluline.


Ja TÄHELEPANU! Nüüd on teil täielikult taastatud Blixt LN sõlme. See võib töötada ka teiste LND varukoopiate (Umbrel, Raspiblitz jne) puhul, kui olete eelnevalt õigesti salvestanud channel.db faili. Nii et Blixt saab sõna otseses mõttes päästa iga LND surnud sõlme.


---

## Blixt - Neljas kontakt


See peatükk käsitleb kohandamist ja Blixt Node'i parem tundmaõppimist. Ma ei hakka kirjeldama kõiki olemasolevaid funktsioone, neid on liiga palju ja neid on juba selgitatud [Blixt Features Page](https://blixtwallet.github.io/features).


Kuid ma toon välja mõned neist, mis on vajalikud, et jätkata oma Blixt'i kasutamist ja saada suurepäraseid kogemusi.


### A - Nimi (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) on standard "vastuvõtja nime" edastamiseks BOLT11 arvetes.


See võib olla ükskõik milline nimi ja seda võib igal ajal muuta.


See valik on väga kasulik erinevatel juhtudel, kui soovite saata nime koos Invoice kirjeldusega, et vastuvõtja saaks vihje, kes on need Sats saanud. See on täiesti vabatahtlik ja ka makseekraanil peab kasutaja märgistama kasti, mis näitab, et ta soovib saata varjunime.


Siin on näide, kuidas ilmub, kui kasutate [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


See on veel üks näide, mis saadetakse teisele Wallet rakendusele, mis toetab NameDesc:


![blixt](assets/en/21.webp)


### B - välgukast


Alates uuest versioonist v0.6.9-420 [hiljuti välja kuulutatud](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420) võttis Blixt kasutusele uue võimsa funktsiooni Lightning Address jaoks Blixtis.


See uus funktsioon on valikuline opt-in, ei ole vaikimisi sisse lülitatud!


Hetkel on vaikimisi LN Box töötab Blixt server ja pakkuda @blixtwallet.com LN Address. Aga KÕIK, kellel on LND avalik sõlme võib käivitada Lightning Box server ja pakkuda LN Address oma domeeni, ise haldamine.


Praegu edastab Blixt server ainult LN aadressidele @blixtwallet.com saadetud maksed Blixt kasutajatele, kes on seadistanud oma LN Address. Kasutajad peavad seadma oma Blixt-sõlme Wallet "püsivasse režiimi", et saada neid makseid oma @blixtwallet.com LN aadressidele.


Vaata versioonimärkustes videodemot sellest, kuidas seadistada LN Address Blixtis.


See LN Address rakendatud Blixt Wallet app, on nagu chat üle LN, instant ja lõbus, toetab ka [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (lisades alias nimi makse). Saate lisada kontaktide nimekirja kõik oma tavalised LN aadressid, mida kasutate vabalt ja on see käepärast vestlemiseks. Nüüd võib Blixt'i pidada täielikuks LN vestlusrakenduseks 😂😂.


Teine kasulik funktsioon on täielik toetus LUD-18-le (mida toetavad ka [Stacker.News](https://stacker.news/r/DarthCoin) ja teised).


![blixt](assets/en/22.webp)


Nagu näete ülaltoodud ekraanipildil, mis on saadetud Stacker News'i kontolt, kuvatakse kenasti logo + LN Address + sõnum. Samamoodi toimib ka Blixtist saatmine, võite lisada oma Blixt LN Address või lihtsalt lisada aliasnime (eelnevalt Blixi seadetes määratud) või isegi mõlemad.


See LUD-18 võimalus võiks olla kasulik ka tellimusteenuste puhul, kus kasutaja saab saata konkreetse varjunime (see ei ole teie sõlme varjunimi ega teie tegelik nimi!) ja selle alusel saab teid registreerida või saada tagasi konkreetse sõnumi või mis iganes muu. Pseudonime ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ kommentaari ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) lisamine LN maksele võib olla mitmeotstarbeline!


Siin on [Lightning Box](https://github.com/hsjoberg/lightning-box) kood, kui te käivitate seda enda, oma pere ja sõprade jaoks, oma noodis.


Siin saab ka käivitada [LSP Dunder server](https://github.com/hsjoberg/dunder-lsp) Blixt mobiilse sõlme jaoks ja pakkuda likviidsust Blixt kasutajatele, kui teil on hea avalik LN sõlme (töötab ainult LND).


### C - LN kanalite ja seed sõnade varukoopia


See on väga oluline omadus !


Pärast LN kanali avamist või sulgemist peaksite tegema varukoopia. Seda saab teha käsitsi, salvestades väikese faili kohalikku seadmesse (tavaliselt allalaadimiskausta) või kasutades Google Drive'i või iCloudi kontot.


![blixt](assets/en/23.webp)


Mine Blixt Settings - Wallet sektsiooni. Seal on teil võimalus salvestada kõik olulised andmed oma Blixt Wallet jaoks:



- "Näita Mnemonic" - kuvab 24 sõna seed, et need üles kirjutada
- "Remove Mnemonic from device" - see on valikuline ja kasutage seda ainult siis, kui soovite tõesti seed sõnu seadmest eemaldada. See EI kustuta teie Wallet, vaid ainult seed. Kuid olge teadlik ! Neid ei ole võimalik taastada, kui te ei ole neid kõigepealt üles kirjutanud.
- "Ekspordi kanali varukoopia" - see valik salvestab väikese faili teie kohalikku seadmesse, tavaliselt "allalaadimiste" kausta, kust saate selle võtta ja turvaliseks säilitamiseks seadmest väljapoole viia.
- "Verify channel backup" - see on hea valik, kui kasutate Google drive'i või iCloudi, et kontrollida eemalt tehtud varukoopia terviklikkust.
- " Google drive'i kanali varukoopia" - salvestab varukoopiafaili teie isiklikku Google'i draivi. Fail on krüpteeritud ja salvestatakse eraldi hoidlasse kui teie tavalised Google'i failid. Seega ei ole muret, et keegi saab lugeda. Igatahes see fail on täiesti kasutu ilma seed sõnad, nii et keegi ei saa võtta oma raha ainult sellest failist.


Soovitan selle jaotise jaoks järgmist:



- kasutage paroolihaldurit, et hoida turvaliselt oma seed ja varundust faili. KeePass või Bitwarden on selleks väga head ja neid saab kasutada multiplatvormil ja ise hostitud või offline.
- TEHA TAGASIVÕTMIST iga kord, kui avate või sulgete kanali. Seda faili uuendatakse kanalite infoga. Seda ei ole vaja teha pärast iga tehingut, mille olete LN-s teinud. Kanali varukoopia ei salvesta seda infot, vaid ainult kanali olekut.


![blixt](assets/en/24.webp)


---

## Blixt - näpunäited ja nipid


### JUHTUM 1 - SÜNKROONIMISPROBLEEMID


"_My Blixt ei sünkroniseeru... Minu Blixt ei näita tasakaalu... Minu Blixt ei saa avada kanaleid... Ma proovisin seda taastada teises seadmes... jne_"


Kõik need probleemid saavad alguse sellest, et teie seade ei sünkroniseeru korralikult. Palun mõistke seda olulist aspekti: Blixt on mobiilne LND sõlme, mis kasutab Neutrinot plokkide sünkroonimiseks / lugemiseks.



- Siin on vähem tehniline selgitus [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Siin on rohkem tehnilisi ressursse [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Siin on, kuidas saab aktiveerida Neutrino oma kodusõlme ja teenida blokifiltreid oma mobiilse sõlme jaoks, [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


MEELDE: Neutrino kasutamine üle clearneti on täiesti turvaline, teie IP või xpub ei leki. Te lihtsalt loete neutrino abil plokke eemal asuvast sõlmpunktist. See on kõik. Kõik muu toimub teie kohalikus seadmes.


Nii et seda ei ole vaja kasutada koos Toriga. Tor lisab teie sünkroonimisprotsessile tohutu viivituse ja muudab teie Blixt väga ebastabiilseks. Kui sa tõesti tahad kasutada üle Tori, ole kindel, mida sa teed ja on hea ühendus ja kannatust. Sama kehtib ka VPN-i kasutamise kohta. Olge ettevaatlik, millist latentsust teile see VPN annab.


Te saate neutriinoserveri latentsust testida, lihtsalt pingerdades seda arvutist või mobiiltelefonist.


![blixt](assets/en/25.webp)


See on tavaline ping neutrino serverile europe.blixtwallet.com, see näitab, et ühendus on väga hea, vastamisaeg on keskmiselt 50ms ja TTL 51. Vastusaeg võib varieeruda, kuid mitte liiga palju. TTL peab olema stabiilne.


Kui need väärtused on suuremad kui 100-150ms, siis teie sünkroonimisprotsess jääb seisma või veel hullem, see võib põhjustada suletud kanaleid peeride poolt ! Ärge ignoreerige seda aspekti.


Ilma korraliku sünkroonimiseta ei näe ka õiget tasakaalu või ei saa teie LN kanalid online ja töökorras olla. Ükskõik kui palju giga ultra terra mbps teil on allalaadimiskiirus IT DOESN'T MATTER. Oluline on ajaline reageerimine ja TTL (time to live).


See on nagu üldine juhtum LATAMi kasutajate jaoks. Ma ei tea, mis seal toimub, kuid teil on kohutav ühendus, mille pings on üle 200 ms, mis võib häirida mis tahes sünkroonimist.


Milline on siis lahendus nende meeleheitel olevate kasutajate jaoks?



- lõpetada Blixt'i kasutamine koos Toriga. On täiesti kasutu
- võite kasutada VPN-i, kuid valige see targalt ja jälgige kogu aeg pingi. Kasutage sellist, mis on teie geograafilisele asukohale lähemal. Kaugus tähendab rohkem ms reageerimisaega, pidage meeles.
- valige targalt oma neutrino-partnerid, siin on nimekiri tuntud avalikest neutrino-serveritest:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Teine võimalus on valida üks sellest loetelust sõlmede teatamise "kompaktsed filtrid" (BIP157 / neutriino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Valige üks, mis on teie geograafilisele asukohale lähemal.


Teine võimalus (parim viis) on luua ühendus kohaliku kogukonna sõlmpunktiga, mida juhib sõber või rühm, keda te tunnete ja mis pakub neutriinode ühendust. [Siin on juhised, kuidas seda teha.] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Nende sõlme ei mõjuta see kuidagi, nad vajavad lihtsalt stabiilset ja avalikku ühendust.


LATAMi piirkonnas on vaja rohkem neutriinoservereid, et tagada parem ja kiire sünkroniseerimine. Nii et palun organiseerige end, koos oma kohaliku Bitcoin kogukonnaga ja otsustage, kes ja kus töötab Bitcoin Core + Neutrino teie enda jaoks. Piisab vaid avalikust IP-st. Kui teil ei ole juurdepääsu avalikule IP-le, võite kasutada VPS-i IP-d ja teha wireguard-tunneli oma kodusõlme. Nii suunate kogu liikluse ümber oma kohalikule VPS-i IP-le, ilma et avaldaksite oma kodusõlme kohta mingit privaatset teavet.


### JUHTUM 2 - EI LÕPETA KUNAGI SÜNKROONIMIST


"_Minu Blixtil on neutrino serveriga hea ühendus, kuid sünkroonimine on takerdunud._"


#### Ajaserver


Mõnikord kasutavad inimesed erinevaid vanu seadmeid või ei ole korralikult ühendatud ajaserveriga. Neutrino sünkroonib ok, kuni jõuab tegelike plokkideni, mis ei vasta tegelikule kohalikule ajale. Te näete Blixt LND logides viga, mis ütleb, et "ploki ajatempel on kaugel tulevikust" või midagi, mis on seotud "päis ei läbinud sanity check'i".


Kiirparandus: seadke seadme õige kellaaeg ja kuupäev ning käivitage Blixt uuesti.


#### Seadmes on vähe ruumi


Mõnikord võib vana seadme kasutamine, millel on vähe ruumi, jõuda künnisele ja jääda kinni. Tõepoolest rohkem te kasutate seda mobiilset LND sõlme, neutrinofailid muutuvad suuremaks ja ka channel.db fail.


Kiire lahendus: Valige "peata LND ja kustuta neutriinofailid". See käivitab rakenduse uuesti ja alustab uut värsket sünkroonimist. Mõnikord võib see kiirkorrigeerimine parandada ka rikutud andmeid. Pidage meeles, et võtab aega, 1 kuni 3 minutit, et täielikult uuesti sünkroonida. See EI kustuta olemasolevaid vahendeid ega kanaleid, kuid jah, pärast resünkroniseerimist võib see käivitada teie Bitcoin aadresside uuesti skaneerimise ja see võib võtta rohkem aega.


Järgmine samm on kontrollida, kui palju andmeid on veel hõivatud. Seda näete Androidi rakenduse info - andmed. Kui see on ikka veel suurem kui 400-500 MB, saate LND failid tihendada. Seega minge Blixt Options - Debug jaotis - valige "Compact DB LND". Käivitage Blixt rakendus uuesti, kui see ei toimu automaatselt. Tihendamine toimub käivitamisel ja ainult üks kord. Nüüd näete, et Blixt andmed on rohkem vähem hõivatud.


#### Püsiv režiim


Mõnikord inimesed ei ava Blixt pikka aega, nii et on liiga vana sünkroonimine. Aga nad ootavad, et nad sünkroniseeritakse kohe, kui nad selle avavad.


Palun olge kannatlik ja vaadake ülevalt pöörlevat ratast. Valikuliselt saate minna Options - See Node Info ja vaadata, kas on sünkroonitud ahelaga ja sünkroonitud graafikuga, mis on märgitud "true". Ilma selle "true" märkuseta ei saa te Blixt'i korralikult kasutada, te ei näe õigesti saldot, te ei näe LN kanaleid võrgus, te ei saa teha makseid.


Kiire lahendus: Blixt-sõlme "elus hoidmiseks" on võimas võimalus. Mine Options - Experiments - vali "Activate Persistent Mode". See käivitab teie Blixt'i uuesti ja paneb LND teenuse püsivasse režiimi, st on alati aktiivne ja hoiab teie sünkroonimise võrgus, isegi kui te vahetate teise rakenduse vastu või lihtsalt sulgete Blixt'i (mitte sunniviisiliselt sulgeda või tappa ülesannet). Võite hoida seda nii kogu päeva, kui teil on stabiilne ühendus ja teil on vaja Blixt'i mitu korda kasutada. See ei tarbi liiga palju akut.


### JUHTUM 3 - TAHAN MIGREERUDA TEISE SEADMESSE


OK selle stsenaariumi kohta kirjutasin põhjaliku juhendi [KKK leheküljel](https://blixtwallet.github.io/faq#blixt-restore): 2 võimalusega, kiire (kanalite koostöövõimekus enne migratsiooni) ja aeglane (sunniviisiline kanalite sulgemine, sest vana seade on surnud).


Kuid ma tahan siinkohal korrata mõningaid olulisi aspekte ja lisada uue "salajase" protseduuri.


MEELDE:



- Tehke alati varukoopia oma kanalite olekust (SCB) pärast iga kord, kui avate või sulgete kanali. Selleks kulub vaid mõni sekund.
- Ärge hoidke vanu SCB-faile, et mitte segadusse sattuda ja neid taastada. On täiesti kasutu ja võib vallandada trahviprotseduuri, kui te neid se. Kasutage alati SCB-faili viimast versiooni, kui jätkate taastamist.
- Salvestage SCB-faili (see on krüpteeritud tekst laiendiga .bin) seadmest välja, turvalisse kohta. Selle faili viimiseks arvutisse või muusse seadmesse saate kasutada funktsiooni [LocalSend](https://github.com/localsend/localsend).
- Salvestage ka oma Blixt seed Wallet turvalisse kohta, näiteks offline paroolihaldurisse / krüpteeritud USB-pulgale.


Salajane meetod: Kuidas migreerida Blixt sõlme ilma olemasolevaid kanaleid sulgemata. Selleks peate tähelepanelikult lugema eelmist lõiku "Kolmas kontakt" selles juhendis "Wallet taastamine".


See protseduur EI OLE NOOBSILE, see on ainult edasijõudnutele! Sellepärast ei ole laialt avatud ja ma soovitan seda teha ainult Blixt arendajate või minu toe abiga. Palun ärge ignoreerige seda nõuannet.


### JUHTUM 4 - MILLISEID EAKAASLASI KASUTADA KANALITE AVAMISEKS?


Nagu ma kirjutasin [Blixt guides leheküljel](https://blixtwallet.github.io/guides), on selle mobiilse LND sõlme abil mitmeid võimalusi kanalite avamiseks. Kuid mõned olulised aspektid tahaksin teile siinkohal meelde tuletada:



- avatud tuntud LSP-sõlmede ja kogukonna poolt garanteeritud eakaaslastega. [Vaata siit nimekirja](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- ei avane ainult juhuslikke Tor-sõlmi. Need on väärtusetud ja te saate ainult probleeme, et ei saa teha makseid. Ükskõik kui hea on teie sõber "node runner" shity Tor-sõlme džunglis, see ei anna teile kunagi parimaid marsruute mobiilse privaatsõlme. Sa ei ava kanaleid kellegagi, sest on sinu sõber. See ei ole Facebook! Sa avad kanali: head marsruudid, väikesed tasud, kättesaadavus.
- ei ole vaja avada kuradi palju väikseid kanaleid, 2-3 või maksimaalselt 4, kuid hea kogus Sats. Ärge avage väikseid kanaleid, on täiesti kasutud. Väiksemad kui 200k mobiilile ei ole palju kasu.
- pidage meeles LSPsid, mis pakuvad sissetulevaid kanaleid ja JIT-kanaleid (just in time). Need on väga kasulikud, sest te ei pea kasutama ühtegi oma UTXO-d, saate avada kanalit rahaliste vahenditega, mis teil juba on teistes LN rahakottides, kuhjates ja valmistades neid ette suurema kanali avamiseks. Te peaksite neid JIT-kanaleid enda kasuks kasutama. [Olen selgitanud selles juhendis] (https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) rohkem võimalusi eakaaslaste jaoks privaatsõlmede jaoks, nagu Blixt. Samuti [siin selles SN-i postitatud juhendis](https://stacker.news/items/679242/r/DarthCoin) selgitasin, kuidas hallata privaatsete mobiilsete sõlmede likviidsust.


---

## Kokkuvõte


OK, Blixt pakub veel palju muid hämmastavaid funktsioone, ma lasen teil neid ükshaaval avastada ja lõbutseda.


See rakendus on tõesti alahinnatud, peamiselt seetõttu, et seda ei toeta ükski riskikapitali rahastamine, see on kogukonnapõhine, ehitatud armastuse ja kirega Bitcoin ja Lightning Network vastu.


See mobiilne LN sõlme, Blixt on väga võimas vahend paljude kasutajate käes, kui nad oskavad seda hästi kasutada. Kujutage lihtsalt ette, et te kõnnite maailmas ringi LN-sõlmega oma taskus ja keegi ei tea seda.


Ja rääkimata kõigist muudest rikkalikest funktsioonidest, mida väga vähesed või ükski teine Wallet rakendus ei suuda pakkuda.


Vahepeal on siin kõik lingid selle hämmastava Bitcoin Lightning Node'i kohta:



- [Blixt Official Webpage](https://blixtwallet.com/)
- [Blixt Github leht](https://github.com/hsjoberg/blixt-Wallet/)
- [Blixt Features page](https://blixtwallet.github.io/features) - selgitatakse ükshaaval iga funktsiooni ja funktsionaalsust.
- [Blixt KKK lehekülg](https://blixtwallet.github.io/faq) - Blixt'i küsimuste ja vastuste loetelu ning tõrkeotsing
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demod, videoõpikud, lisajuhendid ja kasutusjuhendid Blixt'ile
- Allalaadimine: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK otselaadimine](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Telegrammi grupp otsetoetuseks](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Geyser ühisrahastuse lehekülg](https://geyser.fund/project/blixt) - annetage Sats, kui soovite projekti toetada
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonüümne LN chat
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - reklaamvideo (saate testida oma 1. LN kasutamist)
- [Prinditav A4 voldik esimeste sammude kohta Blixt'i kasutamisel, erinevates keeltes](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt pakub ka täisfunktsionaalset demo](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) otse oma veebilehel või spetsiaalses veebiversioonis, et saada täielik kogemus testimiseks, enne kui hakkate seda reaalses maailmas kasutama.


---
**DISCLAIMER:**


*Selle rakenduse arendajad ei maksa ega toeta mind mingil viisil. Kirjutasin selle juhendi, sest nägin, et huvi selle Wallet rakenduse vastu kasvab ja uued kasutajad ei saa ikka veel aru, kuidas sellega alustada. Ka selleks, et aidata Hampus (peamine arendaja) dokumentatsiooniga selle sõlme Wallet.* kasutamise kohta


*Mul ei ole mingit muud huvi selle LN rakenduse edendamiseks kui Bitcoin ja LN vastuvõtmise edendamine. See on ainus võimalus!*


---