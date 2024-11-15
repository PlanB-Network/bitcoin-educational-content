---
name: Sissejuhatus formaalsesse krüptograafiasse
goal: Põhjalik sissejuhatus krüptograafia teadusesse ja praktikasse.
objectives:
  - Uurida Beale'i šifreid ja kaasaegseid krüptograafilisi meetodeid, et mõista krüptograafia põhilisi ja ajaloolisi kontseptsioone.
  - Süveneda arvuteooriasse, gruppidesse ja väljadesse, et omandada krüptograafia aluseks olevad võtmematemaatilised kontseptsioonid.
  - Õppida tundma RC4 voogšifrit ja AES-i 128-bitise võtmega, et saada teadmisi sümmeetrilistest krüptograafilistest algoritmidest.
  - Uurida RSA krüptosüsteemi, võtmejaotust ja räsifunktsioone, et avastada asümmeetrilist krüptograafiat.

---
# Süvitsi sukeldumine krüptograafiasse

On raske leida materjale, mis pakuksid head keskteed krüptograafia õpetamisel.

Ühelt poolt on pikad, formaalsed käsitlused, mis on tõeliselt ligipääsetavad ainult neile, kellel on tugev taust matemaatikas, loogikas või mõnes muus formaalses distsipliinis. Teiselt poolt on väga kõrgel tasemel sissejuhatused, mis tõesti varjavad liiga palju detaile neile, kes on vähemalt natuke uudishimulikud.

See krüptograafia sissejuhatus püüab tabada keskteed. Kuigi see peaks olema suhteliselt keeruline ja detailne kõigile, kes on krüptograafiaga uued, ei ole see tüüpiline alustavate traktaatide küülikuurg.

+++

# Sissejuhatus
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Lühikirjeldus
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

See raamat pakub põhjalikku sissejuhatust krüptograafia teadusesse ja praktikasse. Võimalusel keskendub see kontseptuaalsele, mitte formaalsele materjali esitlusele.

> See kursus põhineb [JWBurgers's repo](https://github.com/JWBurgers/An_Introduction_to_Cryptography)-l. Kõik õigused kuuluvad temale. Sisu ei ole veel lõpetatud ja on siin ainult näitamaks, kuidas me võiksime seda integreerida, kui JWburger nõustub.

### Motivatsioon ja eesmärgid

On raske leida materjale, mis pakuksid head keskteed krüptograafia õpetamisel.

Ühelt poolt on pikad, formaalsed käsitlused, mis on tõeliselt ligipääsetavad ainult neile, kellel on tugev taust matemaatikas, loogikas või mõnes muus formaalses distsipliinis. Teiselt poolt on väga kõrgel tasemel sissejuhatused, mis tõesti varjavad liiga palju detaile neile, kes on vähemalt natuke uudishimulikud.

See krüptograafia sissejuhatus püüab tabada keskteed. Kuigi see peaks olema suhteliselt keeruline ja detailne kõigile, kes on krüptograafiaga uued, ei ole see tüüpiline alustavate traktaatide küülikuurg.

### Sihtgrupp

Arendajatest intellektuaalselt uudishimulikeni, see raamat on kasulik kõigile, kes soovivad rohkem kui pealiskaudset mõistmist krüptograafiast. Kui teie eesmärk on krüptograafia valdkonna valdamine, siis on see raamat samuti hea lähtepunkt.

### Lugemisjuhised

Raamat sisaldab praegu seitset peatükki: "Mis on krüptograafia?" (1. peatükk), "Krüptograafia matemaatilised alused I" (2. peatükk), "Krüptograafia matemaatilised alused II" (3. peatükk), "Sümmeetriline krüptograafia" (4. peatükk), "RC4 ja AES" (5. peatükk), "Asümmeetriline krüptograafia" (6. peatükk) ja "RSA krüptosüsteem" (7. peatükk). Viimane peatükk, "Krüptograafia praktikas", lisatakse veel. See keskendub erinevatele krüptograafilistele rakendustele, sealhulgas transpordikihi turvalisusele, sibulmarsruutimisele ja Bitcoini väärtusvahetussüsteemile.
Kui teil pole tugevat matemaatika tausta, on arvuteooria tõenäoliselt selle raamatu kõige keerulisem teema. Pakun sellest ülevaadet 3. peatükis ning see ilmub ka AES-i esitluses 5. peatükis ja RSA krüptosüsteemi kirjelduses 7. peatükis.
Kui teil on tõesti raskusi nende raamatu osade formaalsete detailidega, soovitan esimesel korral piirduda nende kõrgetasemelise lugemisega.

### Tunnustused

Selle raamatu kujundamisel kõige mõjukam raamat on olnud Jonathan Katzi ja Yehuda Lindelli _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL), 2015. Sellega kaasneb Coursera kursus nimega "Krüptograafia".

Peamised lisallikad, mis on olnud abiks selle raamatu ülevaate loomisel, on Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar ja Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) ja [Paari raamatu põhjal loodud kursus nimega “Introduction to Cryptography”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); ning Bruce Schneier, Applied Cryptography, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons).

Tsiteerin ainult väga spetsiifilist informatsiooni ja tulemusi, mille võtan neist allikatest, kuid tahan siinkohal tunnustada oma üldist võlga neile.

Neile lugejatele, kes soovivad pärast seda sissejuhatust otsida edasijõudnud teadmisi krüptograafia kohta, soovitan väga Katzi ja Lindelli raamatut. Katzi kursus Courseras on raamatust veidi kättesaadavam.

### Panused

Palun vaadake [repository's olevat panuste faili](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md), et saada juhiseid, kuidas projekti toetada.

### Notatsioon

**Võtmesõnad:**

Võtmesõnad tutvustatakse esile tõstes neid paksus kirjas. Näiteks Rijndaeli šifri tutvustamine võtmesõnana näeks välja järgmiselt: **Rijndaeli šiffer**.

Võtmesõnad on selgelt määratletud, välja arvatud juhul, kui need on omadnimed või nende tähendus on arutelust ilmne.

Iga definitsioon antakse tavaliselt võtmesõna tutvustamisel, kuigi mõnikord on mugavam jätta definitsioon hilisemaks.

**Rõhutatud sõnad ja fraasid:**

Sõnu ja fraase rõhutatakse kaldkirjas. Näiteks fraas "Pea oma parooli meeles" näeks välja järgmiselt: *Pea oma parooli meeles*.

**Formaalne notatsioon:**

Formaalne notatsioon puudutab peamiselt muutujaid, juhuslikke muutujaid ja hulki.

* Muutujad: Neid tähistatakse tavaliselt väiketähega (nt "x" või "y"). Mõnikord on need suurtähtedega selguse huvides (nt "M" või "K").
* Juhuslikud muutujad: Neid tähistatakse alati suurtähega (nt "X" või "Y")
* Hulgad: Neid tähistatakse alati paksus, suures kirjas (nt **S**)

# Mis on krüptograafia?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Beale'i šifrid
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>
Alustame oma uurimist krüptograafia valdkonnas ühe selle ajaloo võluvama ja meelelahutuslikuma episoodiga: Beale'i šifrite lugu. [1]
Minu arvates on Beale'i šifrite lugu pigem väljamõeldis kui reaalsus. Kuid väidetavalt juhtus see järgnevalt.

Nii 1820. aasta talvel kui ka 1822. aastal peatus mees nimega Thomas J. Beale kõrtsis, mille omanik oli Robert Morriss Lynchburgis (Virginia). Beale'i teise peatumise lõpus andis ta Morrissile rauast kasti väärtuslike paberitega hoiule.

Mõni kuu hiljem sai Morriss Beale'ilt kirja, mis oli dateeritud 9. maiga 1822. Selles rõhutati rauast kasti sisu suurt väärtust ja anti Morrissile mõned juhised: kui ei Beale ega ükski tema kaaslastest ei tulnud kasti järele, peaks ta selle täpselt kümme aastat kirja kuupäevast (st 9. mail 1832) avama. Mõned paberid kastis oleksid kirjutatud tavalises tekstis. Mitmed teised aga oleksid "mõistetamatud ilma võtme abita". See "võti" toimetataks siis Morrissile Beale'i nimetamata sõbra poolt juunis 1832.

Hoolimata selgetest juhistest, ei avanud Morriss kasti mais 1832 ja Beale'i salapärane sõber ei ilmunud sel aastal juunis. Alles 1845. aastal otsustas kõrtsmik lõpuks kasti avada. Selles leidis Morriss märkuse, mis selgitas, kuidas Beale ja tema kaaslased avastasid kulda ja hõbedat läänes ning matsid selle koos mõningate juveelidega turvalisuse huvides maha. Lisaks sisaldas kast kolme **šifriteksti**: st tekste, mis on kirjutatud koodis ja mis nõuavad **krüptograafilist võtit** ehk saladust ja kaasnevat algoritmi avamiseks. Seda avamisprotsessi nimetatakse **dekrüpteerimiseks**, samas kui lukustamisprotsessi nimetatakse **krüpteerimiseks**. (Nagu selgitatakse 3. peatükis, võib termin šiffer tähendada erinevaid asju. Nimes "Beale'i šifrid" on see lühend šifritekstidest.)

Kolm šifriteksti, mille Morriss rauast kastist leidis, koosnevad igaüks numbritest, mis on eraldatud komadega. Beale'i märkuse kohaselt annavad need šifritekstid eraldi teada aarde asukoha, aarde sisu ja nimekirja õigustatud pärijatest aardele ja nende osadest (viimane teave on oluline juhul, kui Beale ja tema kaaslased ei tulnud kunagi kasti järele).

Morris üritas kakskümmend aastat kolme šifriteksti dekrüpteerida. See oleks olnud lihtne võtmega. Kuid Morrissil polnud võtit ja ta ei õnnestunud oma katsetes taastada algtekste ehk **tavaltekste**, nagu neid krüptograafias tavaliselt nimetatakse.

Elu lõpul andis Morriss kasti 1862. aastal ühele sõbrale. See sõber avaldas hiljem 1885. aastal pamfleti pseudonüümi J.B. Ward all. See sisaldas kirjeldust (väidetavast) kasti ajaloost, kolmest šifritekstist ja lahendusest, mille ta oli teise šifriteksti jaoks leidnud. (Ilmselt on iga šifriteksti jaoks üks võti, mitte üks võti, mis töötab kõigi kolme šifriteksti peal, nagu Beale oma kirjas Morrissile algselt näib vihjanud.)

Teise šifriteksti näete allpool *Joonisel 2*. [2] Selle šifriteksti võtmeks on Ameerika Ühendriikide Iseseisvusdeklaratsioon. Dekrüpteerimisprotseduur taandub järgmiste kahe reegli rakendamisele:
* Iga numbri n puhul šifreeritud tekstis leidke Ameerika Ühendriikide Iseseisvusdeklaratsioonist n-nda sõna
* Asendage number n leitud sõna esimese tähega

*Joonis 1: Beale'i šiffer nr 2*

![Joonis 1: Beale'i šiffer nr 2.](assets/Figure1-1.webp "Joonis 1: Beale'i šiffer nr 2")

Näiteks teise šifreeritud teksti esimene number on 115. Iseseisvusdeklaratsiooni 115. sõna on “instituted,” seega on tavalise teksti esimene täht “i.” Šifreeritud tekst ei näita otseselt sõnade vahesid ja suurtähti. Kuid pärast esimeste sõnade dešifreerimist on loogiline järeldada, et tavaline tekst algas lihtsalt sõnaga “I.” (Tavaline tekst algab fraasiga “I have deposited in the county of Bedford.”)

Pärast dešifreerimist annab teine sõnum üksikasjaliku sisu aarde kohta (kuld, hõbe ja juveelid) ning vihjab, et see oli maetud raudpottidesse ja kaetud kividega Bedfordi maakonnas (Virginia). Inimesed armastavad head müsteeriumi, seega on tehtud suuri jõupingutusi ka teiste kahe Beale'i šifri dešifreerimiseks, eriti selle, mis kirjeldab aarde asukohta. Isegi mitmed silmapaistvad krüptograafid on neid proovinud dešifreerida. Siiski ei ole seni keegi suutnud dešifreerida kahte ülejäänud šifreeritud teksti.

**Märkused:**

[1] Hea kokkuvõtte loo kohta leiate Simon Singhi raamatust *The Code Book*, Fourth Estate (London, 1999), lk. 82-99. Lugu põhjal lühifilmi tegi Andrew Allen 2010. aastal. Filmi, “The Thomas Beale Cipher,” leiate [selle veebisaidilt](http://www.thomasbealecipher.com/).

[2] See pilt on saadaval Beale'i šifrite Wikipedia lehel.

## Kaasaegne krüptograafia
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Värvikad lood nagu Beale'i šifrite oma on see, mida enamik meist seostab krüptograafiaga. Siiski erineb kaasaegne krüptograafia vähemalt neljal olulisel viisil nendest ajaloolistest näidetest.

Esiteks on ajalooliselt krüptograafia olnud mures ainult **saladuslikkuse** (või konfidentsiaalsuse) pärast. [3] Šifreeritud tekste loodi selleks, et tagada, et ainult teatud osapooled võiksid olla teadlikud tavalistes tekstides olevast informatsioonist, nagu Beale'i šifrite puhul. Selleks, et krüpteerimisskeem oma eesmärki hästi teeniks, peaks šifreeritud teksti dešifreerimine olema teostatav ainult siis, kui teil on võti.

Kaasaegne krüptograafia tegeleb laiema teemade ringiga kui ainult saladuslikkus. Need teemad hõlmavad peamiselt (1) **sõnumi terviklikkust**—see tähendab, tagamist, et sõnumit ei ole muudetud; (2) **sõnumi autentsust**—see tähendab, tagamist, et sõnum on tõepoolest saadetud kindlalt saatjalt; ja (3) **mitte-eitamist**—see tähendab, tagamist, et saatja ei saa hiljem valesti eitada, et ta sõnumi saatis. [4]

Oluline eristus, mida meeles pidada, on seega **krüpteerimisskeemi** ja **krüptograafilise skeemi** vahel. Krüpteerimisskeem on mures ainult saladuslikkuse pärast. Kuigi krüpteerimisskeem on krüptograafiline skeem, ei ole vastupidine tõsi. Krüptograafiline skeem võib samuti teenida krüptograafia teisi peateemasid, sealhulgas terviklikkust, autentsust ja mitte-eitamist.
Aususe ja autentsuse teemad on sama olulised kui saladuslikkus. Meie kaasaegsed kommunikatsioonisüsteemid ei suudaks toimida ilma garantiideta seoses kommunikatsiooni aususe ja autentsusega. Samuti on oluline mittevaidlustatavus, näiteks digitaalsete lepingute puhul, kuid see ei ole krüptograafilistes rakendustes nii laialdaselt vajalik kui saladuslikkus, ausus ja autentsus.

Teiseks, klassikalised krüpteerimisskeemid, nagu Beale'i šifrid, hõlmasid alati ühte võtit, mis jagati kõigi asjaomaste osapoolte vahel. Siiski hõlmavad paljud kaasaegsed krüptograafilised skeemid mitte ainult ühte, vaid kahte võtit: **privaatvõtit** ja **avalikku võtit**. Kuigi esimene peaks igas rakenduses jääma privaatseks, on viimane tavaliselt avalik teave (seega ka nende nimed). Krüpteerimise valdkonnas saab avalikku võtit kasutada sõnumi krüpteerimiseks, samas kui privaatvõtit saab kasutada dekrüpteerimiseks.

Krüptograafia haru, mis tegeleb skeemidega, kus kõik osapooled jagavad ühte võtit, on tuntud kui **sümmeetriline krüptograafia**. Sellises skeemis olevat üksikut võtit nimetatakse tavaliselt **privaatvõtmeks** (või salajaseks võtmeks). Krüptograafia haru, mis tegeleb skeemidega, mis nõuavad privaat-avaliku võtme paari, on tuntud kui **asümmeetriline krüptograafia**. Neid harusid nimetatakse mõnikord ka vastavalt **privaatvõtme krüptograafiaks** ja **avaliku võtme krüptograafiaks** (kuigi see võib tekitada segadust, kuna avaliku võtme krüptograafilised skeemid sisaldavad ka privaatvõtmeid).

Asümmeetrilise krüptograafia tekkimine 1970. aastate lõpus on olnud üks krüptograafia ajaloo olulisemaid sündmusi. Ilma selleta ei oleks enamik meie kaasaegseid kommunikatsioonisüsteeme, sealhulgas Bitcoin, võimalikud või vähemalt väga ebapraktilised.

Oluline on märkida, et kaasaegne krüptograafia ei ole ainult sümmeetriliste ja asümmeetriliste võtmekrüptograafiliste skeemide uurimine (kuigi see hõlmab suurt osa valdkonnast). Näiteks tegeleb krüptograafia ka räsifunktsioonide ja pseudosuvaliste numbrite generaatoritega ning nende primitiivide põhjal saab ehitada rakendusi, mis ei ole seotud sümmeetrilise või asümmeetrilise võtmekrüptograafiaga.

Kolmandaks, klassikalised krüpteerimisskeemid, nagu neid kasutati Beale'i šifrites, olid rohkem kunst kui teadus. Nende tajutav turvalisus põhines suuresti intuitsioonil nende keerukuse osas. Tavaliselt parandati neid, kui õpiti tundma uut rünnakut nende vastu, või loobuti neist täielikult, kui rünnak oli eriti tõsine. Kaasaegne krüptograafia on aga range teadus, mis kasutab krüptograafiliste skeemide arendamisel ja analüüsimisel formaalset, matemaatilist lähenemist.

Eelkõige keskendub kaasaegne krüptograafia formaalsetele **turvalisuse tõestustele**. Iga krüptograafilise skeemi turvalisuse tõestus toimub kolmes etapis:

1. **Krüptograafilise turvalisuse definitsiooni** avaldus, see tähendab turvalisuse eesmärkide ja ründaja poolt esitatud ohu kogum.
2. Iga matemaatilise eelduse avaldus seoses skeemi arvutusliku keerukusega. Näiteks võib krüptograafilises skeemis sisalduda pseudosuvaliste numbrite generaator. Kuigi me ei saa tõestada nende olemasolu, võime eeldada, et nad on olemas.
3. Matemaatilise **turvalisuse tõestuse** esitamine skeemi kohta formaalse turvalisuse mõiste ja kõigi matemaatiliste eelduste alusel.

Neljandaks, kuigi ajalooliselt kasutati krüptograafiat peamiselt sõjalistes seadetes, on see digiajastul imbunud meie igapäevategevustesse. Olgu tegemist pangandusega internetis, postitamisega sotsiaalmeedias, toote ostmisega Amazonist oma krediitkaardiga või sõbrale bitcoini jootraha andmisega, krüptograafia on meie digiajastu hädavajalik osa.

Arvestades neid nelja aspekti kaasaegses krüptograafias, võiksime kaasaegset **krüptograafiat** iseloomustada kui teadust, mis tegeleb krüptograafiliste skeemide formaalse arendamise ja analüüsiga digitaalse teabe kaitsmiseks vaenulike rünnakute eest. Turvalisus siin tuleks mõista laialt kui rünnakute ärahoidmist, mis kahjustavad saladuslikkust, ausust, autentimist ja/või mittevaidlustatavust kommunikatsioonis.
Krüptograafia on kõige paremini mõistetav kui **küberturvalisuse** aladistsipliin, mis tegeleb arvutisüsteemide varguse, kahjustamise ja väärkasutuse ärahoidmisega. Tuleb märkida, et paljud küberturvalisuse mured on krüptograafiaga vähe või ainult osaliselt seotud.
Näiteks, kui ettevõte majutab kohapeal kalleid servereid, võivad nad olla mures selle riistvara varguse ja kahjustamise eest. Kuigi see on küberturvalisuse mure, on sellel vähe pistmist krüptograafiaga.

Teise näitena, **phishing rünnakud** on meie kaasaegses ajastus tavaline probleem. Need rünnakud üritavad inimesi petta e-posti või mõne muu sõnumivahendi kaudu loovutama tundlikku teavet nagu paroolid või krediitkaardinumbrid. Kuigi krüptograafia võib aidata phishing rünnakuid teatud määral lahendada, nõuab terviklik lähenemine rohkemat kui lihtsalt krüptograafia kasutamist.

**Märkused:**

[3] Täpsemalt öeldes on krüptograafiliste skeemide olulised rakendused olnud seotud saladuse hoidmisega. Näiteks lapsed kasutavad sageli lihtsaid krüptograafilisi skeeme "lõbu pärast". Sellistel juhtudel saladuse hoidmine tegelikult mureks ei ole.

[4] Bruce Schneier, *Applied Cryptography*, 2. väljaanne, 2015 (Indianapolis, IN: John Wiley & Sons), lk. 2.

[5] Vaata Jonathan Katz ja Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), eriti lk. 16–23, hea kirjelduse saamiseks.

[6] Vrdl. Katz ja Lindell, ibid., lk. 3. Arvan, et nende karakteristika omab mõningaid probleeme, seega esitan siin nende avaldusest veidi erineva versiooni.

## Avatud suhtlus
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Kaasaegne krüptograafia on loodud turvalisuse tagamiseks **avatud suhtluse** keskkonnas. Kui meie suhtluskanal on nii hästi kaitstud, et pealtkuulajatel pole mingit võimalust meie sõnumeid manipuleerida või isegi lihtsalt jälgida, siis on krüptograafia üleliigne. Enamik meie suhtluskanaleid siiski ei ole nii hästi kaitstud.

Kaasaegse maailma suhtluse selgroog on tohutu võrk kiudoptilistest kaablitest. Telefonikõnede tegemine, televiisori vaatamine ja veebis surfamine kaasaegses majapidamises sõltub üldiselt sellest kiudoptiliste kaablite võrgust (väike protsent võib sõltuda puhtalt satelliitidest). Tõsi on, et teil võib kodus olla erinevaid andmeühendusi, nagu koaksiaalkaabel, (asümmeetriline) digitaalne tellijaliin ja kiudoptiline kaabel. Kuid vähemalt arenenud maailmas ühinevad need erinevad andmekandjad kiiresti väljaspool teie maja sõlmpunkti suures kiudoptiliste kaablite võrgus, mis ühendab kogu maailma. Erandid on mõned arenenud maailma kauged piirkonnad, nagu Ameerika Ühendriigid ja Austraalia, kus andmeliiklus võib siiski ka läbida olulisi vahemaid traditsiooniliste vasktelefonijuhtmete kaudu.

Potentsiaalsetel ründajatel oleks võimatu füüsiliselt takistada juurdepääsu sellele kaablite võrgule ja selle toetavale infrastruktuurile. Tegelikult me juba teame, et enamik meie andmeid on erinevate riiklike luureagentuuride poolt olulistel interneti ristmikel pealt kuulatud.[7] See hõlmab kõike alates Facebooki sõnumitest kuni veebiaadressideni, mida külastate.

Kuigi andmete massilise jälgimise nõuab võimsat vastast, nagu riiklik luureagentuur, võivad ründajad, kellel on vaid vähe ressursse, kergesti üritada nuhkida kohalikul tasandil. Kuigi see võib toimuda juhtmete pealtkuulamise tasandil, on palju lihtsam lihtsalt pealt kuulata traadita suhtlust.
Enamik meie kohalikust võrguandmestikust—olgu see siis meie kodudes, kontoris või kohvikus—liigub nüüd raadiolainete kaudu juhtmeta juurdepääsupunktidesse kõik-ühes ruuterites, mitte füüsiliste kaablite kaudu. Seega vajab ründaja vähe ressursse, et pealt kuulata ükskõik millist teie kohalikku liiklust. See on eriti murettekitav, kuna enamik inimesi teeb väga vähe, et kaitsta oma kohalikes võrkudes liikuvaid andmeid. Lisaks võivad potentsiaalsed ründajad sihtida ka meie mobiilse lairibaühendusi, nagu 3G, 4G ja 5G. Kõik need juhtmeta sidevormid on ründajatele kerge sihtmärk.
Seega on sidekanali kaitsmise teel suhtluse saladuses hoidmise idee paljuski kaasaegses maailmas lootusetult petlik püüdlus. Kõik, mida me teame, nõuab tõsist paranoiat: peaksite alati eeldama, et keegi kuulab pealt. Ja krüptograafia on peamine vahend, mis meil on, et saavutada mingisugustki turvalisust selles kaasaegses keskkonnas.

**Märkused:**

[7] Vaadake näiteks Olga Khazani, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, 16. juuli 2013 (saadaval aadressil [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Krüptograafia matemaatilised alused 1
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Juhuslikud muutujad
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Krüptograafia põhineb matemaatikal. Ja kui soovite krüptograafiast rohkem kui pealiskaudset arusaama, peate olema mugav selle matemaatikaga.

See peatükk tutvustab enamikku põhimatemaatikast, millega kokku puutute krüptograafiat õppides. Teemad hõlmavad juhuslikke muutujaid, modulo toiminguid, XOR toiminguid ja pseudosuvalisust. Peaksite materjali nendes jaotistes valdama, et omada krüptograafiast mittepealiskaudset arusaamist.

Järgmine jaotis käsitleb arvuteooriat, mis on palju keerulisem.

### Juhuslikud muutujad

Juhuslikku muutujat tähistatakse tavaliselt mittepaksus, suurtähega. Niisiis, võime rääkida juhuslikust muutujast $X$, juhuslikust muutujast $Y$ või juhuslikust muutujast $Z$. Seda tähistust kasutan ka edaspidi.

**Juhuslik muutuja** võib võtta kahte või enamat võimalikku väärtust, igaühega teatud positiivne tõenäosus. Võimalikud väärtused on loetletud **tulemuste hulgas**.

Iga kord, kui te **valimite** juhuslikku muutujat, valite konkreetse väärtuse selle tulemuste hulgast määratletud tõenäosuste järgi.

Vaadelgem lihtsat näidet. Eeldagem muutujat X, mis on määratletud järgmiselt:

- X-l on tulemuste hulk $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

On lihtne näha, et $X$ on juhuslik muutuja. Esiteks, on kaks või enam võimalikku väärtust, mida $X$ võib võtta, nimelt $1$ ja $2$. Teiseks, iga võimalik väärtus omab positiivset tõenäosust ilmneda, kui te valite $X$, nimelt $0.5$.
Kõik, mida juhuslik muutuja vajab, on tulemuste hulk kahe või enama võimalusega, kus igal võimalusel on positiivne tõenäosus ilmneda valimisel. Põhimõtteliselt saab juhuslikku muutujat defineerida abstraktselt, kontekstist sõltumatult. Sel juhul võiksite mõelda "valimisele" kui mingi loodusliku eksperimendi läbiviimisele, et määrata juhusliku muutuja väärtus.
Muutuja $X$ ülal oli defineeritud abstraktselt. Seega võiksite mõelda muutuja $X$ valimisele kui ausa mündi viskamisele ja “2” määramisele, kui tuleb kiri, ning “1” määramisele, kui tuleb kull. Iga kord, kui te valite $X$, viskate mündi uuesti.

Alternatiivselt võiksite mõelda ka $X$ valimisele kui ausa täringu veeretamisele ja “2” määramisele, kui täring maandub $1$, $3$ või $4$ peale, ning “1” määramisele, kui täring maandub $2$, $5$ või $6$ peale. Iga kord, kui te valite $X$, veerate täringut uuesti.

Tegelikult võib ette kujutada mis tahes looduslikku eksperimenti, mis võimaldaks defineerida $X$ võimalike väärtuste tõenäosused ülal toodud joonisel.

Sageli aga juhuslikke muutujaid ei tutvustata lihtsalt abstraktselt. Selle asemel on võimalike tulemuste hulk selgelt seotud reaalse maailma tähendusega (mitte ainult numbritega). Lisaks võidakse neid tulemusi defineerida mõne konkreetse tüüpi eksperimendi alusel (mitte mis tahes loodusliku eksperimendiga nende väärtustega).

Vaatleme nüüd näidet muutujast $X$, mis ei ole defineeritud abstraktselt. X on defineeritud järgmiselt, et määrata, kumb kahest meeskonnast alustab jalgpallimängu:

- $X$ tulemuste hulk on {punane alustab, sinine alustab}
- Visake konkreetne münt $C$: kiri = “punane alustab”; kull = “sinine alustab”

$$
Pr [X = \text{punane alustab}] = 0.5
$$

$$
Pr [X = \text{sinine alustab}] = 0.5
$$

Sel juhul on X tulemuste hulgale antud konkreetne tähendus, nimelt milline meeskond jalgpallimängus alustab. Lisaks on võimalikud tulemused ja nende seotud tõenäosused määratud konkreetse eksperimendi, nimelt konkreetse mündi $C$ viskamise, abil.

Krüptograafia aruteludes tutvustatakse juhuslikke muutujaid tavaliselt tulemuste hulgaga, millel on reaalse maailma tähendus. See võib olla kõigi sõnumite hulk, mida saab krüpteerida, tuntud kui sõnumiruum, või kõigi võtmete hulk, mida krüpteerimist kasutavad pooled saavad valida, tuntud kui võtmeruum.

Krüptograafia aruteludes ei defineerita juhuslikke muutujaid siiski tavaliselt mõne konkreetse loodusliku eksperimendi alusel, vaid mis tahes eksperimendi alusel, mis võib anda õiged tõenäosusjaotused.

Juhuslikud muutujad võivad olla diskreetse või pideva tõenäosusjaotusega. **Diskreetse tõenäosusjaotusega** juhuslikud muutujad – st diskreetsed juhuslikud muutujad – omavad piiratud arvu võimalikke tulemusi. Seni toodud näidetes olnud juhuslik muutuja $X$ oli diskreetne.

**Pidevad juhuslikud muutujad** võivad selle asemel võtta väärtusi ühes või mitmes intervallis. Võiksite näiteks öelda, et juhuslik muutuja võtab valimisel mis tahes reaalarvu väärtuse vahemikus 0 kuni 1 ja et selles intervallis on iga reaalarv võrdselt tõenäoline. Selles intervallis on lõpmatult palju võimalikke väärtusi.

Krüptograafia arutelude jaoks on vaja mõista ainult diskreetseid juhuslikke muutujaid. Seega tuleks edaspidi juhuslike muutujate arutelusid mõista viitamisena diskreetsetele juhuslikele muutujatele, kui pole öeldud teisiti.

### Juhuslike muutujate graafiline kujutamine
Juhusliku muutuja võimalikke väärtusi ja nendega seotud tõenäosusi on lihtne visualiseerida graafiku abil. Näiteks kaaluge eelmisest jaotisest pärit juhuslikku muutujat $X$ tulemuste hulgaga $\{1, 2\}$, kus $Pr [X = 1] = 0.5$ ja $Pr [X = 2] = 0.5$. Sellist juhuslikku muutujat kuvataks tavaliselt ribagraafiku kujul, nagu *Joonis 1*.
*Joonis 1: Juhuslik muutuja X*

![Joonis 1: Juhuslik muutuja X.](assets/Figure2-1.webp)

Laiad ribad *Joonisel 1* ei tähenda kindlasti, et juhuslik muutuja $X$ on tegelikult pidev. Selle asemel on ribad tehtud laiaks, et need oleksid visuaalselt atraktiivsemad (lihtsalt sirge joon ülespoole pakub vähem intuitiivset visualiseerimist).

### Ühtlased muutujad

Väljendis "juhuslik muutuja" tähendab termin "juhuslik" lihtsalt "tõenäosuslik". Teisisõnu, see tähendab lihtsalt, et kaks või enam võimalikku tulemust muutujal esinevad teatud tõenäosustega. Need tulemused ei pea siiski tingimata olema võrdselt tõenäolised (kuigi termin "juhuslik" võib tõesti omada seda tähendust teistes kontekstides).

**Ühtlane muutuja** on juhusliku muutuja erijuht. See võib võtta kahe või enama väärtuse, kõik võrdse tõenäosusega. Joonisel *1* kujutatud juhuslik muutuja $X$ on selgelt ühtlane muutuja, kuna mõlemad võimalikud tulemused esinevad tõenäosusega $0.5$. Siiski on palju juhuslikke muutujaid, mis ei ole ühtlaste muutujate näited.

Võtke näiteks juhuslik muutuja $Y$. Sellel on tulemuste hulk $\{1, 2, 3, 8, 10\}$ ja järgmine tõenäosusjaotus:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Kuigi kaks võimalikku tulemust on tõepoolest võrdse tõenäosusega esinemiseks, nimelt $1$ ja $8$, võib $Y$ võtta ka teatud väärtusi erinevate tõenäosustega kui $0.25$ valimisel. Seega, kuigi $Y$ on tõepoolest juhuslik muutuja, ei ole see ühtlane muutuja.

$Y$ graafiline kujutis on esitatud *Joonisel 2*.

*Joonis 2: Juhuslik muutuja Y*

![Joonis 2: Juhuslik muutuja Y.](assets/Figure2-2.webp "Joonis 2: Juhuslik muutuja Y")

Lõpliku näitena kaaluge juhuslikku muutujat Z. Sellel on tulemuste hulk {1,3,7,11,12} ja järgmine tõenäosusjaotus:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Seda saab näha *Joonisel 3*. Erinevalt $Y$-st on juhuslik muutuja Z ühtlane muutuja, kuna kõik võimalikud väärtused valimisel on võrdse tõenäosusega.

*Joonis 3: Juhuslik muutuja Z*
![Joonis 3: Juhuslik muutuja Z.](assets/Figure2-3.webp "Joonis 3: Juhuslik muutuja Z")

### Tingimuslik tõenäosus

Oletame, et Bob kavatseb ühtlaselt valida päeva eelmisest kalendriaastast. Mida peaksime järeldama tõenäosuse kohta, et valitud päev on suvel?

Niikaua kui me arvame, et Bobi protsess on tõepoolest täiesti ühtlane, peaksime järeldama, et on 1/4 tõenäosus, et Bob valib päeva suvel. See on **tingimusteta tõenäosus**, et juhuslikult valitud päev on suvel.

Oletame nüüd, et Bobi asemel, et ühtlaselt tõmmata kalendripäev, valib Bob ainult nende päevade seast, mil Crystal Lake'i (New Jersey) keskpäeva temperatuur oli 21 kraadi Celsiust või kõrgem. Arvestades seda lisateavet, mida võime järeldada tõenäosuse kohta, et Bob valib päeva suvel?

Me peaksime tõesti jõudma erineva järelduseni kui varem, isegi ilma igasuguse täiendava konkreetse teabeta (nt keskpäeva temperatuur igal päeval eelmisel kalendriaastal).

Teades, et Crystal Lake asub New Jerseys, ei ootaks me kindlasti, et keskpäeva temperatuur oleks talvel 21 kraadi Celsiust või kõrgem. Selle asemel on palju tõenäolisem, et see on soe päev kevadel või sügisel või päev kusagil suvel. Seega, teades, et Crystal Lake'i valitud päeva keskpäeva temperatuur oli 21 kraadi Celsiust või kõrgem, muutub tõenäosus, et Bobi poolt valitud päev on suvel, palju suuremaks. See on **tingimuslik tõenäosus**, et juhuslikult valitud päev on suvel, arvestades, et Crystal Lake'i keskpäeva temperatuur oli 21 kraadi Celsiust või kõrgem.

Erinevalt eelmisest näitest võivad kahe sündmuse tõenäosused olla ka täiesti seoseta. Sellisel juhul ütleme, et need on **sõltumatud**.

Oletame näiteks, et teatud õiglane münt on maandunud kullile. Arvestades seda fakti, mis on siis tõenäosus, et homme sajab vihma? Tingimuslik tõenäosus sel juhul peaks olema sama mis tingimusteta tõenäosus, et homme sajab vihma, kuna mündi viskamine üldiselt ei mõjuta ilma.

Me kasutame "|" sümbolit tingimuslike tõenäosuste avaldamiseks. Näiteks sündmuse $A$ tõenäosus, arvestades, et sündmus $B$ on aset leidnud, saab kirjutada järgmiselt:

$$
Pr[A|B]
$$

Niisiis, kui kaks sündmust, $A$ ja $B$, on sõltumatud, siis:

$$
Pr[A|B] = Pr[A] \text{ ja } Pr[B|A] = Pr[B]
$$

Sõltumatuse tingimus saab lihtsustada järgmiselt:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Tõenäosusteooria üks võtmeküsimus on tuntud kui **Bayesi teoreem**. See põhimõtteliselt väidab, et $Pr[A|B]$ saab ümber kirjutada järgmiselt:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Tingimuslike tõenäosuste kasutamise asemel konkreetsete sündmustega, võime vaadata ka tingimuslikke tõenäosusi, mis on seotud kahe või enama juhusliku muutujaga üle võimalike sündmuste hulga. Oletame kaks juhuslikku muutujat, $X$ ja $Y$. Me võime tähistada ükskõik millist võimalikku väärtust $X$ jaoks kui $x$, ja ükskõik millist võimalikku väärtust $Y$ jaoks kui $y$. Võime siis öelda, et kaks juhuslikku muutujat on sõltumatud, kui järgmine väide kehtib:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

kõigi $x$ ja $y$ jaoks.

Olgu see väide veidi selgemalt väljendatud.
Eeldame, et tulemuste hulgad $X$ ja $Y$ on määratletud järgnevalt: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ ja **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (On tavapärane näidata väärtuste hulki rasvases kirjas suurtähtedega.)
Nüüd eeldame, et te valite $Y$-st ja märkate $y_1$. Ülaltoodud väide ütleb meile, et tõenäosus nüüd saada $X$-st valimisel $x_1$ on täpselt sama, nagu me poleks kunagi täheldanud $y_1$. See kehtib mis tahes $y_i$ kohta, mille oleksime võinud algselt $Y$-st saada. Lõpuks kehtib see mitte ainult $x_1$ kohta. Mis tahes $x_i$ puhul ei mõjuta tõenäosust $Y$ valimi tulemus. Kõik see kehtib ka juhul, kui $X$ valitakse esimesena.

Lõpetame meie arutelu veidi filosoofilisemal noodil. Igas reaalses olukorras hinnatakse mingi sündmuse tõenäosust alati kindla teabe kogumi alusel. Mingit "tingimusteta tõenäosust" väga range sõna mõttes ei ole.

Näiteks, kui ma küsiksin teilt tõenäosust, et sead lendavad aastaks 2030. Kuigi ma ei anna teile rohkem teavet, teate te selgelt palju maailma kohta, mis võib mõjutada teie otsust. Te pole kunagi näinud, et sead lendaksid. Teate, et enamik inimesi ei oota, et nad lendaksid. Teate, et nad pole tegelikult ehitatud lendamiseks. Ja nii edasi.

Seega, kui me räägime mingi sündmuse "tingimusteta tõenäosusest" reaalses kontekstis, võib see termin tegelikult omada tähendust ainult siis, kui me mõistame seda kui "tõenäosust ilma igasuguse edasise selgesõnalise teabeta". Iga "tingimusliku tõenäosuse" mõistmine peaks seega alati olema mõistetav mingi konkreetse teabe valguses.

Ma võiksin näiteks küsida teilt tõenäosust, et sead lendavad aastaks 2030, pärast seda, kui olen teile andnud tõendeid, et mõned Uus-Meremaa kitsed on õppinud lendama pärast mõneaastast treenimist. Sel juhul kohandate tõenäoliselt oma hinnangut tõenäosusele, et sead lendavad aastaks 2030. Seega on tõenäosus, et sead lendavad aastaks 2030, tingimuslik sellele tõendile Uus-Meremaa kitsede kohta.

## Modulo operatsioon
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

Kõige lihtsam **modulo operatsiooni** väljend on järgmisel kujul: $x \mod y$.

Muutujat $x$ nimetatakse jagatavaks ja muutujat $y$ jagajaks. Positiivse jagatava ja positiivse jagaja korral modulo operatsiooni sooritamiseks määratakse lihtsalt jagamise jääk.

Näiteks, kaaluge väljendit $25 \mod 4$. Arv 4 mahub arvu 25 sisse kokku 6 korda. Selle jagamise jääk on 1. Seega, $25 \mod 4$ võrdub 1-ga. Sarnasel viisil saame hinnata alljärgnevaid väljendeid:

* $29 \mod 30 = 29$ (kuna 30 mahub 29 sisse kokku 0 korda ja jääk on 29)
* $42 \mod 2 = 0$ (kuna 2 mahub 42 sisse kokku 21 korda ja jääk on 0)
* $12 \mod 5 = 2$ (kuna 5 jagub 12-sse kokku 2 korda ja jääk on 2)
* $20 \mod 8 = 4$ (kuna 8 jagub 20-sse kokku 2 korda ja jääk on 4)

Kui jagatav või jagaja on negatiivne, võivad programmeerimiskeeled modulo operatsioone erinevalt käsitleda.

Krüptograafias tuleb kindlasti ette juhtumeid negatiivse jagatavaga. Sellistel juhtudel on tüüpiline lähenemine järgmine:

* Esiteks määrake lähim väärtus, *mis on väiksem või võrdne* jagatavaga, mille korral jagaja jagab jäägita. Nimetame seda väärtust $p$.
* Kui jagatav on $x$, siis modulo operatsiooni tulemus on väärtus $x – p$.

Näiteks, kui jagatav on $–20$ ja jagaja 3. Lähim väärtus, mis on väiksem või võrdne $–20$-ga, mille korral 3 jagab ühtlaselt, on $–21$. Sel juhul on $x – p$ väärtus $–20 – (–21)$. See võrdub 1-ga ja seega $–20 \mod 3$ võrdub 1-ga. Sarnasel viisil saame hinnata alljärgnevaid avaldisi:

* $–8 \mod 5 = 2$
* $–19 \mod 16 = 13$
* $–14 \mod 6 = 4$

Notatsiooni osas näete tavaliselt järgmisi tüüpi avaldisi: $x = [y \mod z]$. Sulgude tõttu kehtib modulo operatsioon sel juhul ainult avaldise paremal poolel. Kui näiteks $y$ võrdub 25 ja $z$ võrdub 4-ga, siis $x$ väärtustatakse kui 1.

Ilma sulgudeta kehtib modulo operatsioon *mõlemal poolel* avaldisest. Eeldagem näiteks järgmist avaldist: $x = y \mod z$. Kui $y$ võrdub 25 ja $z$ võrdub 4-ga, siis teame ainult, et $x \mod 4$ väärtustatakse kui 1. See on kooskõlas mis tahes väärtusega $x$ jaoks hulgast $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.

Matemaatika haru, mis hõlmab modulo operatsioone arvude ja avaldistega, nimetatakse **modulaararitmeetikaks**. Võite mõelda sellele harule kui aritmeetikale juhtudel, kui arvurida ei ole lõpmatult pikk. Kuigi me tavaliselt kohtame modulo operatsioone (positiivsete) täisarvude puhul krüptograafias, võite teostada modulo operatsioone kasutades mis tahes reaalarve.

### Nihešiffer

Modulo operatsioon on krüptograafias sageli kohatav. Illustratsiooniks vaatleme üht kõige kuulsamat ajaloolist krüpteerimisskeemi: nihešifferit.

Defineerime selle esmalt. Eeldame sõnastikku *D*, mis seostab kõik inglise tähestiku tähed järjekorras numbrite hulgaga $\{0, 1, 2, \ldots, 25\}$. Eeldame sõnumiruumi **M**. **Nihešiffer** on siis krüpteerimisskeem, mis on defineeritud järgnevalt:

- Valige ühtlaselt võti $k$ võtmehulgast **K**, kus **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Krüpteerige sõnum $m \in \mathbf{M}$ järgmiselt:
    - Eraldage $m$ tema üksikuteks tähtedeks $m_0, m_1, \ldots, m_i, \ldots, m_l$
- Muutke iga $m_i$ arvuks vastavalt *D*-le
    - Iga $m_i$ jaoks, $c_i = [(m_i + k) \mod 26]$
    - Muutke iga $c_i$ täheks vastavalt *D*-le
    - Seejärel ühendage $c_0, c_1, \ldots, c_l$, et saada krüptotekst $c$
- Dekrüpteerige krüptotekst $c$ järgmiselt:
    - Muutke iga $c_i$ arvuks vastavalt *D*-le
    - Iga $c_i$ jaoks, $m_i = [(c_i – k) \mod 26]$
    - Muutke iga $m_i$ täheks vastavalt *D*-le
    - Seejärel ühendage $m_0, m_1, \ldots, m_l$, et saada algne sõnum $m$

Modulo operaator nihkešifris tagab, et tähed lähevad ringi, nii et kõik krüptoteksti tähed on määratletud. Näiteks, kaaluge nihkešifri rakendamist sõnale “DOG”.

Eeldame, et olete valinud võtme väärtuseks 17. Täht “O” võrdub 15-ga. Ilma modulo operatsioonita lisanduks sellele algteksti numbrile võtmega krüptoteksti number 32. Siiski, seda krüptoteksti numbrit ei saa muuta krüptoteksti täheks, kuna inglise tähestikus on ainult 26 tähte. Modulo operatsioon tagab, et krüptoteksti number on tegelikult 6 (tulemus $32 \mod 26$), mis võrdub krüptoteksti tähega “G”.

Kogu sõna “DOG” krüpteerimine võtme väärtusega 17 on järgmine:

* Sõnum = DOG = D,O,G = 3,15,6
* $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
* $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
* $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
* $c = UGX$

Igaüks saab intuitiivselt aru, kuidas nihkešiffer töötab ja tõenäoliselt kasutab seda ise. Siiski, et edendada oma teadmisi krüptograafiast, on oluline hakata mugavamalt suhtuma formaliseerimisse, kuna skeemid muutuvad palju keerulisemaks. Seetõttu formaliseeriti nihkešifri sammud.

**Märkused:**

[1] Me saame seda väidet täpselt määratleda, kasutades eelmisest jaotisest terminoloogiat. Las ühtlane muutuja $K$ omab $K$ kui oma võimalike tulemuste komplekti. Nii:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...ja nii edasi. Valige ühtlane muutuja $K$ üks kord, et saada konkreetne võti.

## XOR operatsioon
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Kõik arvutiandmed töödeldakse, salvestatakse ja saadetakse võrkude kaudu bittide tasemel. Kõik krüptograafilised skeemid, mis rakendatakse arvutiandmetele, toimivad samuti bittide tasemel.

Näiteks, eeldame, et olete tippinud e-kirja oma e-posti rakendusse. Kõik krüpteeringud, mida rakendate, ei toimu otse teie e-kirja ASCII tähemärkidel. Selle asemel rakendatakse neid teie e-kirja tähtede ja teiste sümbolite bittide esitusele.
Kaasaegse krüptograafia mõistmiseks olulise matemaatilise operatsiooni, peale modulo operatsiooni, on **XOR operatsioon** ehk "eksklusiivne või" operatsioon. See operatsioon võtab sisendiks kaks bitti ja annab väljundiks teise biti. XOR operatsiooni tähistatakse lihtsalt kui "XOR". See annab väljundiks 0, kui kaks bitti on samad, ja 1, kui kaks bitti on erinevad. Allpool näete nelja võimalust. Sümbol $\oplus$ tähistab "XOR":
* $0 \oplus 0 = 0$
* $0 \oplus 1 = 1$
* $1 \oplus 0 = 1$
* $1 \oplus 1 = 0$

Illustratsiooniks, oletame, et teil on sõnum $m_1$ (01111001) ja sõnum $m_2$ (01011001). Nende kahe sõnumi XOR operatsiooni näete allpool.

* $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Protsess on lihtne. Kõigepealt teete XOR operatsiooni $m_1$ ja $m_2$ vasakpoolseimatele bittidele. Sel juhul on see $0 \oplus 0 = 0$. Seejärel teete XOR operatsiooni järgmisele bittide paarile vasakult. Sel juhul on see $1 \oplus 1 = 0$. Jätkate seda protsessi, kuni olete teinud XOR operatsiooni parempoolseimatele bittidele.

On lihtne näha, et XOR operatsioon on kommutatiivne, nimelt $m_1 \oplus m_2 = m_2 \oplus m_1$. Lisaks on XOR operatsioon ka assotsiatiivne. See tähendab, et $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

XOR operatsioon kahe erineva pikkusega stringi peal võib sõltuvalt kontekstist tähendada erinevaid asju. Me ei keskendu siin XOR operatsioonidele erineva pikkusega stringide puhul.

XOR operatsioon on ekvivalentne erijuhtumiga, kus teostatakse modulo operatsioon bittide liitmisele, kui jagaja on 2. Võrdluse võite näha järgmistes tulemustes:

* $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
* $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
* $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
* $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Pseudorandomness
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Arutelus juhuslike ja ühtlaste muutujate üle tegime konkreetse eristuse "juhusliku" ja "ühtlase" vahel. Praktikas säilitatakse seda eristust tavaliselt juhuslike muutujate kirjeldamisel. Kuid meie praeguses kontekstis tuleb see eristus ära jätta ja "juhuslik" ning "ühtlane" kasutatakse sünonüümidena. Ma selgitan põhjust selle jaotise lõpus.

Alustuseks võime nimetada binaarstringi pikkusega $n$ **juhuslikuks** (või **ühtlaseks**), kui see on tulemus ühtlase muutuja $S$ valimisel, mis annab igale sellise pikkusega binaarstringile võrdse tõenäosuse valituks saada.
Kujutage näiteks ette kõikide kaheksakohaliste binaarjärjestuste hulka: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Tavaliselt kirjutatakse 8-bitine järjestus kahe neliku kujul, mida nimetatakse **nibble**.) Nimetagem seda järjestuste hulka **$S_8$**.
Eelneva definitsiooni kohaselt võime siis nimetada konkreetset kaheksakohalist binaarjärjestust juhuslikuks (või ühtlaseks), kui see oli valitud ühtlase muutuja $S$ tulemusena, mis annab igale järjestusele hulgas **$S_8$** võrdse valiku tõenäosuse. Arvestades, et hulk **$S_8$** sisaldab $2^8$ elementi, peaks valimisel tõenäosus olema $1/2^8$ iga hulga järjestuse jaoks.

Binaarjärjestuse juhuslikkuse oluline aspekt on see, et see on määratletud viitega protsessile, mille kaudu see valiti. Seega ei paljasta ükski konkreetne binaarjärjestus iseenesest midagi oma juhuslikkuse kohta valikul.

Näiteks paljud inimesed intuitiivselt arvavad, et järjestust nagu $1111\ 1111$ ei oleks võimalik juhuslikult valida. Kuid see on selgelt vale.

Määratledes ühtlase muutuja $S$ kõigi kaheksakohaliste binaarjärjestuste üle, on $1111\ 1111$ valimise tõenäosus hulgast **$S_8$** sama, mis järjestuse $0111\ 0100$ puhul. Seega ei saa te järjestuse juhuslikkuse kohta midagi öelda, analüüsides ainult järjestust ennast.

Samuti võime rääkida juhuslikest järjestustest ilma, et see tähendaks spetsiifiliselt binaarjärjestusi. Võime näiteks rääkida juhuslikust heksajärjestusest $AF\ 02\ 82$. Sel juhul oleks järjestus valitud juhuslikult kõikide kuuekohaliste heksajärjestuste hulgast. See on samaväärne 24-kohalise binaarjärjestuse juhusliku valimisega, kuna iga heksadigitaal esindab 4 bitti.

Tavaliselt viitab väljend “juhuslik järjestus” ilma täpsustuseta järjestusele, mis on juhuslikult valitud kõikide sama pikkusega järjestuste hulgast. Just nii olen seda eespool kirjeldanud. Järjestust pikkusega $n$ võib muidugi juhuslikult valida ka mõnest teisest hulgast. Näiteks hulgast, mis koosneb ainult osast kõikidest $n$ pikkusega järjestustest, või ehk hulgast, mis sisaldab erineva pikkusega järjestusi. Sellistel juhtudel ei viitaks me sellele kui “juhuslik järjestus”, vaid pigem “järjestus, mis on juhuslikult valitud mingist hulgast **S**”.

Krüptograafia üks võtmekontseptsioone on pseudorandomness. **Pseudorandom järjestus** pikkusega $n$ tundub *nagu* see oleks valitud ühtlase muutuja $S$ tulemusena, mis annab igale järjestusele hulgas **$S_n$** võrdse valiku tõenäosuse. Tegelikult aga on järjestus valitud ühtlase muutuja $S'$ tulemusena, mis määratleb ainult tõenäosusjaotuse – mitte tingimata ühe, mis annab kõikidele võimalikele tulemustele võrdsed tõenäosused – mingi osa hulgast **$S_n$**. Oluline punkt siin on, et keegi ei suuda tegelikult eristada valimeid $S$ ja $S'$ vahel, isegi kui te võtate neid palju.
Kujutage ette näiteks juhuslikku muutujat $S$. Selle tulemuste hulk on **$S_{256}$**, mis on kõikide 256-bitiste binaarjärjestuste hulk. Selles hulgas on $2^{256}$ elementi. Igal elemendil on valimisel võrdne tõenäosus, $1/2^{256}$.

Lisaks kujutage ette juhuslikku muutujat $S'$. Selle tulemuste hulk sisaldab ainult $2^{128}$ 256-bitist binaarjärjestust. Nendel järjestustel on mingi tõenäosusjaotus, kuid see jaotus ei pruugi olla ühtlane.

Oletame nüüd, et võtsin 1000de proove muutujast $S$ ja 1000de proove muutujast $S'$ ning andsin teile mõlema tulemuste hulgad. Ma ütlen teile, milline tulemuste hulk on seotud millise juhusliku muutujaga. Järgmisena võtan proovi ühest kahest juhuslikust muutujast. Kuid seekord ei ütle ma teile, millist juhuslikku muutujat proovin. Kui $S'$ oleks pseudosuvaline, siis idee on, et teie tõenäosus teha õige arvamus selle kohta, millist juhuslikku muutujat proovisin, on praktiliselt mitte parem kui $1/2$.

Tavaliselt toodetakse pseudosuvaline järjestus pikkusega $n$, valides juhuslikult järjestuse suurusega $n – x$, kus $x$ on positiivne täisarv, ja kasutades seda sisendina laiendusalgoritmile. See juhuslik järjestus suurusega $n – x$ on tuntud kui **seeme**.

Pseudosuvalised järjestused on krüptograafia praktiliseks muutmise võtmekontseptsioon. Võtke näiteks voošifrid. Voošifri puhul ühendatakse juhuslikult valitud võti laiendusalgoritmiga, et toota palju suurem pseudosuvaline järjestus. See pseudosuvaline järjestus ühendatakse seejärel lähtetekstiga XOR-operatsiooni kaudu, et toota šifreeritud tekst.

Kui me ei suudaks toota sellist tüüpi pseudosuvalist järjestust voošifri jaoks, siis meil oleks vaja võtit, mis on sama pikk kui sõnum, selle turvalisuse tagamiseks. See ei ole enamikul juhtudel väga praktiline valik.

Selles jaotises arutatud pseudosuvalisuse mõistet saab defineerida formaalsemalt. See laieneb ka teistele kontekstidele. Kuid me ei pea siin seda arutelu süvendama. Kõik, mida te tegelikult peate intuitiivselt mõistma krüptograafia kohta, on erinevus suvalise ja pseudosuvalise järjestuse vahel. [2]

Põhjus, miks me loobume eristusest "suvaline" ja "ühtlane" meie arutelus, peaks nüüd samuti olema selge. Praktikas kasutavad kõik terminit pseudosuvaline, et viidata järjestusele, mis tundub **nagu** see oleks valitud ühtlase muutuja $S$ proovina. Rangelt öeldes peaksime sellist järjestust nimetama "pseudo-ühtlaseks", võttes meie keelekasutuse varasemast. Kuna termin "pseudo-ühtlane" on nii kohmakas ja keegi seda ei kasuta, siis me ei tutvusta seda siin selguse huvides. Selle asemel lihtsalt loobume eristusest "suvaline" ja "ühtlane" praeguses kontekstis.

**Märkused**

[2] Kui olete huvitatud nende küsimuste formaalsemast käsitlusest, võite konsulteerida Katz ja Lindell’i teosega *Introduction to Modern Cryptography*, eriti peatükk 3.


# Krüptograafia matemaatilised alused 2
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>




## Mis on arvuteooria?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>
See peatükk käsitleb keerukamat teemat krüptograafia matemaatilistest alustest: arvuteooriat. Kuigi arvuteooria on oluline sümmeetrilise krüptograafia jaoks (nagu Rijndaeli šiffer), on see eriti tähtis avaliku võtme krüptograafilises kontekstis.
Kui leiate, et arvuteooria üksikasjad on koormavad, soovitaksin esimesel lugemisel teha kõrgtasemel ülevaate. Hiljem võite alati selle juurde tagasi pöörduda.

___

**Arvuteooriat** võiks iseloomustada kui täisarvude omaduste ja matemaatiliste funktsioonide, mis töötavad täisarvudega, uurimist.

Võtke näiteks, et mis tahes kaks arvu $a$ ja $N$ on **teinetestisest priimid** (või **suhtelised priimarvud**), kui nende suurim ühistegur on 1. Oletame nüüd, et on olemas konkreetne täisarv $N$. Kui palju on täisarve, mis on väiksemad kui $N$ ja on $N$-ga teinetestisest priimid? Kas me saame sellele küsimusele vastamiseks teha üldistusi? Need on tüüpilised küsimused, millele arvuteooria püüab vastata.

Kaasaegne arvuteooria toetub abstraktse algebra vahenditele. **Abstraktne algebra** on matemaatika aladistsipliin, kus peamised analüüsiobjektid on abstraktsed objektid, mida tuntakse algebraaliste struktuuridena. **Algebraaline struktuur** on elementide kogum, mis on ühendatud ühe või mitme toiminguga, mis vastavad teatud aksioomidele. Algebraaliste struktuuride kaudu saavad matemaatikud saada ülevaate konkreetsetest matemaatilistest probleemidest, abstraherides nende detailidest.

Abstraktse algebra valdkonda nimetatakse mõnikord ka kaasaegseks algebraks. Võite samuti kohata mõistet **abstraktne matemaatika** (või **puhas matemaatika**). See viimane termin ei viita abstraktsele algebralle, vaid tähendab matemaatika uurimist iseenese pärast, mitte ainult potentsiaalsete rakenduste silmas pidades.

Abstraktse algebra kogumid võivad tegeleda paljude objektide tüüpidega, alates võrdkülgse kolmnurga kuju säilitavatest transformatsioonidest kuni tapeedimustriteni. Arvuteooria jaoks kaalume ainult elementide kogumeid, mis sisaldavad täisarve või funktsioone, mis töötavad täisarvudega.

## Grupid
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Matemaatikas on põhimõiste elementide kogum. Kogumit tähistatakse tavaliselt aksantsulgudega, elementide vahel komadega eraldatult.

Näiteks kõikide täisarvude kogum on $\{…, -2, -1, 0, 1, 2, …\}$. Siin tähendavad kolm punkti, et teatud muster jätkub kindlas suunas. Seega sisaldab kõikide täisarvude kogum ka $3, 4, 5, 6$ ja nii edasi, samuti $-3, -4, -5, -6$ ja nii edasi. Seda kõikide täisarvude kogumit tähistatakse tavaliselt $\mathbb{Z}$-ga.

Teine näide kogumist on $\mathbb{Z} \mod 11$, ehk kõikide täisarvude kogum modulo 11. Erinevalt kogu kogumist $\mathbb{Z}$, sisaldab see kogum ainult piiratud arvu elemente, nimelt $\{0, 1, \ldots, 9, 10\}$.
Levinud viga on arvata, et hulk $\mathbb{Z} \mod 11$ on tegelikult $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Kuid see ei vasta tõele, arvestades, kuidas me varem modulo tehet defineerisime. Kõik negatiivsed täisarvud, mida modulo 11 abil vähendatakse, koonduvad hulka $\{0, 1, \ldots, 9, 10\}$. Näiteks avaldis $-2 \mod 11$ koonduks väärtusele $9$, samal ajal kui avaldis $-27 \mod 11$ koonduks väärtusele $5$.

Teine põhiline mõiste matemaatikas on binaarne tehe. See on iga tehe, mis võtab kaks elementi, et toota kolmas. Näiteks, põhjalikust aritmeetikast ja algebrast teades, olete tuttav nelja fundamentaalse binaarse tehinguga: liitmine, lahutamine, korrutamine ja jagamine.

Neid kahte põhilist matemaatilist mõistet, hulki ja binaarseid tehinguid, kasutatakse grupi mõiste defineerimiseks, mis on abstraktse algebra kõige olulisem struktuur.

Eeldagem konkreetset binaarset tehet $\circ$. Lisaks eeldagem mõnda elementide hulka **S**, mis on varustatud selle tehtega. Kõik, mida "varustatud" siin tähendab, on see, et tehet $\circ$ saab sooritada mis tahes kahe elemendi vahel hulgas **S**.

Kombinatsioon $\langle \mathbf{S}, \circ \rangle$ on siis **grupp**, kui see vastab neljale konkreetsele tingimusele, mida tuntakse grupi aksioomidena.

1. Mis tahes $a$ ja $b$ puhul, mis on elementideks hulgas $\mathbf{S}$, on $a \circ b$ samuti elemendiks hulgas $\mathbf{S}$. Seda tuntakse **sulgemise tingimusena**.
2. Mis tahes $a$, $b$ ja $c$ puhul, mis on elementideks hulgas $\mathbf{S}$, kehtib, et $(a \circ b) \circ c = a \circ (b \circ c)$. Seda tuntakse **assotsiatiivsuse tingimusena**.
3. Hulgas $\mathbf{S}$ on unikaalne element $e$, nii et iga elemendi $a$ puhul hulgas $\mathbf{S}$ kehtib järgmine võrrand: $e \circ a = a \circ e = a$. Kuna selline element $e$ on ainus, nimetatakse seda **ühikelemendiks**. Seda tingimust tuntakse **ühikluse tingimusena**.
4. Iga elemendi $a$ puhul hulgas $\mathbf{S}$ eksisteerib element $b$ hulgas $\mathbf{S}$, nii et kehtib järgmine võrrand: $a \circ b = b \circ a = e$, kus $e$ on ühikelement. Elementi $b$ siin tuntakse kui **pöördelementi**, ja seda tähistatakse tavaliselt kui $a^{-1}$. Seda tingimust tuntakse **pööratavuse tingimusena**.

Vaadelgem gruppe veidi lähemalt. Tähistagem kõikide täisarvude hulka kui $\mathbb{Z}$. See hulk koos standardse liitmisega, ehk $\langle \mathbb{Z}, + \rangle$, vastab selgelt grupi definitsioonile, kuna see vastab eespool nimetatud neljale aksioomile.

1. Mis tahes $x$ ja $y$ puhul, mis on elementideks hulgas $\mathbb{Z}$, on $x + y$ samuti elemendiks hulgas $\mathbb{Z}$. Seega $\langle \mathbb{Z}, + \rangle$ vastab sulgemise tingimusele.
2. Iga $x$, $y$ ja $z$ korral, mis on elementideks hulgas $\mathbb{Z}$, kehtib $(x + y) + z = x + (y + z)$. Seega rühm $\langle \mathbb{Z}, + \rangle$ vastab assotsiatiivsuse tingimusele.
3. Hulgas $\langle \mathbb{Z}, + \rangle$ on olemas neutraalelement, nimelt 0. Iga $x$ korral hulgas $\mathbb{Z}$, kehtib, et: $0 + x = x + 0 = x$. Seega rühm $\langle \mathbb{Z}, + \rangle$ vastab neutraalelemendi tingimusele.
4. Lõpuks, iga elemendi $x$ korral hulgas $\mathbb{Z}$, leidub $y$ nii, et $x + y = y + x = 0$. Kui $x$ oleks näiteks 10, siis $y$ oleks $-10$ (juhul kui $x$ on 0, siis $y$ on samuti 0). Seega rühm $\langle \mathbb{Z}, + \rangle$ vastab pöördelemendi tingimusele.

Oluline on märkida, et kuigi täisarvude hulk koos liitmise tehtega moodustab rühma, ei tähenda see, et see moodustaks rühma korrutamise tehtega. Seda saab kontrollida, testides $\langle \mathbb{Z}, \cdot \rangle$ nelja rühma aksiioomi vastu (kus $\cdot$ tähistab standardset korrutamist).

Esimesed kaks aksiioomi ilmselgelt kehtivad. Lisaks, korrutamise korral võib element 1 toimida neutraalelemendina. Iga täisarv $x$, korrutatuna 1-ga, annab tulemuseks $x$. Siiski, $\langle \mathbb{Z}, \cdot \rangle$ ei vasta pöördelemendi tingimusele. See tähendab, et iga $x$ korral hulgas $\mathbb{Z}$ ei leidu unikaalset elementi $y$, nii et $x \cdot y = 1$.

Näiteks, oletame, et $x = 22$. Milline väärtus $y$ hulgast $\mathbb{Z}$, korrutatuna $x$-ga, annaks neutraalelemendi 1? Väärtus $1/22$ sobiks, kuid see ei kuulu hulka $\mathbb{Z}$. Tegelikult tekib see probleem iga täisarvu $x$ puhul, välja arvatud väärtuste 1 ja -1 puhul (kus $y$ peaks vastavalt olema 1 ja -1).

Kui me lubaksime meie hulka reaalarvud, siis meie probleemid suuresti kaoksid. Iga elemendi $x$ korral hulgas, korrutamine $1/x$-ga annab 1. Kuna murdarvud kuuluvad reaalarvude hulka, leidub pöördelement iga reaalarvu jaoks. Erandiks on null, kuna ükskõik milline korrutamine nulliga ei anna kunagi neutraalelementi 1. Seega, nullist erinevate reaalarvude hulk koos korrutamise tehtega on tõepoolest rühm.

Mõned rühmad vastavad viiendale üldtingimusele, mida tuntakse **kommutatiivsuse tingimusena**. See tingimus on järgmine:

* Oletame rühma $G$ hulgaga **S** ja binaarse operaatoriga $\circ$. Oletame, et $a$ ja $b$ on elementideks hulgas **S**. Kui kehtib, et $a \circ b = b \circ a$ mis tahes kahe elemendi $a$ ja $b$ korral hulgas **S**, siis $G$ vastab kommutatiivsuse tingimusele.
Iga rühm, mis vastab kommutatiivsuse tingimusele, on tuntud kui **kommutatiivne rühm** või **Abeli rühm** (pärast Niels Henrik Abeli). On lihtne tõestada, et nii reaalarvude hulk liitmise teel kui ka täisarvude hulk liitmise teel on Abeli rühmad. Täisarvude hulk korrutamise teel ei ole üldse rühm, seega ei saa see olla Abeli rühm. Seevastu nullist erinevate reaalarvude hulk korrutamise teel on samuti Abeli rühm.
Peate järgima kahte olulist notatsiooni konventsiooni. Esiteks, märgid “+” või “×” kasutatakse sageli rühmaoperatsioonide sümboliseerimiseks, isegi kui elemendid ei ole tegelikult arvud. Sellistel juhtudel ei tohiks neid märke tõlgendada standardse aritmeetilise liitmise või korrutamisena. Selle asemel on need operatsioonid, millel on ainult abstraktne sarnasus nende aritmeetiliste operatsioonidega.

Kui te ei viita spetsiifiliselt aritmeetilisele liitmisele või korrutamisele, on lihtsam kasutada rühmaoperatsioonide jaoks sümboleid nagu $\circ$ ja $\diamond$, kuna neil ei ole väga kultuuriliselt juurdunud tähendusi.

Teiseks, samal põhjusel, miks “+” ja “×” kasutatakse sageli mittearitmeetiliste operatsioonide näitamiseks, sümboliseeritakse rühmade ühikelemente sageli “0” ja “1” abil, isegi kui nende rühmade elemendid ei ole arvud. Kui te ei viita rühma ühikelemendile, mis on arvudega, on lihtsam kasutada neutraalsemat sümbolit nagu “$e$” ühikelemendi näitamiseks.

Matemaatikas on palju erinevaid ja väga olulisi väärtuste hulki, mis on varustatud teatud binaarsete operatsioonidega, ja need on rühmad. Krüptograafilised rakendused töötavad siiski ainult täisarvude hulkadega või vähemalt elementidega, mida kirjeldatakse täisarvudena, st arvuteooria valdkonnas. Seetõttu ei kasutata krüptograafilistes rakendustes reaalarvude hulki, mis on muud kui täisarvud.

Lõpetuseks toome näite elementidest, mida saab “kirjeldada täisarvudena”, kuigi need ei ole täisarvud. Hea näide on elliptiliste kõverate punktid. Kuigi ükski punkt elliptilisel kõveral ei ole selgelt täisarv, kirjeldatakse sellist punkti tõepoolest kahe täisarvuga.

Elliptilised kõverad on näiteks Bitcoini jaoks hädavajalikud. Iga standardne Bitcoini privaatne ja avalik võtmepaar valitakse punktide hulgast, mida määratleb järgmine elliptiline kõver:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(suurim algarv, mis on väiksem kui $2^{256}$). $x$-koordinaat on privaatvõti ja $y$-koordinaat on teie avalik võti.

Bitcoinis tehingute tegemine hõlmab tavaliselt väljundite lukustamist ühele või mitmele avalikule võtmele mingil viisil. Nende tehingute väärtus saab seejärel avada, tehes digitaalseid allkirju vastavate privaatvõtmetega.

## Tsüklilised rühmad
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Üks oluline eristus, mida saame teha, on **lõpliku** ja **lõpmatute rühmade** vahel. Esimesel on lõplik arv elemente, samas kui teisel on lõpmatu arv elemente. Mis tahes lõpliku rühma elementide arvu nimetatakse rühma **järjeks**. Kõik praktiline krüptograafia, mis hõlmab rühmade kasutamist, toetub lõplikele (arvuteoreetilistele) rühmadele.

Avaliku võtme krüptograafias on eriti oluline teatud klass lõplikke Abeli rühmi, mida tuntakse tsükliliste rühmadena. Tsükliliste rühmade mõistmiseks peame esmalt mõistma rühmaelemendi eksponenteerimise kontseptsiooni.
Eeldame, et on grupp $G$ koos grupioperatsiooniga $\circ$, ja et $a$ on elemendiks grupis $G$. Avaldist $a^n$ tuleks seega tõlgendada kui elementi $a$, mis on kombineeritud iseendaga kokku $n – 1$ korda. Näiteks, $a^2$ tähendab $a \circ a$, $a^3$ tähendab $a \circ a \circ a$ ja nii edasi. (Märkus: siin ei pruugi eksponenteerimine olla tingimata eksponenteerimine standardse aritmeetika mõttes.)

Pöördugem näite poole. Eeldame, et $G = \langle \mathbb{Z} \mod 7, + \rangle$, ja et meie väärtus $a$ võrdub 4-ga. Sel juhul, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternatiivselt, $a^4$ esindaks $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Mõned Abeli grupid omavad ühte või mitut elementi, mis võivad jätkuva eksponenteerimise teel anda kõik teised grupi elemendid. Neid elemente nimetatakse **generaatoriteks** või **primitiivelementideks**.

Üks selliste gruppide oluline klass on $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, kus $N$ on algarv. Notatsioon $\mathbb{Z}^*$ tähendab siin, et grupp sisaldab kõiki nullist erinevaid positiivseid täisarve, mis on väiksemad kui $N$. Sellisel grupil on seega alati $N – 1$ elementi.

Vaatleme näiteks $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Sellel grupil on järgmised elemendid: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Selle grupi järk on 10 (mis tõepoolest võrdub $11 – 1$).

Uurime elemendi 2 eksponenteerimist selles grupis. Arvutused kuni $2^{12}$ on allpool näidatud. Pange tähele, et võrrandi vasakul küljel viitab eksponent grupielemendi eksponenteerimisele. Meie konkreetse näite puhul hõlmab see tõepoolest aritmeetilist eksponenteerimist võrrandi paremal küljel (aga see oleks võinud hõlmata näiteks ka liitmist). Selgituseks olen välja kirjutanud korduva operatsiooni, mitte eksponendivormi paremal küljel.

* $2^1 = 2 \mod 11$
* $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
* $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
* $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
* $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
* $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
* $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
* $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
* $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
* $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
* $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
* $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Kui vaadata hoolikalt, võib märgata, et elementi 2 astendades läbitakse kõik $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ elemendid järgmises järjekorras: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Pärast $2^{10}$, elementi 2 edasi astendades, läbitakse kõik elemendid uuesti ja samas järjekorras. Seega on element 2 generaator $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$-s.

Kuigi $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$-l on mitu generaatorit, ei ole kõik selle grupi elemendid generaatorid. Võtame näiteks elemendi 3. Esimese 10 astendamise läbimine, ilma tülikaid arvutusi näitamata, annab järgmised tulemused:

* $3^1 = 3 \mod 11$
* $3^2 = 9 \mod 11$
* $3^3 = 5 \mod 11$
* $3^4 = 4 \mod 11$
* $3^5 = 1 \mod 11$
* $3^6 = 3 \mod 11$
* $3^7 = 9 \mod 11$
* $3^8 = 5 \mod 11$
* $3^9 = 4 \mod 11$
* $3^{10} = 1 \mod 11$
Selle asemel, et läbida kõik väärtused $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ juures, elemendi 3 astendamine toob esile ainult osa neist väärtustest: 3, 9, 5, 4 ja 1. Pärast viiendat astendamist hakkavad need väärtused korduma.
Nüüd saame defineerida **tsüklilise grupi** kui iga grupi, millel on vähemalt üks generaator. See tähendab, et on olemas vähemalt üks grupi element, millest saab teisi grupi elemente toota astendamise teel.

Võib-olla olete märganud meie eespool toodud näites, et nii $2^{10}$ kui ka $3^{10}$ võrdub $1 \mod 11$-ga. Tegelikult, kuigi me ei tee arvutusi, toob grupi $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ mis tahes elemendi astendamine 10-ga kaasa $1 \mod 11$. Miks see nii on?

See on oluline küsimus, kuid vastuse leidmiseks on vaja teha mõningast tööd.

Alustuseks eeldame kahte positiivset täisarvu $a$ ja $N$. Üks oluline teoreem arvuteoorias väidab, et $a$-l on korrutise pöördarv modulo $N$ (st täisarv $b$ nii, et $a \cdot b = 1 \mod N$) ainult siis, kui $a$ ja $N$ suurim ühistegur võrdub 1-ga. See tähendab, kui $a$ ja $N$ on teineteisega võõrad.

Seega, mis tahes täisarvude grupis, mis on varustatud korrutamisega modulo $N$, on komplektis ainult $N$-ga võõrad väiksemad täisarvud. Me võime seda komplekti tähistada kui $\mathbb{Z}^c \mod N$.

Näiteks, eeldame, et $N$ on 10. Ainult täisarvud 1, 3, 7 ja 9 on 10-ga võõrad. Seega komplekt $\mathbb{Z}^c \mod 10$ sisaldab ainult $\{1, 3, 7, 9\}$. Te ei saa luua gruppi täisarvude korrutamisega modulo 10, kasutades muid täisarve vahemikus 1 kuni 10. Selle konkreetse grupi jaoks on pöördarvudeks paarid 1 ja 9 ning 3 ja 7.

Juhtumil, kui $N$ ise on algarv, on kõik täisarvud 1-st kuni $N – 1$-ni $N$-ga võõrad. Sellisel grupil on seega järk $N – 1$. Kasutades meie varasemat tähistust, $\mathbb{Z}^c \mod N$ võrdub $\mathbb{Z}^* \mod N$-ga, kui $N$ on algarv. Grupp, mille me oma varasemas näites valisime, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, on selle klassi gruppide konkreetne näide.

Järgmisena, funktsioon $\phi(N)$ arvutab võõraste arvu kuni numbrini $N$ ja on tuntud kui **Euleri fi-funktsioon**. [1] Vastavalt **Euleri teoreemile**, kui kaks täisarvu $a$ ja $N$ on võõrad, kehtib järgmine:

* $a^{\phi(N)} \mod N = 1 \mod N$
Sellel on oluline tähendus rühmade klassi $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ jaoks, kus $N$ on algarv. Nende rühmade puhul esindab rühmaelemendi eksponenteerimine aritmeetilist eksponenteerimist. See tähendab, et $a^{\phi(N)} \mod N$ esindab aritmeetilist toimingut $a^{\phi(N)} \mod N$. Kuna iga element $a$ nendes korrutusrühmades on algarvuga $N$ võõras, tähendab see, et $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.

Euleri teoreem on tõesti oluline tulemus. Alustuseks tähendab see, et kõik elemendid rühmas $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ saavad eksponenteerimisel läbida ainult teatud arvu väärtusi, mis jagunevad arvuga $N – 1$. Näiteks rühma $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ puhul tähendab see, et iga element saab läbida ainult 2, 5 või 10 elementi. Grupi väärtused, mille kaudu iga element eksponenteerimisel läbib, on tuntud kui **elemendi järk**. Element, mille järk on võrdne grupi järjega, on generaator.

Lisaks tähendab Euleri teoreem, et me saame alati teada tulemuse $a^{N – 1} \mod N$ mis tahes rühma $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ jaoks, kus $N$ on algarv. See kehtib sõltumata sellest, kui keerulised tegelikud arvutused võivad olla.

Näiteks, kui meie rühm on $\mathbb{Z}^* \mod 160,481,182$ (kus 160,481,182 on tõepoolest algarv). Me teame, et kõik täisarvud 1 kuni 160,481,181 peavad olema selle rühma elemendid ja et $\phi(n) = 160,481,181$. Kuigi me ei saa teha kõiki arvutusetappe, teame, et avaldised nagu $514^{160,481,181}$, $2,005^{160,481,181}$ ja $256,212^{160,481,181}$ peavad kõik võrduma $1 \mod 160,481,182$.

**Märkused:**

[1] Funktsioon toimib järgmiselt. Iga täisarv $N$ saab faktoriseerida algarvude korrutiseks. Eeldame, et konkreetne $N$ on faktoriseeritud järgmiselt: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$, kus kõik $p$’d on algarvud ja kõik $e$’d on täisarvud, mis on suuremad või võrdsed 1-ga. Siis:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Euleri Phi funktsiooni valem $N$ algarvude faktoriseerimiseks.

## Väljad
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Rühm on abstraktse algebra põhiline algebraaline struktuur, kuid on palju rohkem. Ainus teine algebraaline struktuur, millega peate tuttav olema, on **väli**, eriti **lõplik väli**. Seda tüüpi algebraaline struktuur on krüptograafias sageli kasutusel, näiteks Advanced Encryption Standardis. Viimane on peamine sümmeetriline krüpteerimisskeem, millega te praktikas kokku puutute.
Väli on tuletatud grupi mõistest. Täpsemalt, **väli** on elementide hulk **S**, mis on varustatud kahe binaarse operaatoriga $\circ$ ja $\diamond$, mis vastavad järgmistele tingimustele:
1. Hulgal **S**, mis on varustatud $\circ$-ga, on Abeli grupp.
2. Hulgal **S**, mis on varustatud $\diamond$-ga, on Abeli grupp "nullist erinevate" elementide jaoks.
3. Hulgal **S**, mis on varustatud kahe operaatoriga, on täidetud nn distributiivne tingimus: Eeldame, et $a$, $b$ ja $c$ on hulga **S** elemendid. Siis hulk **S**, mis on varustatud kahe operaatoriga, vastab distributiivsele omadusele, kui $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Märkige, et nagu gruppide puhul, on välja definitsioon väga abstraktne. See ei tee väiteid elementide tüüpide kohta hulgas **S** ega operaatorite $\circ$ ja $\diamond$ kohta. See lihtsalt väidab, et väli on iga elementide hulk kahe operatsiooniga, mille puhul kehtivad kolm eespool nimetatud tingimust. (Teises Abeli grupis olevat "null" elementi saab abstraktselt tõlgendada.)

Niisiis, mis võiks olla välja näide? Hea näide on hulk $\mathbb{Z} \mod 7$, ehk $\{0, 1, \ldots, 7\}$, mis on defineeritud standardse liitmise (asendus $\circ$ ülal) ja standardse korrutamise (asendus $\diamond$ ülal) üle.

Esiteks, $\mathbb{Z} \mod 7$ vastab tingimusele, et olla Abeli grupp liitmise üle, ja see vastab tingimusele, et olla Abeli grupp korrutamise üle, kui arvestada ainult nullist erinevaid elemente. Teiseks, hulga kombinatsioon kahe operaatoriga vastab distributiivsele tingimusele.

On didaktiliselt kasulik uurida neid väiteid, kasutades mõningaid konkreetseid väärtusi. Võtame katseväärtusteks 5, 2 ja 3, mõned juhuslikult valitud elemendid hulgast $\mathbb{Z} \mod 7$, et uurida välja $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Kasutame neid kolme väärtust järjekorras, nagu on vaja konkreetsete tingimuste uurimiseks.

Uurigem esmalt, kas $\mathbb{Z} \mod 7$, mis on varustatud liitmisega, on Abeli grupp.

1. **Sulgemise tingimus**: Võtame meie väärtusteks 5 ja 2. Sel juhul $[5 + 2] \mod 7 = 7 \mod 7 = 0$. See on tõepoolest element hulgast $\mathbb{Z} \mod 7$, nii et tulemus on kooskõlas sulgemise tingimusega.
2. **Assotsiatiivsuse tingimus**: Võtame meie väärtusteks 5, 2 ja 3. Sel juhul $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. See on kooskõlas assotsiatiivsuse tingimusega.
3. **Identiteedi tingimus**: Võtame meie väärtuseks 5. Sel juhul $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Nii et 0 tundub olevat identiteedielement liitmise jaoks.
4. **Pöördtingimus**: Kaalugem 5 pöördväärtust. Peab kehtima, et $[5 + d] \mod 7 = 0$ mingi väärtuse $d$ jaoks. Sel juhul on unikaalne väärtus hulgast $\mathbb{Z} \mod 7$, mis rahuldab seda tingimust, 2.5. **Kommutatiivsuse tingimus**: Võtame väärtusteks 5 ja 3. Sel juhul on $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. See on kooskõlas kommutatiivsuse tingimusega.

Hulk $\mathbb{Z} \mod 7$, varustatud liitmisega, tundub selgelt olevat Abeli grupp. Uurime nüüd, kas $\mathbb{Z} \mod 7$, varustatud korrutamisega, on Abeli grupp kõigi nullist erinevate elementide jaoks.

1. **Sulgemise tingimus**: Võtame väärtusteks 5 ja 2. Sel juhul on $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. See on samuti element hulgast $\mathbb{Z} \mod 7$, seega tulemus on kooskõlas sulgemise tingimusega.
2. **Assotsiatiivsuse tingimus**: Võtame väärtusteks 5, 2 ja 3. Sel juhul on $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. See on kooskõlas assotsiatiivsuse tingimusega.
3. **Identiteedi tingimus**: Võtame väärtuseks 5. Sel juhul on $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Seega tundub 1 olevat korrutamise identiteetelement.
4. **Pöördtingimus**: Kaalugem 5 pöördväärtust. Peab kehtima, et $[5 \cdot d] \mod 7 = 1$, mingi väärtuse $d$ jaoks. Unikaalne väärtus hulgast $\mathbb{Z} \mod 7$, mis rahuldab seda tingimust, on 3. See on kooskõlas pöördtingimusega.
5. **Kommutatiivsuse tingimus**: Võtame väärtusteks 5 ja 3. Sel juhul on $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. See on kooskõlas kommutatiivsuse tingimusega.

Hulk $\mathbb{Z} \mod 7$ tundub selgelt vastavat Abeli grupi reeglitele, kui see on ühendatud kas liitmise või korrutamisega nullist erinevate elementide jaoks.

Lõpuks tundub, et see hulk koos mõlema tehtega vastab distributiivsuse tingimusele. Võtame väärtusteks 5, 2 ja 3. Näeme, et $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Oleme nüüd näinud, et $\mathbb{Z} \mod 7$, varustatud nii liitmise kui ka korrutamisega, vastab lõpliku korpuse aksioomidele, testides konkreetsete väärtustega. Muidugi võime seda üldiselt ka näidata, kuid ei tee seda siin.

Oluline eristus on kahe tüüpi korpuste vahel: lõplikud ja lõpmatud korpused.
**Lõpmatu väli** hõlmab valda, kus hulk **S** on lõpmatult suur. Reaalarvude hulk $\mathbb{R}$ koos liitmise ja korrutamisega on näide lõpmatust väljast. **Lõplik väli**, tuntud ka kui **Galois' väli**, on väli, kus hulk **S** on lõplik. Meie eespool toodud näide $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ on lõplik väli.
Krüptograafias huvitame me peamiselt lõplikest väljadest. Üldiselt on võimalik näidata, et lõplik väli eksisteerib mingi elementide hulga **S** jaoks, kui ja ainult kui selles on $p^m$ elementi, kus $p$ on algarv ja $m$ positiivne täisarv, mis on suurem või võrdne ühega. Teisisõnu, kui mingi hulga **S** järk on algarv ($p^m$, kus $m = 1$) või mõne algarvu astendaja ($p^m$, kus $m > 1$), siis leiate kaks tehet $\circ$ ja $\diamond$, nii et välja tingimused on täidetud.

Kui mõnel lõplikul väljal on algarvude arv elemente, siis nimetatakse seda **primaarväljaks**. Kui lõpliku välja elementide arv on algarvu astendaja, siis nimetatakse välja **laiendusväljaks**. Krüptograafias huvitavad meid nii primaar- kui ka laiendusväljad. [2]

Krüptograafia peamised primaarväljad on need, kus kõikide täisarvude hulk moduleeritakse mingi algarvuga ja tehted on standardne liitmine ja korrutamine. See lõplike väljade klass hõlmaks $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$ ja nii edasi. Mis tahes primaarvälja $\mathbb{Z} \mod p$ puhul on välja täisarvude hulk järgmine: $\{0, 1, \ldots, p – 2, p – 1\}$.

Krüptograafias huvitavad meid ka laiendusväljad, eriti need väljad, millel on $2^m$ elementi, kus $m > 1$. Selliseid lõplikke välju kasutatakse näiteks Rijndaeli šifris, mis on Advanced Encryption Standardi aluseks. Kuigi primaarväljad on suhteliselt intuitiivsed, ei pruugi need baas 2 laiendusväljad olla arusaadavad neile, kes ei ole tuttavad abstraktse algebraga.

Alustuseks on tõesti tõsi, et igale täisarvude hulgale, millel on $2^m$ elementi, saab määrata kaks tehet, mis muudaks nende kombinatsiooni väljaks (niikaua kui $m$ on positiivne täisarv). Kuid pelgalt välja olemasolu ei tähenda tingimata, et see on kergesti avastatav või eriti praktiline teatud rakendustes.

Nagu selgub, on krüptograafias eriti rakendatavad laiendusväljad $2^m$, mis on määratletud eriliste polünoomiliste avaldiste hulkade üle, mitte mingi täisarvude hulga põhjal.

Näiteks, kui me tahaksime laiendusvälja, millel on $2^3$ (st 8) elementi hulgas. Kuigi võib olla palju erinevaid hulki, mida saab sellise suurusega väljade jaoks kasutada, hõlmab üks selline hulk kõiki unikaalseid polünoome kujul $a_2x^2 + a_1x + a_0$, kus iga koefitsient $a_i$ on kas 0 või 1. Seega sisaldab see hulk **S** järgmisi elemente:
1. $0$: Juhtum, kus $a_2 = 0$, $a_1 = 0$ ja $a_0 = 0$.
2. $1$: Juhtum, kus $a_2 = 0$, $a_1 = 0$ ja $a_0 = 1$.
3. $x$: Juhtum, kus $a_2 = 0$, $a_1 = 1$ ja $a_0 = 0$.
4. $x + 1$: Juhtum, kus $a_2 = 0$, $a_1 = 1$ ja $a_0 = 1$.
5. $x^2$: Juhtum, kus $a_2 = 1$, $a_1 = 0$ ja $a_0 = 0$.
6. $x^2 + 1$: Juhtum, kus $a_2 = 1$, $a_1 = 0$ ja $a_0 = 1$.
7. $x^2 + x$: Juhtum, kus $a_2 = 1$, $a_1 = 1$ ja $a_0 = 0$.
8. $x^2 + x + 1$: Juhtum, kus $a_2 = 1$, $a_1 = 1$ ja $a_0 = 1$.

Niisiis oleks **S** hulk $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Millised kaks tehet saab määratleda selle elementide hulga üle, et tagada nende kombinatsioon on väli?

Esimene tehe hulgal **S** ($\circ$) saab määratleda kui standardne polünoomide liitmine modulo 2. Kõik, mida peate tegema, on liita polünoomid nagu tavaliselt ja seejärel rakendada modulo 2 iga saadud polünoomi koefitsiendile. Siin on mõned näited:

* $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
* $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
* $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

Teine tehe hulgal **S** ($\diamond$), mis on vajalik välja loomiseks, on keerulisem. See on teatud liiki korrutamine, kuid mitte standardne aritmeetiline korrutamine. Selle asemel peate iga elementi vaatama kui vektorit ja mõistma tehet kui nende kahe vektori korrutamist modulo redutseerimatu polünoomiga.

Alustame redutseerimatu polünoomi mõistest. **Redutseerimatu polünoom** on selline, mida ei saa faktoriseerida (nagu ka algarvu ei saa faktoriseerida komponentideks peale 1 ja algarvu enda). Meie eesmärgil huvitavad meid polünoomid, mis on redutseerimatud kõigi täisarvude hulgas. (Pane tähele, et teatud polünoome võib olla võimalik faktoriseerida, näiteks kasutades reaalarve või kompleksarve, isegi kui neid ei saa faktoriseerida kasutades täisarve.)
Näiteks kaaluge polünoomi $x^2 - 3x + 2$. Seda saab ümber kirjutada kujule $(x – 1)(x – 2)$. Seega see ei ole redutseerimatu. Nüüd kaaluge polünoomi $x^2 + 1$. Kasutades ainult täisarve, ei ole võimalik seda avaldist edasi faktoriseerida. Seega on see redutseerimatu polünoom täisarvude suhtes.

Järgmisena pöördume vektorite korrutamise kontseptsiooni juurde. Me ei uurita seda teemat süvitsi, kuid peate mõistma üht põhireeglit: Iga vektori jagamine on võimalik, kuni jagataval on kraad, mis on kõrgem või võrdne jagaja kraadiga. Kui jagataval on madalam kraad kui jagajal, siis jagatavat ei saa enam jagaja poolt jagada.

Näiteks kaaluge avaldist $x^6 + x + 1 \mod x^5 + x^2$. See väheneb edasi, kuna jagatava kraad, 6, on kõrgem kui jagaja kraad, 5. Nüüd kaaluge avaldist $x^5 + x + 1 \mod x^5 + x^2$. See väheneb samuti edasi, kuna jagatava kraad, 5, ja jagaja kraad, 5, on võrdsed.

Kuid nüüd kaaluge avaldist $x^4 + x + 1 \mod x^5 + x^2$. See ei vähene edasi, kuna jagatava kraad, 4, on madalam kui jagaja kraad, 5.

Selle teabe põhjal oleme nüüd valmis leidma meie teise operatsiooni komplektile $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Olen juba öelnud, et teist operatsiooni tuleks mõista kui vektorite korrutamist modulo mingi redutseerimatu polünoomi järgi. See redutseerimatu polünoom peaks tagama, et teine operatsioon määratleb Abeli grupi üle **S** ja on kooskõlas distributiivse tingimusega. Milline peaks olema see redutseerimatu polünoom?

Kuna kõik komplekti vektorid on kraadiga 2 või madalamad, peaks redutseerimatu polünoom olema kraadiga 3. Kui komplekti kahe vektori korrutamine annab polünoomi kraadiga 3 või kõrgem, teame, et modulo polünoom kraadiga 3 annab alati polünoomi kraadiga 2 või madalam. See on nii, kuna iga polünoom kraadiga 3 või kõrgem on alati jagatav polünoomiga kraadiga 3. Lisaks peab jagajana toimiv polünoom olema redutseerimatu.

Selgub, et on mitmeid redutseerimatuid polünoome kraadiga 3, mida me võiksime kasutada meie jagajana. Iga selline polünoom määratleb koos meie komplektiga **S** ja liitmisega modulo 2 erineva välja. See tähendab, et krüptograafias laiendväljade $2^m$ kasutamisel on teil mitu võimalust.

Meie näite puhul eeldagem, et valime polünoomi $x^3 + x + 1$. See on tõepoolest redutseerimatu, kuna te ei saa seda faktoriseerida kasutades täisarve. Lisaks tagab see, et kahe elemendi korrutamine annab alati polünoomi kraadiga 2 või vähem.
Töötame läbi näite teisest operatsioonist, kasutades jagajana polünoomi $x^3 + x + 1$, et illustreerida, kuidas see toimib. Eeldame, et korrutate elemendid $x^2 + 1$ ja $x^2 + x$ meie hulgas **S**. Seejärel peame arvutama avaldise $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Seda saab lihtsustada järgmiselt:
* $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
* $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
* $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Teame, et $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ saab vähendada, kuna jagataval on kõrgem aste (4) kui jagajal (3).

Alustuseks võite näha, et avaldis $x^3 + x + 1$ läheb $x^4 + x^3 + x^2 + x$ sisse kokku $x$ korda. Seda saate kontrollida, korrutades $x^3 + x + 1$ läbi $x$-ga, mis on $x^4 + x^2 + x$. Kuna viimane termin on sama astmega kui jagatav, nimelt 4, teame, et see töötab. Jagamise jääki $x$ abil saate arvutada järgmiselt:

* $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
* $[x^3] \mod x^3 + x + 1 =$
* $x^3$

Niisiis, pärast $x^4 + x^3 + x^2 + x$ jagamist $x^3 + x + 1$-ga kokku $x$ korda, on meil jääk $x^3$. Kas seda saab veel jagada $x^3 + x + 1$-ga?

Intuitiivselt võib tunduda ahvatlev öelda, et $x^3$ ei saa enam jagada $x^3 + x + 1$-ga, kuna viimane termin tundub suurem. Siiski, meenutage meie varasemat arutelu vektorite jagamise üle. Niikaua kui jagataval on astme suurus sama suur või suurem kui jagajal, saab avaldist edasi vähendada. Konkreetselt, avaldis $x^3 + x + 1$ saab minna $x^3$ sisse täpselt 1 kord. Jääk arvutatakse järgmiselt:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Võite imestada, miks $(x^3) - (x^3 + x + 1)$ võrdub $x + 1$ ja mitte $-x - 1$-ga. Pidage meeles, et meie välja esimene operatsioon on defineeritud modulo 2 järgi. Seega, kahe vektori lahutamine annab täpselt sama tulemuse kui kahe vektori liitmine.
Kokkuvõtteks, korrutades $x^2 + 1$ ja $x^2 + x$: Kui korrutate neid kahte terminit, saate neljanda astme polünoomi, $x^4 + x^3 + x^2 + x$, mida tuleb vähendada modulo $x^3 + x + 1$ järgi. Neljanda astme polünoom jaguneb $x^3 + x + 1$ täpselt $x + 1$ korda. Jääk pärast $x^4 + x^3 + x^2 + x$ jagamist $x^3 + x + 1$ täpselt $x + 1$ korda on $x + 1$. See on tõepoolest element meie komplektis $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.
Miks võiksid laiendatud väljad alusega 2 üle polünoomide komplektide, nagu eespool toodud näites, olla krüptograafia jaoks kasulikud? Põhjus on selles, et polünoomide koefitsiente sellistes komplektides, kas 0 või 1, võib vaadelda kui binaarstringide elemente kindla pikkusega. Meie eespool toodud näite komplekt **S** võiks näiteks olla vaadeldav hoopis kui komplekt **S**, mis sisaldab kõiki kolme pikkusega binaarstringe (000 kuni 111). Seega võib **S**-il toimuvaid operatsioone kasutada ka nende binaarstringide operatsioonide sooritamiseks ja sama pikkusega binaarstringi tootmiseks.

**Märkused:**

[2] Laiendatud väljad muutuvad väga vastuoluliseks. Erinevalt täisarvude elementidest on neil polünoomide komplektid. Lisaks sooritatakse kõik operatsioonid modulo mõne redutseerimatu polünoomi järgi.

## Abstraktne algebra praktikas
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Hoolimata ametlikust keelekasutusest ja arutelu abstraktsusest, ei tohiks grupi kontseptsioon olla liiga keeruline mõistmiseks. See on lihtsalt elementide kogum koos binaarse operatsiooniga, kus selle binaarse operatsiooni sooritamine nendel elementidel vastab neljale üldisele tingimusele. Abelia rühmal on lihtsalt üks lisatingimus, mida tuntakse kommutatiivsusena. Tsükliline rühm omakorda on eriline liik Abelia rühmast, nimelt selline, millel on generaator. Väli on lihtsalt keerukam konstruktsioon baasilise grupi mõistest.

Kuid kui olete praktiliselt meelestatud inimene, võite sel hetkel mõelda: Kes hoolib? Kas teadmine, et mingi elementide kogum koos operaatoriga on rühm, või isegi Abelia või tsükliline rühm, omab mingit reaalset tähtsust? Kas teadmine, et midagi on väli?

Ilma liiga palju detailidesse laskumata on vastus “jah”. Rühmad loodi esmakordselt 19. sajandil Prantsuse matemaatiku Evariste Galois' poolt. Ta kasutas neid järelduste tegemiseks polünoomvõrrandite lahendamise kohta, mille aste oli suurem kui viis.

Sellest ajast alates on grupi kontseptsioon aidanud valgust heita mitmetele probleemidele matemaatikas ja mujal. Näiteks füüsik Murray-Gellman suutis nende alusel ennustada osakese olemasolu enne selle tegelikku vaatlust eksperimentides. [3] Teise näitena kasutavad keemikud grupiteooriat molekulide kujude klassifitseerimiseks. Matemaatikud on isegi kasutanud grupi kontseptsiooni järelduste tegemiseks midagi nii konkreetset kui tapeet!
Põhimõtteliselt näitab see, et elementide kogum koos mingi tehtega on grupp, tähendab, et teie kirjeldatav omab teatud sümmeetriat. Mitte sümmeetriat tavapärases mõttes, vaid abstraktsemas vormis. Ja see võib pakkuda olulist teavet konkreetsete süsteemide ja probleemide kohta. Abstraktse algebra keerukamad mõisted annavad meile lisateavet.
Kõige tähtsamalt näete te arvuteoreetiliste gruppide ja väljade tähtsust praktikas nende rakendamise kaudu krüptograafias, eriti avaliku võtme krüptograafias. Oleme juba arutanud väljade puhul, näiteks kuidas laiendatud välju kasutatakse Rijndaeli šifris. Töötame selle näite läbi *5. peatükis*.

Abstraktse algebra edasiseks aruteluks soovitaksin ma Socratica suurepärast videoseeriat abstraktsest algebrast. [4] Eriti soovitaksin järgmisi videoid: “Mis on abstraktne algebra?”, “Grupi definitsioon (laiendatud)”, “Ringi definitsioon (laiendatud)” ja “Välja definitsioon (laiendatud)”. Need neli videot annavad teile lisateavet palju eelneva arutelu kohta. (Me ei arutanud ringe, kuid väli on lihtsalt eritüüpi ring.)

Kaasaegse arvuteooria edasiseks aruteluks võite konsulteerida paljude edasijõudnute aruteludega krüptograafia kohta. Pakuksin soovitustena Jonathan Katzi ja Yehuda Lindelli teost “Introduction to Modern Cryptography” või Christof Paari ja Jan Pelzli teost “Understanding Cryptography” edasiseks aruteluks. [5]

**Märkused:**

[3] Vaata [YouTube'i videot](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Abstraktne Algebra](https://www.socratica.com/subject/abstract-algebra)

[5] Katz ja Lindell, *Introduction to Modern Cryptography*, 2. väljaanne, 2015 (CRC Press: Boca Raton, FL). Paar ja Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlin).

# Sümmeetriline Krüptograafia
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice ja Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Üks kahest peamisest krüptograafia harust on sümmeetriline krüptograafia. See hõlmab krüpteerimisskeeme samuti kui skeeme, mis on seotud autentimise ja terviklusega. Kuni 1970ndateni oleks kogu krüptograafia koosnenud sümmeetrilistest krüpteerimisskeemidest.

Peamine arutelu algab, vaadeldes sümmeetrilisi krüpteerimisskeeme ja tehes olulise vahet voogšifrite ja plokšifrite vahel. Seejärel pöördume sõnumi autentimiskoodide poole, mis on skeemid sõnumi tervikluse ja autentsuse tagamiseks. Lõpuks uurime, kuidas sümmeetrilisi krüpteerimisskeeme ja sõnumi autentimiskoode saab kombineerida turvalise suhtluse tagamiseks.

See peatükk arutleb möödaminnes erinevate sümmeetriliste krüptograafiliste skeemide üle praktikas. Järgmine peatükk pakub üksikasjalikku ekspositsiooni krüpteerimisest voogšifri ja plokšifriga praktikas, nimelt vastavalt RC4 ja AES.

Enne sümmeetrilise krüptograafia arutelu alustamist tahan ma lühidalt teha mõned märkused Alice'i ja Bobi illustratsioonide kohta selles ja järgnevates peatükkides.

___

Krüptograafia põhimõtete illustreerimisel toetuvad inimesed sageli näidetele, mis hõlmavad Alice'i ja Bobi. Ma teen seda samuti.

Eriti kui olete krüptograafiaga uus, on oluline mõista, et need Alice'i ja Bobi näited on mõeldud ainult krüptograafiliste põhimõtete ja konstruktsioonide illustreerimiseks lihtsustatud keskkonnas. Põhimõtted ja konstruktsioonid on siiski kohaldatavad palju laiemas reaalelu kontekstis.
Järgnevalt on viis olulist punkti, mida meeles pidada krüptograafia näidetes, mis hõlmavad Alicet ja Bobi:
1. Neid saab hõlpsasti tõlkida näideteks teiste tegelastega, nagu ettevõtted või valitsusorganisatsioonid.
2. Neid saab hõlpsasti laiendada, et kaasata kolm või enam tegelast.
3. Näidetes on Bob ja Alice tavaliselt aktiivsed osalejad iga sõnumi loomisel ja krüptograafiliste skeemide rakendamisel sellele sõnumile. Kuid tegelikkuses on elektrooniline suhtlus suuresti automatiseeritud. Näiteks veebilehte külastades, mis kasutab transpordikihi turvalisust, käideldakse krüptograafiat tavaliselt teie arvuti ja veebiserveri poolt.
4. Elektroonilise suhtluse kontekstis on suhtluskanali kaudu saadetavad "sõnumid" tavaliselt TCP/IP paketid. Need võivad kuuluda e-kirjale, Facebooki sõnumile, telefonivestlusele, failiedastusele, veebilehele, tarkvara üleslaadimisele jne. Need ei ole sõnumid traditsioonilises mõttes. Siiski lihtsustavad krüptograafid sageli seda reaalsust, öeldes, et sõnum on näiteks e-kiri.
5. Näited keskenduvad tavaliselt elektroonilisele suhtlusele, kuid neid saab laiendada ka traditsioonilistele suhtlusvormidele, nagu kirjad.

## Sümmeetrilised krüpteerimisskeemid
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Me võime lahtiselt defineerida **sümmeetrilise krüpteerimisskeemi** kui iga krüptograafilist skeemi, mis sisaldab kolme algoritmi:

1. **Võtme genereerimise algoritm**, mis genereerib privaatvõtme.
2. **Krüpteerimisalgoritm**, mis võtab sisendina privaatvõtme ja lihtteksti ning väljastab krüptoteksti.
3. **Dekrüpteerimisalgoritm**, mis võtab sisendina privaatvõtme ja krüptoteksti ning väljastab algse lihtteksti.

Tavaliselt pakub krüpteerimisskeem—olgu see siis sümmeetriline või asümmeetriline—krüpteerimise malli, mis põhineb tuumalgoritmil, mitte täpsel spetsifikatsioonil.

Näiteks võtke Salsa20, sümmeetriline krüpteerimisskeem. Seda saab kasutada nii 128- kui ka 256-bitiste võtme pikkustega. Võtme pikkuse valik mõjutab algoritmi mõningaid väiksemaid detaile (täpsemalt algoritmi läbimiste arvu).

Kuid ei öelda, et Salsa20 kasutamine 128-bitise võtmega on erinev krüpteerimisskeem kui Salsa20 kasutamine 256-bitise võtmega. Tuumalgoritm jääb samaks. Ainult siis, kui tuumalgoritm muutub, räägiksime tõesti kahest erinevast krüpteerimisskeemist.

Sümmeetrilised krüpteerimisskeemid on tavaliselt kasulikud kahe liiki juhtudel: (1) Need, kus kaks või enam agenti suhtlevad kaugelt ja soovivad hoida oma suhtluse sisu saladuses; ja (2) need, kus üks agent soovib hoida sõnumi sisu saladuses ajas.

Olukorda (1) näete allpool *Joonisel 1*. Bob soovib saata sõnumi $M$ Alicele kaugelt, kuid ei soovi, et teised saaksid seda sõnumit lugeda.

Bob krüpteerib esmalt sõnumi $M$ privaatvõtmega $K$. Seejärel saadab ta krüptoteksti $C$ Alicele. Kui Alice on krüptoteksti kätte saanud, saab ta selle dekrüpteerida võtmega $K$ ja lugeda lihtteksti. Hea krüpteerimisskeemi korral ei tohiks ükski ründaja, kes krüptoteksti $C$ pealt kuulab, suuta sõnumi $M$ kohta midagi olulist teada saada.

Olukorda (2) näete allpool *Joonisel 2*. Bob soovib takistada teistel teatud teabe vaatamist. Tüüpiline olukord võib olla see, kus Bob on töötaja, kes salvestab tundlikke andmeid oma arvutisse, mida ei tohiks lugeda ei välised isikud ega tema kolleegid.
Bob krüpteerib sõnumi $M$ ajal $T_0$ võtmega $K$, et toota krüptoteksti $C$. Ajal $T_1$ vajab ta sõnumit uuesti ja dekrüpteerib krüptoteksti $C$ võtmega $K$. Ükski ründaja, kes võis vahepeal krüptotekstiga $C$ kokku puutuda, ei oleks tohtinud suuta sellest midagi olulist sõnumi $M$ kohta järeldada.

*Joonis 1: Saladus ruumis*

![Joonis 1: Saladus ruumis](assets/Figure4-1.webp "Joonis 1: Saladus ruumis")

*Joonis 2: Saladus ajas*

![Joonis 2: Saladus ajas](assets/Figure4-2.webp "Joonis 2: Saladus ajas")

## Näide: Nihkešiffer
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

2. peatükis tutvustasime nihkešifferit, mis on väga lihtsa sümmeetrilise krüpteerimisskeemi näide. Vaatame seda siin uuesti.

Eeldame sõnastikku *D*, mis seostab kõik inglise tähestiku tähed järjekorras numbrite komplektiga $\{0,1,2,\dots,25\}$. Eeldame võimalike sõnumite komplekti **M**. Nihkešiffer on siis krüpteerimisskeem, mis on defineeritud järgnevalt:

- Vali juhuslikult võti $k$ võimalike võtmete komplektist **K**, kus **K** = $\{0,1,2,\dots,25\}$
- Krüpteeri sõnum $m \in$ **M**, järgmiselt:
    - Eralda $m$ selle üksikuteks tähtedeks $m_0, m_1,\dots, m_i, \dots, m_l$
    - Teisenda iga $m_i$ numbriks vastavalt *D*-le
    - Iga $m_i$ jaoks, $c_i = [(m_i + k) \mod 26]$
    - Teisenda iga $c_i$ täheks vastavalt *D*-le
    - Seejärel ühenda $c_0, c_1,\dots, c_l$, et saada krüptotekst $c$
- Dekrüpteeri krüptotekst $c$ järgmiselt:
    - Teisenda iga $c_i$ number vastavalt *D*-le
    - Iga $c_i$ jaoks, $m_i = [(c_i - k) \mod 26]$
    - Teisenda iga $m_i$ täht vastavalt *D*-le
    - Seejärel ühenda $m_0, m_1,\dots, m_l$, et saada algne sõnum $m$

Nihkešiffer on sümmeetriline krüpteerimisskeem, kuna nii krüpteerimiseks kui ka dekrüpteerimiseks kasutatakse sama võtit. Näiteks, kui soovid krüpteerida sõnumit “DOG” kasutades nihkešifferit ja oled juhuslikult valinud võtmeks "24", siis krüpteerimine selle võtmega annaks tulemuseks “BME”. Ainus viis algse sõnumi taastamiseks on kasutada sama võtit, "24", dekrüpteerimisprotsessis.

See nihkešiffer on **monoalfabeetilise asendusšifferi** näide: krüpteerimisskeem, kus krüptoteksti tähestik on fikseeritud (st kasutatakse ainult ühte tähestikku). Eeldades, et dekrüpteerimisalgoritm on deterministlik, võib iga sümbol asenduskrüptotekstis vastata maksimaalselt ühele sümbolile algtekstis.
1700ndateni tuginesid paljud krüpteerimise rakendused suuresti monoalfabeetilistele asenduskoodidele, kuigi tihti olid need palju keerulisemad kui nihešiffer. Näiteks võisite juhuslikult valida tähestikust iga algteksti tähe jaoks ühe tähe, tingimusel, et iga täht esineb krüptoteksti tähestikus ainult üks kord. See tähendab, et teil oleks faktoriaal 26 võimalikku privaatvõtit, mis oli ennearvutiajastul tohutu.

Pange tähele, et krüptograafias kohtate terminit **šiffer** palju. Olge teadlikud, et sellel terminil on mitu tähendust. Tegelikult tean ma vähemalt viit erinevat tähendust, mida see termin krüptograafias omab.

Mõnel juhul viitab see krüpteerimisskeemile, nagu see teeb nihešifferi ja monoalfabeetilise asenduskoodi puhul. Siiski võib termin viidata ka spetsiifiliselt krüpteerimisalgoritmile, privaatvõtmele või lihtsalt mis tahes sellise krüpteerimisskeemi krüptotekstile.

Lõpuks võib termin šiffer viidata ka põhialgoritmile, millest saab konstrueerida krüptograafilisi skeeme. Need võivad hõlmata erinevaid krüpteerimisalgoritme, kuid ka teisi tüüpi krüptograafilisi skeeme. See termini tähendus muutub oluliseks plokkšifferite kontekstis (vt allpool jaotist "Plokkšifrid").

Võite samuti kohata termineid **krüpteerima** või **dekrüpteerima**. Need terminid on lihtsalt sünonüümid krüpteerimisele ja dekrüpteerimisele.

## Jõuga ründamine ja Kerckhoffi põhimõte
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Nihešiffer on väga ebaturvaline sümmeetriline krüpteerimisskeem, vähemalt tänapäeva maailmas. [1] Ründaja võiks lihtsalt proovida dekrüpteerida mis tahes krüptoteksti kõigi 26 võimaliku võtmega, et näha, milline tulemus mõistlik tundub. Sellist tüüpi rünnakut, kus ründaja lihtsalt tsüklitab võtmete vahel, et näha, mis toimib, tuntakse kui **jõuga ründamist** või **amendavat võtmeotsingut**.

Et mis tahes krüpteerimisskeem vastaks minimaalsele turvalisuse mõistele, peab sellel olema võtmeruum, mis on nii suur, et jõuga rünnakud on teostamatud. Kõik kaasaegsed krüpteerimisskeemid vastavad sellele standardile. Seda tuntakse kui **piisava võtmeruumi põhimõtet**. Sarnane põhimõte kehtib tavaliselt ka erinevat tüüpi krüptograafilistes skeemides.

Et saada ettekujutus kaasaegsete krüpteerimisskeemide tohutust võtmeruumi suurusest, eeldagem, et fail on krüpteeritud 128-bitise võtmega, kasutades arenenud krüpteerimisstandardit. See tähendab, et ründajal on vaja läbi käia $2^{128}$ võtit, et teostada jõuga rünnakut. 0,78% eduvõimalusega sellise strateegiaga peaks ründaja läbi käima umbes $2.65 \times 10^{36}$ võtit.

Eeldagem optimistlikult, et ründaja suudab proovida $10^{16}$ võtit sekundis (st 10 kvadriljonit võtit sekundis). Et testida 0,78% kõigist võtmeruumi võtmetest, peaks tema rünnak kestma $2.65 \times 10^{20}$ sekundit. See on umbes 8,4 triljonit aastat. Seega isegi absurdse võimsusega vastase jõuga rünnak ei ole realistlik kaasaegse 128-bitise krüpteerimisskeemiga. See on piisava võtmeruumi põhimõtte mäng.

Kas nihešiffer on turvalisem, kui ründaja ei tea krüpteerimisalgoritmi? Võib-olla, kuid mitte palju.
Igal juhul eeldab kaasaegne krüptograafia alati, et mis tahes sümmeetrilise krüpteerimisskeemi turvalisus sõltub ainult privaatvõtme saladuses hoidmisest. Eeldatakse, et ründaja teab kõiki teisi detaile, sealhulgas sõnumiruumi, võtmeruumi, šifreeritud teksti ruumi, võtme valiku algoritmi, krüpteerimisalgoritmi ja dekrüpteerimisalgoritmi.
Mõte, et sümmeetrilise krüpteerimisskeemi turvalisus võib sõltuda ainult privaatvõtme saladusest, on tuntud kui **Kerckhoffs’i printsiip**.

Nagu Kerckhoffs algselt kavandas, kehtib see printsiip ainult sümmeetriliste krüpteerimisskeemide kohta. Printsiibi üldisem versioon kehtib siiski kõigi teiste kaasaegsete krüptograafiliste skeemide kohta: ühegi krüptograafilise skeemi kujundus ei tohi olla saladus, et see oleks turvaline; saladus võib ulatuda ainult mõne teabejada, tavaliselt privaatvõtmeni.

Kerckhoffs’i printsiip on kaasaegse krüptograafia jaoks keskne neljal põhjusel. [2] Esiteks, konkreetsete rakenduste jaoks on krüptograafilisi skeeme piiratud arv. Näiteks kasutavad enamik kaasaegseid sümmeetrilise krüpteerimise rakendusi Rijndaeli šifrit. Seega on skeemi kujunduse osas saladuse hoidmine väga piiratud. Rijndaeli šifri jaoks mõne privaatvõtme saladuses hoidmine pakub aga palju rohkem paindlikkust.

Teiseks, teabejada asendamine on lihtsam kui terve krüptograafilise skeemi asendamine. Kujutage ette, et ettevõtte kõigil töötajatel on sama krüpteerimistarkvara ja iga kahe töötaja vahel on privaatvõti konfidentsiaalseks suhtlemiseks. Võtmete kompromiteerimine on selles stsenaariumis tülikas, kuid vähemalt saaks ettevõte selliste turvaintsidentide korral tarkvara alles hoida. Kui ettevõte sõltuks skeemi saladusest, siis iga sellise saladuse rikkumine nõuaks kogu tarkvara asendamist.

Kolmandaks, Kerckhoffs’i printsiip võimaldab krüptograafiliste skeemide standardiseerimist ja ühilduvust kasutajate vahel. Sellel on tohutu kasu efektiivsusele. Näiteks on raske ette kujutada, kuidas miljonid inimesed saaksid iga päev turvaliselt Google'i veebiserveritega ühendust luua, kui see turvalisus nõuaks krüptograafiliste skeemide saladuses hoidmist.

Neljandaks, Kerckhoffs’i printsiip võimaldab krüptograafiliste skeemide avalikku kontrolli. Selline kontroll on absoluutselt vajalik turvaliste krüptograafiliste skeemide saavutamiseks. Näiteks sümmeetrilise krüptograafia peamine algoritm, Rijndaeli šifer, oli konkursi tulemus, mille korraldas Riiklik Standardite ja Tehnoloogia Instituut aastatel 1997 kuni 2000.

Iga süsteem, mis üritab saavutada **turvalisust läbi obskuursuse**, sõltub oma kujunduse ja/või rakenduse detailide saladuses hoidmisest. Krüptograafias oleks see spetsiifiliselt süsteem, mis sõltub krüptograafilise skeemi kujunduse detailide saladuses hoidmisest. Seega on turvalisus läbi obskuursuse otseses vastuolus Kerckhoffs’i printsiibiga.

Avatuse võime kvaliteeti ja turvalisust tugevdada ulatub digitaalses maailmas kaugemale kui ainult krüptograafia. Vabad ja avatud lähtekoodiga Linuxi distributsioonid, nagu näiteks Debian, omavad üldiselt mitmeid eeliseid oma Windowsi ja MacOSi vastaste ees privaatsuse, stabiilsuse, turvalisuse ja paindlikkuse osas. Kuigi sellel võib olla mitu põhjust, on kõige olulisem põhimõte tõenäoliselt, nagu Eric Raymond oma kuulsas essees "Katedraal ja Bazaar" sõnastas, et "piisavalt paljude silmapaaride korral on kõik vead pealiskaudsed." [3] See on rahva tarkuse tüüpi põhimõte, mis andis Linuxile selle kõige olulisema edu.
Üks ei saa kunagi üheselt väita, et krüptograafiline skeem on "turvaline" või "mitteturvaline". Selle asemel on krüptograafiliste skeemide puhul erinevad turvalisuse mõisted. Iga **krüptograafilise turvalisuse definitsioon** peab täpsustama (1) turvalisuse eesmärgid, samuti (2) ründaja võimekused. Krüptograafiliste skeemide analüüsimine ühe või mitme kindla turvalisuse mõiste alusel annab ülevaate nende rakendustest ja piirangutest. 
Kuigi me ei süvene kõikidesse krüptograafilise turvalisuse erinevate mõistete detailidesse, peaksite teadma, et kaks eeldust on ühised kõigile kaasaegsetele krüptograafilise turvalisuse mõistetele, mis puudutavad sümmeetrilisi ja asümmeetrilisi skeeme (ja mingil määral ka teisi krüptograafilisi primitiive):

* Ründaja teadmised skeemi kohta vastavad Kerckhoffs’i põhimõttele.
* Ründaja ei saa teostada skeemi vastu teostatavat jõumeetodil rünnakut. Eelkõige ei luba krüptograafilise turvalisuse ohumudelid isegi jõumeetodil rünnakuid, kuna eeldatakse, et need ei ole asjakohased.

**Märkused:**

[1] Seutoniuse järgi kasutas Julius Caesar oma sõjalises suhtluses nihkešifrit, mille püsiv võtmeväärtus oli 3. Seega A muutus alati D-ks, B alati E-ks, C alati F-ks jne. See konkreetne nihkešifri versioon on seega saanud tuntuks kui **Caesari šiffer** (kuigi see ei ole tegelikult šiffer kaasaegses sõna mõttes, kuna võtmeväärtus on püsiv). Caesari šiffer võis olla turvaline esimesel sajandil eKr, kui Rooma vaenlased olid krüpteerimisega väga vähe tuttavad. Kuid kaasaegses ajas ei oleks see kindlasti väga turvaline skeem.

[2] Jonathan Katz ja Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), lk 7f.

[3] Eric Raymond, “The Cathedral and the Bazaar,” ettekanne esitati Linux Kongressil, Würzburg, Saksamaa (27. mai 1997). On olemas mitu järgnevat versiooni samuti kui raamat. Minu viited on pärit raamatu leheküljelt 30: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, parandatud väljaanne. (2001), O’Reilly: Sebastopol, CA.

## Voogšifrid
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Sümmeetrilised krüpteerimisskeemid jagunevad standardsete kriteeriumide alusel kaheks tüübiks: **voogšifrid** ja **plokšifrid**. See eristus on siiski mõnevõrra problemaatiline, kuna inimesed kasutavad neid termineid ebaühtlaselt. Järgmistes jaotistes seletan ma eristust viisil, nagu mina seda parimaks pean. Peaksite siiski teadma, et paljud inimesed kasutavad neid termineid erinevalt, kui ma siin välja toon.

Alustame esmalt voogšifritest. **Voogšiffer** on sümmeetriline krüpteerimisskeem, kus krüpteerimine koosneb kahest sammust.

Esiteks, tekstitähtede pikkune jada toodetakse privaatvõtme abil. Seda jada nimetatakse **võtmevoog**.

Järgmiseks kombineeritakse matemaatiliselt võtmevoog ja algtekst, et toota krüptotekst. See kombinatsioon on tavaliselt XOR-operatsioon. Dekrüpteerimiseks võite lihtsalt operatsiooni ümber pöörata. (Märkus: $A \oplus B = B \oplus A$, juhul kui $A$ ja $B$ on bitijadad. Seega XOR-operatsiooni järjekord voogšifris tulemuse jaoks ei oma tähtsust. Seda omadust tuntakse kui **kommutatiivsust**.)
Tüüpiline XOR voogšifri skeem on kujutatud *joonisel 3*. Kõigepealt võtate privaatvõtme $K$ ja kasutate seda võtmestiku genereerimiseks. Võtmestik ühendatakse seejärel lihttekstiga XOR operatsiooni kaudu, et toota šifreeritud tekst. Iga agent, kes saab šifreeritud teksti, saab selle hõlpsalt dešifreerida, kui tal on võti $K$. Kõik, mida ta peab tegema, on luua šifreeritud teksti pikkune võtmestik vastavalt skeemi määratud protseduurile ja teha sellega XOR operatsioon.

*Joonis 3: XOR voogšifri skeem*

![Joonis 3: XOR voogšifri skeem](assets/Figure4-3.webp "Joonis 3: XOR voogšifri skeem")

Pea meeles, et krüpteerimisskeem on tavaliselt mall krüpteerimiseks sama põhialgoritmiga, mitte täpne spetsifikatsioon. Samuti on voogšifri skeem tavaliselt krüpteerimise mall, kus saab kasutada erineva pikkusega võtmeid. Kuigi võtme pikkus võib mõjutada skeemi mõningaid väikseid detaile, ei mõjuta see selle põhivormi.

Nihkešifri on näide väga lihtsast ja ebaturvalisest voogšifrist. Kasutades ühte tähte (privaatvõtit), saate toota sõnumi pikkuse tähtede jada (võtmestiku). See võtmestik ühendatakse seejärel lihttekstiga modulo operatsiooni kaudu, et toota šifreeritud tekst. (Seda modulo operatsiooni saab lihtsustada XOR operatsiooniks, kui tähti esitatakse bittidena).

Teine kuulus voogšifri näide on **Vigenère'i šifri**, mille arendas täielikult välja Blaise de Vigenère 16. sajandi lõpus (kuigi teised olid teinud palju eelnevat tööd). See on **polüalfabeetilise asendusšifri** näide: krüpteerimisskeem, kus lihtteksti sümboli šifreeritud teksti tähestik muutub sõltuvalt selle positsioonist tekstis. Erinevalt monoalfabeetilisest asendusšifrist, võivad šifreeritud teksti sümbolid olla seotud rohkem kui ühe lihtteksti sümboliga.

Krüpteerimise populaarsuse kasvades renessansiaegses Euroopas kasvas ka **krüptoanalüüs**—see tähendab šifreeritud tekstide murdmist—eriti kasutades **sagedusanalüüsi**. Viimane kasutab meie keele statistilisi regulaarsusi šifreeritud tekstide murdmiseks ja avastati juba üheksandal sajandil Araabia õpetlaste poolt. See on tehnika, mis töötab eriti hästi pikemate tekstidega. Ja isegi kõige keerukamad monoalfabeetilised asendusšifrid ei olnud enam piisavad sagedusanalüüsi vastu 1700ndatel Euroopas, eriti sõjalises ja turvaseadetes. Kuna Vigenère'i šifri pakkus olulist turvalisuse edasiminekut, muutus see sel perioodil populaarseks ja oli laialt levinud 1700ndate lõpuks.

Informaalselt öeldes töötab krüpteerimisskeem järgmiselt:

1. Valige mitmetäheline sõna privaatvõtmeks.
2. Iga sõnumi puhul rakendage nihkešifrit iga sõnumi tähele, kasutades vastavat tähte võtmesõnas nihkena.
3. Kui olete võtmesõna läbi käinud, kuid ei ole veel kogu lihtteksti šifreerinud, rakendage võtmesõna tähti uuesti nihkešifrina vastavatele tähtedele teksti ülejäänud osas.
4. Jätkake seda protsessi, kuni kogu sõnum on šifreeritud.

Näiteks, eeldades, et teie privaatvõti on "GOLD" ja soovite krüpteerida sõnumi "CRYPTOGRAPHY". Sel juhul toimiksite vastavalt Vigenère'i šifri järgi järgnevalt:

- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Seega, šifreeritud tekst $c$ = "IFJSZCRUGDSB".

Teine tuntud näide voolušifrist on **ühekordne plokk**. Ühekordse plokiga loote lihtsalt juhuslike bittide jada, mis on sama pikk kui algteksti sõnum, ja toodate šifreeritud teksti XOR-operatsiooni kaudu. Seega on privaatvõti ja võtmevoog ühekordse ploki puhul samaväärsed.

Kuigi nihkešifrit ja Vigenère'i šifrit peetakse tänapäeval väga ebaturvaliseks, on ühekordne plokk õigesti kasutades väga turvaline. Ilmselt kõige kuulsam ühekordse ploki rakendus oli vähemalt kuni 1980. aastateni **Washingtoni-Moskva otseühendus**. [4]

Otseühendus on otsene suhtluskanal Washingtoni ja Moskva vahel kiireloomuliste küsimuste jaoks, mis paigaldati pärast Kuuba raketikriisi. Aastate jooksul on tehnoloogia muutunud. Praegu hõlmab see otseseid kiudoptilisi kaableid ning kahte satelliitlinki (redundantsi jaoks), mis võimaldavad e-kirju ja tekstisõnumeid. Link lõpeb mitmes kohas USAs. Pentagon, Valge Maja ja Raven Rocki mägi on teadaolevad lõpp-punktid. Vastupidiselt levinud arvamusele ei ole otseühendus kunagi hõlmanud telefone.

Ühekordse ploki skeem töötas põhimõtteliselt järgmiselt. Nii Washingtonil kui ka Moskval oli kaks juhuslike numbrite komplekti. Üks juhuslike numbrite komplekt, mille lõid venelased, puudutas sõnumite krüpteerimist ja dekrüpteerimist vene keeles. Teine juhuslike numbrite komplekt, mille lõid ameeriklased, puudutas sõnumite krüpteerimist ja dekrüpteerimist inglise keeles. Aeg-ajalt toimetati teisele poolele usaldusväärsete kullerite poolt rohkem juhuslikke numbreid.

Washington ja Moskva suutsid seejärel kasutada neid juhuslikke numbreid ühekordsete plokkide loomiseks, et suhelda salaja. Iga kord, kui oli vaja suhelda, kasutaksite oma sõnumi jaoks järgmist juhuslike numbrite osa.

Kuigi ühekordne plokk on väga turvaline, seisab see silmitsi oluliste praktiliste piirangutega: võti peab olema sama pikk kui sõnum ja ühekordse ploki ühtegi osa ei tohi uuesti kasutada. See tähendab, et peate jälgima, kus te ühekordses plokis parasjagu olete, hoidma tohutul hulgal bitte ja vahetama aeg-ajalt juhuslikke bitte oma vastaspooltega. Seetõttu ei kasutata ühekordset plokki praktikas sageli.

Selle asemel kasutatakse praktikas peamiselt **pseudosuvalisi voolušifreid**. Salsa20 ja sellele tihedalt seotud variant ChaCha on tavaliselt kasutatavad pseudosuvalised voolušifrid.
Nende pseudosuvaliste voogšifrite puhul valite esmalt juhuslikult võtme K, mis on lühem kui avateksti pikkus. Selline juhuslik võti K luuakse tavaliselt meie arvuti poolt ettearvamatute andmete põhjal, mida see aja jooksul kogub, nagu võrgusõnumite vahel kuluv aeg, hiire liigutused jne. 
See juhuslik võti $K$ sisestatakse seejärel laiendusalgoritmi, mis loob pseudosuvalise võtmestriimi sama pikana kui sõnum. Saate täpselt määrata, kui pikk peab võtmestriim olema (nt 500 bitti, 1000 bitti, 1200 bitti, 29 117 bitti jne).

Pseudosuvaline võtmestriim näib *nagu* see oleks valitud täiesti juhuslikult kõigi sama pikkusega stringide hulgast. Seega tundub krüpteerimine pseudosuvalise võtmestriimiga nagu see oleks tehtud ühekordse padjaga. Kuid see muidugi nii ei ole.

Kuna meie privaatvõti on lühem kui võtmestriim ja meie laiendusalgoritm peab olema deterministlik, et krüpteerimise/dekrüpteerimise protsess töötaks, ei saa iga sellise pikkusega võtmestriim olla meie laiendusoperatsiooni väljund.

Oletame näiteks, et meie privaatvõtmel on pikkus 128 bitti ja et me saame selle sisestada laiendusalgoritmi, et luua palju pikem võtmestriim, öelgem 2500 bitti. Kuna meie laiendusalgoritm peab olema deterministlik, saab meie algoritm valida maksimaalselt $1/2^{128}$ stringi pikkusega 2500 bitti. Seega ei saaks sellist võtmestriimi kunagi valida täiesti juhuslikult kõigi sama pikkusega stringide seast.

Meie voogšifri definitsioonil on kaks aspekti: (1) privaatvõtme abil genereeritakse avatekstiga sama pikk võtmestriim; ja (2) see võtmestriim ühendatakse avatekstiga, tavaliselt XOR-operatsiooni kaudu, et toota šifreeritud tekst.

Mõnikord määratletakse tingimus (1) rangemalt, väites, et võtmestriim peab olema spetsiifiliselt pseudosuvaline. See tähendab, et ei nihkešifrit ega ühekordset padi ei peetaks voogšifriteks.

Minu arvates annab tingimuse (1) laiem määratlemine lihtsama viisi krüpteerimisskeemide organiseerimiseks. Lisaks tähendab see, et me ei pea lõpetama konkreetse krüpteerimisskeemi nimetamist voogšifriks lihtsalt seetõttu, et saame teada, et see ei sõltu tegelikult pseudosuvalistest võtmestriimidest.

**Märkused:**

[4] Crypto Museum, "Washington-Moscow hotline," 2013, saadaval aadressil [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Blokšifrid
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Esimene viis, kuidas **blokšifrit** üldiselt mõistetakse, on midagi primitiivsemat kui voogšifrit: Põhialgoritm, mis teostab pikkust säilitavat transformatsiooni sobiva pikkusega stringil võtme abil. Seda algoritmi saab kasutada krüpteerimisskeemide ja võib-olla ka teist tüüpi krüptograafiliste skeemide loomiseks.
Sageli võib plokšiffer töödelda sisendstringe erineva pikkusega, nagu 64, 128 või 256 bitti, samuti võib see kasutada erineva pikkusega võtmeid, nagu 128, 192 või 256 bitti. Kuigi algoritmi mõned detailid võivad sõltuvalt neist muutujatest muutuda, jääb põhialgoritm samaks. Kui see muutuks, räägiksime kahest erinevast plokšifrist. Märkige, et siin kasutatav põhialgoritmi terminoloogia on sama, mis krüpteerimisskeemide puhul.
Plokšifri tööpõhimõtet saab näha allpool *Joonisel 4*. Sõnum $M$ pikkusega $L$ ja võti $K$ on plokšifri sisendid. See väljastab sõnumi $M'$ pikkusega $L$. Enamiku plokšifrite puhul ei pea võti olema sama pikk kui $M$ ja $M'$.

*Joonis 4: Plokšiffer*

![Joonis 4: Plokšiffer](assets/Figure4-4.webp "Joonis 4: Plokšiffer")

Plokšiffer iseenesest ei ole krüpteerimisskeem. Kuid plokšifrit saab kasutada erinevate **töörežiimidega** erinevate krüpteerimisskeemide loomiseks. Töörežiim lisab plokšifri väliseid lisatoiminguid.

Selle illustreerimiseks eeldagem plokšifrit (BC), mis nõuab 128-bitist sisendstringi ja 128-bitist privaatvõtit. Allpool olev joonis 5 näitab, kuidas seda plokšifrit saab kasutada **elektroonilise koodiraamatu režiimiga** (**ECB režiim**) krüpteerimisskeemi loomiseks. (Paremal olevad kolm punkti näitavad, et seda mustrit saab vajadusel korrata).

*Joonis 5: Plokšiffer ECB režiimiga*

![Joonis 5: Plokšiffer ECB režiimiga](assets/Figure4-5.webp "Joonis 5: Plokšiffer ECB režiimiga")

Elektroonilise koodiraamatu krüpteerimisprotsess plokšifriga on järgmine. Vaadake, kas saate oma tavateksti sõnumi jagada 128-bitisteks plokkideks. Kui mitte, lisage sõnumile **täidis**, et tulemus saaks ühtlaselt jagatud 128-bitise ploki suurusega. See on teie andmed, mida kasutatakse krüpteerimisprotsessis.

Nüüd jagage andmed 128-bitisteks stringideks ($M_1$, $M_2$, $M_3$ jne). Läbige iga 128-bitine string plokšifriga koos teie 128-bitise võtmega, et toota 128-bitiseid krüptoteksti tükke ($C_1$, $C_2$, $C_3$ jne). Need tükid, kui need uuesti kokku panna, moodustavad täieliku krüptoteksti.

Dekrüpteerimine on lihtsalt vastupidine protsess, kuigi saaja vajab mingit äratuntavat viisi, kuidas eemaldada dekrüpteeritud andmetest mis tahes täidis, et taastada algne tavateksti sõnum.

Kuigi suhteliselt lihtne, puudub plokšifril elektroonilise koodiraamatu režiimis turvalisus. See on seetõttu, et see viib **deterministliku krüpteerimiseni**. Iga kahe identse 128-bitise andmestringi krüpteerimine toimub täpselt samal viisil. Seda teavet saab ära kasutada.

Selle asemel peaks iga plokšifrist konstrueeritud krüpteerimisskeem olema **probabilistlik**: see tähendab, et mis tahes sõnumi $M$ või mis tahes konkreetse $M$ tüki krüpteerimine peaks üldiselt iga kord andma erineva tulemuse. [5]

**Šifriplokkide aheldamise režiim** (**CBC režiim**) on tõenäoliselt kõige levinum režiim, mida kasutatakse plokšifriga. Kui see on õigesti tehtud, toodab kombinatsioon probabilistliku krüpteerimisskeemi. Selle töörežiimi kujutist saate näha allpool *Joonisel 6*.

*Joonis 6: Plokšiffer CBC režiimiga*
![Joonis 6: Plokkšiffer CBC režiimis](assets/Figure4-6.webp "Joonis 6: Plokkšiffer CBC režiimis")
Eeldame, et ploki suurus on taas 128 bitti. Alustuseks peate veenduma, et teie algne lihttekstsõnum saab vajaliku täitmise.

Seejärel teete oma lihtteksti esimese 128-bitise osa **algvektoriga**, mis on samuti 128 bitti, XOR-tehte. Tulemus asetatakse plokkšifrisse, et toota esimese ploki jaoks šifreeritud tekst. Teise 128-bitise ploki jaoks teete esmalt lihtteksti ja esimese ploki šifreeritud teksti XOR-tehte, enne kui asetate selle plokkšifrisse. Jätkate seda protsessi, kuni olete kogu oma lihttekstsõnumi šifreerinud.

Lõpetades saadate šifreeritud sõnumi koos krüpteerimata algvektoriga saajale. Saaja peab teadma algvektorit, muidu ei saa ta šifreeritud teksti dekrüpteerida.

See konstruktsioon on palju turvalisem kui elektrooniline koodiraamat režiim, kui seda õigesti kasutada. Peaksite esmalt tagama, et algvektor oleks juhuslik või pseudorandomne jada. Lisaks peaksite iga kord, kui kasutate seda krüpteerimisskeemi, kasutama erinevat algvektorit.

Teisisõnu, teie algvektor peaks olema juhuslik või pseudorandomne ühekordne number, kus **ühekordne number** tähendab "numbrit, mida kasutatakse ainult üks kord". Kui järgite seda tava, siis tagab CBC režiim plokkšifriga, et ükskõik millised kaks identset lihttekstiplokki šifreeritakse iga kord erinevalt.

Lõpuks pöörame tähelepanu **väljundi tagasiside režiimile** (**OFB režiim**). Selle režiimi kujutist näete *Joonisel 7*.

*Joonis 7: Plokkšiffer OFB režiimis*

![Joonis 7: Plokkšiffer OFB režiimis](assets/Figure4-7.webp "Joonis 7: Plokkšiffer OFB režiimis")

OFB režiimis valite samuti algvektori. Kuid siin, esimese ploki jaoks, sisestatakse algvektor otse plokkšifrisse koos teie võtmega. Saadud 128 bitti käsitletakse seejärel võtmehelina. See võtmeheli tehakse XOR-tehte lihttekstiga, et toota ploki jaoks šifreeritud tekst. Järgnevate plokkide jaoks kasutate eelmisest plokkist saadud võtmeheli sisendina plokkšifris ja kordate samme.

Kui vaadata tähelepanelikult, siis tegelikult on OFB režiimis plokkšifrist loodud voogšiffer. Te genereerite võtmeheli osi 128 bitti, kuni teil on lihtteksti pikkus (visates ära viimasest 128-bitisest võtmeheli osast vajaduseta jäänud bitid). Seejärel teete võtmeheliga XOR-tehte oma lihttekstsõnumiga, et saada šifreeritud tekst.

Eelmises jaotises voogšifrite kohta mainisin, et võtmeheli toodetakse privaatvõtme abil. Täpsemalt, see ei pea olema loodud ainult privaatvõtmega. Nagu näete OFB režiimis, toodetakse võtmeheli nii privaatvõtme kui ka algvektori toel.

Pange tähele, et nagu CBC režiimis, on oluline valida iga kord, kui kasutate plokkšifrit OFB režiimis, algvektoriks pseudorandomne või juhuslik ühekordne number. Vastasel juhul šifreeritakse sama 128-bitine sõnumitekst erinevates suhtlustes samal viisil. See on üks viis probabilistliku krüpteerimise loomiseks voogšifriga.
Mõned voogšifrid kasutavad võtmevoo loomiseks ainult privaatvõtit. Nende voogšifride puhul on oluline, et iga suhtlusjuhtumi jaoks valiksite privaatvõtme jaoks juhusliku nonce. Vastasel juhul on ka nende voogšifride krüpteerimistulemused deterministlikud, mis toob kaasa turvaprobleeme.
Kõige populaarsem kaasaegne plokšiffer on **Rijndaeli šiffer**. See oli võidutöö viieteistkümnest esitlusest konkursil, mille korraldas Riiklik Standardite ja Tehnoloogia Instituut (NIST) aastatel 1997 kuni 2000, et asendada vanem krüpteerimisstandard, **andmekrüpteerimisstandard** (**DES**).

Rijndaeli šifferit saab kasutada erinevate spetsifikatsioonidega võtmepikkuste ja plokkide suuruste jaoks, samuti erinevates töörežiimides. NISTi konkursi komitee võttis vastu piiratud versiooni Rijndaeli šifrist—nimelt sellise, mis nõuab 128-bitiseid plokkide suurusi ja võtmepikkusi kas 128, 192 või 256 bitti—kui osa **arenenud krüpteerimisstandardist** (**AES**). See on tõepoolest peamine standard sümmeetrilise krüpteerimise rakendustele. See on nii turvaline, et isegi NSA on ilmselt nõus seda kasutama 256-bitiste võtmetega salajaste dokumentide jaoks. [6]

AES plokšiffer selgitatakse üksikasjalikult *5. peatükis*.

**Märkused:**

[5] Probabilistliku krüpteerimise tähtsust rõhutasid esmakordselt Shafi Goldwasser ja Silvio Micali, “Probabilistlik krüpteerimine,” _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Vaata NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Segaduse selgitamine
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Segadus plokšifrite ja voogšifrite eristamisel tekib, sest mõnikord mõistetakse terminit plokšiffer kui viidet spetsiifiliselt *plokšiffrile plokkrežiimi krüpteerimisega*.

Võtke arvesse eelmises jaotises mainitud ECB ja CBC režiime. Need nõuavad spetsiifiliselt, et krüpteerimiseks mõeldud andmed oleksid jagatavad ploki suurusega (mis tähendab, et võib-olla peate algsele sõnumile lisama polsterdust). Lisaks töödeldakse andmeid nendes režiimides otse plokšifri abil (mitte ainult ei kombineerita seda plokšifri operatsiooni tulemusega nagu OFB režiimis).

Seega, alternatiivselt, võite defineerida **plokšifri** kui mis tahes krüpteerimisskeemi, mis töötab korraga fikseeritud pikkusega plokkidega sõnumist (kus iga plokk peab olema pikem kui bait, vastasel juhul muutub see voogšifriks). Nii krüpteerimiseks mõeldud andmed kui ka šifreeritud tekst peavad jagunema ühtlaselt selle ploki suurusega. Tavaliselt on ploki suurus 64, 128, 192 või 256 bitti pikk. Seevastu voogšiffer saab krüpteerida sõnumeid ühe biti või baidi kaupa korraga.

Selle spetsiifilisema plokšifri mõistmisega võite tõepoolest väita, et kaasaegsed krüpteerimisskeemid on kas voog- või plokšifrid. Edaspidi kasutan terminit plokšiffer üldisemas mõttes, kui pole öeldud teisiti.
Eelmises jaotises OFB režiimi arutelu tõstatas veel ühe huvitava punkti. Mõned voogšifrid on ehitatud plokšifridest, nagu Rijndael OFB-ga. Mõned, nagu Salsa20 ja ChaCha, ei ole loodud plokšifridest. Viimaseid võiks nimetada **primitiivseteks voogšifrideks**. (Tegelikult ei ole selliste voogšifride jaoks standardiseeritud terminit.)

Kui inimesed räägivad voogšifride ja plokšifride eelistest ning puudustest, võrdlevad nad tavaliselt primitiivseid voogšifreid plokšifritel põhinevate krüpteerimisskeemidega.

Kuigi voogšifri saab alati hõlpsasti konstrueerida plokšifrist, on tavaliselt väga keeruline ehitada mingit tüüpi konstruktsiooni plokšifreerimisrežiimiga (näiteks CBC režiimiga) primitiivsest voogšifrist.

Sellest arutelust peaksid nüüd aru saama *Joonis 8*. See annab ülevaate sümmeetrilistest krüpteerimisskeemidest. Me kasutame kolme tüüpi krüpteerimisskeeme: primitiivsed voogšifrid, plokšifri voogšifrid ja plokšifrid plokirežiimis (diagrammil nimetatud ka "plokšifrid").

*Joonis 8: Ülevaade sümmeetrilistest krüpteerimisskeemidest*

![Joonis 8: Ülevaade sümmeetrilistest krüpteerimisskeemidest](assets/Figure4-8.webp "Joonis 8: Ülevaade sümmeetrilistest krüpteerimisskeemidest")


## Sõnumi autentimiskoodid
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Krüpteerimine on seotud saladusega. Kuid krüptograafia tegeleb ka laiemate teemadega, nagu sõnumi terviklikkus, autentsus ja mittetagasivõetavus. Niinimetatud **sõnumi autentimiskoodid** (MAC-id) on sümmeetrilised krüptograafilised skeemid, mis toetavad autentsust ja terviklikkust suhtluses.

Miks on suhtluses vajalik midagi muud peale saladuse? Oletame, et Bob saadab Alicele sõnumi praktiliselt murdmatus krüpteeringus. Iga ründaja, kes selle sõnumi pealt kuulab, ei suuda saada olulisi teadmisi sõnumi sisu kohta. Siiski on ründajal vähemalt kaks muud rünnakuteed:

1. Ta võib pealt kuulata šifreeritud teksti, muuta selle sisu ja saata muudetud šifreeritud teksti edasi Alicele.
2. Ta võib blokeerida Bobi sõnumi täielikult ja saata oma loodud šifreeritud teksti.

Mõlemal juhul ei pruugi ründajal olla ülevaadet šifreeritud tekstide (1) ja (2) sisust. Kuid ta võib siiski sel viisil põhjustada olulist kahju. Siin muutuvad oluliseks sõnumi autentimiskoodid.

Sõnumi autentimiskoode määratletakse laialt kui sümmeetrilisi krüptograafilisi skeeme kolme algoritmiga: võtme genereerimise algoritm, sildi genereerimise algoritm ja kontrollimise algoritm. Turvaline MAC tagab, et sildid on **eksistentsiaalselt võltsimiskindlad** ükskõik millise ründaja jaoks - see tähendab, et nad ei saa edukalt luua sõnumile silti, mis kontrollimisel kehtiks, kui neil pole privaatvõtit.

Bob ja Alice saavad konkreetse sõnumi manipuleerimist võidelda MAC-i abil. Oletame hetkeks, et neile ei lähe korda saladus. Nad soovivad ainult tagada, et Alice'i poolt vastu võetud sõnum oli tõepoolest Bobilt ja seda ei ole mingil viisil muudetud.

Protsess on kujutatud *Joonisel 9*. **MAC** (Message Authentication Code) kasutamiseks genereeriksid nad esmalt privaatvõtme $K$, mis on nende kahe vahel jagatud. Bob loob sõnumile sildi $T$, kasutades privaatvõtit $K$. Seejärel saadab ta sõnumi koos sõnumi sildiga Alicele. Ta saab seejärel kontrollida, et Bob tõepoolest tegi sildi, käivitades kontrollimisalgoritmi privaatvõtme, sõnumi ja sildi abil.

*Joonis 9: Ülevaade sümmeetrilistest krüpteerimisskeemidest*
![Joonis 9: Sümmeetrilise krüpteerimise skeemide ülevaade](assets/Figure4-9.webp "Joonis 9: Sümmeetrilise krüpteerimise skeemide ülevaade")
Tänu **eksistentsiaalsele võltsimiskindlusele** ei saa ründaja sõnumit $M$ mingil viisil muuta ega luua oma sõnumit kehtiva märgisega. See kehtib isegi siis, kui ründaja jälgib paljude sõnumite märgiseid Bobi ja Alice'i vahel, mis kasutavad sama privaatvõtit. Parimal juhul võiks ründaja takistada Alicel sõnumi $M$ vastuvõtmist (probleem, mida krüptograafia ei saa lahendada).

MAC tagab, et sõnumi lõi tegelikult Bob. See autentsus tähendab automaatselt sõnumi terviklikkust – see tähendab, kui Bob on loonud mingi sõnumi, siis, ipso facto, seda ei ole mingil viisil muutnud ründaja. Seega edaspidi peaks iga autentimise mure olema automaatselt mõistetav kui mure terviklikkuse pärast.

Kuigi ma olen oma arutelus teinud vahet sõnumi autentsuse ja terviklikkuse vahel, on tavaline kasutada neid termineid sünonüümidena. Need viitavad siis ideele sõnumitest, mis on loodud kindla saatja poolt ja mida ei ole mingil viisil muudetud. Selles vaimus nimetatakse sõnumi autentimiskoodid sageli ka **sõnumi terviklikkuskoodideks**.

## Autentitud krüpteerimine
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Tavaliselt sooviksite tagada nii saladuse kui ka autentsuse suhtluses ning seetõttu kasutatakse tavaliselt koos krüpteerimisskeeme ja MAC-skeeme.

**Autentitud krüpteerimisskeem** on skeem, mis ühendab krüpteerimise MAC-iga väga turvalisel viisil. Eelkõige peab see vastama eksistentsiaalse võltsimiskindluse standarditele, samuti väga tugevale saladuse mõistele, nimelt ühele, mis on vastupidav **valitud-šifriteksti rünnakutele**. [7]

Selleks, et krüpteerimisskeem oleks vastupidav valitud-šifriteksti rünnakutele, peab see vastama **mittemuudetavuse** standarditele: see tähendab, et iga ründaja poolt šifreeritud teksti muudatus peaks andma kas kehtetu šifreeritud teksti või sellise, mis dekrüpteerituna ei ole mingil moel seotud algsega. [8]

Kuna autentitud krüpteerimisskeem tagab, et ründaja poolt loodud šifreeritud tekst on alati kehtetu (kuna märgist ei kinnitata), vastab see valitud-šifriteksti rünnakutele vastupanu standarditele. Huvitaval kombel saab tõestada, et autentitud krüpteerimisskeemi saab alati luua eksistentsiaalselt võltsimiskindla MAC-i ja krüpteerimisskeemi kombinatsioonist, mis vastab vähem tugevale turvalisuse mõistele, tuntud kui **valitud-avaliku-teksti rünnaku turvalisus**.

Me ei süvene kõikidesse autentitud krüpteerimisskeemide loomise detailidesse. Kuid on oluline teada kahte nende konstruktsiooni detaili.

Esiteks, autentitud krüpteerimisskeem tegeleb esmalt krüpteerimisega ja seejärel loob sõnumimärgise šifreeritud tekstil. Selgub, et teised lähenemised – nagu šifreeritud teksti ühendamine märgisega avalikul tekstil või esmalt märgise loomine ja seejärel nii avaliku teksti kui ka märgise krüpteerimine – on turvalised. Lisaks on mõlemal toimingul oma juhuslikult valitud privaatvõti, vastasel juhul on teie turvalisus tõsiselt ohustatud.

Eelmainitud põhimõte kehtib üldisemalt: *alati peaksite kasutama erinevaid võtmeid, kui ühendate põhilisi krüptograafilisi skeeme*.

Autentitud krüpteerimisskeemi kujutatakse *Joonisel 10*. Bob loob esmalt šifreeritud teksti $C$ sõnumist $M$, kasutades juhuslikult valitud võtit $K_C$. Seejärel loob ta sõnumimärgise $T$, juhtides šifreeritud teksti ja teise juhuslikult valitud võtme $K_T$ läbi märgise genereerimise algoritmi. Nii šifreeritud tekst kui ka sõnumimärgis saadetakse Alicele.
Alice kontrollib nüüd esmalt, kas silt on kehtiv antud šifreeritud teksti $C$ ja võtme $K_T$ puhul. Kui see on kehtiv, saab ta seejärel sõnumi lahti šifreerida võtmega $K_C$. Ta on mitte ainult kindlustatud väga tugeva salajasuse mõistega nende suhtluses, vaid ta teab ka, et sõnumi lõi Bob.
*Joonis 10: Autentitud krüpteerimise skeem*

![Joonis 10: Autentitud krüpteerimise skeem](assets/Figure4-10.webp "Joonis 10: Autentitud krüpteerimise skeem")

Kuidas luuakse MAC-e? Kuigi MAC-e saab luua mitmel viisil, on üks levinud ja tõhus viis nende loomiseks läbi **krüptograafiliste räsifunktsioonide**.

Tutvustame krüptograafilisi räsifunktsioone põhjalikumalt *6. peatükis*. Praegu piisab teadmiseks, et **räsifunktsioon** on tõhusalt arvutatav funktsioon, mis võtab sisendeid suvalises suuruses ja annab fikseeritud pikkusega väljundeid. Näiteks populaarne räsifunktsioon **SHA-256** (turvaline räsialgoritm 256) genereerib alati 256-bitise väljundi sõltumata sisendi suurusest. Mõned räsifunktsioonid, nagu SHA-256, omavad kasulikke rakendusi krüptograafias.

Kõige tavalisem sildiga toode, mis luuakse krüptograafilise räsifunktsiooniga, on **räsi-põhine sõnumi autentimiskood** (HMAC). Protsess on kujutatud *Joonisel 11*. Osapool loob privaatvõtmest $K$ kaks erinevat võtit, sisemise võtme $K_1$ ja välimise võtme $K_2$. Tavaline tekst $M$ või šifreeritud tekst $C$ räsitakse koos sisemise võtmega. Tulemus $T'$ räsitakse seejärel välimise võtmega, et toota sõnumi silt $T$.

On mitmeid räsifunktsioone, mida saab kasutada HMAC-i loomiseks. Kõige sagedamini kasutatav räsifunktsioon on SHA-256.

*Joonis 11: HMAC*

![Joonis 11: HMAC](assets/Figure4-11.webp "Joonis 11: HMAC")

**Märkused:**

[7] Selles jaotises arutatud spetsiifilised tulemused pärinevad Katzist ja Lindellist, lk 131–47.

[8] Tehniliselt on valitud šifreeritud teksti rünnakute definitsioon erinev kui mittemuudetavuse mõiste. Kuid võib näidata, et need kaks turvalisuse mõistet on ekvivalentsed.

## Turvalised suhtlusseansid
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Eeldame, et kaks osapoolt on suhtlusseansis, nii et nad saadavad mitu sõnumit edasi-tagasi.

Autentitud krüpteerimise skeem võimaldab sõnumi saajal kontrollida, et see loodi tema suhtluspartneri poolt (seni, kuni privaatvõti ei ole lekkinud). See toimib piisavalt hästi ühe sõnumi puhul. Tavaliselt aga saadavad kaks osapoolt sõnumeid edasi-tagasi suhtlusseansis. Ja selles olukorras jääb lihtne autentitud krüpteerimise skeem, nagu eelmises jaotises kirjeldatud, turvalisuse tagamisel lühikeseks.

Peamine põhjus on see, et autentitud krüpteerimise skeem ei anna mingit garantiid, et sõnum saadeti tegelikult ka agentuuri poolt, kes selle suhtlusseansi jooksul lõi. Kaaluge järgmisi kolme rünnakuvektorit:

1. **Kordusrünnak**: Ründaja saadab uuesti šifreeritud teksti ja sildi, mille ta varasemalt kahe osapoole vahel pealt kuulas.
2. **Ümberjärjestamise rünnak**: Ründaja pealtkuulab kaks sõnumit erinevatel aegadel ja saadab need saajale vastupidises järjekorras.
3. **Peegeldusrünnak**: Ründaja jälgib sõnumit, mis saadeti A-lt B-le, ja saadab selle sõnumi ka A-le.

Kuigi ründajal pole šifreeritud teksti kohta teadmisi ja ta ei saa luua võltsitud šifreeritud tekste, võivad ülaltoodud rünnakud siiski suhtluses olulist kahju tekitada.
Eeldame näiteks, et teatud sõnum kahe osapoole vahel hõlmab finantsvahendite ülekandmist. Kordusattack võib vahendid teist korda üle kanda. Tavalisel autentitud krüpteerimisskeemil pole selliste rünnakute vastu kaitset. 
Õnneks saab selliseid rünnakuid suhtlusseansis lihtsalt leevendada, kasutades **identifikaatoreid** ja **suhtelisi ajaindikaatoreid**.

Identifikaatoreid saab lisada krüpteerimisele eelnevale lihttekstile. See takistaks igasuguseid peegeldusrünnakuid. Suhteline ajaindikaator võib näiteks olla järjekorranumber teatud suhtlusseansis. Iga osapool lisab sõnumile enne krüpteerimist järjekorranumbri, nii et vastuvõtja teab, millises järjekorras sõnumid saadeti. See kõrvaldab rünnakute võimaluse, kus sõnumeid paigutatakse ümber. Samuti kõrvaldab see kordusattackid. Iga ründaja poolt edastatud sõnumil on vana järjekorranumber ja vastuvõtja teab, et ei tohiks sõnumit uuesti töödelda.

Et illustreerida, kuidas turvalised suhtlusseansid töötavad, eeldame taas Alice'i ja Bobi. Nad saadavad kokku neli sõnumit edasi-tagasi. Allpool *joonisel 11* näete, kuidas autentitud krüpteerimisskeem identifikaatorite ja järjekorranumbritega töötaks.

Suhtlusseanss algab Bobi poolt saadetud krüptotekstiga $C_{0,B}$ Alice'ile koos sõnumi märgisega $T_{0,B}$. Krüptotekst sisaldab sõnumit, samuti identifikaatorit (BOB) ja järjekorranumbrit (0). Märgis $T_{0,B}$ on tehtud kogu krüptoteksti peale. Nende järgnevas suhtluses järgivad Alice ja Bob seda protokolli, vajadusel välju uuendades.

*Joonis 12: Turvaline suhtlusseanss*

![Joonis 12: Turvaline suhtlusseanss](assets/Figure4-12.webp "Joonis 12: Turvaline suhtlusseanss")

# RC4 ja AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## RC4 voogšiffer
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

Sel peatükis arutame krüpteerimisskeemi üksikasju, mis kasutab kaasaegset primitiivset voogšifrit, RC4 (või "Rivest cipher 4"), ja kaasaegset plokšifrit, AES. Kuigi RC4 šiffer on krüpteerimismeetodina ebasoosingusse langenud, on AES kaasaegse sümmeetrilise krüpteerimise standard. Need kaks näidet peaksid andma parema ettekujutuse, kuidas sümmeetriline krüpteerimine sisemiselt töötab.

___

Selleks, et mõista, kuidas kaasaegsed pseudosuvalised voogšifrid töötavad, keskendun RC4 voogšiffrile. See on pseudosuvaline voogšiffer, mida kasutati WEP- ja WAP-traadita juurdepääsupunktide turvaprotokollides ning TLS-is. Kuna RC4-l on palju tõestatud nõrkusi, on see ebasoosingusse langenud. Tegelikult keelab Internet Engineering Task Force nüüd RC4 komplektide kasutamise klient- ja serverirakendustes kõigis TLS-i juhtumites. Siiski töötab see hästi näitena, et illustreerida, kuidas primitiivne voogšiffer töötab.

Alustuseks näitan esmalt, kuidas krüpteerida lihtteksti sõnumit beebi RC4 šiffriga. Eeldame, et meie lihtteksti sõnum on “SOUP.” Krüpteerimine meie beebi RC4 šiffriga toimub siis neljas etapis.

### 1. samm
Esmalt defineerige massiiv **S** nii, et $S[0] = 0$ kuni $S[7] = 7$. Siin tähendab massiiv lihtsalt indeksi järgi organiseeritud muudetavate väärtuste kogumit, mida mõnes programmeerimiskeeltes (nt Python) nimetatakse ka listiks. Sel juhul jookseb indeks 0-st 7-ni ja väärtused samuti 0-st 7-ni. Seega on **S** järgmine:
- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Siin olevad väärtused ei ole ASCII numbrid, vaid 1-baidiste stringide kümnendväärtuste esitused. Seega väärtus 2 võrdub $0000 \ 0011$. Massiivi **S** pikkus on seega 8 baiti.

### 2. samm

Teiseks defineerige võtmemassiiv **K** 8 baidi pikkusega, valides võtme 1 ja 8 baiti vahel (baidi murdosad ei ole lubatud). Kuna iga bait on 8 bitti, võite iga oma võtme baidi jaoks valida suvalise numbri vahemikus 0 kuni 255.

Oletame, et valime oma võtme **k** kui $[14, 48, 9]$, nii et selle pikkus on 3 baiti. Iga meie võtmemassiivi indeks seatakse vastavalt selle konkreetse võtme elemendi kümnendväärtusele järjekorras. Kui olete kogu võtme läbi käinud, alustage algusest, kuni olete täitnud võtmemassiivi 8 pesa. Seega on meie võtmemassiiv järgmine:

- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### 3. samm

Kolmandaks muudame massiivi **S** kasutades võtmemassiivi **K**, protsessis, mida tuntakse kui **võtme ajakava**. Protsess on järgmine pseudokoodis:

- Loo muutujad **j** ja **i**
- Sea muutuja $j = 0$
- Iga $i$ jaoks 0-st 7-ni:
    - Sea $j = (j + S[i] + K[i]) \mod 8$
    - Vaheta $S[i]$ ja $S[j]$

Massiivi **S** muutmine on esitatud *Tabelis 1*.

Alustades, näete **S** algseisu kui $[0, 1, 2, 3, 4, 5, 6, 7]$ algväärtusega 0 **j** jaoks. See muudetakse kasutades võtmemassiivi $[14, 48, 9, 14, 48, 9, 14, 48]$.

Tsükkel for algab $i = 0$-st. Vastavalt meie pseudokoodile ülal, muutub **j** uueks väärtuseks 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Vahetades $S[0]$ ja $S[6]$, muutub **S** seisund pärast 1 vooru $[6, 1, 2, 3, 4, 5, 0, 7]$.
Järgmises reas, $i = 1$. For-tsükli uuesti läbides saab **j** väärtuseks 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Vahetades $S[1]$ ja $S[7]$ praeguses **S** olekus, $[6, 1, 2, 3, 4, 5, 0, 7]$, saame pärast teist vooru $[6, 7, 2, 3, 4, 5, 0, 1]$.

Jätkame seda protsessi, kuni oleme loonud **S** massiivi lõpliku rea allosas, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Tabel 1: Võtme ajastamise tabel*

| Voor    | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Algus   |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### 4. samm
Neljanda sammuna toodame **keystream**'i. See on pseudosuvaline jada, mille pikkus on võrdne sõnumiga, mida soovime saata. Seda kasutatakse algse sõnumi “SOUP” krüpteerimiseks. Kuna keystream peab olema sama pikk kui sõnum, on meil vaja ühte, mis on 4 baiti pikk.

Keystream toodetakse järgneva pseudokoodi abil:

- Loo muutujad **j**, **i** ja **t**.
- Sea $j = 0$.
- Iga $i$ jaoks plaintext'is, alustades $i = 1$ ja jätkates kuni $i = 4$, toodetakse iga keystream'i bait järgmiselt:
    - $j = (j + S[i]) \mod 8$
    - Vaheta $S[i]$ ja $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - $i^{th}$ bait keystream'is = $S[t]$

Arvutusi saab jälgida *Tabelis 2*.

**S** algseis on $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Sea $i = 1$, **j** väärtuseks saab 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Seejärel vahetame $S[1]$ ja $S[4]$, et toota **S** transformatsioon teises reas, $[6, 3, 1, 0, 4, 7, 5, 2]$. **t** väärtuseks saab siis 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Lõpuks on keystream'i bait $S[7]$, ehk 2.

Seejärel jätkame teiste baitide tootmist, kuni meil on järgmised neli baiti: 2, 6, 3 ja 7. Igaüht neist baitidest saab seejärel kasutada plaintext'i, "SOUP", iga tähe krüpteerimiseks.

Alustuseks, kasutades ASCII tabelit, näeme, et “SOUP” kodeerituna aluseks olevate baitide kümnendarvudega on “83 79 85 80”. Kombineerituna keystream'iga “2 6 3 7” saame “85 85 88 87”, mis jääb samaks pärast modulo 256 operatsiooni. ASCII's on krüptotekst “85 85 88 87” võrdne “UUXW”.

Mis juhtub, kui krüpteerida soovitud sõna on pikem kui massiiv **S**? Sellisel juhul jätkab massiiv **S** ülal kuvatud viisil transformeerumist iga plaintext'i baiti **i** jaoks, kuni meil on keystream'is baitide arv võrdne plaintext'i tähtede arvuga.


*Tabel 2: Keystream'i genereerimine*

| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    || 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Ülaltoodud näide, millest just rääkisime, on vaid lihtsustatud versioon **RC4 voošifrist**. Tegelikul RC4 voošifril on **S** massiiv 256 baiti pikk, mitte 8 baiti, ja võti võib olla vahemikus 1 kuni 256 baiti, mitte 1 kuni 8 baiti. Võtmemassiiv ja võtmevood on seejärel kõik toodetud arvestades **S** massiivi 256-baidist pikkust. Arvutused muutuvad märkimisväärselt keerukamaks, kuid põhimõtted jäävad samaks. Kasutades sama võtit, [14,48,9], standardse RC4 šifriga, krüpteeritakse lihttekst "SOUP" kui 67 02 ed df heksadetsimaalformaadis.

Voošifrit, milles võtmevoog uueneb sõltumatult lihttekstist või šifreeritud tekstist, nimetatakse **sünkroonseks voošifriks**. Võtmevoog sõltub ainult võtmest. Selgelt on RC4 näide sünkroonsest voošifrist, kuna võtmevoog ei oma seost ei lihtteksti ega šifreeritud tekstiga. Kõik meie eelmises peatükis mainitud primitiivsed voošifrid, sealhulgas nihkešifrit, Vigenère'i šifrit ja ühekordset paberit, olid samuti sünkroonse tüüpi.

Seevastu **asünkroonne voošifrit** on selline, mille võtmevoog on toodetud nii võtme kui ka šifreeritud teksti eelnevate elementide poolt. Seda tüüpi šifrit nimetatakse ka **ise-sünkroniseerivaks šifriks**.

Oluline on, et RC4-ga toodetud võtmevoogu tuleks kohelda kui ühekordset paberit ja te ei saa võtmevoogu järgmisel korral täpselt samal viisil toota. Praktiline lahendus on võtme iga kord muutmise asemel kombineerida võti **nonce'iga**, et toota baitvoog.

## AES 128-bitise võtmega
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Nagu eelmises peatükis mainitud, korraldas Riiklik Standardite ja Tehnoloogia Instituut (NIST) aastatel 1997 kuni 2000 võistluse, et määrata uus sümmeetriline krüpteerimisstandard. **Rijndaeli šifrit** osutus võitjaks. Nimi on sõnamäng Belgia loojate, Vincent Rijmeni ja Joan Daemeni nimedest.
Rijndaeli šiffer on **plokkšiffer**, mis tähendab, et on olemas põhialgoritm, mida saab kasutada erinevate võtme pikkuste ja ploki suurustega. Seejärel saab seda kasutada erinevate töörežiimidega, et konstrueerida krüpteerimisskeeme.
NISTi võistluse komitee võttis omaks piiratud versiooni Rijndaeli šifrist—nimelt sellise, mis nõuab 128-bitiseid ploki suurusi ja võtme pikkusi kas 128 biti, 192 biti või 256 biti ulatuses—osana **Advanced Encryption Standard (AES)**'ist. Seda piiratud versiooni Rijndaeli šifrist saab samuti kasutada mitme töörežiimi all. Standardi spetsifikatsioon on tuntud kui **Advanced Encryption Standard (AES)**.

Selleks, et näidata, kuidas Rijndaeli šiffer töötab, AES-i tuum, illustreerin ma krüpteerimisprotsessi 128-bitise võtmega. Võtme suurus mõjutab krüpteerimise iga ploki jaoks peetavate voorude arvu. 128-bitiste võtmete puhul on vajalik 10 vooru. 192-bitiste ja 256-bitiste puhul oleks see vastavalt 12 ja 14 vooru.

Lisaks eeldan, et AES-i kasutatakse **ECB-režiimis**. See teeb esitluse veidi lihtsamaks ja Rijndaeli algoritmi jaoks ei oma tähtsust. Kindlasti, ECB režiim ei ole praktikas turvaline, kuna see viib deterministliku krüpteerimiseni. Kõige sagedamini kasutatav turvaline režiim AES-iga on **CBC** (Cipher Block Chaining).

Nimetagem võtit $K_0$. Konstruktsioon ülaltoodud parameetritega näeb välja nagu *Joonis 1*, kus $M_i$ tähistab 128-bitist osa tavatekstist ja $C_i$ 128-bitist osa šifreeritud tekstist. Kui tavateksti ei saa ploki suurusega võrdselt jagada, lisatakse viimasele plokile polsterdus.


*Joonis 1: AES-ECB 128-bitise võtmega*

![Joonis 1: AES-ECB 128-bitise võtmega](assets/Figure5-1.webp "Joonis 1: AES-ECB 128-bitise võtmega")

Iga 128-bitine tekstiplokk läbib Rijndaeli krüpteerimisskeemis kümme vooru. See nõuab iga vooru jaoks eraldi vooruvõtit ($K_1$ kuni $K_{10}$). Need on toodetud iga vooru jaoks algsest 128-bitisest võtmest $K_0$, kasutades **võtme laiendamise algoritmi**. Seega, iga krüpteeritava tekstiploki jaoks kasutame algset võtit $K_0$ ning kümme eraldi vooruvõtit. Pane tähele, et neid samu 11 võtit kasutatakse iga 128-bitise tavateksti ploki krüpteerimiseks, mis seda nõuab.

Võtme laiendamise algoritm on pikk ja keeruline. Selle läbitöötamine ei paku didaktilist kasu. Võite võtme laiendamise algoritmi ise uurida, kui soovite. Kui vooruvõtmed on toodetud, manipuleerib Rijndaeli šiffer esimest 128-bitist tavateksti plokki, $M_1$, nagu on näha *Joonisel 2*. Nüüd käime läbi need sammud.

*Joonis 2: $M_1$ manipuleerimine Rijndaeli šifriga:*

**Voor 0:**
- XOR $M_1$ ja $K_0$, et toota $S_0$

---

**Voor n n = {1,...,9}:**
- XOR $S_{n-1}$ ja $K_n$
- Baidi Asendus
- Ridade Nihutamine
- Veergude Segamine
- XOR $S$ ja $K_n$, et toota $S_n$

---

**Voor 10:**
- XOR $S_9$ ja $K_{10}$ - baitide asendamine
- Read nihutamine
- XOR $S$ ja $K_{10}$, et toota $S_{10}$
- $S_{10}$ = $C_1$

### Voor 0

Rijndaeli šifri voor 0 on lihtne. Massiiv $S_0$ saadakse 128-bitise avateksti ja privaatvõtme XOR-operatsiooni tulemusena. See tähendab,

- $S_0 = M_1 \oplus K_0$

### Voor 1

Voorus 1 kombineeritakse massiiv $S_0$ esmalt vooruvõtmega $K_1$, kasutades XOR-operatsiooni. See toodab uue oleku $S$.

Teiseks viiakse läbi **baitide asendamise** operatsioon praeguses $S$ olekus. See toimib nii, et võetakse iga 16-baidise $S$ massiivi bait ja asendatakse see baidiga massiivist, mida nimetatakse **Rijndaeli S-kastiks**. Igal baidil on unikaalne transformatsioon ja tulemusena saadakse uus olek $S$. Rijndaeli S-kasti kuvatakse *joonisel 3*.

*Joonis 3: Rijndaeli S-Kast*

|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
| 50  | 53  | D1  | 00  | ED  | 20  | FC  | B1  | 5B  | 6A  | CB  | BE  | 39  | 4A  | 4C  | 58  | CF  ||
| 60  | D0  | EF  | AA  | FB  | 43  | 4D  | 33  | 85  | 45  | F9  | 02  | 7F  | 50  | 3C  | 9F  | A8  |
| 70  | 51  | A3  | 40  | 8F  | 92  | 9D  | 38  | F5  | BC  | B6  | DA  | 21  | 10  | FF  | F3  | D2  |
| 80  | CD  | 0C  | 13  | EC  | 5F  | 97  | 44  | 17  | C4  | A7  | 7E  | 3D  | 64  | 5D  | 19  | 73  |
| 90  | 60  | 81  | 4F  | DC  | 22  | 2A  | 90  | 88  | 46  | EE  | B8  | 14  | DE  | 5E  | 0B  | DB  |
| A0  | E0  | 32  | 3A  | 0A  | 49  | 06  | 24  | 5C  | C2  | D3  | AC  | 62  | 91  | 95  | E4  | 79  |
| B0  | E7  | C8  | 37  | 6D  | 8D  | D5  | 4E  | A9  | 6C  | 56  | F4  | EA  | 65  | 7A  | AE  | 08  |
| C0  | BA  | 78  | 25  | 2E  | 1C  | A6  | B4  | C6  | E8  | DD  | 74  | 1F  | 4B  | BD  | 8B  | 8A  |
| D0  | 70  | 3E  | B5  | 66  | 48  | 03  | F6  | 0E  | 61  | 35  | 57  | B9  | 86  | C1  | 1D  | 9E  |
| E0  | E1  | F8  | 98  | 11  | 69  | D9  | 8E  | 94  | 9B  | 1E  | 87  | E9  | CE  | 55  | 28  | DF  |
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |

See S-kast on üks koht, kus abstraktne algebra mängib rolli Rijndaeli šifris, eriti **Galois' väljad**.

Alustuseks defineerite iga võimaliku bait elemendi 00 kuni FF kui 8-bitise vektori. Iga selline vektor on elemendiks **Galois' väljal GF(2^8)**, kus modulo operatsiooni jaoks on redutseerimatu polünoom $x^8 + x^4 + x^3 + x + 1$. Galois' väli nende spetsifikatsioonidega on samuti tuntud kui **Rijndaeli lõplik väli**.

Järgmiseks, iga võimaliku elemendi jaoks väljal, loome nn **Nybergi S-kasti**. Selles kastis on iga bait kaardistatud oma **multiplikatiivsele pöördarvule** (st nii, et nende korrutis võrdub 1-ga). Seejärel kaardistame need väärtused Nybergi S-kastist Rijndaeli S-kasti kasutades **afiiinset teisendust**.

Kolmas operatsioon **S** massiivil on **ridade nihutamise** operatsioon. See võtab **S** oleku ja loetleb kõik kuusteist baiti maatriksis. Maatriksi täitmine algab ülevalt vasakult ja liigub edasi minnes ülevalt alla ja seejärel, iga kord kui veerg on täidetud, nihutades ühe veeru paremale ja üles.

Kui **S** maatriks on koostatud, nihutatakse neli rida. Esimene rida jääb samaks. Teine rida liigub ühe võrra vasakule. Kolmas liigub kaks võrra vasakule. Neljas liigub kolm võrra vasakule. Protsessi näide on toodud *Joonisel 4*. **S** algolek on näidatud ülal ja tulemuslik olek pärast ridade nihutamise operatsiooni on näidatud allpool.

*Joonis 4: Ridade nihutamise operatsioon*

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


Neljandas sammus ilmuvad **Galois' väljad** jälle. Alustuseks korrutatakse iga **S** maatriksi veerg 4 x 4 maatriksi veeruga, mida näeb *Joonisel 5*. Kuid selle asemel, et tegemist oleks tavalise maatriksikorrutusega, on see vektorite korrutamine **modulo redutseerimatu polünoomi**, $x^8 + x^4 + x^3 + x + 1$. Saadud vektori kordajad esindavad baidi üksikuid bitte.

*Joonis 5: Veergude segamise maatriks*

| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   || 03   | 01   | 01   | 02   |

Esimese veeru korrutamine **S** maatriksi esimese veeruga ülaltoodud 4 x 4 maatriksiga annab tulemuse *Joonisel 6*.

*Joonis 6: Esimese veeru korrutamine:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Järgmise sammuna tuleb kõik maatriksi elemendid teisendada polünoomideks. Näiteks F1, mis esindab 1 baiti, muutub $x^7 + x^6 + x^5 + x^4 + 1$-ks ja 03, mis samuti esindab 1 baiti, muutub $x + 1$-ks.

Kõik korrutamised tehakse seejärel **modulo** $x^8 + x^4 + x^3 + x + 1$. See toob kaasa nelja polünoomi liitmise igas veeru neljast lahtrist. Pärast nende liitmiste sooritamist **modulo 2**, saadakse neli polünoomi. Iga selline polünoom esindab 8-bitist jada ehk 1 baiti **S**-st. Me ei soorita siin kõiki neid arvutusi *Joonisel 6* kujutatud maatriksis, kuna need on mahukad.

Pärast esimese veeru töötlemist töödeldakse **S** maatriksi teisi kolme veeru samal viisil. Lõpuks saadakse maatriks, mis koosneb kuusteistkümnest baidist ja mida saab teisendada massiiviks.

Viimase sammuna kombineeritakse massiiv **S** uuesti ringvõtmega **XOR** operatsiooni kaudu. See toodab oleku $S_1$. See tähendab,

- $S_1 = S \oplus K_0$

### Voorud 2 kuni 10

Voorud 2 kuni 9 on lihtsalt vooru 1 kordus, *mutatis mutandis*. Viimane voor näeb välja väga sarnane eelnevatele voorudele, välja arvatud see, et **segamise veerge** sammu ei toimu. See tähendab, et voor 10 viiakse läbi järgmiselt:

- $S_9 \oplus K_{10}$
- Baidi Asendamine
- Read Nihutamine
- $S_{10} = S \oplus K_{10}$

Olek $S_{10}$ on nüüd seadistatud $C_1$-ks, esimeseks 128 bitiks šifreeritud tekstist. Järgnevate 128-bitiste tavateksti plokkide töötlemine annab täieliku šifreeritud teksti **C**.

### Rijndaeli šifri toimingud

Mis on erinevate toimingute põhjendus Rijndaeli šifris?

Detailidesse laskumata hinnatakse krüpteerimisskeeme selle alusel, kuivõrd need loovad segadust ja hajutatust. Kui krüpteerimisskeemil on kõrge **segaduse** aste, tähendab see, et šifreeritud tekst näeb välja drastiliselt erinev tavatekstist. Kui krüpteerimisskeemil on kõrge **hajutatuse** aste, tähendab see, et iga väike muudatus tavatekstis toodab drastiliselt erineva šifreeritud teksti.
Rijndaeli šifri toimingute põhjendus seisneb selles, et need toodavad nii kõrget segaduse kui ka difusiooni astet. Segadus tekib baitide asendamise toimingust, samal ajal kui difusioon tekib ridade nihutamise ja veergude segamise toimingutest.
# Asümmeetriline krüptograafia
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Võtmete jaotamise ja haldamise probleem
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Nagu sümmeetrilise krüptograafia puhul, saab asümmeetrilisi skeeme kasutada nii saladuse hoidmiseks kui ka autentimiseks. Erinevus seisneb siiski selles, et nende skeemide puhul kasutatakse kahte võtit, mitte ühte: privaatvõtit ja avalikku võtit.

Alustame oma uurimist asümmeetrilise krüptograafia avastamisest, eriti probleemidest, mis seda esile kutsusid. Järgnevalt arutame, kuidas asümmeetrilised skeemid krüpteerimiseks ja autentimiseks kõrgel tasemel töötavad. Seejärel tutvustame räsi funktsioone, mis on võtmetähtsusega asümmeetriliste autentimisskeemide mõistmisel ning omavad tähtsust ka teistes krüptograafilistes kontekstides, nagu näiteks 4. peatükis arutatud räsi-põhised sõnumi autentimiskoodid.

___

Kujutage ette, et Bob soovib osta uue vihmamantli Jim’s Sporting Goods'ist, veebipõhisest spordikaupade jaemüüjast, millel on miljoneid kliente Põhja-Ameerikas. See saab olema tema esimene ost neilt ja ta soovib kasutada oma krediitkaarti. Seega peab Bob esmalt looma konto Jim’s Sporting Goods'is, mis nõuab isiklike andmete, nagu tema aadressi ja krediitkaardi informatsiooni, saatmist. Seejärel saab ta läbida vajalikud sammud vihmamantli ostmiseks.

Bob ja Jim’s Sporting Goods soovivad tagada, et nende suhtlus oleks kogu protsessi vältel turvaline, arvestades, et Internet on avatud suhtlussüsteem. Nad soovivad näiteks tagada, et ükski potentsiaalne ründaja ei saaks teada Bobi krediitkaardi ja aadressi andmeid ning et ükski potentsiaalne ründaja ei saaks korrata tema oste või luua tema nimel võltsoste.

Eelmises peatükis arutatud edasijõudnud autentitud krüpteerimisskeem võiks kindlasti muuta suhtluse Bobi ja Jim’s Sporting Goods'i vahel turvaliseks. Kuid on selgeid praktilisi takistusi sellise skeemi rakendamisel.

Nende praktiliste takistuste illustreerimiseks kujutage ette, et elame maailmas, kus eksisteerivad ainult sümmeetrilise krüptograafia vahendid. Mida saaksid Jim’s Sporting Goods ja Bob siis teha, et tagada turvaline suhtlus?

Sellistes tingimustes seisaksid nad silmitsi märkimisväärsete kuludega turvaliseks suhtlemiseks. Kuna Internet on avatud suhtlussüsteem, ei saa nad lihtsalt vahetada võtmeid selle kaudu. Seega peavad Bob ja Jim’s Sporting Goods'i esindaja tegema võtmevahetuse isiklikult.

Üks võimalus on, et Jim’s Sporting Goods loob erilised võtmevahetuse kohad, kus Bob ja teised uued kliendid saavad turvalise suhtluse jaoks võtmeid hankida. See tooks kaasa märkimisväärseid organisatsioonilisi kulusid ja vähendaks oluliselt uute klientide ostude tegemise efektiivsust.

Teisalt võib Jim’s Sporting Goods saata Bobile võtmepaari usaldusväärse kulleri kaudu. See on tõenäoliselt efektiivsem kui võtmevahetuse kohtade korraldamine. Kuid see tooks siiski kaasa märkimisväärseid kulusid, eriti kui paljud kliendid teevad ainult ühe või mõned ostud.

Lisaks sunnib sümmeetriline autentitud krüpteerimisskeem Jim’s Sporting Goods'i hoidma eraldi võtmekomplekte kõigi oma klientide jaoks. See oleks märkimisväärne praktiline väljakutse tuhandete klientide puhul, rääkimata miljonitest.
Selle viimase punkti mõistmiseks kujutage ette, et Jimi Spordikaubad annab igale kliendile sama paari võtmeid. See võimaldaks igal kliendil – või ükskõik kellel, kes need võtmed kätte saaks – lugeda ja isegi manipuleerida kõigi suhtlustega Jimi Spordikaupade ja selle klientide vahel. Sel juhul võiks sama hästi üldse krüptograafiat oma suhtluses mitte kasutada.

Isegi võtmete korduv kasutamine ainult mõne kliendi jaoks on kohutav turvapraktika. Iga potentsiaalne ründaja võiks proovida seda skeemi omadust ära kasutada (pidage meeles, et eeldatakse, et ründajad teavad kõike skeemi kohta peale võtmete, vastavalt Kerckhoffs’i põhimõttele).

Seega peaks Jimi Spordikaubad hoidma iga kliendi jaoks paari võtmeid, olenemata sellest, kuidas neid võtmepaare jaotatakse. See esitab selgelt mitmeid praktilisi probleeme.

- Jimi Spordikaubad peaks hoidma miljoneid võtmepaare, iga kliendi jaoks ühe komplekti.
- Neid võtmeid tuleks korralikult kaitsta, kuna need oleksid kindel sihtmärk häkkeritele. Iga turvaintsident nõuaks kulukate võtmevahetuste kordamist, kas erilistes võtmevahetuspunktides või kulleri kaudu.
- Iga Jimi Spordikaupade klient peaks kodus turvaliselt hoidma võtmepaari. Kaod ja vargused juhtuvad, nõudes võtmevahetuste kordamist. Kliendid peaksid läbima selle protsessi ka mis tahes muude veebipoodide või muud tüüpi üksustega, kellega nad soovivad interneti kaudu suhelda ja tehinguid teha.

Need kaks peamist väljakutset, mida just kirjeldati, olid kuni 1970ndate lõpuni väga fundamentaalsed mured. Neid tunti vastavalt **võtmete levitamise probleemi** ja **võtmete haldamise probleemina**.

Need probleemid olid alati olemas olnud, muidugi, ja sageli tekitanud peavalu minevikus. Näiteks sõjaväejõud pidid pidevalt levitama raamatuid võtmetega turvaliseks suhtluseks välitöötajatele suurte riskide ja kuludega. Kuid need probleemid muutusid hullemaks, kuna maailm liikus üha enam pika vahemaa digitaalse suhtluse poole, eriti valitsusväliste üksuste jaoks.

Kui neid probleeme poleks 1970ndatel lahendatud, siis tõenäoliselt ei oleks Jimi Spordikaupade juures efektiivset ja turvalist ostlemist olemas olnud. Tegelikult oleks enamik meie kaasaegsest maailmast, kus on praktiline ja turvaline e-posti kasutamine, internetipangandus ja ostlemine, tõenäoliselt olnud vaid kauge fantaasia. Midagi isegi Bitcoinile sarnanevat ei oleks üldse olemas olnud.

Niisiis, mis juhtus 1970ndatel? Kuidas on võimalik, et me saame hetkega teha oste internetis ja turvaliselt sirvida maailma laia veebi? Kuidas on võimalik, et me saame hetkega saata Bitcoine üle kogu maailma oma nutitelefonidest?

## Uued suunad krüptograafias
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

1970ndatel pälvisid võtmete levitamise ja haldamise probleemid Ameerika akadeemiliste krüptograafide rühma tähelepanu: Whitfield Diffie, Martin Hellman ja Ralph Merkle. Tugeva skeptitsismi valitseva osa oma kolleegide seas silmitsi seistes asusid nad lahendust otsima.

Vähemalt üks peamine motivatsioon nende ettevõtmiseks oli ettenägelikkus, et avatud arvutisuhtlus mõjutab meie maailma sügavalt. Nagu Diffie ja Hellman märkisid 1976. aastal,
Arvutiga juhitavate kommunikatsioonivõrkude areng lubab vaevata ja odavat kontakti inimeste või arvutite vahel maailma eri otstes, asendades enamiku postist ja paljud väljasõidud telekommunikatsiooniga. Paljudel rakendustel peavad need kontaktid olema turvatud nii pealtkuulamise kui ka ebaseaduslike sõnumite sisestamise vastu. Praegu aga jääb turvaprobleemide lahendamine oluliselt maha teistest kommunikatsioonitehnoloogia valdkondadest. *Kaasaegne krüptograafia ei suuda nõudmisi täita, kuna selle kasutamine tooks kasutajatele kaasa sellised tõsised ebamugavused, mis kõrvaldaksid paljud teleprotsessi eelised.* [1] Diffie, Hellmani ja Merkle'i visadus tasus end ära. Nende tulemuste esimene avaldamine oli Diffie ja Hellmani poolt 1976. aastal pealkirjaga “New Directions in Cryptography.” Selles esitlesid nad kahte originaalset lahendust võtmehalduse ja võtmejaotuse probleemidele.

Esimene lahendus, mida nad pakkusid, oli kaug-*võtmevahetusprotokoll*, see tähendab reeglite kogum ühe või mitme sümmeetrilise võtme vahetamiseks turvamata suhtluskanali kaudu. See protokoll on nüüd tuntud kui *Diffie-Hellmani võtmevahetus* või *Diffie-Hellmani-Merkle'i võtmevahetus*. [2]

Diffie-Hellmani võtmevahetusega vahetavad kaks osapoolt esmalt mõningast informatsiooni avalikult turvamata kanalil nagu Internet. Selle informatsiooni põhjal loovad nad seejärel iseseisvalt sümmeetrilise võtme (või paar sümmeetrilist võtit) turvaliseks suhtluseks. Kuigi mõlemad osapooled loovad oma võtmed iseseisvalt, tagab avalikult jagatud informatsioon, et see võtmete loomise protsess annab mõlemale neist sama tulemuse.

Oluline on, et kuigi kõik võivad jälgida informatsiooni, mida osapooled avalikult turvamata kanali kaudu vahetavad, saavad ainult need kaks osapoolt, kes informatsiooni vahetavad, sellest sümmeetrilisi võtmeid luua.

See kõlab muidugi täiesti vastuoluliselt. Kuidas saavad kaks osapoolt vahetada mõningast informatsiooni avalikult, mis lubab ainult neil luua sümmeetrilisi võtmeid? Miks ei suudaks keegi teine, kes jälgib informatsiooni vahetust, luua samu võtmeid?

See tugineb muidugi mõnele kaunile matemaatikale. Diffie-Hellmani võtmevahetus toimib ühesuunalise funktsiooni abil, millel on lõks. Arutame neid kahte terminit järjekorras.

Oletame, et teile on antud mingi funktsioon $f(x)$ ja tulemus $f(a) = y$, kus $a$ on konkreetne väärtus $x$ jaoks. Me ütleme, et $f(x)$ on **ühesuunaline funktsioon**, kui on lihtne arvutada väärtust $y$, kui on antud $a$ ja $f(x)$, kuid on arvutuslikult teostamatu arvutada väärtust $a$, kui on antud $y$ ja $f(x)$. Nimi **ühesuunaline funktsioon** tuleneb muidugi asjaolust, et sellist funktsiooni on praktiline arvutada ainult ühes suunas.

Mõnel ühesuunalisel funktsioonil on see, mida tuntakse kui **lõksu**. Kuigi on praktiliselt võimatu arvutada $a$, kui on antud ainult $y$ ja $f(x)$, on olemas teatud teave $Z$, mis muudab $a$ arvutamise $y$-st arvutuslikult teostatavaks. See teave $Z$ on tuntud kui **lõks**. Ühesuunalisi funktsioone, millel on lõks, tuntakse kui **lõksufunktsioone**.
Me ei süvene siin Diffie-Helmanni võtmevahetuse detailidesse. Kuid põhimõtteliselt loob iga osaleja teatud informatsiooni, millest osa jagatakse avalikult ja millest osa jääb salajaseks. Seejärel võtab iga osapool oma salajase informatsiooni ja teise osapoole poolt jagatud avaliku informatsiooni, et luua privaatvõti. Ja üsna imelisel kombel jõuavad mõlemad osapooled sama privaatvõtmeni. 
Ükski osapool, kes jälgib ainult kahe osapoole vahel avalikult jagatud informatsiooni Diffie-Helmanni võtmevahetuses, ei suuda neid arvutusi korrata. Selleks oleks vaja ühe kahest osapoolest privaatset informatsiooni.

Kuigi Diffie-Helmanni võtmevahetuse põhiversioon, mis esitati 1976. aasta artiklis, ei ole väga turvaline, on selle põhiprotokolli keerukamad versioonid kindlasti tänapäeval veel kasutusel. Kõige tähtsam on, et iga võtmevahetusprotokoll transpordikihi turvalisuse protokolli viimases versioonis (versioon 1.3) on sisuliselt rikastatud versioon protokollist, mille esitasid Diffie ja Hellman 1976. aastal. Transpordikihi turvalisuse protokoll on valdav protokoll veebisisu vahetamiseks vastavalt hüperteksti edastusprotokollile (http), mis on veebisisu vahetamise standard.

Oluline on märkida, et Diffie-Helmanni võtmevahetus ei ole asümmeetriline skeem. Rangelt öeldes kuulub see tõenäoliselt sümmeetrilise võtmekrüptograafia valdkonda. Kuid kuna nii Diffie-Helmanni võtmevahetus kui ka asümmeetriline krüptograafia tuginevad ühesuunalistele arvuteoreetilistele funktsioonidele koos lõksudega, arutatakse neid tavaliselt koos.

Teine viis, kuidas Diffie ja Hellman pakkusid oma 1976. aasta artiklis võtmete jaotuse ja halduse probleemi lahendada, oli muidugi asümmeetrilise krüptograafia kaudu.

Erinevalt nende Diffie-Hellmani võtmevahetuse esitlusest andsid nad ainult üldised kontuurid, kuidas asümmeetrilisi krüptograafilisi skeeme võiks usutavalt konstrueerida. Nad ei pakkunud ühtegi ühesuunalist funktsiooni, mis võiks spetsiifiliselt täita mõistliku turvalisuse tingimusi sellistes skeemides.

Praktiline asümmeetrilise skeemi rakendus leiti siiski aasta hiljem kolme erineva akadeemilise krüptograafi ja matemaatiku poolt: Ronald Rivest, Adi Shamir ja Leonard Adleman. [3] Nende tutvustatud krüptosüsteem sai tuntuks kui **RSA krüptosüsteem** (nende perekonnanimede järgi).

Asümmeetrilises krüptograafias (ja Diffie-Helmanni võtmevahetuses) kasutatavad lõksufunktsioonid on seotud kahe peamise **arvutuslikult keeruka probleemiga**: algarvude tegurdamine ja diskreetsete logaritmide arvutamine.

**Algarvude tegurdamine** nõuab, nagu nimigi ütleb, täisarvu lagundamist selle algarvudeks. RSA probleem on kaugelt kõige tuntum näide krüptosüsteemist, mis on seotud algarvude tegurdamisega.

**Diskreetse logaritmi probleem** on probleem, mis esineb tsüklilistes gruppides. Antud generaatori korral konkreetses tsüklilises grupis nõuab see unikaalse eksponendi arvutamist, mis on vajalik teise elemendi tootmiseks grupis generaatorist.

Diskreetse logaritmi põhised skeemid tuginevad kahele peamisele tsükliliste gruppide liigile: täisarvude korrutusgrupid ja grupid, mis hõlmavad punkte elliptilistel kõveratel. Algupärane Diffie-Helmanni võtmevahetus, nagu esitati "Uutes suundades krüptograafias", töötab täisarvude tsüklilise korrutusgrupiga. Bitcoini digitaalne allkirja algoritm ja hiljuti tutvustatud Schnorri allkirja skeem (2021) põhinevad mõlemad diskreetse logaritmi probleemil konkreetse elliptilise kõvera tsüklilises grupis.

Järgnevalt pöörame tähelepanu kõrgetasemelisele ülevaatele saladusest ja autentimisest asümmeetrilises seades. Enne seda peame siiski tegema lühikese ajaloolise märkuse.
Tundub nüüd usutav, et grupp Briti krüptograafe ja matemaatikuid, kes töötasid Valitsuse Sidepeakorteri (GCHQ) heaks, olid iseseisvalt teinud eespool mainitud avastused mõned aastad varem. Sellesse gruppi kuulusid James Ellis, Clifford Cocks ja Malcolm Williamson.

Nende endi ja GCHQ aruannete kohaselt oli James Ellis see, kes esimesena töötas välja avaliku võtme krüptograafia kontseptsiooni 1969. aastal. Väidetavalt avastas Clifford Cocks seejärel RSA krüptograafiasüsteemi 1973. aastal ja Malcolm Williamson Diffie-Hellmani võtmevahetuse kontseptsiooni 1974. aastal. [4] Nende avastused aga väidetavalt ei avalikustatud enne 1997. aastat, arvestades GCHQ-s tehtud töö salajast olemust.

**Märkused:**

[1] Whitfield Diffie ja Martin Hellman, “New directions in cryptography,” _IEEE Transactions on Information Theory_ IT-22 (1976), lk. 644–654, lk. 644.

[2] Ralph Merkle arutleb samuti võtmevahetuse protokolli üle oma töös “Secure communications over insecure channels”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Kuigi Merkle esitas selle töö enne Diffie ja Hellmani tööd, avaldati see hiljem. Merkle'i lahendus ei ole eksponentsiaalselt turvaline, erinevalt Diffie-Hellmani omast.

[3] Ron Rivest, Adi Shamir ja Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, _Communications of the Association for Computing Machinery_, 21 (1978), lk. 120–26.

[4] Hea ülevaate nendest avastustest pakub Simon Singh, _The Code Book_, Fourth Estate (London, 1999), 6. peatükk.

## Asümmeetriline krüpteerimine ja autentimine
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Ülevaade **asümmeetrilisest krüpteerimisest** Bobi ja Alice'i abil on esitatud *joonisel 1*.

Alice loob esmalt võtmepaari, mis koosneb ühest avalikust võtmest ($K_P$) ja ühest privaatsest võtmest ($K_S$), kus “P” $K_P$-s tähistab “public” (avalik) ja “S” $K_S$-s “secret” (salajane). Seejärel jagab ta seda avalikku võtit vabalt teistega. Naaseme selle jaotusprotsessi detailide juurde veidi hiljem. Praegu eeldame, et igaüks, sealhulgas Bob, saab Alice'i avaliku võtme $K_P$ turvaliselt kätte.

Hiljem soovib Bob saata sõnumi $M$ Alice'ile. Kuna see sisaldab tundlikku teavet, soovib ta, et sõnumi sisu jääks saladuseks kõigile peale Alice'i. Seega krüpteerib Bob esmalt oma sõnumi $M$, kasutades $K_P$. Seejärel saadab ta tulemuseks oleva šifreeritud teksti $C$ Alice'ile, kes dekrüpteerib $C$ $K_S$ abil, et taastada algne sõnum $M$.

*Joonis 1: Asümmeetriline krüpteerimine*

![Joonis 1: Asümmeetriline krüpteerimine](assets/Figure6-1.webp "Joonis 1: Asümmeetriline krüpteerimine")



Iga vaenlane, kes kuulab pealt Bobi ja Alice'i suhtlust, võib märgata $C$. Ta teab ka $K_P$ ja krüpteerimisalgoritmi $E(\cdot)$. Oluline on aga see, et see teave ei võimalda ründajal šifreeritud teksti $C$ teostatavalt dekrüpteerida. Dekrüpteerimiseks on konkreetselt vajalik $K_S$, mida ründajal ei ole.
Sümmeetrilised krüpteerimisskeemid peavad üldiselt olema turvalised ründaja vastu, kes suudab õiguspäraselt krüpteerida selgetekstisõnumeid (tuntud kui valitud šifreeritud teksti ründe turvalisus). Siiski ei ole see kavandatud spetsiaalselt selleks, et võimaldada ründajal või kellelgi teisel selliseid õiguspäraseid šifreeritud tekste luua.
See on teravas kontrastis asümmeetrilise krüpteerimisskeemiga, mille peamine eesmärk on võimaldada kõigil, sealhulgas ründajatel, luua õiguspäraseid šifreeritud tekste. Seega võib asümmeetrilisi krüpteerimisskeeme nimetada **mitme juurdepääsuga šifriks**.

Et paremini mõista, mis toimub, kujutage ette, et selle asemel, et saata sõnum elektrooniliselt, soovis Bob saata füüsilise kirja salajaselt. Üks viis salajasuse tagamiseks oleks, kui Alice saadaks Bobile turvalise tabaluku, kuid hoiaks võtit enda käes. Pärast kirja kirjutamist võiks Bob panna kirja kasti ja sulgeda selle Alice'i tabalukuga. Seejärel võiks ta saata lukustatud kasti sõnumiga Alicele, kellel on võti selle avamiseks.

Kuigi Bob suudab tabaluku lukustada, ei saa ei tema ega ükski teine isik, kes kasti kinni püüab, tabalukku avada, kui see on tõepoolest turvaline. Ainult Alice saab selle avada ja näha Bobi kirja sisu, sest tal on võti.

Asümmeetriline krüpteerimisskeem on, üldjoontes öeldes, selle protsessi digitaalne versioon. Tabalukk on sarnane avalikule võtmele ja tabaluku võti on sarnane privaatvõtmega. Kuna tabalukk on digitaalne, on Alicel siiski palju lihtsam ja mitte nii kulukas seda jagada kõigile, kes võivad soovida talle salajasi sõnumeid saata.

Autentimiseks asümmeetrilises seades kasutame **digitaalseid allkirju**. Need täidavad seega sama funktsiooni kui sõnumi autentimiskoodid sümmeetrilises seades. Digitaalsete allkirjade ülevaade on esitatud *joonisel 2*.

Bob loob esmalt võtmepaari, mis koosneb avalikust võtmest ($K_P$) ja privaatvõtmest ($K_S$), ning jagab oma avalikku võtit. Kui ta soovib saata Alicele autentitud sõnumi, võtab ta esmalt oma sõnumi $M$ ja oma privaatvõtme, et luua **digitaalne allkiri** $D$. Seejärel saadab Bob Alicele oma sõnumi koos digitaalse allkirjaga.

Alice sisestab sõnumi, avaliku võtme ja digitaalse allkirja **kontrollimisalgoritmi**. See algoritm toodab kas **tõene** kehtiva allkirja või **väär** kehtetu allkirja korral.

Digitaalne allkiri on, nagu nimi selgelt viitab, kirjaliku allkirja digitaalne ekvivalent kirjadel, lepingutel ja nii edasi. Tegelikult on digitaalne allkiri tavaliselt palju turvalisem. Kirjaliku allkirja võib teatud vaevaga võltsida; protsessi lihtsustab asjaolu, et kirjalikke allkirju ei kontrollita sageli põhjalikult. Turvaline digitaalne allkiri on aga, nagu turvaline sõnumi autentimiskood, **eksistentsiaalselt võltsimiskindel**: see tähendab, et turvalise digitaalse allkirja skeemi korral ei saa keegi loogiliselt luua allkirja sõnumile, mis läbib kontrollimisprotseduuri, kui neil pole privaatvõtit.

*Joonis 2: Asümmeetriline autentimine*

![Joonis 2: Asümmeetriline autentimine](assets/Figure6-2.webp "Joonis 2: Asümmeetriline autentimine")

Nagu asümmeetrilise krüpteerimise puhul, näeme huvitavat kontrasti digitaalsete allkirjade ja sõnumi autentimiskoodide vahel. Viimase puhul saab kontrollimisalgoritmi kasutada ainult üks osapooltest, kes on turvalise suhtlusega kursis. See on nii, sest see nõuab privaatvõtit. Asümmeetrilises seades aga võib igaüks kontrollida Bobi tehtud digitaalset allkirja $S$.
Kõik see teeb digitaalallkirjadest äärmiselt võimsa tööriista. See on näiteks aluseks lepingute allkirjastamisele, mida saab õiguslikel eesmärkidel kontrollida. Kui Bob oleks eelpool mainitud vahetuses lepingule allkirja andnud, saab Alice näidata kohtule sõnumit $M$, lepingut ja allkirja $S$. Kohus saab seejärel Bobi avaliku võtme abil allkirja kontrollida. [5]
Teise näitena on digitaalallkirjad olulised turvalise tarkvara ja tarkvarauuenduste levitamisel. Sellist avalikku kontrollitavust ei oleks võimalik luua ainult sõnumi autentimiskoodide abil.

Viimase näitena digitaalallkirjade võimsusest võtke arvesse Bitcoini. Üks levinumaid väärarusaamu Bitcoini kohta, eriti meedias, on see, et tehingud on krüpteeritud: tegelikult ei ole nad seda. Selle asemel töötavad Bitcoin tehingud digitaalallkirjade abil, et tagada turvalisus.

Bitcoinid eksisteerivad partiidena, mida nimetatakse kulutamata tehinguväljunditeks (või **UTXO-deks**). Oletame, et saate kindlal Bitcoin aadressil kolm makset, igaüks 2 bitcoini. Tehniliselt ei ole teil nüüd sellel aadressil 6 bitcoini. Selle asemel on teil kolm 2-bitcoinist partiid, mis on lukustatud krüptograafilise probleemiga, mis on seotud selle aadressiga. Iga makse tegemisel võite kasutada ühte, kahte või kõiki kolme neist partiidest, sõltuvalt sellest, kui palju teil tehingu jaoks vaja on.

Kulutamata tehinguväljundite omandiõiguse tõend esitatakse tavaliselt ühe või mitme digitaalallkirja kaudu. Bitcoin töötab täpselt seetõttu, et kehtivate digitaalallkirjade loomine kulutamata tehinguväljunditele on arvutuslikult teostamatu, kui te ei oma salajast teavet, mis on nende loomiseks vajalik.

Praegu sisaldavad Bitcoin tehingud läbipaistvalt kogu teavet, mida võrgus osalejad peavad kontrollima, nagu tehingu kasutatud kulutamata tehinguväljundite päritolu. Kuigi on võimalik peita osa sellest teabest ja siiski lubada kontrollimist (nagu teevad mõned alternatiivsed krüptorahad, nagu Monero), loob see ka erilisi turvariske.

Segadus tekib mõnikord digitaalallkirjade ja digitaalselt jäädvustatud kirjalike allkirjade vahel. Viimasel juhul jäädvustate oma kirjaliku allkirja pildi ja kleepite selle elektroonilisele dokumendile, näiteks töölepingule. See aga ei ole krüptograafilises mõttes digitaalallkiri. Viimane on lihtsalt pikk number, mida saab toota ainult eraõigusliku võtme olemasolul.

Nagu sümmeetrilise võtme seadistuses, saate kasutada ka asümmeetrilist krüpteerimist ja autentimisskeeme koos. Sarnased põhimõtted kehtivad. Esiteks peaksite kasutama erinevaid era- ja avaliku võtme paare krüpteerimiseks ja digitaalallkirjade tegemiseks. Lisaks peaksite esmalt sõnumi krüpteerima ja seejärel autentima.

Oluline on, et paljudes rakendustes ei kasutata asümmeetrilist krüptograafiat kogu suhtlusprotsessi vältel. Selle asemel kasutatakse seda tavaliselt ainult *sümmeetriliste võtmete vahetamiseks* osapoolte vahel, millega nad tegelikult suhtlevad.

See on näiteks juhul, kui ostate kaupu veebis. Tundes müüja avalikku võtit, saab ta saata teile digitaalselt allkirjastatud sõnumeid, mille autentsust saate kontrollida. Selle põhjal saate järgida mitmeid protokolle sümmeetriliste võtmete turvaliseks vahetamiseks.

Peamine põhjus eelpool mainitud lähenemisviisi sageduseks on see, et asümmeetriline krüptograafia on palju vähem efektiivne kui sümmeetriline krüptograafia, et toota teatud turvatase. See on üks põhjus, miks me vajame sümmeetrilise võtme krüptograafiat avaliku krüptograafia kõrval. Lisaks on sümmeetriline võtme krüptograafia palju loomulikum erirakendustes, nagu arvutikasutaja oma andmete krüpteerimine.

Niisiis, kuidas täpselt digitaalallkirjad ja avaliku võtme krüpteerimine lahendavad võtmete levitamise ja võtmete haldamise probleemid?
Siin ei ole ühtset vastust. Asümmeetriline krüptograafia on tööriist ja selle kasutamiseks ei ole ainult üks viis. Kuid võtame meie varasema näite Jim's Sporting Goods'ist, et näidata, kuidas probleeme tavaliselt selles näites lahendatakse.
Alguses pöörduks Jim's Sporting Goods tõenäoliselt **sertifitseerimisasutuse** poole, organisatsiooni poole, mis toetab avaliku võtme levitamist. Sertifitseerimisasutus registreeriks mõned andmed Jim's Sporting Goods kohta ja annaks sellele avaliku võtme. Seejärel saadaks ta Jim's Sporting Goods'ile sertifikaadi, mida tuntakse **TLS/SSL sertifikaadina**, milles Jim's Sporting Goods'i avalik võti on digitaalselt allkirjastatud kasutades sertifitseerimisasutuse enda avalikku võtit. Sel viisil kinnitab sertifitseerimisasutus, et kindel avalik võti kuulub tõepoolest Jim's Sporting Goods'ile.

Selle protsessi mõistmise võti TLS/SSL sertifikaatidega on see, et kuigi te tavaliselt ei oma Jim's Sporting Goods'i avalikku võtit kusagil oma arvutis salvestatuna, on tunnustatud sertifitseerimisasutuste avalikud võtmed tõepoolest salvestatud teie brauserisse või operatsioonisüsteemi. Need on salvestatud nn **juursertifikaatides**.

Seega, kui Jim's Sporting Goods annab teile oma TLS/SSL sertifikaadi, saate kontrollida sertifitseerimisasutuse digitaalset allkirja brauseris või operatsioonisüsteemis oleva juursertifikaadi kaudu. Kui allkiri on kehtiv, võite olla suhteliselt kindel, et sertifikaadil olev avalik võti kuulub tõepoolest Jim's Sporting Goods'ile. Selle põhjal on lihtne seadistada protokoll turvaliseks suhtluseks Jim's Sporting Goods'iga.

Võtmete levitamine on nüüd Jim's Sporting Goods'i jaoks muutunud oluliselt lihtsamaks. Pole raske mõista, et võtmete haldamine on samuti muutunud palju lihtsamaks. Selle asemel, et pidada salvestama tuhandeid võtmeid, peab Jim's Sporting Goods lihtsalt salvestama privaatvõtme, mis võimaldab tal teha allkirju avalikule võtmele oma SSL sertifikaadil. Iga kord, kui klient tuleb Jim's Sporting Goods'i saidile, saavad nad selle avaliku võtme põhjal luua turvalise suhtlusseansi. Kliendid ei pea samuti salvestama mingit teavet (peale tunnustatud sertifitseerimisasutuste avalike võtmete oma operatsioonisüsteemis ja brauseris).

**Märkused:**

[5] Iga skeem, mis üritab saavutada vaidlustamatust, teine teema, mida arutasime 1. peatükis, peab oma aluses hõlmama digitaalseid allkirju.

## Hash funktsioonid
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hash funktsioonid on krüptograafias kõikjal levinud. Need ei ole ei sümmeetrilised ega asümmeetrilised skeemid, vaid kuuluvad omaette krüptograafilisse kategooriasse.

Me juba kohtusime hash funktsioonidega 4. peatükis, kui lõime hash-põhiseid autentimissõnumeid. Need on samuti olulised digitaalsete allkirjade kontekstis, kuigi veidi erineval põhjusel: Digitaalsed allkirjad tehakse tavaliselt mõne (krüpteeritud) sõnumi hash-väärtuse, mitte tegeliku (krüpteeritud) sõnumi peale. Selles jaotises pakun ma hash funktsioonidele põhjalikumat tutvustust.

Alustame hash funktsiooni defineerimisest. **Hash funktsioon** on iga tõhusalt arvutatav funktsioon, mis võtab sisendeid suvalises suuruses ja annab fikseeritud pikkusega väljundeid.

**Krüptograafiline hash funktsioon** on lihtsalt hash funktsioon, mis on kasulik krüptograafia rakendustes. Krüptograafilise hash funktsiooni väljundit nimetatakse tavaliselt **hashiks**, **hash-väärtuseks** või **sõnumi kokkuvõtteks**.

Krüptograafia kontekstis viitab "hash funktsioon" tavaliselt krüptograafilisele hash funktsioonile. Ma võtan selle praktika edaspidi kasutusele.
Üks populaarne räsifunktsioon on **SHA-256** (turvaline räsialgoritm 256). Sõltumata sisendi suurusest (nt 15 bitti, 100 bitti või 10 000 bitti), annab see funktsioon 256-bitise räsi väärtuse. Allpool näete mõningaid SHA-256 funktsiooni näidisväljundeid.
“Hello”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

“Krüptograafia on lõbus”: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Kõik väljundid on täpselt 256 bitti, esitatud kuueteistkümnendsüsteemis (iga kuueteistkümnendsüsteemi number saab esitada nelja binaarnumbri abil). Seega, isegi kui sisestasite SHA-256 funktsiooni Tolkieni raamatu *Sõrmuste Isand*, oleks väljund ikkagi 256 bitti.

Räsifunktsioone nagu SHA-256 kasutatakse krüptograafias mitmel eesmärgil. Milliseid omadusi räsifunktsioonilt nõutakse, sõltub konkreetse rakenduse kontekstist. Krüptograafias räsifunktsioonidelt üldiselt soovitud kaks peamist omadust on: [6]

1.	Kokkupõrkekindlus
2.	Peitmine

Räsifunktsiooni $H$ peetakse **kokkupõrkekindlaks**, kui on ebatõenäoline leida kahte väärtust, $x$ ja $y$, nii, et $x \neq y$, kuid $H(x) = H(y)$.

Kokkupõrkekindlad räsifunktsioonid on olulised näiteks tarkvara verifitseerimisel. Kujutage ette, et soovite alla laadida Bitcoin Core 0.21.0 Windowsi väljalaske (serverirakendus Bitcoin võrguliikluse töötlemiseks). Peamised sammud, mida peate tarkvara legitiimsuse kontrollimiseks tegema, on järgmised:

1.	Esiteks peate alla laadima ja importima ühe või mitme Bitcoin Core'i kaastöötaja avalikud võtmed tarkvarasse, mis suudab digitaalallkirju kontrollida (nt Kleopetra). Neid avalikke võtmeid saate leida [siit](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). On soovitatav kontrollida Bitcoin Core'i tarkvara mitme kaastöötaja avalike võtmetega.
2.	Järgmisena peate kontrollima imporditud avalikke võtmeid. Vähemalt üks samm, mida peaksite tegema, on kontrollida, kas leitud avalikud võtmed on samad, mis on avaldatud erinevates muudes kohtades. Võite näiteks konsulteerida inimeste isiklike veebilehtede, Twitteri lehtede või Githubi lehtedega, kelle avalikke võtmeid olete importinud. Tavaliselt tehakse avalike võtmete võrdlus, võrreldes avaliku võtme lühikest räsi, mida tuntakse kui sõrmejälge.
3.	Järgmisena peate alla laadima Bitcoin Core'i täitmisfaili nende [veebisaidilt](www.bitcoincore.org). Seal on saadaval paketid Linuxi, Windowsi ja MAC operatsioonisüsteemidele.
4.	Järgmisena peate leidma kaks väljalaskefaili. Esimene neist sisaldab allalaaditud täitmisfaili ametlikku SHA-256 räsi koos kõigi teiste välja lastud pakettide räsidega. Teine väljalaskefail sisaldab erinevate kaastöötajate allkirju väljalaskefaili üle, mis sisaldab pakettide räsisid. Mõlemad väljalaskefailid peaksid asuma Bitcoin Core'i veebisaidil.
5. Järgmisena peaksite arvutama allalaaditud käivitatava faili SHA-256 räsi Bitcoin Core'i veebisaidilt oma arvutis. Seejärel võrrelge seda tulemust ametliku paketi räsi väärtusega. Need peaksid olema samad.  
6. Lõpuks peaksite kontrollima, et üks või mitu allkirja vabastusfailil koos ametlike paketi räsidega vastab tõepoolest ühele või mitmele avalikule võtmele, mille te importisite (Bitcoin Core'i väljalasked ei ole alati kõigi poolt allkirjastatud). Seda saate teha rakendusega nagu Kleopetra.

Selle tarkvara kontrollimise protsessi kaks peamist eelist on järgmised. Esiteks tagab see, et Bitcoin Core'i veebisaidilt allalaadimisel ei esinenud edastusvigu. Teiseks tagab see, et ükski ründaja ei oleks suutnud teid panna allalaadima muudetud, pahatahtlikku koodi, kas häkkides Bitcoin Core'i veebisaiti või liiklust pealt kuulates.

Kuidas täpselt kaitseb ülaltoodud tarkvara kontrollimise protsess neid probleeme vastu?

Kui te hoolikalt kontrollisite importitud avalikke võtmeid, siis võite olla üsna kindel, et need võtmed on tõepoolest nende omad ja neid ei ole kompromiteeritud. Kuna digitaalsetel allkirjadel on eksistentsiaalne võltsimiskindlus, teate, et ainult need panustajad oleksid saanud teha digitaalse allkirja ametlike paketi räside üle vabastusfailis.

Eeldades, et vabastusfailil olevad allkirjad kontrolluvad. Nüüd saate võrrelda lokaalselt arvutatud räsi väärtust Windowsi käivitatava faili jaoks, mille olete allalaadinud, sellega, mis on korrektselt allkirjastatud vabastusfailis. Kuna teate, et SHA-256 räsi funktsioon on kokkupõrkekindel, tähendab vastavus, et teie käivitatav fail on täpselt sama mis ametlik käivitatav fail.

Pöördugem nüüd räsi funktsioonide teise levinud omaduse juurde: **varjamine**. Iga räsi funktsioon \(H\) peetakse varjamise omadusega, kui suvaliselt valitud \(x\) jaoks väga suurest vahemikust on võimatu leida \(x\), kui on antud ainult \(H(x)\).

Allpool näete sõnumi SHA-256 väljundit, mille ma kirjutasin. Piisava juhuslikkuse tagamiseks sisaldas sõnum lõpus juhuslikult genereeritud tähemärkide jada. Kuna SHA-256-l on varjamise omadus, ei suudaks keegi seda sõnumit dešifreerida.

- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Kuid ma ei jäta teid põnevuses kuni SHA-256 nõrgeneb. Algne sõnum, mille kirjutasin, oli järgmine:

* "See on väga juhuslik sõnum, või noh üsna juhuslik. See algusosa ei ole, kuid ma lõpetan mõningate suhteliselt juhuslike tähemärkidega, et tagada väga ettearvamatu sõnum. XLWz4dVG3BxUWm7zQ9qS".

Üks levinud viis, kuidas varjamise omadusega räsi funktsioone kasutatakse, on paroolihalduses (kokkupõrkekindlus on ka selle rakenduse jaoks oluline). Iga korralik veebipõhine kontoteenus nagu Facebook või Google ei salvesta teie paroole otse, et hallata juurdepääsu teie kontole. Selle asemel salvestavad nad ainult parooli räsi. Iga kord, kui sisestate brauseris oma parooli, arvutatakse esmalt räsi. Ainult see räsi saadetakse teenusepakkuja serverisse ja võrreldakse tagaotsas olevas andmebaasis salvestatud räsi väärtusega. Varjamise omadus aitab tagada, et ründajad ei saa seda räsi väärtusest taastada.
Paroolide haldamine räsi abil toimib muidugi ainult siis, kui kasutajad valivad tõepoolest keerulisi paroole. Peitmise omadus eeldab, et x on valitud juhuslikult väga suurest vahemikust. Paroolide valimine nagu "1234", "minuparool" või teie sünnikuupäev ei paku mingit tegelikku turvalisust. Pikad nimekirjad levinud paroolidest ja nende räsidest on olemas, mida ründajad saavad ära kasutada, kui nad kunagi saavad kätte teie parooli räsi. Selliseid rünnakuid tuntakse **sõnaraamatu rünnakutena**. Kui ründajad teavad mõningaid teie isiklikke detaile, võivad nad samuti proovida mõningaid informeeritud oletusi. Seetõttu on teil alati vaja pikki, turvalisi paroole (eelistatavalt pikki, juhuslikke jadasid paroolihaldurist).

Mõnikord võib rakendus vajada räsi funktsiooni, mis omab nii kokkupõrkekindlust kui ka peitmist. Kuid kindlasti mitte alati. Tarkvara kontrollimise protsess, millest me rääkisime, näiteks nõuab ainult, et räsi funktsioon näitaks kokkupõrkekindlust, peitmine ei ole oluline.

Kuigi kokkupõrkekindlus ja peitmine on peamised omadused, mida krüptograafias räsi funktsioonidelt otsitakse, võivad teatud rakendustes olla soovitavad ka muud tüüpi omadused.

**Märkused:**

[6] Termin "peitmine" ei ole üldkeel, vaid on võetud spetsiifiliselt Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller ja Steven Goldfeder raamatust *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), 1. peatükk.

# RSA krüptosüsteem
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Faktoriseerimise probleem
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Kuigi sümmeetriline krüptograafia on tavaliselt enamiku inimeste jaoks üsna intuitiivne, ei ole see tavaliselt nii asümmeetrilise krüptograafiaga. Kuigi te tõenäoliselt olete mugav kõrgetasemelise kirjeldusega, mida eelmistes jaotistes pakuti, mõtlete tõenäoliselt, mis täpselt on ühesuunalised funktsioonid ja kuidas neid kasutatakse asümmeetriliste skeemide konstrueerimiseks.

Sel peatükis ma eemaldan mõningad müsteeriumid, mis ümbritsevad asümmeetrilist krüptograafiat, vaadeldes sügavamalt konkreetset näidet, nimelt RSA krüptosüsteemi. Esimeses jaotises tutvustan ma faktoriseerimise probleemi, millel RSA probleem põhineb. Seejärel käsitleme mitmeid olulisi tulemusi arvuteooriast. Viimases jaotises paneme selle teabe kokku, et selgitada RSA probleemi ja kuidas seda saab kasutada asümmeetriliste krüptograafiliste skeemide loomiseks.

Selle arutelu süvendamine ei ole lihtne ülesanne. See nõuab üsna mitme arvuteoreetilise teoreemi ja ettepaneku tutvustamist. Kuid ärge laske matemaatikal end heidutada. Selle arutelu läbitöötamine parandab oluliselt teie mõistmist, mis on asümmeetrilise krüptograafia aluseks, ja on väärt investeering.

Vaadelgem nüüd esmalt faktoriseerimise probleemi.

___

Kui te korrutate kaks arvu, ütleme $a$ ja $b$, nimetame arve $a$ ja $b$ **teguriteks** ja tulemust **korrutiseks**. Katse kirjutada number $N$ kahe või enama teguri korrutisena nimetatakse **faktoriseerimiseks** või **faktoriseerimiseks**. [1] Iga probleemi, mis seda nõuab, võite nimetada **faktoriseerimise probleemiks**.

Umbes 2500 aastat tagasi avastas Kreeka matemaatik Euclid Aleksandriast võtmeteoreemi täisarvude faktoriseerimise kohta. Seda nimetatakse tavaliselt **ainulaadse faktoriseerimise teoreemiks** ja see väidab järgmist:

**Teoreem 1**. Iga täisarv $N$, mis on suurem kui 1, on kas algarv või seda saab väljendada algarvude korrutisena.
Kogu selle avalduse hilisem osa tähendab lihtsalt seda, et võite võtta ükskõik millise algarvulise täisarvu $N$, mis on suurem kui 1, ja kirjutada selle välja algarvude korrutisena. Allpool on mitu näidet algarvuliste täisarvude kohta, mis on kirjutatud algarvude tegurite korrutisena.
* $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
* $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
* $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Kõigi kolme ülaltoodud täisarvu puhul on nende algarvude tegurite arvutamine suhteliselt lihtne, isegi kui teile on antud ainult $N$. Alustate väikseima algarvuga, nimelt 2-ga, ja vaatate, mitu korda täisarv $N$ on jagatav sellega. Seejärel liigute edasi, testides $N$ jagatavust 3, 5, 7 jne. Jätkate seda protsessi, kuni teie täisarv $N$ on kirjutatud ainult algarvude korrutisena.

Võtame näiteks täisarvu 84. Allpool näete protsessi selle algarvude tegurite määramiseks. Igal sammul võtame välja väikseima järelejäänud algarvu teguri (vasakul) ja määrame ülejäänud teguritava osa. Jätkame, kuni ülejäänud osa on samuti algarv. Igal sammul kuvatakse 84 praegune tegurdamine paremal ääres.

* Algarvu tegur = 2: ülejäänud osa = 42 	($84 = 2 \cdot 42$)
* Algarvu tegur = 2: ülejäänud osa = 21 	($84 = 2 \cdot 2 \cdot 21$)
* Algarvu tegur = 3: ülejäänud osa = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
* Kuna 7 on algarv, on tulemuseks $2 \cdot 2 \cdot 3 \cdot 7$, ehk $2^2 \cdot 3 \cdot 7$.

Eeldame nüüd, et $N$ on väga suur. Kui keeruline oleks vähendada $N$ selle algarvude teguriteks?

See sõltub tõesti $N$-st. Eeldame näiteks, et $N$ on 50,450,400. Kuigi see number tundub hirmutav, ei ole arvutused nii keerulised ja neid saab hõlpsasti teha käsitsi. Nagu eespool, alustate lihtsalt 2-ga ja töötate edasi. Allpool näete selle protsessi tulemust sarnasel viisil nagu eespool.

* 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)  
* 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)  
* 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)  
* 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)  
* 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
* 3: 525,525 ($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
* 3: 175,175 ($50,450,400 = 2^5 \cdot 3^2 \cdot 175,175$)
* 5: 35,035 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35,035$)
* 5: 7,007 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7,007$)
* 7: 1,001 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1,001$)
* 7: 143 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
* 11: 13 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
* Kuna 13 on algarv, on tulemus $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Selle probleemi käsitsi lahendamine võtab aega. Arvuti suudab muidugi seda teha murdosa sekundiga. Tegelikult suudab arvuti tihti isegi väga suuri täisarve murdosa sekundiga teguriteks lahutada.

Siiski on teatud erandid. Oletame, et valime esmalt juhuslikult kaks väga suurt algarvu. Tavaliselt tähistatakse neid $p$ ja $q$ ning ma järgin siin seda konventsiooni.

Konkreetsuse huvides öelgem, et $p$ ja $q$ on mõlemad 1024-bitised algarvud ja et nende esitamiseks on tõepoolest vaja vähemalt 1024 bitti (nii et esimene bitt peab olema 1). Seega näiteks 37 ei saaks olla üks algarvudest. Sa võid kindlasti esitada 37 1024 bitiga. Kuid ilmselgelt *ei vaja* sa nii palju bitte selle esitamiseks. Sa võid esitada 37 mis tahes jadaga, mis on 6 bitti või rohkem. (6 bitis oleks 37 esitatud kui $100101$).

On oluline mõista, kui suured on $p$ ja $q$, kui need on valitud ülaltoodud tingimustel. Näitena olen valinud juhusliku algarvu, mis vajab esitamiseks vähemalt 1024 bitti allpool.
* 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589

Eeldame nüüd, et pärast juhuslike algarvude $p$ ja $q$ valimist korrutame need, et saada täisarv $N$. See viimane täisarv on seega 2048-bitine number, mis nõuab oma esitamiseks vähemalt 2048 bitti. See on palju, palju suurem kui kas $p$ või $q$.

Eeldame, et annate arvutile ainult $N$ ja palute tal leida $N$ kaks 1024-bitist algarvulist tegurit. Tõenäosus, et arvuti avastab $p$ ja $q$, on äärmiselt väike. Võib öelda, et see on praktilistel eesmärkidel võimatu. See kehtib isegi siis, kui kasutaksite superarvutit või isegi superarvutite võrku.

Alustuseks eeldame, et arvuti üritab probleemi lahendada, tsükliliselt läbides 1024-bitiseid numbreid, testides igal juhul, kas need on algarvud ja kas need on $N$ tegurid. Testitavate algarvude hulk on siis ligikaudu $1.265 \cdot 10^{305}$. [2]

Isegi kui võtate kõik planeedi arvutid ja panete nad sel viisil 1024-bitiseid algarve otsima ja testima, nõuaks miljardist ühe võimalusega edukalt $N$ algarvulise teguri leidmine arvutusperioodi, mis on palju pikem kui Universumi vanus.

Nüüd praktikas suudab arvuti paremini hakkama saada kui just kirjeldatud robustne protseduur. On olemas mitmeid algoritme, mida arvuti saab rakendada, et jõuda tegurite lahutamiseni kiiremini. Siiski on oluline, et isegi nende tõhusamate algoritmide kasutamisel on arvuti ülesanne endiselt arvutuslikult teostamatu. [3]

Oluline on, et tegurite lahutamise raskus just kirjeldatud tingimustel põhineb eeldusel, et ei ole olemas arvutuslikult tõhusaid algoritme algarvuliste tegurite arvutamiseks. Me ei saa tegelikult tõestada, et tõhus algoritm ei eksisteeri. Siiski on see eeldus väga usutav: hoolimata sadu aastaid kestnud ulatuslikest jõupingutustest, pole me veel leidnud sellist arvutuslikult tõhusat algoritmi.

Seega võib tegurite lahutamise probleemi teatud asjaoludel usutavalt eeldada olevat raske probleem. Eriti siis, kui $p$ ja $q$ on väga suured algarvud, nende korrutise $N$ arvutamine ei ole keeruline; kuid ainult $N$ antud tegurite lahutamine on praktiliselt võimatu.


**Märkused:**

[1] Tegurite lahutamine võib olla oluline ka teiste matemaatiliste objektidega töötamisel kui ainult numbrid. Näiteks võib olla kasulik faktoriseerida polünoomilisi avaldisi nagu $x^2 - 2x + 1$. Meie arutelus keskendume ainult numbrite, eriti täisarvude faktoriseerimisele.
[2] Vastavalt **algarvude teoreemile** on algarvude arv, mis on väiksem või võrdne $N$-ga, ligikaudu $N/\ln(N)$. See tähendab, et saate ligikaudselt arvutada 1024-bitiste algarvude arvu järgmiselt:
$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...mis on ligikaudu $1.265 \times 10^{305}$.

[3] Sama kehtib ka diskreetsete logaritmide probleemide kohta. Seetõttu töötavad asümmeetrilised konstruktsioonid palju suuremate võtmetega kui sümmeetrilised krüptograafilised konstruktsioonid.

## Arvuteoreetilised tulemused
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Kahjuks ei saa faktoriseerimise probleemi otse kasutada asümmeetrilistes krüptograafilistes skeemides. Siiski saame kasutada keerukamat, kuid sellega seotud probleemi: RSA probleemi.

RSA probleemi mõistmiseks peame mõistma mitmeid teoreeme ja propositsioone arvuteooriast. Need on esitatud selles jaotises kolmes alajaotises: (1) N järjekord, (2) pööratavus modulo N ja (3) Euleri teoreem.

Mõned materjalid nendes kolmes alajaotises on juba tutvustatud *3. peatükis*. Kuid ma esitan siin need materjalid mugavuse huvides uuesti.

### N järjekord

Täisarv $a$ on **teine-teisele võõras** või **suhteline algarv** täisarvuga $N$, kui nende suurim ühistegur on 1. Kuigi 1 ei ole tavapäraselt algarv, on see iga täisarvu teine-teisele võõras (nagu ka $-1$).

Näiteks, kui $a = 18$ ja $N = 37$, siis need on selgelt teine-teisele võõrad. Suurim täisarv, mis jagab nii 18 kui ka 37, on 1. Vastupidisel juhul, kui $a = 42$ ja $N = 16$, siis need ei ole selgelt teine-teisele võõrad. Mõlemad numbrid on jagatavad 2-ga, mis on suurem kui 1.

Nüüd saame defineerida $N$ järjekorra järgmiselt. Eeldame, et $N$ on täisarv, mis on suurem kui 1. **N järjekord** on siis kõikide $N$-ga teine-teisele võõraste arvude arv, nii et iga teine-teisele võõra $a$ puhul kehtib järgmine tingimus: $1 \leq a < N$.

Näiteks, kui $N = 12$, siis ainult 1, 5, 7 ja 11 on teine-teisele võõrad, mis vastavad ülaltoodud nõudele. Seega on 12 järjekord võrdne 4-ga.

Eeldame, et $N$ on algarv. Siis iga täisarv, mis on väiksem kui $N$, kuid suurem või võrdne 1-ga, on sellega teine-teisele võõras. See hõlmab kõiki elemente järgmises hulgas: $\{1,2,3,….,N - 1\}$. Seega, kui $N$ on algarv, on $N$ järjekord $N - 1$. See on väljendatud propositsioonis 1, kus $\phi(N)$ tähistab $N$ järjekorda.

**Propositsioon 1**. $\phi(N) = N - 1$, kui $N$ on algarv
Eeldame, et $N$ ei ole algarv. Sel juhul saate arvutada selle järku kasutades **Euleri fi-funktsiooni**. Kuigi väikese täisarvu järje arvutamine on suhteliselt lihtne, muutub Euleri fi-funktsioon eriti oluliseks suurte täisarvude puhul. Euleri fi-funktsiooni ettepanek on allpool esitatud.

**Teoreem 2**. Olgu $N$ võrdne $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, kus hulk $\{p_i\}$ koosneb kõikidest $N$ erinevatest algarvulistest teguritest ja iga $e_i$ näitab, mitu korda algarvuline tegur $p_i$ esineb $N$ jaoks. Siis

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Teoreem 2** näitab, et kui olete mittelgarvu $N$ jaotanud selle erinevateks algarvulisteks teguriteks, on $N$ järje arvutamine lihtne.

Näiteks, eeldame, et $N = 270$. See ei ole selgelt algarv. $N$ jaotamine selle algarvulisteks teguriteks annab avaldise: $2 \cdot 3^3 \cdot 5$. Euleri fi-funktsiooni kohaselt on $N$ järk siis järgmine:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Eeldame järgmisena, et $N$ on kahe algarvu, $p$ ja $q$, korrutis. **Teoreem 2** ülal, siis, väidab, et $N$ järk on järgmine:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

See on võtmetulemus eriti RSA probleemi jaoks ja on esitatud **Propositsioonis 2** allpool.

**Propositsioon 2**. Kui $N$ on kahe algarvu, $p$ ja $q$, korrutis, siis $N$ järk on korrutis $(p - 1) \cdot (q - 1)$.

Illustratsiooniks, eeldame, et $N = 119$. See täisarv on jaotatav kaheks algarvuks, nimelt 7 ja 17. Seega, Euleri fi-funktsiooni kohaselt on 119 järk järgmine:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Teisisõnu, täisarvul 119 on vahemikus 1 kuni 119 kokku 96 kaasalgarvu. Tegelikult hõlmab see hulk kõiki täisarve 1 kuni 119, mis ei ole kordne ei 7 ega 17-ga.
Edaspidi tähistagem koprimeide hulka, mis määrab $N$ järjekorra, kui $C_N$. Meie näites, kus $N = 119$, on hulk $C_{119}$ liiga suur, et seda täielikult loetleda. Kuid mõned elemendid on järgmised:
$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Pööratavus modulo N

Võime öelda, et täisarv $a$ on **pööratav modulo N**, kui eksisteerib vähemalt üks täisarv $b$ nii, et $a \cdot b \mod N = 1 \mod N$. Iga selline täisarv $b$ nimetatakse $a$ **pöördarvuks** (või **korrutise pöördarvuks**) modulo $N$ vähendamisel.

Oletame näiteks, et $a = 5$ ja $N = 11$. On palju täisarve, millega saab korrutada 5, nii et $5 \cdot b \mod 11 = 1 \mod 11$. Kaaluge näiteks täisarve 20 ja 31. On lihtne näha, et mõlemad need täisarvud on 5 pöördarvud modulo 11 vähendamisel.

* $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
* $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Kuigi 5-l on palju pöördarve modulo 11 vähendamisel, võib näidata, et eksisteerib ainult üks positiivne 5 pöördarv, mis on väiksem kui 11. Tegelikult ei ole see ainulaadne meie konkreetsele näitele, vaid üldine tulemus.

**Ettepanek 3**. Kui täisarv $a$ on pööratav modulo $N$, peab olema nii, et täpselt üks positiivne $a$ pöördarv on väiksem kui $N$. (Seega, see ainulaadne $a$ pöördarv peab tulema hulgast $\{1, \dots, N - 1\}$).

Tähistagem **Ettepaneku 3** kohaselt $a$ ainulaadset pöördarvu kui $a^{-1}$. Juhtumil, kui $a = 5$ ja $N = 11$, võite näha, et $a^{-1} = 9$, arvestades, et $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Pange tähele, et võite saada väärtuse 9 $a^{-1}$ jaoks meie näites ka lihtsalt vähendades mis tahes muud $a$ pöördarvu modulo 11. Näiteks $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Seega, kui täisarv $a > N$ on pööratav modulo $N$, siis peab $a \mod N$ samuti olema pööratav modulo $N$.

Ei ole tingimata nii, et $a$ pöördarv eksisteerib modulo $N$ vähendamisel. Oletame näiteks, et $a = 2$ ja $N = 8$. Pole ühtegi $b$ ega konkreetset $a^{-1}$, nii et $2 \cdot b \mod 8 = 1 \mod 8$. See on seetõttu, et mis tahes $b$ väärtus alati toodab 2 kordset, nii et 8-ga jagamine ei saa kunagi anda jääki, mis võrdub 1-ga.
Kuidas me täpselt teame, kas mingil täisarvul $a$ on olemas pöördarv antud $N$ jaoks? Nagu te võisite eespool toodud näites märgata, on 2 ja 8 suurim ühistegur suurem kui 1, nimelt 2. Ja see on tegelikult illustratiivne järgnevale üldisele tulemusele:
**Propositsioon 4**. Täisarvul $a$ on olemas pöördarv modulo $N$ järgi, ja täpsemalt ainulaadne positiivne pöördarv, mis on väiksem kui $N$, kui ja ainult siis, kui $a$ ja $N$ suurim ühistegur on 1 (st, kui nad on teineteisele võõrad).

Juhtumi puhul, kui $a = 5$ ja $N = 11$, jõudsime järeldusele, et $a^{-1} = 9$, arvestades, et $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. On oluline märkida, et vastupidine on samuti tõsi. See tähendab, kui $a = 9$ ja $N = 11$, siis kehtib, et $a^{-1} = 5$.

### Euleri teoreem

Enne RSA probleemi juurde liikumist peame mõistma veel üht olulist teoreemi, nimelt **Euleri teoreemi**. See väidab järgmist:

**Teoreem 3**. Eeldame, et kaks täisarvu $a$ ja $N$ on teineteisele võõrad. Siis $a^{\phi(N)} \mod N = 1 \mod N$.

See on märkimisväärne tulemus, kuid esialgu veidi segadusttekitav. Vaatame näidet, et seda mõista.

Eeldame, et $a = 5$ ja $N = 7$. Need on tõepoolest teineteisele võõrad, nagu Euleri teoreem nõuab. Me teame, et 7 järjekord on 6, arvestades, et 7 on algarv (vt **Propositsioon 1**).

Mida Euleri teoreem nüüd väidab, on see, et $5^6 \mod 7$ peab olema võrdne $1 \mod 7$-ga. Allpool on arvutused, mis näitavad, et see on tõepoolest tõsi.

* $5^6 \mod 7 = 15,625 \mod 7 = 1 \mod N$

Täisarv 7 jagub arvuga 15,624 kokku 2,233 korda. Seega, jagades 16,625 arvuga 7, on jääk 1.

Järgnevalt, kasutades Euleri Fi funktsiooni, **Teoreem 2**, võite tuletada allpool toodud **Propositsiooni 5**.

**Propositsioon 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ mis tahes positiivsete täisarvude $a$ ja $b$ jaoks.

Me ei näita, miks see nii on. Kuid märkige lihtsalt, et olete juba näinud selle propositsiooni tõestust asjaoluga, et $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$, kui $p$ ja $q$ on algarvud, nagu on öeldud **Propositsioonis 2**.

Euleri teoreem koos **Propositsiooniga 5** omab olulisi tagajärgi. Vaadake, mis juhtub näiteks allpool toodud avaldistes, kus $a$ ja $N$ on teineteisele võõrad.

* $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
* $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$* $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Seega Euleri teoreemi ja **Propositsioon 5** kombinatsioon võimaldab meil lihtsalt arvutada mitmeid avaldisi. Üldiselt võime kokkuvõtlikult öelda **Propositsioon 6** järgi.

**Propositsioon 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Nüüd peame kõik kokku panema keerulises viimases sammus.

Nii nagu $N$-il on järk $\phi(N)$, mis sisaldab hulga $C_N$ elemente, teame, et täisarvul $\phi(N)$ peab omakorda samuti olema järk ja koprime hulk. Seadkem $\phi(N) = R$. Siis teame, et on olemas ka väärtus $\phi(R)$ ja koprime hulk $C_R$.

Eeldagem, et valime nüüd täisarvu $e$ hulgast $C_R$. **Propositsioon 3** järgi teame, et sellel täisarvul $e$ on ainult üks unikaalne positiivne pöördväärtus, mis on väiksem kui $R$. See tähendab, et $e$-l on üks unikaalne pöördväärtus hulgast $C_R$. Nimetagem seda pöördväärtust $d$-ks. Pöördväärtuse definitsiooni järgi tähendab see, et $e \cdot d = 1 \mod R$.

Seda tulemust saame kasutada meie algse täisarvu $N$ kohta tehtava väite tegemiseks. See on kokkuvõtlikult esitatud **Propositsioon 7**.

**Propositsioon 7**. Eeldagem, et $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Siis mis tahes elemendi $a$ puhul hulgast $C_N$ peab kehtima, et $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Nüüd on meil kõik arvuteoreetilised tulemused, mis on vajalikud RSA probleemi selgeks sõnastamiseks.

## RSA krüptosüsteem
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Oleme nüüd valmis sõnastama RSA probleemi. Eeldagem, et loote muutujate hulga, mis koosneb $p$, $q$, $N$, $\phi(N)$, $e$, $d$ ja $y$. Nimetagem seda hulka $\Pi$. See luuakse järgmiselt:

1. Genereerige kaks juhuslikku võrdse suurusega algarvu $p$ ja $q$ ning arvutage nende korrutis $N$.
2. Arvutage $N$ järk, $\phi(N)$, järgneva korrutise abil: $(p - 1) \cdot (q - 1)$.
3. Valige $e > 2$ nii, et see oleks väiksem ja koprime $\phi(N)$-ga.
4. Arvutage $d$, seades $e \cdot d \mod \phi(N) = 1$.
5. Valige juhuslik väärtus $y$, mis on väiksem ja koprime $N$-ga.
RSA probleem seisneb sellise $x$ leidmises, et $x^e = y$, olles antud ainult osaline teave $\Pi$ kohta, nimelt muutujad $N$, $e$ ja $y$. Kui $p$ ja $q$ on väga suured, tavaliselt soovitatakse, et nende suurus oleks 1024 bitti, peetakse RSA probleemi raskeks. Nüüd saate aru, miks see nii on, arvestades eelnevat arutelu.

Lihtne viis $x$ arvutamiseks, kui $x^e \mod N = y \mod N$, on lihtsalt arvutada $y^d \mod N$. Me teame, et $y^d \mod N = x \mod N$ järgmiste arvutuste põhjal:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Probleem on selles, et me ei tea väärtust $d$, kuna seda ei antud probleemis. Seega ei saa me otse arvutada $y^d \mod N$, et saada $x \mod N$.

Siiski võime olla võimelised kaudselt arvutama $d$ väärtuse $N$ järjekorra, $\phi(N)$, põhjal, kuna teame, et $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Kuid eelduse kohaselt ei antud probleemis ka $\phi(N)$ väärtust.

Lõpuks võiks järjekorda kaudselt arvutada algarvude $p$ ja $q$ abil, nii et lõpuks saaksime arvutada $d$. Kuid eelduse kohaselt ei antud meile ka väärtusi $p$ ja $q$.

Rangelt öeldes, isegi kui faktoriseerimisprobleem RSA probleemi raames on raske, ei saa me tõestada, et RSA probleem on samuti raske. Võib nimelt olla muid viise RSA probleemi lahendamiseks kui faktoriseerimise kaudu. Siiski on üldiselt aktsepteeritud ja eeldatav, et kui faktoriseerimisprobleem RSA probleemi raames on raske, siis on RSA probleem ise samuti raske.

Kui RSA probleem on tõepoolest raske, siis see loob ühesuunalise funktsiooni lõksuga. Siin on funktsioon $f(g) = g^e \mod N$. Teades $f(g)$, võiks igaüks hõlpsalt arvutada väärtuse $y$ konkreetse $g = x$ jaoks. Siiski on praktiliselt võimatu arvutada konkreetset väärtust $x$ ainult väärtust $y$ ja funktsiooni $f(g)$ teades. Erand on siis, kui teile antakse teave $d$, lõks. Sel juhul saate lihtsalt arvutada $y^d$, et saada $x$.

Vaadelgem konkreetset näidet, et illustreerida RSA probleemi. Ma ei saa valida RSA probleemi, mis oleks peetud raskeks ülaltoodud tingimustel, kuna numbrid oleksid kohmakad. Selle asemel on see näide lihtsalt selleks, et illustreerida, kuidas RSA probleem üldiselt toimib.

Alustuseks eeldame, et valite kaks juhuslikku algarvu 13 ja 31. Nii et $p = 13$ ja $q = 31$. Nende kahe algarvu korrutis $N$ võrdub 403-ga. Me saame hõlpsalt arvutada 403 järjekorra. See on võrdne $(13 - 1) \cdot (31 - 1) = 360$.
Järgnevalt, nagu RSA probleemi 3. sammu poolt ette nähtud, peame valima 360 jaoks võõrarvu, mis on suurem kui 2 ja väiksem kui 360. Me ei pea seda väärtust juhuslikult valima. Oletame, et valime 103. See on 360 võõrarv, kuna selle suurim ühistegur 103-ga on 1.
4. samm nõuab nüüd, et arvutaksime väärtuse $d$ nii, et $103 \cdot d \mod 360 = 1$. See ei ole kerge ülesanne käsitsi, kui $N$ väärtus on suur. See nõuab, et kasutaksime protseduuri, mida nimetatakse **laiendatud Eukleidese algoritmiks**.

Kuigi ma ei näita protseduuri siin, annab see väärtuse 7, kui $e = 103$. Võite kontrollida, et väärtuste paar 103 ja 7 tõepoolest vastab üldtingimusele $e \cdot d \mod \phi(n) = 1$ allpool toodud arvutuste kaudu.

* $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Oluliselt, arvestades *Propositsiooni 4*, teame, et ükski teine täisarv vahemikus 1 kuni 360 $d$ jaoks ei anna tulemust, et $103 \cdot d = 1 \mod 360$. Lisaks tähendab propositsioon, et $e$ jaoks erineva väärtuse valimine annab $d$ jaoks erineva unikaalse väärtuse.

RSA probleemi 5. sammus peame valima mõne positiivse täisarvu $y$, mis on 403 väiksem võõrarv. Oletame, et seame $y = 2^{103}$. Kahe astendamine 103-ga annab allpool toodud tulemuse.

* $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$

RSA probleem antud näites on nüüd järgmine: Teile on antud $N = 403$, $e = 103$ ja $y = 349 \mod 403$. Nüüd peate arvutama $x$ nii, et $x^{103} = 349 \mod 403$. See tähendab, et peate leidma algse väärtuse enne astendamist 103-ga oli 2.

Oleks lihtne (vähemalt arvuti jaoks) arvutada $x$, kui teaksime, et $d = 7$. Sel juhul võiksite lihtsalt määrata $x$ alljärgnevalt.

* $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$

Probleem on selles, et teile ei ole antud teavet, et $d = 7$. Loomulikult võiksite arvutada $d$ faktist, et $103 \cdot d = 1 \mod 360$. Probleem on selles, et teile ei ole antud ka teavet, et $N$ järjekord on 360. Lõpuks võiksite arvutada ka 403 järjekorra, arvutades järgmise korrutise: $(p - 1) \cdot (q - 1)$. Kuid teile ei ole öeldud ka seda, et $p = 13$ ja $q = 31$.

Muidugi võiks arvuti siiski suhteliselt kergesti lahendada RSA probleemi selle näite jaoks, kuna kaasatud algarvud ei ole suured. Kuid kui algarvud muutuvad väga suureks, seisab see silmitsi praktiliselt võimatu ülesandega.
Oleme nüüd tutvustanud RSA probleemi, tingimuste kogumit, mille korral probleemi lahendamine on keeruline, ja selle aluseks olevat matemaatikat. Kuidas aitab see kõik kaasa asümmeetrilisele krüptograafiale? Täpsemalt, kuidas saame RSA probleemi keerukuse teatud tingimustel muuta krüpteerimisskeemiks või digitaalseks allkirjastamise skeemiks?
Üks lähenemine on võtta RSA probleem ja luua skeemid otsekohesel viisil. Näiteks, kujutage ette, et genereerite muutujate kogumi $\Pi$, nagu on kirjeldatud RSA probleemis, ja tagate, et $p$ ja $q$ on piisavalt suured. Määrate oma avaliku võtme võrduma $(N, e)$ ja jagate seda teavet maailmaga. Nagu eespool kirjeldatud, hoiate $p$, $q$, $\phi(n)$ ja $d$ väärtused salajas. Tegelikult on $d$ teie privaatvõti.

Igaüks, kes soovib teile sõnumit $m$ saata, mis on elemendiks $C_N$, võib lihtsalt krüpteerida selle järgmiselt: $c = m^e \mod N$. (Siin tekstis $c$ on ekvivalentne väärtusega $y$ RSA probleemis.) Te saate selle sõnumi hõlpsalt dekrüpteerida, lihtsalt arvutades $c^d \mod N$.

Võite proovida luua digitaalse allkirjastamise skeemi samal viisil. Eeldame, et soovite kellelegi sõnumit $m$ saata digitaalse allkirjaga $S$. Saate lihtsalt seada $S = m^d \mod N$ ja saata paari $(m,S)$ saajale. Igaüks saab digitaalset allkirja kontrollida, lihtsalt kontrollides, kas $S^e \mod N = m \mod N$. Ründajal oleks aga tõeliselt keeruline luua kehtiv $S$ sõnumile, arvestades, et neil ei ole $d$.

Kahjuks ei ole RSA probleemi, mis iseenesest on keeruline probleem, muutmine krüptograafiliseks skeemiks nii lihtne. Otsekohese krüpteerimisskeemi puhul saate oma sõnumitena valida ainult $N$-ga koprimeid. See ei jäta meile palju võimalikke sõnumeid, kindlasti mitte piisavalt standardseks suhtluseks. Lisaks tuleb neid sõnumeid valida juhuslikult. See tundub üsna ebapraktiline. Lõpuks, iga kord valitud sõnum annab täpselt sama šifreeritud teksti. See on igas krüpteerimisskeemis äärmiselt ebasoovitav ja ei vasta ühelegi rangele kaasaegsele turvalisuse standardile krüpteerimises.

Probleemid muutuvad veelgi hullemaks meie otsekohese digitaalse allkirjastamise skeemi puhul. Nagu praegu seisab, võib iga ründaja hõlpsalt võltsida digitaalseid allkirju, lihtsalt esmalt valides $N$-ga koprime allkirjaks ja seejärel arvutades vastava algse sõnumi. See selgelt rikub eksistentsiaalse võltsimatu nõuet.

Siiski, lisades natuke nutikat keerukust, saab RSA probleemi kasutada turvalise avaliku võtme krüpteerimisskeemi ning turvalise digitaalse allkirjastamise skeemi loomiseks. Me ei hakka siin selliste konstruktsioonide üksikasju käsitlema. [4] Oluline on siiski märkida, et see lisakomplekssus ei muuda fundamentaalset aluseks olevat RSA probleemi, millel need skeemid põhinevad.

**Märkused:**

[4] Vaata näiteks Jonathan Katz ja Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), lk. 410–32 RSA krüpteerimise ja lk. 444–41 RSA digitaalsete allkirjade kohta.

## Kursuse hindamine
<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>
<isCourseReview>true</isCourseReview>