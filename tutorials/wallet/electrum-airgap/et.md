---
name: Electrum Airgap
description: Esimene samm turvalisuse suunas, cold wallet Electrumiga
---
![cover](assets/cover.webp)



## Cold Wallet



Selles õpetuses selgitan, kuidas teha oma esimene õhulõhega allkirjastamise seade, mis on internetist lahti ühendatud, isegi ilma spetsiaalse Hardware Wallet-ga. Kõik, mida vajate, on kaks arvutit, mis on saadaval:




- vana seadme igaveseks takistada ühendamist internetti;
- teie igapäevaselt kasutatav arvuti.



See konfiguratsioon võimaldab suuremat turvalisust kui klassikaline "Hot Wallet": vana arvuti - ilma võrguühenduseta - on teie privaatvõtmete hoidja, mis ei ole kunagi Internetis avatud, vaid salvestatud võrguühenduseta ("airgap" või "Cold").



Selle asemel paigaldate Wallet ekraani ("watch-only") oma igapäevasesse arvutisse, mis on ühendatud võrku ja mille abil saate näiteks kontrollida saldosid ja koostada kviitungitehinguid.



## Wallet Airgap: Mis ja kuidas



Selles juhendis toodud samme tehes paigaldame kahte Software Wallet Electrumi kahte erinevasse arvutisse ja lõpuks loome kaks rahakotti erinevate võtmesalvestustega: Wallet airgap kasutab kogu Wallet HD hierarhiat, samas kui Wallet display luuakse avaliku peavõti abil.



Need kaks rahakotti on igas mõttes üksteisest väga erinevad. Ainus ühine asi, nagu me näeme, on aadressid:




- gW-13 airgap-arvutis saab ainult allkirjastada, kuid võrgust lahti ühendatud, ei tea kasutatavat saldot ja aadressi;
- gW-12 igapäevases arvutis saab privaatvõtmete puudumisel ainult tehinguid ette valmistada ja paljundada, ilma et ta suudaks kulutusi käsutada.



## Esialgne ettevalmistus



Electrumi allalaadimiseks soovitan järgida selle õpetuse esimesi samme:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Pärast allalaadimist kontrollige alati väljalase enne selle paigaldamist, seejärel jätkake "One Server" konfigureerimist, nagu te leiate abiosast "Start with a Dummy Wallet".



Konfiguratsioonitoiming "Üks server" on vajalik ainult Wallet puhul, mis on paigaldatud igapäevasesse arvutisse, kuna teine arvuti on alati võrguühenduseta.



Järgnevad toimingud hõlmavad harjutamist kahes erinevas arvutis (ja rahakotis), seega - mugavuse ja fookuse huvides - valisin Wallet airgap'i heleda teemaga, samas kui Wallet ekraanil on tume teema.



## Wallet Õhulõhe loomine



Pärast Electrumi allalaadimist ja kontrollimist võtke koopia käivitatavast failist ja viige see oma arvutisse võrguühenduseta. Seejärel käivitage see ja installige Electrum.



Topeltklõpsake Electrumi käivitamiseks: arvuti, kus te seda Wallet kasutate, on võrguühenduseta, ignoreerige võrgu seadistusi ja minge Wallet loomisele, mida käesolevas juhendis nimetame `airgap`.



![image](assets/en/01.webp)



Valige _Standardne rahakott_.



![image](assets/en/02.webp)



Ja seejärel valige _Create a new seed_, et tarkvara generate Mnemonic saaks Mnemonic.



![image](assets/en/03.webp)



Kirjutage täpselt 12 generate sõna Electrumilt paberkandjale ja jätkake kontrollimist, sisestades sõnad uuesti järjekorras, kui Electrum seda nõuab.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Kui Wallet loomine on lõpetatud, määrake keerukas parool (`Strong`), et krüpteerida Wallet fail airgap-seadmes. See samm on väga delikaatne ja oluline, sest nüüd valitud parool takistab juurdepääsu Wallet-le, millel on dispositiivne õigus, mis võimaldab kulutada raha tehingute allkirjastamiseks.



![image](assets/en/06.webp)



Vajutades nuppu _Finish_ on Wallet määratletud ja ilmub ekraanile. Loomulikult on võrguühenduse indikaator, s.t. värviline täpp paremas alumises nurgas, punane, kuna arvuti on lahti ühendatud ja ei võimalda Wallet-l võrguklahve paljastada.



![image](assets/en/07.webp)



## Visualiseerimise loomine Wallet



Nüüd, kui teie Wallet-l on offline-privaatvõtmed, peate seadistama Wallet kuvamise ehk "ainult vaatamise", mis võimaldab teil vaadata saldot, samuti valmistada ette kviitungitehinguid, et jätkata Sats turvalist kogumist.



Valige võrguühenduseta seadmes asuva Wallet menüüst _Wallet_ -> _Informatsioon_



![image](assets/en/08.webp)



Avaneb aken, mis sisaldab kogu teie Wallet teavet, kus saate märkida `derivatsioonitee` ja `master fingerprint`, näiteks märkida need Mnemonic lause sõnade kõrvale (tungivalt soovitatav).



![image](assets/en/09.webp)



Pidage meeles, et te võtate need andmed ühenduseta arvutist, seega peate kopeerima/liita `zpub` tekstifaili ja salvestama selle usb-pulgale.



Nüüd saate liikuda arvutisse, mis on ühendatud internetti, käivitada Electrumi ja luua uue Wallet.



Valige menüüst _File_ käsk _New/Restore_.



![image](assets/en/10.webp)



Uus Wallet on ainult vaatamiseks, nii et selles juhendis nimetame seda "ainult vaatamiseks".



![image](assets/en/12.webp)



Järgmisel ekraanil valige _Standardne rahakott_ ja jätkake, klõpsates nuppu _Järgmine_.



![image](assets/en/13.webp)



Võtmesalvestuse valimisel olge ettevaatlik: ekraani Wallet loomiseks valige _Kasutage üldvõtit_. Seejärel jätkake _Next_.



![image](assets/en/14.webp)



Sisestage siia Wallet-st offline kopeeritud `zpub`, mille tõite siia arvutisse usb-meedia kaudu.



![image](assets/en/15.webp)



Lõpetuseks määrake ka sellele Wallet-le tugev parool, mis võib erineda selle Cold jaoks valitud paroolist.



Ilmub ekraanil Wallet koos hoiatusega. Teade tuletab teile meelde, et tegemist on ainult näidikuga Wallet ja et te ei saa sellega seotud vahendeid kulutada.



**Märkuskaev**: **selle Wallet UTXOde käsutamiseks peate seega alati omama privaatvõtmeid**. Hea varundussüsteemiga ei ole teil raske jääda oma Bitcoine täielikult valdama.



![image](assets/en/16.webp)



See hoiatus ilmub iga kord, kui avate selle Wallet. Klõpsake _Ok_ ja liigume edasi kontrollimise sammu juurde.



## Kahe Wallet kontrollimine



Nagu me selle juhendi alguses õppisime, on Wallet õhupiir ja selle kuvamine Wallet kaks portfelli, millel on erinevad funktsioonid, kuid **jagavad samu aadresse**.



Kui me vaatame kahte rahakotti kõrvuti, märkame visuaalselt, et Wallet õhupiiril on sümbol "seed", samas kui ainult kellal seda ei ole. Juba see detail aitab teil meeles pidada, et Wallet ekraanil Wallet ei ole privaatseid võtmeid.



![image](assets/en/17.webp)



Esimese täpse kontrolli tegemiseks valige siiski mõlemas rahakotis menüü "Aadressid": kuna neil on samad aadressid, peaks aadresside nimekiri olema mõlemas identne.



![image](assets/en/18.webp)



⚠️ **TÄHELEPANU**: **ei saa olla mingit vahepealset teed; aadressid peavad olema samad. Kui need on erinevad, tuleb kogu senine töö kustutada ja alustada uuesti**.



Nüüd saate teha kaks erinevat kontrolli. Kõigepealt proovige kustutada mõlemad rahakotid ja taastada need nullist, kumbki vastavas arvutis. Juhul, kui te jätkate seda kontrollimist, on Wallet kuvamise protseduurid identsed eespool kirjeldatud protseduuridega.



Wallet airgap'i puhul peate aga `keystore'i ekraanil valima _Mulle on juba seemne_ ja sisestama sõnad, kopeerides need oma paberil olevast varukoopiast.



Pärast "no-load" prooviperioodi lõppu võite proovida teha väikese summa tehingu ja kulutada selle kohe.



## Tehingute vastuvõtmine ja kulutamine



Et alustada Electrumi airgap'i kasutamist, saate teha väikese summaga kviitungitehingu ja seejärel kulutada selle oma Address jaoks. Seejärel saate tutvuda protseduuriga, kontrollides, et teil on täielik kontroll rahaliste vahendite üle.



**Märkus**: Ma ei soovita, et te hoiustaksite Wallet-sse suurt summat enne, kui olete kindel, et saate kõik operatsioonid sujuvalt läbi viia.



Allpool kirjeldatud sammud võivad esmapilgul tunduda keerulised. Ärge laske end sellest heidutada: kui olete neid esimest korda proovinud, leiate, et nende tegemiseks kulub vaid mõni minut.



Raha saamiseks peate tingimata kasutama ekraanil Wallet, mis asub teie arvutis, mis on ühendatud internetti. Menüüst `Receive` klõpsake _Create request_, et Electrum generate oleks esimene vaba Address ja kasutage seda, et saata meile paar Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Kui tehing on paljundatud, näete juba, et - nagu on loomulik - see on nähtav ainult Wallet ekraanil, mitte aga Wallet õhupiiril.



![image](assets/en/21.webp)



Pärast seda, kui teie tehing on saanud kinnituse, saate valmistada kulu ette ja seega proovida allkirjastamise protseduuri Wallet-võrguväliselt. Seejärel valmistage tehing ette ainult vaatluse teel ja vajutage selle kontrollimiseks _Preview_



![image](assets/en/22.webp)



Saate täiustatud tehinguakna, kus saate seda näha:




- tehing ei ole allkirjastatud (staatus: allkirjastamata);
- käsklused "Sign" ja "Broadcast" on keelatud.



Ainus asi, mida saate teha, on eksportida tehingu sellisena, nagu see on, viia see Wallet õhupiirile ja allkirjastada see.



Sisestage USB-mälupulk arvutisse ja valige vasakus allosas asuvast menüüst _Jagamine_.



![image](assets/en/23.webp)



Seejärel valige _Save to file_.



![image](assets/en/24.webp)



Salvestage tehing usb-pulgale.



Märkate, et Electrum annab failile nime, mille esimesed numbrid on transaction ID, ja faili laiendus on `.PSBT`, mis tähendab `Partially Signed Bitcoin Transaction`.



Väljavõtke meedium koos failiga `.PSBT` ja ühendage see arvutiga võrguühenduseta.



Valige nüüd Wallet airgapist menüüst _Tööriistad_, seejärel _Load transaction_ ja seejärel From file_.



![image](assets/en/25.webp)



Valige failihalduriga selle asukohast `.PSBT`.



![image](assets/en/29.webp)



Võrguväline arvutitarkvara avab automaatselt täiustatud tehinguakna, mis on täiesti identne sellega, mida nägite Wallet ekraanil. Staatus on `Unsigned`, kuid erinevus seisneb selles, et käsk `Sign` on siin aktiivne. Ja just seda peate te täitma.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Nüüd, kui tehing on allkirjastatud, pidage meeles, et teie Wallet on võrguühenduseta masinas. Seetõttu - isegi kui te näete käsku "Broadcast" aktiivsena - ei saa teie Wallet tehingut Bitcoin võrku edastada.



Nüüd on vaja korrata allkirjastatud tehingu eksportimist usb-pulgale, et saaksite selle importida internetti ühendatud arvutisse ja seda levitada.



Valige vasakpoolsest alumisest menüüst uuesti _Jagamine_ ja seejärel _Salvesta faili_.



![image](assets/en/28.webp)



Nüüd on failil teine laiendus: **PSBT" asemel on tehingul nüüd laiendus "txn". Nüüdsest alates võimaldab Electrum teil allkirjastatud tehinguid allkirjastamata tehingutest ära tunda**.



![image](assets/en/30.webp)



Tehingu lõplikuks edastamiseks võtke usb-pulk võrguühenduseta arvutist välja ja sisestage see internetti ühendatud arvutisse.



Kordage Watch-only'st importimise protseduuri, st valige menüüst _Tööriistad_ _Load transaction_ ja lõpuks _From file_.



![image](assets/en/31.webp)



Electrum avab teile tehinguakna, mis erineb oluliselt sellest, mida näidati varem sellel Wallet-l, kuna see on nüüd allkirjastatud (`Status: allkirjastatud`) ja käsk `Broadcast` on juurdepääsetav.



Viimane toiming, mida peate tegema, on just see:



![image](assets/en/32.webp)



## Järeldused



Teie testid on nüüdseks lõppenud. Kui te järgisite juhendit ja saite samad tulemused, siis olete loonud Wallet Cold koos Electrumiga kahes erinevas arvutis, mida saate kasutada airgap-moodis oma Bitcoins säilitamiseks.



Ainsad asjad, millele peate tähelepanu pöörama, on kaks:


1) **ei tohi kunagi kasutada Wallet õhulõiku generate vastuvõtuaadressidele**. Kuna see on võrguühenduseta, pakub ta teile alati esimest Address, mis langeb kokku sellega, mida te just kasutasite proovitehingu tegemiseks;



![image](assets/en/33.webp)



nagu ülaltoodud pildilt näha, ei tea võrguühenduseta Wallet oma Address ajalugu. Ta on selles osas täiesti pime. **Ainsaks ülesandeks, mida ta saab teie jaoks teha, on teie offline-võtmete salvestamine ja tehingute allkirjastamine**_.



2) Kasutage ainult selleks otstarbeks mõeldud USB-mälupulka, **ei kasuta andmekandjat, mida kasutate sageli**. Igapäevased vahendid on suurema tõenäosusega küberrünnaku objektiks ja tahtmatult võite rünnata isegi arvutit, mida hoiate võrguühenduseta. USB-pulgal, mida kasutate ainult selleks otstarbeks, on väga vähe võimalusi võtta ühendust oma arvutiga võrgus, eriti kui olete hodler, kes ei pea kulutama, vähendades seega viiruste, pahavara jne. saamise ja seejärel edastamise tõenäosust.