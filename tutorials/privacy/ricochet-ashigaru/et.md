---
name: Ricochet
description: Ricochet tehingute mõistmine ja kasutamine
---
![cover ricochet](assets/cover.webp)

***HOIATUS:** Pärast Samourai Wallet'i asutajate arreteerimist ja nende serverite konfiskeerimist 24. aprillil ei ole Ricochet tööriist enam saadaval. Siiski on võimalik, et see tööriist taastatakse tulevastel nädalatel. Vahepeal saate Ricochet'i teha ainult käsitsi. Selle artikli teoreetiline osa jääb oluliseks, et mõista selle toimimist ja õppida, kuidas seda käsitsi teha.*

_Jälgime selle juhtumi arenguid ning sellega seotud tööriistade arenguid tähelepanelikult. Kinnitame, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

> *"Premium tööriist, mis lisab teie tehingule lisahüppeid ajaloos. Hämmasta musti nimekirju ja aita kaitsta end ebaõiglaste kolmandate osapoolte konto sulgemiste eest."*

## Mis on Ricochet?
Ricochet on tehnika, mis hõlmab mitme fiktiivse tehingu sooritamist iseendale, et simuleerida bitcoini omandiõiguse ülekandmist. See tööriist erineb teistest Samourai tehingutest, kuna see ei paku potentsiaalset anonüümsust, vaid pigem tagasiulatuvat anonüümsust. Ricochet aitab hägustada spetsiifikaid, mis võiksid ohustada Bitcoini mündi fungibilisust.

Näiteks, kui teete coinjoin'i, siis teie mündi väljund segust tuvastatakse sellisena. Ahela analüüsi tööriistad suudavad tuvastada coinjoin tehingute mustreid ja märgistada mündid, mis neist väljuvad. Tõepoolest, coinjoin'i eesmärk on murda mündi ajaloolised seosed, kuid selle läbimine coinjoin'ide kaudu on tuvastatav. Analoogiana võib tuua näite teksti krüpteerimisest: kuigi me ei pääse ligi algsele lihttekstile, on lihtne tuvastada, et on rakendatud krüpteerimist.

Täpsemalt, see "coinjoin väljundi mündi" silt võib mõjutada UTXO fungibilisust. Reguleeritud asutused, nagu vahetusplatvormid, võivad keelduda UTXO vastuvõtmisest, mis on läbinud coinjoin'i, või isegi nõuda selle omanikult selgitusi, riskiga, et nende konto blokeeritakse või vahendid külmutatakse. Mõnel juhul võib platvorm isegi teatada teie käitumisest riigiasutustele.

Siin tuleb mängu Ricochet meetod. Et hägustada coinjoin'i jäetud jalajälge, sooritab Ricochet neli järjestikust tehingut, kus kasutaja kannab oma vahendid endale erinevatele aadressidele. Pärast seda tehingute jada suunab Ricochet tööriist lõpuks bitcoini nende lõppsihtkohta, näiteks vahetusplatvormile. Eesmärk on luua distantsi algse coinjoin tehingu ja lõpliku kulutamise teo vahel. Sel viisil arvavad ahela analüüsi tööriistad, et pärast coinjoin'i on tõenäoliselt toimunud omandiõiguse ülekanne, ja seetõttu pole vaja saatja vastu meetmeid võtta.
![ricochet diagram](assets/en/1.webp)
Ricochet meetodi ees seistes võiks arvata, et ahelaanalüüsi tarkvara süvendaks oma uurimist rohkem kui nelja hüppe taha. Siiski seisavad need platvormid dilemma ees, kuidas optimeerida tuvastamise läve. Nad peavad kehtestama piiri hüpete arvule, pärast mida nad tunnistavad, et tõenäoliselt on toimunud omandiõiguse muutus ja et eelneva coinjoin'iga seos tuleks eirata. Kuid selle läve määramine on riskantne: vaadeldavate hüpete arvu iga laiendamine suurendab eksponentsiaalselt valepositiivsete juhtumite mahtu, st isikuid, kes on ekslikult märgitud coinjoin'is osalejateks, kuigi operatsiooni tegelikult sooritas keegi teine. See stsenaarium kujutab neile ettevõtetele suurt riski, kuna valepositiivsed juhtumid põhjustavad rahulolematust, mis võib mõjutada kliente konkurentide juurde pöörduma. Pikas perspektiivis viib liiga ambitsioonikas lävi platvormi olukorda, kus ta kaotab rohkem kliente kui tema konkurendid, mis võib ohustada selle elujõulisust. Seega on nende platvormide jaoks keeruline suurendada vaadeldavate hüpete arvu ja 4 on sageli piisav arv, et nende analüüse tõrjuda.
Seega, **kõige tavalisem kasutusjuht Ricochet'i puhul tekib siis, kui on vajalik varjata eelnevat osalemist coinjoin'is UTXO puhul, mis kuulub teile**. Ideaalis on parim vältida bitcoini ülekandmist, mis on läbinud coinjoin'i, reguleeritud asutustele. Siiski, juhul kui muud võimalust pole, eriti kiireloomulisuse korral bitcoini fiat-valuutaks muutmiseks, pakub Ricochet efektiivset lahendust.

## Kuidas Ricochet töötab Samourai Wallet'is?
Ricochet on lihtsalt meetod, kus saadetakse bitcoine iseendale. Seega on täiesti võimalik Ricochet'i manuaalselt simuleerida ilma spetsialiseeritud tööriista kasutamata. Siiski, neile, kes soovivad protsessi automatiseerida, samal ajal saades kasu viimistletumast tulemusest, on Ricochet tööriist, mis on kättesaadav läbi Samourai Wallet rakenduse, hea lahendus.

Kuna teenus on Samourai's tasuline, kaasneb Ricochet'iga teenustasu `100,000 sats`, lisaks kaevandamistasud. Seega on selle kasutamine soovitatav suuremate summade ülekandmiseks.

Samourai rakendus pakub kahte Ricochet'i varianti:
- Tugevdatud Ricochet ehk "astmeline kohaletoimetamine" pakub eelist levitada Samourai teenustasusid viie järjestikuse tehingu vahel. See valik tagab ka, et iga tehing edastatakse erineval ajal ja salvestatakse erinevasse plokki, mis jäljendab tihedalt omandiõiguse muutumise käitumist. Kuigi aeglasem, on see meetod eelistatav neile, kes ei kiirusta, kuna see maksimeerib Ricochet'i efektiivsust, suurendades selle vastupanu ahelaanalüüsile.
- Klassikaline Ricochet, mis on mõeldud operatsiooni kiireks sooritamiseks, edastades kõik tehingud vähendatud ajavahemiku jooksul. See meetod pakub seega vähem privaatsust ja madalamat vastupanu analüüsile võrreldes tugevdatud meetodiga. Seda tuleks eelistada ainult kiireloomuliste ülekannete puhul.

## Kuidas sooritada Ricochet tehingut Samourai Wallet'is?
Ricochet tehingu sooritamiseks Samourai Wallet rakendusest, järgige meie videoõpetust:
![Ricochet YouTube videoõpetus](https://youtu.be/Gsz0zuVo3N4)

Kui soovite uurida selles õpetuses sooritatud Ricochet tehinguid, siin need on:
- Esimene Ricochet tehing: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://mempool.space/fr/testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Viimane Ricochet tehing: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://mempool.space/fr/testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)
**Välised Ressursid:**
- https://docs.samourai.io/en/wallet/features/ricochet