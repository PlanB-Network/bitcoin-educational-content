---
name: COLDCARD Q - Key Teleport
description: Mis on Key Teleport ja kuidas seda kasutada?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Mis on **Key Teleport** funktsioon, mida Coinkite pakub oma lipulaeva ColdCardQ seadmega?



**Key Teleport** võimaldab teil konfidentsiaalseid andmeid 2 ColdCardQ vahel turvaliselt edastada. Edastuskanal ei pea isegi olema krüpteeritud ja võib olla avalik.



Seda saab kasutada ülekandmiseks:





- gW-0 fraasid (ColdCard Q seed master või ColdCardQ [seed Vault](https://coldcard.com/docs/temporary-seeds/#seed-vault) salvestatud saladused).
- **konfidentsiaalsed märkmed ja paroolid**: see võib olla mis tahes salajane või kogu [Secure Notes & Passwords] kataloog (https://coldcard.com/docs/secure_notes/) teie ColdCardQ-s.
- kogu teie **ColdCardQ varukoopia**: selle varukoopia saanud ColdCardQ-l ei tohi olla seed Master, et see toimiks.
- gW-3 (**Partiilselt allkirjastatud Bitcoin tehingud** osana mitme allkirja süsteemist).



See eeldab, et olete uuendanud oma [seadme püsivara versioonile v1.3.2Q](https://coldcard.com/docs/upgrade/) või uuemale versioonile.



## Kuidas ma kasutan Key Teleport'i?



### 1- Igasuguste andmete edastamiseks



Siin vaatleme seed lausete, märkmete, paroolide või kogu ColdCardQ varukoopia ülekandmist. PSBT ülekandeid mitme allkirjaga tehingute puhul käsitletakse hiljem.



#### Valmistage seade ette saladuste vastuvõtmiseks



Valige oma ColdCardQ menüüst **"Täpsemad / Tööriistad**" valik **"Key Teleport (start) "**.


Järgmisel ekraanil pakutakse välja 8-kohaline parool, siin "20420219". Te peate selle salasõna saatjale edastama. Kasutage selle salasõna saatmiseks näiteks SMS-i või oma lemmik turvalist sõnumsüsteemi või isegi häälkõnet.



Seejärel klõpsake oma ColdCardQ-l nupule **"Enter**", et liikuda edasi järgmise sammu juurde.




![CCQ-key-teleport](assets/fr/01.webp)




Ekraanile luuakse QR-kood. Jällegi peate selle QR-koodi edastama ColdCardQ "saatjale". Kõige lihtsam viis seda teha on videokõne kaudu.



**SE EI TOHI SEDA QR-KOODI SAATA SAMA ÜLEKANDEKANALI KAUDU, MIDA KASUTATI EELMISE 8-KOHALISE SALASÕNA SAATMISEKS**.



![CCQ-key-teleport](assets/fr/02.webp)



*Neile, keda see huvitab, püüame aru saada, milline on see mehhanism, mis võimaldab saladuste edastamist turvamata kanalite kaudu*



*Mida me siin tegelikult teeme, on saladuste edastamise algatamine Diffie-Hellmani meetodi abil, mida ma olen käsitlenud allpool toodud BTC204 kursusel*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Praegu on meil:*




- genereeritakse efemeriaalne võtmepaar (avalik/privaatne vastavalt Ka ja ka, kusjuures Ka=G.ka, G on ECDH-generaatori punkt) ja 8-kohaline salasõna.
- kasutas seda parooli avaliku võtme (Ka) krüpteerimiseks AES-256-CTR abil, seejärel edastas selle parooli sidekanali A kaudu "saatvale" **ColdCardQ**-le
- lõpuks edastasime krüpteeritud paketi saatjale eespool kirjeldatud QR-koodi kaudu, kasutades teist, esimesest erinevat sidekanalit B.



#### Valmistage ette seade, mis saadab saladusi



Klõpsake saatvas seadmes nupule **"QR "**, et skaneerida vastuvõtva seadme poolt saadetud QR-kood, seejärel sisestage 8-kohaline parool, mis teile eelmises etapis eraldi kanali kaudu edastati. Nüüd oleme valmis alustama andmete saatmist "saatvast" seadmest.



**Palun, ärge sisestage 8-kohalist salasõna valesti, sest veateadet ei kuvata ja protsess jätkub. Lõplik andmeedastus siiski ebaõnnestub ja te peate alustama uuesti**.



![CCQ-key-teleport](assets/fr/03.webp)



*Uudishimulikumatele teie seas, vaatame veelkord, millega me krüptograafia ja salajase ülekande osas tegeleme:*




- me impordime krüpteeritud andmed, skaneerides vastuvõtvas seadmes QR-koodi.
- siis me dekrüpteerisime need, kasutades 8-kohalist parooli, mis edastati meile sekundaarse kanali kaudu.
- seega on meil olemas vastuvõtja poolt algselt loodud avalik võti (Ka).
- Seejärel koostame generate uue efemerse võtmepaari (Kb/kb, Kb=G.kb) saatvas seadmes, mida kasutame ECDH-i kohaldamiseks Ka suhtes. Seetõttu teostame operatsiooni kb.Ka=Ks , kus Ks on **"Seansivõtmeks "**




Nüüd palutakse teil valida 2 ColdCardQ vahel edastatavate saladuste laad (konfidentsiaalsed märkmed, parool, täielik varukoopia, teie võlvikus sisalduvad seemned, seed seadme master).



![CCQ-key-teleport](assets/fr/04.webp)



Siin on meie saladus lühisõnum, valides **"Kiirsõnum "**. Kirjutage oma sõnum (meie puhul "PlanB Network rocks") ja vajutage seejärel **"ENTER "**.


Seejärel genereerib seade uue juhusliku salasõna nimega **"Telepordi salasõna "** , näiteks "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Vajutage **"ENTER "** ja teile kuvatakse uus QR-kood. Laske see vastuvõtva seadmega skaneerida. Ja edastage teises sidekanalis **"Teleport Password "** vastuvõtjale.



![CCQ-key-teleport](assets/fr/06.webp)



*Siin jälle uudishimulikele, selles etapis:*




- pärast edastatavate saladuste valimist generate uus juhuslik parool nimega **"Teleport Password"**.
- seejärel krüpteerime saladused AES-256-CTR abil, kasutades eelmises etapis genereeritud **"Session Key"**, *"Ks"*.
- me lisame juba **"Seansivõtmega "** krüpteeritud paketile meie avaliku võtmega Kb, seejärel lisame veel Layer AES-256-CTR krüpteeringu koos **"Telepordi parooliga "**. Seejärel kodeeritakse kogu asi QR-koodiks




#### Saladuste üleandmise lõpuleviimine vastuvõtvale seadmele



Vajutage nuppu **"QR "**, et skaneerida saatva seadme poolt visioonikanali kaudu esitatud QR-koodi. Teil palutakse sisestada oma **"Teleport Password "** meile "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Seejärel dekrüpteeritakse andmed ja tehakse need vastuvõtvale seadmele arusaadavaks. Saadud sõnum on tõepoolest "PlanB Network rocks". See on kõik.



![CCQ-key-teleport](assets/fr/08.webp)



*Mis tegelikult juhtus selle viimase etapi jooksul :*?




- oleme dekrüpteerinud saatja poolt edastatud andmed, kasutades **"Teleport Password"**.
- meil on seega avalik võti Kb ja meie salajane sõnum, mis on krüpteeritud **"Seansivõtmega "**, "Ks". Kuid kuidas me saame seda teha, sest vastuvõtjana ei tea me Ks, mille on loonud saatja?
- Me peame kohaldama oma isiklikku võtit "ka" algsest sammust **"Valmistage seade, mis saab andmeid"**, avalikku võtit Kb.
- Tegelikult, arvutades ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, leiame Ks. Mida kasutatakse lõpuks salajase sõnumi dešifreerimiseks.



### 2- PSBT üleviimine Multisig-le (edasijõudnud)



See eeldab, et teie Wallet Multisig on juba loodud ja et teie ColdCardQ seade on juba eelseadistatud nii, et see suudab teha mitme allkirjaga tehinguid. Kui see ei ole nii, on selgitused saadaval [siin](https://coldcard.com/docs/Multisig/) Coinkite'i veebisaidil.



Kiire meeldetuletus, mis on mitme allkirjaga Wallet (Multisig).



Tavaliselt on teie Wallet vahendite kulutamiseks vaja ainult ühte isiklikku võtit, et avada teie aadressidega seotud UTXOd.


Wallet Multisig puhul võib vahendite kulutamiseks olla vaja kuni 15 isiklikku võtit ja seega 15 allkirja. Seda nimetatakse "M N-st" portfelliks, kusjuures N on vahemikus 1-15 ja M on vahendite kulutamiseks vajalike allkirjade arv. Näiteks Wallet Multisig 3 out of 5 nõuab vähemalt 3 allkirja võimalikust 5-st.



Väljakutse on siis kooskõlastada allakirjutanute vahel, et allkirjastada "PSBT" omakorda "Partially Signed Bitcoin Transaction" jaoks. Selles kontekstis saab "**Key Teleport**" kasutada PSBT edastamiseks kaasallkirjastajate vahel lihtsal ja konfidentsiaalsel viisil. Selleks piisab ka lihtsast videokõnest kaasallkirjutajate vahel.



Siin on näha, kuidas seda tehakse Multisig 3 of 4 puhul.



**allkirjastaja 1:**



Allakirjutanu 1 impordib ja allkirjastab PSBT. Lõpuks klõpsab ta **"T "**, et kasutada **"Key Teleport "**, et edastada PSBT allakirjutajale 2.



![CCQ-key-teleport](assets/fr/09.webp)




Pärast allakirjutanu 2 valimist, klõpsates **"ENTER "**, antakse "TELEPORT PASSWORD" (siin JJ YC AB 6A), mis tuleb edastada allakirjutanu 2-le teise sidekanali kaudu. Näiteks SMS või häälkõne, kuid **ei** videokõne.



Vajutage uuesti **"ENTER "** ja ilmub QR-kood, mis kujutab PSBT, mis on allkirjastatud 1 ja seejärel krüpteeritud "TELEPORT PASSWORD".



![CCQ-key-teleport](assets/fr/10.webp)



**allkirjastaja 2:**



Allakirjutanu 2 skaneerib allakirjutanu 1 poolt talle esitatud QR-koodi. Seejärel sisestab sekundaarse sidekanali kaudu edastatud "TELEPORT PASSWORD", et dekrüpteerida edastatud andmed.



Allakirjutanu 2 allkirjastab tehingu ja seejärel klõpsab **"T "**, et edastada PSBT "Key Teleport" kaudu allakirjutanu 3-le.


On selge, et 2 allkirja on juba kantud. Puudub vaid 3. allakirjutaja allkiri, et tehing oleks kehtiv. Valige allakirjutanu 3, klõpsates **"ENTER "**.



![CCQ-key-teleport](assets/fr/11.webp)



Ja luuakse uus "TELEPORT PASSWORD", millele järgneb uuesti QR-kood, mis kodeerib PSBT, mis on allkirjastatud 1 ja 2 ning seejärel krüpteeritud selle uue "TELEPORT PASSWORD" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**allkirjastaja 3:**



Korrake sama sammu nagu eespool.


Allakirjutanu 3 skaneerib allakirjutanu 2 poolt talle esitatud QR-koodi. Seejärel sisestab sekundaarse sidekanali kaudu edastatud "TELEPORT PASSWORD".



Allakirjutanu 3 allkirjastab tehingu ja kuna seekord on rakendatud 3 allkirja neljast, siis on tehing märgitud lõpetatuks ja on valmis levitamiseks erinevate andmekandjate kaudu (SD-kaart, NFC, QR jne).



![CCQ-key-teleport](assets/fr/13.webp)



Kui teie ColdCardQ "Push Tx" funktsioon on aktiveeritud, kinnitage oma ColdCardQ lihtsalt mis tahes NFC-ühendusega Interneti-ühendusega seadme (nutitelefoni/tahvelarvuti) tagaküljele, et edastada tehing üle Bitcoin võrgu.



![CCQ-key-teleport](assets/fr/14.webp)



*PSBT ülekandmiseks ühelt allakirjutajalt teisele kasutatakse "Key Teleport" lihtsalt "Teleport Password" abil igas etapis, mis krüpteerib PSBT, kui see kantakse üle ühelt allakirjutajalt teisele. Kuna edastatud andmeid ei saa kasutada vahendite varastamiseks, ei ole vaja Diffie-Hellmani, nagu on vaja väga konfidentsiaalsete saladuste (seed, parool jne...)* saatmisel.



![CCQ-key-teleport](assets/fr/15.webp)



*Allikas: [ColdCard ametlik kodulehekülg](https://coldcard.com/)*