---
name: Lightning Network+
description: Saage tasuta sissetulevat likviidsust koos koostööst tulenevate avanemistega oma Lightning-sõlmes
---

![cover](assets/cover.webp)



## Sissejuhatus



[LN+ (Lightning Network Plus)] (https://lightningnetwork.plus/) on kogukonnaplatvorm, mis on loodud Lightning Network sõlmede operaatorite vahelise koostöö hõlbustamiseks. Selle peamine eesmärk on parandada Lightning-võrgu ühenduvust, likviidsust ja detsentraliseerimist, ilma et oleks vaja tsentraliseeritud vahendajaid.



Selles õpetuses keskendutakse **"Swaps "** teenusele, mis on LN+ kõige laialdasemalt kasutatav ja struktureeriv funktsioon tänapäeval. Tutvustatakse ka teisi platvormi pakutavaid teenuseid.



## LN+ ülevaade



### Mis on Lightning Network Plus?



Lightning Network Plus (LN+) on kogukonnaplatvorm välgussõlmede operaatoritele, kes soovivad teha otsest ja vabatahtlikku koostööd. Selle eesmärk on hõlbustada kasulike, tasakaalustatud ja jätkusuutlike Lightning-kanalite loomist, vältides samal ajal vajadust tsentraliseeritud lahenduste või pealesunnitud keskuste järele.



LN+ põhineb ühel põhiprintsiibil: vastastikune koostöö, mis põhineb läbipaistvusel, vastastikkusel ja mainel.



### LN+ teenused lühidalt



LN+ pakub mitmeid teenuseid, mille eesmärk on parandada Lightning-võrgu topoloogiat ja likviidsust, sealhulgas :





- Vahetus**: kanalite vastastikune avamine operaatorite vahel (põhiteenus).
- Rõngad**: mitme osaleja vahelised ringikujulised kanaliavad.
- Usalduspõhised vahetustehingud**: variandid, mis tuginevad rohkem osalejate usaldusele ja ajaloole.
- Sotsiaalsed funktsioonid**: profiilid, kommentaarid ja mainesüsteem.



Selle õpetuse ülejäänud osas keskendume ainult **Swaps** teenusele, mis on praeguse LN+ kasutamise keskmes.



## LN+ "Swaps" teenus



### LN+ vahetuse määratlus



LN+ **vahetus** on kahe Lightning-sõlme operaatori vaheline vabatahtlik kokkulepe avada vastastikku samaväärse (või eelnevalt kokkulepitud) võimsusega Lightning-kanalid. Erinevalt tavalisest ühepoolsest kanali avamisest põhineb vahetusleping **selge vastastikkuse põhimõttel**.



Praktikas :





- Te avate kanali oma partneri sõlme.
- Teie partner avab kanali teie sõlme.
- Mõlemad osapooled seovad sarnase koguse on-chain bitcoine.



### Mis on sõlmeoperaatorite vahetuste eesmärk?



Swapteenus tegeleb mitmete põhiprobleemidega, millega Lightning-ettevõtjad kokku puutuvad:





- Parem ühenduvus**: kasulike kahesuunaliste kanalite loomine kohe pärast nende avamist.
- Parem likviidsuse juhtimine**: igal osapoolel on nii sissetulev kui ka väljaminev võimsus.
- Vähendatud oht, et kanalid on ebavajalikud**: partnerit julgustatakse kanalit avatuna hoidma.
- Suurem detsentraliseerimine**: operaatorite vahelised otseühendused, ilma pealesunnitud sõlmpunktideta.



### Milliste sõlmprofiilide puhul on vahetused kasulikud?



Vahetuslepingud on eriti kasulikud :





- Uued sõlmed, kes soovivad kiiresti parandada oma marsruutimisvõimet.
- Vahendajad, kes soovivad suurendada oma kanali graafiku tihedust.
- Marsruutimisele orienteeritud sõlmed, mis soovivad oma topoloogiat optimeerida.



## Ühendage oma Lightning-sõlm LN+-ga



### Tehnilised nõuded



Enne alustamist vajate :





- Töötav Lightning-sõlm (LND, Core Lightning või Eclair).
- Juurdepääs sõlme haldusliidesele.
- Piisav on-chain võimsus kanalite avamiseks.



Mine [Lightning Network](https://lightningnetwork.plus/) Plus veebilehele ja klõpsa kasutajaliidese paremas ülaosas olevale nupule "Sisselogimine".



![capture](assets/fr/03.webp)



### Autentimine sõnumi allkirja abil



Enda autentimiseks peate esitatud sõnumi allkirjastama, kasutades oma Lightning-sõlme privaatvõtit. ThunderHub abil on see toiming väga lihtne.



Alustage LN+ poolt kuvatava teate kopeerimisest.



![capture](assets/fr/04.webp)



Mine ThunderHubs vahekaardile "Tööriistad" ja klõpsa seejärel nupule "Allkiri" sektsioonis "Sõnumid".



![capture](assets/fr/05.webp)



Sisestage LN+ poolt esitatud autentimissõnum, seejärel klõpsake nuppu "Allkirjastada".



![capture](assets/fr/06.webp)



Seejärel allkirjastab ThunderHub selle sõnumi, kasutades teie sõlme privaatvõtit. Kopeerige genereeritud allkiri.



![capture](assets/fr/07.webp)



Sisestage see allkiri LN+ veebisaidi vastavasse väljale ja klõpsake seejärel nuppu "Allkirjastamine".



![capture](assets/fr/08.webp)



Nüüd olete LN+-ga ühendatud oma Lightning-sõlme abil. See protsess võimaldab LN+-l kontrollida, et te olete nende platvormil taotletava sõlme seaduslik omanik.



![capture](assets/fr/09.webp)



Soovi korral saate oma LN+ profiili isikupärastada, lisades näiteks lühikese elulookirjelduse.



## Osaleda olemasolevas vahetustehingus



### Juurdepääs vahetuspakkumistele



Oma esimese kanali avamisel osalemiseks minge kasutajaliidese ülaosas asuvasse menüüsse `Swaps`. Siit leiate kõik hetkel saadaval olevad swapid, sõltuvalt teie sõlme omadustest.



![capture](assets/fr/10.webp)



### Abikõlblikkuse tingimused



Olemasoleva vahetuspakkumisega liitumiseks valige lihtsalt vastav kuulutus ja registreeruge. LN+ võimaldab aga vahetustehingu loojal määratleda teatavad **kõlblikkuse tingimused**, näiteks :





- minimaalne arv kanaleid on juba avatud ;
- minimaalne sõlme koguvõimsus ;
- teatud tüüpi ühendused on lubatud.



### Hiljutised sõlmed



Selle tulemusena on võimalik, et eriti kasutamise algstaadiumis on teie sõlme jaoks **vähe või üldse mitte ühtegi pakkumist**. See on tavaline olukord uute või veel ühendamata sõlmede puhul.



Minu puhul ei vastanud ükski pakkumine nõutavatele kriteeriumidele, hoolimata mõne avatud kanali olemasolust.



## Loo oma vahetuspakkumine



### Millal peaksite looma oma vahetuslepingu?



Kui olemasolevat pakkumist ei ole, on omaenda vahetuslepingu loomine sageli parim lahendus. Samuti võimaldab see säilitada kontrolli vahetuslepingu parameetrite üle.



### Vahetuskonfiguratsioon



Klõpsake **Start Liquidity Swap**, seejärel konfigureerige oma pakkumise parameetrid:





- valige osalejate koguarv (3, 4 või 5);
- näitab avatavate kanalite läbilaskevõimet;
- määratleda kohustusperiood, mille jooksul osalejad nõustuvad oma kanaleid mitte sulgema;
- täpsustada kõik osalejate suhtes kohaldatavad piirangud (minimaalne kanalite arv, minimaalne koguvõimsus, vastuvõetava ühenduse tüüp).



![capture](assets/fr/11.webp)



### Avaldamine ja osalejate ootused



Kui kõik parameetrid on sisestatud, klõpsake pakkumise avaldamiseks **Start Liquidity Swap**. Nüüd peate vaid ootama, et teised operaatorid registreeruksid.



![capture](assets/fr/12.webp)



## Vahetuse lõpuleviimine



### Efektiivne kanali avanemine



Nüüd, kui kõik vahetuspositsioonid on võetud, saab iga osaleja oma LN+ kasutajaliidesest näha, millise sõlme jaoks ta peab Lightning-kanali avama.



![capture](assets/fr/13.webp)



Avage kanal, kasutades LN+ poolt antud sõlme ID-d ja järgides näidatud summat. Seda toimingut saab teha ThunderHub, mõne teise Lightning-sõlme halduri või otse teie sõlme põhiliidese kaudu.



![capture](assets/fr/14.webp)



Kui kanal on avatud, ilmub see ootavate kanalite sektsiooni.



![capture](assets/fr/15.webp)



### Kinnitus LN+-s



Seejärel naaske LN+-sse, et kinnitada, et olete algatanud kanali avamise, klõpsates nupule "Kanali avamine algas".



![capture](assets/fr/16.webp)



### Vahetuse lõpp



Kui kõik osalejad on avanud kanalid, milleks nad on võtnud kohustuse, loetakse vahetus lõpuleviiduks.



## Maine ja head suhtlemistavad



### LN+ mainesüsteem



LN+ sisaldab mainesüsteemi, mis põhineb osalejate poolt vahetuste lõpus jäetud arvamustel. Need arvamused on avalikud ja mõjutavad otseselt operaatori võimalust liituda või luua tulevasi vahetustehinguid.



![capture](assets/fr/17.webp)



### Soovitatavad parimad tavad



Hea maine säilitamiseks ja vahetustehingute sujuvaks toimimiseks on soovitatav :





- järgida kanali avamise tähtaegu ;
- suhelda probleemide või viivituste korral kiiresti;
- kasutage kommentaaride sektsiooni, et vahetada arvamusi teiste osalejatega;
- mitte sulgeda kanalit enne kohustuseperioodi lõppu.




![capture](assets/fr/18.webp)



### Miks maine on LN+ jaoks keskse tähtsusega



LN+ põhineb vabatahtliku koostöö mudelil, millel puuduvad tugevad tehnilised piirangud. Seepärast on maine peamine stiimul osalejate usaldusväärsuse ja usaldusväärsuse tagamiseks.



## Muud LN+ teenused



Lisaks vahetuslepingutele pakub LN+ muid teenuseid, mille eesmärk on parandada ühenduvust ja koordineerimist välgussõlmede operaatorite vahel. Rõngad** võimaldavad mitmel osalejal luua kanalite avamise silmuse, tugevdades seeläbi marsruutimisradade redundantsust ja Lightning-graafi tihedust. Usalduspõhised vahetustehingud** põhinevad sarnastel põhimõtetel nagu klassikalised vahetustehingud, kuid pakuvad suuremat paindlikkust osalejatele, kellel on platvormil juba väljakujunenud maine.



LN+ sisaldab ka sotsiaalseid funktsioone, nagu avalikud sõlmprofiilid, kommentaaride vahetamine ja mainesüsteem. Need vahendid ei ole iseenesest tehnilised teenused, vaid mängivad keskset rolli platvormi tõrgeteta toimimises, hõlbustades suhtlust, koordineerimist ja usaldust operaatorite vahel.



## Kokkuvõte



LN+ Swapsi teenus on tõhus vahend Lightning-võrgustiku ühenduvuse, likviidsuse ja detsentraliseerimise parandamiseks. Edendades vastastikuseid, koordineeritud kanalite avamisi, võimaldab LN+ sõlmede operaatoritel tugevdada oma topoloogiat, edendades samal ajal vastutustundlikku, detsentraliseeritud koostööd.