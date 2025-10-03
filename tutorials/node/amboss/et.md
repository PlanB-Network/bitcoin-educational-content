---
name: Amboss
description: Uurige ja analüüsige Lightning Network
---

![cover](assets/cover.webp)



Lightning Network on Bitcoin protokolli Layer, mis töötati välja eelkõige selleks, et edendada Bitcoin maksete kasutuselevõttu igapäevaselt, suurendades iga tehingu töötlemiskiirust. Detsentraliseerimise põhimõttel põhinev Lightning Network koosneb sõlmedest (arvutitest, mis kasutavad Lightningi rakendamist), mis suhtlevad üksteisega peer-to-peer, edastades üksteisele andmeid (maksed ja maksete kontrollimine).



https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Nii nagu põhiketi puhul, on ka siin muutunud oluliseks võimaldada kasutajatel saada teavet ja teavet võrgu seisundi kohta, et hõlbustada sõlmedevahelisi ühendusi ja vähendada võrgus üldiselt tekkivat likviidsusprobleemi. Tõepoolest, Lightning Network-s soovitame Bitcoin põhiahelas tehtavatest tehingutest suhteliselt väiksemate summade mikromakseid.



Oluline on märkida, et kõik Lightning-sõlmed ei ole Ambossi platvormil saadaval.



Nagu [Mempool Space](https://Mempool.space), mis annab kasulikku teavet Bitcoin protokolli peamise ahela kohta, alates 2022 [Amboss](https://amboss.space) annab teavet :





- Lightning Network-sõlmede sõlmpunktid
- Maksekanalid ja nende maksevõime
- Lightning Network areng ajas
- Statistika maksude kohta, mis on seotud teie maksete edastamise sõlmpunktidega.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Selles õpetuses tutvustame teile seda platvormi, mis on oluline ressurss Lightning Network kasutajatele, neile, kes soovivad oma sõlme ühendada, et laiendada võrku jne.




## Leia paarid



Amboss platvormi üks eesmärk on võimaldada võrgu erinevatel sõlmpunktidel üksteisega ühendust luua ja omavahel teavet vahetada. Platvormi avalehel saate otse otsida juba tuttava sõlme nime või leida sõlmi kõige populaarsematest Lightning-portfellidest, mida kasutate.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Kodulehelt leiate ka sõlmed, mis on liigitatud vastavalt :




- Võimsuse areng: sõlme avaliku võtmega seotud Bitcoin kogus ja kõigis tema kanalites saadaolev kogus.
- Kanali areng: uute ühenduste arv teiste võrgusõlmedega.
- Sõlme populaarsus: kui sageli sõlme kasutatakse.



![nodes](assets/fr/03.webp)



Seega tuleb õige sõlme valimisel kontrollida järgmisi kriteeriume:





- Veenduge, et sõlmes on piisav kogus bitcoine; mida suurem on sõlme võimsus, seda rohkem bitcoine saate maksta.





- Veenduge, et sõlmpunktil on palju ühendusi ja avatud kanaleid teiste võrgusõlmedega.





- Veenduge, et sõlme on aktiivne ja tema kolleegid hindavad seda endiselt, kontrollides uute kanalite arvu; mida rohkem uusi kanaleid on sellel sõlmel avatud, seda enam hindavad teised võrgus olevad sõlmed teda.



Kui olete õige sõlme leidnud, klõpsake selle nimele, et suunata teid sõlme infolehele.



Sellel Interface, kontrollides äsja loodud kanali Timestamp, saate aimu selle sõlme aktiivsusest. Samuti leiate teavet selle sõlme kanalite läbilaskevõime kohta: see teave on oluline, kui soovite seda sõlme aktiivselt maksete tegemiseks kasutada.




![node_info](assets/fr/04.webp)



Vasakpoolses osas leiate rohkem üksikasju selle sõlme asukoha kohta. Näiteks saate vaadata :




- Avalik võti: identifikaator kohe sõlme nime all.
- Selle sõlme geograafiline asukoht.




![channels](assets/fr/05.webp)



See Interface ütleb teile selle sõlme Address ühenduse: see on kujul `pubkey@ip:port`. Meie näites tahame ühendada sõlme, mille :




- avalik võti `pubkey` on: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Sadam: `9735`



![geoinfo](assets/fr/06.webp)



Jaotises **Kanalid** näete avatud kanalite nimekirja ja sõlme ühendusi teiste võrgusõlmedega. Selles Interface on mitu teavet, mis on olulised, et kinnitada, et see sõlmpunkt vastab meie vajadustele või on usaldusväärne:





- Sissetuleku suhtarv**: Summa, mida sõlmpunkt nõuab teilt iga saadud miljoni Satoshi eest, sõltuvalt valitud kanalist.
- Suhtarv (osad miljoni kohta)** : see näitab, mitu Satoshi miljoni ühiku kohta võtab sõlmpunkt teilt tasu, kui otsustate teha makse ühe oma kanali kaudu. Oletame, et te otsustate teha makse `10_000 Sats` kanali kaudu, mille ppm suhe on `500 Sats`, siis peate te maksma sõlmpunktile `10_000 * 500 / 1_000_000` satoshi, mis vastab `5 Sats`-le.
- [HTLC](https://planb.network/resources/glossary/HTLC) maksimum** : Maksimaalne summa, mida see sõlmpunkt lubab ühe kanali kaudu läbida.



Vaadates selle Interface tabelit, leiate kogu selle teabe ka selle sõlme kohta, millele see on vastavuses.



![channels_info](assets/fr/07.webp)



Jaotises **Kanalite kaardid** näete selle sõlme erinevate kanalite jaotust ja läbilaskevõimet. Saate muuta kuvatavaid jaotuskriteeriume, valides ühe valiku paremal asuvast rippmenüüst.



![cha_maps](assets/fr/08.webp)



Jaotises **Lõpetatud kanalid** on rühmitatud kõik sõlme endised kanalid vastavalt sulgemise tüübile:




- Vastastikune sulgemine**: kujutab endast mõlema osapoole kokkulepet, kes kasutavad oma isiklikku võtit, et allkirjastada tehing, mis tähistab kanali sulgemist ja saldode jaotamist selles
- **Võimendatud sulgemine**: kujutab endast kanali ühe osa järsku, ühepoolset sulgemist. Seda tüüpi sulgemine ei ole soovitatav, sest Lightning Network on karistuspõhine protokoll: kui püüate kanali tasakaalu rikkuda, riskite kogu oma olemasoleva tasakaalu kaotamisega selles kanalis.



![closed](assets/fr/09.webp)



Hankige teavet transiiditasude kohta maksete suunamise eest kasutatava sõlme kanali kaudu



![fees](assets/fr/10.webp)



## Võrguteave



Amboss ei keskendu mitte ainult võrgu liikmete teabele, vaid ka võrgu enda olukorrale.



Jaotises **Statistika** leiate vasakpoolse menüü "Simulatsioonid" alt graafiku, mis näitab eduka makse tõenäosust sõltuvalt maksesummast.



Tegelikult märkate, et kõver väheneb, sest kui teie makse summa suureneb, siis on teil vähem võimalusi, et see makse läheb läbi. See peegeldab Lightning Network tegelikku likviidsusprobleemi. Näiteks teie 10_000 satelliidi suurusel maksel on 79% tõenäosus, et see tehakse. Teisest küljest, 3_000_000_000` satoshi suuruse makse puhul on teil vähem kui 13% tõenäosus õnnestumiseks.



![network](assets/fr/11.webp)



Menüü **Võrgustatistika** võimaldab graafiliselt kuvada statistikat :




- Maksekanalid
- Sõlmed
- Võimsus
- Tasud
- Kanali areng.



![network_stat](assets/fr/12.webp)



Menüüs **Turustatistika** võimaldab valik **Tellimuse üksikasjad** vaadata likviidsuse nõudlust Lightning Networks. See graafik võib näidata ka seda, milliste kanalite järele on kõige suurem nõudlus ja/või millised kanalid on märkimisväärse mahuga.



![markets](assets/fr/13.webp)




## Tööriistad



Amboss pakub mitmeid vahendeid, mis aitavad teil otsinguid ja tegevusi optimeerida.



### Lightning Network dekooder



See tööriist on peamiselt vastutav Lightning Invoice, Lightning Address või Lightning URL-i struktuuri üksikasjade esitamise eest.



Esitage avalehel jaotises **Tööriistad** näiteks oma Lightning Address.



![decoder](assets/fr/14.webp)



Sellest dekooderist saate sellist teavet nagu :




- teie Lightning Address-ga seotud sõlme avalik võti;
- Invoice kehtivusaeg teie Address-st;
- Minimaalne ja maksimaalne saadetav summa;
- Teie Address-ga seotud Nostr-sõlm, kui Nostr on selles sõlmes lubatud.



![decode](assets/fr/15.webp)



### Magma IA



Avastage Amboss'i uusim vahend, millega saate tõhusalt hallata oma ühendusi Lightning Network sõlmedega. Magma AI kasutab spetsiaalset tehisintellekti, et keskenduda olulisele probleemile: hea sõlmede valiku tegemine, millega ühendada.



![magma](assets/fr/16.webp)



### Satoshi kalkulaator



Uuri välja Bitcoin praegune hind kohalikus vääringus (EUR / USD). Kasutage koduleheküljel olevat satoshis-kalkulaatorit, et leida praegune turuhind.



![calculator](assets/fr/17.webp)




Nüüd olete teinud täieliku ringkäigu platvormi funktsioonide ja analüüsivahenditega. Allpool leiate meie artikli Bitcoin **Mempool.space** eksplorteri kohta.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f