---
term: BIP
---

Akronüüm "Bitcoin Improvement Proposal" jaoks. Bitcoin Improvement Proposal (BIP) on ametlik protsess Bitcoin'i protokolli ja selle standardite paranduste ning muudatuste ettepanekute tegemiseks ja dokumenteerimiseks. Kuna Bitcoin'il ei ole keskset üksust, mis otsustaks uuenduste üle, võimaldavad BIPid kogukonnal ettepanekuid teha, arutada ja parandusi struktureeritud ja läbipaistval viisil rakendada. Iga BIP kirjeldab ettepaneku eesmärke, põhjendusi, võimalikku mõju ühilduvusele, samuti eeliseid ja puudusi. BIPe võivad kirjutada kõik kogukonna liikmed, kuid need peavad olema heaks kiidetud teiste arendajate ja toimetajate poolt, kes haldavad Bitcoin Core GitHubi andmebaasi: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun ja Ruben Somsen. Siiski on oluline mõista, et nende isikute roll BIPide toimetamisel ei tähenda, et nad kontrolliksid Bitcoin'i. Kui keegi teeb ettepaneku paranduse kohta, mis ei ole formaalses BIP raamistikus aktsepteeritud, võivad nad selle siiski otse Bitcoin'i kogukonnale esitada või isegi luua haru, mis sisaldab nende muudatust. BIP protsessi eelis seisneb selle formaalsuses ja tsentraliseerituses, mis hõlbustavad arutelu, et vältida Bitcoin'i kasutajate vahelist lõhestumist, püüdes uuendusi konsensuslikul viisil rakendada. Lõpuks on majanduslik enamus see, mis määrab protokolli võimudünaamika.

BIPid on klassifitseeritud kolme peamise kategooria alla:
* *Standards Track BIPid*: Puudutavad muudatusi, mis mõjutavad otseselt Bitcoin'i rakendusi, nagu tehingute ja plokkide valideerimise reeglid;
* *Informational BIPid*: Pakuvad teavet või soovitusi ilma otseseid muudatusi protokollis ettepanema;
* *Process BIPid*: Kirjeldavad muudatusi Bitcoin'i ümbritsevates protseduurides, nagu valitsemisprotsessid.

Standards Track ja Informational BIPid on samuti klassifitseeritud "Kihi" järgi:
* *Konsensuse Kiht*: BIPid selles kihis puudutavad Bitcoin'i konsensusreegleid, nagu muudatused ploki või tehingute valideerimise reeglites. Need ettepanekud võivad olla kas pehmed kahvlid (tagasiühilduvad muudatused) või kõvad kahvlid (mitte-tagasiühilduvad muudatused). Näiteks kuuluvad SegWit'i ja Taproot'i BIPid sellesse kategooriasse;
* *Peer Services*: See kiht puudutab Bitcoin'i sõlmede võrgu toimimist, st kuidas sõlmed leiavad ja suhtlevad üksteisega internetis.
* *API/RPC*: Selle kihi BIPid puudutavad rakendusprogrammeerimisliideseid (API) ja kaugprotseduurikutseid (RPC), mis võimaldavad Bitcoin'i tarkvaral sõlmedega suhelda;
* *Rakenduste Kiht*: See kiht puudutab rakendusi, mis on ehitatud Bitcoin'i peale. Selles kategoorias olevad BIPid tegelevad tavaliselt muudatustega Bitcoin'i rahakoti standardite tasandil.

BIPi esitamise protsess algab idee kontseptualiseerimise ja aruteluga *Bitcoin-dev* meililistis. Kui idee on paljutõotav, koostab autor BIPi järgides kindlat formaati ja esitab selle Pull Request'ina Core GitHubi repositooriumis. Toimetajad vaatavad selle ettepaneku üle, et kontrollida, kas see vastab kõigile kriteeriumidele. BIP peab olema tehniliselt teostatav, kasulik protokollile, vastama nõutavale vormingule ja olema kooskõlas Bitcoin'i filosoofiaga. Kui BIP vastab nendele tingimustele, integreeritakse see ametlikult BIPide GitHubi repositooriumisse. Seejärel omistatakse sellele number. See number otsustatakse tavaliselt toimetaja poolt, sageli Luke Dashjr, ja see omistatakse loogiliselt: BIPid, mis tegelevad sarnaste teemadega, saavad sageli järjestikused numbrid.

BIPid läbivad oma elutsükli jooksul erinevaid staatuseid. Praegune staatus on märgitud iga BIPi päisesse:
* Mustand: Ettepanek on endiselt mustandi ja arutelu faasis;
* Pakutud: BIP peetakse lõpetatuks ja on valmis ühiskonna poolt ülevaatamiseks;
* Edasi lükatud: BIP on championi või toimetaja poolt hilisemaks ajaks kõrvale pandud;
* Tagasi lükatud: BIP klassifitseeritakse tagasi lükatuks, kui see ei ole 3 aasta jooksul ühtegi tegevust üles näidanud. Selle autor võib hiljem valida selle taasalustamise, mis võimaldaks sellel naasta mustandi staatusesse;
* Tagasi võetud: BIP on selle autori poolt tagasi võetud;
* Lõplik: BIP on vastu võetud ja laialdaselt Bitcoini peal rakendatud;
* Aktiivne: Ainult protsessi BIPide puhul, see staatus omistatakse, kui teatud konsensus on saavutatud;
* Asendatud / Aegunud: BIP ei ole enam kohaldatav või on asendatud uuema ettepanekuga, mis muudab selle tarbetuks.

![](../../dictionnaire/assets/25.png)

> ► *BIP on lühend sõnast "Bitcoin Improvement Proposal". Prantsuse keeles võib seda tõlkida kui "Proposition d'amélioration de Bitcoin". Siiski, enamik Prantsuse tekste kasutab otse lühendit "BIP" kui üldnimetust, mõnikord naissoost, mõnikord meessoost.*