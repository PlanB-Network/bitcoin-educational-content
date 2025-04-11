---
name: Whirlpool Stats Tools - Anonsets
description: Mõista anonset'i kontseptsiooni ja kuidas seda WST abil arvutada
---
![kaas](assets/cover.webp)

***HOIATUS:** Pärast Samourai Wallet'i asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil ei ole Whirlpooli statistikatööriist enam allalaadimiseks saadaval, kuna see oli majutatud Samourai Gitlabis. Isegi kui olete selle tööriista varem oma masinasse kohalikult alla laadinud või see oli installitud teie RoninDojo sõlme, ei toimi WST praegu. Selle töövõime sõltus OXT.me poolt pakutavatest andmetest ja see sait ei ole enam kättesaadav. Praegu ei ole WST eriti kasulik, kuna Whirlpooli protokoll on mitteaktiivne. Siiski on võimalik, et need tarkvarad võidakse järgnevate nädalate jooksul taas kasutusele võtta. Lisaks jääb selle artikli teoreetiline osa asjakohaseks mõistmaks üldiselt coinjoinide põhimõtteid ja eesmärke (mitte ainult Whirlpooli), samuti Whirlpooli mudeli efektiivsuse mõistmiseks. Samuti saate õppida, kuidas kvantifitseerida coinjoin tsüklite poolt pakutavat privaatsust.*

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Kinnitame, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

*"Katkesta jäljed, mida sinu mündid maha jätavad"*

Selles õpetuses uurime anonsetide kontseptsiooni, indikaatoreid, mis võimaldavad meil hinnata coinjoin protsessi kvaliteeti Whirlpoolis. Käsitleme nende indikaatorite arvutamise meetodit ja tõlgendamist. Teoreetilise osa järel liigume praktikale, õppides arvutama konkreetse tehingu anonsete Pythoni tööriista *Whirlpooli statistikatööriistade* (WST) abil.

## Mis on coinjoin Bitcoinis?
**Coinjoin on tehnika, mis katkestab bitcoinide jälgitavuse blockchainis**. See põhineb koostööl põhineval tehingul, millel on sama nimega spetsiifiline struktuur: coinjoin tehing.

Coinjoin tehingud suurendavad Bitcoin kasutajate privaatsust, muutes välisvaatlejate jaoks ahela analüüsi keerulisemaks. Nende struktuur võimaldab ühendada mitme kasutaja mündid üheks tehinguks, varjates seeläbi radu ja muutes sisend- ja väljundiaadresside vaheliste seoste kindlakstegemise keeruliseks.

Coinjoini põhimõte põhineb koostööl: mitu kasutajat, kes soovivad oma bitcoine segada, panevad samaväärsed summad sama tehingu sisenditena. Need summad jaotatakse seejärel väljundites võrdse väärtusega. Tehingu lõppedes muutub võimatuks seostada konkreetset väljundit kindla kasutajaga. Sisendite ja väljundite vahel puudub otsene seos, katkestades seeläbi seose kasutajate ja nende UTXO vahel, samuti iga mündi ajaloo.

![coinjoin](assets/notext/1.webp)

Näide coinjoin tehingust:
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)
Selleks, et teostada coinjoin, tagades samal ajal, et iga kasutaja hoiab oma vahendeid alati kontrolli all, algab protsess tehingu koostamisega koordinaatori poolt, kes seejärel edastab selle igale osalejale. Iga kasutaja allkirjastab tehingu pärast selle sobivuse kontrollimist. Kõik kogutud allkirjad integreeritakse lõpuks tehingusse. Kui kasutaja või koordinaator üritab vahendeid ümber suunata, muutes coinjoin tehingu väljundeid, muutuvad allkirjad kehtetuks, mis viib tehingu tagasilükkamiseni sõlmede poolt.
Coinjoin'i rakendusi on mitmeid, nagu Whirlpool, JoinMarket või Wabisabi, millest igaüks püüab hallata koordineerimist osalejate vahel ja suurendada coinjoin tehingute tõhusust.
Selles õpetuses keskendume minu lemmikrakendusele: Whirlpool, mis on saadaval Samourai Walletis ja Sparrow Walletis. Minu arvates on see kõige tõhusam rakendus coinjoinide jaoks Bitcoinil.
## Mis on coinjoin'i kasulikkus Bitcoinil?
Coinjoin'i kasulikkus seisneb selles, et see võimaldab luua usutava eitamise, uputades teie mündi gruppi eristamatute müntide hulka. Selle tegevuse eesmärk on katkestada jälgitavuse lingid, nii minevikust olevikku kui ka olevikust minevikku.

Teisisõnu, analüütik, kes teab teie algset tehingut coinjoin tsüklite sissepääsul, ei tohiks suuta kindlalt tuvastada teie UTXO-d tsüklite väljapääsul (analüüs tsükli sissepääsust tsükli väljapääsuni).

![coinjoin](assets/en/2.webp)

Vastupidi, analüütik, kes teab teie UTXO-d coinjoin tsüklite väljapääsul, ei tohiks suuta kindlaks teha algset tehingut tsüklite sissepääsul (analüüs tsükli väljapääsust tsükli sissepääsuni).

![coinjoin](assets/en/3.webp)

Selleks, et hinnata analüütiku raskust mineviku ja oleviku ning vastupidi seostamisel, on vajalik kvantifitseerida gruppe, mille sees teie münt on peidetud. See mõõt annab meile analüüside arvu, millel on identne tõenäosus. Seega, kui õige analüüs on uputatud 3 teise võrdse tõenäosusega analüüsi hulka, on teie varjatus väga madal. Teisest küljest, kui õige analüüs on 20 000 võrdselt tõenäolise analüüsi hulgas, on teie münt väga hästi peidetud.

Ja täpselt, nende gruppide suurused esindavad indikaatoreid, mida nimetatakse "anonsetideks".

## Anonsettide mõistmine
Anonsetid toimivad indikaatoritena, et hinnata konkreetse UTXO privaatsuse astet. Täpsemalt mõõdavad nad eristamatute UTXO-de arvu komplektis, mis sisaldab uuritavat münti. Homogeense UTXO komplekti nõue tähendab, et anonsetid arvutatakse tavaliselt coinjoin tsüklite üle. Nende indikaatorite kasutamine on eriti asjakohane Whirlpool coinjoinide puhul nende ühtluse tõttu.

Anonsetid võimaldavad, kui see on asjakohane, hinnata coinjoinide kvaliteeti. Suur anonseti suurus tähendab suuremat anonüümsuse taset, kuna konkreetse UTXO eristamine komplektis muutub keeruliseks.

On kahte tüüpi anonsete:
- **Tuleviku anonüümsuse komplekt;**
- **Tagasivaate anonüümsuse komplekt.**
Esimene indikaator näitab grupi suurust, mille hulgas uuritav UTXO tsükli lõpus peidus on, teades UTXO-d sissepääsul, see tähendab, selle grupi sees olevate eristamatute müntide arvu. See indikaator võimaldab mõõta mündi konfidentsiaalsuse vastupanuvõimet analüüsile minevikust olevikku (sissepääsust väljapääsuni). Inglise keeles nimetatakse seda indikaatorit "forward anonset" või "forward-looking metrics".
![coinjoin](assets/en/4.webp)
See mõõdik hindab, mil määral on teie UTXO kaitstud katsete eest taastada selle ajalugu alates sisenemispunktist kuni väljumispunktini coinjoin protsessis.

Näiteks, kui teie tehing osales esimeses coinjoin tsüklis ja kaks järglastsüklit olid lõpetatud, oleks teie mündi eeldatav anonüümsete osalejate hulk `13`:

![coinjoin](assets/en/5.webp)

Teine näitaja näitab antud mündi võimalike allikate arvu, teades UTXO-d tsükli lõpus. See näitaja mõõdab mündi konfidentsiaalsuse vastupanuvõimet analüüsile praegusest minevikku (väljumisest sisenemiseni), st kui raske on analüütikul jälitada tagasi teie mündi päritolu enne coinjoin tsükleid. Inglise keeles nimetatakse seda näitajat "*backward anonset*" või "*backward-looking metrics*".

![coinjoin](assets/en/6.webp)

Teie UTXO teades tsüklite väljumisel, määrab tagasivaatav anonüümsete osalejate hulk potentsiaalsete Tx0 tehingute arvu, mis võisid moodustada teie sisenemise coinjoin tsüklitesse. Allpool olevas diagrammis vastab see kõigi oranžide mullide summale.

![coinjoin](assets/en/7.webp)

## Anonüümsete osalejate hulga arvutamine Whirlpool Stats Tools (WST) abil
Oma mündid, mis on läbinud coinjoin tsükleid, nende näitajate iseseisvaks arvutamiseks võite kasutada spetsiaalselt Samourai Wallet poolt välja töötatud tööriista: *Whirlpool Stats Tools*.

Kui teil on RoninDojo, on WST teie sõlmes eelinstalleeritud. Seega võite installimise sammud vahele jätta ja otse kasutamise juurde asuda. Neile, kellel ei ole RoninDojo sõlme, vaatame, kuidas edasi minna selle tööriista installimisega arvutisse.

Teil on vaja: Tor Browser (või Tor), Python 3.4.4 või uuem, git ja pip. Avage terminal. Nende tarkvarade olemasolu ja versiooni kontrollimiseks süsteemis sisestage järgmised käsud:
```plaintext
python --version
git --version
pip --version
```

Vajadusel saate need alla laadida nende vastavatelt veebilehtedelt:
- https://www.python.org/downloads/ (pip tuleb otse koos Pythoniga alates versioonist 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.
Kui kõik need tarkvarad on installeeritud, kloonige terminalist WST repositoorium:
```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```

![WST](assets/notext/8.webp)

Liikuge WST kataloogi:
```plaintext
cd whirlpool_stats
```

Installeerige sõltuvused:
```plaintext
pip3 install -r ./requirements.txt
```

![WST](assets/notext/9.webp)

Võite need ka käsitsi installeerida (valikuline):
```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

Liikuge `/whirlpool_stats` alamkataloogi:
```plaintext
cd whirlpool_stats
```

Käivitage WST:
```plaintext
python3 wst.py
```

![WST](assets/notext/10.webp)

Käivitage Tor või Tor Browser taustal.

**-> RoninDojo kasutajad, võite juhendi juurde otse siit jätkata.**

Seadistage proxy Tor'i jaoks (RoninDojo),
```plaintext
socks5 127.0.0.1:9050
```
või Tor Browser'ile, olenevalt sellest, mida kasutate:
```plaintext
socks5 127.0.0.1:9150
```

See manipulatsioon võimaldab teil OXT kaudu andmeid alla laadida Tori kaudu, et mitte lekitada teavet oma tehingute kohta. Kui olete algaja ja see samm tundub keeruline, siis teadke, et see hõlmab lihtsalt teie internetiliikluse suunamist Tori kaudu. Kõige lihtsam meetod seisneb Tor Browser'i taustal arvutis käivitamises, seejärel ainult teise käsu täitmisel, et ühenduda selle brauseri kaudu (`socks5 127.0.0.1:9150`).

![WST](assets/notext/11.webp)

Seejärel navigeerige töökataloogi, millest kavatsete WST andmeid alla laadida, kasutades käsku `workdir`. See kaust hakkab hoidma tehingute andmeid, mille te OXT-st `.csv` failide kujul alla laadite. See teave on oluline teie poolt soovitud näitajate arvutamiseks. Teil on vabadus valida selle kataloogi asukoht. Tark võib olla luua kaust spetsiaalselt WST andmete jaoks. Näiteks valime allalaadimiste kausta. Kui kasutate RoninDojo, siis see samm pole vajalik:
```plaintext
workdir path/to/your/directory
```

Käsurea viip peaks seejärel muutuma, et näidata teie töökataloogi.

![WST](assets/notext/12.webp)

Seejärel laadige alla andmed basseinist, mis sisaldab teie tehingut. Näiteks, kui ma olen `100,000 sats` basseinis, on käsk:
```plaintext
download 0001
```

![WST](assets/notext/13.webp)

WST-s on nimetuskoodid järgmised:
- Bassein 0.5 bitcoini: `05`
- Bassein 0.05 bitcoini: `005`
- Bassein 0.01 bitcoini: `001`
- Bassein 0.001 bitcoini: `0001`
Kui andmed on alla laaditud, laadige need. Näiteks, kui ma olen basseinis `100,000 sats`, on käsk:
```plaintext
load 0001
```

See samm võtab mõne minuti, olenevalt teie arvutist. Nüüd on hea aeg endale kohvi teha! :)

![WST](assets/notext/14.webp)

Pärast andmete laadimist tippige käsk `score`, millele järgneb teie TXID (tehingu identifikaator), et saada selle anonüümsete osalejate arv:
```plaintext
score TXID
```

**Tähelepanu**, TXID valik varieerub sõltuvalt anonüümsete osalejate arvust, mida soovite arvutada. Et hinnata mündi tuleviku anonüümsete osalejate arvu, on vajalik sisestada `score` käsu kaudu TXID, mis vastab selle esimesele coinjoin'ile, mis on esimene segamine, mida selle UTXO-ga tehti. Teisest küljest, et määrata tagasivaatav anonüümsete osalejate arv, peate sisestama TXID viimasest tehtud coinjoin'ist. Kokkuvõttes arvutatakse tuleviku anonüümsete osalejate arv esimese segamise TXID-st, samal ajal kui tagasivaatav anonüümsete osalejate arv arvutatakse viimase segamise TXID-st.

WST seejärel kuvab tagasivaatava skoori (*Tagasivaatavad mõõdikud*) ja tuleviku skoori (*Edasivaatavad mõõdikud*). Näiteks võtsin ma TXID juhuslikust mündist Whirlpoolis, mis ei kuulu mulle.

![WST](assets/notext/15.webp)
Käesolev tehing: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)
Kui me käsitame seda tehingut kui esimest coinjoin'i teostust antud mündi jaoks, siis saab see kasu potentsiaalsest anonüümsuskomplektist `86,871`. See tähendab, et see on peidetud `86,871` eristamatu mündi hulka. Väline vaatleja, kes tunneb seda münti coinjoin'i tsüklite alguses ja üritab selle väljundit jälitada, seisab silmitsi `86,871` võimaliku UTXO-ga, millest igaühel on identne tõenäosus olla otsitav münt.

Kui me käsitame seda tehingut kui mündi viimast coinjoin'i, siis on sellel tagasiulatuvalt anonüümsuskomplekt `42,185`. See tähendab, et on `42,185` potentsiaalset allikat sellele UTXO-le. Kui väline vaatleja tuvastab selle mündi tsüklite lõpus ja soovib selle päritolu jälitada, seisab ta silmitsi `42,185` võimaliku allikaga, kõigil võrdne tõenäosus olla otsitav päritolu.
Lisaks anonüümsuskomplekti skooridele pakub WST teile ka teie väljundi difusioonimäära basseinis, lähtudes anonüümsuskomplektist. See teine näitaja lihtsalt võimaldab teil hinnata oma tüki parendamise potentsiaali. See määr on eriti kasulik potentsiaalse anonüümsuskomplekti jaoks. Tõepoolest, kui teie tükil on difusioonimäär 15%, tähendab see, et see võib segi minna basseini 15% tükkidega. See on hea, kuid teil on siiski suur arenguruum, jätkates remiximist. Teisest küljest, kui teie tükil on difusioonimäär 95%, siis läheneb see basseini piiridele. Võite jätkata remiximist, kuid teie anonüümsuskomplekt ei suurene palju.

On oluline märkida, et WST poolt arvutatud anonüümsuskomplektid ei ole täiesti täpsed. Arvestades töödeldavate andmete tohutut mahtu, kasutab WST *HyperLogLogPlusPlus* algoritmi, et oluliselt vähendada kohaliku andmetöötlusega seotud koormust ja vajalikku mälu. See on algoritm, mis võimaldab hinnata eristatavate väärtuste arvu väga suurtes andmekogumites, säilitades samal ajal kõrge täpsuse tulemuses. Seega on pakutud skoorid piisavalt head, et neid oma analüüsides kasutada, kuna need on väga lähedased hinnangud tegelikkusele, kuid neid ei tohiks tõlgendada täpsete ühikväärtustena.

Kokkuvõttes pidage meeles, et teie tükkide anonüümsuskomplektide süstemaatiline arvutamine coinjoin'ides ei ole hädavajalik. Whirlpooli disain ise pakub juba garantiisid. Tõepoolest, tagasiulatuva anonüümsuskomplekti pärast muretsemine on harva vajalik. Alates teie esialgsest segamisest saate eriti kõrge tagasiulatuva skoori tänu varasemate segamiste pärandile alates Genesis coinjoin'ist. Mis puutub potentsiaalsesse anonüümsuskomplekti, siis piisab, kui hoida teie tükki post-mix kontol piisavalt kaua.
See on põhjus, miks ma pean Whirlpooli kasutamist eriti oluliseks *Hodl -> Mix -> Spend -> Replace* strateegias. Minu arvates on kõige loogilisem lähenemine hoida suurem osa oma bitcoini säästudest külmas rahakotis, samal ajal pidevalt säilitades teatud arvu münte coinjoinides Samourai's, et katta igapäevaseid kulusid. Kui coinjoinidest pärit bitcoine on kulutatud, asendatakse need uutega, et naasta määratletud segatud tükkide lävele. See meetod võimaldab vabaneda meie UTXO anonüümsete komplektide pärast muretsemisest, samal ajal muutes coinjoinide efektiivsuseks vajaliku aja palju vähem piiravaks.
**Välised Ressursid:**

- [Podcast prantsuse keeles ahela analüüsist](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Wikipedia artikkel HyperLogLog kohta](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourai repositoorium Whirlpooli statistika jaoks
- Whirlpooli veebileht Samourai poolt
- [Mediumi artikkel inglise keeles privaatsusest ja Bitcoinist Samourai poolt](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Mediumi artikkel inglise keeles anonüümsuse komplekti kontseptsioonist Samourai poolt](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)