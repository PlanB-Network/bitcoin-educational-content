---
term: BIP

---
Akronüüm "Bitcoin Improvement Proposal" (Bitcoini täiustamise ettepanek) Bitcoini parandusettepanek (Bitcoin Improvement Proposal, BIP) on ametlik protsess, mille käigus tehakse ettepanekuid ja dokumenteeritakse Bitcoini protokolli ja selle standardite parandusi ja muudatusi. Kuna Bitcoinil ei ole keskset üksust, kes uuenduste üle otsustaks, võimaldavad BIP-d kogukonnal teha ettepanekuid, arutada ja rakendada parandusi struktureeritud ja läbipaistval viisil. Igas piirhoiatusprogrammis kirjeldatakse üksikasjalikult kavandatava paranduse eesmärke, põhjendusi, võimalikku mõju ühilduvusele ning eeliseid ja puudusi. Piiranguid võib kirjutada iga kogukonna liige, kuid need peavad olema heaks kiidetud teiste arendajate ja Bitcoin Core GitHubi andmebaasi haldavate toimetajate poolt: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun ja Ruben Somsen. Siiski on oluline mõista, et nende isikute roll BIPi redigeerimisel ei tähenda, et nad kontrollivad Bitcoini. Kui keegi pakub välja paranduse, mis ei ole ametlikus BIPi raamistikus heaks kiidetud, võib ta selle ikkagi esitada otse Bitcoini kogukonnale või isegi luua hargnemise, mis sisaldab tema muudatust. BIP-protsessi eelis seisneb selle formaalsuses ja tsentraliseerituses, mis hõlbustab arutelu, et vältida Bitcoini kasutajate vahelist jagunemist, püüdes uuendusi rakendada konsensuslikul viisil. Lõppkokkuvõttes määrab võimu dünaamika protokollis majandusliku enamuse põhimõte.

Piirangud jagunevad kolme põhikategooriasse:


- Standardite jälgimise piiripunktid*: Puudutavad muudatusi, mis mõjutavad otseselt Bitcoini rakendusi, näiteks tehingu- ja plokkide valideerimise reegleid;
- Informatiivsed piiripunktid*: Anda teavet või anda soovitusi, ilma et pakutaks välja otseseid muudatusi protokollile;
- Protsessi piiripunktid*: Kirjeldage muudatusi Bitcoini ümbritsevates menetlustes, näiteks juhtimisprotsessides.

Standardite jälgimise ja teavitamise piiripunktid on samuti liigitatud "kihi" järgi:


- Konsensuskihi*: Selles kihis olevad BIP-d puudutavad Bitcoini konsensusreegleid, näiteks ploki või tehingu valideerimise reeglite muutmist. Need ettepanekud võivad olla kas pehmed hargnemised (tagasiühilduvad muudatused) või kõvad hargnemised (mitte tagasiühilduvad muudatused). Sellesse kategooriasse kuuluvad näiteks SegWit ja Taproot BIP-d;
- Vastastikused teenused*: See kiht on seotud Bitcoini sõlmede võrgu toimimisega, st kuidas sõlmed leiavad üksteist ja suhtlevad omavahel Internetis.
- API/RPC*: Selle kihi piiripunktid puudutavad rakendusprogrammeerimise liideseid (API) ja kaugprotseduurikõnesid (RPC), mis võimaldavad Bitcoini tarkvaral suhelda sõlmedega;
- Rakenduskihi*: See kiht puudutab Bitcoini peal ehitatud rakendusi. Selle kategooria piiripunktid tegelevad tavaliselt muudatustega Bitcoini rahakoti standardite tasandil.

Piiranguprogrammi esitamise protsess algab idee kavandamise ja arutamisega *Bitcoin-dev* meililistis. Kui idee on paljutõotav, koostab autor BIPi konkreetse formaadi järgi ja esitab selle Pull Request'i kaudu Core GitHubi repositooriumis. Redaktorid vaatavad selle ettepaneku läbi, et kontrollida, kas see vastab kõigile kriteeriumidele. BIP peab olema tehniliselt teostatav, protokollile kasulik, vastama nõutavale vormingule ja olema kooskõlas Bitcoini filosoofiaga. Kui BIP vastab nendele tingimustele, integreeritakse see ametlikult GitHubi BIPide repositooriumi. Seejärel antakse sellele number. Selle numbri otsustab tavaliselt toimetaja, sageli Luke Dashjr, ja see määratakse loogiliselt: Sarnaseid teemasid käsitlevad veebisaidid saavad sageli järjestikused numbrid.

Seejärel läbivad piiripunktid oma elutsükli jooksul erinevaid staatusi. Praegune staatus on esitatud iga piiripunkti päises:


- Eelnõu: Ettepanek on veel koostamise ja arutelu etapis;
- Kavandatud: Piirangut peetakse täielikuks ja valmis kogukonnale läbivaatamiseks;
- Edasilükatud: Piirangut ootab meister või toimetaja hilisemaks;
- Tagasilükatud: Piirangut liigitatakse tagasi lükatuks, kui see ei ole 3 aasta jooksul olnud aktiivne. Selle autor võib otsustada seda hiljem jätkata, mis võimaldaks selle tagasi viia eelnõu staatusesse;
- Tagasivõetud: Selle autor on piiritletud projekti tagasi võtnud;
- Lõplik: Bitcoini piiripunkt on aktsepteeritud ja seda rakendatakse laialdaselt;
- Aktiivne: Protsessi piiripunktide puhul määratakse see staatus pärast teatud konsensuse saavutamist;
- Asendatud / Vananenud: Piirangut ei kohaldata enam või see on asendatud uuema ettepanekuga, mis muudab selle tarbetuks.

![](../../dictionnaire/assets/25.webp)

> ► *BIP on akronüüm "Bitcoin Improvement Proposal". Prantsuse keelde saab seda tõlkida kui "Proposition d'amélioration de Bitcoin". Enamikus prantsuse keelsetes tekstides kasutatakse aga akronüümi "BIP" otse üldnimena, mõnikord feminiinses, mõnikord maskuliinses käändes.*