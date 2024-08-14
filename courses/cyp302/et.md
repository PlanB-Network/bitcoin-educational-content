---
name: Sissejuhatus formaalsesse krüptograafiasse
goal: Süvitsi sissejuhatus krüptograafia teadusesse ja praktikasse.
objectives:
  - Uurida Beale'i šifreid ja kaasaegseid krüptograafilisi meetodeid, et mõista krüptograafia põhilisi ja ajaloolisi kontseptsioone.
  - Süveneda arvuteooriasse, gruppidesse ja väljadesse, et omandada krüptograafia aluseks olevad võtmematemaatilised kontseptsioonid.
  - Õppida RC4 voogšifrit ja AES-i 128-bitise võtmega, et tutvuda sümmeetriliste krüptograafiliste algoritmidega.
  - Uurida RSA krüptosüsteemi, võtmejaotust ja räsifunktsioone, et avastada asümmeetrilist krüptograafiat.

---
# Süvitsi sukeldumine krüptograafiasse

On raske leida materjale, mis pakuksid head keskteed krüptograafia õpetamisel.

Ühelt poolt on pikad, formaalsed käsitlused, mis on tõeliselt ligipääsetavad ainult neile, kellel on tugev taust matemaatikas, loogikas või mõnes muus formaalses distsipliinis. Teiselt poolt on väga üldised sissejuhatused, mis tõesti varjavad liiga palju detaile neile, kes on vähemalt natuke uudishimulikud.

See krüptograafia sissejuhatus püüab tabada keskteed. Kuigi see peaks olema suhteliselt keeruline ja detailne kõigile, kes on krüptograafiaga uued, ei ole see tüüpilise alustava käsitluse küülikuurg.

+++

# Sissejuhatus krüptograafiasse
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Lühikirjeldus
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

See raamat pakub süvitsi sissejuhatust krüptograafia teadusesse ja praktikasse. Võimalusel keskendutakse kontseptuaalsele, mitte formaalsele materjali esitlusele.

> See kursus põhineb [JWBurgers'i repol](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Kõik õigused kuuluvad temale. Sisu ei ole veel lõpetatud ja on siin ainult näitamaks, kuidas me võiksime seda integreerida, kui JWburger nõustub.

### Motivatsioon ja eesmärgid

On raske leida materjale, mis pakuksid head keskteed krüptograafia õpetamisel.

Ühelt poolt on pikad, formaalsed käsitlused, mis on tõeliselt ligipääsetavad ainult neile, kellel on tugev taust matemaatikas, loogikas või mõnes muus formaalses distsipliinis. Teiselt poolt on väga üldised sissejuhatused, mis tõesti varjavad liiga palju detaile neile, kes on vähemalt natuke uudishimulikud.

See krüptograafia sissejuhatus püüab tabada keskteed. Kuigi see peaks olema suhteliselt keeruline ja detailne kõigile, kes on krüptograafiaga uued, ei ole see tüüpilise alustava käsitluse küülikuurg.

### Sihtgrupp

Arendajatest intellektuaalselt uudishimulikeni, see raamat on kasulik kõigile, kes soovivad rohkem kui pealiskaudset mõistmist krüptograafiast. Kui teie eesmärk on meisterdada krüptograafia valdkonnas, siis on see raamat samuti hea alguspunkt.

### Lugemisjuhised

Raamat sisaldab praegu seitset peatükki: "Mis on krüptograafia?" (1. peatükk), "Krüptograafia matemaatilised alused I" (2. peatükk), "Krüptograafia matemaatilised alused II" (3. peatükk), "Sümmeetriline krüptograafia" (4. peatükk), "RC4 ja AES" (5. peatükk), "Asümmeetriline krüptograafia" (6. peatükk) ja "RSA krüptosüsteem" (7. peatükk). Viimane peatükk, "Krüptograafia praktikas", lisatakse veel. See keskendub erinevatele krüptograafilistele rakendustele, sealhulgas transpordikihi turvalisusele, sibulmarsruutimisele ja Bitcoini väärtusvahetussüsteemile.
Kui teil pole tugevat matemaatika tausta, on arvuteooria tõenäoliselt selle raamatu kõige keerulisem teema. Pakun sellest ülevaadet 3. peatükis ning see ilmub ka AESi tutvustuses 5. peatükis ja RSA krüptosüsteemi käsitluses 7. peatükis.
Kui teil on tõesti raskusi nende raamatu osade formaalsete detailidega, soovitan esimesel korral piirduda nende kõrgetasemelise lugemisega.

### Tunnustused

Selle raamatu kujundamisel kõige mõjukam raamat on olnud Jonathan Katzi ja Yehuda Lindelli _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL), 2015. Courseras on saadaval kaasnev kursus nimega "Cryptography."

Peamised lisallikad, mis on olnud abiks selle raamatu ülevaate loomisel, on Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar ja Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) ja Paari põhjal loodud kursus nimega “Introduction to Cryptography” (saadaval aadressil https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); ning Bruce Schneier, Applied Cryptography, 2. väljaanne, 2015 (Indianapolis, IN: John Wiley & Sons).

Tsiteerin ainult väga spetsiifilist informatsiooni ja tulemusi, mille võtan nendest allikatest, kuid tahan siinkohal tunnustada oma üldist võlga neile.

Nendele lugejatele, kes soovivad pärast seda sissejuhatust krüptograafia kohta rohkem edasijõudnud teadmisi otsida, soovitan väga Katzi ja Lindelli raamatut. Katzi kursus Courseras on raamatust veidi kättesaadavam.

### Panused

Palun vaadake läbi panuste fail repositooriumis, et saada juhiseid, kuidas projekti toetada.

# Mis on krüptograafia?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

Alustame meie uurimist krüptograafia valdkonnas ühe selle ajaloo võluvama ja meelelahutuslikuma episoodiga: Beale'i šifridest.<sup>[1](#footnote1)</sup>

Minu arvates on Beale'i šifride lugu tõenäolisemalt väljamõeldis kui reaalsus. Kuid väidetavalt toimus see järgnevalt.

## Beale'i šifrid
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Nii 1820. aasta talvel kui ka 1822. aastal peatus mees nimega Thomas J. Beale Lynchburgis (Virginia) Robert Morrissi omanduses olevas võõrastemajas. Beale'i teise peatumise lõpus andis ta Morrissile rauast kasti väärtuslike paberitega hoiule.

Mõni kuu hiljem sai Morriss Beale'ilt kirja, mis oli dateeritud 9. maiga 1822. Selles rõhutati rauast kasti sisu suurt väärtust ja anti Morrissile mõned juhised: kui ei Beale ega ükski tema kaaslastest ei tulnud kunagi kasti nõudma, peaks ta selle avama täpselt kümme aastat kirja kuupäevast (st 9. mail 1832). Mõned kasti sees olevad paberid oleksid kirjutatud tavalises tekstis. Mitmed teised aga oleksid “mõistetamatud ilma võtme abita.” See “võti” toimetataks siis Morrissile Beale'i nimetamata sõbra poolt 1832. aasta juunis.
Hoolimata selgetest juhistest ei avanud Morriss kasti 1832. aasta mais ja Beale'i salapärane sõber ei ilmunud kunagi juunis samal aastal. Alles 1845. aastal otsustas kõrtsmik lõpuks kasti avada. Selles leidis Morriss märkme, mis selgitas, kuidas Beale ja tema kaaslased avastasid läänes kulla ja hõbeda ning matsid selle koos mõningate juveelidega turvalisuse huvides maha. Lisaks sisaldas kast kolme **šifriteksti**: see tähendab, tekste, mis on kirjutatud koodis ja mille avamiseks on vaja **krüptograafilist võtit** ehk saladust ja kaasnevat algoritmi. Seda šifriteksti avamise protsessi nimetatakse **dekrüpteerimiseks**, samas kui lukustamise protsessi nimetatakse **krüpteerimiseks**. (Nagu selgitatakse 3. peatükis, võib terminil šiffer olla mitu tähendust. Nimes "Beale'i šifrid" on see lühend šifritekstidest.)
Kolm šifriteksti, mille Morriss raudkastist leidis, koosnevad igaüks komadega eraldatud numbrite jadast. Beale'i märkme kohaselt annavad need šifritekstid eraldi teada aarde asukoha, aarde sisu ja nimekirja õigustatud pärijatest koos nende osadega (viimane teave on oluline juhul, kui Beale ja tema kaaslased ei tuleks kunagi kasti nõudma).

Morris üritas kolme šifriteksti dekrüpteerida kakskümmend aastat. See oleks olnud lihtne võtmega. Kuid Morrissil ei olnud võtit ja ta ei õnnestunud oma katsetes taastada algtekste ehk **tavatekste**, nagu neid krüptograafias tavaliselt nimetatakse.

Elu lõpupoole andis Morriss kasti üle sõbrale 1862. aastal. See sõber avaldas hiljem 1885. aastal pamfleti pseudonüümi J.B. Ward all. See sisaldas (väidetavat) kasti ajalugu, kolme šifriteksti ja lahenduse, mille ta oli teise šifriteksti jaoks leidnud. (Ilmselt on igale šifritekstile oma võti, mitte üks võti, mis töötab kõigi kolme šifriteksti peal, nagu Beale oma kirjas Morrissile algselt näis vihjanud.)

Teise šifriteksti näete allpool *Joonisel 2*.<sup>[2](#footnote2)</sup> Selle šifriteksti võti on Ameerika Ühendriikide Iseseisvusdeklaratsioon. Dekrüpteerimisprotseduur taandub järgmiste kahe reegli rakendamisele:

* Iga šifritekstis oleva numbri n puhul leidke Ameerika Ühendriikide Iseseisvusdeklaratsioonis n-nda sõna
* Asendage number n leitud sõna esimese tähega

*Joonis 1: Beale'i šiffer nr 2*

![Joonis 1: Beale'i šiffer nr 2.](assets/Figure1-1.webp "Joonis 1: Beale'i šiffer nr. 2")

Näiteks teise šifriteksti esimene number on 115. Iseseisvusdeklaratsiooni 115. sõna on “instituted,” seega on tavateksti esimene täht “i.” Šifritekst ei näita otseselt sõnade vahet ega suurtähti. Kuid pärast esimeste sõnade dekrüpteerimist võite loogiliselt järeldada, et tavateksti esimene sõna oli lihtsalt “I.” (Tavatekst algab fraasiga “I have deposited in the county of Bedford.”)
Pärast dešifreerimist annab teine sõnum üksikasjaliku sisu aarde kohta (kuld, hõbe ja juveelid) ning viitab sellele, et see oli maetud raudpottidesse ja kaetud kividega Bedfordi maakonnas (Virginia). Inimesed armastavad head müsteeriumi, seega on suuri jõupingutusi kulutatud teiste kahe Beale'i šifri dešifreerimisele, eriti sellele, mis kirjeldab aarde asukohta. Isegi mitmed tuntud krüptograafid on neid proovinud lahti muukida. Siiski, seni pole keegi suutnud dešifreerida kahte ülejäänud šifriteksti.

## Kaasaegne krüptograafia
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Värvikad lood nagu Beale'i šifrid on see, mida enamik meist seostab krüptograafiaga. Ometi erineb kaasaegne krüptograafia vähemalt neljal olulisel viisil nendest ajaloolistest näidetest.

Esiteks, ajalooliselt on krüptograafia olnud mures ainult **saladuslikkuse** (või konfidentsiaalsuse) pärast. Šifritekste loodi selleks, et tagada, et ainult teatud osapooled võiksid olla teadlikud selgetekstides olevast informatsioonist, nagu Beale'i šifrite puhul. Selleks, et krüpteerimisskeem teeniks seda eesmärki hästi, peaks šifriteksti dešifreerimine olema teostatav ainult siis, kui sul on võti.

Kaasaegne krüptograafia tegeleb laiema teemade ringiga kui ainult saladuslikkus. Need teemad hõlmavad peamiselt (1) **sõnumi terviklikkust**—see tähendab, kinnitamist, et sõnumit ei ole muudetud; (2) **sõnumi autentsust**—see tähendab, kinnitamist, et sõnum on tõepoolest saadetud kindlalt saatjalt; ja (3) **mitte-eitamist**—see tähendab, kinnitamist, et saatja ei saa hiljem valesti eitada, et ta sõnumi saatis.

Oluline eristus, mida meeles pidada, on seega vahel **krüpteerimisskeemi** ja **krüptograafilise skeemi** vahel. Krüpteerimisskeem tegeleb ainult saladuslikkusega. Kuigi krüpteerimisskeem on krüptograafiline skeem, vastupidine ei pruugi olla tõsi. Krüptograafiline skeem võib samuti teenida krüptograafia teisi peateemasid, sealhulgas terviklikkust, autentsust ja mitte-eitamist.

Terviklikkuse ja autentsuse teemad on sama olulised kui saladuslikkus. Meie kaasaegsed kommunikatsioonisüsteemid ei suudaks toimida ilma garantiideta kommunikatsiooni terviklikkuse ja autentsuse osas. Mitte-eitamine on samuti oluline mure, näiteks digitaalsete lepingute puhul, kuid vähem üldlevinud vajadus krüptograafilistes rakendustes kui saladuslikkus, terviklikkus ja autentsus.

Teiseks, klassikalised krüpteerimisskeemid nagu Beale'i šifrid hõlmavad alati ühte võtit, mis jagati kõigi asjakohaste osapoolte vahel. Siiski, paljud kaasaegsed krüptograafilised skeemid hõlmavad mitte ainult ühte, vaid kahte võtit: **privaatset** ja **avalikku võtit**. Kuigi esimene peaks jääma privaatseks igas rakenduses, on viimane tavaliselt avalik teave (seega nende nimed). Krüpteerimise valdkonnas saab avalikku võtit kasutada sõnumi krüpteerimiseks, samal ajal kui privaatvõtit saab kasutada dekrüpteerimiseks.

Krüptograafia haru, mis tegeleb skeemidega, kus kõik osapooled jagavad ühte võtit, on tuntud kui **sümmeetriline krüptograafia**. Sellises skeemis olevat üksikut võtit nimetatakse tavaliselt **privaatvõtmeks** (või salajaseks võtmeks). Krüptograafia haru, mis tegeleb skeemidega, mis nõuavad privaat-avaliku võtme paari, on tuntud kui **asümmeetriline krüptograafia**. Neid harusid nimetatakse mõnikord ka **privaatvõtme krüptograafiaks** ja **avaliku võtme krüptograafiaks**, vastavalt (kuigi see võib tekitada segadust, kuna avaliku võtme krüptograafilised skeemid omavad samuti privaatvõtmeid).
Asümmeetrilise krüptograafia tulek 1970ndate lõpus on olnud üks olulisemaid sündmusi krüptograafia ajaloos. Ilma selleta ei oleks enamik meie kaasaegseid suhtlussüsteeme, sealhulgas Bitcoin, võimalikud või vähemalt väga ebapraktilised.
Oluliselt, kaasaegne krüptograafia ei ole ainult sümmeetriliste ja asümmeetriliste võtmekrüptograafia skeemide uurimine (kuigi see hõlmab suurt osa valdkonnast). Näiteks tegeleb krüptograafia ka räsifunktsioonide ja pseudosuvaliste numbrite generaatoritega, ning nende primitiivide põhjal saab ehitada rakendusi, mis ei ole seotud sümmeetrilise või asümmeetrilise võtmekrüptograafiaga.

Kolmandaks, klassikalised krüpteerimisskeemid, nagu neid kasutati Beale'i šifrites, olid rohkem kunst kui teadus. Nende tajutav turvalisus põhines suuresti intuitsioonil nende keerukuse osas. Tavaliselt parandati neid, kui õpiti tundma uut rünnakut nende vastu, või loobuti neist täielikult, kui rünnak oli eriti tõsine. Kaasaegne krüptograafia on aga range teadus, mis kasutab formaalset, matemaatilist lähenemist nii krüptograafiliste skeemide väljatöötamiseks kui ka analüüsimiseks.

Eelkõige keskendub kaasaegne krüptograafia formaalsetele **turvalisuse tõestustele**. Iga krüptograafilise skeemi turvalisuse tõestus toimub kolmes etapis:

1. **Krüptograafilise turvalisuse definitsiooni** avaldus, see tähendab turvalisuse eesmärkide ja ründaja poolt esitatud ohu kogum.
2. Matemaatiliste eelduste avaldus skeemi arvutusliku keerukuse osas. Näiteks võib krüptograafiline skeem sisaldada pseudosuvaliste numbrite generaatorit. Kuigi me ei saa tõestada nende olemasolu, võime eeldada, et nad on olemas.
3. Matemaatilise **turvalisuse tõestuse** esitamine skeemi kohta, lähtudes formaalsest turvalisuse mõistest ja kõigist matemaatilistest eeldustest.

Neljandaks, kuigi ajalooliselt kasutati krüptograafiat peamiselt sõjalistes seadetes, on see digiajastul imbunud meie igapäevategevustesse. Olgu selleks siis internetipangandus, postitamine sotsiaalmeedias, toote ostmisega Amazonist krediitkaardiga või sõbrale bitcoini jootraha andmine, krüptograafia on meie digiajastu hädavajalik osa.

Arvestades neid nelja aspekti kaasaegses krüptograafias, võiksime kaasaegset **krüptograafiat** iseloomustada kui teadust, mis tegeleb krüptograafiliste skeemide formaalse väljatöötamise ja analüüsiga digitaalse informatsiooni kaitsmiseks vaenulike rünnakute eest. Turvalisus siin tuleks mõista laialt kui rünnakute ärahoidmist, mis kahjustavad saladuse hoidmist, terviklikkust, autentsust ja/või mittetagasivõetavust suhtluses.

Krüptograafiat tuleks näha kui **küberjulgeoleku** aladistsipliini, mis tegeleb arvutisüsteemide varguse, kahjustamise ja väärkasutuse ärahoidmisega. Märkige, et paljud küberjulgeoleku mured on krüptograafiaga vähe või ainult osaliselt seotud.

Näiteks, kui ettevõte majutab kohapeal kalleid servereid, võivad nad olla mures selle riistvara varguse ja kahjustamise eest. Kuigi see on küberjulgeoleku mure, ei ole sel palju pistmist krüptograafiaga.

Teise näitena, **phishing rünnakud** on meie kaasaegses ajastus levinud probleem. Need rünnakud üritavad inimesi petta e-posti või mõne muu sõnumivahendi kaudu loovutama tundlikku teavet nagu paroole või krediitkaardinumbreid. Kuigi krüptograafia võib aidata phishing rünnakutega teatud määral tegeleda, nõuab terviklik lähenemine enamat kui lihtsalt mõningate krüptograafia kasutamist.

## Avatud suhtlus

Kaasaegne krüptograafia on loodud tagama turvalisuse tagatisi **avatud suhtluse** keskkonnas. Kui meie suhtluskanal on nii hästi kaitstud, et pealtkuulajatel pole mingit võimalust meie sõnumeid manipuleerida või isegi lihtsalt jälgida, siis on krüptograafia üleliigne. Enamik meie suhtluskanaleid siiski pole nii hästi kaitstud.
Kaasaegse maailma suhtluse selgroog on tohutu võrgustik kiudoptilisi kaableid. Telefonikõnede tegemine, televiisori vaatamine ja veebis surfamine kaasaegses majapidamises sõltub üldiselt sellest kiudoptiliste kaablite võrgustikust (väike protsent võib sõltuda puhtalt satelliitidest). Tõsi on, et teil võib kodus olla erinevaid andmesideühendusi, nagu koaksiaalkaabel, (asümmeetriline) digitaalne tellijaliin ja kiudoptiline kaabel. Kuid vähemalt arenenud maailmas ühinevad need erinevad andmekandjad kiiresti väljaspool teie maja sõlmpunkti tohutus kiudoptiliste kaablite võrgustikus, mis ühendab kogu maakera. Erandid on mõned arenenud maailma kauged piirkonnad, nagu Ameerika Ühendriikides ja Austraalias, kus andmeliiklus võib endiselt ka läbida olulisi vahemaid traditsiooniliste vasktelefonijuhtmete kaudu.
Potentsiaalsetel ründajatel oleks võimatu takistada füüsilist juurdepääsu sellele kaablite võrgustikule ja selle toetavale infrastruktuurile. Tegelikult teame juba, et enamik meie andmeid pealtkuulavad erinevad riiklikud luureagentuurid Interneti olulistel ristmikel. See hõlmab kõike alates Facebooki sõnumitest kuni veebiaadressideni, mida külastate.

Andmete massilise jälgimise nõuab võimsat vastast, nagu riiklik luureagentuur, kuid ründajad, kellel on vaid vähesed ressursid, võivad kergesti üritada nuhkida kohalikul tasandil. Kuigi see võib toimuda juhtmete pealtkuulamise tasandil, on palju lihtsam lihtsalt juhtmevaba side pealt kuulata.

Enamik meie kohalikust võrguandmetest - olgu see siis meie kodudes, kontoris või kohvikus - liigub nüüd raadiolainete kaudu juhtmevabadesse pääsupunktidesse kõik-ühes ruuterites, mitte füüsiliste kaablite kaudu. Seega vajab ründaja teie kohaliku liikluse pealtkuulamiseks vähe ressursse. See on eriti murettekitav, kuna enamik inimesi teeb oma kohalike võrkude kaudu liikuvate andmete kaitsmiseks väga vähe. Lisaks võivad potentsiaalsed ründajad sihtida ka meie mobiilse lairibaühendusi, nagu 3G, 4G ja 5G. Kõik need juhtmevabad sideliigid on ründajatele kergeks sihtmärgiks.

Seega on kommunikatsiooni salajas hoidmise idee, kaitstes suhtluskanalit, paljuski kaasaegses maailmas lootusetult petlik püüdlus. Kõik, mida teame, õigustab tõsist paranoiat: peaksite alati eeldama, et keegi kuulab. Ja krüptograafia on peamine vahend, mis meil on mingisuguse turvalisuse saavutamiseks selles kaasaegses keskkonnas.

### Märkused
[^1]: Hea kokkuvõtte loo kohta leiate Simon Singhi raamatust *The Code Book*, Fourth Estate (London, 1999), lk 82-99. Loo põhjal tegi Andrew Allen 2010. aastal lühifilmi. Filmi “The Thomas Beale Cipher” leiate selle veebisaidilt [^1].

[^2]: See pilt on saadaval Wikipedia lehel Beale'i šifrite kohta [^2].

[^3]: Täpsemalt öeldes on krüptograafiliste skeemide olulised rakendused olnud seotud saladuse hoidmisega. Näiteks lapsed kasutavad sageli lihtsaid krüptograafilisi skeeme “lõbu pärast”. Sellistel juhtudel saladus tegelikult ei ole mure [^3].

[^4]: Bruce Schneier, *Applied Cryptography*, 2. väljaanne, 2015 (Indianapolis, IN: John Wiley & Sons), lk 2 [^4].

[^5]: Vaadake Jonathan Katzi ja Yehuda Lindelli raamatut *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), eriti lk 16–23, hea kirjelduse saamiseks [^5].

[^6]: Vt Katz ja Lindell, samas, lk 3. Arvan, et nende karakteristikul on mõningaid probleeme, seega esitan siin nende avaldusest veidi erineva versiooni [^6].
[^7]: Vaadake näiteks Olga Khazani artiklit, "The creepy, long-standing practice of undersea cable tapping", *The Atlantic*, 16. juuli 2013 (saadaval aadressil [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)) [^7].

# Krüptograafia matemaatilised alused I
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

Krüptograafia põhineb matemaatikal. Ja kui soovite mõista krüptograafiat rohkem kui pealiskaudselt, peate olema mugav selle matemaatikaga.

See peatükk tutvustab enamikku põhilisest matemaatikast, millega kokku puutute krüptograafiat õppides. Teemad hõlmavad juhuslikke muutujaid, modulo operatsioone, XOR operatsioone ja pseudorandomnessi. Peaksite omandama need jaotised materjalid, et mõista krüptograafiat mittepealiskaudselt.

Järgmine peatükk käsitleb arvuteooriat, mis on palju keerulisem.

## Juhuslikud muutujad
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Juhuslikku muutujat tähistatakse tavaliselt mittepaksus, suurtähes. Näiteks võime rääkida juhuslikust muutujast X, juhuslikust muutujast Y või juhuslikust muutujast Z. Seda notatsiooni kasutan ka edaspidi.

**Juhuslik muutuja** võib võtta kahte või enamat võimalikku väärtust, igaühega teatud positiivse tõenäosusega. Võimalikud väärtused on loetletud **tulemuste hulgas**.

Iga kord, kui te **valimite** juhuslikku muutujat, tõmbate selle tulemuste hulgast kindla väärtuse vastavalt määratletud tõenäosustele.

Vaadelgem lihtsat näidet. Eeldagem muutujat X, mis on määratletud järgmiselt:

* X tulemuste hulk on {1,2}
* Pr [X = 1] = 0,5
* Pr [X = 2] = 0,5

On lihtne näha, et X on juhuslik muutuja. Esiteks, on kaks või enam võimalikku väärtust, mida X võib võtta, nimelt 1 ja 2. Teiseks, iga võimalik väärtus omab positiivset tõenäosust ilmneda, kui te valite X, nimelt 0,5.

Kõik, mida juhuslik muutuja nõuab, on tulemuste hulk kahe või enama võimalusega, kus iga võimalusel on positiivne tõenäosus ilmneda valimisel. Põhimõtteliselt võib juhuslikku muutujat siis defineerida abstraktselt, kontekstist sõltumatult. Sel juhul võite mõelda „valimisele“ kui mingi loodusliku eksperimendi läbiviimisele, et määrata juhusliku muutuja väärtus.

Muutuja X eespool oli defineeritud abstraktselt. Seega võite mõelda muutuja X valimisele kui ausa mündi viskamisele ja „2“ määramisele, kui tuleb kiri, ning „1“ määramisele, kui tuleb kull. Iga X valimi puhul viskate mündi uuesti.

Alternatiivselt võite mõelda ka X valimisele kui ausa täringu veeretamisele ja „2“ määramisele, kui täring maandub 1, 3 või 4 peale, ning „1“ määramisele, kui täring maandub 2, 5 või 6 peale. Iga kord, kui valite X, veerate täringut uuesti.

Tegelikult võib iga looduslik eksperiment, mis võimaldaks defineerida eespool nimetatud X võimalike väärtuste tõenäosused, olla ette kujutatud seoses tõmbamisega.
Sageli ei tutvustata juhuslikke muutujaid lihtsalt abstraktselt. Selle asemel on võimalike tulemuste hulk selgelt seotud reaalse maailma tähendusega (mitte ainult numbrite kujul). Lisaks võivad need tulemused olla määratletud mingi konkreetse eksperimendi suhtes (mitte igasuguse loomuliku eksperimendi puhul nende väärtustega).
Vaatleme nüüd näidet muutuja X kohta, mis ei ole määratletud abstraktselt. X on määratletud järgmiselt, et otsustada, kumb kahest meeskonnast jalgpallimängu alustab:

* X tulemuste hulk on {punane alustab, sinine alustab}
* Visatakse konkreetset münti C: kiri = “punane alustab”; kull = “sinine alustab”
* Pr [X = punane alustab] = 0.5
* Pr [X = sinine alustab] = 0.5

Sel juhul on X tulemuste hulk varustatud konkreetse tähendusega, nimelt milline meeskond jalgpallimängus alustab. Lisaks on võimalikud tulemused ja nende tõenäosused määratud konkreetse eksperimendi, nimelt konkreetse münti C viskamise, abil.

Krüptograafia aruteludes tutvustatakse juhuslikke muutujaid tavaliselt tulemuste hulgaga, millel on reaalse maailma tähendus. See võib olla kõigi sõnumite hulk, mida saab krüpteerida, tuntud kui sõnumiruum, või kõigi võtmete hulk, mida krüpteerimist kasutavad pooled saavad valida, tuntud kui võtmeruum.

Krüptograafia aruteludes ei määratleta juhuslikke muutujaid siiski tavaliselt mingi konkreetse loomuliku eksperimendi suhtes, vaid igasuguse eksperimendi suhtes, mis võib anda õigeid tõenäosusjaotusi.

Juhuslikud muutujad võivad olla diskreetse või pideva tõenäosusjaotusega. **Diskreetse tõenäosusjaotusega** juhuslikud muutujad - ehk diskreetsed juhuslikud muutujad - omavad piiratud arvu võimalikke tulemusi. Seni toodud näidetes oli juhuslik muutuja X diskreetne.

**Pidevad juhuslikud muutujad** võivad võtta väärtusi ühes või mitmes intervallis. Võiks öelda, näiteks, et juhuslik muutuja võtab proovimisel mis tahes reaalarvu väärtuse vahemikus 0 kuni 1, ja et selles intervallis on iga reaalarv võrdselt tõenäoline. Selles intervallis on lõpmatult palju võimalikke väärtusi.

Krüptograafia arutelude jaoks on vaja mõista ainult diskreetseid juhuslikke muutujaid. Seega tuleks edaspidi juhuslike muutujate arutelusid mõista kui viiteid diskreetsetele juhuslikele muutujatele, kui ei ole spetsiifiliselt teisiti öeldud.

### Juhuslike muutujate graafiline kujutamine

Juhusliku muutuja võimalikke väärtusi ja nendega seotud tõenäosusi saab hõlpsasti visualiseerida graafiku abil. Näiteks, vaadeldes eelmises jaotises toodud juhuslikku muutujat X tulemuste hulgaga {1,2}, ja Pr [X = 1] = 0.5 ning Pr [X = 2] = 0.5. Tavaliselt kujutaksime sellist juhuslikku muutujat ribagraafiku kujul, nagu *Joonis 1*.

*Joonis 1: Juhuslik muutuja X*

![Joonis 1: Juhuslik muutuja X.](assets/Figure2-1.webp)

*Joonis 1* laiad ribad ei tähenda kindlasti, et juhuslik muutuja X on tegelikult pidev. Ribad on tehtud laiaks, et need oleksid visuaalselt atraktiivsemad (lihtsalt sirge joon ülespoole pakub vähem intuitiivset visualiseerimist).

### Ühtlased muutujad

Väljendis “juhuslik muutuja” tähendab termin “juhuslik” lihtsalt “tõenäoline”. Teisisõnu, see tähendab, et muutuja kaks või enam võimalikku tulemust esinevad teatud tõenäosustega. Need tulemused ei pea siiski tingimata olema võrdselt tõenäolised (kuigi termin “juhuslik” võib teistes kontekstides tõesti seda tähendada).
**Ühtlane muutuja** on juhusliku muutuja erijuhtum. See võib võtta kahte või enamat väärtust, kõik võrdse tõenäosusega. Juhuslik muutuja X, mida on kujutatud *joonisel 1*, on selgelt ühtlane muutuja, kuna mõlemad võimalikud tulemused esinevad tõenäosusega 0,5. Siiski on palju juhuslikke muutujaid, mis ei ole ühtlaste muutujate näited.
Võtame näiteks juhusliku muutuja Y. Selle tulemuste hulk on {1,2,3,8,10} ja järgmine tõenäosusjaotus: Pr [Y = 1] = 0,25; Pr [Y = 2] = 0,35; Pr [Y = 3] = 0,1; Pr [Y = 8] = 0,25; Pr [Y = 10] = 0,05.

Kuigi kaks võimalikku tulemust tõepoolest esinevad võrdse tõenäosusega, nimelt 1 ja 8, võib Y võtta ka teatud väärtusi erinevate tõenäosustega kui 0,25 valimisel. Seega, kuigi Y on tõepoolest juhuslik muutuja, ei ole see ühtlane muutuja.

Y graafiline kujutis on esitatud *joonisel 2*.

*Joonis 2: Juhuslik muutuja Y*

![Joonis 2: Juhuslik muutuja Y.](assets/Figure2-2.webp "Joonis 2: Juhuslik muutuja Y")

Lõpliku näitena vaadake juhuslikku muutujat Z. Selle tulemuste hulk on {1,3,7,11,12} ja järgmine tõenäosusjaotus: Pr (2) = 0,2; Pr (3) = 0,2; Pr (9) = 0,2; Pr (11) = 0,2; Pr (12) = 0,2. Seda saab näha joonisel 3. Juhuslik muutuja Z on, erinevalt Y-st, tõepoolest ühtlane muutuja, kuna kõik võimalike väärtuste tõenäosused valimisel on võrdsed.

*Joonis 3: Juhuslik muutuja Z*

![Joonis 3: Juhuslik muutuja Z.](assets/Figure2-3.webp "Joonis 3: Juhuslik muutuja Z")


### Tingimuslik tõenäosus

Eeldame, et Bob kavatseb ühtlaselt valida päeva eelmisest kalendriaastast. Mida peaksime järeldama tõenäosuse kohta, et valitud päev on suvel?

Niikaua kui me arvame, et Bobi protsess on tõepoolest tõeliselt ühtlane, peaksime järeldama, et on 1/4 tõenäosus, et Bob valib päeva suvel. See on **tingimusteta tõenäosus**, et juhuslikult valitud päev on suvel.

Eeldame nüüd, et Bob ei vali ühtlaselt kalendripäeva, vaid valib ühtlaselt nende päevade hulgast, mil Crystal Lake'i (New Jersey) keskpäevane temperatuur oli 21 kraadi Celsiust või kõrgem. Arvestades seda lisateavet, mida võime järeldada tõenäosuse kohta, et Bob valib päeva suvel?

Me peaksime tõesti jõudma erineva järelduseni kui varem, isegi ilma täiendava konkreetse teabeta (nt iga päeva keskpäevane temperatuur eelmisel kalendriaastal).

Teades, et Crystal Lake asub New Jerseys, ei ootaks me kindlasti, et keskpäevane temperatuur oleks talvel 21 kraadi Celsiust või kõrgem. Selle asemel on palju tõenäolisem, et tegemist on soojema päevaga kevadel või sügisel või päevaga kusagil suvel. Seega, teades, et Crystal Lake'i valitud päeva keskpäevane temperatuur oli 21 kraadi Celsiust või kõrgem, muutub tõenäosus, et Bobi valitud päev on suvel, palju suuremaks. See on **tingimuslik tõenäosus**, et juhuslikult valitud päev on suvel, arvestades, et Crystal Lake'i keskpäevane temperatuur oli 21 kraadi Celsiust või kõrgem.
Erinevalt eelmisest näitest võivad kahe sündmuse tõenäosused olla ka täiesti seosetud. Sellisel juhul ütleme, et need on **sõltumatud**.
Oletame näiteks, et teatud aus münt on maandunud kullale. Arvestades seda fakti, mis on siis tõenäosus, et homme sajab vihma? Tingimuslik tõenäosus sel juhul peaks olema sama mis tingimusteta tõenäosus, et homme sajab vihma, kuna mündi viskamine üldiselt ei mõjuta ilma.

Tingimusliku tõenäosuse avalduste kirjutamiseks kasutame sümbolit “|”. Näiteks sündmuse A tõenäosus, arvestades, et sündmus B on aset leidnud, võib olla kirjutatud järgmiselt: Pr[A|B]. Seega, kui kaks sündmust, A ja B, on sõltumatud, siis Pr[A|B] = Pr[A] ja Pr[B|A] = Pr[B]. Sõltumatuse tingimus saab lihtsustatult väljendada järgmiselt: Pr[A,B] = Pr[A]*Pr[B].

Tõenäosusteoorias on üks võtmetulemus tuntud kui **Bayesi teoreem**. See põhimõtteliselt väidab, et Pr[A|B] saab ümber kirjutada järgmiselt:

Pr[A|B] = (Pr[B|A] • Pr[A]) / Pr[B]

Erinevate sündmuste spetsiifiliste tingimuslike tõenäosuste asemel võime vaadata ka kahe või enama juhusliku muutuja tingimuslikke tõenäosusi võimalike sündmuste hulgas. Oletame kaks juhuslikku muutujat, X ja Y. Mis tahes võimalikku väärtust X jaoks võime tähistada x-ga ja mis tahes võimalikku väärtust Y jaoks y-ga. Võime siis öelda, et kaks juhuslikku muutujat on sõltumatud, kui järgmine väide kehtib:

Pr[X = x,Y = y] = Pr[X = x] • Pr[Y = y] kõigi x ja y jaoks

Olgu see väide veidi selgemalt väljendatud.

Oletame, et X ja Y tulemuste hulgad on määratletud järgmiselt: **X** = {x<sub>1</sub>,x<sub>2</sub>….,x<sub>i</sub>,….x<sub>n</sub>} ja **Y** = {y<sub>1</sub>,y<sub>2</sub>….,y<sub>i</sub>,….y<sub>m</sub>}. (Tavaliselt tähistatakse väärtuste hulki julgete, suurtähtedega.)

Nüüd oletame, et te võtate proovi Y-st ja täheldate y<sub>1</sub>. Ülaltoodud väide ütleb meile, et tõenäosus saada nüüd x<sub>1</sub> proovist X on täpselt sama, nagu me poleks kunagi täheldanud y<sub>1</sub>. See kehtib mis tahes y<sub>i</sub> kohta, mille oleksime võinud saada algselt Y-st proovides. Lõpuks kehtib see mitte ainult x<sub>1</sub> kohta. Mis tahes x<sub>i</sub> esinemise tõenäosus ei ole mõjutatud Y proovist saadud tulemusest. Kõik see kehtib ka juhul, kui X proovitakse esimesena.

Lõpetagem meie arutelu veidi filosoofilisemal noodil. Mis tahes reaalses olukorras hinnatakse sündmuse tõenäosust alati kindla informatsioonikogumi vastu. Tingimusteta tõenäosust väga range sõna mõttes ei ole olemas.

Näiteks, kui ma küsiksin teilt tõenäosust, et sead lendavad aastaks 2030. Kuigi ma ei anna teile rohkem informatsiooni, teate te selgelt palju maailma kohta, mis võib mõjutada teie otsust. Te pole kunagi näinud, et sead lendaksid. Teate, et enamik inimesi ei oota, et nad lendaksid. Teate, et nad pole tegelikult ehitatud lendamiseks. Ja nii edasi.
Seega, kui me räägime mingi sündmuse "tingimusteta tõenäosusest" reaalses kontekstis, võib see termin tegelikult omada tähendust ainult siis, kui me mõistame seda kui "tõenäosust ilma igasuguse täiendava selge informatsioonita". Iga "tingimusliku tõenäosuse" mõistmine peaks seega alati olema mõistetav mingi konkreetse informatsiooni valguses.
Näiteks võiksin ma teilt küsida, milline on tõenäosus, et sead lendavad aastaks 2030, pärast seda, kui olen teile andnud tõendeid selle kohta, et mõned Uus-Meremaa kitsed on õppinud lendama pärast mõneaastast treeningut. Sel juhul kohandate tõenäoliselt oma hinnangut tõenäosusele, et sead lendavad aastaks 2030. Seega on tõenäosus, et sead lendavad aastaks 2030, tingimuslik sellele tõendile Uus-Meremaa kitsede kohta.

## Modulo operatsioon
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

Kõige lihtsam **modulo operatsiooni** väljend on järgmisel kujul: x mod y.

Muutujat x nimetatakse jagatavaks ja muutujat y jagajaks. Positiivse jagatava ja positiivse jagaja korral modulo operatsiooni sooritamiseks määratakse lihtsalt jagamise jääk.

Näiteks, kaaluge väljendit 25 mod 4. Arv 4 jagub arvuga 25 kokku 6 korda. Selle jagamise jääk on 1. Seega, 25 mod 4 võrdub 1-ga. Sarnasel viisil saame hinnata alljärgnevaid väljendeid:

* 29 mod 30 = 29 (kuna 30 jagub 29-ga kokku 0 korda ja jääk on 29)
* 42 mod 2 = 0 (kuna 2 jagub 42-ga kokku 21 korda ja jääk on 0)
* 12 mod 5 = 2 (kuna 5 jagub 12-ga kokku 2 korda ja jääk on 2)
* 20 mod 8 = 4 (kuna 8 jagub 20-ga kokku 2 korda ja jääk on 4)

Kui jagatav või jagaja on negatiivne, võivad programmeerimiskeeled modulo operatsioone erinevalt käsitleda.

Krüptograafias tuleb kindlasti ette juhtumeid negatiivse jagatavaga. Sellistel juhtudel on tüüpiline lähenemine järgmine:

* Esiteks määrake lähim väärtus, *mis on võrdne või väiksem kui* jagatav ja mille korral jagaja jagub jäägita. Nimetame seda väärtust p-ks.
* Kui jagatav on x, siis modulo operatsiooni tulemus on x – p väärtus.

Näiteks, eeldame, et jagatav on –20 ja jagaja 3. Lähim väärtus, mis on võrdne või väiksem kui –20 ja mille korral 3 jagub ühtlaselt, on –21. Sel juhul on x – p väärtus –20 – (–21). See võrdub 1-ga ja seega –20 mod 3 võrdub 1-ga. Sarnasel viisil saame hinnata alljärgnevaid väljendeid:

* –8 mod 5 = 2
* –19 mod 16 = 13
* –14 mod 6 = 4

Notatsiooni osas näete tavaliselt järgmisi tüüpi väljendeid: x = [y mod z]. Tänu sulgudele kehtib modulo operatsioon sel juhul ainult avaldise paremal poolel. Kui y võrdub 25 ja z võrdub 4, siis näiteks x võrdub 1-ga.
Ilma sulgudeta rakendub modulo tehe *mõlemale poolele* avaldises. Oletame näiteks järgmist avaldist: x = y mod z. Kui y on võrdne 25 ja z on võrdne 4, siis teame ainult, et x mod 4 annab tulemuseks 1. See on kooskõlas mis tahes x väärtusega hulgast {….– 7, – 3, 1, 5, 9….}. 
Matemaatika haru, mis hõlmab modulo tehteid arvudel ja avaldistel, nimetatakse **modulaararitmeetikaks**. Võite mõelda sellele harule kui aritmeetikale juhtudel, kui arvurida ei ole lõpmatult pikk. Kuigi me tavaliselt kohtame modulo tehteid (positiivsete) täisarvude puhul krüptograafias, võite modulo tehteid teostada ka mis tahes reaalarvudega.

### Nihkešiffer

Modulo tehet kohatakse sageli krüptograafias. Selle illustreerimiseks vaatleme üht kõige kuulsamat ajaloolist krüpteerimisskeemi: nihkešifferit.

Defineerime selle esmalt. Oletame sõnastikku *D*, mis seostab kõik inglise tähestiku tähed järjekorras arvude hulgaga {0,1,2…,25}. Eeldame sõnumiruumi **M**. **Nihkešiffer** on siis krüpteerimisskeem, mis on defineeritud järgmiselt:

- Vali ühtlaselt võti k võtmeruumist **K**, kus **K** = {0,1,2,…,25}<sup>[1](#footnote1)</sup>
- Krüpteeri sõnum m є **M**, järgmiselt:
    - Eralda m tema üksikuteks tähtedeks m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Teisenda iga m<sub>i</sub> arvuks vastavalt *D*-le
    - Iga m<sub>i</sub> puhul, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Teisenda iga c<sub>i</sub> täheks vastavalt *D*-le
    - Seejärel ühenda c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub>, et saada krüptotekst c
- Dekrüpteeri krüptotekst c järgmiselt:
    -- Teisenda iga c<sub>i</sub> arvuks vastavalt *D*-le
    -- Iga c<sub>i</sub> puhul, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    -- Teisenda iga m<sub>i</sub> täheks vastavalt *D*-le
    -- Seejärel ühenda m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub>, et saada algne sõnum m

Modulo operaator nihkešifris tagab, et tähed liiguvad ringi, nii et kõik krüptoteksti tähed on määratletud. Näiteks, kui rakendada nihkešifrit sõnale “DOG”.

Oletame, et olete ühtlaselt valinud võtme väärtusega 17. Täht “O” vastab arvule 15. Ilma modulo tehteta oleks selle algteksti numbri ja võtme liitmisel saadud krüptoteksti number 32. Kuid seda krüptoteksti numbrit ei saa teisendada krüptoteksti täheks, kuna inglise tähestikus on ainult 26 tähte. Modulo tehe tagab, et krüptoteksti number on tegelikult 6 (32 mod 26 tulemus), mis vastab krüptoteksti tähele “G”.

Kogu sõna “DOG” krüpteerimine võtme väärtusega 17 on järgmine:
* Sõnum = KOER = K,O,E,R = 3,15,6* c<sub>0</sub> = [(3 + 17) Mod 26] = [(20) Mod 26] = 20 = U
* c<sub>1</sub> = [(15 + 17) Mod 26] = [(32) Mod 26] = 6 = G
* c<sub>2</sub> = [(6 + 17) Mod 26] = [(23) Mod 26] = 23 = X
* c = UGX

Igaüks võib intuitiivselt mõista, kuidas nihkešiffer töötab ja tõenäoliselt seda ka ise kasutada. Siiski, et edendada oma teadmisi krüptograafiast, on oluline hakata mugavamalt suhtuma formaliseerimisega, kuna skeemid muutuvad palju keerulisemaks. Seetõttu formaliseeritigi nihkešifferi sammud.

## XOR operatsioon
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Kõik arvutiandmed töödeldakse, salvestatakse ja saadetakse võrkudes biti tasemel. Kõik krüptograafilised skeemid, mis rakendatakse arvutiandmetele, toimivad samuti biti tasemel.

Näiteks, kujutage ette, et olete oma e-posti rakendusse kirjutanud e-kirja. Kõik krüpteeringud, mida rakendate, ei toimu otse teie e-kirja ASCII tähemärkidel. Selle asemel rakendatakse neid tähemärkide ja teiste sümbolite bitiesitusele teie e-kirjas.

Üks oluline matemaatiline operatsioon, mida mõista kaasaegses krüptograafias peale modulo operatsiooni, on **XOR operatsioon** ehk "eksklusiivne või" operatsioon. See operatsioon võtab sisendiks kaks bitti ja annab väljundiks teise biti. XOR operatsioon lihtsalt tähistatakse kui "XOR". See annab 0, kui kaks bitti on samad, ja 1, kui kaks bitti on erinevad. Allpool näete nelja võimalust.

* 0 XOR 0 = 0
* 0 XOR 1 = 1
* 1 XOR 0 = 1
* 1 XOR 1 = 0

Võite teostada XOR operatsiooni kahe pikema sõnumi peal kui üks bitt, joondades nende kahe sõnumi bitid üles ja teostades XOR operatsiooni iga bitipaari peal eraldi.

Näiteks, kujutage ette, et teil on sõnum m<sub>1</sub> (01111001) ja sõnum m<sub>2</sub> (01011001). Nende kahe sõnumi XOR operatsiooni näete allpool.

* m<sub>1</sub> XOR m<sub>2</sub> = 01111001 XOR 01011001 = 00100000

Protsess on lihtne. Teete esmalt XOR operatsiooni m<sub>1</sub> ja m<sub>2</sub> vasakpoolseimatele bittidele. Sel juhul on see 0 XOR 0 = 0. Seejärel teete XOR operatsiooni järgmisele bitipaari vasakult. Sel juhul on see 1 XOR 1 = 0. Jätkate seda protsessi, kuni olete teostanud XOR operatsiooni parempoolseimatele bittidele.
On lihtne märgata, et XOR operatsioon on kommutatiivne, nimelt m<sub>1</sub> XOR m<sub>2</sub> = m<sub>2</sub> XOR m<sub>1</sub>. Lisaks on XOR operatsioon ka assotsiatiivne. See tähendab, et (m<sub>1</sub> XOR m<sub>2</sub>) XOR m<sub>3</sub> = m<sub>1</sub> XOR (m<sub>2</sub> XOR m<sub>3</sub>).
XOR operatsioon kahe erineva pikkusega stringi peal võib sõltuvalt kontekstist tähendada erinevaid asju. Me ei keskendu siin XOR operatsioonidele erineva pikkusega stringide puhul.

XOR operatsioon on võrdne erijuhtumiga, kus teostatakse modulo operatsioon bittide liitmisele, kui jagaja on 2. Võrdsust näete järgmistes tulemustes:

* (0 + 0) mod 2 = 0 XOR 0 = 0
* (1 + 0) mod 2 = 1 XOR 0 = 1
* (0 + 1) mod 2 = 0 XOR 1 = 1
* (1 + 1) mod 2 = 1 XOR 1 = 0

## Pseudorandomness
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Arutelus juhuslike ja ühtlaste muutujate üle tegime konkreetse vahet mõistete "juhuslik" ja "ühtlane" vahel. Praktikas hoitakse seda vahet tavaliselt, kui kirjeldatakse juhuslikke muutujaid. Kuid meie praeguses kontekstis tuleb see vahet ära jätta ja "juhuslik" ning "ühtlane" kasutatakse sünonüümidena. Ma selgitan põhjust selle jaotise lõpus.

Alustuseks võime nimetada binaarstringi pikkusega n **juhuslikuks** (või **ühtlaseks**), kui see oli tulemus, mis saadi ühtlase muutuja S valimisel, mis annab igale sellise pikkusega binaarstringile võrdse tõenäosuse valituks osutuda.

Oletame näiteks kõigi 8-bitiste binaarstringide hulka: {0000 0000, 0000 0001,…, 1111 1111}. (Tavaliselt kirjutatakse 8-bitine string kahe neliku kujul, mida nimetatakse **nibble**.) Nimetame seda stringide hulka **S<sub>8</sub>**.

Eelneva definitsiooni kohaselt võime siis nimetada konkreetset 8-bitist binaarstringi juhuslikuks (või ühtlaseks), kui see oli tulemus, mis saadi ühtlase muutuja S valimisel, mis annab igale stringile hulgas **S<sub>8</sub>** võrdse tõenäosuse valituks osutuda. Arvestades, et hulka **S<sub>8</sub>** kuulub 2<sup>8</sup> elementi, peaks valimisel iga stringi tõenäosus olema 1/2<sup>8</sup>.

Binaarstringi juhuslikkuse võtmeelement on see, et see on määratletud viitega protsessile, mille kaudu see valiti. Seega ei avalda ükski konkreetne binaarstring iseenesest midagi oma juhuslikkuse kohta valikul.

Näiteks paljud inimesed intuitiivselt arvavad, et string nagu 1111 1111 ei oleks saanud olla juhuslikult valitud. Kuid see on selgelt vale.
Määratledes ühtlase muutuja S kõigi 8 pikkuste binaarstringide üle, on tõenäosus valida komplektist **S<sub>8</sub>** string 1111 1111 sama mis stringi 0111 01001 valimisel. Seega ei saa te stringi juhuslikkuse kohta midagi öelda, lihtsalt analüüsides stringi ennast.
Me võime samuti rääkida juhuslikest stringidest, ilma et see tähendaks spetsiifiliselt binaarstringe. Näiteks võime rääkida juhuslikust heksastringist AF 02 82. Sel juhul oleks string valitud juhuslikult kõigi 6 pikkuste heksastringide hulgast. See on võrdväärne 24 pikkuse binaarstringi juhusliku valimisega, kuna iga heksadigitaal esindab 4 bitti.

Tavaliselt viitab väljend "juhuslik string" ilma täpsustuseta stringile, mis on juhuslikult valitud kõigi sama pikkusega stringide hulgast. Just nii olen ma seda eespool kirjeldanud. Stringi pikkusega n võib muidugi samuti juhuslikult valida erinevast komplektist. Näiteks ühest, mis moodustab ainult alamhulga kõigist n pikkusega stringidest, või ehk komplektist, mis sisaldab erineva pikkusega stringe. Sellistel juhtudel ei viitaks me sellele kui "juhuslik string", vaid pigem "string, mis on juhuslikult valitud mõnest komplektist **S**".

Krüptograafia üks võtmekontseptsioone on pseudorandomness. **Pseudorandom string** pikkusega n tundub *nagu* see oleks valitud ühtlasest muutujast S, mis annab igale stringile **S<sub>n</sub>** võrdsed valimise tõenäosused. Tegelikult aga on string valitud ühtlasest muutujast S', mis määratleb ainult tõenäosusjaotuse – mitte tingimata ühega, mis annab kõikidele võimalikele tulemustele võrdsed tõenäosused – **S<sub>n</sub>** alamhulgal. Oluline punkt siin on, et keegi ei saa tegelikult vahet teha S ja S' valimite vahel, isegi kui te võtate neid palju.

Eeldame näiteks juhuslikku muutujat S. Selle tulemuste komplekt on **S<sub>256</sub>**, see on kõigi 256 pikkuste binaarstringide hulk. Sellel hulgal on 2<sup>256</sup> elementi. Igal elemendil on valimisel võrdne tõenäosus, 1/2<sup>256</sup>.

Lisaks eeldame juhuslikku muutujat S’. Selle tulemuste hulk sisaldab ainult 2<sup>128</sup> binaarstringi pikkusega 256. Sellel on mingi tõenäosusjaotus nende stringide üle, kuid see jaotus ei pruugi olla ühtlane.

Eeldame nüüd, et võtsin 1000 valimit S-st ja 1000 valimit S'-st ning andsin mõlema tulemuste komplektid teile. Ma ütlen teile, milline tulemuste komplekt on seotud millise juhusliku muutujaga. Järgmisena võtan valimi ühest kahest juhuslikust muutujast. Kuid seekord ei ütle ma teile, millist juhuslikku muutujat ma valin. Kui S' oleks pseudorandom, siis idee on, et teie tõenäosus teha õige arvamus selle kohta, kumma juhusliku muutuja ma valisin, on praktiliselt mitte parem kui 1/2.

Tavaliselt toodetakse pseudorandom stringi pikkusega n, valides juhuslikult stringi suurusega n – x, kus x on positiivne täisarv, ja kasutades seda sisendina laiendusalgoritmile. See juhuslik string suurusega n – x on tuntud kui **seeme**.
Pseudorandom jadad on krüptograafia praktiliseks muutmise võtmemõiste. Võtame näiteks voogšifrid. Voogšifri puhul ühendatakse juhuslikult valitud võti laiendava algoritmiga, et toota palju pikem pseudorandom jada. See pseudorandom jada seejärel ühendatakse algtekstiga XOR-operatsiooni abil, et toota šifreeritud tekst. Kui me ei suudaks toota sellist tüüpi pseudorandom jada voogšifri jaoks, siis meil oleks vaja võtit, mis on sama pikk kui sõnum, et tagada selle turvalisus. See ei ole enamikul juhtudel väga praktiline valik.

Siin jaotises arutatud pseudorandomsuse mõistet saab defineerida formaalsemalt. See laieneb ka teistele kontekstidele. Kuid me ei pea siin seda arutelu süvendama. Kõik, mida te tegelikult peate intuitiivselt mõistma krüptograafia kohta, on erinevus juhusliku ja pseudorandom jada vahel.

Põhjus, miks me loobume eristamast "juhuslikku" ja "ühtlast" meie arutelus, peaks nüüd samuti olema selge. Praktikas kasutavad kõik terminit pseudorandom, et viidata jadale, mis tundub **nagu** see oleks saadud ühtlase muutuja S valimisel. Rangelt öeldes peaksime nimetama sellist jada "pseudo-ühtlaseks", kasutades meie varasemat keelekasutust. Kuna termin "pseudo-ühtlane" on nii kohmakas ja keegi ei kasuta seda, siis me ei tutvusta seda siin selguse huvides. Selle asemel lihtsalt loobume eristamast "juhuslikku" ja "ühtlast" praeguses kontekstis.

## Märkused
<chapterId>7cccd92c-15bc-5394-9024-af126988ecd7</chapterId>

[^1]: Seda väidet saab täpselt defineerida, kasutades eelmisest jaotisest pärit terminoloogiat. Olgu ühtlane muutuja K-l **K** kui selle võimalike tulemuste hulk. Nii Pr [K = 0] = 1/26, Pr [K = 1] = 1/26, ja nii edasi. Valige ühtlane muutuja K üks kord, et saada konkreetne võti [^1].

[^2]: Kui olete huvitatud nende küsimuste formaalsemast käsitlusest, võite konsulteerida Katz ja Lindell’i teosega *Introduction to Modern Cryptography*, eriti peatükk 3 [^2].

# Krüptograafia matemaatilised alused II
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

See peatükk käsitleb krüptograafia matemaatiliste aluste keerukamat teemat: arvuteooriat. Kuigi arvuteooria on oluline sümmeetrilises krüptograafias (näiteks Rijndaeli šifris), on see eriti oluline avaliku võtme krüptograafilises kontekstis.

Kui leiate arvuteooria detaile koormavaks, soovitaksin esimesel lugemisel kõrgtasemel lähenemist. Saate alati hiljem selle juurde tagasi pöörduda.

## Mis on arvuteooria?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Arvuteooriat võiks iseloomustada kui täisarvude ja matemaatiliste funktsioonide, mis töötavad täisarvudega, omaduste uurimist.

Võtke näiteks, et kaks arvu a ja N on **teinetest sõltumatud** (või **suhtelised algarvud**), kui nende suurim ühistegur on 1. Oletame nüüd konkreetset täisarvu N. Kui palju on täisarve, mis on väiksemad kui N ja on N-ga teinetest sõltumatud? Kas me saame teha üldisi väiteid selle küsimuse vastuste kohta? Need on tüüpilised küsimused, mida arvuteooria püüab vastata.
Kaasaegne arvuteooria tugineb abstraktse algebra vahenditele. **Abstraktne algebra** on matemaatika aladistsipliin, kus peamised analüüsiobjektid on abstraktsed objektid, mida tuntakse algebrastruktuuridena. **Algebrastruktuur** on elementide kogum, mis on ühendatud ühe või mitme tehtega, mis vastavad teatud aksioomidele. Algebrastruktuuride kaudu saavad matemaatikud saada ülevaate konkreetsetest matemaatilistest probleemidest, abstraherides nende detailidest.
Abstraktse algebra valdkonda nimetatakse mõnikord ka kaasaegseks algebraks. Võite samuti kohata mõistet **abstraktne matemaatika** (või **puhas matemaatika**). See viimane termin ei viita abstraktsele algebralle, vaid tähendab matemaatika uurimist iseenese pärast, mitte ainult potentsiaalsete rakenduste silmas pidades.

Abstraktse algebra kogumid võivad tegeleda paljude objektide tüüpidega, alates võrdkülgse kolmnurga kuju säilitavatest transformatsioonidest kuni tapeedimustriteni. Arvuteoorias kaalume ainult elementide kogumeid, mis sisaldavad täisarve või funktsioone, mis töötavad täisarvudega.

## Grupid
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Matemaatikas on põhimõiste elementide kogum. Kogumit tähistatakse tavaliselt aksantsulgudega, elementide eraldamiseks kasutatakse komasid.

Näiteks kõikide täisarvude kogum on {…,-2,-1,0,1,2,…}. Siin tähendab kolm punkti, et teatud muster jätkub kindlas suunas. Seega hõlmab kõikide täisarvude kogum ka 3, 4, 5, 6 ja nii edasi, samuti -3, -4, -5, -6 ja nii edasi. Seda kõikide täisarvude kogumit tähistatakse tavaliselt ℤ-ga.

Teine näide kogumist on ℤ mod 11 ehk kõikide täisarvude kogum modulo 11. Erinevalt terve kogumi ℤ-st sisaldab see kogum ainult piiratud arvu elemente, nimelt {0,1,…,9,10}.

Levinud eksiarvamus on arvata, et kogum ℤ mod 11 on tegelikult {-10,-9,…,0,…,9,10}. Kuid see pole nii, arvestades, kuidas me modulo tehet varem defineerisime. Kõik negatiivsed täisarvud, mida modulo 11 vähendatakse, mähitakse ümber {0,1,…,9,10}-ni. Näiteks avaldis -2 mod 11 mähitakse ümber 9-ks, samal ajal kui avaldis -27 mod 11 mähitakse ümber 5-ks.

Teine põhimõiste matemaatikas on binaartehe. See on iga tehe, mis võtab kaks elementi, et toota kolmas. Näiteks põhiaritmeetikast ja algebrast olete tuttav nelja põhilise binaartehtega: liitmine, lahutamine, korrutamine ja jagamine.

Neid kahte põhimatemaatilist kontseptsiooni, kogumeid ja binaartehteid, kasutatakse grupi mõiste määratlemiseks, mis on abstraktse algebra kõige olulisem struktuur.

Eeldame konkreetset binaartehte ◌. Lisaks eeldame elementide kogumit **S**, mis on varustatud selle tehtega. „Varustatud“ tähendab siin, et tehet ◌ saab teostada mis tahes kahe elemendi vahel kogumis **S**.

Kombinatsioon 〈**S**, ◌〉 on siis **grupp**, kui see vastab neljale konkreetsele tingimusele, mida tuntakse grupi aksioomidena.

1. Mis tahes a ja b, mis on elementideks kogumis **S**, on a ◌ b samuti kogumi **S** element. Seda tuntakse **sulgemistingimusena**.
2. Iga a, b ja c, mis on hulga **S** elemendid, kehtib, et (a ◌ b) ◌ c = a ◌ (b ◌ c). Seda nimetatakse **assotsiatiivsuse tingimuseks**. 3. Hulgas **S** on unikaalne element e, nii et iga elemendi a puhul hulgas **S** kehtib järgmine võrrand: e ◌ a = a ◌ e = a. Kuna selline element e on ainus, nimetatakse seda **ühikelemendiks**. Seda tingimust nimetatakse **ühiktingimuseks**.
4. Iga elemendi a puhul hulgas **S** eksisteerib element b hulgas **S**, nii et kehtib järgmine võrrand: a ◌ b = b ◌ a = e, kus e on ühikelement. Elementi b nimetatakse siin **pöördelemendiks**, ja seda tähistatakse tavaliselt kui a<sup>-1</sup>. Seda tingimust nimetatakse **pööratavuse tingimuseks**.

Vaadelgem gruppe veidi lähemalt. Tähistagem kõikide täisarvude hulka kui ℤ. See hulk koos standardse liitmisega, ehk 〈ℤ, +〉, vastab selgelt grupi definitsioonile, kuna see vastab eespool nimetatud neljale aksioomile.

1. Iga x ja y puhul, mis on ℤ elemendid, on x + y samuti ℤ elemendiks. Seega 〈ℤ, +〉 vastab sulgemise tingimusele.
2. Iga x, y ja z puhul, mis on ℤ elemendid, (x + y) + z = x + (y + z). Seega 〈ℤ, +〉 vastab assotsiatiivsuse tingimusele.
3. 〈ℤ, +〉 hulgas on ühikelement, nimelt 0. Iga x puhul ℤ-s kehtib, et: 0 + x = x + 0 = x. Seega 〈ℤ, +〉 vastab ühiktingimusele.
4. Lõpuks, iga elemendi x puhul ℤ-s on olemas y nii, et x + y = y + x = 0. Kui x oleks näiteks 10, siis y oleks –10 (juhul kui x on 0, on y samuti 0). Seega 〈ℤ, +〉 vastab pööratavuse tingimusele.

Oluline on märkida, et täisarvude hulk koos liitmisega moodustab grupi, kuid see ei tähenda, et see moodustaks grupi korrutamisega. Saate seda kontrollida, testides 〈ℤ, •〉 nelja grupi aksioomi vastu (kus • tähistab standardset korrutamist).

Esimesed kaks aksioomi ilmselgelt kehtivad. Lisaks, korrutamise korral võib element 1 toimida ühikelemendina. Iga täisarv x, korrutatuna 1-ga, annab tulemuseks x. Siiski, 〈ℤ, •〉 ei vasta pööratavuse tingimusele. See tähendab, et iga x puhul ℤ-s ei ole unikaalset elementi y ℤ-s, nii et x • y = 1.

Näiteks, eeldame, et x = 22. Milline y väärtus hulgast ℤ, korrutatuna x-ga, annaks ühikelemendi 1? Väärtus 1/22 toimiks, kuid see ei ole hulgas ℤ. Tegelikult tekib see probleem iga täisarvu x puhul, välja arvatud väärtuste 1 ja -1 puhul (kus y peaks olema vastavalt 1 ja -1).
Kui me lubaksime oma hulgale tegelikke arve, siis meie probleemid suuresti kaoksid. Iga elemendi x puhul hulgas annab korrutamine 1/x tulemuseks 1. Kuna murdarvud kuuluvad tegelike arvude hulka, leidub iga tegeliku arvu jaoks pöördarv. Erandiks on null, kuna ükskõik milline korrutamine nulliga ei anna kunagi tulemuseks ühikelementi 1. Seega, nullist erinevate tegelike arvude hulk, varustatuna korrutamisega, on tõepoolest rühm.

Mõned rühmad vastavad viiendale üldisele tingimusele, mida tuntakse **kommutatiivsuse tingimusena**. See tingimus on järgmine:

* Eeldame rühma G hulgaga **S** ja binaarse operaatoriga ◌. Eeldame, et a ja b on elemendid hulgast **S**. Kui kehtib, et a ◌ b = b ◌ a mis tahes kahe elemendi a ja b puhul hulgast **S**, siis G vastab kommutatiivsuse tingimusele.

Iga rühm, mis vastab kommutatiivsuse tingimusele, on tuntud kui **kommutatiivne rühm** või **Abeli rühm** (pärast Niels Henrik Abeli). On lihtne kontrollida, et nii tegelike arvude hulk liitmise kui ka täisarvude hulk liitmise suhtes on Abeli rühmad. Täisarvude hulk korrutamise suhtes ei ole üldse rühm, seega ei saa see olla Abeli rühm. Seevastu nullist erinevate tegelike arvude hulk korrutamise suhtes on samuti Abeli rühm.

Te peaksite tähele panema kahte olulist notatsiooni konventsiooni. Esiteks, märgid “+” või “x” kasutatakse sageli rühmaoperatsioonide sümboliseerimiseks, isegi kui elemendid ei ole tegelikult arvud. Sellistel juhtudel ei tohiks neid märke tõlgendada standardse aritmeetilise liitmise või korrutamisena. Selle asemel on need operatsioonid, millel on ainult abstraktne sarnasus nende aritmeetiliste operatsioonidega.

Kui te ei viita spetsiifiliselt aritmeetilisele liitmisele või korrutamisele, on lihtsam kasutada rühmaoperatsioonide jaoks sümboleid nagu ◌ ja ◊, kuna neil ei ole väga kultuuriliselt juurdunud tähendusi.

Teiseks, samal põhjusel, miks “+” ja “x” kasutatakse sageli mittearitmeetiliste operatsioonide näitamiseks, sümboliseeritakse rühmade ühikelemente sageli “0” ja “1” abil, isegi kui nende rühmade elemendid ei ole arvud. Kui te ei viita rühma ühikelemendile, mis on arvudega, on lihtsam kasutada neutraalsemat sümbolit nagu “e” ühikelemendi näitamiseks.

Paljud erinevad ja väga olulised väärtuste hulgad matemaatikas, mis on varustatud teatud binaarsete operatsioonidega, on rühmad. Krüptograafilised rakendused töötavad siiski ainult täisarvude hulkadega või vähemalt elementidega, mida kirjeldatakse täisarvudena, st arvuteooria valdkonnas. Seetõttu ei kasutata krüptograafilistes rakendustes tegelike arvude hulki peale täisarvude.

Lõpetuseks toome näite elementidest, mida saab "kirjeldada täisarvudena", kuigi need ei ole täisarvud. Hea näide on elliptiliste kõverate punktid. Kuigi ükski punkt elliptilisel kõveral ei ole selgelt täisarv, kirjeldatakse sellist punkti tõepoolest kahe täisarvuga.

Elliptilised kõverad on näiteks Bitcoini jaoks hädavajalikud. Iga standardne Bitcoini privaat- ja avaliku võtme paar valitakse punktide hulgast, mida määratleb järgmine elliptiline kõver: x<sup>3</sup> + 7 = y<sup>2</sup> mod 2<sup>256</sup> – 232 – 29 – 28 – 27 – 26 - 24 - 1 (suurim algarv, mis on väiksem kui 2<sup>256</sup>). x-koordinaat on privaatvõti ja y-koordinaat on teie avalik võti.
Bitcoinis tehingute tegemine hõlmab tavaliselt väljundite lukustamist ühele või mitmele avalikule võtmele mingil viisil. Nende tehingute väärtust saab seejärel avada, luues digitaalseid allkirju vastavate privaatvõtmetega.

## Tsüklilised grupid
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Üks oluline eristus, mida saame teha, on **lõpliku** ja **lõpmatute gruppide** vahel. Esimesel on lõplik arv elemente, samas kui teisel on lõpmatu arv elemente. Mis tahes lõpliku grupi elementide arvu nimetatakse **grupi järjeks**. Kõik praktiline krüptograafia, mis hõlmab gruppide kasutamist, toetub lõplikele (arvuteoreetilistele) gruppidele.

Avaliku võtme krüptograafias on eriti oluline teatud klass lõplikke Abeli gruppe, mida tuntakse tsükliliste gruppide nime all. Tsükliliste gruppide mõistmiseks peame kõigepealt mõistma grupielemendi eksponenteerimise kontseptsiooni.

Eeldagem, et grupil G on grupioperatsioon ◌ ja et a on G elemendiks. Avaldist a<sup>n</sup> tuleks seega tõlgendada kui elementi a, mis on kombineeritud iseendaga kokku n – 1 korda. Näiteks a<sup>2</sup> tähendab a ◌ a, a<sup>3</sup> tähendab a ◌ a ◌ a ja nii edasi. (Märkus: eksponenteerimine siin ei pruugi tingimata olla eksponenteerimine standardse aritmeetika mõttes.)

Pöördugem näite poole. Eeldagem, et G = 〈ℤ mod 7,+〉 ja et meie väärtus a võrdub 4-ga. Sel juhul a<sup>2</sup> = [4 + 4 mod 7] = [8 mod 7] = 1 mod 7. Alternatiivselt a<sup>4</sup> esindaks [4 + 4 + 4 + 4 mod 7] = [16 mod 7] = 2 mod 7.

Mõnedel Abeli gruppidel on üks või mitu elementi, mis võivad kõiki teisi grupielemente tekitada jätkuva eksponenteerimise teel. Neid elemente nimetatakse **generaatoriteks** või **primitiivelementideks**.

Üks selliste gruppide oluline klass on 〈ℤ* mod N, •〉, kus N on algarv. Notatsioon ℤ* tähendab siin, et grupp sisaldab kõiki nullist erinevaid positiivseid täisarve, mis on väiksemad kui N. Sellisel grupil on seega alati N – 1 elementi.

Vaatleme näiteks G = 〈ℤ* mod 11, •〉. Sellel grupil on järgmised elemendid: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. Selle grupi järk on 10 (mis tõepoolest võrdub 11 – 1-ga).

Uurime elemendi 2 eksponenteerimist sellest grupist. Arvutused kuni 2<sup>12</sup>-ni on allpool näidatud. Pange tähele, et võrrandi vasakul küljel viitab eksponent grupielemendi eksponenteerimisele. Meie konkreetse näite puhul hõlmab see tõepoolest aritmeetilist eksponenteerimist võrrandi paremal küljel (kuid see oleks võinud hõlmata näiteks ka liitmist). Selgituseks olen välja kirjutanud korduva operatsiooni, mitte eksponendi vormi paremal küljel.

* 2<sup>1</sup> = 2 mod 11
* 2<sup>2</sup> = 2 · 2 mod 11 = 4 mod 11
* 2<sup>3</sup> = 2 · 2 · 2 mod 11 = 8 mod 11
* 2<sup>4</sup> = 2 · 2 · 2 · 2 mod 11 = 16 mod 11 = 5 mod 11
* 2<sup>5</sup> = 2 · 2 · 2 · 2 · 2 mod 11 = 32 mod 11 = 10 mod 11
* 2<sup>6</sup> = 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 64 mod 11 = 9 mod 11
* 2<sup>7</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 128 mod 11 = 7 mod 11
* 2<sup>8</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 256 mod 11 = 3 mod 11
* 2<sup>9</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 512 mod 11 = 6 mod 11
* 2<sup>10</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 1024 mod 11 = 1 mod 11
* 2<sup>11</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 2048 mod 11 = 2 mod 11
* 2<sup>12</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 4096 mod 11 = 4 mod 11

Kui vaadata hoolikalt, võib märgata, et elementi 2 astendades läbitakse kõik 〈ℤ* mod 11, •〉 elemendid järgmises järjekorras: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Pärast 2<sup>10</sup> jätkub elementi 2 astendamine, läbides kõik elemendid uuesti ja samas järjekorras. Seega on element 2 generaator 〈ℤ* mod 11, •〉-s.

Kuigi 〈ℤ* mod 11, •〉-l on mitu generaatorit, ei ole kõik selle grupi elemendid generaatorid. Võtame näiteks elemendi 3. Esimese 10 astendamise läbimine, ilma tülikaid arvutusi näitamata, annab järgmised tulemused:

* 3<sup>1</sup> = 3 mod 11
* 3<sup>2</sup> = 9 mod 11
* 3<sup>3</sup> = 5 mod 11
* 3<sup>4</sup> = 4 mod 11
* 3<sup>5</sup> = 1 mod 11
* 3<sup>6</sup> = 3 mod 11
* 3<sup>7</sup> = 9 mod 11
* 3<sup>8</sup> = 5 mod 11
* 3<sup>9</sup> = 4 mod 11
* 3<sup>10</sup> = 1 mod 11

Selle asemel, et läbida kõik väärtused 〈ℤ* mod 11, •〉, toob elemendi 3 astendamine esile ainult osa neist väärtustest: 3, 9, 5, 4 ja 1. Pärast viiendat astendamist hakkavad need väärtused korduma.

Nüüd saame defineerida **tsüklilise grupi** kui iga grupi, millel on vähemalt üks generaator. See tähendab, et on olemas vähemalt üks grupi element, millest saab teisi grupi elemente toota astendamise teel.

Võib-olla olete meie eespool toodud näites märganud, et nii 2<sup>10</sup> kui ka 3<sup>10</sup> võrdub 1 mod 11. Tegelikult, kuigi me ei tee arvutusi, toob grupi 〈ℤ* mod 11, •〉 mis tahes elemendi astendamine 10-ga esile 1 mod 11. Miks see nii on?

See on oluline küsimus, kuid vastuse leidmine nõuab tööd.

Alustuseks eeldame kahte positiivset täisarvu a ja N. Üks oluline teoreem arvuteoorias väidab, et a-l on korrutise pöördarv modulo N (st täisarv b nii, et a • b = 1 mod N), kui ja ainult siis, kui a ja N suurim ühistegur võrdub 1-ga. See tähendab, kui a ja N on teineteisega võõrad.

Seega, mis tahes täisarvude grupis, mis on varustatud korrutamisega modulo N, on komplektis ainult N-ga võõrad väiksemad täisarvud. Me võime seda komplekti tähistada ℤ<sup>c</sup> mod N.

Näiteks, eeldame, et N on 10. Ainult täisarvud 1, 3, 7 ja 9 on 10-ga võõrad. Seega komplekt ℤ<sup>c</sup> mod 10 sisaldab ainult {1, 3, 7, 9}. Te ei saa luua gruppi täisarvude korrutamisega modulo 10 kasutades muid täisarve vahemikus 1 kuni 10. Selle konkreetse grupi puhul on pöördarvudeks paarid 1 ja 9 ning 3 ja 7.

Juhtumil, kui N ise on algarv, on kõik täisarvud 1-st kuni N – 1 N-ga võõrad. Selline grupp on seega järjekorras N – 1. Kasutades meie varasemat tähistust, ℤ<sup>c</sup> mod N võrdub ℤ* mod N, kui N on algarv. Grupp, mille me oma varasemas näites valisime, 〈ℤ* mod 11, •〉, on selle klassi gruppide konkreetne näide.

Järgmisena, funktsioon φ(N) arvutab võõraste arvu kuni numbrini N ja on tuntud kui **Euleri fi-funktsioon**.<sup>[1](#footnote1)</sup> **Euleri teoreemi** kohaselt, kui kaks täisarvu a ja N on võõrad, kehtib järgnev:

* a<sup>φ(N)</sup> mod N = 1 mod N
Sellel on oluline tähendus rühmade klassi 〈ℤ* mod N, •〉 jaoks, kus N on algarv. Nende rühmade puhul esindab rühmaelemendi eksponenteerimine aritmeetilist eksponenteerimist. See tähendab, et a<sup>φ(N)</sup> mod N esindab aritmeetilist operatsiooni a<sup>φ(N)</sup> mod N. Kuna iga element a nendes korrutusrühmades on algarvuga N võõras, tähendab see, et a<sup>φ(N)</sup> mod N = a<sup>N – 1</sup> mod N = 1 mod N. 
Euleri teoreem on tõesti oluline tulemus. Alustuseks tähendab see, et kõik elemendid rühmas 〈ℤ* mod N, •〉 saavad eksponenteerimisel läbida ainult arvu väärtusi, mis jagunevad N – 1-ga. Näiteks 〈ℤ* mod 11, •〉 puhul tähendab see, et iga element saab läbida ainult 2, 5 või 10 elementi. Rühma väärtused, mille kaudu iga element eksponenteerimisel läbib, on tuntud kui **elemendi järk**. Element, mille järk on võrdne rühma järjega, on generaator.

Lisaks tähendab Euleri teoreem, et me saame alati teada tulemuse a<sup>N – 1</sup> mod N mis tahes rühma 〈ℤ* mod N, •〉 jaoks, kus N on algarv. See kehtib sõltumata sellest, kui keerulised tegelikud arvutused võivad olla.

Näiteks, kui meie rühm on ℤ* mod 160,481,182 (kus 160,481,182 on tõepoolest algarv), teame, et kõik täisarvud 1 kuni 160,481,181 peavad olema selle rühma elemendid ja et φ(n) = 160,481,181. Kuigi me ei saa teha kõiki arvutusetappe, teame, et avaldised nagu 514<sup>160,481,181</sup>, 2,005<sup>160,481,181</sup> ja 256,212<sup>160,481,181</sup> peavad kõik võrduma 1 mod 160,481,182.

## Väljad
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Rühm on abstraktse algebra põhiline algebraaline struktuur, kuid on palju rohkem. Ainus teine algebraaline struktuur, millega peate tuttav olema, on välja struktuur, eriti lõpliku välja struktuur. Seda tüüpi algebraaline struktuur on krüptograafias sageli kasutusel, näiteks Advanced Encryption Standardis. Viimane on peamine sümmeetriline krüpteerimisskeem, millega te praktikas kokku puutute.

Väli on tuletatud rühma mõistest. Konkreetselt on **väli** elementide kogum **S**, mis on varustatud kahe binaarse operaatoriga ◌ ja ◊, mis vastab järgmistele tingimustele:

1. Kogum **S**, mis on varustatud ◌-ga, on Abeli rühm.
2. Kogum **S**, mis on varustatud ◊-ga, on Abeli rühm "nullist erinevate" elementide jaoks.
3. Kogum **S**, mis on varustatud kahe operaatoriga, vastab nn distributiivsele tingimusele: Eeldame, et a, b ja c on **S** elementidest. Siis **S**, mis on varustatud kahe operaatoriga, vastab distributiivsele omadusele, kui a ◌ (b ◊ c) = a ◌ b ◊ a ◌ c.
Pange tähele, et nagu gruppide puhul, on välja definitsioon väga abstraktne. See ei tee väiteid elementide tüüpide kohta **S**-is ega operatsioonide ◌ ja ◊ kohta. See lihtsalt väidab, et väli on iga elementide kogum kahe operatsiooniga, mille puhul kehtivad kolm ülaltoodud tingimust. (Teises Abeli grupis olevat "null" elementi saab abstraktselt tõlgendada.)
Niisiis, mis võiks olla välja näide? Hea näide on hulk ℤ mod 7 ehk {0,1,…,7}, mis on defineeritud standardse liitmise (asendades ◌ ülal) ja standardse korrutamise (asendades ◊ ülal) alusel.

Esiteks, ℤ mod 7 vastab tingimusele olemaks Abeli grupp liitmise osas ja see vastab tingimusele olemaks Abeli grupp korrutamise osas, kui arvestada ainult nullist erinevaid elemente. Teiseks, hulga ja kahe operaatori kombinatsioon vastab distributiivse tingimuse nõuetele.

On didaktiliselt kasulik uurida neid väiteid, kasutades mõningaid konkreetseid väärtusi. Võtame katseväärtusteks 5, 2 ja 3, mõned juhuslikult valitud elemendid hulgast ℤ mod 7, et uurida välja 〈ℤ mod 7, +, •〉. Me kasutame neid kolme väärtust järjekorras, nagu on vajalik konkreetsete tingimuste uurimiseks.

Uurigem esmalt, kas ℤ mod 7 koos liitmisega on Abeli grupp.

1. Sulgemise tingimus: Võtame meie väärtusteks 5 ja 2. Sel juhul on [5 + 2] mod 7 = 7 mod 7 = 0. See on tõepoolest ℤ mod 7 element, nii et tulemus on kooskõlas sulgemise tingimusega.
2. Assotsiatiivsuse tingimus: Võtame meie väärtusteks 5, 2 ja 3. Sel juhul on [(5 + 2) + 3] mod 7 = [5 + (2 + 3)] mod 7 = 10 mod 7 = 3. See on kooskõlas assotsiatiivsuse tingimusega.
3. Identiteedi tingimus: Võtame meie väärtuseks 5. Sel juhul on [5 + 0] mod 7 = [0 + 5] mod 7 = 5. Nii et 0 tundub olevat liitmise identiteedielement.
4. Inversi tingimus: Kaaluge 5 inversi. Peab kehtima, et [5 + d] mod 7 = 0, mingi väärtuse d jaoks. Sel juhul on ℤ mod 7-st ainulaadne väärtus, mis vastab sellele tingimusele, 2.
5. Kommutatiivsuse tingimus: Võtame meie väärtusteks 5 ja 3. Sel juhul on [5 + 3] mod 7 = [3 + 5] mod 7 = 1. See on kooskõlas kommutatiivsuse tingimusega.

Hulk ℤ mod 7 koos liitmisega tundub selgelt olevat Abeli grupp. Uurigem nüüd, kas ℤ mod 7 koos korrutamisega on Abeli grupp kõigi nullist erinevate elementide jaoks.

1. Sulgemise tingimus: Võtame meie väärtusteks 5 ja 2. Sel juhul on [5 • 2] mod 7 = 10 mod 7 = 3. See on samuti ℤ mod 7 element, nii et tulemus on kooskõlas sulgemise tingimusega.
2. Assotsiatiivsuse tingimus: Võtame väärtusteks 5, 2 ja 3. Sel juhul [(5 • 2) • 3] mod 7 = [5 • (2 • 3)] mod 7 = 30 mod 7 = 2. See vastab assotsiatiivsuse tingimusele.
3. Ühikelemendi tingimus: Võtame väärtuseks 5. Sel juhul [5 • 1] mod 7 = [1 • 5] mod 7 = 5. Seega tundub, et 1 on korrutamise ühikelement.
4. Pöördelemendi tingimus: Kaalume 5 pöördelementi. Peab kehtima, et [5 • d] mod 7 = 1, mingi väärtuse d korral. Ainulaadne väärtus ℤ mod 7-st, mis vastab sellele tingimusele, on 3. See vastab pöördelemendi tingimusele.
5. Kommutatiivsuse tingimus: Võtame väärtusteks 5 ja 3. Sel juhul [5 • 3] mod 7 = [3 • 5] mod 7 = 15 mod 7 = 1. See vastab kommutatiivsuse tingimusele.

Komplekt ℤ mod 7 tundub selgelt vastavat Abeli grupi reeglitele, kui seda kasutatakse koos kas liitmise või korrutamisega nullist erinevate elementide puhul.

Lõpuks tundub, et see komplekt koos mõlema tehtega vastab distributiivsuse tingimusele. Võtame väärtusteks 5, 2 ja 3. Näeme, et [5 • (2 + 3)] mod 7 = [5 • 2 + 5 • 3] mod 7 = 25 mod 7 = 4.

Oleme nüüd näinud, et ℤ mod 7 koos liitmise ja korrutamisega vastab lõpliku välja aksioomidele, kui testida konkreetsete väärtustega. Muidugi saame näidata, et see kehtib üldiselt, kuid ei tee seda siin.

Oluline eristus on kahe tüüpi väljade vahel: lõplikud ja lõpmatud väljad.

**Lõpmatu välja** puhul on tegemist väljaga, kus komplekt **S** on lõpmatult suur. Reaalarvude komplekt ℝ koos liitmise ja korrutamisega on näide lõpmatust väljast. **Lõplik välja**, tuntud ka kui **Galois' välja**, on välja, kus komplekt **S** on lõplik. Meie eespool toodud näide 〈ℤ mod 7, +, •〉 on lõplik välja.

Krüptograafias oleme peamiselt huvitatud lõplikest väljadest. Üldiselt saab näidata, et lõplik välja eksisteerib mingi elementide komplekti **S** jaoks, kui ja ainult siis, kui selles on p<sup>m</sup> elementi, kus p on algarv ja m positiivne täisarv, mis on suurem või võrdne ühega. Teisisõnu, kui mingi komplekti **S** järjekord on algarv (p<sup>m</sup>, kus m = 1) või mingi algarvu aste (p<sup>m</sup>, kus m > 1), siis leiate kaks tehet ◌ ja ◊, nii et välja tingimused on täidetud.

Kui mõnes lõplikus väljas on algarv elemente, siis nimetatakse seda **algväljaks**. Kui lõpliku välja elementide arv on algarvu aste, siis nimetatakse välja **laiendväljaks**. Krüptograafias oleme huvitatud nii alg- kui ka laiendväljadest.<sup>[2](#footnote2)</sup>
Krüptograafia peamised põhihuvid on sellised, kus kõikide täisarvude hulk moduleeritakse mingi algarvuga ja operaatoriteks on standardne liitmine ja korrutamine. See lõplike väljade klass hõlmaks ℤ mod 2, ℤ mod 3, ℤ mod 5, ℤ mod 7, ℤ mod 11, ℤ mod 13 ja nii edasi. Mis tahes algarvu välja ℤ mod p puhul on välja täisarvude hulk järgmine: {0,1,….,p – 2, p – 1}.
Krüptograafias huvitavad meid ka laiendatud väljad, eriti need väljad, millel on 2<sup>m</sup> elementi, kus m > 1. Selliseid lõplikke välju kasutatakse näiteks Rijndaeli šifris, mis on Advanced Encryption Standardi aluseks. Kuigi algarvu väljad on suhteliselt intuitiivsed, ei pruugi need baas 2 laiendatud väljad olla arusaadavad kõigile, kes ei ole tuttavad abstraktse algebraga.

Alustuseks on tõesti tõsi, et igale täisarvude hulgale, millel on 2<sup>m</sup> elementi, saab määrata kaks operaatorit, mis muudaksid nende kombinatsiooni väljaks (niikaua kui m on positiivne täisarv). Kuid lihtsalt seetõttu, et välja olemasolu on võimalik, ei tähenda see tingimata, et see on kergesti avastatav või eriti praktiline teatud rakendustes.

Selgub, et krüptograafias eriti rakendatavad 2<sup>m</sup> laiendatud väljad on need, mis on määratletud eriliste polünoomiliste avaldiste hulkade üle, mitte mingi täisarvude hulga põhjal.

Näiteks, kui me sooviksime laiendatud välja, millel on 2<sup>3</sup> (st 8) elementi hulgas. Kuigi võib olla palju erinevaid hulki, mida saab sellise suurusega väljade jaoks kasutada, hõlmab üks selline hulk kõiki unikaalseid polünoome kujul a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub>, kus iga koefitsient a<sub>i</sub> on kas 0 või 1. Seega hõlmab see hulk **S** järgmisi elemente:

1. 0: Juhtum, kus a<sub>2</sub> = 0, a<sub>1</sub> = 0 ja a<sub>0</sub> = 0.
2. 1: Juhtum, kus a<sub>2</sub> = 0, a<sub>1</sub> = 0 ja a<sub>0</sub> = 1.
3. x: Juhtum, kus a<sub>2</sub> = 0, a<sub>1</sub> = 1 ja a<sub>0</sub> = 0.
4. x + 1: Juhtum, kus a<sub>2</sub> = 0, a<sub>1</sub> = 1 ja a<sub>0</sub> = 1.
5. x<sup>2</sup>: Juhtum, kus a<sub>2</sub>= 1, a<sub>1</sub> = 0 ja a<sub>0</sub> = 0.
6. x<sup>2</sup> + 1: Juhtum, kus a<sub>2</sub> = 1, a<sub>1</sub> = 0 ja a<sub>0</sub> = 1.
7. x<sup>2</sup> + x: Juhtum, kus a<sub>2</sub> = 1, a<sub>1</sub> = 1 ja a<sub>0</sub> = 0. 8. x<sup>2</sup> + x + 1: Juhtum, kus a<sub>2</sub> = 1, a<sub>1</sub> = 1 ja a<sub>0</sub> = 1.

Seega **S** oleks hulk {0,1,x,x + 1, x<sup>2</sup>,x<sup>2</sup> + 1, x<sup>2</sup> + x, x<sup>2</sup> + x + 1}. Millised kaks tehet saab määratleda selle elementide hulga üle, et tagada nende kombinatsioon on väli?

Esimese tehte hulgal S (◌) saab määratleda kui standardset polünoomide liitmist modulo 2. Kõik, mida pead tegema, on liita polünoomid nagu tavaliselt ja seejärel rakendada modulo 2 iga saadud polünoomi koefitsiendile. Siin on mõned näited:

* [(x<sup>2</sup>) + (x<sup>2</sup> + x + 1)] mod 2 = [2x<sup>2</sup> + x + 1] mod 2 = x + 1
* [(x<sup>2</sup> + x) + (x)] mod 2 = [x<sup>2</sup> + 2x] mod 2 = x<sup>2</sup>
* [(x + 1) + (x<sup>2</sup> + x + 1)] mod 2 = [x<sup>2</sup> + 2x + 2] mod 2 = x<sup>2</sup> + 1

Teine tehe hulgal S (◌), mis on vajalik välja loomiseks, on keerulisem. See on mingi korrutamine, kuid mitte standardne aritmeetiline korrutamine. Selle asemel pead sa iga elementi vaatama kui vektorit ja mõistma tehet kui nende kahe vektori korrutamist modulo redutseerimatu polünoomiga.

Pöördugem esmalt redutseerimatu polünoomi idee poole. **Redutseerimatu polünoom** on selline, mida ei saa faktoriseerida (nagu ka algarvu ei saa faktoriseerida komponentideks peale 1 ja algarvu enda). Meie eesmärgil huvitavad meid polünoomid, mis on redutseerimatud kõigi täisarvude suhtes. (Pane tähele, et teatud polünoome võib olla võimalik faktoriseerida, näiteks kasutades reaalarve või kompleksarve, isegi kui sa ei saa neid faktoriseerida kasutades täisarve.)

Näiteks kaaluge polünoomi x<sup>2</sup> - 3x + 2. Seda saab ümber kirjutada kui (x – 1)(x – 2). Seega, see ei ole redutseerimatu. Nüüd kaaluge polünoomi x<sup>2</sup> + 1. Kasutades ainult täisarve, ei ole võimalik seda avaldist edasi faktoriseerida. Seega, see on redutseerimatu polünoom täisarvude suhtes.
Järgmisena pöördume vektorite korrutamise kontseptsiooni juurde. Me ei süvene sellesse teemasse põhjalikult, vaid peate mõistma üht põhireeglit: Iga vektori jagamine on võimalik, kuni jagataval on kõrgem või võrdne aste jagajaga. Kui jagataval on madalam aste kui jagajal, siis ei saa jagatavat enam jagajaga jagada.
Näiteks, kaaluge avaldist x<sup>6</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. See väheneb edasi, kuna jagatava aste, 6, on kõrgem kui jagaja aste, 5. Nüüd kaaluge avaldist x<sup>5</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. See väheneb samuti edasi, kuna jagatava aste, 5, ja jagaja aste, 5, on võrdsed.

Siiski, nüüd kaaluge avaldist x<sup>4</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. See ei vähene edasi, kuna jagatava aste, 4, on madalam kui jagaja aste, 5.

Selle teabe põhjal oleme nüüd valmis leidma meie teise operatsiooni komplektile {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Olen juba öelnud, et teist operatsiooni tuleks mõista kui vektorite korrutamist modulo mingi redutseerimatu polünoomi järgi. See redutseerimatu polünoom peaks tagama, et teine operatsioon määratleb Abeli grupi üle **S** ja on kooskõlas distributiivse tingimusega. Milline peaks see redutseerimatu polünoom olema?

Kuna kõik komplekti vektorid on astmega 2 või madalamad, peaks redutseerimatu polünoom olema astmega 3. Kui komplektis olevate kahe vektori korrutamine annab polünoomi astmega 3 või kõrgema, teame, et modulo polünoom astmega 3 annab alati polünoomi astmega 2 või madalama. See on nii, kuna iga polünoom astmega 3 või kõrgem on alati jagatav polünoomiga astmega 3. Lisaks peab jagajana toimiv polünoom olema redutseerimatu.

Selgub, et on mitmeid redutseerimatuid polünoome astmega 3, mida me võiksime kasutada meie jagajana. Iga selline polünoom määratleb erineva välja koos meie komplektiga S ja liitmisega modulo 2. See tähendab, et teil on mitu võimalust, kui kasutate laiendatud välju 2<sup>m</sup> krüptograafias.

Meie näite puhul eeldame, et valime polünoomi x<sup>3</sup> + x + 1. See on tõepoolest redutseerimatu, kuna te ei saa seda teguriteks jaotada täisarvude abil. Lisaks tagab see, et kahe elemendi korrutamine annab alati polünoomi astmega 2 või vähem.
Töötame läbi näite teisest operatsioonist, kasutades jagajana polünoomi x<sup>3</sup> + x + 1, et illustreerida, kuidas see toimib. Oletame, et korrutate elemendid x<sup>2</sup> + 1 ja x<sup>2</sup> + x meie hulgas **S**. Seejärel peame arvutama avaldise [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1. Seda saab lihtsustada järgmiselt:
* [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 =
* [x<sup>2</sup> • x<sup>2</sup> + x<sup>2</sup> • x + 1 • x<sup>2</sup> + 1 • x] mod x<sup>3</sup> + x + 1 = 
* [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1
    
Teame, et [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1 saab vähendada, kuna jagataval on kõrgem aste (4) kui jagajal (3).

Alustuseks võite näha, et avaldis x<sup>3</sup> + x + 1 läheb x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x sisse kokku x korda. Seda saate kontrollida, korrutades x<sup>3</sup> + x + 1 x-ga, mis on x<sup>4</sup> + x<sup>2</sup> + x. Kuna viimane termin on sama astmega kui jagatav, nimelt 4, teame, et see töötab. Jagamise jäägi saate arvutada x järgi järgmiselt:

* [(x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x) – (x<sup>4</sup> + x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 = 
* [x<sup>3</sup>] mod x<sup>3</sup> + x + 1 =
* x<sup>3</sup>

Niisiis, pärast x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x jagamist x<sup>3</sup> + x + 1-ga kokku x korda, on meil jääk x<sup>3</sup>. Kas seda saab veel jagada x<sup>3</sup> + x + 1-ga?
Intuitiivselt võib tunduda ahvatlev öelda, et x<sup>3</sup> ei saa enam jagada x<sup>3</sup> + x + 1-ga, kuna viimane termin tundub suurem. Siiski, meenutage meie varasemat arutelu vektorite jagamise üle. Niikaua kui jagataval on kraad, mis on suurem või võrdne jagajaga, saab avaldist edasi lihtsustada. Konkreetselt, avaldis x<sup>3</sup> + x + 1 mahub x<sup>3</sup>-sse täpselt 1 kord. Jääk arvutatakse järgmiselt:
[(x<sup>3</sup>) – (x<sup>3</sup> + x + 1)] mod x<sup>3</sup> + x + 1 = 
[x + 1] mod x<sup>3</sup> + x + 1 = 
x + 1

Võib-olla mõtlete, miks (x<sup>3</sup>) – (x<sup>3</sup> + x + 1) võrdub x + 1-ga, mitte – x – 1-ga. Pea meeles, et meie välja esimene toiming on defineeritud modulo 2 järgi. Seega, kahe vektori lahutamine annab täpselt sama tulemuse kui kahe vektori liitmine.

Kokkuvõtteks x<sup>2</sup> + 1 ja x<sup>2</sup> + x korrutamisest: Kui te korrutate neid kahte terminit, saate 4. astme polünoomi, x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x, mida tuleb vähendada modulo x<sup>3</sup> + x + 1 järgi. 4. astme polünoom jaguneb x<sup>3</sup> + x + 1-ga täpselt x + 1 korda. Jääk pärast x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x jagamist x<sup>3</sup> + x + 1-ga täpselt x + 1 korda on x + 1. See on tõepoolest element meie komplektis {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Miks võiksid laiendatud väljad baasiga 2 üle polünoomide komplektide, nagu eespool toodud näites, olla kasulikud krüptograafias? Põhjus on selles, et selliste komplektide polünoomide koefitsiente, kas 0 või 1, saab vaadelda kui binaarstringide elemente kindla pikkusega. Komplekt **S** meie näites eespool, näiteks, võiks selle asemel vaadelda kui komplekti S, mis hõlmab kõiki 3-pikkusega binaarstringe (000 kuni 111). Seega saab **S**-il toiminguid kasutada ka nende binaarstringidega toimingute sooritamiseks ja sama pikkusega binaarstringi tootmiseks.

## Abstraktne algebra praktikas
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>
Hoolimata ametlikust keelekasutusest ja arutelu abstraktsusest, ei tohiks rühma kontseptsioon olla liiga keeruline mõistmiseks. See on lihtsalt elementide kogum koos binaarse operatsiooniga, kus selle binaarse operatsiooni sooritamine nendel elementidel vastab neljale üldisele tingimusele. Abelia rühmal on lihtsalt üks lisatingimus, mida nimetatakse kommutatiivsuseks. Tsükliline rühm omakorda on eriline liik Abelia rühmast, nimelt selline, millel on generaator. Väli on lihtsalt keerukam konstruktsioon baasilisest rühma mõistest.

Kuid kui olete praktiliselt meelestatud inimene, võite sel hetkel mõelda: Kes hoolib? Kas teadmine, et mingi elementide kogum koos operaatoriga on rühm, või isegi Abelia või tsükliline rühm, omab mingit reaalset tähtsust? Kas teadmine, et midagi on väli?

Liiga palju detaile sisse laskmata on vastus "jah". Rühmad loodi esmakordselt 19. sajandil prantsuse matemaatiku Evariste Galois poolt. Ta kasutas neid järelduste tegemiseks polünoomvõrrandite lahendamise kohta, mille aste oli suurem kui viis.

Sellest ajast alates on rühma kontseptsioon aidanud valgust heita paljudele probleemidele matemaatikas ja mujal. Näiteks füüsik Murray-Gellman suutis nende põhjal ennustada osakese olemasolu enne, kui see tegelikult eksperimentides täheldati.<sup>[3](#footnote3)</sup> Teise näitena kasutavad keemikud rühmateooriat molekulide kuju klassifitseerimiseks. Matemaatikud on isegi kasutanud rühma kontseptsiooni järelduste tegemiseks midagi nii konkreetset kui tapeet!

Põhimõtteliselt näitab, et elementide kogum koos mõne operaatoriga on rühm, tähendab, et kirjeldate midagi, millel on teatud sümmeetria. Mitte sümmeetria tavapärases mõttes, vaid abstraktsemas vormis. Ja see võib pakkuda olulist sissevaadet konkreetsetesse süsteemidesse ja probleemidesse. Abstraktsest algebrast pärit keerukamad mõisted annavad meile lisateavet.

Kõige tähtsamalt näete arvuteoreetiliste rühmade ja väljade tähtsust praktikas nende rakendamise kaudu krüptograafias, eriti avaliku võtme krüptograafias. Oleme juba arutanud väljade puhul, näiteks kuidas laiendatud välju kasutatakse Rijndaeli šifris. Me töötame selle näite läbi *5. peatükis*.

## Edasine uurimine
<chapterId>ab51038d-82bd-5c5d-a759-276cfbf7fbce</chapterId>

Abstraktse algebraga edasiseks aruteluks soovitaksin Socratica suurepärast videosarja abstraktse algebraga. Eriti soovitaksin järgmisi videoid: “Mis on abstraktne algebra?”, “Rühma definitsioon (laiendatud)”, “Ringi definitsioon (laiendatud)” ja “Välja definitsioon (laiendatud)”. Need neli videot annavad teile lisateavet palju eelnevalt arutatud teemade kohta. (Me ei arutanud ringe, kuid väli on lihtsalt eriline tüüp ringist.)

Kaasaegse arvuteooria edasiseks aruteluks võite konsulteerida paljude edasijõudnute aruteludega krüptograafia kohta. Pakuksin soovitustena Jonathan Katz'i ja Yehuda Lindell'i raamatut "Introduction to Modern Cryptography" või Christof Paar'i ja Jan Pelzl'i raamatut "Understanding Cryptography" edasiseks aruteluks.<sup>[5](#footnote5)</sup>

### Märkused
[^1]: Funktsioon toimib järgnevalt. Iga täisarv N on võimalik faktoriseerida algarvude korrutiseks. Eeldame, et konkreetne N on faktoriseeritud järgmiselt: p<sub>1</sub><sup>e1</sup> • p<sub>2</sub><sup>e2</sup> …. • p<sub>m</sub><sup>em</sup>, kus kõik p-d on algarvud ja kõik e-d on täisarvud, mis on suuremad või võrdsed 1-ga. Siis φ(N) = Sum<sub>i=1…m</sub>[p<sub>i</sub><sup>ei</sup> – p<sub>i</sub><sup>ei - 1</sup>] [^1].
[^2]: Laiendatud väljad muutuvad väga vastuintuitiivseks. Erinevalt täisarvude elementidest, on neil polünoomide hulgad. Lisaks viiakse kõik toimingud läbi modulo mõne redutseerimatu polünoomi suhtes [^2].

[^3]: Vaata [YouTube Video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be) [^3].

[^4]: Socratica, [Abstraktne Algebra](https://www.socratica.com/subject/abstract-algebra) [^4].

[^5]: Katz ja Lindell, *Sissejuhatus Kaasaegsesse Krüptograafiasse*, 2. väljaanne, 2015 (CRC Press: Boca Raton, FL). Paar ja Pelzl, *Krüptograafia Mõistmine*, 2010 (Springer-Verlag: Berliin) [^5].


# Sümmeetriline Krüptograafia
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

Üks kahest peamisest krüptograafia harust on sümmeetriline krüptograafia. See hõlmab krüpteerimisskeeme samuti kui skeeme, mis on seotud autentimise ja terviklikkusega. Kuni 1970ndateni oleks kogu krüptograafia koosnenud sümmeetrilistest krüpteerimisskeemidest.

Peamine arutelu algab sümmeetriliste krüpteerimisskeemide vaatlemisega ja teeb olulise eristuse voogšifrite ja plokšifrite vahel. Seejärel pöördume sõnumi autentimiskoodide poole, mis on skeemid sõnumi terviklikkuse ja autentsuse tagamiseks. Lõpuks uurime, kuidas sümmeetrilisi krüpteerimisskeeme ja sõnumi autentimiskoode saab kombineerida turvalise suhtluse tagamiseks.

See peatükk arutleb möödaminnes erinevate sümmeetriliste krüptograafiliste skeemide üle praktikas. Järgmine peatükk pakub üksikasjalikku ekspositsiooni krüpteerimisest praktikas voogšifri ja plokšifriga, nimelt vastavalt RC4 ja AES.

Enne sümmeetrilise krüptograafia arutelu alustamist tahan lühidalt teha mõned märkused Alice'i ja Bobi illustratsioonide kohta selles ja järgnevates peatükkides.


## Alice ja Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Krüptograafia põhimõtete illustreerimisel toetuvad inimesed sageli näidetele, mis hõlmavad Alice'i ja Bobi. Mina teen seda samuti.

Eriti kui olete krüptograafiaga uus, on oluline mõista, et need Alice'i ja Bobi näited on mõeldud ainult krüptograafiliste põhimõtete ja konstruktsioonide illustreerimiseks lihtsustatud keskkonnas. Põhimõtted ja konstruktsioonid on siiski kohaldatavad palju laiemas reaalelu kontekstis.

Järgnevalt on viis peamist punkti, mida tuleks meeles pidada krüptograafias Alice'i ja Bobi näidete kohta:

1. Neid saab hõlpsasti tõlkida näideteks teiste tegelastega, nagu ettevõtted või valitsusorganisatsioonid.
2. Neid saab hõlpsasti laiendada, et hõlmata kolme või enamat tegelast.
3. Näidetes on Bob ja Alice tavaliselt aktiivsed osalejad iga sõnumi loomisel ja krüptograafiliste skeemide rakendamisel sellele sõnumile. Kuid tegelikkuses on elektrooniline suhtlus suuresti automatiseeritud. Näiteks, kui külastate veebisaiti, mis kasutab transpordikihi turvalisust, siis krüptograafia on tavaliselt täielikult teie arvuti ja veebiserveri poolt hallatud. 4. Elektroonilise suhtluse kontekstis on "sõnumid", mis suhtluskanali kaudu saadetakse, tavaliselt TCP/IP paketid. Need võivad kuuluda e-kirjale, Facebooki sõnumile, telefonivestlusele, failiedastusele, veebisaidile, tarkvara üleslaadimisele jne. Need ei ole sõnumid traditsioonilises mõttes. Siiski lihtsustavad krüptograafid sageli seda reaalsust, öeldes näiteks, et sõnum on e-kiri.
5. Näited keskenduvad tavaliselt elektroonilisele suhtlusele, kuid neid saab laiendada ka traditsioonilistele suhtlusvormidele, nagu kirjad.

## Sümmeetrilised krüpteerimisskeemid
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Me võime lahtiselt defineerida **sümmeetrilise krüpteerimisskeemi** kui igat krüptograafilist skeemi, mis sisaldab kolme algoritmi:

1. **Võtme genereerimise algoritm**, mis genereerib privaatvõtme.
2. **Krüpteerimisalgoritm**, mis võtab sisendiks privaatvõtme ja lihtteksti ning väljastab krüptoteksti.
3. **Dekrüpteerimisalgoritm**, mis võtab sisendiks privaatvõtme ja krüptoteksti ning väljastab algse lihtteksti.

Tavaliselt pakub krüpteerimisskeem—olgu see siis sümmeetriline või asümmeetriline—krüpteerimise malli, mis põhineb põhialgoritmil, mitte täpsel spetsifikatsioonil.

Näiteks, kaaluge Salsa20, mis on sümmeetriline krüpteerimisskeem. Seda saab kasutada nii 128- kui ka 256-bitiste võtmepikkustega. Võtmepikkuse valik mõjutab algoritmi mõningaid väiksemaid detaile (täpsemalt algoritmi läbimiste arvu).

Kuid ei öelda, et Salsa20 kasutamine 128-bitise võtmega on erinev krüpteerimisskeem kui Salsa20 kasutamine 256-bitise võtmega. Põhialgoritm jääb samaks. Ainult siis, kui põhialgoritm muutub, räägiksime tõesti kahest erinevast krüpteerimisskeemist.

Sümmeetrilised krüpteerimisskeemid on tavaliselt kasulikud kahe liiki juhtudel: (1) Need, kus kaks või enam agenti suhtlevad kaugelt ja soovivad hoida oma suhtluse sisu saladuses; ja (2) need, kus üks agent soovib hoida sõnumi sisu saladuses ajas.

Olukorda (1) näete allpool *Joonisel 1*. Bob soovib saata sõnumi M Alicele kaugelt, kuid ei soovi, et teised saaksid seda sõnumit lugeda.

Bob esmalt krüpteerib sõnumi M privaatvõtmega K. Seejärel saadab ta krüptoteksti C Alicele. Kui Alice on krüptoteksti kätte saanud, saab ta selle dekrüpteerida võtmega K ja lugeda lihtteksti. Hea krüpteerimisskeemi korral ei tohiks ükski ründaja, kes krüptoteksti C pealt kuulab, suuta sõnumi M kohta midagi olulist teada saada.

Olukorda (2) näete allpool *Joonisel 2*. Bob soovib takistada teistel teatud teabe vaatamist. Tüüpiline olukord võib olla see, kus Bob on töötaja, kes salvestab tundlikke andmeid oma arvutisse, mida ei tohiks lugeda ei välised isikud ega tema kolleegid.
Bob krüpteerib sõnumi M ajal T<sub>0</sub> võtmega K, et toota krüptoteksti C. Ajal T<sub>1</sub> vajab ta sõnumit uuesti ja dekrüpteerib krüptoteksti C võtmega K. Iga ründaja, kes võis vahepeal krüptotekstiga C kokku puutuda, ei oleks pidanud suutma sellest midagi olulist sõnumi M kohta järeldada.
*Joonis 1: Saladus ruumis*

![Joonis 1: Saladus ruumis](assets/Figure4-1.webp "Joonis 1: Saladus ruumis")

*Joonis 2: Saladus ajas*

![Joonis 2: Saladus ajas](assets/Figure4-2.webp "Joonis 2: Saladus ajas")

## Näide: Nihkešiffer
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

2. peatükis kohtusime nihkešifriga, mis on väga lihtsa sümmeetrilise krüpteerimisskeemi näide. Vaatame seda siin uuesti.

Eeldame sõnastikku *D*, mis seostab kõik inglise tähestiku tähed järjekorras numbrite komplektiga {0,1,2…,25}. Eeldame võimalike sõnumite komplekti **M**. Nihkešiffer on siis krüpteerimisskeem, mis on määratletud järgmiselt:

- Vali juhuslikult võti k võimalike võtmete komplektist **K**, kus **K** = {0,1,2,…,25}
- Krüpteeri sõnum m є **M**, järgmiselt:
    - Eralda m selle üksikuteks tähtedeks m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Teisenda iga m<sub>i</sub> numbriks vastavalt *D*-le
    - Iga m<sub>i</sub> jaoks, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Teisenda iga c<sub>i</sub> täheks vastavalt *D*-le
    - Seejärel ühenda c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub>, et saada krüptotekst c
- Dekrüpteeri krüptotekst c järgmiselt:
    - Teisenda iga c<sub>i</sub> numberiks vastavalt *D*-le
    - Iga c<sub>i</sub> jaoks, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    - Teisenda iga m<sub>i</sub> täheks vastavalt *D*-le
    - Seejärel ühenda m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub>, et saada algne sõnum m

Nihkešifferi puhul on tegemist sümmeetrilise krüpteerimisskeemiga, kuna nii krüpteerimis- kui ka dekrüpteerimisprotsessiks kasutatakse sama võtit. Näiteks, kui soovite krüpteerida sõnumit “DOG” kasutades nihkešifrit ja olete juhuslikult valinud võtmeks "24", siis selle võtmega krüpteerimine annaks tulemuseks “BME”. Algse sõnumi taastamiseks on ainus viis kasutada sama võtit, "24", dekrüpteerimisprotsessis.
See Shifti šiffer on näide **monoalfabeetilisest asendusšifrist**: krüpteerimisskeemist, kus šifriteksti tähestik on fikseeritud (st kasutatakse ainult ühte tähestikku). Eeldades, et dekrüpteerimisalgoritm on deterministlik, võib asendusšifri tekstis olev iga sümbol maksimaalselt vastata ühele sümbolile algtekstis.
Kuni 1700ndateni tuginesid krüpteerimise rakendused suuresti monoalfabeetilistele asendusšifritele, kuigi tihti olid need palju keerukamad kui Shifti šiffer. Näiteks võisite juhuslikult valida tähestikust iga algteksti tähe jaoks ühe tähe, tingimusel, et iga täht esineb šifriteksti tähestikus ainult üks kord. See tähendab, et teil oleks faktoriaal 26 võimalikku privaatvõtit, mis oli ennearvutiajastul tohutu.

Pange tähele, et krüptograafias tuleb terminiga **šiffer** sageli kokku puutuda. Olge teadlik, et sellel terminil on mitu tähendust. Tegelikult tean ma vähemalt viit erinevat tähendust, mida see termin krüptograafias omab.

Mõnel juhul viitab see krüpteerimisskeemile, nagu seda tehakse Shifti šifris ja monoalfabeetilises asendusšifris. Siiski võib termin viidata ka spetsiifiliselt krüpteerimisalgoritmile, privaatvõtmele või lihtsalt mis tahes sellise krüpteerimisskeemi šifritekstile.

Lõpuks võib termin šiffer viidata ka põhialgoritmile, millest saab konstrueerida krüptograafilisi skeeme. Need võivad hõlmata erinevaid krüpteerimisalgoritme, aga ka teisi krüptograafilisi skeeme. See termini tähendus muutub oluliseks plokkšifrite kontekstis (vt allpool jaotist „Plokkšifrid“).

Võite samuti kohata termineid **krüpteerima** või **dekrüpteerima**. Need terminid on lihtsalt sünonüümid krüpteerimisele ja dekrüpteerimisele.

## Jõuga ründamine ja Kerckhoffi põhimõte
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Shifti šiffer on väga ebaturvaline sümmeetriline krüpteerimisskeem, vähemalt tänapäeva maailmas.<sup>[1](#footnote1)</sup> Ründaja võiks lihtsalt proovida dekrüpteerida mis tahes šifriteksti kõigi 26 võimaliku võtmega, et näha, milline tulemus mõistlik tundub. Sellist tüüpi rünnakut, kus ründaja lihtsalt tsüklitab võtmete vahel, et näha, mis toimib, tuntakse kui **jõuga ründamist** või **amendavat võtmeotsingut**.

Et mis tahes krüpteerimisskeem vastaks minimaalsele turvalisuse mõistele, peab sellel olema võtmeruum, mis on nii suur, et jõuga rünnakud on teostamatud. Kõik tänapäeva krüpteerimisskeemid vastavad sellele standardile. Seda tuntakse kui **piisava võtmeruumi põhimõtet**. Sarnane põhimõte kehtib tavaliselt ka erinevat tüüpi krüptograafilistes skeemides.

Et saada ettekujutus tänapäeva krüpteerimisskeemide tohutust võtmeruumi suurusest, eeldagem, et fail on krüpteeritud 128-bitise võtmega, kasutades täiustatud krüpteerimisstandardit. See tähendab, et ründajal on komplekt 2<sup>128</sup> võtit, mille hulgast ta peab jõuga rünnaku jaoks läbi käima. 0,78% eduvõimalusega sellise strateegiaga peaks ründaja läbi käima umbes 2,65 x 10<sup>36</sup> võtit.
Eeldame optimistlikult, et ründaja suudab sekundis proovida 10 kvadriljonit võtit (st 10<sup>16</sup> võtit sekundis). Selleks, et testida 0,78% kõikidest võtmeruumi võtmetest, peaks tema rünnak kestma 2,65 x 10<sup>20</sup> sekundit. See on umbes 8,4 triljonit aastat. Seega isegi äärmiselt võimsa vastase jõuga rünnak ei ole realistlik kaasaegse 128-bitise krüpteerimisskeemi puhul. See on piisava võtmeruumi põhimõtte mängumaal.

Kas nihkešiffer on turvalisem, kui ründaja ei tea krüpteerimisalgoritmi? Võib-olla, kuid mitte palju.

Igal juhul eeldab kaasaegne krüptograafia alati, et mis tahes sümmeetrilise krüpteerimisskeemi turvalisus sõltub ainult privaatvõtme saladuses hoidmisest. Eeldatakse, et ründaja teab kõiki teisi detaile, sealhulgas sõnumiruumi, võtmeruumi, šifreeritud teksti ruumi, võtme valiku algoritmi, krüpteerimisalgoritmi ja dekrüpteerimisalgoritmi.

Mõte, et sümmeetrilise krüpteerimisskeemi turvalisus võib sõltuda ainult privaatvõtme saladusest, on tuntud kui **Kerckhoffs’ põhimõte**.

Nagu Kerckhoffs algselt kavandas, kehtib põhimõte ainult sümmeetriliste krüpteerimisskeemide kohta. Üldisem versioon põhimõttest kehtib aga kõigi teiste tänapäeva krüptograafiliste skeemide kohta: ükski krüptograafiline skeem ei tohi oma turvalisuse tagamiseks nõuda disaini saladuses hoidmist; saladus võib laieneda ainult mõnele teabe stringile, tavaliselt privaatvõtmele.

Kerckhoffs’ põhimõte on kaasaegse krüptograafia jaoks keskne neljal põhjusel.<sup>[2](#footnote2)</sup> Esiteks, konkreetsete rakenduste jaoks on krüptograafilisi skeeme piiratud arv. Näiteks, enamik kaasaegseid sümmeetrilise krüpteerimise rakendusi kasutab Rijndaeli šifrit. Seega on teie saladus skeemi disaini osas väga piiratud. Siiski on Rijndaeli šifri privaatvõtme saladuses hoidmises palju rohkem paindlikkust.

Teiseks, teabe stringi asendamine on lihtsam kui terve krüptograafilise skeemi asendamine. Eeldame, et ettevõtte kõigil töötajatel on sama krüpteerimistarkvara ja iga kahe töötaja vahel on privaatvõti konfidentsiaalseks suhtluseks. Võtmete kompromiteerimine on selles stsenaariumis tülikas, kuid vähemalt saaks ettevõte selliste turvaintsidentide korral tarkvara alles hoida. Kui ettevõte sõltuks skeemi saladusest, siis iga sellise saladuse rikkumine nõuaks kogu tarkvara asendamist.

Kolmandaks, Kerckhoffs’ põhimõte võimaldab krüptograafiliste skeemide standardiseerimist ja ühilduvust kasutajate vahel. Sellel on tohutud eelised efektiivsuse osas. Näiteks on raske ette kujutada, kuidas miljonid inimesed saaksid iga päev turvaliselt ühenduda Google'i veebiserveritega, kui see turvalisus nõuaks krüptograafiliste skeemide saladuses hoidmist.

Neljandaks, Kerckhoffi põhimõte võimaldab krüptograafiliste skeemide avalikku kontrolli. Selline kontroll on absoluutselt vajalik turvaliste krüptograafiliste skeemide saavutamiseks. Näiteks sümmeetrilise krüptograafia peamine põhialgoritm, Rijndaeli šiffer, oli konkursi tulemus, mille korraldas Riiklik Standardite ja Tehnoloogia Instituut aastatel 1997 kuni 2000.

Iga süsteem, mis üritab saavutada **turvalisust varjatuse abil**, on selline, mis sõltub oma disaini ja/või rakenduse detailide saladuses hoidmisest. Krüptograafias oleks see spetsiifiliselt süsteem, mis sõltub krüptograafilise skeemi disaini detailide saladuses hoidmisest. Seega on turvalisus varjatuse abil otseses vastuolus Kerckhoffs’ põhimõttega.
Avatus, mis tugevdab kvaliteeti ja turvalisust, ulatub digitaalses maailmas kaugemale kui ainult krüptograafia. Vabad ja avatud lähtekoodiga Linuxi distributsioonid, nagu näiteks Debian, omavad üldiselt mitmeid eeliseid võrreldes nende Windowsi ja MacOSi vastastega privaatsuse, stabiilsuse, turvalisuse ja paindlikkuse osas. Kuigi sellel võib olla mitmeid põhjuseid, on kõige olulisem põhimõte tõenäoliselt, nagu Eric Raymond oma kuulsas essees "The Cathedral and the Bazaar" sõnastas, et "[p]iisavalt paljude silmapaaride korral on kõik vead pealiskaudsed." Just see rahva tarkuse tüüpi põhimõte andis Linuxile selle kõige olulisema edu.
Krüptograafilist skeemi ei saa kunagi üheselt öelda, et see on "turvaline" või "mitteturvaline". Selle asemel on krüptograafilistel skeemidel erinevad turvalisuse mõisted. Iga **krüptograafilise turvalisuse definitsioon** peab määrama (1) turvalisuse eesmärgid, samuti (2) ründaja võimekused. Krüptograafiliste skeemide analüüsimine ühe või mitme konkreetse turvalisuse mõiste alusel annab ülevaate nende rakendustest ja piirangutest.

Kuigi me ei süvene kõikidesse krüptograafilise turvalisuse erinevate mõistete detailidesse, peaksite teadma, et kaks eeldust on kõigile kaasaegsetele krüptograafilise turvalisuse mõistetele ühised nii sümmeetriliste kui ka asümmeetriliste skeemide (ja mingil määral ka teiste krüptograafiliste primitiivide) puhul:

* Ründaja teadmised skeemi kohta vastavad Kerckhoffs’ põhimõttele.
* Ründaja ei saa skeemi vastu teostada teostatavat jõurünnakut. Eelkõige ei luba krüptograafilise turvalisuse ohumudelid isegi jõurünnakuid, kuna eeldatakse, et need ei ole asjakohased.

## Voogšifrid
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Sümmeetrilised krüpteerimisskeemid jagunevad tavaliselt kaheks tüübiks: voogšifrid ja plokšifrid. See eristus on siiski mõnevõrra problemaatiline, kuna inimesed kasutavad neid termineid ebaühtlaselt. Järgmistes jaotistes esitan ma eristuse viisil, mis minu arvates on parim. Peaksite siiski teadma, et paljud inimesed kasutavad neid termineid veidi teisiti, kui ma siin esitan.

Alustame voogšifridest. **Voogšifer** on sümmeetriline krüpteerimisskeem, kus krüpteerimine koosneb kahest sammust.

Esiteks, genereeritakse teksti pikkune string privaatvõtme abil. Seda stringi nimetatakse **võtmevooguks**.

Järgmisena kombineeritakse võtmevoog matemaatiliselt lähtetekstiga, et toota šifreeritud tekst. See kombinatsioon on tavaliselt XOR-operatsioon. Dekrüpteerimiseks võib lihtsalt operatsiooni ümber pöörata. (Märkus: A XOR B = B XOR A, juhul kui A ja B on bitijadad. Seega XOR-operatsiooni järjekord voogšifris tulemuse jaoks ei oma tähtsust. Seda omadust tuntakse kommutatiivsusena.)

Tüüpiline XOR voogšifer on kujutatud *joonisel 3*. Kõigepealt võtate privaatvõtme K ja kasutate seda võtmevoo genereerimiseks. Võtmevoog kombineeritakse seejärel lähtetekstiga XOR-operatsiooni abil, et toota šifreeritud tekst. Iga agent, kes saab šifreeritud teksti, saab selle hõlpsalt dekrüpteerida, kui tal on võti K. Kõik, mida ta peab tegema, on genereerida võtmevoog nii pikk kui šifreeritud tekst vastavalt skeemi määratud protseduurile ja teostada see XOR-operatsiooniga šifreeritud tekstiga.

*Joonis 3: XOR voogšifer*

![Joonis 3: XOR voogšifer](assets/Figure4-3.webp "Joonis 3: XOR voogšifer")
Olge teadlikud, et krüpteerimisskeem on tavaliselt mall krüpteerimiseks sama põhialgoritmiga, mitte täpne spetsifikatsioon. Laiendatult on voogšiffer tavaliselt krüpteerimise mall, milles saab kasutada erineva pikkusega võtmeid. Kuigi võtme pikkus võib mõjutada skeemi mõningaid väikseid detaile, ei mõjuta see selle põhivormi.

Nihešiffer on näide väga lihtsast ja ebaturvalisest voogšifrist. Kasutades ühte tähte (privaatvõtit), saate toota tähtede jada sõnumi pikkusega (võtmestik). See võtmestik ühendatakse seejärel algtekstiga modulo operatsiooni kaudu, et toota šifreeritud tekst. (Seda modulo operatsiooni saab lihtsustada XOR operatsiooniks, kui esitada tähed bittidena).

Teine kuulus voogšifri näide on **Vigenère'i šiffer**, mille arendas täielikult välja Blaise de Vigenère 16. sajandi lõpus (kuigi teised olid teinud palju eeltööd). See on **polüalfabeetilise asendusšifri** näide: krüpteerimisskeem, kus šifreeritud teksti tähestik algteksti sümboli jaoks muutub sõltuvalt selle positsioonist tekstis. Erinevalt monoalfabeetilisest asendusšifrist, võivad šifreeritud teksti sümbolid olla seotud rohkem kui ühe algteksti sümboliga.

Krüpteerimise populaarsuse kasvades renessansiaegses Euroopas kasvas ka **krüptoanalüüs**—see tähendab šifreeritud tekstide murdmist—eriti kasutades **sagedusanalüüsi**. Viimane kasutab meie keele statistilisi regulaarsusi šifreeritud tekstide murdmiseks ja avastati juba üheksandal sajandil Araabia õpetlaste poolt. See on tehnika, mis töötab eriti hästi pikemate tekstidega. Ja isegi kõige keerukamad monoalfabeetilised asendusšifrid ei olnud enam piisavad sagedusanalüüsi vastu 1700ndatel Euroopas, eriti sõjaväe- ja turvaseadetes. Kuna Vigenère'i šiffer pakkus olulist turvalisuse edasiminekut, muutus see sel perioodil populaarseks ja oli laialt levinud 1700ndate lõpuks.

Mitteametlikult öeldes töötab krüpteerimisskeem järgmiselt:

1.	Valige mitmetäheline sõna privaatvõtmeks
2.	Iga sõnumi puhul rakendage nihešifrit iga sõnumi tähele, kasutades vastavat tähte võtmesõnas nihešifrina
3.	Kui olete võtmesõna läbi käinud, kuid ei ole veel täielikult šifreerinud algteksti, rakendage uuesti võtmesõna tähti nihešifrina vastavatele tähtedele teksti ülejäänud osas
4.	Jätkake seda protsessi, kuni kogu sõnum on šifreeritud

Näiteks, kui teie privaatvõti on GOLD ja soovite krüpteerida sõnumi "CRYPTOGRAPHY", siis toimiksite Vigenère'i šifri kohaselt järgmiselt:

- c<sub>0</sub>  = [(2 + 6) Mod 26] = 8 = I
- c<sub>1</sub>  = [(17 + 14) Mod 26] = 5 = F
- c<sub>2</sub>  = [(24 + 11) Mod 26] = 9 = J
- c<sub>3</sub>  = [(15 + 3) Mod 26] = 18 = S
- c<sub>4</sub>  = [(19 + 6) Mod 26] = 25 = Z
- c<sub>5</sub>  = [(14 + 14) Mod 26] = 2 = C
- c<sub>6</sub>  = [(6 + 11) Mod 26] = 17 = R
- c<sub>7</sub> = [(17 + 3) Mod 26] = 20 = U
- c<sub>8</sub> = [(0 + 6) Mod 26] = 6 = G
- c<sub>9</sub> = [(15 + 14) Mod 26] = 3 = D
- c<sub>10</sub> = [(7 + 11) Mod 26] = 18 = S
- c<sub>11</sub> = [(24 + 3) Mod 26] = 1 = B
- c = "IFJSZCRUGDSB"

Teine tuntud näide voošifrist on **ühekordne plokk**. Ühekordse ploki puhul loote lihtsalt juhuslikest bittidest koosneva stringi, mis on sama pikk kui selgetekstiline sõnum, ja toodate šifreeritud teksti XOR-operatsiooni kaudu. Seega on privaatvõti ja võtmevoog ühekordse ploki puhul võrdsed.

Kuigi nihkešifri ja Vigenère'i šifrid on tänapäeval väga ebaturvalised, on ühekordne plokk korrektselt kasutatuna väga turvaline. Ilmselt kõige kuulsam ühekordse ploki rakendus oli vähemalt kuni 1980. aastateni **Washingtoni-Moskva otseühendus**.<sup>[4](#footnote4)</sup>

Otseühendus on otsene suhtluskanal Washingtoni ja Moskva vahel kiireloomuliste küsimuste jaoks, mis paigaldati pärast Kuuba raketikriisi. Aastate jooksul on tehnoloogia muutunud. Praegu hõlmab see otseseid kiudoptilisi kaableid ning kahte satelliitlinki (redundantsi jaoks), mis võimaldavad e-kirju ja tekstisõnumeid. Link lõppeb mitmes kohas USA-s. Pentagon, Valge Maja ja Raven Rocki mägi on tuntud lõpp-punktid. Vastupidiselt levinud arvamusele ei ole otseühendus kunagi hõlmanud telefone.

Ühekordse ploki skeem töötas sisuliselt järgmiselt. Nii Washingtonil kui ka Moskval oli kaks juhuslike numbrite komplekti. Üks juhuslike numbrite komplekt, mille lõid venelased, puudutas sõnumite krüpteerimist ja dekrüpteerimist vene keeles. Teine juhuslike numbrite komplekt, mille lõid ameeriklased, puudutas sõnumite krüpteerimist ja dekrüpteerimist inglise keeles. Aeg-ajalt toimetati teisele poolele usaldusväärsete kullerite abil rohkem juhuslikke numbreid.

Washington ja Moskva suutsid seejärel kasutada neid juhuslikke numbreid ühekordsete plokkide loomiseks, et suhelda salaja. Iga kord, kui oli vaja suhelda, kasutati järgmist osa juhuslikest numbritest oma sõnumi jaoks.

Kuigi ühekordne plokk on väga turvaline, seisab see silmitsi oluliste praktiliste piirangutega: võti peab olema sama pikk kui sõnum ja ühekordse ploki ühtegi osa ei tohi uuesti kasutada. See tähendab, et peate jälgima, kus te ühekordses plokis parasjagu olete, hoidma tohutul hulgal bitte ja vahetama aeg-ajalt oma vastaspooltega juhuslikke bitte. Seetõttu ei kasutata ühekordset plokki praktikas sageli.

Selle asemel kasutatakse praktikas peamiselt **pseudosuvalisi voošifreid**. Salsa20 ja sellele tihedalt seotud variant ChaCha on tavaliselt kasutatavad pseudosuvalised voošifrid.

Nende pseudosuvaliste voošifrite puhul valite esmalt juhuslikult võtme K, mis on lühem kui selgetekst. Selline juhuslik võti K luuakse tavaliselt meie arvuti poolt ettearvamatute andmete põhjal, mida ta aja jooksul kogub, nagu näiteks võrgusõnumite vahel kuluv aeg, hiire liigutused jne.
See juhuslik võti K sisestatakse seejärel laiendusalgoritmi, mis loob pseudosuvalise võtmehulga, mis on sama pikk kui sõnum. Saate täpselt määrata, kui pikk peab võtmehulk olema (nt 500 bitti, 1000 bitti, 1200 bitti, 29 117 bitti jne).
Pseudosuvaline võtmehulk näib *nagu* see oleks valitud täiesti juhuslikult kõikide sama pikkusega stringide hulgast. Seega tundub krüpteerimine pseudosuvalise võtmehulgaga nagu see oleks tehtud ühekordse padjaga. Kuid see muidugi nii ei ole.

Kuna meie privaatvõti on lühem kui võtmehulk ja meie laiendusalgoritm peab olema deterministlik, et krüpteerimise/dekrüpteerimise protsess töötaks, ei saa iga sellise pikkusega võtmehulk olla meie laiendusoperatsiooni tulemus.

Oletame näiteks, et meie privaatvõtmel on pikkus 128 bitti ja et me saame selle sisestada laiendusalgoritmi, et luua palju pikem võtmehulk, öelgem 2500 bitti. Kuna meie laiendusalgoritm peab olema deterministlik, saab meie algoritm valida maksimaalselt 1/2<sup>128</sup> stringi pikkusega 2500 bitti. Seega sellist võtmehulka ei saaks kunagi täiesti juhuslikult valida kõikide sama pikkusega stringide hulgast.

Meie voogšifri definitsioonil on kaks aspekti: (1) võtmehulk, mis on sama pikk kui avatekst, genereeritakse privaatvõtme abil; ja (2) see võtmehulk ühendatakse avatekstiga, tavaliselt XOR-operatsiooni kaudu, et toota šifreeritud tekst.

Mõnikord määratlevad inimesed tingimust (1) rangemalt, väites, et võtmehulk peab kindlasti olema pseudosuvaline. See tähendab, et ei nihkešifrit ega ühekordset patja ei peetaks voogšifriteks.

Minu arvates annab tingimuse (1) laiem määratlus lihtsama viisi krüpteerimisskeemide korraldamiseks. Lisaks tähendab see, et me ei pea lõpetama konkreetse krüpteerimisskeemi nimetamist voogšifriks lihtsalt seetõttu, et saame teada, et see ei sõltu tegelikult pseudosuvalistest võtmehulkadest.

## Blokkšifrid
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Esimene viis, kuidas **blokkšifrit** üldiselt mõistetakse, on midagi primitiivsemat kui voogšiffer: Põhialgoritm, mis teostab pikkust säilitavat transformatsiooni sobiva pikkusega stringil võtme abil. Seda algoritmi saab kasutada krüpteerimisskeemide ja võib-olla ka teiste krüptograafiliste skeemide loomiseks.

Sageli võib blokkšiffer võtta sisendstringe erineva pikkusega, nagu 64, 128 või 256 bitti, samuti võtmeid erineva pikkusega, nagu 128, 192 või 256 bitti. Kuigi algoritmi mõned detailid võivad sõltuvalt neist muutujatest muutuda, ei muutu põhialgoritm. Kui see muutuks, räägiksime kahest erinevast blokkšifrist. Pange tähele, et põhialgoritmi terminoloogia kasutamine siin on sama mis krüpteerimisskeemide puhul.

Blokkšifri tööpõhimõtet saab näha allpool *Joonisel 4*. Sõnum M pikkusega L ja võti K on blokkšifri sisendid. See väljastab sõnumi M’ pikkusega L. Võti ei pea enamiku blokkšifrite puhul olema sama pikk kui M ja M’.

*Joonis 4: Blokkšiffer*

![Joonis 4: Blokkšiffer](assets/Figure4-4.webp "Joonis 4: Blokkšiffer")
Plokkšiffer iseenesest ei ole krüpteerimisskeem. Kuid plokkšifrit saab kasutada erinevate **töörežiimidega** erinevate krüpteerimisskeemide loomiseks. Töörežiim lisab plokkšifri väliseid lisatoiminguid.

Selle toimimise illustreerimiseks kujutage ette plokkšifrit (BC), mis nõuab 128-bitist sisendstringi ja 128-bitist privaatvõtit. Allpool olev joonis 5 näitab, kuidas seda plokkšifrit saab kasutada **elektroonilise koodiraamatu režiimiga** (**ECB režiim**) krüpteerimisskeemi loomiseks. (Paremal olevad kolm punkti näitavad, et seda mustrit saab vajadusel korrata).

*Joonis 5: Plokkšiffer ECB režiimiga*

![Joonis 5: Plokkšiffer ECB režiimiga](assets/Figure4-5.webp "Joonis 5: Plokkšiffer ECB režiimiga")

Elektroonilise koodiraamatu krüpteerimisprotsess plokkšifriga on järgmine. Vaadake, kas saate oma tavateksti sõnumi jagada 128-bitisteks plokkideks. Kui ei, siis lisage sõnumile **täidis**, et tulemus oleks 128-bitise ploki suurusega ühtlaselt jagatav. See on teie krüpteerimisprotsessis kasutatav andmed.

Nüüd jagage andmed 128-bitisteks juppideks (M<sub>1</sub>, M<sub>2</sub>, M<sub>3</sub> jne). Käitage iga 128-bitine jupp läbi plokkšifri koos teie 128-bitise võtmega, et toota 128-bitiseid krüptoteksti juppe (C<sub>1</sub>, C<sub>2</sub>, C<sub>3</sub> jne). Need jupid taasühendatuna moodustavad täieliku krüptoteksti.

Dekrüpteerimine on lihtsalt vastupidine protsess, kuigi saaja vajab mingit äratuntavat viisi, kuidas dekrüpteeritud andmetest eemaldada mis tahes täidis, et taastada algne tavateksti sõnum.

Kuigi suhteliselt lihtne, jääb plokkšiffer elektroonilise koodiraamatu režiimis turvalisusest puudu. See on seetõttu, et see viib **deterministliku krüpteerimiseni**. Iga kahe identse 128-bitise andmejada krüpteeritakse täpselt samal viisil. Seda teavet saab ära kasutada.

Selle asemel peaks iga plokkšifrist konstrueeritud krüpteerimisskeem olema **probabilistlik**: see tähendab, et mis tahes sõnumi M või mis tahes konkreetse M jupi krüpteerimine peaks üldiselt iga kord andma erineva tulemuse.<sup>[5](#footnote5)</sup>

**Šifriplokkide aheldamise režiim** (**CBC režiim**) on tõenäoliselt kõige tavalisem režiim, mida kasutatakse koos plokkšifriga. Kui see on õigesti tehtud, toodab kombinatsioon probabilistliku krüpteerimisskeemi. Selle töörežiimi kujutist näete allpool joonisel 6.

*Joonis 6: Plokkšiffer CBC režiimiga*

![Joonis 6: Plokkšiffer CBC režiimiga](assets/Figure4-6.webp "Joonis 6: Plokkšiffer CBC režiimiga")

Eeldame, et ploki suurus on jällegi 128 bitti. Seega alguses peate jälle veenduma, et teie algne tavateksti sõnum saab vajaliku täidise.

Seejärel teete esimese 128-bitise osa oma tavatekstist **algvektoriga** 128-bitist XOR-tehet. Tulemus pannakse plokkšifrisse, et toota esimese ploki jaoks krüptotekst. Teise 128-bitise ploki jaoks teete esmalt tavatekstiga XOR-tehet esimese ploki krüptotekstiga, enne kui panete selle plokkšifrisse. Jätkate seda protsessi, kuni olete krüpteerinud kogu oma tavateksti sõnumi.

Kui olete lõpetanud, saadate krüpteeritud sõnumi koos krüpteerimata algvektoriga saajale. Saaja peab teadma algvektorit, muidu ei saa ta krüptoteksti dekrüpteerida.
See konstruktsioon on palju turvalisem kui elektrooniline koodiraamat (electronic code book mode), kui seda õigesti kasutada. Esiteks peaksid tagama, et initsialiseerimisvektor oleks juhuslik või pseudorandomne jada. Lisaks peaksid iga kord, kui kasutad seda krüpteerimisskeemi, kasutama erinevat initsialiseerimisvektorit. 
Teisisõnu, sinu initsialiseerimisvektor peaks olema juhuslik või pseudorandomne nonce, kus **nonce** tähendab "number, mida kasutatakse ainult üks kord". Kui järgid seda tava, siis CBC režiim koos plokkšifriga tagab, et ükskõik millised kaks identset tekstiplokki krüpteeritakse iga kord erinevalt.

Lõpuks pöörame tähelepanu **väljundi tagasiside režiimile** (**OFB režiim**). Saad näha selle režiimi kujutist *Joonisel 7*.

*Joonis 7: Plokkšiffer OFB režiimis*

![Joonis 7: Plokkšiffer OFB režiimis](assets/Figure4-7.webp "Joonis 7: Plokkšiffer OFB režiimis")

OFB režiimis valitakse samuti initsialiseerimisvektor. Kuid siin, esimese ploki jaoks, sisestatakse initsialiseerimisvektor otse plokkšifrisse koos sinu võtmega. Saadud 128-bitised andmed käsitletakse seejärel võtmestriimina. See võtmestriim rakendatakse XOR operatsiooniga algtekstile, et toota ploki krüptotekst. Järgnevate plokkide jaoks kasutad eelmisest plokist saadud võtmestriimi sisendina plokkšifris ja kordad samme.

Kui vaatad hoolikalt, siis tegelikult on siin plokkšifrist OFB režiimis loodud voogšiffer. Sa genereerid 128-bitiseid võtmestriimi osi seni, kuni sul on algteksti pikkus (visates ära viimasest 128-bitisest võtmestriimi osast vajaduseta bitid). Seejärel rakendad XOR operatsiooni võtmestriimile koos oma algtekstiga, et saada krüptotekst.

Eelmises jaotises voogšifrite kohta mainisin, et võtmestriimi toodetakse privaatvõtme abil. Täpsemalt öeldes, see ei pea olema loodud ainult privaatvõtmega. Nagu näed OFB režiimis, toodetakse võtmestriim nii privaatvõtme kui ka initsialiseerimisvektori toel.

Pane tähele, et nagu CBC režiimis, on oluline valida pseudorandomne või juhuslik nonce initsialiseerimisvektoriks iga kord, kui kasutad plokkšifrit OFB režiimis. Vastasel juhul krüpteeritakse sama 128-bitine sõnumistring erinevates suhtlustes samal viisil. See on üks viis, kuidas luua probabilistlik krüpteerimine voogšifriga.

Mõned voogšifrid kasutavad võtmestriimi loomiseks ainult privaatvõtit. Nende voogšifrite puhul on oluline, et kasutaksid iga suhtlusjuhtumi jaoks juhuslikku nonce'i, et valida privaatvõti. Vastasel juhul on ka nende voogšifrite krüpteerimise tulemused deterministlikud, põhjustades turvaprobleeme.

Kõige populaarsem kaasaegne plokkšiffer on **Rijndaeli šiffer**. See oli võidukas töö viieteistkümnest esitlusest konkursil, mille korraldas Riiklik Standardite ja Tehnoloogia Instituut (NIST) aastatel 1997 kuni 2000, et asendada vanem krüpteerimisstandard, **andmekrüpteerimisstandard** (**DES**).
Rijndaeli šifferit saab kasutada erinevate spetsifikatsioonidega võtmepikkuste ja ploki suuruste jaoks, samuti erinevates töörežiimides. NISTi võistluse komitee võttis omaks piiratud versiooni Rijndaeli šifrist—nimelt sellise, mis nõuab 128-bitiseid ploki suurusi ja võtmepikkusi kas 128, 192 või 256 bitti—osana **arenenud krüpteerimisstandardist** (**AES**). See on tõepoolest peamine standard sümmeetrilise krüpteerimise rakendustele. See on nii turvaline, et isegi NSA on ilmselt nõus seda kasutama 256-bitiste võtmetega ülisalajaste dokumentide jaoks.<sup>[6](#footnote6)</sup>
AES plokkišiffer selgitatakse üksikasjalikult *5. peatükis*.

## Segaduse selgitamine
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Segadus plokišifrite ja voogšifrite eristamise vahel tekib, sest mõnikord mõistavad inimesed terminit plokišiffer kui viidet spetsiifiliselt *plokišiffrile plokkrežiimi krüpteerimisega*.

Kaalu eelmises jaotises mainitud ECB ja CBC režiime. Need nõuavad spetsiifiliselt, et krüpteerimiseks mõeldud andmed oleksid jagatavad ploki suurusega (mis tähendab, et võib-olla peate kasutama täitmist algsele sõnumile). Lisaks töödeldakse andmeid nendes režiimides ka otse plokišifri poolt (mitte ainult ei kombineerita seda plokišifri operatsiooni tulemusega nagu OFB režiimis).

Seega võib alternatiivselt määratleda **plokišifri** kui mis tahes krüpteerimisskeemi, mis töötab korraga fikseeritud pikkusega plokkidega sõnumist (kus iga plokk peab olema pikem kui bait, muidu see muutub voogšifriks). Nii krüpteerimiseks mõeldud andmed kui ka šifreeritud tekst peavad jagunema ühtlaselt selle ploki suurusega. Tavaliselt on ploki suurus 64, 128, 192 või 256 bitti pikk. Voogšiffer seevastu saab krüpteerida sõnumeid ühe biti või baidi kaupa korraga.

Selle spetsiifilisema arusaamaga plokišifrist võite tõepoolest väita, et kaasaegsed krüpteerimisskeemid on kas voog- või plokišifrid. Edaspidi kasutan terminit plokišiffer üldisemas mõttes, kui pole öeldud teisiti.

Eelmises jaotises toodud arutelu OFB režiimi kohta tõstatab veel ühe huvitava punkti. Mõned voogšifrid on ehitatud plokišifritest, nagu Rijndael OFB-ga. Mõned, nagu Salsa20 ja ChaCha, ei ole loodud plokišifritest. Viimaseid võiks nimetada **primitiivseteks voogšifriteks**. (Tegelikult ei ole selliste voogšifrite viitamiseks standardiseeritud terminit.)

Rääkides voogšifrite ja plokišifrite eelistest ja puudustest, võrreldakse tavaliselt primitiivseid voogšifreid plokišifritel põhinevate krüpteerimisskeemidega.

Kuigi voogšifri saab alati hõlpsasti konstrueerida plokišifrist, on tavaliselt väga raske ehitada mingit tüüpi konstruktsiooni plokkrežiimi krüpteerimisega (nagu CBC režiimiga) primitiivsest voogšifrist.

Sellest arutelust peaksid nüüd aru saama *Joonis 8*. See annab ülevaate sümmeetrilistest krüpteerimisskeemidest. Kasutame kolme liiki krüpteerimisskeeme: primitiivsed voogšifrid, plokišifri voogšifrid ja plokišifrid plokkrežiimis (diagrammil nimetatud ka "plokišifrid").

*Joonis 8: Ülevaade sümmeetrilistest krüpteerimisskeemidest*

![Joonis 8: Ülevaade sümmeetrilistest krüpteerimisskeemidest](assets/Figure4-8.webp "Joonis 8: Ülevaade sümmeetrilistest krüpteerimisskeemidest")

## Sõnumi autentimiskoodid
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>
Krüpteerimine on seotud saladuse hoidmisega. Kuid krüptograafia tegeleb ka laiemate teemadega, nagu sõnumi terviklikkus, autentsus ja mittetagasivõetavus. Niinimetatud **sõnumi autentimiskoodid** (MAC-id) on sümmeetrilise võtme krüptograafilised skeemid, mis toetavad autentsust ja terviklikkust suhtluses.

Miks on vaja midagi muud peale saladuse hoidmise suhtluses? Oletame, et Bob saadab Alicele sõnumi praktiliselt murdmatus krüpteeringus. Iga ründaja, kes selle sõnumi pealt kuulab, ei suuda saada olulist teavet selle sisu kohta. Siiski on ründajal vähemalt kaks muud rünnakuteed:

1. Ta võib pealt kuulata krüptoteksti, muuta selle sisu ja saata muudetud krüptoteksti edasi Alicele.
2. Ta võib blokeerida Bobi sõnumi täielikult ja saata oma loodud krüptoteksti.

Mõlemal juhul ei pruugi ründajal olla ülevaadet krüptotekstide (1) ja (2) sisust. Kuid ta võib siiski sel viisil tekitada olulist kahju. Siin muutuvad sõnumi autentimiskoodid oluliseks.

Sõnumi autentimiskoode määratletakse laialdaselt kui sümmeetrilisi krüptograafilisi skeeme kolme algoritmiga: võtme genereerimise algoritm, sildi genereerimise algoritm ja kontrollimise algoritm. Turvaline MAC tagab, et sildid on **eksistentsiaalselt võltsimiskindlad** igale ründajale – see tähendab, et nad ei suuda edukalt luua sõnumile silti, mis kontrollimisel kehtiks, kui neil pole privaatvõtit.

Bob ja Alice saavad kasutada MAC-i, et võidelda konkreetse sõnumi manipuleerimise vastu. Oletame hetkeks, et neid ei huvita saladuse hoidmine. Nad soovivad ainult tagada, et Alice'i poolt vastu võetud sõnum oli tõepoolest Bobilt ja seda ei muudetud mingil viisil.

Protsess on kujutatud *joonisel 9*. MAC-i kasutamiseks genereeriksid nad esmalt privaatvõtme K, mis on jagatud nende kahe vahel. Bob loob sõnumile sildi T, kasutades privaatvõtit K. Seejärel saadab ta sõnumi koos sõnumi sildiga Alicele. Ta saab seejärel kontrollida, et Bob tõepoolest tegi sildi, käivitades privaatvõtme, sõnumi ja sildi läbi kontrollimise algoritmi.

*Joonis 9: Sümmeetrilise krüpteerimise skeemide ülevaade*

![Joonis 9: Sümmeetrilise krüpteerimise skeemide ülevaade](assets/Figure4-9.webp "Joonis 9: Sümmeetrilise krüpteerimise skeemide ülevaade")

Tänu eksistentsiaalsele võltsimiskindlusele ei saa ründaja sõnumit M mingil viisil muuta ega luua oma sõnumit kehtiva sildiga. See kehtib isegi siis, kui ründaja jälgib paljusid Bobi ja Alice'i vahelisi sõnumeid, mis kasutavad sama privaatvõtit. Parimal juhul võiks ründaja takistada Alicel sõnumi M vastuvõtmist (probleem, mida krüptograafia ei saa lahendada).

MAC tagab, et sõnum loodi tegelikult Bobi poolt. See autentsus tähendab automaatselt sõnumi terviklikkust – see tähendab, kui Bob on loonud mingi sõnumi, siis ipso facto seda ei muudetud mingil viisil ründaja poolt. Seega edaspidi peaks iga autentsuse mure automaatselt tähendama muret terviklikkuse pärast.

Kuigi ma olen oma arutelus teinud vahet sõnumi autentsuse ja terviklikkuse vahel, on samuti tavaline kasutada neid termineid sünonüümidena. Need viitavad siis ideele sõnumitest, mis olid loodud konkreetse saatja poolt ja mida ei muudetud mingil viisil. Selles vaimus nimetatakse sõnumi autentimiskoode sageli ka **sõnumi terviklikkuse koodideks**.

## Authenticated encryption
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>
Tavaliselt soovite tagada nii suhtluse saladuslikkuse kui ka autentsuse, seetõttu kasutatakse tavaliselt koos krüpteerimisskeeme ja MAC-skeeme. 
**Autentitud krüpteerimisskeem** on skeem, mis ühendab krüpteerimise MAC-iga väga turvalisel viisil. Konkreetselt peab see vastama standarditele eksistentsiaalse võltsimise suhtes ning väga tugevale saladuse mõistele, nimelt sellisele, mis on vastupidav **valitudšifritekst-rünnakutele**.<sup>[7](#footnote7)</sup>

Selleks, et krüpteerimisskeem oleks vastupidav valitudšifritekst-rünnakutele, peab see vastama **mittemuudetavuse** standarditele: see tähendab, et iga ründaja poolt tehtud šifreeritud teksti muudatus peaks andma kas kehtetu šifreeritud teksti või sellise, mis dekrüpteerimisel annab algtekstiga mitteseotud tähendusega teksti.<sup>[8](#footnote8)</sup>

Kuna autentitud krüpteerimisskeem tagab, et ründaja loodud šifreeritud tekst on alati kehtetu (kuna silti ei verifitseerita), vastab see valitudšifritekst-rünnakutele vastupanu standarditele. Huvitaval kombel võib tõestada, et autentitud krüpteerimisskeemi saab alati luua eksistentsiaalselt võltsimiskindla MAC-i ja krüpteerimisskeemi kombinatsioonist, mis vastab vähem tugevale turvalisuse mõistele, tuntud kui **valitudtekst-rünnaku turvalisus**.

Me ei süvene kõikidesse autentitud krüpteerimisskeemide konstrueerimise detailidesse. Kuid on oluline teada kahte nende konstrueerimise detaili.

Esiteks, autentitud krüpteerimisskeem tegeleb esmalt krüpteerimisega ja seejärel loob sõnumisildi šifreeritud tekstil. Selgub, et teised lähenemised—nagu šifreeritud teksti ühendamine sildiga algtekstil, või esmalt sildi loomine ja seejärel nii algteksti kui ka sildi krüpteerimine—on turvalisuse mõttes ebakindlad. Lisaks on mõlemal toimingul oma eraldi juhuslikult valitud privaatvõti, vastasel juhul on teie turvalisus tõsiselt ohustatud.

Eelmainitud põhimõte kehtib üldisemalt: *alati tuleks kasutada erinevaid võtmeid, kui ühendate põhilisi krüptograafilisi skeeme*.

Autentitud krüpteerimisskeemi kujutatakse *joonisel 10*. Bob loob esmalt sõnumist M šifreeritud teksti C, kasutades juhuslikult valitud võtit K<sub>C</sub>. Seejärel loob ta sõnumisildi T, viies šifreeritud teksti ja teise juhuslikult valitud võtme K<sub>T</sub> läbi sildi genereerimise algoritmi. Nii šifreeritud tekst kui ka sõnumisilt saadetakse Alicele.

Alice kontrollib nüüd esmalt, kas silt on kehtiv, arvestades šifreeritud teksti C ja võtit K<sub>T</sub>. Kui see on kehtiv, saab ta seejärel sõnumi lahti krüpteerida, kasutades võtit K<sub>C</sub>. Ta on mitte ainult kindel väga tugevas saladuse mõistes nende suhtluses, vaid teab ka, et sõnumi lõi Bob.

*Joonis 10: Autentitud krüpteerimisskeem*

![Joonis 10: Autentitud krüpteerimisskeem](assets/Figure4-10.webp "Joonis 10: Autentitud krüpteerimisskeem")

Kuidas luuakse MAC-e? Kuigi MAC-e saab luua mitmel viisil, on üks levinud ja tõhus viis nende loomiseks krüptograafiliste räsifunktsioonide kaudu.

Tutvustame krüptograafilisi räsifunktsioone põhjalikumalt *peatükis 6*. Praegu piisab teadmiseks, et **räsifunktsioon** on tõhusalt arvutatav funktsioon, mis võtab sisendeid suvalise suurusega ja annab fikseeritud pikkusega väljundeid. Näiteks populaarne räsifunktsioon **SHA-256** (secure hash algorithm 256) genereerib alati 256-bitise väljundi sõltumata sisendi suurusest. Mõned räsifunktsioonid, nagu SHA-256, omavad kasulikke rakendusi krüptograafias.
Kõige levinum krüptograafilise räsifunktsiooniga loodud märgise tüüp on **hash-põhine sõnumi autentimiskood** (HMAC). Protsess on kujutatud *joonisel 11*. Üks osapool loob privaatvõtmest K kaks erinevat võtit, sisemise võtme K<sub>1</sub> ja välimise võtme K<sub>2</sub>. Seejärel räsistatakse koos sisemise võtmega kas tavaline tekst M või šifreeritud tekst C. Tulemus T' räsistatakse seejärel välimise võtmega, et toota sõnumi märgis T.
On olemas mitmeid räsifunktsioone, mida saab kasutada HMACi loomiseks. Kõige sagedamini kasutatav räsifunktsioon on SHA-256.

*Joonis 11: HMAC*

![Joonis 11: HMAC](assets/Figure4-11.webp "Joonis 11: HMAC")


## Turvalised suhtlussessioonid
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Eeldame, et kaks osapoolt on suhtlussessioonis, nii et nad saadavad mitu sõnumit edasi-tagasi.

Autentitud krüpteerimisskeem võimaldab sõnumi saajal kontrollida, kas see on loodud tema partneri poolt suhtlussessioonis (eeldusel, et privaatvõti ei ole lekkinud). See töötab ühe sõnumi puhul piisavalt hästi. Tavaliselt aga saadavad kaks osapoolt sõnumeid edasi-tagasi suhtlussessioonis. Ja selles olukorras jääb lihtne autentitud krüpteerimisskeem, nagu eelmises jaotises kirjeldatud, turvalisuse tagamisel lühikeseks.

Peamine põhjus on see, et autentitud krüpteerimisskeem ei anna mingit garantiid, et sõnum saadeti tegelikult ka agenti poolt, kes selle suhtlussessiooni jooksul lõi. Kaaluge järgmisi kolme ründevektorit:

1. **Kordus rünne**: Ründaja saadab uuesti šifreeritud teksti ja märgise, mille ta varasemalt kahe osapoole vahel pealt kuulas.
2. **Ümberjärjestamise rünne**: Ründaja pealtkuulab kaks sõnumit erinevatel aegadel ja saadab need saajale vastupidises järjekorras.
3. **Peegeldusrünne**: Ründaja jälgib sõnumit, mis saadeti A-lt B-le, ja saadab selle sõnumi ka A-le.

Kuigi ründajal pole šifreeritud teksti teadmisi ja ta ei saa luua võltsitud šifreeritud tekste, võivad ülaltoodud ründed siiski suhtluses olulist kahju tekitada.

Eeldame näiteks, et kahe osapoole vaheline konkreetne sõnum hõlmab finantsvahendite ülekannet. Kordusrünne võib vahendid teist korda üle kanda. Tavalisel autentitud krüpteerimisskeemil pole selliste rünnete vastu kaitset.

Õnneks saab neid ründetüüpe suhtlussessioonis hõlpsasti leevendada, kasutades **identifikaatoreid** ja **suhtelisi ajaindikaatoreid**.

Identifikaatoreid saab lisada tavalisele sõnumile enne krüpteerimist. See takistab igasuguseid peegeldusründeid. Suhteline ajaindikaator võib näiteks olla järjekorranumber konkreetse suhtlussessiooni jaoks. Iga osapool lisab sõnumile enne krüpteerimist järjekorranumbri, nii et saaja teab, millises järjekorras sõnumid saadeti. See kõrvaldab ümberjärjestamise rünnete võimaluse. Samuti kõrvaldab see kordusründed. Iga ründaja poolt hiljem saadetud sõnumil on vana järjekorranumber ja saaja teab, et sõnumit ei tohiks uuesti töödelda.

Turvaliste suhtlussessioonide toimimise illustreerimiseks eeldagem taas Alicit ja Bobi. Nad saadavad kokku neli sõnumit edasi-tagasi. Allpool *joonisel 11* näete, kuidas autentitud krüpteerimisskeem identifikaatorite ja järjekorranumbritega töötab.
Suhtlussessioon algab sellega, et Bob saadab Alice'ile krüptoteksti C<sub>0,B</sub> koos sõnumi märgisega T<sub>0,B</sub>. Krüptotekst sisaldab sõnumit, samuti identifikaatorit (BOB) ja järjekorranumbrit (0). Märgis T<sub>0,B</sub> on loodud kogu krüptoteksti põhjal. Nende järgnevas suhtluses järgivad Alice ja Bob seda protokolli, vajadusel välju uuendades.
*Joonis 12: Turvaline suhtlussessioon*

![Joonis 12: Turvaline suhtlussessioon](assets/Figure4-12.webp "Joonis 12: Turvaline suhtlussessioon")


## Märkused
<chapterId>b96d38dd-c9cb-56a7-8764-4af8526bc63f</chapterId>

[^1]: Seutoniuse järgi kasutas Julius Caesar oma sõjalises suhtluses nihkešifrit, mille püsiv võtmeväärtus oli 3. Seega A muutus alati D-ks, B alati E-ks, C alati F-ks jne. See konkreetne nihkešifri versioon on seetõttu saanud tuntuks kui **Caesari šiffer** (kuigi see ei ole tegelikult šiffer kaasaegses mõistes, kuna võtmeväärtus on püsiv). Caesari šiffer võis olla turvaline esimesel sajandil eKr, kui Rooma vaenlased olid krüpteerimisega väga vähe tuttavad. Kuid kaasaegses ajas ei oleks see kindlasti väga turvaline skeem [^1].

[^2]: Jonathan Katz ja Yehuda Lindell, *Sissejuhatus kaasaegsesse krüptograafiasse*, CRC Press (Boca Raton, FL: 2015), lk. 7f [^2].

[^3]: Eric Raymond, “Katedraal ja basaar,” ettekanne esitati Linux Kongressil, Würzburg, Saksamaa (27. mai 1997). On olemas mitu järgnevat versiooni ning ka raamat. Minu viited on raamatu leheküljelt 30: Eric Raymond, *Katedraal ja basaar: Mõtisklusi Linuxist ja avatud lähtekoodiga tarkvarast kogemata revolutsionääri poolt*, parandatud väljaanne. (2001), O’Reilly: Sebastopol, CA [^3].

[^4]: Crypto Museum, "Washington-Moskva otseühendus," 2013, saadaval aadressil [Crypto Museum](https://www.cryptomuseum.com/crypto/hotline/index.htm) [^4].

[^5]: Probabilistliku krüpteerimise tähtsust rõhutasid esmakordselt Shafi Goldwasser ja Silvio Micali, “Probabilistlik krüpteerimine,” *Journal of Co [^5].



# RC4 ja AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

Sel peatükis arutame üksikasju krüpteerimisskeemi kohta, mis kasutab kaasaegset primitiivset voogšifrit, RC4 (või "Rivest šiffer 4"), ja kaasaegset plokšifrit, AES. Kuigi RC4 šiffer on krüpteerimismeetodina ebasoosingusse langenud, on AES kaasaegse sümmeetrilise krüpteerimise standard. Need kaks näidet peaksid andma parema ettekujutuse, kuidas sümmeetriline krüpteerimine sisuliselt toimib.


## RC4 voogšiffer
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>
Selleks, et mõista, kuidas tänapäevased pseudorandom jadatsifrid töötavad, keskendun RC4 jadatsifri näitele. RC4 on pseudorandom jadatsifri, mida kasutati WEP ja WAP juhtmevaba ligipääsupunkti turvaprotokollides ning TLS-is. Kuna RC4-l on palju tõestatud nõrkusi, on see muutunud ebasoovitavaks. Tegelikult keelab Internet Engineering Task Force nüüd kõigis TLS-i juhtumites klientide ja serverirakenduste RC4 komplektide kasutamise.<sup>[3](#footnote3)</sup> Sellest hoolimata toimib see hästi näitena, et illustreerida, kuidas primitiivne jadatsifri töötab.
Alustuseks näitan, kuidas krüpteerida lihttekstsõnumit beebi RC4 tsifriga. Oletame, et meie lihttekstsõnum on “SOUP.” Krüpteerimine meie beebi RC4 tsifriga toimub siis neljas etapis.

### 1. samm

Esmalt defineeri massiiv S nii, et S[0] = 0 kuni S[7] = 7. Massiiv siin lihtsalt tähendab muudetavat väärtuste kogumit, mis on korraldatud indeksi järgi, mida mõnes programmeerimiskeeles nimetatakse ka listiks (nt Python). Sel juhul jookseb indeks 0-st 7-ni ja väärtused samuti 0-st 7-ni. Seega on S järgmine:

- S = [0,1,2,3,4,5,6,7]

Siin olevad väärtused ei ole ASCII numbrid, vaid 1 baiti stringide kümnendarvude esitused. Seega väärtus 2 võrdub 0000 0011. Massiivi S pikkus on seega 8 baiti.

### 2. samm

Teiseks, defineeri võtmemassiiv K pikkusega 8 baiti, valides võtme vahemikus 1 kuni 8 baiti (baitide murdosad pole lubatud). Kuna iga bait on 8 bitti, võid iga võtme baiti jaoks valida suvalise numbri vahemikus 0 kuni 255.

Oletame, et valime oma võtme k kui [14,48,9], nii et selle pikkus on 3 baiti. Iga meie võtmemassiivi indeks seatakse siis vastavalt selle konkreetse võtme elemendi kümnendarvule, järjekorras. Kui oled kogu võtme läbi käinud, alusta jälle algusest, kuni oled täitnud võtmemassiivi 8 pesa. Seega on meie võtmemassiiv järgmine:

- K = [14,48,9,14,48,9,14,48]

### 3. samm

Kolmandaks, me transformeerime massiivi S kasutades võtmemassiivi K, protsessis, mida tuntakse kui võtme ajakava. Protsess on järgmine pseudokoodis:

- Loo muutujad j ja i
- Sea muutuja j = 0
- Iga i jaoks 0-st 7-ni:
	- Sea j = j + S[i] + K[i] mod 8
	- Vaheta S[i] ja S[j]

Massiivi S transformatsioon on esitatud *Tabelis 1*.

Alustuseks, näed S algseisu kui [0,1,2,3,4,5,6,7] algväärtusega 0 j jaoks. See transformeeritakse kasutades võtmemassiivi [14,48,9,14,48,9,14,48].
For-tsükkel algab i = 0-ga. Nagu meie pseudokoodis ülalpool mainitud, saab j uueks väärtuseks 6 (j = j + S[0] + K[0] mod 8 = 0 + 0 + 14 mod 8 = 6 mod 8). Vahetades S[0] ja S[6], muutub S seis pärast 1 vooru [6,1,2,3,4,5,0,7]. 
Järgmises reas on i = 1. For-tsüklist uuesti läbides saab j väärtuseks 7 (j = j + S[1] + K[1] mod 8 = 6 + 1 + 48 mod 8 = 55 mod 8 = 7 mod 8). Vahetades S[1] ja S[7] praeguses S seisus, [6,1,2,3,4,5,0,7], saame pärast 2. vooru [6,7,2,3,4,5,0,1].

Jätkame seda protsessi kuni toodame S massiivi lõpliku rea allpool, [6,4,1,0,3,7,5,2].

*Tabel 1: Võtme ajastamise tabel*

![Tabel 1: Võtme ajastamise tabel](assets/Table5-1.webp "Tabel 1: Võtme ajastamise tabel")

### 4. samm

Neljanda sammuna toodame võtmehoidla. See on pseudosuvaline jada, mille pikkus on võrdne sõnumiga, mida soovime saata. Seda kasutatakse algse sõnumi “SOUP” krüpteerimiseks. Kuna võtmehoidla peab olema sama pikk kui sõnum, on meil vaja 4 baiti pikkust võtmehoidlat.

Võtmehoidla toodetakse järgneva pseudokoodi abil:

- Loo muutujad j, i ja t
- Sea j = 0
- Iga plaintexti i jaoks, alustades i = 1 ja jätkates kuni i = 4, toodetakse iga võtmehoidla bait järgmiselt:
    - j = j + S[i] mod 8
	- Vaheta S[i] ja S[j]
	- t = S[i] + S[j] mod 8
	- i-s bait võtmehoidlas = S[t]

Võite jälgida arvutusi *Tabelis 2*.

S algseis = S = [6,4,1,0,3,7,5,2]. Seades i = 1, saab j väärtuseks 4 (j = j + S[i] mod 8 = 0 + 4 mod 8 = 4). Seejärel vahetame S[1] ja S[4], et toota S teisendus teises reas, [6,3,1,0,4,7,5,2]. Väärtus t on seejärel 7 (t = S[i] + S[j] mod 8 = 3 + 4 mod 8 = 7). Lõpuks on võtmehoidla bait siis S[7], ehk 2.

Seejärel võime jätkata teiste baitide tootmist, kuni meil on järgmised neli baiti: 2, 6, 3 ja 7. Igaüht neist baitidest saab seejärel kasutada plaintexti "SOUP" iga tähe krüpteerimiseks.
Alustuseks, kasutades ASCII tabelit, näeme, et sõna "SOUP" kodeerituna aluseks olevate baitide kümnendarvudeks on "83 79 85 80". Kombineerituna võtmehulgaga "2 6 3 2" saame "85 85 88 82", mis jääb samaks ka pärast modulo 256 operatsiooni. ASCII-s vastab šifritekst "85 85 88 82" tähendusele "UUXR". 
Mis juhtub, kui krüpteerida tuleb sõna, mis on pikem kui massiiv S? Sellisel juhul jätkab massiiv S muundumist ülal kirjeldatud viisil iga selgeteksti baiti i jaoks, kuni võtmehulga baitide arv on võrdne selgeteksti tähtede arvuga.

*Tabel 2: Võtmehulga genereerimine*

![Tabel 2: Võtmehulga genereerimine](assets/Table5-2.webp "Tabel 2: Võtmehulga genereerimine")

Just arutatud näide on lihtsustatud versioon RC4 voolušifrist. Tegelik RC4 voolušifris on S massiiv 256 baiti pikk, mitte 8 baiti, ja võti võib olla vahemikus 1 kuni 256 baiti, mitte 1 kuni 8 baiti. Võtmemassiiv ja võtmehulgad on siis kõik toodetud arvestades S massiivi 256 baiti pikkust. Arvutused muutuvad märkimisväärselt keerukamaks, kuid põhimõtted jäävad samaks. Kasutades sama võtit, [14,48,9], standardse RC4 šifriga, krüpteeritakse selgeteksti sõnum "SOUP" kui 67 02 ed df heksadetsimaalformaadis.

Voolušifrit, milles võtmehulk uueneb sõltumatult selgetekstist või šifreeritud tekstist, nimetatakse **sünkroonseks voolušifriks**. Võtmehulk sõltub ainult võtmest. Selgelt on RC4 näide sünkroonsest voolušifrist, kuna võtmehulk ei ole seotud ei selgeteksti ega šifreeritud tekstiga. Kõik meie eelmises peatükis mainitud primitiivsed voolušifrid, sealhulgas nihkešifri, Vigenère'i šifri ja ühekordse padja, olid samuti sünkroonse tüüpi.

Seevastu **asünkroonne voolušifri** toodab võtmehulka, mis on loodud nii võtme kui ka eelnevate šifreeritud teksti elementide põhjal. Seda tüüpi šifrit nimetatakse ka **ise-sünkroniseeruvaks šifriks**.

Oluline on, et RC4-ga toodetud võtmehulka tuleks kohelda kui ühekordset padi, ja te ei saa võtmehulka täpselt samal viisil järgmine kord toota. Praktiline lahendus on võti kombineerida nö nonce'iga, et toota baitjada.

## AES 128-bitise võtmega
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Nagu eelmises peatükis mainitud, korraldas Riiklik Standardite ja Tehnoloogia Instituut (NIST) aastatel 1997 kuni 2000 võistluse, et määrata uus sümmeetriline krüpteerimisstandard. Rijndaeli šifri osutus võitjaks. Nimi on sõnamäng Belgia loojate, Vincent Rijmeni ja Joan Daemeni nimedest.

Rijndaeli šifri on plokšifri, mis tähendab, et on olemas põhialgoritm, mida saab kasutada erinevate spetsifikatsioonidega võtme pikkuste ja ploki suuruste jaoks. Seda saab seejärel kasutada erinevate töörežiimidega, et konstrueerida krüpteerimisskeeme.
NISTi võistluse komitee võttis kasutusele piiratud versiooni Rijndaeli šifrist—nimelt sellise, mis nõuab 128-bitiseid ploki suurusi ja võtme pikkusi kas 128, 192 või 256 bitti—osana täiustatud krüpteerimisstandardist. Seda piiratud versiooni Rijndaeli šifrist saab kasutada ka mitmes töörežiimis. Standardi spetsifikatsioon on tuntud kui Täiustatud Krüpteerimisstandard (AES).

Selleks, et näidata, kuidas Rijndaeli šiffer töötab, AESi tuum, illustreerin ma krüpteerimisprotsessi 128-bitise võtmega. Võtme suurus mõjutab krüpteerimise iga ploki jaoks toimuvate voorude arvu. 128-bitiste võtmete puhul on vaja 10 vooru. 192 ja 256 biti puhul oleks vastavalt 12 ja 14 vooru.

Lisaks eeldan, et AESi kasutatakse ECB-režiimis. See teeb esitluse veidi lihtsamaks ja Rijndaeli algoritmi jaoks ei oma tähtsust. Kindlasti, ECB režiim ei ole praktikas turvaline, kuna see viib deterministliku krüpteerimiseni. AESiga kõige sagedamini kasutatav turvaline režiim on CBC.

Nimetagem võtit K<sub>0</sub>. Eelmainitud parameetritega konstruktsioon näeb välja nagu joonisel 1, kus M<sub>i</sub> tähistab 128-bitist osa tavatekstist ja C<sub>i</sub> 128-bitist osa šifreeritud tekstist. Kui tavateksti ei saa ploki suurusega võrdselt jagada, lisatakse viimasele plokile täidis.

*Joonis 1: AES-ECB 128-bitise võtmega*

![Joonis 1: AES-ECB 128-bitise võtmega](assets/Figure5-1.webp "Joonis 1: AES-ECB 128-bitise võtmega")

Iga 128-bitine tekstiplokk läbib Rijndaeli krüpteerimisskeemis kümme vooru. See nõuab iga vooru jaoks eraldi vooruvõtit (K<sub>1</sub> kuni K<sub>10</sub>). Need vooruvõtmed toodetakse iga vooru jaoks algsest 128-bitisest võtmest K<sub>0</sub>, kasutades võtme laiendamise algoritmi. Seega, iga krüpteeritava tekstiploki jaoks kasutame algset võtit K<sub>0</sub> ning kümme eraldi vooruvõtit. Pane tähele, et neid samu 11 võtit kasutatakse iga 128-bitise tavateksti ploki krüpteerimiseks, mis nõuab krüpteerimist.

Võtme laiendamise algoritm on pikk ja keeruline. Selle läbitöötamine ei paku didaktilist kasu. Võite võtme laiendamise algoritmi ise uurida, kui soovite. Kui vooruvõtmed on toodetud, manipuleerib Rijndaeli šiffer esimest 128-bitist tavateksti plokki, M<sub>1</sub>, nagu on näha joonisel 2. Nüüd vaatame neid samme.

*Joonis 2: M<sub>1</sub> manipuleerimine Rijndaeli šifriga*

![Joonis 2: AES-ECB 128-bitise võtmega](assets/Figure5-2.webp "Joonis 2: AES-ECB 128-bitise võtmega")

### Voor 0

Rijndaeli šifri voor 0 on lihtne. Massiiv S<sub>0</sub> toodetakse XOR-operatsiooniga 128-bitise tavateksti ja privaatvõtme vahel. See tähendab,

- S<sub>0</sub> = M<sub>1</sub> XOR K<sub>0</sub>
Esimeses voorus kombineeritakse massiiv S<sub>0</sub> esmalt vooru võtmega K<sub>1</sub>, kasutades XOR-operatsiooni. See toodab S-i uue oleku.
Teiseks, praeguse S-i oleku peal viiakse läbi baitide asendamise operatsioon. See töötab nii, et võetakse iga 16-baidise S-massiivi bait ja asendatakse see **Rijndaeli S-kasti** massiivi baidiga. Igal baidil on unikaalne transformatsioon ja tulemusena saadakse S-i uus olek. Rijndaeli S-kast on kuvatud *Joonisel 3*.

*Joonis 3: Rijndaeli S-Kast*

![Joonis 3: Rijndaeli S-Kast](assets/Figure5-3.webp "Joonis 3: Rijndaeli S-Kast")

See S-kast on üks koht, kus abstraktne algebra mängib rolli Rijndaeli šifris, eriti Galois' väljad.

Alguses defineerite iga võimaliku baidielemendi 00 kuni FF kui 8-bitise vektori. Iga selline vektor on Galois' välja GF(2<sup>8</sup>) element, kus modulo operatsiooni jaoks on redutseerimatu polünoom x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Galois' välja nende spetsifikatsioonidega nimetatakse ka Rijndaeli Lõplikuks Väljaks.

Järgmisena, iga võimaliku elemendi jaoks väljal loome, mida nimetatakse **Nybergi S-kastiks**. Selles kastis on iga bait kaardistatud oma korrutise pöördväärtusele (st nii, et nende korrutis võrdub 1-ga). Seejärel kaardistame need väärtused Nybergi S-kastist Rijndaeli S-kasti, kasutades afiinset transformatsiooni.

S-massiivi kolmas operatsioon on ridade nihutamise operatsioon. See võtab S-i oleku ja loetleb kõik kuusteist baiti maatriksis. Maatriksi täitmine algab ülevalt vasakult ja liigub edasi, minnes ülevalt alla ja seejärel, iga kord kui veerg on täidetud, nihutades ühe veeru paremale ja üles.

Kui S-i maatriks on konstrueeritud, nihutatakse neli rida. Esimene rida jääb samaks. Teine rida liigub ühe võrra vasakule. Kolmas liigub kaks võrra vasakule. Neljas liigub kolm võrra vasakule. Protsessi näide on toodud *Joonisel 4*. S-i algolek on näidatud ülal, tulemuseks olev olek pärast ridade nihutamise operatsiooni on näidatud allpool.

*Joonis 4: Ridade nihutamise operatsioon*

![Joonis 4: Ridade nihutamise operatsioon](assets/Figure5-4.webp "Joonis 4: Ridade nihutamise operatsioon")

Neljandas sammus tulevad Galois' väljad taas mängu. Alguses korrutatakse iga S-maatriksi veerg 4 x 4 maatriksi veeruga, mida näeb *Joonisel 5*. Kuid selle asemel, et tegemist oleks tavalise maatriksikorrutusega, on see vektorite korrutamine modulo redutseerimatu polünoomi, x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Tulemuseks olevad vektori koefitsiendid esindavad baidi üksikuid bitte.

*Joonis 5: Veergude segamise maatriks*

![Joonis 5: Veergude segamise maatriks](assets/Figure5-5.webp "Joonis 5: Veergude segamise maatriks")

S-maatriksi esimese veeru korrutamine ülaloleva 4 x 4 maatriksiga annab tulemuse *Joonisel 6*.
*Joonis 6: Esimese veeru korrutamine*
![Joonis 6: Esimese veeru korrutamine](assets/Figure5-6.webp "Joonis 6: Esimese veeru korrutamine")

Järgmise sammuna tuleb kõik maatriksi elemendid teisendada polünoomideks. Näiteks F1, mis esindab 1 baiti, muutub x<sup>7</sup> + x<sup>6</sup> + x<sup>5</sup> + x<sup>4</sup> + 1-ks ja 03, mis samuti esindab 1 baiti, muutub x + 1-ks.

Kõik korrutamised tehakse seejärel modulo x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Selle tulemusena saadakse igas veeru neljas lahtris neli polünoomi. Pärast nende liitmist modulo 2 saadakse neli polünoomi. Iga selline polünoom esindab 8-bitist jada ehk 1 baiti S-s. Me ei teosta siin kõiki neid arvutusi *Joonisel 6* kuna need on mahukad.

Pärast esimese veeru töötlemist töödeldakse S maatriksi teisi kolme veeru samal viisil. Lõpuks saadakse kuusteist baiti sisaldav maatriks, mida saab teisendada massiiviks.

Viimase sammuna ühendatakse massiiv S uuesti vooru võtmega XOR-operatsiooni kaudu. See toodab oleku S<sub>1</sub>. See tähendab,

- S<sub>1</sub> = S XOR K<sub>0</sub>

### Voorud 2 kuni 10

Voorud 2 kuni 9 on lihtsalt vooru 1 kordus, *mutatis mutandis*. Viimane voor näeb välja väga sarnane eelnevatele voorudele, välja arvatud see, et segamise samm on elimineeritud. See tähendab, et voor 10 viiakse läbi järgmiselt:

- S<sub>9</sub> XOR K<sub>10</sub>
- Baidi asendamine
- Readade nihutamine
- S<sub>10</sub> = S XOR K<sub>10</sub>

Olek S<sub>10</sub> on nüüd seadistatud C<sub>1</sub>-ks, esimeseks 128 bitiks šifreeritud tekstist. Järgnevate 128-bitiste tekstiplokkide töötlemine annab täieliku šifreeritud teksti C.

### Rijndaeli šifri toimingud

Mis on erinevate toimingute põhjendus Rijndaeli šifris?

Detailidesse laskumata hinnatakse krüpteerimisskeeme selle alusel, kuivõrd need loovad segadust ja hajutatust. Kui krüpteerimisskeemil on kõrge **segaduse** aste, tähendab see, et šifreeritud tekst näeb välja drastiliselt erinev algtekstist. Kui krüpteerimisskeemil on kõrge **hajutatuse** aste, tähendab see, et iga väike muudatus algtekstis toodab drastiliselt erineva šifreeritud teksti.

Rijndaeli šifri toimingute põhjendus on see, et need toodavad nii kõrget segaduse kui ka hajutatuse astet. Segadus tekib baidi asendamise toimingu kaudu, samal ajal kui hajutatus tekib readade nihutamise ja veergude segamise toimingute kaudu.

# Asümmeetriline krüptograafia
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

Nagu sümmeetrilise krüptograafia puhul, saab asümmeetrilisi skeeme kasutada nii saladuse hoidmiseks kui ka autentsuse tagamiseks. Erinevus seisneb siiski selles, et nende skeemide puhul kasutatakse kahte võtit, mitte ühte: privaatvõtit ja avalikku võtit.
Meie uurimistöö algab asümmeetrilise krüptograafia avastamisega, eriti probleemidega, mis seda esile kutsusid. Järgnevalt arutame, kuidas asümmeetrilised skeemid krüpteerimiseks ja autentimiseks kõrgel tasemel töötavad. Seejärel tutvustame räsifunktsioone, mis on võtmetähtsusega asümmeetriliste autentimisskeemide mõistmisel ning omavad tähtsust ka teistes krüptograafilistes kontekstides, nagu näiteks räsi-põhised sõnumi autentimiskoodid, millest rääkisime 4. peatükis.

## Võtmete jaotamise ja haldamise probleem
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Oletame, et Bob soovib osta uue vihmamantli Jim’s Sporting Goods'ist, veebipõhisest spordikaupade jaemüüjast, millel on miljoneid kliente Põhja-Ameerikas. See saab olema tema esimene ost neilt ja ta soovib kasutada oma krediitkaarti. Seega peab Bob esmalt looma konto Jim’s Sporting Goods'is, mis nõuab isiklike andmete, nagu tema aadressi ja krediitkaardi informatsiooni, edastamist. Seejärel saab ta läbida sammud, mis on vajalikud vihmamantli ostmiseks.

Bob ja Jim’s Sporting Goods soovivad tagada, et nende suhtlus on kogu protsessi vältel turvaline, arvestades, et Internet on avatud suhtlussüsteem. Nad soovivad näiteks tagada, et ükski potentsiaalne ründaja ei saaks teada Bobi krediitkaardi ja aadressi detaile ning et ükski potentsiaalne ründaja ei saaks korrata tema oste või luua tema nimel võltsoste.

Täiustatud autentitud krüpteerimisskeem, millest eelmises peatükis rääkisime, võiks kindlasti muuta Bobi ja Jim’s Sporting Goods'i vahelise suhtluse turvaliseks. Kuid sellise skeemi rakendamisel on selgelt praktilisi takistusi.

Nende praktiliste takistuste illustreerimiseks oletame, et elame maailmas, kus eksisteerivad ainult sümmeetrilise krüptograafia vahendid. Mida saaksid Jim’s Sporting Goods ja Bob siis teha, et tagada turvaline suhtlus?

Sellistes oludes seisaksid nad silmitsi märkimisväärsete kuludega turvaliseks suhtlemiseks. Kuna Internet on avatud suhtlussüsteem, ei saa nad lihtsalt vahetada võtmete komplekti selle kaudu. Seega peab Bob ja Jim’s Sporting Goods'i esindaja tegema võtmevahetuse isiklikult.

Üks võimalus on, et Jim’s Sporting Goods loob erilised võtmevahetuse kohad, kus Bob ja teised uued kliendid saavad turvalise suhtluse jaoks võtmete komplekti kätte. See tooks ilmselgelt kaasa märkimisväärseid organisatsioonilisi kulusid ja vähendaks oluliselt uute klientide ostude tegemise efektiivsust.

Teisalt võib Jim’s Sporting Goods saata Bobile võtmepaari usaldusväärse kulleri kaudu. See on tõenäoliselt efektiivsem kui võtmevahetuse kohtade korraldamine. Kuid see tooks siiski kaasa märkimisväärseid kulusid, eriti kui paljud kliendid teevad ainult ühe või mõned ostud.

Järgmiseks sunnib sümmeetriline skeem autentitud krüpteerimiseks Jim’s Sporting Goods'i säilitama eraldi võtmekomplekte kõigi oma klientide jaoks. See oleks märkimisväärne praktiline väljakutse tuhandete klientide jaoks, rääkimata miljonitest.

Selle viimase punkti mõistmiseks oletame, et Jim’s Sporting Goods annab igale kliendile sama võtmepaari. See võimaldaks igal kliendil – või kellel iganes, kes võiks selle võtmepaari kätte saada – lugeda ja isegi manipuleerida kõigi suhtlustega Jim’s Sporting Goods'i ja selle klientide vahel. Siis võiks sama hästi üldse mitte kasutada krüptograafiat oma suhtluses.

Isegi võtmekomplekti kordamine ainult mõne kliendi jaoks on kohutav turvapraktika. Iga potentsiaalne ründaja võiks proovida ära kasutada selle skeemi omadust (pidage meeles, et ründajatele eeldatakse, et nad teavad kõike skeemi kohta peale võtmete, vastavalt Kerckhoffs’i põhimõttele.)

Seega peab Jim’s Sporting Goods säilitama võtmepaari iga kliendi jaoks, olenemata sellest, kuidas neid võtmepaare jaotatakse. See esitab selgelt mitmeid praktilisi probleeme.

- Jim’s Sporting Goods peab säilitama miljoneid võtmepaare, ühe komplekti iga kliendi jaoks.
- Neid võtmeid tuleks korralikult turvata, kuna need oleksid kindel sihtmärk häkkeritele. Iga turvaintsident nõuaks kulukate võtmevahetuste kordamist, kas erilistes võtmevahetuspunktides või kulleri abil. - Iga Jim's Sporting Goods'i klient peaks kodus turvaliselt hoidma võtmepaari. Kadumised ja vargused toimuvad, nõudes võtmevahetuste kordamist. Kliendid peaksid läbima selle protsessi ka mis tahes muude veebipoodide või muud tüüpi üksustega, kellega nad soovivad Interneti kaudu suhelda ja tehinguid teha.

Need kaks peamist väljakutset, mida just kirjeldati, olid väga fundamentaalsed mured kuni 1970ndate lõpuni. Neid tunti vastavalt kui **võtmete levitamise probleemi** ja **võtmete haldamise probleemi**.

Need probleemid olid alati olemas olnud, muidugi, ja sageli tekitanud peavalu minevikus. Näiteks sõjaväejõud peaksid pidevalt levitama raamatuid võtmetega turvaliseks suhtluseks välitöötajatele suurte riskide ja kuludega. Kuid need probleemid muutusid hullemaks, kuna maailm liikus üha enam pika vahemaa digitaalse suhtluse poole, eriti valitsusväliste üksuste jaoks.

Kui neid probleeme poleks 1970ndatel lahendatud, siis tõenäoliselt ei oleks Jim's Sporting Goods'is efektiivset ja turvalist ostlemist olemas olnud. Tegelikult, suurem osa meie kaasaegsest maailmast praktilise ja turvalise e-posti, veebipanga ja ostlemisega oleks tõenäoliselt olnud vaid kauge unistus. Midagi isegi Bitcoinile sarnanevat ei oleks saanud üldse olemas olla.

Niisiis, mis juhtus 1970ndatel? Kuidas on võimalik, et me saame hetkega teha oste veebis ja turvaliselt sirvida World Wide Web'i? Kuidas on võimalik, et me saame hetkega saata Bitcoine üle kogu maailma oma nutitelefonidest?

## Uued suunad krüptograafias
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

1970ndateks olid võtmete levitamise ja haldamise probleemid pälvinud Ameerika akadeemiliste krüptograafide grupi tähelepanu: Whitfield Diffie, Martin Hellman ja Ralph Merkle. Tugeva skeptitsismi all oma kolleegide enamuse poolt, nad asusid otsima lahendust sellele.

Vähemalt üks peamine motivatsioon nende ettevõtmiseks oli ettenägelikkus, et avatud arvutisuhtlus mõjutab meie maailma sügavalt. Nagu Diffie ja Hellman märkisid 1976. aastal,

> Arvutijuhtimisega suhtlusvõrkude areng lubab vaevata ja odavalt kontakteeruda inimeste või arvutitega maailma vastaskülgedel, asendades enamiku postist ja paljud väljasõidud telekommunikatsiooniga. Paljude rakenduste puhul peavad need kontaktid olema turvatud nii pealtkuulamise kui ka ebaseaduslike sõnumite sisestamise vastu. Praegu aga jääb turvaprobleemide lahendamine teistest kommunikatsioonitehnoloogia valdkondadest maha. *Kaasaegne krüptograafia ei suuda nõudmistele vastata, kuna selle kasutamine tooks kasutajatele kaasa sellised tõsised ebamugavused, et see kaotaks paljud teleprotsessi eelised.*<sup>[1](#footnote1)</sup>

Diffie, Hellmani ja Merkle'i visadus tasus end ära. Nende tulemuste esimene avaldamine oli Diffie ja Hellmani poolt 1976. aastal pealkirjaga “Uued suunad krüptograafias.” Selles esitlesid nad kahte originaalset viisi võtmete levitamise ja haldamise probleemide lahendamiseks.
Esimese lahendusena pakkusid nad välja kaug-*võtmevahetusprotokolli*, see tähendab reeglite kogumit ühe või mitme sümmeetrilise võtme vahetamiseks ebaturvalise suhtluskanali kaudu. See protokoll on nüüd tuntud kui *Diffie-Helmanni võtmevahetus* või *Diffie-Helmann-Merkle võtmevahetus*.<sup>[2](#footnote2)</sup>
Diffie-Helmanni võtmevahetuse korral vahetavad kaks osapoolt esmalt mõningast informatsiooni avalikult ebaturvalisel kanalil, nagu näiteks Internet. Selle informatsiooni põhjal loovad nad seejärel iseseisvalt sümmeetrilise võtme (või paar sümmeetrilist võtit) turvaliseks suhtluseks. Kuigi mõlemad osapooled loovad oma võtmed iseseisvalt, tagab avalikult jagatud informatsioon, et see võtmete loomise protsess annab mõlemale neist sama tulemuse.

Oluline on, et kuigi kõik võivad jälgida osapoolte poolt ebaturvalisel kanalil avalikult vahetatavat informatsiooni, saavad ainult kaks informatsiooni vahetavat osapoolt sellest luua sümmeetrilisi võtmeid.

See kõlab muidugi täiesti vastuoluliselt. Kuidas saavad kaks osapoolt avalikult vahetada teavet, mis võimaldab ainult neil luua sümmeetrilisi võtmeid? Miks ei suudaks keegi teine, kes jälgib informatsiooni vahetust, luua samu võtmeid?

See tugineb muidugi mõnele kaunile matemaatikale. Diffie-Helmanni võtmevahetus toimib ühesuunalise funktsiooni abil, millel on lõks. Arutame neid kahte terminit järjekorras.

Eeldame, et teile on antud mingi funktsioon f(x) ja tulemus f(a) = y, kus a on konkreetne väärtus x jaoks. Me ütleme, et f(x) on **ühesuunaline funktsioon**, kui y väärtuse arvutamine on lihtne, kui on antud a ja f(x), kuid a väärtuse arvutamine on arvutuslikult teostamatu, kui on antud y ja f(x). Ühesuunalise funktsiooni nimi tuleneb muidugi asjaolust, et sellist funktsiooni on praktiline arvutada ainult ühes suunas.

Mõnedel ühesuunalistel funktsioonidel on see, mida tuntakse kui lõksu. Kuigi a arvutamine ainult y ja f(x) alusel on praktiliselt võimatu, on olemas teatud teave Z, mis muudab a arvutamise y-st arvutuslikult teostatavaks. See teave Z on tuntud kui **lõks**. Ühesuunalisi funktsioone, millel on lõks, tuntakse kui **lõksufunktsioone**.

Me ei süvene siin Diffie-Helmanni võtmevahetuse detailidesse. Kuid sisuliselt loob iga osaleja teatud informatsiooni, millest osa jagatakse avalikult ja osa jääb salajaseks. Iga osapool võtab seejärel oma salajase teabe ja teise osapoole poolt jagatud avaliku teabe, et luua privaatvõti. Ja üsna imelikul kombel lõppeb mõlemal osapoolel sama privaatvõtmega.

Ükski osapool, kes jälgib ainult kahe osapoole vahel Diffie-Helmanni võtmevahetuses avalikult jagatud teavet, ei suuda neid arvutusi korrata. Selleks oleks vaja ühe kahest osapoolest privaatset teavet.

Kuigi Diffie-Helmanni võtmevahetuse põhiversioon, mis esitati 1976. aasta artiklis, ei ole väga turvaline, on selle põhiprotokolli keerukamad versioonid kindlasti tänapäeval veel kasutusel. Kõige tähtsam on, et iga võtmevahetusprotokoll transpordikihi turvalisuse protokolli (version 1.3) viimases versioonis on sisuliselt rikastatud versioon protokollist, mille esitasid Diffie ja Hellman 1976. aastal. Transpordikihi turvalisuse protokoll on peamine protokoll veebisisu vahetamiseks vastavalt hüperteksti edastusprotokollile (http), mis on veebisisu vahetamise standard.
Oluline on märkida, et Diffie-Helmanni võtmevahetus ei ole asümmeetriline skeem. Rangelt öeldes kuulub see pigem sümmeetrilise võtme krüptograafia valdkonda. Kuid kuna nii Diffie-Helmanni võtmevahetus kui ka asümmeetriline krüptograafia tuginevad ühesuunalistele arvuteoreetilistele funktsioonidele koos lõksudega, arutatakse neid tavaliselt koos.
Teine viis, kuidas Diffie ja Helmann pakkusid oma 1976. aasta artiklis võtmete jaotuse ja halduse probleemi lahendamiseks, oli muidugi asümmeetrilise krüptograafia kaudu.

Erinevalt nende Diffie-Hellmani võtmevahetuse esitlusest, pakkusid nad ainult üldisi kontuure, kuidas asümmeetrilisi krüptograafilisi skeeme võiks usutavalt konstrueerida. Nad ei pakkunud ühtegi konkreetset ühesuunalist funktsiooni, mis võiks spetsiifiliselt täita mõistliku turvalisuse tingimusi sellistes skeemides.

Praktiline asümmeetrilise skeemi rakendus leiti siiski aasta hiljem kolme erineva akadeemilise krüptograafi ja matemaatiku poolt: Ronald Rivest, Adi Shamir ja Leonard Adleman.<sup>[3](#footnote3)</sup> Nende tutvustatud krüptosüsteem sai tuntuks kui **RSA krüptosüsteem** (nende perekonnanimede järgi).

Asümmeetrilises krüptograafias (ja Diffie Helmanni võtmevahetuses) kasutatavad lõksufunktsioonid on seotud kahe peamise **arvutuslikult keeruka probleemiga**: algarvude tegurdamine ja diskreetsete logaritmide arvutamine.

**Algarvude tegurdamine** nõuab, nagu nimigi ütleb, täisarvu lagundamist selle algarvudeks. RSA probleem on kaugelt kõige tuntum näide krüptosüsteemist, mis on seotud algarvude tegurdamisega.

**Diskreetse logaritmi probleem** on probleem, mis esineb tsüklilistes gruppides. Antud generaatori korral konkreetses tsüklilises grupis nõuab see unikaalse eksponendi arvutamist, mis on vajalik teise elemendi tootmiseks grupis generaatorist.

Diskreetse logaritmi põhised skeemid tuginevad kahele peamisele tsükliliste gruppide liigile: täisarvude korrutamise grupid ja grupid, mis hõlmavad punkte elliptilistel kõveratel. Algupärane Diffie Helmanni võtmevahetus, nagu esitleti artiklis "New Directions in Cryptography", töötab täisarvude korrutamise tsüklilise grupiga. Bitcoini digitaalne allkirjastamise algoritm ja hiljuti tutvustatud Schnorri allkirjastamise skeem (2021) põhinevad mõlemad diskreetse logaritmi probleemil konkreetse elliptilise kõvera tsüklilises grupis.

Järgnevalt pöördume kõrgetasemelise ülevaate juurde saladusest ja autentimisest asümmeetrilises seades. Enne seda peame siiski tegema lühikese ajaloolise märkuse.

Nüüd tundub usutav, et Suurbritannia krüptograafide ja matemaatikute rühm, kes töötas Valitsuse Sidepeakorteri (GCHQ) heaks, oli mõned aastad varem sõltumatult teinud eespool mainitud avastused. Sellesse rühma kuulusid James Ellis, Clifford Cocks ja Malcolm Williamson.

Nende endi ja GCHQ aruannete kohaselt oli James Ellis see, kes esimesena töötas välja avaliku võtme krüptograafia kontseptsiooni 1969. aastal. Väidetavalt avastas Clifford Cocks seejärel RSA krüptograafilise süsteemi 1973. aastal ja Malcolm Williamson Diffie Helmanni võtmevahetuse kontseptsiooni 1974. aastal.<sup>[4](#footnote4)</sup> Nende avastused aga väidetavalt ei tulnud ilmsiks enne 1997. aastat, arvestades GCHQ-s tehtud töö salajast olemust.


## Asümmeetriline krüpteerimine ja autentimine
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Ülevaade asümmeetrilisest krüpteerimisest Bobi ja Alice'i abil on esitatud *Joonisel 1*.
Alice loob esmalt võtmepaari, mis koosneb ühest avalikust võtmest (K<sub>P</sub>) ja ühest privaatvõtmest (K<sub>S</sub>), kus "P" K<sub>P</sub>-s tähistab "public" (avalik) ja "S" K<sub>S</sub>-s "secret" (salajane). Seejärel jagab ta seda avalikku võtit vabalt teistega. Naaseme selle jaotusprotsessi detailide juurde veidi hiljem. Kuid praegu eeldame, et igaüks, sealhulgas Bob, saab Alice'i avaliku võtme K<sub>P</sub> turvaliselt kätte saada.
Hiljem soovib Bob saata sõnumi M Alice'ile. Kuna see sisaldab tundlikku teavet, soovib ta, et sõnumi sisu jääks saladuseks kõigile peale Alice'i. Seega krüpteerib Bob esmalt oma sõnumi M kasutades K<sub>P</sub>. Seejärel saadab ta tulemuseks oleva šifreeritud teksti C Alice'ile, kes dekrüpteerib C K<sub>S</sub> abil, et taastada algne sõnum M.

*Joonis 1: Asümmeetriline krüpteerimine*

![Joonis 1: Asümmeetriline krüpteerimine](assets/Figure6-1.webp "Joonis 1: Asümmeetriline krüpteerimine")

Iga vaenlane, kes kuulab pealt Bobi ja Alice'i suhtlust, võib märgata C-d. Ta teab ka K<sub>P</sub> ja krüpteerimisalgoritmi E(·). Oluline on aga see, et see teave ei võimalda ründajal šifreeritud teksti C realistlikult dekrüpteerida. Dekrüpteerimine nõuab spetsiifiliselt K<sub>S</sub>, mida ründajal ei ole.

Sümmeetrilised krüpteerimisskeemid peavad üldiselt olema turvalised ründaja vastu, kes suudab õiguspäraselt krüpteerida lihttekstsõnumeid (tuntud kui valitud-šifreeritud teksti ründe turvalisus). Neid ei ole siiski kavandatud spetsiaalselt selle eesmärgiga, et võimaldada ründajal või kellelgi teisel selliseid õiguspäraseid šifreeritud tekste luua.

See on teravas kontrastis asümmeetrilise krüpteerimisskeemiga, mille peamine eesmärk on võimaldada kõigil, sealhulgas ründajatel, luua õiguspäraseid šifreeritud tekste. Seega võib asümmeetrilisi krüpteerimisskeeme nimetada **mitme juurdepääsuga šifrideks**.

Et paremini mõista, mis toimub, kujutage ette, et Bob soovis sõnumit saata mitte elektrooniliselt, vaid salajas füüsilise kirjana. Üks viis salajasuse tagamiseks oleks, kui Alice saadaks Bobile turvalise tabaluku, kuid hoiaks võtit enda käes. Pärast kirja kirjutamist võiks Bob panna kirja kasti ja sulgeda selle Alice'i tabalukuga. Seejärel võiks ta lukustatud kasti sõnumiga Alice'ile saata, kellel on võti see avada.

Kuigi Bob suudab tabaluku lukustada, ei saa ei tema ega ükski teine isik, kes kasti kätte saab, tabalukku avada, kui see on tõepoolest turvaline. Ainult Alice saab selle avada ja näha Bobi kirja sisu, sest tal on võti.

Asümmeetriline krüpteerimisskeem on, üldjoontes öeldes, selle protsessi digitaalne versioon. Tabalukk on analoogne avaliku võtmega ja tabaluku võti on analoogne privaatvõtmega. Kuna tabalukk on digitaalne, on Alice'il palju lihtsam ja vähem kulukas seda jagada kõigiga, kes võivad soovida talle salajasi sõnumeid saata.

Autentimiseks asümmeetrilises seades kasutame **digitaalseid allkirju**. Need täidavad seega sama funktsiooni kui sõnumi autentimiskoodid sümmeetrilises seades. Digitaalsete allkirjade ülevaade on esitatud *Joonisel 2*.
Bob loob esmalt võtmepaari, mis koosneb avalikust võtmest (K<sub>P</sub>) ja privaatvõtmest (K<sub>S</sub>), ning jagab oma avaliku võtme. Kui ta soovib saata Alice'ile autentitud sõnumi, võtab ta esmalt oma sõnumi M ja oma privaatvõtme, et luua digitaalne allkiri D. Seejärel saadab Bob Alice'ile oma sõnumi koos digitaalse allkirjaga. Alice sisestab sõnumi, avaliku võtme ja digitaalse allkirja kontrollimisalgoritmi. See algoritm annab tulemuseks kas true (tõene) valide allkirja korral või false (väär) vale allkirja korral.
Digitaalne allkiri on, nagu nimi selgelt viitab, kirjaliku allkirja digitaalne ekvivalent kirjadel, lepingutel ja nii edasi. Tegelikult on digitaalne allkiri tavaliselt palju turvalisem. Kirjaliku allkirja võltsimine nõuab teatud pingutust; protsessi lihtsustab asjaolu, et kirjalikke allkirju tihti ei kontrollita põhjalikult. Turvaline digitaalne allkiri on aga, nagu turvaline sõnumi autentimiskood, **eksistentsiaalselt võltsimiskindel**: see tähendab, et turvalise digitaalse allkirja skeemi korral ei saa keegi loogiliselt luua allkirja sõnumile, mis läbiks kontrollimisprotseduuri, välja arvatud juhul, kui neil on privaatvõti.

*Joonis 2: Asümmeetriline autentimine*

![Joonis 2: Asümmeetriline autentimine](assets/Figure6-2.webp "Joonis 2: Asümmeetriline autentimine")

Nagu asümmeetrilise krüpteerimise puhul, näeme huvitavat kontrasti digitaalsete allkirjade ja sõnumi autentimiskoodide vahel. Viimase puhul saab kontrollimisalgoritmi kasutada ainult üks turvalise suhtlusega seotud osapool, kuna see nõuab privaatvõtit. Asümmeetrilises seades aga võib igaüks kontrollida Bobi poolt tehtud digitaalset allkirja S.

Kõik see teeb digitaalsetest allkirjadest äärmiselt võimsa tööriista. See on näiteks aluseks lepingutele allkirjade tegemisel, mida saab õiguslikel eesmärkidel kontrollida. Kui Bob oleks eelpool toodud vahetuses lepingule allkirja teinud, saab Alice näidata sõnumit M, lepingut ja allkirja S kohtule. Kohus saab seejärel kontrollida allkirja kasutades Bobi avalikku võtit.<sup>[5](#footnote5)</sup>

Teise näitena on digitaalsed allkirjad oluline aspekt turvalise tarkvara ja tarkvarauuenduste levitamisel. Sellist avalikku kontrollitavust ei saaks kunagi luua ainult sõnumi autentimiskoodide abil.

Viimase näitena digitaalsete allkirjade võimsusest kaaluge Bitcoini. Üks levinumaid väärarusaamu Bitcoini kohta, eriti meedias, on see, et tehingud on krüpteeritud: tegelikult ei ole. Selle asemel töötavad Bitcoin tehingud digitaalsete allkirjadega, tagamaks turvalisust.

Bitcoinid eksisteerivad partiidena, mida nimetatakse kulutamata tehinguväljunditeks (või UTXO'deks). Oletame, et saate kindlal Bitcoin aadressil kolm makset, igaüks 2 bitcoini. Tehniliselt ei ole teil nüüd sellel aadressil 6 bitcoini. Selle asemel on teil kolm 2 bitcoini partiid, mis on lukustatud krüptograafilise probleemiga, mis on seotud selle aadressiga. Iga makse tegemisel võite kasutada ühte, kahte või kõiki kolme neist partiist, olenevalt sellest, kui palju te tehingu jaoks vajate.

Kulutamata tehinguväljundite üle omandiõiguse tõendamiseks kasutatakse tavaliselt ühte või mitut digitaalset allkirja. Bitcoin toimib täpselt seetõttu, et kehtivate digitaalsete allkirjade loomine kulutamata tehinguväljunditele on arvutuslikult teostamatu, välja arvatud juhul, kui olete valduses salajastest andmetest, mis on nende loomiseks vajalikud.
Praegu sisaldavad Bitcoin'i tehingud läbipaistvalt kogu teavet, mida võrgus osalejad peavad kontrollima, nagu tehingu kasutamata tehinguväljundite päritolu. Kuigi on võimalik peita osa sellest teabest ja siiski lubada kontrollimist (nagu mõned alternatiivsed krüptovaluutad, näiteks Monero, teevad), loob see ka erilisi turvariske.
Segadus tekib mõnikord digitaalsete allkirjade ja digitaalselt jäädvustatud kirjalike allkirjade üle. Viimasel juhul jäädvustate oma kirjaliku allkirja pildi ja kleepite selle elektroonilisele dokumendile, nagu tööleping. See siiski ei ole digitaalne allkiri krüptograafilises mõttes. Viimane on lihtsalt pikk number, mida saab toota ainult eravõtme valduses olles.

Nagu sümmeetrilise võtme seadistuses, saate kasutada ka asümmeetrilist krüpteerimist ja autentimisskeeme koos. Sarnased põhimõtted kehtivad. Esiteks peaksite kasutama erinevaid privaatse-avaliku võtme paare krüpteerimiseks ja digitaalsete allkirjade tegemiseks. Lisaks peaksite esmalt sõnumi krüpteerima ja seejärel autentima.

Oluliselt, paljudes rakendustes ei kasutata asümmeetrilist krüptograafiat kogu suhtlusprotsessi vältel. Selle asemel kasutatakse seda tavaliselt ainult *sümmeetriliste võtmete vahetamiseks* osapoolte vahel, millega nad tegelikult suhtlevad.

See on näiteks juhul, kui ostate kaupu veebis. Tundes müüja avalikku võtit, saab ta saata teile digitaalselt allkirjastatud sõnumeid, mida saate kontrollida nende autentsuse osas. Selle põhjal saate järgida ühte mitmest protokollist sümmeetriliste võtmete turvaliseks vahetamiseks suhtlemiseks.

Peamine põhjus nimetatud lähenemisviisi sageduseks on see, et asümmeetriline krüptograafia on palju vähem efektiivne kui sümmeetriline krüptograafia, et toota teatud turvatase. See on üks põhjus, miks me ikka vajame sümmeetrilise võtme krüptograafiat avaliku krüptograafia kõrval. Lisaks on sümmeetrilise võtme krüptograafia palju loomulikum erirakendustes, nagu arvutikasutaja oma andmete krüpteerimine.

Niisiis, kuidas täpselt digitaalsed allkirjad ja avaliku võtme krüpteerimine lahendavad võtmete levitamise ja võtmete haldamise probleemid?

Siin ei ole üht vastust. Asümmeetriline krüptograafia on tööriist ja selle tööriista kasutamiseks ei ole üht kindlat viisi. Kuid võtame meie varasema näite Jim's Sporting Goods'ist, et näidata, kuidas probleeme tavaliselt selles näites lahendatakse.

Alustuseks läheneks Jim's Sporting Goods tõenäoliselt **sertifitseerimisasutusele**, organisatsioonile, mis toetab avaliku võtme levitamist. Sertifitseerimisasutus registreeriks mõned üksikasjad Jim's Sporting Goods kohta ja annaks sellele avaliku võtme. Seejärel saadaks ta Jim's Sporting Goods'ile sertifikaadi, mida tuntakse kui **TLS/SSL sertifikaati**, Jim's Sporting Goods'i avaliku võtmega, mis on digitaalselt allkirjastatud kasutades sertifitseerimisasutuse enda avalikku võtit. Sel viisil kinnitab sertifitseerimisasutus, et teatud avalik võti kuulub tõepoolest Jim's Sporting Goods'ile.

TLS/SSL sertifikaatidega seotud protsessi mõistmise võti on see, et kuigi te tavaliselt ei oma Jim's Sporting Goods'i avalikku võtit kusagil oma arvutis salvestatuna, on tunnustatud sertifitseerimisasutuste avalikud võtmed tõepoolest salvestatud teie brauserisse või operatsioonisüsteemi. Need on salvestatud nn **juursertifikaatidesse**.

Seega, kui Jim's Sporting Goods annab teile oma TLS/SSL sertifikaadi, saate kontrollida sertifitseerimisasutuse digitaalset allkirja brauseris või operatsioonisüsteemis oleva juursertifikaadi kaudu. Kui allkiri on kehtiv, võite olla suhteliselt kindel, et sertifikaadil olev avalik võti tõepoolest kuulub Jim's Sporting Goods'ile. Selle põhjal on lihtne seadistada protokoll turvaliseks suhtlemiseks Jim's Sporting Goods'iga.
Võtmete jagamine on Jim's Sporting Goods jaoks nüüdseks muutunud märkimisväärselt lihtsamaks. Pole raske märgata, et ka võtmete haldamine on oluliselt lihtsustunud. Selle asemel, et hoida tuhandeid võtmeid, peab Jim's Sporting Goods säilitama ainult privaatvõtme, mis võimaldab neil teha allkirju oma SSL-sertifikaadi avalikule võtmele. Iga kord, kui klient tuleb Jim's Sporting Goods'i saidile, saavad nad selle avaliku võtme abil luua turvalise suhtlusseansi. Kliendid ei pea samuti säilitama mingit teavet (välja arvatud tunnustatud sertifitseerimisasutuste avalikud võtmed oma operatsioonisüsteemis ja brauseris).

## Räsifunktsioonid
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Räsifunktsioonid on krüptograafias kõikjal levinud. Need ei ole ei sümmeetrilised ega asümmeetrilised skeemid, vaid kuuluvad omaette krüptograafilisse kategooriasse.

Räsifunktsioonidega puutusime juba kokku 4. peatükis, kus loodi räsi-põhiseid autentimissõnumeid. Need on olulised ka digitaalallkirjade kontekstis, kuigi veidi erineval põhjusel: Digitaalallkirjad tehakse tavaliselt mõne (krüpteeritud) sõnumi räsi väärtusele, mitte tegelikule (krüpteeritud) sõnumile. Selles jaotises pakun ma räsifunktsioonide kohta põhjalikumat tutvustust.

Alustame räsifunktsiooni määratlemisest. **Räsifunktsioon** on iga tõhusalt arvutatav funktsioon, mis võtab sisendeid suvalises suuruses ja annab fikseeritud pikkusega väljundeid.

**Krüptograafiline räsifunktsioon** on lihtsalt räsifunktsioon, mis on kasulik rakendustes krüptograafias. Krüptograafilise räsifunktsiooni väljundit nimetatakse tavaliselt **räsiks**, **räsi-väärtuseks** või **sõnumi kokkuvõtteks**.

Krüptograafia kontekstis viitab "räsifunktsioon" tavaliselt krüptograafilisele räsifunktsioonile. Ma võtan selle praktika edaspidi kasutusele.

Üks populaarne räsifunktsioon on **SHA-256** (turvaline räsialgoritm 256). Olenemata sisendi suurusest (nt 15 bitti, 100 bitti või 10 000 bitti), annab see funktsioon 256-bitise räsi väärtuse. Allpool näete mõningaid SHA-256 funktsiooni väljundite näiteid.

* “Hello”: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
* “52398”: a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90
* “Cryptography is fun”: 3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c

Kõik väljundid on täpselt 256 bitti, esitatud kuueteistkümnendsüsteemis (iga heksadetsimaalne number saab esitada nelja binaarse numbriga). Seega, isegi kui sisestasite SHA-256 funktsiooni Tolkieni raamatu *Sõrmuste Isand*, oleks väljund ikkagi 256 bitti.

Räsifunktsioone nagu SHA-256 kasutatakse krüptograafias mitmesugustel eesmärkidel. Milliseid omadusi räsifunktsioonilt nõutakse, sõltub konkreetse rakenduse kontekstist. Krüptograafias räsifunktsioonidelt üldiselt soovitud kaks peamist omadust on:

1.	Kokkupõrkekindlus
2.	Peitmine

Räsifunktsiooni H peetakse **kokkupõrkekindlaks**, kui on teostamatu leida kahte väärtust, x ja y, nii, et x ≠ y, kuid H(x) = H(y).
Kokkupõrkekindlad räsifunktsioonid on olulised näiteks tarkvara autentsuse kontrollimisel. Kujutage ette, et soovite alla laadida Bitcoin Core 0.21.0 Windowsi versiooni (serverirakendus Bitcoin võrguliikluse töötlemiseks). Peamised sammud, mida peate tarkvara legitiimsuse kontrollimiseks tegema, on järgmised:
1. Esiteks peate alla laadima ja importima ühe või mitme Bitcoin Core'i panustaja avalikud võtmed tarkvarasse, mis suudab digitaalallkirju kontrollida (nt Kleopetra). Neid avalikke võtmeid saate leida [siit](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Soovitatav on kontrollida Bitcoin Core'i tarkvara mitme panustaja avalike võtmetega.
2. Järgmiseks peate kontrollima importitud avalikke võtmeid. Vähemalt üks samm, mida peaksite tegema, on kontrollida, kas leitud avalikud võtmed on samad, mis on avaldatud erinevates teistes kohtades. Näiteks võiksite konsulteerida inimeste isiklike veebilehtede, Twitteri lehtede või Githubi lehtedega, kelle avalikud võtmed te importisite. Tavaliselt tehakse avalike võtmete võrdlemine, võrreldes avaliku võtme lühikest räsi, mida tuntakse sõrmejäljena.
3. Järgmiseks peate alla laadima Bitcoin Core'i täitmisfaili nende [veebisaidilt](www.bitcoincore.org). Seal on saadaval paketid Linuxi, Windowsi ja MAC operatsioonisüsteemidele.
4. Järgmiseks peate leidma kaks väljalaskefaili. Esimene neist sisaldab allalaaditud täitmisfaili ametlikku SHA-256 räsi koos kõigi teiste välja lastud pakettide räsidega. Teine väljalaskefail sisaldab erinevate panustajate allkirju väljalaskefailil pakettide räsidega. Mõlemad need väljalaskefailid peaksid asuma Bitcoin Core'i veebisaidil.
5. Järgmiseks peate arvutama allalaaditud täitmisfaili SHA-256 räsi oma arvutis Bitcoin Core'i veebisaidilt. Seejärel võrrelge seda tulemust ametliku paketi räsi tulemusega täitmisfailile. Need peaksid olema samad.
6. Lõpuks peate kontrollima, et üks või mitu väljalaskefailil ametlike pakettide räsidega digitaalallkirja vastab tõepoolest ühele või mitmele teie poolt imporditud avalikule võtmele (Bitcoin Core'i väljalasked ei ole alati kõigi poolt allkirjastatud). Seda saate teha rakendusega nagu Kleopetra.

Selle tarkvara kontrollimise protsessi kaks peamist eelist on järgmised. Esiteks tagab see, et Bitcoin Core'i veebisaidilt allalaadimisel ei esinenud edastusvigu. Teiseks tagab see, et ükski ründaja ei oleks suutnud teid panna alla laadima muudetud, pahatahtlikku koodi, kas häkkides Bitcoin Core'i veebisaiti või pealt kuulates liiklust.

Kuidas täpselt kaitseb ülaltoodud tarkvara kontrollimise protsess neid probleeme vastu?

Kui te hoolikalt kontrollisite importitud avalikke võtmeid, siis võite olla üsna kindel, et need võtmed on tõepoolest nende omad ja ei ole kompromiteeritud. Arvestades, et digitaalallkirjadel on eksistentsiaalne võltsimiskindlus, teate, et ainult need panustajad oleksid saanud teha digitaalallkirja ametlike pakettide räsidega väljalaskefailil.

Eeldades, et väljalaskefailil olevad allkirjad kontrolluvad. Nüüd saate võrrelda lokaalselt arvutatud räsi väärtust Windowsi täitmisfailile, mille alla laadisite, sellega, mis on korrektselt allkirjastatud väljalaskefailis. Kuna teate, et SHA-256 räsifunktsioon on kokkupõrkekindel, tähendab vastavus, et teie täitmisfail on täpselt sama kui ametlik täitmisfail.

Pöördugem nüüd räsifunktsioonide teise levinud omaduse juurde: varjamine. Iga räsifunktsioon H peetakse varjatuse omadusega, kui suvaliselt valitud x puhul väga suurest vahemikust on x leidmine H(x) antud korral teostamatu.
Allpool näete SHA-256 väljundit sõnumist, mille kirjutasin. Et tagada piisav juhuslikkus, sisaldas sõnum lõpus juhuslikult genereeritud tähemärkide jada. Kuna SHA-256 omab varjamisomadust, ei suudaks keegi seda sõnumit dešifreerida.
* b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded

Kuid ma ei jäta teid põnevuses, kuni SHA-256 muutub nõrgemaks. Algne sõnum, mille kirjutasin, oli järgmine:

* “See on väga juhuslik sõnum, või noh üsna juhuslik. See algusosa ei ole, kuid ma lõpetan mõningate suhteliselt juhuslike tähemärkidega, et tagada väga ettearvamatu sõnum. XLWz4dVG3BxUWm7zQ9qS”.

Tavaline viis, kuidas varjamisomadusega räsifunktsioone kasutatakse, on paroolihalduses (kokkupõrkekindlus on samuti selle rakenduse jaoks oluline). Iga korralik veebipõhine kontopõhine teenus nagu Facebook või Google ei salvesta teie paroole otse, et hallata juurdepääsu teie kontole. Selle asemel salvestavad nad ainult parooli räsi. Iga kord, kui te brauseris oma parooli sisestate, arvutatakse esmalt räsi. Ainult see räsi saadetakse teenusepakkuja serverisse ja võrreldakse tagaotsas asuva andmebaasi salvestatud räsi väärtusega. Varjamisomadus aitab tagada, et ründajad ei saa seda räsi väärtusest taastada.

Paroolihaldus räside kaudu toimib muidugi ainult siis, kui kasutajad valivad tegelikult keerulisi paroole. Varjamisomadus eeldab, et x on valitud juhuslikult väga suurest vahemikust. Paroolide valimine nagu “1234”, “minuparool” või teie sünnikuupäev ei paku mingit tegelikku turvalisust. Olemas on pikad nimekirjad levinud paroolidest ja nende räsidest, mida ründajad saavad ära kasutada, kui nad kunagi saavad kätte teie parooli räsi. Selliseid rünnakuid tuntakse **sõnaraamatu rünnakutena**. Kui ründajad teavad mõningaid teie isiklikke andmeid, võivad nad samuti teha mõningaid teadlikke oletusi. Seega vajate alati pikki, turvalisi paroole (eelistatavalt pikki, juhuslikke jadasid paroolihaldurist).

Mõnikord võib rakendus vajada räsifunktsiooni, mis omab nii kokkupõrkekindlust kui ka varjamist. Kuid kindlasti mitte alati. Näiteks tarkvara kontrollimise protsess, millest rääkisime, nõuab ainult, et räsifunktsioon näitaks kokkupõrkekindlust, varjamine ei ole oluline.

Kuigi kokkupõrkekindlus ja varjamine on krüptograafias räsifunktsioonide otsitavad peamised omadused, võivad teatud rakendustes olla soovitavad ka muud tüüpi omadused.

### Märkused
[^1]: Whitfield Diffie ja Martin Hellman, “New directions in cryptography,” *IEEE Transactions on Information Theory* IT-22 (1976), lk. 644–654, lk. 644 [^1].

[^2]: Ralph Merkle arutleb ka võtmevahetuse protokolli üle “Secure communications over insecure channels”, *Communications of the Association for Computing Machinery*, 21 (1978), 294–99. Kuigi Merkle esitas selle artikli enne Diffie ja Hellmani oma, avaldati see hiljem. Merkle'i lahendus ei ole eksponentsiaalselt turvaline, erinevalt Diffie-Hellmani omast [^2].

[^3]: Ron Rivest, Adi Shamir ja Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, *Communications of the Association for Computing Machinery*, 21 (1978), lk. 120–26 [^3].

[^4]: Hea ülevaate nendest avastustest pakub Simon Singh, *The Code Book*, Fourth Estate (London, 1999), 6. peatükk [^4].
[^5]: Iga skeem, mis püüab saavutada vaidlustamatust, teine teema, mida arutasime *1. peatükis*, peab oma alusel hõlmama digitaalseid allkirju [^5].
[^6]: Terminoloogia "peitmine" ei ole üldkeel, vaid on võetud spetsiifiliselt Arvind Narayanani, Joseph Bonneau, Edward Felteni, Andrew Milleri ja Steven Goldfederi teosest *Bitcoin ja krüptorahatehnoloogiad*, Princeton University Press (Princeton, 2016), 1. peatükk [^6].

# RSA krüptosüsteem
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

Kuigi sümmeetriline krüptograafia on enamiku inimeste jaoks tavaliselt üsna intuitiivne, ei kehti see tavaliselt asümmeetrilise krüptograafia kohta. Kuigi olete tõenäoliselt mugav kõrgtasemel kirjeldusega, mida pakuti eelmistes jaotistes, mõtlete tõenäoliselt, mis täpselt on ühesuunalised funktsioonid ja kuidas neid kasutatakse asümmeetriliste skeemide konstrueerimiseks.

Sel peatükil eemaldan mõningad müsteeriumid, mis ümbritsevad asümmeetrilist krüptograafiat, vaadeldes sügavamalt konkreetset näidet, nimelt RSA krüptosüsteemi. Esimeses jaotises tutvustan faktoriseerimisprobleemi, millel RSA probleem põhineb. Seejärel käsittelen mitmeid olulisi tulemusi arvuteooriast. Viimases jaotises paneme selle teabe kokku, et selgitada RSA probleemi ja kuidas seda saab kasutada asümmeetriliste krüptograafiliste skeemide loomiseks.

Selle sügavuse lisamine meie arutellu ei ole lihtne ülesanne. See nõuab üsna mitme arvuteoreetilise teoreemi ja ettepaneku tutvustamist. Kuid ärge laske matemaatikal end heidutada. Selle arutelu läbitöötamine parandab oluliselt teie mõistmist, mis on asümmeetrilise krüptograafia aluseks, ja on väärt investeering.

Vaadelgem nüüd esmalt faktoriseerimisprobleemi.

## Faktoriseerimisprobleem
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Kui korrutate kaks arvu, ütleme a ja b, nimetame arve a ja b **teguriteks** ning tulemust **korrutiseks**. Katse kirjutada arv N kahe või enama teguri korrutisena nimetatakse **faktoriseerimiseks** või **faktoriseerimiseks**.<sup>[1](#footnote1)</sup> Iga probleemi, mis seda nõuab, võite nimetada **faktoriseerimisprobleemiks**.

Umbes 2500 aastat tagasi avastas Kreeka matemaatik Euclid Aleksandriast võtmeteoreemi täisarvude faktoriseerimise kohta. Seda nimetatakse tavaliselt **ainulaadse faktoriseerimise teoreemiks** ja see väidab järgmist:

*Teoreem 1*. Iga täisarv N, mis on suurem kui 1, on kas algarv või seda saab väljendada algarvude korrutisena.

Kogu selle väite hilisem osa tähendab lihtsalt seda, et võite võtta mis tahes mitte-algarvu N, mis on suurem kui 1, ja kirjutada selle välja algarvude korrutisena. Allpool on mitu näidet mitte-algarvudest, mis on kirjutatud algarvude korrutistena.

* 18 = 2 • 3 • 3 = 2 • 3<sup>2</sup>
* 84 = 2 • 2 • 3 • 7 = 2<sup>2</sup> • 3 • 7
* 144 = 2 • 2 • 2 • 2 • 3 • 3 = 2<sup>4</sup> • 3<sup>2</sup>
Kõigi kolme eelmainitud täisarvu puhul on nende algarvudeks jagamine suhteliselt lihtne, isegi kui on antud ainult N. Alustate väikseimast algarvust, nimelt 2, ja vaatate, mitu korda täisarv N on jagatav sellega. Seejärel liigute edasi, testides N jagatavust 3, 5, 7 jne. Jätkate seda protsessi, kuni teie täisarv N on kirjutatud ainult algarvude korrutisena.
Võtame näiteks täisarvu 84. Allpool näete protsessi selle algarvudeks jagamiseks. Igal sammul võtame välja väikseima järelejäänud algarvu (vasakul) ja määrame ülejäänud jagatava osa. Jätkame, kuni ülejäänud osa on samuti algarv. Igal sammul kuvatakse 84 praegune tegurdus paremal ääres.

* Algarv = 2: ülejäänud osa = 42 	(84 = 2 • 42)
* Algarv = 2: ülejäänud osa = 21 	(84 = 2 • 2 • 21)
* Algarv = 3: ülejäänud osa = 7 		(84 = 2 • 2 • 3 • 7)
* Kuna 7 on algarv, on tulemus 2 • 2 • 3 • 7 ehk 2<sup>2</sup> • 3 • 7.

Oletame nüüd, et N on väga suur. Kui keeruline oleks N jagada selle algarvudeks?

See sõltub tegelikult N-st. Oletame näiteks, et N on 50,450,400. Kuigi see number tundub hirmutav, ei ole arvutused nii keerulised ja neid saab kergesti teha käsitsi. Nagu eespool, alustate lihtsalt 2-st ja töötate edasi. Allpool näete selle protsessi tulemust sarnasel viisil nagu eespool.

* 2: 25,225,200 	(50,450,400 = 2 • 25,225,200)  
* 2: 12,612,600 	(50,450,400 = 2<sup>2</sup> • 12,612,600)  
* 2: 6,306,300 		(50,450,400 = 2<sup>3</sup> • 6,306,300)  
* 2: 3,153,150 		(50,450,400 = 2<sup>4</sup> • 3,153,150)  
* 2: 1,576,575 		(50,450,400 = 2<sup>5</sup> • 1,576,575)  
* 3: 525,525 		(50,450,400 = 2<sup>5</sup> • 3 • 525,525)
* 3: 175,175 		(50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 175,175)
* 5: 35,035 		(50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5 • 35,035)
* 5: 7,007		    (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7,007)
* 7: 1,001		    (50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7 • 1,001)* 7: 143			(50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 143)
* 11: 13			(50,450,400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13)
* Kuna 13 on algarv, on tulemus 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13.

Selle probleemi käsitsi lahendamine võtab aega. Arvuti suudab muidugi seda teha murdosa sekundist. Tegelikult suudab arvuti tihti isegi väga suuri täisarve murdosa sekundist faktoriseerida.

Siiski on teatud erandid. Oletame, et valime esmalt juhuslikult kaks väga suurt algarvu. Tavaliselt tähistatakse neid p ja q-ga ning ma järgin siin seda konventsiooni.

Konkreetsuse huvides öelgem, et p ja q on mõlemad 1024-bitised algarvud ja et nende esitamiseks on tõepoolest vaja vähemalt 1024 bitti (nii et esimene bitt peab olema 1). Seega näiteks 37 ei saaks olla üks algarvudest. Sa võid kindlasti esitada 37 1024 bitiga. Kuid ilmselgelt *ei vaja* sa nii palju bitte selle esitamiseks. Sa võid esitada 37 mis tahes jadaga, mis on 6 bitti või rohkem. (6 bitis oleks 37 esitatud kui 100101).

On oluline mõista, kui suured on p ja q, kui need on valitud ülaltoodud tingimustel. Näitena olen valinud juhusliku algarvu, mis vajab esitamiseks vähemalt 1024 bitti allpool.

* 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589

Oletame nüüd, et pärast algarvude p ja q juhuslikku valimist korrutame need, et saada täisarv N. See viimane täisarv on seega 2048-bitine number, mis nõuab esitamiseks vähemalt 2048 bitti. See on palju, palju suurem kui kas p või q.
Kujutage ette, et annate arvutile ainult N ja palute tal leida kaks 1024-bitist algarvu tegurit N-st. Tõenäosus, et arvuti avastab p ja q, on äärmiselt väike. Võib öelda, et kõik praktilised eesmärgid on see võimatu. See kehtib isegi siis, kui kasutaksite superarvutit või isegi superarvutite võrku.

Alustuseks kujutage ette, et arvuti üritab probleemi lahendada, läbides 1024-bitiseid numbreid, testides igal juhul, kas need on algarvud ja kas need on N tegurid. Testitavate algarvude hulk on siis ligikaudu 1.265 • 10<sup>305</sup>.<sup>[2](#footnote2)</sup>

Isegi kui võtate kõik planeedi arvutid ja panete nad sel viisil 1024-bitiseid algarve otsima ja testima, oleks miljardist ühe võimalusega edukalt leida N algarvuline tegur vajalik arvutusperiood palju pikem kui Universumi vanus.

Praktikas suudab arvuti paremini toimida kui just kirjeldatud robustne protseduur. On olemas mitu algoritmi, mida arvuti saab rakendada, et jõuda tegurite lahutamiseni kiiremini. Punkt on siiski selles, et isegi nende tõhusamate algoritmide kasutamisel on arvuti ülesanne endiselt arvutuslikult teostamatu.<sup>[3](#footnote3)</sup>

Oluline on, et just kirjeldatud tingimustel põhineva tegurdamise raskus põhineb eeldusel, et ei ole olemas arvutuslikult tõhusaid algoritme algarvuliste tegurite arvutamiseks. Me ei saa tegelikult tõestada, et tõhus algoritm ei eksisteeri. Siiski on see eeldus väga usutav: hoolimata sadu aastaid kestnud ulatuslikest jõupingutustest pole me veel leidnud sellist arvutuslikult tõhusat algoritmi.

Seega võib teatud asjaoludel tegurdamise probleemi usutavalt pidada raskeks probleemiks. Eriti siis, kui p ja q on väga suured algarvud, nende korrutise N arvutamine ei ole keeruline; kuid tegurdamine ainult N alusel on praktiliselt võimatu.

## Arvuteoreetilised tulemused
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Kahjuks ei saa tegurdamise probleemi otseselt kasutada asümmeetriliste krüptograafiliste skeemide jaoks. Siiski saame kasutada keerukamat, kuid sellega seotud probleemi: RSA probleemi.

RSA probleemi mõistmiseks peame mõistma mitmeid teoreeme ja propositsioone arvuteooriast. Need on esitatud selles jaotises kolmes alajaotises: (1) N järjekord, (2) pööratavus modulo N ja (3) Euleri teoreem.

Mõned selles kolmes alajaotises juba tutvustatud materjalid on esitatud *peatükis 3*. Kuid ma esitan siin need materjalid mugavuse huvides uuesti.

### N järjekord

Täisarv a on **võõrarv** või **suhteline algarv** täisarvuga N, kui nende vaheline suurim ühistegur on 1. Kuigi 1 ei ole tavapäraselt algarv, on see iga täisarvu võõrarv (nagu ka – 1).

Näiteks, kui a = 18 ja N = 37. Need on selgelt võõrarvud. Suurim täisarv, mis jagab nii 18 kui ka 37, on 1. Vastupidisel juhul, kui a = 42 ja N = 16. Need ei ole selgelt võõrarvud. Mõlemad numbrid on jagatavad 2-ga, mis on suurem kui 1.
Nüüd saame määratleda N järjekorra järgmiselt. Eeldame, et N on täisarv, mis on suurem kui 1. **N järjekord** on siis kõikide N-ga vastastikku algarvuliste arvude hulk, nii et iga sellise algarvu a puhul kehtib järgmine tingimus: 1 ≤ a < N.
Näiteks, kui N = 12, siis 1, 5, 7 ja 11 on ainsad algarvud, mis vastavad ülaltoodud nõudele. Seega on 12 järjekord võrdne 4-ga.

Eeldame, et N on algarv. Siis iga täisarv, mis on väiksem kui N, kuid suurem või võrdne 1-ga, on sellega algarvuline. See hõlmab kõiki elemente järgmises hulgas: {1,2,3….,N – 1}. Seega, kui N on algarv, on N järjekord N – 1. See on väljendatud propositsioonis 1, kus φ(N) tähistab N järjekorda.

**Propositsioon 1**. φ(N) = N – 1, kui N on algarv

Eeldame, et N ei ole algarv. Siis saate selle järjekorda arvutada kasutades **Euleri fi funktsiooni**. Kuigi väikese täisarvu järjekorra arvutamine on suhteliselt lihtne, muutub Euleri fi funktsioon eriti oluliseks suuremate täisarvude puhul. Euleri fi funktsiooni propositsioon on väljendatud allpool.

*Teoreem 2*. Olgu N võrdne p<sub>1</sub><sup>e_1</sup> • p<sub>2</sub><sup>e_2</sup> • … • p<sub>i</sub><sup>e_i</sup> • … • p<sub>n</sub><sup>e_n</sup>, kus hulk {p<sub>i</sub>} koosneb kõigist N erinevatest algarvulistest teguritest ja iga e_i näitab, mitu korda algarvuline tegur p<sub>i</sub> N-s esineb. Siis φ(N) = p<sub>1</sub><sup>e_1 - 1</sup> • (p<sub>1</sub> - 1) • p<sub>2</sub><sup>e_2 - 1</sup> • (p<sub>2</sub> - 1) • … • p<sub>n</sub><sup>e_n - 1</sup> • (p<sub>n</sub> - 1).

*Teoreem 2* näitab, et kui olete mittelgarvu N jaotanud selle erinevateks algarvulisteks teguriteks, on N järjekorra arvutamine lihtne.

Näiteks, eeldame, et N = 270. See ei ole selgelt algarv. N jagamine selle algarvulisteks teguriteks annab väljendi: 2 • 3<sup>3</sup> • 5. Euleri fi funktsiooni kohaselt on N järjekord siis järgmine:

* φ(N) = 2<sup>1 – 1</sup> (2 – 1) + 3<sup>3 – 1</sup> (3 – 1) + 5<sup>1 – 1</sup> (5 – 1) = 1 (1) + 9 (2) + 1 (4) = 1 + 18 + 4 = 23
Eeldame järgnevalt, et N on kahe algarvu, p ja q, korrutis. *Teoreem 2* ülal, seega, väidab, et N järjekord on järgmine: p<sup>1 – 1</sup> (p – 1) x q<sup>1 – 1</sup> (q – 1) = (p – 1) x (q – 1). See on RSA probleemi jaoks eriti oluline tulemus ja on väljendatud *Propositsioonis 2* allpool.
*Propositsioon 2*. Kui N on kahe algarvu, p ja q, korrutis, siis N järjekord on toote (p – 1) x (q – 1).

Illustratsiooniks eeldame, et N = 119. See täisarv on faktoriseeritav kaheks algarvuks, nimelt 7 ja 17. Seega, Euleri Fi funktsioon viitab sellele, et 119 järjekord on järgmine:

* φ(119) = (7 – 1) • (17 – 1) = 6 • 16 = 96.

Teisisõnu, täisarvul 119 on vahemikus 1 kuni 119 kokku 96 koalgarvu. Tegelikult hõlmab see komplekt kõiki täisarve 1-st kuni 119-ni, mis ei ole kordajad kas 7 või 17.

Edaspidi tähistame N järjekorda määravat koalgarvude komplekti kui **C<sub>N</sub>**. Meie näites, kus N = 119, on komplekt **C<sub>119</sub>** liiga suur, et seda täielikult loetleda. Kuid mõned elemendid on järgmised: **C<sub>119</sub>** = {1,2,….6,8….13,15,16,18,….,33,35….,96}.

### Pööratavus modulo N

Võime öelda, et täisarv a on **pööratav modulo N**, kui eksisteerib vähemalt üks täisarv b nii, et a x b modulo N = 1 modulo N. Iga selline täisarv b nimetatakse a **inversiks** (või **korrutise inversiks**) antud reduktsiooni järgi modulo N.

Eeldame näiteks, et a = 5 ja N = 11. On palju täisarve, millega saab korrutada 5, nii et 5 x b mod 11 = 1 mod 11. Kaaluge näiteks täisarve 20 ja 31. On lihtne näha, et mõlemad need täisarvud on 5 inversid reduktsiooni modulo 11 jaoks.

* 5 x 20 mod 11 = 100 mod 11 = 1 mod 11
* 5 x 31 mod 11 = 155 mod 11 = 1 mod 11

Kuigi 5-l on palju inverse modulo 11 järgi, võib näidata, et eksisteerib ainult üks positiivne 5 invers, mis on väiksem kui 11. Tegelikult ei ole see ainulaadne meie konkreetsele näitele, vaid üldine tulemus.

*Propositsioon 3*. Kui täisarv a on pööratav modulo N, peab olema nii, et täpselt üks positiivne a invers on väiksem kui N. (Seega, see ainulaadne a invers peab tulema komplektist {1,…,N – 1}).
Märgime Proposition 3 unikaalset pöördväärtust a jaoks kui a<sup>-1</sup>. Juhtumi puhul, kui a = 5 ja N = 11, näete, et a<sup>-1</sup> = 9, arvestades, et 5 x 9 mod 11 = 45 mod 11 = 1 mod 11. 
Pange tähele, et meie näites saate väärtuse 9 a<sup>-1</sup> jaoks lihtsalt saada, vähendades mis tahes muud a pöördväärtust modulo 11 järgi. Näiteks 20 mod 11 = 31 mod 11 = 9 mod 11. Seega, kui täisarv a > N on pööratav modulo N järgi, siis a mod N peab samuti olema pööratav modulo N järgi.

See ei ole tingimata nii, et a pöördväärtus eksisteerib modulo N järgi vähendamisel. Oletame näiteks, et a = 2 ja N = 8. Pole ühtegi b-d, ega konkreetset a<sup>-1</sup>, nii et 2 x b mod 8 = 1 mod 8. See on seetõttu, et mis tahes b väärtus toodab alati 2 kordset, nii et jagamine 8-ga ei saa kunagi anda jääki, mis võrdub 1-ga.

Kuidas me täpselt teame, kas mõnel täisarvul a on pöördväärtus antud N jaoks? Nagu te võisite eespool märgitud näites märgata, suurim ühistegur 2 ja 8 vahel on suurem kui 1, nimelt 2. Ja see on tegelikult järgmise üldise tulemuse illustratsioon:

*Proposition 4*. Täisarvul a on pöördväärtus antud modulo N järgi vähendamisel, ja eriti unikaalne positiivne pöördväärtus, mis on väiksem kui N, kui ja ainult siis, kui suurim ühistegur a ja N vahel on 1 (st, kui nad on teineteisega koprimeed).

Juhtumi puhul, kui a = 5 ja N = 11, jõudsime järeldusele, et a<sup>-1</sup> = 9, arvestades, et 5 x 9 mod 11 = 45 mod 11 = 1 mod 11. On oluline märkida, et vastupidine on samuti tõsi. See tähendab, kui a = 9 ja N = 11, siis on tõsi, et a<sup>-1</sup> = 5.

### Euleri teoreem

Enne RSA probleemi juurde liikumist peame mõistma veel üht olulist teoreemi, nimelt **Euleri teoreemi**. See väidab järgmist:

*Theorem 3*. Eeldame, et kaks täisarvu a ja N on koprimeed. Siis, a<sup>φ(N)</sup> mod N = 1 mod N.

See on märkimisväärne tulemus, kuid esmapilgul veidi segadusttekitav. Pöördume näite poole, et seda mõista.

Oletame, et a = 5 ja N = 7. Need on tõepoolest koprimeed, nagu Euleri teoreem nõuab. Me teame, et 7 järjekord on 6, arvestades, et 7 on algarv (vt **Proposition 1**).

Mida Euleri teoreem nüüd väidab, on see, et 5<sup>6</sup> mod 7 peab olema võrdne 1 mod 7-ga. Allpool on arvutused, mis näitavad, et see on tõepoolest tõsi.

* 5<sup>6</sup> mod 7 = 15,625 mod 7 = 1 mod N

Täisarv 7 jagab 15,624 kokku 2,233 korda. Seega, jagades 16,625 7-ga, on jääk 1.

Järgmisena, kasutades Euleri Phi funktsiooni, *Theorem 2*, saate tuletada allpool toodud *Proposition 5*.
*Ettepanek 5*. φ(a • b) = φ(a) • φ(b) iga positiivse täisarvu a ja b korral.
Me ei näita, miks see nii on. Kuid märgime lihtsalt, et olete juba näinud selle ettepaneku tõestust asjaolust, et φ(p • q) = φ(p) • φ(q) = (p – 1) • (q – 1), kui p ja q on algarvud, nagu on öeldud *Ettepanekus 2*.

Euleri teoreem koos *Ettepanekuga 5* omab olulisi tagajärgi. Vaadake, mis juhtub näiteks alljärgnevates avaldistes, kus a ja N on teineteisega algarvulised.

* a<sup>2 • φ(N)</sup> mod N = a<sup>φ(N)</sup> • a<sup>φ(N)</sup> mod N = 1 • 1 mod N = 1 mod N
* a<sup>φ(N) + 1</sup> mod N = a<sup>φ(N)</sup> • a<sup>1</sup> mod N = 1 • a<sup>1</sup> mod N = a mod N
* a<sup>8 • φ(N) + 3</sup> mod N = a<sup>8 • φ(N)</sup> • a<sup>3</sup>  mod N = 1 • a<sup>3</sup>  mod N = a<sup>3</sup>  mod N

Seega Euleri teoreemi ja *Ettepaneku 5* kombinatsioon võimaldab meil lihtsalt arvutada mitmeid avaldisi. Üldiselt võime kokkuvõtte teha *Ettepanekus 6*.

*Ettepanek 6*. a<sup>x</sup> mod N = a<sup>x mod φ(N)</sup>

Nüüd peame kõik kokku panema keerulises viimases sammus.

Nii nagu N-l on järjekord φ(N), mis sisaldab hulga **C<sub>N</sub>** elemente, teame, et täisarvul φ(N) peab omakorda samuti olema järjekord ja hulk algarvulisi. Olgu φ(N) = R. Siis teame, et on olemas ka väärtus φ(R) ja hulk algarvulisi **C<sub>R</sub>**.

Eeldame, et valime nüüd täisarvu e hulgast **C<sub>R</sub>**. Me teame *Ettepanekust 3*, et sellel täisarvul e on ainult üks unikaalne positiivne pöördväärtus, mis on väiksem kui R. See tähendab, et e-l on üks unikaalne pöördväärtus hulgast **C<sub>R</sub>**. Nimetame selle pöördväärtuse d-ks. Pöördväärtuse definitsiooni järgi tähendab see, et e • d = 1 mod R.

Seda tulemust saame kasutada meie algse täisarvu N kohta avalduse tegemiseks. See on kokkuvõtlikult öeldud *Ettepanekus 7*.

*Ettepanek 7*. Eeldame, et e • d mod φ(N) = 1 mod φ(N). Siis iga elemendi a korral hulgast **C<sub>N</sub>** peab kehtima, et a<sup>e • d mod φ(N)</sup> = a<sup>1 mod φ(N)</sup> = a mod N.

Nüüd on meil kõik arvuteoreetilised tulemused, mis on vajalikud RSA probleemi selgeks sõnastamiseks.


## RSA krüptosüsteem
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>
Oleme nüüd valmis tutvustama RSA probleemi. Kujutage ette, et loote muutujate komplekti, mis koosneb p-st, q-st, N-st, φ(N)-st, e-st, d-st ja y-st. Nimetagem seda komplekti Π-ks. See luuakse järgmiselt:
1. Genereerige kaks juhuslikku algarvu p ja q võrdse suurusega ning arvutage nende korrutis N.
2. Arvutage N-i järk, φ(N), järgneva korrutise abil: (p – 1) • (q – 1).
3. Valige e > 2 nii, et see oleks väiksem ja teineteisest võõras φ(N)-ga.
4. Arvutage d, seades e • d mod φ(N) = 1.
5. Valige juhuslik väärtus y, mis on väiksem ja teineteisest võõras N-ga.

RSA probleem seisneb sellise x leidmises, et x^e = y, olles antud ainult osaline teave Π kohta, nimelt muutujad N, e ja y. Kui p ja q on väga suured, tavaliselt soovitatakse, et need oleksid 1024 bitti suurused, peetakse RSA probleemi raskeks. Nüüd saate aru, miks see nii on, arvestades eelnevat arutelu.

Lihtne viis x arvutamiseks, kui x^e mod N = y mod N, on lihtsalt arvutada y^d mod N. Me teame, et y^d mod N = x mod N järgmiste arvutuste põhjal:

* y^d mod N = x^(e • d) mod N = x^(e • d mod φ(N)) mod N = x^(1 mod φ(N)) mod N = x mod N.

Probleem on selles, et me ei tea väärtust d, kuna seda ei antud probleemis. Seega ei saa me otse arvutada y^d mod N, et saada x mod N.

Siiski võime olla võimelised kaudselt arvutama d väärtust N-i järjest, φ(n), kuna teame, et e • d mod φ(N) = 1 mod φ(N). Kuid eelduse kohaselt ei antud probleemis ka φ(N) väärtust.

Lõpuks võiks järge kaudselt arvutada algarvude p ja q abil, nii et lõpuks võiksime arvutada d. Kuid eelduse kohaselt ei antud meile ka p ja q väärtusi.

Rangelt öeldes, isegi kui faktoriseerimisprobleem RSA probleemi raames on raske, ei saa me tõestada, et RSA probleem on samuti raske. Võib nimelt olla muid viise RSA probleemi lahendamiseks kui faktoriseerimise kaudu. Siiski on üldiselt aktsepteeritud ja eeldatav, et kui faktoriseerimisprobleem RSA probleemi raames on raske, siis on RSA probleem ise samuti raske.

Kui RSA probleem on tõepoolest raske, siis see loob ühesuunalise funktsiooni lõksuuksega. Funktsioon siin on f(g) = g^e mod N. Teades f(g), võiks igaüks kergesti arvutada väärtuse y konkreetse g = x jaoks. Siiski on praktiliselt võimatu arvutada konkreetset väärtust x ainult teades väärtust y ja funktsiooni f(g). Erand on siis, kui teile antakse teave d, lõksuukse kohta. Sel juhul saate lihtsalt arvutada y^d, et saada x.

Lähme läbi konkreetse näite, et illustreerida RSA probleemi. Ma ei saa valida RSA probleemi, mis oleks eeltoodud tingimustel peetud raskeks, kuna numbrid oleksid kohmakad. Selle asemel on see näide lihtsalt selleks, et illustreerida, kuidas RSA probleem üldiselt toimib.
Alustuseks oletame, et valite kaks juhuslikku algarvu 13 ja 31. Seega p = 13 ja q = 31. Nende kahe algarvu korrutis N on võrdne 403-ga. Me saame kergesti arvutada 403 järku. See on võrdne (13 – 1) • (31 – 1) = 360-ga.
Järgmisena, nagu RSA probleemi kolmandas sammus nõutud, peame valima 360-le suurema kui 2 ja väiksema kui 360 oleva vastastikuse algarvu. Me ei pea seda väärtust juhuslikult valima. Oletame, et valime 103. See on 360 vastastikune algarv, kuna selle suurim ühistegur 103-ga on 1.

Nüüd nõuab samm 4, et arvutaksime väärtuse d nii, et 103 • d mod 360 = 1. See ei ole käsitsi lihtne ülesanne, kui N väärtus on suur. See nõuab, et kasutaksime protseduuri, mida nimetatakse **laiendatud Eukleidese algoritmiks**.

Kuigi ma ei näita protseduuri siin, annab see tulemuseks 7, kui e = 103. Võite kontrollida, et väärtuste paar 103 ja 7 tõepoolest vastab üldtingimusele e • d mod φ(n) = 1 allpool toodud arvutuste kaudu.

* 103 • 7 mod 360 = 721 mod 360 = 1 mod 360

Oluliselt, arvestades *Proposition 4*, teame, et ükski teine täisarv vahemikus 1 kuni 360 d jaoks ei anna tulemust, et 103 • d = 1 mod 360. Lisaks tähendab propositsioon, et e jaoks erineva väärtuse valimine annab d jaoks erineva unikaalse väärtuse.

RSA probleemi viiendas sammus peame valima mõne positiivse täisarvu y, mis on 403 väiksem vastastikune algarv. Oletame, et seame y = 2<sup>103</sup>. Kahe astendamine 103-ga annab allpool toodud tulemuse.

* 2<sup>103</sup> mod 403 = 10,141,204,801,825,835,211,973,625,643,008 mod 403 = 349 mod 403

RSA probleem selles konkreetses näites on nüüd järgmine: Teile on antud N = 403, e = 103 ja y = 349 mod 403. Nüüd peate arvutama x nii, et x<sup>103</sup> = 349 mod 403. See tähendab, et peate leidma algse väärtuse enne 103-ga astendamist, mis oli 2.

See oleks lihtne (vähemalt arvutile), arvutada x, kui teaksime, et d = 7. Sel juhul võiksite lihtsalt määrata x alljärgnevalt.

* x = y<sup>7</sup> mod 403 = 349<sup>7</sup> mod 403 = 630,634,881,591,804,949 mod 403 = 2 mod 403

Probleem on selles, et teile ei ole antud teavet, et d = 7. Loomulikult võiksite arvutada d faktist, et 103 • d = 1 mod 360. Probleem on selles, et teile ei ole antud ka teavet, et N järk = 360. Lõpuks võiksite samuti arvutada 403 järku, arvutades järgneva korrutise: (p – 1) • (q – 1). Kuid teile ei ole öeldud ka seda, et p = 13 ja q = 31.
Muidugi, arvuti suudaks selle näite RSA probleemi suhteliselt kergesti lahendada, kuna kaasatud algarvud ei ole suured. Kuid kui algarvud muutuvad väga suureks, seisab see silmitsi praktiliselt võimatu ülesandega.  
Oleme nüüd tutvustanud RSA probleemi, tingimuste kogumit, mille korral on see raske, ja aluseks olevat matemaatikat. Kuidas aitab see kõik kaasa asümmeetrilisele krüptograafiale? Eelkõige, kuidas saame muuta RSA probleemi raskuse teatud tingimustel krüpteerimisskeemiks või digitaalseks allkirjastamise skeemiks?

Üks lähenemine on võtta RSA probleem ja luua skeemid otsekohesel viisil. Näiteks, eeldame, et genereerisite muutujate komplekti Π, nagu kirjeldatud RSA probleemis, ja tagate, et p ja q on piisavalt suured. Määrate oma avaliku võtme võrdseks (N, e) ja jagate seda teavet maailmaga. Nagu eespool kirjeldatud, hoiate p, q, φ(n) ja d väärtused salajas. Tegelikult on d teie privaatvõti.

Igaüks, kes soovib teile sõnumit m saata, mis on element **C<sub>N</sub>**, võib lihtsalt krüpteerida selle järgmiselt: c = m<sup>e</sup> mod N. (Siin olev krüptotekst c on võrdne väärtusega y RSA probleemis.) Saate selle sõnumi hõlpsalt dekrüpteerida, lihtsalt arvutades c<sup>d</sup> mod N.

Võite proovida luua digitaalse allkirjastamise skeemi samal viisil. Eeldame, et soovite saata kellelegi sõnumi m digitaalse allkirjaga S. Saate lihtsalt seada S = m<sup>d</sup> mod N ja saata paari (m,S) saajale. Igaüks saab digitaalset allkirja kontrollida, lihtsalt kontrollides, kas S<sup>e</sup> mod N = m mod N. Igal ründajal oleks aga tõeliselt raske luua kehtivat S sõnumile, arvestades, et neil ei ole d.

Kahjuks ei ole RSA probleemi, mis iseenesest on raske probleem, muutmine krüptograafiliseks skeemiks nii lihtne. Otsekohese krüpteerimisskeemi puhul saate valida ainult N-ga koprimeeruvad sõnumid. See ei jäta meile palju võimalikke sõnumeid, kindlasti mitte piisavalt standardseks suhtluseks. Lisaks tuleb neid sõnumeid valida juhuslikult. See tundub veidi ebapraktiline. Lõpuks, iga kord valitud sõnum annab täpselt sama krüptoteksti. See on igasuguse krüpteerimisskeemi puhul äärmiselt ebasoovitav ja ei vasta ühelegi rangele kaasaegsele turvalisuse mõistele krüpteerimises.

Probleemid muutuvad veelgi hullemaks meie otsekohese digitaalse allkirjastamise skeemi jaoks. Nagu seisab, võib iga ründaja kergesti võltsida digitaalseid allkirju, lihtsalt esmalt valides N-ga koprimeeruva allkirja ja seejärel arvutades vastava algse sõnumi. See selgelt rikub eksistentsiaalse võltsimatu nõuet.

Siiski, lisades natuke nutikat keerukust, saab RSA probleemi kasutada turvalise avaliku võtme krüpteerimisskeemi ning turvalise digitaalse allkirjastamise skeemi loomiseks. Me ei hakka siin selliste konstruktsioonide üksikasju käsitlema.<sup>[4](#footnote4)</sup> Oluline on siiski, et see lisakomplekssus ei muuda fundamentaalset aluseks olevat RSA probleemi, millel need skeemid põhinevad.

### Märkused

[^1]: Faktoriseerimine võib olla oluline ka teiste matemaatiliste objektidega töötamisel kui ainult numbrid. Näiteks võib olla kasulik faktoriseerida polünoomilisi avaldisi nagu x^2 – 2x + 1. Meie arutelus keskendume ainult numbrite, eriti täisarvude faktoriseerimisele [^1].
[^2]: Algarvu teoreemi kohaselt on algarvude arv, mis on väiksem või võrdne N-ga, ligikaudu N/ln(N). See tähendab, et saate ligikaudselt arvutada 1024-bitiste algarvude arvu, kasutades valem 2^1024/ln(2^1024) - 2^1023/ln(2^1023), mis võrdub ligikaudu 1.265 x 10^305 [^2].

# Panused
<partId>4556aab1-4876-552a-b6db-df6837bbf27a</partId>

## Teave
<chapterId>ff08a57b-740f-5d7e-8cf2-81db0908166e</chapterId>

Igasugused panused on väga teretulnud. Enne panustamist palun tutvuge allpool oleva taustainfoga minu enda plaanide kohta raamatu jaoks ning panustamise juhistega.

### Praegused plaanid

Minu praegused plaanid raamatu edasiarendamiseks on järgmised:

- Luua viimane peatükk, mis käsitleb praktiliste krüptograafiliste rakenduste detaile, nagu transportkihi turvalisus, sibulmarsruutimine ja väärtusevahetus Bitcoinis
- Luua paremaid ja rohkem jooniseid ning diagramme kirjaliku arutelu toetamiseks
- Kasutada LaTeX Math'i või mõnda muud vormindamisrakendust formaalse notatsiooni jaoks (mitte ainult Markdown)

### Panustamise juhised

Kui teil on väiksemaid parandusi või ettepanekuid olemasoleva teksti kohta, võite luua pull request'i või tõstatada probleemi. Kui loote pull request'i, palun järgige järgmisi juhiseid:

- Looge commit'id eraldi harul teie repositooriumi fork'is
- Sildistage commit'id selgelt
- Looge eraldi commit'id loogiliselt eristatavate probleemide jaoks, et muuta ülevaatamisprotsess lihtsamaks

Kui teil on raamatu kohta olulisemaid ettepanekuid, palun tõstatage probleem või võtke minuga otse ühendust aadressil **jaburgers@protonmail.com**.

### Litsents

Selle repositooriumi töö on litsentseeritud Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0) alusel.

Litsentsi lühikirjelduse leiate [siit](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Litsentsi täisversiooni leiate [siit](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).

## Notatsioon
<chapterId>07250f8d-ad7c-5531-a70c-4417d6d1b865</chapterId>

### Võtmesõnad

Võtmesõnad tutvustatakse esiletõstmisega paksus kirjas. Näiteks Rijndaeli šifri tutvustamine võtmesõnana näeks välja järgmiselt: **Rijndaeli šiffer**.

Võtmesõnad on selgelt määratletud, välja arvatud juhul, kui need on omadnimed või nende tähendus on arutelust ilmne.

Definitsioon antakse tavaliselt võtmesõna tutvustamisel, kuigi mõnikord on mugavam jätta definitsioon hilisemaks.

### Rõhutatud sõnad ja fraasid

Sõnu ja fraase rõhutatakse kursiivis. Näiteks fraas "Pea oma parool meeles" näeks välja järgmiselt: *Pea oma parool meeles*.

### Formaalne notatsioon

Formaalne notatsioon puudutab peamiselt muutujaid, juhuslikke muutujaid ja hulki.

* Muutujad: Neid tähistatakse tavaliselt väiketähega (nt "x" või "y"). Mõnikord on need suurtähtedega selguse huvides (nt "M" või "K").
* Juhuslikud muutujad: Neid tähistatakse alati suurtähega (nt "X" või "Y").
* Komplektid: Need on alati näidatud paksus kirjas suurtähtedega (nt, **S**)