---
name: Slipstream
description: Allkirjastatud tehingu saatmine otse kaevandajale Slipstreami abil, ilma seda Bitcoini võrku levitamata
---

![cover](assets/cover.webp)

Tavaliselt levitatakse tehing pärast allkirjastamist automaatselt kõikidele võrgus olevatele Bitcoini sõlmedele. Seejärel ootab see kaevandamist.

Kuni tehing ei ole aga plokis, võib teie privaatvõtme kätte saanud ründaja selle asendada ja vahendid varastada. Tüüpiliselt on see nii juhul, kui kasutate ColdCardi riistvaralist rahakotti.

Kaevandusettevõtte MARA tööriist Slipstream võimaldab tehingu võrku levitamisest mööda minna: tehing saadetakse otse (ja ainult) ühele kaevandajale, mis hoiab selle privaatsena ja väldib selle avalikustamist võrgus. Tõenäoliselt võtab tehingu kaevandamine kauem aega, kuid see on kaitstud asendusrünnaku eest.

Allpool pakume õpetust, mis võimaldab nii [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) kasutajatel kui ka [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) rahakoti kasutajatel kasutada kaevandaja MARA tööriista Slipstream lehe [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) kaudu.

⚠️ **Hoiatus**: see tööriist on mõeldud ainult teatud profiilidele, peamiselt Liana rahakottidele, Miniscripti rahakottidele ja mõnda tüüpi multisigidele. Wizardsardine **soovitab selle kasutamisest sõnaselgelt hoiduda** nende rahakottide puhul, mille vahendid on juba kriitilises vargusohus, näiteks nende puhul, mille taastefraas genereeriti juhuslike arvude generaatori haavatavusest mõjutatud ColdCardi seadmel. Sellises olukorras käib võidujooks ründajaga sekundite peale ning ühele ainsale kaevandajale saadetud tehingu kinnitamine võtab palju kauem aega kui tavapäraselt levitatud tehingul. Kui see puudutab teid, lugege kõigepealt meie sellele pühendatud õpetust:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Liana kasutajatele

Lianat haldab Wizardsardine, kes on lehe [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) väljaandja, mistõttu on tee otsene: teil tuleb lihtsalt eksportida allkirjastatud PSBT-fail selle asemel, et seda levitada.

*Eeldus: teie Liana rahakotil peavad olema vahendid.*

### 1. samm: Koostage oma tehing Lianaga

Nagu tavaliselt, koostage oma tehing, lisades sihtaadressi, kirjelduse ja summa (siin rahakotis saadaolev maksimum).

Tasumäära seadmiseks:

- valige mündid, mida soovite kulutada, klõpsates all vasakul asuvat väikest kastikest pealkirja "Coins selection" all;
- seejärel sisestage tasumäär. Pidage meeles seada tasud pakutud määrast tunduvalt kõrgemaks, nagu on kirjeldatud sellel lehel: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Lõpuks klõpsake nuppu "Next".

![Tehingu koostamine Lianas](assets/fr/01.webp)

### 2. samm: Kontrollige oma tehingu andmeid

Enne nupule "Sign" klõpsamist kontrollige oma tehingu andmeid, eelkõige:

- saadetavat summat;
- tehingutasudeks eraldatud satoshide arvu;
- kuid ennekõike aadressi, millele te vahendeid saadate (pidage meeles kontrollida aadressi 5/6 esimest märki, 5/6 viimast ning 5/6 märki aadressi keskelt, et vältida "aadressi mürgitamise" tüüpi rünnakuid).

![Tehingu andmete kontrollimine](assets/fr/02.webp)

### 3. samm: Valige allkirjastavad rahakotid

Seejärel valige tarkvaralised ja/või riistvaralised rahakotid, millega peate oma tehingu allkirjastama. Väike meeldetuletus: 2/2 multisig-rahakoti puhul on teil vaja 2 allkirja 2-st.

### 4. samm: Eksportige oma tehingu PSBT-fail

Bitcoini tehing on nüüd allkirjastatud sobivate võtmetega. Ärge klõpsake nuppu "Broadcast", vastasel juhul jagatakse seda kogu võrguga ja kui te kasutate ColdCardi riistvaralist rahakotti, jääb teie tehing avalikult nähtavaks ning teie vahendid on ohus.

Nüüd võite klõpsata nuppu "Export" ja seejärel salvestada PSBT-faili kohapeal oma arvutisse.

![PSBT-faili eksportimine Lianast](assets/fr/03.webp)

### 5. samm: Saatke tehing kaevandajale outofband.wizardsardine.com kaudu

Nüüd viimased sammud. Tehingu saatmiseks kaevandajale tuleb teil vaid võtta PSBT-fail ja lohistada see ettenähtud alale.

![PSBT-faili lohistamine lehele outofband.wizardsardine.com](assets/fr/04.webp)

Seejärel kuvatakse tehing nii, nagu allpool näidatud.

![Tehing järjekorras](assets/fr/05.webp)

### 6. samm: Saatke tehing Slipstreami kaudu

Lõpuks tuleb teil vaid klõpsata nuppu "Send", et tehing saadetaks Slipstreami kaudu MARA-le.

![Tehingu saatmine Slipstreami kaudu](assets/fr/06.webp)

Mõne sekundi jooksul muutub tehingu olek "Sending" olekuks "Accepted":

![Slipstreami poolt aktsepteeritud tehing](assets/fr/07.webp)

Jääb üle vaid kopeerida tehingu identifikaator (TXID) ja kleepida see lehele [mempool.space](https://mempool.space/), et jälgida selle kaevandamist:

![TXID otsimine lehel mempool.space](assets/fr/08.webp)

Pange tähele: tehingu juures kuvatakse "Transaction not found" seni, kuni kaevandaja MARA kaevandab ploki ja lisab sellesse teie tehingu. See võib võtta mitukümmend minutit või isegi tunde, sest MARA-le kuulub vaid umbes 4,5% Bitcoini võrgu räsivõimsusest. 4. augusti 2026 seisuga vastab see ligikaudu ühele kaevandatud plokile iga 3 tunni ja 45 minuti järel.

## Teiste rahakottide kasutajatele

Kui te ei kasuta rahakotti [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), kuid soovite tööriista siiski kasutada, siis siin on õpetus 2/2 multisig-rahakotiga. Selleks kasutame tarkvaralist rahakotti [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Eeldus: teie Sparrow rahakotil peavad olema vahendid.*

### 1. samm: Koostage oma tehing

Rahakotiga [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) koostage tehing oma multisig-rahakotis. Pidage meeles seada tasud pakutud määrast tunduvalt kõrgemaks, nagu on kirjeldatud sellel lehel: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Kui see on koostatud, klõpsake nuppu "Create Transaction".

![Tehingu loomine Sparrows](assets/fr/09.webp)

### 2. samm: Viige oma tehing lõpule

Tehingu lõpuleviimiseks tuleb see nüüd allkirjastada. Selleks klõpsake nuppu "Finalize Transaction for Signing".

![Tehingu lõpuleviimine allkirjastamiseks](assets/fr/10.webp)

### 3. samm: Allkirjastage oma tehing oma erinevate võtmetega

Nüüd on käes aeg tehing allkirjastada. Selleks piisab, kui allkirjastate selle tarkvaralis(t)e või riistvaralis(t)e rahakotti(de)ga, mida kasutate.

![Tehingu allkirjastamine multisigi võtmetega](assets/fr/11.webp)

### 4. samm: Laadige allkirjastatud tehing alla ja ärge levitage seda võrku

Bitcoini tehing on nüüd allkirjastatud meie 2/2 multisigi mõlema võtmega. Ärge klõpsake nuppu "Broadcast Transaction", vastasel juhul jagatakse seda kogu võrguga ja kui te kasutate ColdCardi riistvaralist rahakotti, jääb teie tehing avalikult nähtavaks ning teie vahendid on ohus.

![Allkirjastatud tehing, valmis, kuid levitamata](assets/fr/12.webp)

### 5. samm: Kuvage allkirjastatud tehingu skript või laadige alla PSBT-fail

Allkirjastatud Bitcoini tehingu kuvamiseks klõpsake nüüd nuppu "View Final Transaction". Seejärel saate kopeerida allkirjastatud Bitcoini tehingu skripti:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Allkirjastatud tehingu skripti kuvamine](assets/fr/13.webp)

Kui soovite tehingu faili alla laadida, saate kas:

- klõpsata "File" ja seejärel "Save transaction…";
- või klõpsata all paremal võrguühenduse nuppu (kollane nupp) ja seejärel klõpsata "Save Final Transaction".

Seejärel salvestatakse tehing kohapeal teie arvutisse.

![Lõpliku tehingu kohalik salvestamine](assets/fr/14.webp)

### 6. samm: Saatke tehing kaevandajale outofband.wizardsardine.com kaudu

Nüüd viimased sammud. Tehingu saatmiseks kaevandajale tuleb teil vaid:

- minna lehele [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- kleepida eelmises sammus kopeeritud allkirjastatud tehingu skript ja seejärel klõpsata allpool nuppu "ADD TO QUEUE";

![Tehingu skripti kleepimine tööriista](assets/fr/15.webp)

- või võtta fail ja lohistada see ettenähtud alale.

![Tehingufaili lohistamine tööriista](assets/fr/16.webp)

Seejärel kuvatakse tehing nii, nagu allpool näidatud.

![Tehing järjekorras](assets/fr/17.webp)

Kui teade annab teile teada, et teie tehingu sisendite satoshide kogusumma ei ole teada (ja et seetõttu ei saa tasude satoshide arvu arvutada), tuleb teil sisendite satoshide kogusumma lihtsalt käsitsi sisestada. Selle leidmiseks klõpsake lihtsalt oma tehingu kuvale Sparrows, skeemi keskel:

![Sisendite kogusumma Sparrows](assets/fr/18.webp)

Seejärel sisestage see summa (meie näites 15 904 satsi) tööriista [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Sisendite kogusumma käsitsi sisestamine](assets/fr/19.webp)

Lõpuks kontrollige, et tasumäär oleks õige.

### 7. samm: Saatke tehing Slipstreami kaudu

Lõpuks tuleb teil vaid klõpsata nuppu "Send", et tehing saadetaks Slipstreami kaudu MARA-le.

![Tehingu saatmine Slipstreami kaudu](assets/fr/20.webp)

Mõne sekundi jooksul muutub tehingu olek "Sending" olekuks "Accepted":

![Slipstreami poolt aktsepteeritud tehing](assets/fr/21.webp)

Jääb üle vaid kopeerida tehingu identifikaator (TXID) ja kleepida see lehele [mempool.space](https://mempool.space/), et jälgida selle kaevandamist:

![TXID otsimine lehel mempool.space](assets/fr/22.webp)

Pange tähele: tehingu juures kuvatakse "Transaction not found" seni, kuni kaevandaja MARA kaevandab ploki ja lisab sellesse teie tehingu. See võib võtta mitukümmend minutit või isegi tunde, sest MARA-le kuulub vaid umbes 4,5% Bitcoini võrgu räsivõimsusest. 4. augusti 2026 seisuga vastab see ligikaudu ühele kaevandatud plokile iga 3 tunni ja 45 minuti järel.
