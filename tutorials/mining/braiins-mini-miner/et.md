---
name: Braiins Mini Miner
description: Mining valmistamine hõlpsasti kodust.
---
![cover](assets/cover.webp)



### Sissejuhatus



Mini Miner braiins BMM 100 on toode, mille on loonud Mining pool Braiins. Sellel seadmel on atraktiivne disain ja see on äärmiselt vaikne. See toodab 1,1 Th/s arvutusvõimsust ja tarbib umbes 40 vatti. Erinevalt teistest seadmetest ei ole see avatud lähtekoodiga, kuid seda on tõesti lihtne paigaldada, see võtab tõesti vaid paar klõpsu! Mini Miner BMM 100 on esimene välja antud versioon. Nüüd on tootmises versioon 2, mille nimi on BMM 101, mis erineb esimesest suurema ekraani ja Wi-Fi olemasolu poolest, kuid paigaldusprotseduurid on samad.



Palju rohkem olulist teavet leiate ka otse [tootja veebisait](https://braiins.com/hardware/mini-Miner-bmm-100), kus on täielik juhend.



### Ülevaade BMM 100-st



seade näeb välja nagu rööptahukas, mille esiküljel on ekraan



![image](assets/en/01.webp)



ventilaator ülemisel küljel



![image](assets/en/02.webp)



samas tagaküljel on meil: auk voolu jaoks, ruumi SD-kaardi jaoks (mida võib olla vaja uuenduste jaoks), väike nupp, mis ütleb `IP REPORT`, mis annab teile teada mini Miner IP Address, mis Address on vajalik seadme armatuurlauale juurdepääsuks. Kui nuppu vajutatakse, kuvatakse IP Address umbes 5 sekundiks, seejärel kaob ja seadistatud ekraan ilmub uuesti. Kui teil on siiski vaja mõnda seadistust muuta, vajutage lihtsalt uuesti kõnealust nuppu ja IP Address ilmub uuesti ekraanile. Jätkates nimekirjaga leiame Ethernet-porti ja juurdepääsu seadme lähtestamise teostamiseks, mille jaoks tuleb haarata viigust ja hoida seda 10 sekundit all, et lähtestada kõik mini Miner seaded. Lõpuks leiame kaks märgutuld, ühe Green ja ühe punase, mis näitavad meile Miner olekut.



![image](assets/en/03.webp)



### Mini Miner ühendamine



Peate seadme ühendama internetiühendusega etherneti kaudu, märkige, et uue versiooni (BMM 101) puhul ei ole see enam vajalik. Tagasi selle mini Miner juurde, kui me leiame asukoha, peame selle kõigepealt internetiühendusega ja seejärel vooluga ühendama: seade lülitub automaatselt sisse ja näitab ekraanil oma IP Address.



### Konfiguratsioon



Me peame avama brauseri ja sisestama otsinguribale IP Address, mis näitab meile mini Miner. Tuletan teile meelde, et seadme leidmiseks võrgus peab see olema kohalik, seega peab arvuti, mida kasutate, olema ühendatud samasse võrku kui mini Miner. Kui oleme sisestanud IP Address, vajutame enter ja ekraanile ilmub sisselogimisleht mini Miner operatsioonisüsteemi, milleks on Braiins OS, sisselogimisleht.



![image](assets/en/06.webp)



Sisselogimiseks peate sisestama kasutajanimeks `root`, parooli võite jätta tühjaks. Klõpsake sisselogimisnuppu ja teie mini Miner armatuurlaud ilmub.



![image](assets/en/07.webp)



### Üldised seaded



Lähme süsteemi



![image](assets/en/24.webp)



seadistustest leiame mõned üldised seaded, nagu teema (heledad või tumedad), keel, ajavöönd ja paroolide muutmine.



![image](assets/en/25.webp)



Kui me läheme selle asemel "Mini Miner ekraanile", siis on meil meie mini Miner seaded, näiteks ekraani kuvamine. Me saame valida, kas näidata aega või Bitcoin hinda või ekraani koos masina olekuteabega, näiteks toote Hash, temperatuuri, tarbitud vattide ja nii edasi. Siin on teie otsustada, mida soovite ekraanil näha; me saame ka muuta ekraani heledust, määrata öise režiimi ja kuvada aega 12-tunnise või 24-tunnise formaadiga.



![image](assets/en/26.webp)



Kui olete muudatused teinud, klõpsake nuppu "Muudatuste salvestamine" ja näete muudatusi oma seadme ekraanil



![image](assets/en/27.webp)



### Ühendus Mining pool-ga



Nüüd ei ole me veel töökorras, sest me peame Mining käivitamiseks ühenduma basseiniga, nii et me peame minema "Configuration"



![image](assets/en/08.webp)



ja esimene kirje on lihtsalt "Poolid".



![image](assets/en/09.webp)



Siinkohal peame otsustama, millist basseini kasutada. Selles õpetuses näitan teile kahte võimalust. Esimene on ühendada meid Mining pool Braiinsiga, mida kasutavad ka professionaalsed kaevurid, nagu näete sellest õpetusest:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Teine võimalus on ühendada meid Mining pool, mis mina soolo, nagu Public Pool, järgige seda juhendit, et seda teha:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

#### Braiins bassein



Selle basseiniga ühendumiseks peame looma konto. see bassein teeb ka makseid, kasutades Lightning Network, nii et me saame päevas paar Sats. Selleks peame looma Address välgu, millele saame preemiaid. Kui te ei tea, kuidas luua kontot braiins pooli või kuidas luua oma Address välk, võite järgida seda juhendit:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Kui see on tehtud, oleme Braiinsi basseinis armatuurlaual. Mida me peame tegema, on öelda basseinile, et me tahame ühendada ühe meie kaevuritega, nii et ekraani vasakul poolel on mitmeid kirjeid. Me peame minema "töötajate" juurde



![image](assets/en/04.webp)



ja me peame klõpsama lillat värvi nupule paremal, millel on kirjas "Connect workers" (ühenda töötajad)



![image](assets/en/05.webp)



Siin tuleb aken, kus on teave, mida me vajame meie mini Miner ühendamiseks basseiniga. Ainus muudatus, mida me saame teha, on valida Stratum V2. Selle kohta, mis on Stratum v2, leiate selle kirje [glossary] (https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Nüüd peame kopeerima selle stringi, mis algab stratumv2. Nii et me klõpsame väikesele "copy" sümbolile, seejärel läheme meie mini Miner armatuurlauale, mille me jätsime konfiguratsiooni ja basseinidesse. Vajutame add new pool (lisa uus bassein)



![image](assets/en/11.webp)



ja kleepige kopeeritud string Pool URL-i all olevasse ruumi.



![image](assets/en/12.webp)



Nüüd peame lisama kasutajanime ja parooli. Lähme tagasi basseini dashboadile. Selle all on meil ka userID ja parool. UserID ja meie kasutajanimi, see, mille andsime konto loomisel, lisaks Miner nimi, mille tahame sisestada. sa võid otsustada, kas sa annad nime seadmele, mida sa ühendad basseiniga, see on vabatahtlik, kuid soovitav on see sisestada, et kui sa ühendad mitu seadet, siis on neid lihtsam kohe tuvastada. Kui te ei soovi midagi selle asemel panna, võite jätta `workerName`.



![image](assets/en/13.webp)



Seejärel läheme meie mini Miner ja sisestame kasutajanime. Siin sisestame minu puhul "finalstepbitcoin", mis on minu kasutajaID, miniminer dot. See on nimi, mille ma otsustasin seadmele anda. Kui te ei soovi sellele nime anda, siis kirjutage lihtsalt userid dot workername. Minu puhul oleks see finalstepbitcoin.workername. Kui olete kasutajanime sisestanud, saate valida parooli ja kirjutada selle tühjale väljale. Võite panna ka anithing123, mis on see, mida ka pooli ekraanil näidatakse, kuid see tahab lihtsalt näidata, et võite panna mis tahes parooli.



Kui olete kõik andmed sisestanud, peate vajutama paremal asuvat salvestusnuppu (see, mis on disketi kujuline) ja nii olete mini Miner-s konfigureerinud basseinide andmed.



![image](assets/en/14.webp)



Nüüd tuleb minna tagasi basseini armatuurlauale ja klõpsata nupule "Ühendatud! Mine tagasi."



![image](assets/en/15.webp)



Oleme ühendanud meie mini Miner braiins basseiniga! Nüüd näete seda töötajate nimekirjas. Kui see ei ilmu, siis tehke värskendus ja oodake mõni hetk. Kui ta ilmub, kontrollige, et tal on staatus "OK" koos Green märkega.



![image](assets/en/17.webp)



kui te lähete tagasi armatuurlauale, peaksite hakkama nägema liikumist graafikul ja nägema meie seadme Hashrate. See tähendab, et bassein võtab meie tööd vastu ja seega oleme igatahes õõnestamas.



![image](assets/en/16.webp)



#### Avalik bassein



Selle basseini kaudu saab proovida oma õnne ja kaevandada üksi, tuginedes basseini. Sellisel juhul ei saa me tasu, kuid me saame kogu tasu, kui meil õnnestub kunagi plokki kaevandada. Seejärel ühendame avaliku basseiniga, ainult Mining-le mõeldud basseiniga, mis on täiesti avatud. Avame brauseris uue akna ja läheme aadressile [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



seal läheb lehekülg kogu vajaliku teabega. Seejärel kopeerime sinna kihi Address



![image](assets/en/19.webp)



siis läheme tagasi meie mini Miner armatuurlauale, läheme konfiguratsiooni ja basseinide juurde, klõpsame add new pool (sama protsess nagu eespool) ja kleebime "stratum Address alla basseini url.



![image](assets/en/20.webp)



Nüüd läheme tagasi basseini lehele ja näeme, et kasutajanimeks peame sisestama Bitcoin Address, mis on see, millele me saame tasu juhul, kui me õõnestame blokki, siis punkt ja siis meie seadme nimi, nagu me varem tegime Braiins Pool, samas kui salasõna saame ise valida.



![image](assets/en/21.webp)



Me läheme tagasi mini Miner ja alla kasutajanimi kleebime Address Bitcoin, millele järgneb punkt ja nimi, ma panen `miniminer`. Salasõnaks panen hoopis test, sisestate mis iganes soovite.



![image](assets/en/22.webp)



Nüüd salvestame seaded ja lülitame Braiins basseini välja.



![image](assets/en/23.webp)



Hea! Me oleme nüüd Mining avalikus basseinis!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)