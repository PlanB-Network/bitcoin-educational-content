---
name: BIP-39 Passphrase
description: Mõistmaks, kuidas paroolilause töötab
---
![cover](assets/cover.webp)

## Mis on BIP39 paroolilause?

HD rahakotid genereeritakse tavaliselt mnemoonilisest fraasist, mis koosneb 12 või 24 sõnast. See fraas on väga oluline, kuna see võimaldab kõigi rahakoti võtmete taastamist juhul, kui selle füüsiline kandja (näiteks riistvaraline rahakott) kaob. Siiski kujutab see endast ühtset rikkepunkti, sest kui see kompromiteeritakse, võib ründaja varastada kõik bitcoini.

![PASSPHRASE BIP39](assets/notext/01.webp)

Siin tulebki mängu paroolilause. See on valikuline salasõna, mille võite vabalt valida, mis lisatakse mnemoonilisele fraasile võtmete tuletamise protsessis, et suurendada rahakoti turvalisust.

![PASSPHRASE BIP39](assets/notext/02.webp)

Olge ettevaatlik, et mitte segi ajada paroolilauset oma riistvaralise rahakoti PIN-koodiga või parooliga, mida kasutate oma rahakotile arvutis juurdepääsu avamiseks. Erinevalt kõigist neist elementidest mängib paroolilause rolli teie rahakoti võtmete tuletamisel. **See tähendab, et ilma selleta ei saa te kunagi oma bitcoine taastada.**

Paroolilause töötab koos mnemoonilise fraasiga, muutes seemet, millest võtmed genereeritakse. Seega, isegi kui keegi saab kätte teie 12 või 24-sõnalise fraasi, ei saa nad ilma paroolilauseita teie vahenditele ligi. **Paroolilause kasutamine loob sisuliselt uue rahakoti eristuvate võtmetega. Paroolilause muutmine (isegi vähesel määral) genereerib erineva rahakoti.**

## Miks peaksite kasutama paroolilauset?

Paroolilause on suvaline ja võib olla kasutaja poolt valitud mis tahes tähemärkide kombinatsioon. Paroolilause kasutamine pakub seega mitmeid eeliseid. Esiteks vähendab see kõiki riske, mis on seotud mnemoonilise fraasi kompromiteerimisega, nõudes teist faktorit vahenditele juurdepääsuks (sissemurdmine, juurdepääs teie koju jne).

Järgmisena saab seda strateegiliselt kasutada petterahakoti loomiseks, et tegeleda füüsiliste piirangutega teie vahendite varastamisel, nagu kurikuulus "*5-dollarine mutrivõtmerünnak*". Selles stsenaariumis on idee omada rahakotti ilma paroolilauseita, mis sisaldab ainult väikest kogust bitcoine, piisavalt, et rahuldada potentsiaalset ründajat, samal ajal omades peidetud rahakotti. Viimane kasutab sama mnemoonilist fraasi, kuid on turvatud lisaparoolilausega.

Lõpuks on paroolilause kasutamine huvitav, kui soovitakse kontrollida HD rahakoti seemne genereerimise juhuslikkust.

## Kuidas valida hea paroolilause?
Et paroolilause oleks efektiivne, peab see olema piisavalt pikk ja juhuslik. Nagu tugeva parooli puhul, soovitan valida paroolilause, mis on võimalikult pikk ja juhuslik, sisaldades erinevaid tähti, numbreid ja sümboleid, et muuta mis tahes jõuga ründamine võimatuks.

[Trezori 2019. aasta uuringu](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) kohaselt võiks ründaja, kellel on ligipääs teie seemnfraasile ja kes kasutab AWS-is renditud tippklassi GPU-d (NVIDIA Tesla V100), testida 1 dollari eest ligi 620 miljonit parooli. Võrdluseks: 2019. aasta võimekuse juures maksaks 12 juhusliku väiketähega parooli murdmine keskmiselt **77 miljonit dollarit**.

Soovitan siiski mitte piirduda 12 tähemärgiga. Selle asemel püüdke järgida tugeva parooli praeguseid standardeid: 2025. aastal kasutage vähemalt 13 juhuslikku tähemärki, mis sisaldavad numbreid, väikeseid ja suuri tähti ning sümboleid; või 14 tähemärki, kui kasutate ainult väikeseid ja suuri tähti. Loomulikult soovitan minna veel kaugemale ja kasutada näiteks 20 tähemärgi pikkust pääsõna koos sümbolitega, et olla valmis tulevaste arengute jaoks ja arvestada inimlike riskidega, mida nendes uuringutes ei käsitleta.

On ka oluline korralikult salvestada see paroolilause, samamoodi nagu mnemoonilise fraasi puhul. **Selle kaotamine tähendab juurdepääsu kaotamist teie bitcoine'idele**. Ma soovitan tungivalt mitte jätta seda ainult oma peaga meelde, kuna see suurendab mõttetult kaotuse riski. Ideaalne on kirjutada see füüsilisele kandjale (paberile või metallile) eraldi mnemoonilisest fraasist. See varukoopia peab ilmselgelt olema hoitud erinevas kohas, kus teie mnemooniline fraas on, et vältida mõlema samaaegset kompromiteerimist.

## Õpetused

Paroolilause seadistamiseks Ledger seadmel (Stax, Flex või Nano), võite konsulteerida selle õpetusega:

https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

COLDCARD seadmel:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

Jade Plus seadmel:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Passport (batch-2) seadmel:

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Trezor-seadmel (Safe 3, Safe 5 või Model One):

https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

