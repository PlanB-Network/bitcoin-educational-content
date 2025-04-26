---
name: Remix - Whirlpool
description: Mitu korda peaks Whirlpoolis remixe tegema?
---
![kaane remix- wp](assets/cover.webp)

***HOIATUS:** Pärast Samourai Walleti asutajate vahistamist ja nende serverite konfiskeerimist 24. aprillil ei ole Whirlpooli statistikatööriist enam allalaadimiseks saadaval, kuna see oli majutatud Samourai Gitlabis. Isegi kui olete selle tööriista varem oma masinasse kohalikult alla laadinud või see oli paigaldatud teie RoninDojo sõlme, ei toimi WST praegu. See sõltus oma tööks OXT.me poolt pakutavatest andmetest ja see sait ei ole enam kättesaadav. Praegu ei ole WST eriti kasulik, kuna Whirlpooli protokoll on mitteaktiivne. Siiski on võimalik, et need tarkvarad võidakse järgnevate nädalate jooksul taaskehtestada. Lisaks jääb selle artikli teoreetiline osa asjakohaseks mõistmaks üldiselt coinjoins'i põhimõtteid ja eesmärke (mitte ainult Whirlpooli), samuti Whirlpooli mudeli tõhusust. Samuti saate õppida, kuidas kvantifitseerida coinjoin tsüklite poolt pakutavat privaatsust.*

_Jälgime selle juhtumi arenguid ning seotud tööriistade arenguid tähelepanelikult. Kinnitame, et uuendame seda õpetust, kui saabub uut teavet._

_Seda õpetust pakutakse ainult hariduslikel ja informatiivsetel eesmärkidel. Me ei toeta ega julgusta nende tööriistade kasutamist kuritegelikel eesmärkidel. Iga kasutaja vastutab oma jurisdiktsiooni seadustega kooskõlas olemise eest._

---

> *"Katkesta link, mille sinu mündid maha jätavad"*

See on küsimus, mida mulle tihti esitatakse. **Kui teete Whirlpoolis coinjoins'e, mitu korda peaks remixe tegema, et saavutada rahuldavaid tulemusi?**

Coinjoin'i eesmärk on pakkuda usutavat eitamist, segades teie mündi grupiga eristamatutest müntidest. Selle tegevuse eesmärk on katkestada jälgitavuse lingid, nii minevikust olevikku kui ka olevikust minevikku. Teisisõnu, analüütik, kes teab teie algset tehingut coinjoin tsüklite sisenemisel, ei tohiks suuta kindlalt tuvastada teie UTXO-d remix tsüklite väljumisel (analüüs sisenemistsüklitest väljumistsükliteni).
![minevik-olevik lingid diagramm](assets/en/1.webp)

Vastupidi, analüütik, kes teab teie UTXO-d coinjoin tsüklite väljumisel, ei tohiks suuta kindlaks teha algset tehingut tsüklite sisenemisel (analüüs väljumistsüklitest sisenemistsükliteni).
![olevik-minevik lingid diagramm](assets/en/2.webp)
Siiski ei ole remixide arv usaldusväärne kriteerium analüütiku raskuste hindamiseks seoste loomisel mineviku ja oleviku vahel või vastupidi. Asjakohasem näitaja oleks gruppide suurus, milles teie münt peidus on. Neid näitajaid nimetatakse "anonsetideks". Whirlpooli puhul on anonsete kahte tüüpi.

Esiteks, me saame määrata grupi suuruse, kus teie UTXO on peidus coinjoin tsüklite väljumisel, st ehk eristamatute müntide arvu selles grupis.
![tõenäolised UTXO-d väljumisel](assets/en/3.webp)
See näitaja, mida prantsuse keeles nimetatakse "prospective anonset", inglise keeles "forward anonset" või "forward-looking metrics", võimaldab meil hinnata teie mündi vastupanuvõimet analüüsidele, mis jälgivad selle teekonda coinjoin tsüklite sisenemisest väljumiseni. See mõõdik hindab ulatust, mil määral teie UTXO on kaitstud katsete eest taastada selle ajalugu alates sisenemispunktist kuni väljumispunktini coinjoin protsessis. Näiteks, kui teie tehing osales esimeses coinjoin tsüklis ja seejärel viidi läbi kaks täiendavat allavoolu tsüklit, oleks teie mündi prospective anonset `13`: ![forward anonset](assets/en/4.webp)
Teiseks, teine näitaja on arvutatav, et hinnata teie tüki vastupanuvõimet analüüsile olevikust minevikku. Teades teie UTXO-d tsüklite lõpus, määrab see näitaja potentsiaalsete Tx0 tehingute arvu, mis oleksid võinud moodustada teie sisendi coinjoin tsüklites (analüüs tsüklite lõpust alguseni). See näitaja mõõdab, kui keeruline on analüütikul jälitada teie tüki päritolu pärast selle läbimist coinjoins'ist. ![Probable sources at input](assets/en/5.webp)
Selle näitaja nimi on "backward anonset" või "backward-looking metrics". Prantsuse keeles meeldib mulle seda nimetada "anonset rétrospectif". Allpool olevas diagrammis vastab see kõigile oranžidele Tx0 mullidele:
![backward anonset](assets/en/6.webp)
Nende näitajate arvutusmeetodi kohta lisateabe saamiseks soovitan lugeda [minu Twitteri lõime](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) sellel teemal. Samuti valmistame ette põhjalikumat artiklit PlanB võrgustiku kohta.

Ma tean, et antud vastus võib tunduda ebapiisav, kuna lootsite saada konkreetset arvu remixe, ja suunan teid dokumentatsiooni juurde. Põhjus selleks on, et remixide arv on ebausaldusväärne näitaja anonüümsuse hindamiseks coinjoin tsüklites. Seetõttu ei ole võimalik määratleda kindlat arvu remixe kui absoluutset ja universaalset turvalisuse läve.

On tõsi, et iga teie tüki lisaremix suurendab selle anonüümsuskomplekte. Siiski on oluline mõista, et peamiselt on just teie eakaaslaste tehtud remixid, mis aitavad kasvatada teie prospective anonset'i. Whirlpooli mudeliga võib teie tehing saavutada märkimisväärseid prospective anonset'i tasemeid vaid kahe või kolme coinjoin tsükliga, ainult tänu eelnevates coinjoins'ides osalenud eakaaslaste tegevusele.

Retrospective anonset, teisest küljest, ei ole meie juhul mure. Tegelikult, alates teie esimesest coinjoinist, saate kasu eelnevate basseini tehingute pärandist, andes kohe teie tükile kõrge backward anonset'i, marginaalse suurenemisega igas järgnevas tsüklis.
On oluline mõista, et usutava eitamise loomine ei ole kunagi lõplik. See sõltub teie mündi jälitamise tõenäosusest. See tõenäosus väheneb, kui suureneb rühmade suurus, mis seda varjavad. Seetõttu peaksite oma eesmärke anonüümsuskomplektide osas kohandama vastavalt oma isiklikele ootustele. Küsige endalt, millised põhjused viivad teid coinjoins'i kasutamiseni ja milliseid anonüümsuse tasemeid on vaja nende eesmärkide saavutamiseks. Näiteks, kui coinjoins'i kasutamine on suunatud lihtsalt teie rahakoti privaatsuse säilitamisele, saates mõned satsid oma ristilapsele sünnipäevaks, ei ole väga kõrged anonüümsuse tasemed vajalikud. Teie ristilaps tõenäoliselt ei suuda teostada süvitsi ahela analüüsi ja isegi kui suudaks, ei oleks tagajärjed teie elule katastroofilised. Siiski, kui te olete autoritaarse režiimi sihtmärk, kus väikseimgi informatsioonitükk võib kaasa tuua vangistuse, peavad teie tegevusi juhtima palju rangemad kriteeriumid.
Nende kuulsate anonüümsuskomplektide näitajate määramiseks võite kasutada Pythoni tööriista nimega **WST** (Whirlpool Stats Tool).

Siiski ei ole alati vajalik arvutada iga teie coinjoined mündi anonüümsuskomplekte. Whirlpooli disain ise juba annab teile garantiid. Nagu varem mainitud, ei ole tagasiulatuva anonüümsuskomplekti pärast harva muret. Alates teie esialgsest segamisest saate juba eriti kõrge tagasiulatuva skoori. Mis puutub tulevikku suunatud anonüümsuskomplekti, siis peate lihtsalt hoidma oma münti post-mix kontol piisavalt kaua. Näiteks siin on ühe minu `100,000 sats` mündi anonüümsuskomplektide skoorid pärast kahte kuud coinjoin basseinis:
![WST anonüümsuskomplektid](assets/en/7.webp)
See näitab tagasiulatuva skoori `34,593` ja tulevikku suunatud skoori `45,202`. Konkreetselt tähendab see kahte asja:
- Kui analüütik teab minu münti tsüklite lõpus ja üritab selle päritolu jälitada, kohtab ta `34,593` potentsiaalset allikat, igaüks võrdse tõenäosusega olla minu oma.
- Kui analüütik teab minu münti tsüklite alguses ja üritab kindlaks teha selle vastavust lõpus, seisab ta silmitsi `45,202` võimaliku UTXO-ga, igaüks sama tõenäosusega olla minu oma.
Seetõttu pean Whirlpooli kasutamist eriti asjakohaseks strateegias `Hodl -> Mix -> Spend -> Replace`. Minu arvates on kõige loogilisem lähenemine hoida enamus oma säästudest bitcoinides külmas rahakotis, samal ajal pidevalt säilitades teatud arvu münte coinjoinis Samourai's, et katta igapäevaseid kulusid. Kui coinjoins'ist pärit bitcoine on kulutatud, asendatakse need uutega, et naasta määratletud segatud müntide lävele. See meetod võimaldab meil vabaneda murest meie UTXO-de anonüümsuskomplektide pärast, muutes samal ajal coinjoins'i efektiivseks muutmiseks vajaliku aja palju vähem piiravaks.

Loodan, et see vastus on valgustanud Whirlpooli mudelit. Kui soovite rohkem teada saada, kuidas coinjoins töötab Bitcoinis, soovitan lugeda [minu põhjalikku artiklit sellel teemal](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2).

**Välised ressursid:**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
Kuna palutud tekstid asuvad veebilinkidel, mida ma ei saa sirvida ega sisu otse vaadata, ei saa ma neid tekste otseselt tõlkida. Siiski võin anda üldise juhendi, kuidas tõlkida tehnilist sisu inglise keelest eesti keelde, eriti seoses krüptoraha ja privaatsustehnoloogiatega nagu Whirlpool.

1. **Tehniliste terminite tõlkimine:**
   - Jätke spetsiifilised tehnilised terminid, nagu "Whirlpool", "CoinJoin", "anonymity sets" muutmata, kuna need viitavad kindlatele tehnoloogiatele või kontseptsioonidele, millel ei pruugi olla täpset vastet eesti keeles.
   - Kui termin on laialdaselt tuntud ja kasutusel ka eesti keeles (nt "blockchain" kui "plokiahel"), kasutage vastavat eestikeelset terminit.

2. **URLide ja markdowni vorminduse säilitamine:**
   - Ärge tõlkige URL-e. Need tuleb jätta originaalkujul.
   - Säilitage markdowni vormindus, et tagada struktuuri järjepidevus. Näiteks, kui algtekstis on loetelu punktid või pealkirjad teatud viisil vormindatud, kasutage sama vormindust ka tõlkes.

3. **Kultuuriliste ja kontekstispetsiifiliste viidete käsitlemine:**
   - Kui tekst sisaldab viiteid, mis on mõistetavad ainult kindlas kultuurilises või geograafilises kontekstis, leidke sobivaim viis nende edasiandmiseks eesti keeles. Vajadusel lisage selgitus.
   - Näiteks, kui originaaltekstis on mängitud sõnadega, mis põhinevad inglise keele eripäradel, leidke eesti keeles sarnane või asendav väljendusviis, mis säilitab originaali kavatsetud tähenduse.

4. **YAML omaduste tõlkimine:**
   - Säilitage YAML omaduste nimed inglise keeles (nt `name:`, `goal:`, `objectives:`), kuid tõlgege nende väärtused eesti keelde.

5. **Tehnilise sisu terviklikkuse säilitamine:**
   - Veenduge, et tõlge oleks tehniliselt täpne ja arusaadav. Ärge tehke järeleandmisi tehnilise sisu täpsuses, isegi kui see tähendab keerukamate või pikemate lausete kasutamist.

6. **Lõplik toimetamine ja kontroll:**
   - Pärast tõlke esmast valmimist kontrollige teksti uuesti, et veenduda selle loogilisuses, tehnilises täpsuses ja keeleliselt korrektsuses. Vajadusel tehke parandusi.

Kuna ma ei saa konkreetseid tekste tõlkida, loodan, et need juhised aitavad teil tõlkida tehnilist sisu inglise keelest eesti keelde.