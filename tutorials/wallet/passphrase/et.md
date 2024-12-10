---
name: BIP39 Paroolilause
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

On ka oluline korralikult salvestada see paroolilause, samamoodi nagu mnemoonilise fraasi puhul. **Selle kaotamine tähendab juurdepääsu kaotamist teie bitcoine'idele**. Ma soovitan tungivalt mitte jätta seda ainult oma peaga meelde, kuna see suurendab mõttetult kaotuse riski. Ideaalne on kirjutada see füüsilisele kandjale (paberile või metallile) eraldi mnemoonilisest fraasist. See varukoopia peab ilmselgelt olema hoitud erinevas kohas, kus teie mnemooniline fraas on, et vältida mõlema samaaegset kompromiteerimist.

## Õpetused

Paroolilause seadistamiseks Ledger seadmel (Stax, Flex või Nano), võite konsulteerida selle õpetusega:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49