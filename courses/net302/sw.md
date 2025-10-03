---
name: Mitandao ya IP kutoka kwa nadharia hadi mazoezi
goal: Zuia misingi ya mitandao ya IP ili kuisanidi vyema na kuisuluhisha.
objectives: 


  - Kuelewa usanifu na uendeshaji wa protocol ya TCP/IP
  - Eleza tofauti, faida na vikwazo vya IPv4 na IPv6
  - Tambua na utofautishe kati ya aina tofauti za IP Address
  - Sanidi na uthibitishe Ip address kwenye mifumo ya Unix/Linux
  - Tumia zana kuu za uchunguzi kuchambua na kutatua matatizo ya mtandao


---

# Ujuzi Muhimu wa Kuabiri Ulimwengu wa IP


Ingia ndani ya moyo wa ulimwengu wa IP na ujipatie maarifa ya kuelewa na kudhibiti mitandao yako ipasavyo. Katika kozi hii, utajifunza kila kitu unachohitaji kujua kuhusu mitandao ya kompyuta kwa njia iliyo wazi na ya vitendo.


Utajifunza jinsi mitandao na Ip address zinavyofanya kazi, jinsi ya kutofautisha kati ya IPv4 na IPv6, jinsi ya kutambua na kutumia kategoria tofauti za Address, na jinsi ya kufahamu umuhimu kamili wa itifaki ya TCP/IP na viungo inayotengeneza kati ya Ip address, address halisi na majina ya DNS.


NET 302 inalenga zaidi wanafunzi, watumiaji wa Linux au wadadisi tu ambao wanataka kuelewa misingi ya mtandao na kuimarisha uhuru wao katika kudhibiti, kutatua na kuboresha miundomsingi.


Jiunge nasi na ugeuze maarifa yako kuwa utaalamu halisi wa kiutendaji!

___


Kozi hii ya NET 302 ni mabadiliko ya kozi *Msingi wa Mtandao: TCP/IP, IPv4 na IPv6*, iliyoandikwa kwa Kifaransa na Philippe Pierre na kuchapishwa kwenye [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), chini ya leseni ya Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).



Mabadiliko makubwa yamefanywa kwa toleo asilia na Loïc Morel: maandishi yameandikwa upya kabisa, yamepanuliwa na kuboreshwa ili kutoa maudhui yaliyosasishwa na ya kina, huku kikihifadhi ari ya elimu ya kazi asili ya Philippe Pierre. Michoro pia imerekebishwa.


+++


# Utangulizi


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Muhtasari wa kozi


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Kozi hii inatoa utangulizi kamili wa misingi ya mitandao ya IP. Imeundwa katika sehemu kuu nne, kila moja ikishughulikia kipengele muhimu cha kuelewa, kusanidi na kutambua masuala katika mtandao wa kompyuta.


### TCP/IP PROTOCOL 


Katika sehemu hii ya kwanza, tutaweka msingi kwa kuchunguza dhana ya mtandao na historia ya protocol ya TCP/IP. Tutasoma elements zake kuu: IP, TCP, pamoja na kuangalia kwa ufupi protocol ya IPv5 QoS. Pia tutashughulikia kanuni za awali za huduma ili kuelewa vyema mantiki ya ubadilishanaji wa data.


### IPv4 address 


Kisha tutaendelea hadi kwenye moduli iliyowekwa kwa IPv4 address. Utajifunza jinsi IPv4 inavyotumika katika mazoezi, aina zake tofauti za Address (faragha, umma, matangazo, n.k.), jukumu la msingi la DNS, na pia jinsi anwani za Ethaneti na itifaki ya ARP inavyofanya kazi. Pia utagundua NAT (Tafsiri ya Mtandao wa Address) na misingi ya usanidi wa mtandao.


### IPv6 address 


Sehemu ya tatu inalenga katika kushughulikia IPv6, ambayo ni muhimu kwa Address vikwazo vya IPv4. Tutapitia viwango na ufafanuzi wake, Address Assignment ndani ya mtandao wa ndani, usimamizi wa blocks za Address na uhusiano kati ya IPv6 na DNS.


### Zana za uchunguzi wa mtandao


Hatimaye, tutahitimisha kwa uwasilishaji wa zana kuu za uchunguzi wa mtandao. Hizi zitakuwezesha kuchambua, kudhibiti na kutatua malfunctions. Sehemu hii itaundwa na tabaka: Ufikiaji wa Mtandao, Mtandao, Usafiri na tabaka za Juu.


Kufikia mwisho wa kozi hii, utakuwa na maarifa ya kimsingi ya kusimamia ipasavyo miundombinu ya mtandao na kutambua matatizo yanayoweza kutokea.


Je, uko tayari kuzama katika ulimwengu wa mitandao ya kompyuta? Twende!


**KUMBUKA**: Maelezo yanatokana na mfumo wa GNU/Linux CentOS 7. Walakini, usanidi wa mtandao kwa kiasi kikubwa ni sawa wakati wa kulinganisha Debian na mfumo wa CentOS. Kwa hivyo, hatutafanya tofauti yoyote. Wakati kuna moja, tutakiambisha kwa nembo mahususi.


**N.B.**: Ukikutana na maneno yoyote usiyoyafahamu wakati wa kozi, tafadhali soma [faharasa](https://planb.network/resources/glossary) kwa ufafanuzi.



# Protocol za TCP/IP


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Mtandao ni nini?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



Katika sehemu hii ya kwanza, tutaangalia kwa kina protocol ya TCP/IP, msingi wa mawasiliano ya kisasa ya kidijitali. Tutajadili asili yake, kanuni zake za msingi, na mfumo wa kushughulikia unaotumia, ambao ni muhimu ili kuhakikisha mtiririko wa habari kati ya vifaa vilivyounganishwa.


Pia tutaeleza kwa undani vipengele vikuu vinavyounda muundo huu, na kueleza jinsi vinavyoingiliana ili kuunda mtandao unaofanya kazi, unaotegemewa na unaoweza kusambazwa. Lakini kwanza, ni muhimu kurudi kwenye dhana ya mtandao.


Etymologically, mtandao unarejelea seti ya pointi zilizounganishwa kwa kila mmoja, na kutengeneza muundo uliounganishwa. Katika mawasiliano ya simu na kompyuta, ufafanuzi huu hutafsiriwa katika kundi la vifaa (kompyuta, ruta, swichi, pointi za kufikia, n.k.) zenye uwezo wa kubadilishana data kupitia vyombo vya habari vya kimwili au visivyotumia waya. Mtandao kwa hivyo huwezesha mtiririko wa habari unaoendelea au wa mara kwa mara, kulingana na mahitaji, juu ya protocol zinazotumika na asili ya usanifu uliotumiwa.


Baada ya muda, topology kadhaa za asili zimetengenezwa ili kukidhi mahitaji tofauti ya gharama, utendakazi, uthabiti, na urahisi wa matengenezo. Hizi ni pamoja na:


- mtandao wa pete,
- mtandao wa miti,
- mtandao wa basi,
- nyota mtandao,
- mtandao wa wavu.



### Mtandao wa pete


Katika topology ya pete, vifaa vinaunganishwa kwenye kitanzi kilichofungwa: kila kituo kinaunganishwa na kinachofuata, na cha mwisho kinaunganishwa na cha kwanza. Katika usanidi huu, kila kifaa hufanya kazi kama relay, kupitisha data kwenye kiungo kinachofuata. Kulingana na aina ya mtandao, habari inaweza kuzunguka kwa mwelekeo mmoja tu, au kwa zote mbili.


Faida ya mpangilio huu iko katika unyenyekevu wa cabling yake, na kutokuwepo kwa utegemezi wa vifaa vya kati yoyote. Hata hivyo, kuendelea kwa mtandao mzima inategemea afya ya kila kipengele cha mtu binafsi: kushindwa kwa kituo kimoja kunaweza kuharibu mfumo mzima wa mawasiliano. Hii ndiyo sababu mifumo ya upunguzaji au ya kupita mara nyingi huwekwa.



![Image](assets/fr/001.webp)



### Mtandao wa miti


Mtandao wa miti, au topology ya kihierarkia, imeundwa baada ya muundo wa mti wa familia. Inajumuisha viwango vya mfululizo: node ya mizizi iliyo juu inaunganisha nodes kadhaa za ngazi ya chini, ambazo zinaweza kuunganishwa na nodes nyingine, na kadhalika.


Mpangilio huu wa daraja hufanya kazi vyema hasa kwa mitandao mikubwa inayohitaji mgawanyo wazi wa majukumu na usimamizi uliogawanywa. Hata hivyo, pia hufanya mtandao kuwa hatari kwa kushindwa kwa nodes za ngazi ya juu: kupoteza mzizi au tawi kuu kunaweza kukata sehemu nzima ya miundombinu.



![Image](assets/fr/002.webp)



### Mtandao wa bus


Katika topology ya basi, vifaa vyote vinashiriki njia sawa ya upokezaji, kwa kawaida laini ya koaxia au nyuzi macho. Kila kitengo kimeunganishwa kwa urahisi, kumaanisha kuwa hakibadilishi mawimbi, na kinaweza kutuma au kupokea data kupitia kituo hiki kilichoshirikiwa.


Faida kuu ya topolojia ya bus ni gharama ya chini ya usakinishaji, shukrani kwa njia rahisi ya kuweka kebo.  Hata hivyo, katika utekelezaji wa zamani wa msingi wa koaxial (Ethernet 10BASE2/10BASE5), kukata au kupoteza kituo kimoja kunaweza kutatiza au hata kusimamisha trafiki yote, kwani mwendelezo wa umeme wa basi na kizuizi cha kuzima havitadumishwa tena. Kuwa na kiungo kimoja cha kimwili pia ni udhaifu mkubwa: mapumziko yoyote au kosa huacha mawasiliano kwa mtandao mzima.



![Image](assets/fr/003.webp)



### Mtandao wa nyota


Topology ya nyota, pia inajulikana kama "kitovu na kuzungumza", ndiyo inayojulikana zaidi leo, haswa katika mitandao ya Ethernet ya nyumbani na ofisini. Hapa, vifaa vyote vinaunganishwa kwenye kifaa kimoja cha kati.


Mpangilio huu hurahisisha usimamizi na matengenezo: ikiwa kifaa kimoja cha pembeni kitashindwa, mtandao uliosalia hauathiriwi. Kikwazo ni kwamba kifaa cha kati ni hatua moja ya kushindwa: ikiwa inakwenda chini, mawasiliano huacha kila mahali. Ubora wa kebo na urefu wa kiungo lazima pia uzingatiwe kwa uangalifu ili kudumisha utendakazi mzuri.



![Image](assets/fr/004.webp)



**Kumbuka**: bado kuna mitandao iliyopangwa kwa mstari, topolojia inayofanana na basi, ambapo vifaa vimeunganishwa kimoja baada ya kingine. Suluhisho hili, ingawa ni la gharama ya chini kupeleka, lina shida kubwa kwamba mapumziko moja hutenga baadhi ya wapangishi, na kugawanya mtandao katika vikundi vidogo huru.


### Mtandao wa matundu


Mtandao wa matundu umeundwa kwa ajili ya upunguzaji wa juu zaidi: kila kifaa kimeunganishwa moja kwa moja kwa kila kifaa kingine. Hii inahakikisha uendelevu wa huduma hata kama viungo au vifaa vingi havifanyi kazi, kwa kuwa trafiki inaweza kuelekezwa kwenye njia mbadala.


Biashara ni kwamba idadi ya miunganisho itakayoanzishwa inaongezeka kwa kasi na idadi ya vituo. Kwa sehemu za uunganisho za `N`, viungo tofauti vya `N × (N-1) / 2` vinahitajika, na kufanya topolojia hii kuwa ghali na changamano kusambaza. Kwa hivyo inatumika hasa katika mitandao muhimu inayohitaji upatikanaji wa juu sana, kama vile sehemu fulani za Mtandao au mifumo nyeti ya viwanda.



![Image](assets/fr/005.webp)



Tofauti zingine zipo, kama vile mitandao ya gridi au hypercube, ambayo imeundwa kwa mahitaji maalum katika kompyuta iliyosambazwa au usindikaji sambamba.


Katika kiwango cha kimataifa, Intaneti ni muunganisho mkubwa wa mitandao inayotumia topolojia mbalimbali, iliyounganishwa na address za kawaida (IPv4 na IPv6) na mkusanyiko wa protocol sanifu zinazofafanuliwa na IETF (Internet Engineering Task Force) (*Kikosi Kazi cha Uhandisi Mtandaoni*). Uanuwai huu unamaanisha kuwa Mtandao haufuati topology moja: muundo wake unaweza kunyumbulika, unaweza kupanuka na huru kutokana na mpango wa kimantiki wa kushughulikia unaoifanya itumike.



## Asili ya TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Asili ya TCP protocol ni *ARPA* (Advanced Research Projects Agency, iliyopewa jina *DARPA* mnamo 1972), ambayo ilizindua mradi wa ARPANET mnamo 1966. Sehemu ya kwanza ya ARPANET ilianza kufanya kazi mnamo Oktoba 1969, ikiunganisha vyuo vikuu vya UCLA na Stanford. Kusudi lilikuwa kuunganisha vituo vya utafiti kupitia mtandao wa packet switching ambao unaweza kuwezesha mawasiliano kuendelea hata katika tukio la kuharibika kwa miundombinu.


Kama sehemu ya mabadiliko haya, ARPA ilifadhili Chuo Kikuu cha Berkeley ili kuunganisha protocol za kwanza za TCP/IP katika mfumo wake wa BSD Unix. Hii ilichukua jukumu kubwa katika kueneza na kusawazisha protocol, kwanza katika ulimwengu wa kitaaluma, na baadaye katika tasnia.


**Kumbuka**: wakati huo, wanasayansi wa kompyuta bado hawakuwa na Linux (ambayo haingeonekana hadi mapema miaka ya 1990), wala Minix, mfumo wa elimu uliobuniwa na Andrew Tanenbaum.  Chaguzi kuu zilikuwa Unix, au, wakati mwingine, fremu kuu za umiliki kama OpenVMS. Shukrani kwa unyumbufu wake na uwazi, Unix ilikuwa muhimu katika kueneza dhana za kwanza za mitandao.


Kwa kusema kweli, TCP/IP si protocol moja bali ni safu ya protocol iliyojengwa karibu na TCP na IP. Ilipata umaarufu kwa sababu ilitoa programu sanifu ya Interface ya kubadilishana data kati ya mashine kwenye mtandao mmoja. Interface hii, kulingana na primitives inayoitwa "soketi", ilifanya iwezekane kuunda miunganisho ya kuaminika na rahisi huku ikijumuisha itifaki muhimu za programu.


Kwa hivyo ARPANET ndio msingi wa kihistoria wa mtandao wa leo. Hakika, Mtandao ni mtandao wa kimataifa unaozingatia kanuni ya ubadilishaji wa pakiti, ambapo taarifa huzunguka kwa kutumia seti ya protocol sanifu zinazohakikisha utangamano na ushirikiano kati ya mifumo tofauti tofauti. Usanifu huu wazi umewezesha ukuzaji na usambazaji wa huduma na programu nyingi, pamoja na:


- barua pepe,
- World Wide Web (www),
- kuhamisha na kushiriki faili...


Utawala na mageuzi ya protocol hizi unasimamiwa na ***Internet Architecture Board*** (IAB).

Shirika hili linaratibu maelekezo ya kiufundi kupitia miundo miwili mikuu:



- **IRTF** (_Kikosi Kazi cha Utafiti wa Mtandao_), ambacho hufanya utafiti wa muda mrefu juu ya mageuzi na uboreshaji wa itifaki.
- **IETF** (_Internet Engineering Task Force_), ambayo hutengeneza, kusawazisha, na kuweka kumbukumbu za itifaki za uendeshaji zinazotumiwa kwenye Mtandao.


Usambazaji wa rasilimali za mtandao (safu za IP Address, nambari za mfumo unaojitegemea, majina ya vikoa vya mizizi, n.k.) huratibiwa kimataifa na **IANA/ICANN**. Usimamizi wa uendeshaji unategemea: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Ulaya, Mashariki ya Kati, Asia ya Kati), **ARIN**, **APNIC**, **LACNIC** na **AFRINIC**.


Vibainishi vyote vya protocol ya TCP/IP hunakiliwa katika hati zinazoitwa **RFC** (_Request for Comments_), ambazo hutumika kama marejeleo ya kiufundi yanayoidhinishwa. RFCs husasishwa kila mara na kuhesabiwa ili kuonyesha mabadiliko yanayoendelea ya safu ya itifaki.


Rafu ya TCP/IP mara nyingi huwakilishwa kama rundo la safu nne za utendaji, mara nyingi ikilinganishwa na muundo wa saba-Layer **OSI** (_Open Systems Interconnection_) uliotengenezwa na **ISO** (_International Standards Organization_), ambayo hutumika kama marejeleo ya dhana ya mtandao.


Tabaka nne za muundo wa TCP/IP ni:


- NETWORK ACCESS Layer, ambayo hutoa kiungo halisi na itifaki za udhibiti wa ufikiaji wa midia;
- INTERNET Layer, ambayo inashughulikia uelekezaji na anwani ya IP;
- TRANSPORT Layer, ambayo inahakikisha kutegemewa na usimamizi wa mtiririko wa data kwa kutumia itifaki kama vile TCP au UDP ;
- APPLICATION Layer, ambayo huunganisha pamoja itifaki za watumiaji na programu kama vile HTTP, FTP, SMTP na DNS.



![Image](assets/fr/006.webp)



Leo, toleo linalotumiwa sana la IP ni IPv4, lakini nafasi yake ya 32-bit Address ina mapungufu ya wazi. Hii ilisababisha kuundwa kwa IPv6, ambayo inatumia ushughulikiaji wa 128-bit na inatoa uwezo usio na kikomo: muhimu kwa ajili ya kusaidia ukuaji wa kulipuka wa vifaa vilivyounganishwa na kukabiliana na changamoto za Mtandao wa Mambo, uhamaji na usalama.


Kila Layer ya rundo la TCP/IP hutoa huduma mahususi, na kuifanya iwezekane kwa mahitaji mbalimbali ya mtandao ya Address kwa njia ya kawaida: maambukizi ya kimwili, ushughulikiaji wa kimantiki, uadilifu wa data, na huduma za kiwango cha programu.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## protocol ya IPv5 QoS


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



Kichwa cha pakiti ya IP ni muundo muhimu wa data, umegawanywa katika sehemu kadhaa, kila moja ikiwa na jukumu maalum la kuhakikisha kuwa pakiti zinapitishwa na kuchakatwa kwa usahihi zinaposafiri kupitia mtandao. Sehemu hizi ni pamoja na IP fikio Address (inahitajika kuelekeza pakiti kwa mpokeaji anayekusudiwa), urefu wa kichwa unaoonyeshwa na sehemu ya IHL (*Internet Header Length*), jumla ya urefu wa pakiti iliyorekodiwa katika *Uga wa Jumla ya Urefu*, maelezo ya udhibiti na uthibitishaji, na vigezo vingine vya kudhibiti mtiririko na ubora wa mawasiliano.


Sehemu ya kwanza kabisa kwenye kichwa inaitwa Toleo. Thamani hii ya 4-bit inabainisha ni toleo gani la itifaki ya IP ambalo pakiti inafuata. Ni muhimu kwa sababu inaambia kila kipanga njia au kifaa cha kati jinsi ya kutafsiri na kushughulikia data iliyoambatanishwa.


**Kumbuka**: Usimamizi na ugawaji wa matoleo ya itifaki za IP uko chini ya **IANA**. Sehemu ya biti 4 inaruhusu mchanganyiko wa tarakimu 16 (thamani 0 hadi 15). Hadi sasa, ugawaji wao ni kama ifuatavyo:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Miongoni mwa hizi ni IPv5, ambayo, ingawa haijulikani kwa umma, ilikuwepo kama ST (_Stream Protocol_). Iliyoundwa katika miaka ya 1980, IPv5 iliundwa kwa Address hitaji linalokua wakati huo: kutoa "_Ubora wa Huduma_" (QoS) kwa mtiririko fulani wa data ambao ulihitaji uwasilishaji endelevu, thabiti, kama vile mitiririko ya Voice over IP au media titika. Lengo lake lilikuwa kuhakikisha kipimo data hadi mwisho na kipaumbele, dhana sawa na kile RSVP (_Itifaki ya Uhifadhi wa Rasilimali_) inatoa leo kwa ajili ya kuhifadhi rasilimali za mtandao kwenye vipanga njia vya kisasa.


Hata hivyo, IPv5 ilisalia kuwa ya majaribio na ilitekelezwa kwa idadi ndogo tu ya vifaa vya mtandao. Kupitishwa kwake kidogo, pamoja na hitaji linalokua kwa kasi la nafasi zaidi ya Address, kulisababisha wabunifu wa Intaneti kuruka moja kwa moja kutoka IPv4 hadi IPv6. Hii iliepuka vikwazo vya IPv4 vya Address na hatari yoyote ya kuchanganyikiwa au kutopatana na vipimo vya majaribio vya IPv5.


Ingawa IPv5 haijawahi kuona matumizi mengi, ilichukua jukumu muhimu katika kuunda mawazo ya mapema kuhusu QoS na usimamizi wa trafiki. Leo, ni zaidi ya alama ya kihistoria kuliko kiwango cha kufanya kazi.


**Kikumbusho** - Itifaki ni seti ya sheria za mawasiliano: miundo ya data, algoriti, miundo ya pakiti, na kanuni zinazoruhusu vifaa tofauti kupata maelezo ya Exchange kwa uhakika na kwa kueleweka. Huduma ni utekelezaji thabiti wa itifaki kupitia programu maalum (wateja, seva) zinazofuata sheria hizi na kufanya utendaji kupatikana kwa watumiaji na programu.


Sasa tunaweza kuangalia kwa karibu muundo na uendeshaji wa itifaki ya IP, msingi muhimu wa mawasiliano yote ya mtandao.



## IP protocol


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Ufafanuzi na maelezo ya jumla


Itifaki ya IP, au "***Internet protocol***", ndiyo uti wa mgongo wa modeli ya TCP/IP. Hubeba pakiti za data kutoka kwa seva pangishi moja hadi nyingine ndani ya mtandao, iwe ya ndani au kote ulimwenguni. Ina majukumu mawili muhimu: kusimamia ushughulikiaji wa kimantiki wa vifaa, na kuhakikisha pakiti zinapitishwa kwenye mitandao ambayo mara nyingi haibadiliki na iliyounganishwa.


Katika kiwango cha kimwili, upitishaji hutegemea miingiliano ya maunzi ili kuanzisha miunganisho ya uhakika kati ya node. Hata hivyo, ni protocol ya IP inayowezesha mawasiliano kutoka mwisho hadi mwisho, na kuipa kila pakiti taarifa inayohitaji ili kupitia njia nyingi zinazowezekana hadi inapoenda.


Usanidi tatu wa mtandao wa Elements huamua jinsi pakiti inatumwa kwenye njia yake:


- **IP Address**: humtambulisha kwa njia ya kipekee mwenyeji lengwa katika mtandao.
- **Subnet Mask**: hubainisha ni sehemu gani ya address inayotambulisha mtandao na ni sehemu gani inayotambulisha seva pangishi, na kuwezesha mgawanyiko wa kimantiki katika nyavu ndogo.
- **Gateway**: linaonyesha kipanga njia cha kati ambacho pakiti inapaswa kupita ili kufikia mtandao wa nje au sehemu nyingine ya mtandao wa ndani.


Kwenye Mtandao, data haitiririki kama mtiririko mmoja unaoendelea, lakini hutumwa kama **datagram**: vizuizi huru vya data, kila kimoja kikiwa na taarifa zote zinazohitajika ili kuwasilishwa. Hii ndiyo kanuni ya **Packet switching**, ambapo maelezo hugawanywa katika vitengo vinavyojitosheleza ambavyo vinaweza kuchukua njia tofauti kumfikia mpokeaji sawa.


Kando na upakiaji (*payload*), kila data ya IP ina kichwa kilichopangwa chenye sehemu kama vile Address lengwa, chanzo cha Address, aina ya huduma, nambari ya toleo la itifaki na maelezo mengine ya udhibiti yanayohitajika ili kudhibiti utumaji.


Ukubwa wa juu zaidi wa kinadharia wa datagram ya IP ni **65,536**, ​​kikomo kilichowekwa na sehemu ya jumla ya urefu katika kichwa. Kwa mazoezi, saizi hii haifikiwi mara chache, kwani mitandao halisi inayobeba pakiti (Ethaneti, Wi-Fi, optics ya nyuzi...) kwa kawaida huweka vikomo vikali zaidi vinavyojulikana kama **MTU** (_Maximum Transmission Unit_). Ikiwa datagram inazidi MTU ya kiungo cha kimwili, lazima igawanywe katika pakiti ndogo, kila moja ikitumwa kando na kuunganishwa tena wakati wa kuwasili.


Uwezo huu wa kubadilika hufanya IP kuwa protocol thabiti na inayoweza kunyumbulika, inayoweza kufanya kazi juu ya anuwai ya teknolojia za msingi huku ikidumisha utangamano wa ulimwengu wote kati ya mifumo na mitandao tofauti tofauti.



### Kugawanyika kwa datagrams za IP


Datagram ya IP inapohitaji kupita kwenye mtandao ambao uwezo wake wa kutuma ni mdogo kuliko datagramu yenyewe, lazima iwe **imegawanywa** ili iweze kusafiri bila tatizo. Kikomo hiki cha ukubwa halisi kinaitwa **MTU** (Maximum Transmission Unit): saizi kubwa zaidi ya fremu inayoweza kupita kwenye mtandao fulani bila kugawanyika.


Kila teknolojia ya mtandao inaweka MTU yake mwenyewe, imedhamiriwa na vifaa vyake na sifa za itifaki. Maadili ya kawaida ni pamoja na:


- **ARPANET**: baiti 1000
- **Ethernet**: baiti 1500
- **FDDI**: baiti 4470


Datagram inapozidi MTU ya sehemu ya mtandao inayohitaji kuvuka, vifaa vya kuelekeza vitaigawanya katika **vipande** vidogo ambavyo vinatii kikomo. Hii hutokea kwa kawaida wakati wa kusonga kutoka kwa mtandao wa juu wa MTU hadi kwa uwezo wa chini. Kwa mfano, datagramu inayotoka kwa mtandao wa FDDI inaweza kuhitaji kugawanywa kabla ya kutumwa kwa sehemu ya Ethernet.



![Image](assets/fr/008.webp)



Mchakato wa kugawanyika hufanya kazi kama hii:


- Gateway huvunja datagramu katika vipande ambavyo si kubwa kuliko MTU ya mtandao lengwa.
- Ukubwa wa kila kipande ni mgawo wa baiti 8, kwa kuwa IP protocol hutumia kitengo hiki kusimba urekebishaji wa kuunganisha tena.
- Kila kipande hupata kichwa chake cha IP, ambacho kina maelezo yanayohitajika na mpokeaji wa mwisho ili kuviunganisha tena kwa mpangilio sahihi.


Mara baada ya kugawanyika, vipande husafiri kwa kujitegemea kupitia mtandao. Wanaweza kuchukua njia tofauti, kulingana na jedwali za kuelekeza, mizigo ya viungo, au kukatika. Hakuna hakikisho kuwa watafika kwa mpangilio waliotumwa.


Inapowasili, mashine ya kupokea hushughulikia **reassembly**. Kwa kutumia maelezo katika vichwa (kitambulishi kilichoshirikiwa, suluhu, na bendera za kugawanyika), hurejesha vipande katika mpangilio unaofaa ili kuunda upya datagram asili kabla ya kuisambaza kwa Layer inayofuata. Ikiwa hata kipande kimoja kitapotea au kupotoshwa, datagramu nzima kawaida hutupwa, bila kila kipande, matokeo hayatakuwa kamili au hayatumiki.


Ingawa ni bora, kugawanyika na kuunganisha upya huja na upande wa chini: usindikaji wa ziada kwa vipanga njia na wapangishi, na nafasi kubwa ya kupoteza pakiti, ambayo inaweza kuongeza utumaji upya. Ndio maana usimamizi makini wa MTU na uboreshaji wa saizi ya pakiti ni muhimu kwa mawasiliano laini na bora ya IP.



### Ufungaji wa data


Ili kuhakikisha kuwa data inaelekezwa kwa njia ipasavyo katika tabaka za muundo wa TCP/IP, mchakato wa **Encapsulation** una jukumu muhimu. Katika kila hatua ujumbe unaposafiri kutoka kwa programu ya mtumaji hadi kwa mashine ya mpokeaji, maelezo ya ziada, yanayojulikana kama vichwa, huongezwa. Vijajuu hivi hupeana vifaa vya kati na tabaka za programu maagizo wanayohitaji ili kuchakata, kuwasilisha, na, ikihitajika, kuunganisha upya data.


Ujumbe unapotumwa, hupitia safu nne za mrundikano wa TCP/IP. Katika kila Layer, kichwa kipya kinaongezwa mbele ya data iliyopo: kila kichwa kina metadata mahususi, kama vile address za kimantiki au halisi, bandari za mawasiliano, nambari za mfuatano, bendera za kudhibiti makosa, na taarifa yoyote inayohitajika kudhibiti utumaji na uelekezaji.


Uhamisho kwa hivyo unafuata mchakato ulioandaliwa:


- Programu ya Layer (Application Layer) huunda **ujumbe** wa awali, ulio na data ghafi.
- Transport Layer huijumuisha katika **sehemu**, na kuongeza vyanzo na bandari lengwa, nambari za mfuatano, na mbinu za kudhibiti mtiririko.
- Network Layer huongeza kwenye sehemu kichwa cha IP ili kuunda **datagram**, inayobainisha chanzo na anwani za IP.
- Network Access Layer hufunga datagramu katika **frame**, na kuongeza MAC address na misimbo ya kuangalia uadilifu (CRC).



![Image](assets/fr/009.webp)



Mchakato huu wa usimbaji huhakikisha uadilifu na ufuatiliaji wa data, na pia uwezo wake wa kubadilika: wakati wa kusonga kutoka mtandao mmoja hadi mwingine, vichwa hutoa vifaa na taarifa zinazohitajika kuchagua njia, kuangalia uhalali, au kufanya mgawanyiko ikiwa ni lazima.


Baada ya kuwasili, mchakato umebadilishwa: mashine ya kupokea inapata sura kwenye Network Access Layer, ambayo inasoma na kuondosha kichwa kinachofanana. Datagram kisha hupitishwa kwa Network Layer, ambao husoma kichwa cha IP na kuiondoa kwa zamu ili kutoa sehemu hiyo kwa Transport Layer. Transport Layer huchakata vichwa vya usafiri, hukagua uadilifu wa mtiririko, na hatimaye kuwasilisha **ujumbe** kwa programu inayolengwa katika hali yake ya asili.



![Image](assets/fr/010.webp)



Mabadiliko ya data katika kila Layer yanaweza kufupishwa kama:


- **Ujumbe (message)**: kizuizi cha habari kwenye Maombi ya Layer.
- **Segment (sehemu)**: kitengo cha data baada ya kufungwa na Usafiri Layer.
- **Datagram**: fomu iliyochukuliwa kufuatia kuongezwa kwa kichwa cha IP na Network Layer.
- **Frame**: Kizuizi cha mwisho kiko tayari kutumwa kupitia mkondo halisi na Network Access Layer.


![Image](assets/fr/011.webp)



Utaratibu huu, muhimu kwa kutegemewa na ujumuishaji wa mawasiliano ya Mtandaoni, huhakikisha kwamba kila kipande cha data, haijalishi kimegawanyika au changamano kiasi gani, kinaweza kusafirishwa kutoka mwanzo hadi mwisho huku kikiendelea kueleweka na kutumiwa na mashine inayopokea.



### IP address


Hata kukiwa na ubadilishaji wa pakiti, mgawanyiko, na uwekaji maelezo, mtandao bado haungeweza kufanya kazi bila mfumo wa kuhutubia unaotegemewa. Ili kuhakikisha kwamba kila pakiti ya data inamfikia mpokeaji sahihi, Mtandao wa Layer hutumia kitambulisho cha kipekee: **IP Address**.

Katika IPv4, IP Address imewekwa kwenye **biti 32** na imeandikwa kama nambari nne za decimal zikitenganishwa na nukta, katika umbizo la N1.N2.N3.N4 linalofahamika (kwa mfano: 192.168.1.12).


IP Address ina sehemu mbili:



- **netid**: hutambua mtandao ambao mwenyeji ni wake
- **hostid**: hutambua mwenyeji mahususi ndani ya mtandao huo

Utengano huu huruhusu Mtandao wa kimataifa kupangwa kimantiki katika mitandao mingi iliyounganishwa.


Kihistoria, mfumo wa IPv4 ulitegemea mpango wa msingi wa darasa, unaoitwa kutoka A hadi E, ambao ulifafanua aina mbalimbali za Address na matumizi yaliyokusudiwa. Kila darasa lilitenga idadi fulani ya biti kwa _netid_ na _hostid_, na kuathiri moja kwa moja idadi inayowezekana ya mitandao na wapangishaji.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Sio thamani zote zinazowezekana zinaweza kupewa wapangishaji. Kwa mfano, katika **darasa C** Address, byte ya mwisho inatoa bits 8 (maadili 256). Lakini mbili kati ya hizi zimehifadhiwa:


- 0: inabainisha mtandao wenyewe
- 255: ni **matangazo** Address, inayotumiwa kutuma pakiti kwa wapangishi wote kwenye mtandao mara moja.

Hiyo inaacha address 254 zinazoweza kutumika kwa vifaa.


Idadi ya address zinazopatikana hutofautiana sana kati ya madarasa: kutoka mitandao mikubwa ya umma katika darasa A, hadi mitandao ya ushirika katika darasa B, hadi mitandao midogo ya ndani katika darasa C.



![Image](assets/fr/013.webp)



Baadhi ya safu za Address zimehifadhiwa kwa matumizi ya kibinafsi na kamwe hazipitishwi moja kwa moja kwenye Mtandao. Hizi hujulikana kama **anwani za kibinafsi**, na hutumiwa ndani ya mashirika, biashara, au nyumba, na zinahitaji tafsiri ya Address, kwa kawaida NAT (*Network Address Translation*), ili kufikia Mtandao wa umma. Hizi ni:


- **Darasa A**: kutoka 10.0.0.0 hadi 10.255.255.255
- **Darasa B**: kutoka 172.16.0.0 hadi 172.31.255.255
- **Darasa C**: kutoka 192.168.0.0 hadi 192.168.255.255


Wakati kifaa kilicho na Address ya kibinafsi kinapofikia Mtandao, kipanga njia au lango lililowezeshwa na NAT huibadilisha na Address halali ya umma.


Mfano: Ikiwa mwenyeji ana Address **192.168.7.5**, tunaweza kukisia:


- 192.168.7.0: Network Address
- 192.168.7.1: mara nyingi Gateway ya ndani
- 192.168.7.5: mwenyeji mwenyewe


Kesi nyingine maalum ni **127.0.0.1**, inayojulikana kama "***loopback***".

Kwenye mifumo ya Linux, inahusishwa na Interface **lo**. Address hii inaruhusu mashine kutumia Address yenyewe kwa majaribio ya ndani au uchunguzi, bila kupitia Interface halisi. Masafa yote ya **127.0.0.0/8** yamehifadhiwa kwa madhumuni haya.


Ili kuboresha matumizi ya Address na kubuni mitandao changamano, **subnetmask** (_netmask_) ni muhimu. Kinyago hiki cha jozi hutenganisha _netid_ kutoka _hostid_ katika IP Address.

Kila darasa lina mask chaguo-msingi:


- **255.0.0.0** kwa darasa A,
- **255.255.0.0** kwa darasa B,
- **255.255.255.0** kwa darasa C.


Muundo mzuri wa mtandao unafuata kanuni ya msingi: vifaa vinavyopaswa kuwasiliana moja kwa moja vinapaswa kuwa katika mtandao mmoja au subnet. Ili kugawa mtandao, tunatumia subnetting, kugawa mtandao katika nyati ndogo kwa kutumia mask maalum zaidi.


Mfano wa mtandao mdogo:

Mtandao wa **darasa la C**: 192.168.1.0/24 na barakoa chaguo-msingi ya 255.255.255.0.

Tunataka subnet 4 za hadi wapangishi 60 kila moja.


**Hatua ya 1**: Idadi ya address zinazohitajika kwa kila mtandao kidogo = 60 + 2 address zilizohifadhiwa (mtandao + matangazo) = 62.


**Hatua ya 2**: Tafuta nguvu iliyo karibu zaidi ya 2 ≥ 62. -> 2⁶ = 64.


**Hatua ya 3: Rekebisha barakoa. Weka _netid_ biti na uhifadhi biti _hostid_ zinazohitajika. Tunapata mask ya binary ambayo, mara tu inabadilishwa, inatoa 255.255.255.192.**


```
11111111 11111111 11111111 11000000
```


**Hatua ya 4**: Kokotoa safu za Address kwa kila subnet, ukibadilisha biti zilizohifadhiwa kwa seva pangishi.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Hatua ya 5**: Hii inaunda mitandao midogo minne, kila moja ikisaidia hadi mashine 62, huku ikidumisha mpango wa jumla wa kushughulikia. Sehemu _hostid_ imegawanywa katika sehemu _subnetid_ na sehemu ya mwenyeji.



![Image](assets/fr/016.webp)



Kanuni hii ya msingi ya kuweka neti ndogo bado ni muhimu sana katika uhandisi wa kisasa wa mtandao, ikiruhusu ugawaji sahihi wa IP, udhibiti bora wa trafiki, utengaji mkubwa wa sehemu, na usimamizi mbaya wa mtandao.



### CIDR akihutubia


Mwanzoni mwa miaka ya 1990, mtandao ulipoenea kwa kasi kupitia biashara na mashirika, mfumo wa jadi wa anwani wa IP kulingana na madarasa (A, B, C) ulianza kuonyesha mipaka yake.

Muundo wake thabiti ulisababisha upotevu mkubwa wa anwani za IP na kufanya meza za uelekezaji kuzidi kuwa kubwa, ngumu, na ngumu kutunza.

Kwa Address masuala haya, mbinu inayoweza kunyumbulika na bora zaidi ilianzishwa: **CIDR** (_Classless Inter-Domain Routing_). CIDR imekuwa kiwango polepole, kwa kiasi kikubwa kuchukua nafasi ya mfumo wa zamani wa msingi wa darasa.


Wazo la msingi nyuma ya CIDR ni uwezo wa kuweka mitandao kadhaa iliyo karibu, haswa vizuizi vya Hatari C, kuwa kitengo kimoja cha kimantiki kiitwacho **supernet** (_supernet_). Kwa muunganisho huu, ingizo moja katika jedwali la kuelekeza linaweza kuwakilisha mitandao midogo mingi, kupunguza idadi ya njia ambazo vipanga njia zinahitaji kushughulikia na kuboresha utendakazi wao.


Ingawa mitandao ya Daraja C mwanzoni ilikuwa na hitaji kubwa la kujumlisha kwa sababu ya uwezo wao mdogo, kanuni hiyo pia imetumika kwa Daraja B na, kwa nadharia, hata mitandao ya Daraja A, ingawa mitandao hii haiathiriwi sana kutokana na safu kubwa ya Address.


Kwa CIDR, dhana ya madarasa ya kudumu hupotea. Nafasi ya Address inachukuliwa kuwa masafa endelevu ambayo yanaweza kugawanywa au kujumlishwa inavyohitajika. Vitalu vya CIDR hufafanuliwa kwa kutumia vinyago vya subnet ambavyo havizuilii kwa chaguo-msingi za madarasa ya A, B, au C. Kizuizi cha CIDR kinaweza kuwakilisha mtandao mmoja au seti ya mitandao midogo inayoshiriki kiambishi awali sawa.


Block ya CIDR imeandikwa katika muundo "Address/kiambishi awali", ambapo nambari baada ya kufyeka inaonyesha ni bits ngapi zinazounda sehemu ya mtandao. Kwa mfano, /17 ina maana kwamba bits 17 za kwanza zinatambua mtandao, wakati bits 15 zilizobaki zinatambua majeshi.


Mfano:

Block ya /17 ina address 2^(32-17) kwa hivyo 2^15 = jumla ya address 32,768. Kutoa address mbili zilizohifadhiwa (mtandao na utangazaji) huacha address 32,766 zinazoweza kutumika. Hii inaruhusu wasimamizi wa mtandao kuongeza ukubwa wa net zao ndogo kwa usahihi ili kulingana na mahitaji ya ulimwengu halisi, ili kuepuka upotevu usiohitajika.


Ili kurahisisha ukubwa wa CIDR kueleweka, hapa kuna jedwali la viambishi awali vya kawaida na vinyago sawa vya subnet na address zinazoweza kutumika:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**KUMBUKA**: Kihistoria, RFC 950 ilikataza matumizi ya subnet sufuri, hasa ili kuzuia mkanganyiko katika uelekezaji. Block hii iliondolewa na RFC 1878, ambayo inaruhusu matumizi yake kikamilifu. Block ya zamani ilitokana zaidi na kutopatana na maunzi ya zamani ambayo hayakuweza kushughulikia CIDR ipasavyo. Vifaa vya kisasa havina tatizo kama hilo.


Kwa mfano, subnet **1.0.0.0** yenye barakoa ya subnet **255.255.0.0** ambayo mara moja ilikuwa na utata na kitambulisho cha mtandao cha darasa A, sasa ni halali na kinaweza kutumika.


**KIDOKEZO**:kwa hesabu za subnet isiyo na hitilafu na ubadilishaji wa haraka wa anwani hadi nukuu za CIDR, kuna zana muhimu kama vile ***ipcalc***. "Kikokotoo hiki cha mtandao" kinaonyesha kwa uwazi uchanganuzi wa Address, safu zinazopatikana, na vinyago vinavyohusiana, bora kwa wasimamizi na wanafunzi wanaojifunza CIDR .


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## TCP Protocol 


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



**TCP Protocol** (_Transmission Control Protocol_) ina jukumu kuu katika TRANSPORT Layer ya muundo wa TCP/IP. Inafanya kazi kama daraja kati ya programu na Network Layer, kuhakikisha uhamisho wa kuaminika wa data kati ya mashine mbili za mbali.

Ingawa protocol ya IP hutuma pakiti tu bila kuhakikisha uwasilishaji au agizo, TCP inahakikisha uadilifu na uthabiti wa mtiririko wa data, ikitoa bila hasara, kwa mpangilio sahihi, na bila nakala.


Majukumu makuu ya TCP ni pamoja na:


- Kupanga upya sehemu zilizopokelewa;
- Kufuatilia mtiririko wa data ili kuepuka msongamano;
- Kugawanya au kuunganisha tena blocks za data katika vitengo vinavyofaa (sehemu);
- Kusimamia uanzishwaji na kukomesha uhusiano kati ya ncha zote mbili za mawasiliano.


TCP ni protocol inayolenga muunganisho, kumaanisha kuwa inaanzisha uhusiano wa wazi, unaoendelea kati ya mteja na seva. Ili kufanya hivyo, hutumia **nambari za mfuatano** na **shukrani**: kwa kila sehemu inayotumwa, kitambulisho cha kipekee kinawekwa ili mashine inayopokea iweze kuangalia mpangilio na uadilifu wa data. Kisha mpokeaji hurejesha sehemu ya kukiri huku **kiala** kilichowekwa kuwa 1, kuthibitisha risiti na kuashiria nambari inayofuata ya mfuatano inayotarajiwa.



![Image](assets/fr/018.webp)



Ili kuboresha kutegemewa, TCP hutumia kipima muda: mara sehemu inapotumwa, hesabu huanza. Ikiwa uthibitishaji hautafika ndani ya muda ulioisha, mtumaji hutuma tena sehemu hiyo kiotomatiki, akidhani ilipotea kwenye usafiri. Utaratibu huu wa utumaji upya wa kiotomatiki hurekebisha hasara inayopatikana kwa mitandao ya IP, ambayo inaweza kutokea katika hali ya msongamano, hitilafu za uelekezaji, au hitilafu za maunzi.



![Image](assets/fr/019.webp)



TCP ina uwezo wa kutambua na kushughulikia nakala. Ikiwa sehemu iliyotumwa tena itawasili lakini ya asili pia itaonekana, mpokeaji hutumia nambari za mfuatano kutambua nakala na kubakisha nakala sahihi pekee, kuondoa utata wowote.


Ili mchakato huu ufanye kazi, mashine zote mbili lazima zishiriki uelewa wa pamoja wa nambari zao za mfuatano wa mwanzo. Hii inahakikishwa kwa kufuata utaratibu mkali wa uunganisho: kwa upande mmoja, **seva** inasikiliza kwenye bandari maalum, kusubiri ombi linaloingia (mode passive); kwa upande mwingine, **mteja** huanzisha muunganisho kikamilifu kwa kutuma ombi kwa seva kwenye bandari hiyo hiyo ya huduma.


**KUMBUKA**: "bandari" ni kitambulisho cha nambari (kutoka 0 hadi 65,535) kilichotolewa kwa programu ya mtandao kwenye kompyuta. Inatumika kutofautisha huduma nyingi zinazoendeshwa kwa wakati mmoja kwenye IP sawa Address. Mteja anapotuma data, hubainisha nambari ya mlango ili mfumo wa uendeshaji wa seva ujue ni programu gani inapaswa kuipokea (k.m. 80 kwa HTTP, 443 kwa HTTPS, 25 kwa SMTP). Bandari hufanya kama milango maalum, inayoelekeza trafiki ndani na nje, kuzuia mkanganyiko kati ya huduma, na kuruhusu udhibiti mzuri wa ufikiaji kupitia ngome au sheria za uchujaji.


Usawazishaji wa mfuatano wa Exchange unatokana na utaratibu maarufu wa **"*three-way handshake*"**, sawa na jinsi watu wawili wanavyosalimiana ili kuanzisha mawasiliano. Awamu hii ya uanzishaji, ambayo inahakikisha kuegemea kwa TCP, hufanyika katika hatua 3:

1. **SYN:** Mteja hutuma sehemu ya awali ya ulandanishi (**SYN**) ikiwa na seti inayofaa ya flag na nambari ya mfuatano wa mwanzo (k.m., C);

2. **SYN-ACK:** Seva inayopokea hujibu kwa sehemu ya kukiri (**SYN-ACK**), inakubali nambari ya mfuatano ya mteja na kutoa nambari yake ya awali ya mfuatano;

3. **ACK:** Mteja anatuma kibali cha mwisho (**ACK**) kuthibitisha upokeaji wa nambari ya mfuatano wa seva, na kukamilisha usawazishaji. flag ya SYN sasa imezimwa na alama ya ACK inasalia imewekwa kuonyesha kwamba muunganisho umeanzishwa.



![Image](assets/fr/020.webp)



Protocol hii ya Exchange inahakikisha kuwa pande zote mbili zinashiriki msingi sawa wa nambari kabla ya kutuma data ya upakiaji. Mara tu ulandanishi huu unapokamilika, kipindi hufunguliwa: sehemu sasa zinaweza kusafiri katika pande zote mbili, kila moja ikikubaliwa baada ya kupokelewa, na kuhakikisha kiwango cha juu cha kutegemewa kwa mtiririko wa data.


***three-way handshake*** kunahusu tu uanzishaji wa muunganisho. Kwa kufunga, TCP hutumia *four-way handshake*: FIN → ACK → FIN → ACK, ambayo inahakikisha kwamba hakuna sehemu ya upitishaji inayopotea kabla muunganisho haujatolewa kabisa.


Ingawa imeundwa kwa ajili ya uimara na kutegemewa, mchakato huu pia umetoa uwezekano wa udhaifu unaoweza kunyonywa. Kwa mfano, mashambulizi kama vile **IP Spoofing** yanalenga kukwepa au kuharibu uhusiano huu wa uaminifu kwa kujifanya kama mashine iliyoidhinishwa kupitia nambari za mfuatano za uwongo, na hivyo kusababisha ukiukaji unaoruhusu uingiliaji au upotoshaji wa mtiririko wa data.


Ili kupunguza hatari za utekaji nyara wa ulandanishi na kudhibiti upakiaji wa mtandao, protocol ya TCP hutumia mbinu ya kudhibiti mtiririko inayojulikana kama **Sliding Window**. Mfumo huu unadhibiti ni kiasi gani cha data kinaweza kutumwa bila kuhitaji uthibitisho wa mara moja kwa kila sehemu, hivyo basi kupunguza upakiaji usio wa lazima kwenye mtandao huku ukiendelea kutegemewa.


Kwa maneno ya kiutendaji, dirisha la kutelezesha linafafanua anuwai ya nambari za mfuatano ambazo zinaweza kuzunguka kwa uhuru kati ya mtumaji na mpokeaji bila kila sehemu ya mtu binafsi kutambuliwa. Shukrani zinavyopokelewa na mfumo wa kutuma, dirisha "huteremsha": huteleza kwenda kulia kutengeneza nafasi kwa sehemu mpya kutumwa. Ukubwa wa dirisha hili (muhimu kwa ajili ya kuboresha matokeo huku ukiepuka msongamano) umebainishwa katika sehemu ya "*Window*" ya kichwa cha TCP.


**Mfano**: ikiwa nambari ya mfuatano wa mwanzo ni 3 na dirisha linaendelea hadi 5, sehemu zilizo na nambari 3 hadi 5 zinaweza kutumwa bila kusubiri uthibitisho wa mtu binafsi.



![Image](assets/fr/021.webp)



Ukubwa wa dirisha la sliding haijawekwa; inabadilika kwa nguvu kwa hali ya mtandao na uwezo wa usindikaji wa mpokeaji.  Ikiwa mpokeaji anaweza kushughulikia kiasi kikubwa cha data, inaonyesha hii kupitia uwanja wa Dirisha, na kumfanya mtumaji kupanua dirisha lake. Kinyume chake, katika kesi ya upakiaji au hatari ya kueneza, mpokeaji anaweza kuomba kupunguzwa, mtumaji atasubiri hadi dirisha lisonge mbele ili kutuma sehemu za ziada.


Protocol hutoa utaratibu wa ulinganifu wa kufunga muunganisho wa TCP ili kuhakikisha uzimaji safi na wa utaratibu. Mashine yoyote inaweza kuanzisha kufungwa kwa kutuma sehemu iliyo na alama ya **FIN** iliyowekwa kuwa 1, kuashiria dhamira yake ya kusitisha mawasiliano. Kisha husubiri hadi sehemu zote za usafiri wa umma zipokewe na kupuuza data yoyote zaidi.


Baada ya kupokea sehemu hii, mashine nyingine hutuma kibali, ambacho pia kimewekwa alama ya FIN. Kisha humaliza kutuma data yoyote iliyosalia kabla ya kufahamisha programu ya ndani kuwa muunganisho umefungwa. Uthibitishaji huu maradufu huhakikisha kuzima kwa utaratibu na kupunguza hatari ya kupoteza data.


Usimamizi huu sahihi, unaochanganya uelekezaji unaonyumbulika wa IP na udhibiti mkali wa TCP, mara nyingi unaonyeshwa na mchoro unaotofautisha kasi ya protocol ya IP (ambayo inafanya kazi kwa **"juhudi bora zaidi "** msingi, bila hakikisho la uwasilishaji) dhidi ya kutegemewa kwa protocol ya TCP (ambayo inasimamia uwasilishaji kupitia shukrani na mashauriano).



![Image](assets/fr/022.webp)



Katika baadhi ya matukio, hata hivyo, kuegemea kabisa sio kipaumbele: kasi na unyenyekevu ni. Hii ni kweli kwa programu kama vile utiririshaji wa moja kwa moja au VoIP, ambayo inaweza kustahimili upotezaji wa pakiti bila kuathiri sana matumizi ya mtumiaji. Katika hali kama hizi, **UDP** (Itifaki_ya Data ya Mtumiaji_) inapendekezwa.


UDP hufanya kazi kwa kanuni tofauti kabisa na TCP: haina muunganisho, kumaanisha hakuna uhusiano wa awali ulioanzishwa kati ya mtumaji na mpokeaji. Wakati mashine inatuma pakiti kupitia UDP, zinapitishwa kwa njia moja; mpokeaji haitumi shukrani, na mtumaji hana uthibitisho kwamba ujumbe umefika. Kijajuu cha UDP ni chache kimakusudi, kinajumuisha mlango wa chanzo pekee, mlango wa mwisho, urefu wa sehemu na cheki, bila uthibitisho uliojumuishwa ndani au utaratibu wa udhibiti wa serikali. Kama kawaida, anwani za IP hubebwa na kichwa cha msingi cha IP.


Mfano wa kawaida ni kwamba TCP ni kama **simu**, ambapo mzunguko huanzishwa, kufuatwa na kudhibitiwa katika mazungumzo yote. Wakati, itifaki ya UDP ni kama **kuchapisha barua**, ambapo mtumaji huweka barua kwenye kisanduku cha barua bila uthibitisho wa moja kwa moja wa kuwasilishwa au maoni ya utaratibu.


Usaidizi huu kati ya TCP na UDP huwezesha mitandao ya kisasa kukabiliana na mahitaji mbalimbali, kuchagua kutegemewa kwa kiwango cha juu au kasi ya kipaumbele, kulingana na programu.



## Vitu vya awali vya huduma


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Usanifu wa tabaka na shirika la Exchange


Kama tulivyoona, **huduma** ni utekelezaji madhubuti wa protocol ambazo tumeelezea kufikia sasa. Ingawa muundo wa TCP/IP unatofautiana na mtindo wa **OSI**, unachukua mbinu sawa ya tabaka: kila Layer imeundwa kutekeleza kazi mahususi na kutoa **huduma** kwa Layer moja kwa moja juu yake, na kusababisha usanifu wa msimu, thabiti, na unaoweza kudumishwa kwa urahisi.


Kila Layer inajenga juu ya uwezo wa ile iliyo chini yake, na kwa upande wake inatoa Layer hapo juu na Interface thabiti kwa ajili ya kudhibiti data. Katika usanifu huu, kila Layer ina **miundo ya data** yake, iliyofafanuliwa kwa uangalifu ili kuhakikisha utangamano kamili na tabaka zingine. Utangamano huu ni muhimu kwa mawasiliano laini, ya kutegemewa, na ya wazi kutoka ncha moja hadi nyingine.


Vipengele viwili muhimu vinatawala mabadilishano haya:



- **vertical component**: uhusiano kati ya Layer moja na ile iliyo juu au chini yake (kutoka Layer N hadi Layer N+1, na kinyume chake).




![Image](assets/fr/023.webp)




- **horizontal component (Kipengele cha mlalo)**: mwingiliano kati ya programu za mbali, yaani, mazungumzo kati ya **client** na **server**, katika pande zote mbili.



![Image](assets/fr/024.webp)



Usanifu wa tabaka hufuata kanuni kwamba kila Layer inashughulikia habari tu ndani ya upeo wake: miundo ya data, vichwa na taratibu za udhibiti hutofautiana kutoka kwa Layer hadi nyingine, lakini kwa pamoja huunda mfumo madhubuti, kuhakikisha data inaelekezwa hatua kwa hatua hadi mwisho wake.


**Kikumbusho**: Istilahi mahususi hutumika kuelezea vitengo vya data vinavyobadilishwa kati ya safu:

- **ujumbe** kwa Application Layer,
- **sehemu** ya transport layer (TCP),
- **datagram** ya Internet Layer (IP),
- **fremu** ya Network access layer.


Jedwali hapa chini linatoa muhtasari wa masharti ya muktadha wa TCP na UDP:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Vitengo vya awali vya huduma na data


Kiini cha mfumo huu ni **well-known service identifiers**, ambavyo hufanya kama violesura vya mawasiliano. Vipengele hivi vya awali hufanya kazi kama madawati ya huduma, kusikiliza kwenye **port** maalum zilizohifadhiwa na kuruhusu michakato ya kuanzisha, kudumisha, na kuzima miunganisho ya mtandao kwa njia inayodhibitiwa. Ingawa itifaki hupanga umbizo na uwasilishaji wa data kwenye mtandao, ni **huduma na huduma zake za awali** ambazo hutoa kiungo cha wima kati ya safu.


Kwa kuchanganya kipengele cha mlalo (mawasiliano kati ya programu zilizosambazwa) na kipengele cha wima (mwingiliano wa ndani kati ya tabaka), muundo wa TCP/IP unatoa usanifu kamili unaoweza kupanuka. Kuingiliana kwa mitazamo hii miwili kunatoa muhtasari wazi wa jinsi data inavyobadilishwa katika mawasiliano ya mtandao yaliyopangwa.



![Image](assets/fr/026.webp)



### Muhtasari wa sehemu


Katika sehemu hii kuu ya kwanza, tuligundua usanifu msingi ambao unasimamia usanidi na uendeshaji wa mitandao ya leo iliyounganishwa kwenye mtandao. Usanifu huu unatokana na **mfano wa Layer nne**, uliochochewa na muundo wa OSI, na umejengwa karibu na **TCP/IP** protocol ya Suite, uti wa mgongo wa mawasiliano ya kisasa. Tuliona kwamba TCP, pamoja na mbinu yake ya uunganisho, inahakikisha uhamisho wa kuaminika, wakati UDP, nyepesi na ya haraka, inapendekezwa wakati kasi ni muhimu zaidi kuliko kuegemea.


Utendakazi ufaao wa modeli hii unategemea utekelezaji wa protocol kupitia **vitabu vya awali vya huduma**. Hizi huhakikisha kiungo kati ya tabaka, kuwezesha uchakataji wa data kurekebishwa kwa mahitaji mahususi ya kila ngazi, kutoka kwa usafiri hadi programu, ikiwa ni pamoja na mtandao na ufikiaji wa mtandao. Mbinu hii ya msimu hufanya mfumo kuwa rahisi na thabiti.


IP address ni msingi mwingine wa miundombinu hii. Kila kifaa kilichounganishwa kinatambuliwa na **IP Address ya kipekee**, iliyochukuliwa kutoka nafasi ya Address iliyopangwa katika **classes** (kutoka A hadi E). Baadhi ya address hizi zimehifadhiwa kwa madhumuni maalum, kama vile loopback ya ndani au multicast, wakati nyingine, zinazojulikana kama "address za kibinafsi", hazipitishwi kwenye Network Address Translation (NAT). Uainishaji huu huwezesha shirika la kimantiki, la ngazi ya mitandao.


Pia tulichunguza dhana ya **mitandao midogo**, inayowezesha kugawanya sehemu za mtandao ili kudhibiti vyema rasilimali za IP na kuboresha mtiririko wa data. Ingawa ugawanyaji kwa mikono kwa kutumia vinyago vidogo unasalia kuwa kanuni muhimu, kwa kiasi kikubwa umekuwa wa kisasa kutokana na **CIDR** (_Classless Inter-Domain Routing_). Mbinu hii imebadilisha usimamizi wa Address kwa kuwezesha ugawaji unaonyumbulika zaidi na wa kimantiki wa safu za IP, huku ukipunguza ukubwa wa jedwali za kuelekeza.


Kwa kufahamu dhana hizi - tabaka, protocol, huduma za awali, kushughulikia na kuweka chini - unapata msingi thabiti wa kuelewa utendakazi wa kiufundi wa mitandao ya kisasa, na kwa kusanidi kwa ufanisi miundombinu ya mtandao ili kukidhi mahitaji ya leo.


Katika sehemu inayofuata, tutaangalia kwa karibu address ya IPv4.



#  IPv4 address 


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Kwa kutumia IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



Katika sehemu hii, tutaingia ndani zaidi na kuangalia jinsi **IPv4 Address** zinavyotekelezwa katika mtandao wa ulimwengu halisi. Tutachanganua umbizo lao, mantiki nyuma yao, na jinsi wanavyounganishwa na mtandao mwingine muhimu wa Elements kama vile **majina ya DNS**, **address za MAC**, **mitandao midogo** na **mbinu za tafsiri**.


IP Address ni kitambulishi cha kipekee cha nambari kilichotolewa kwa kila **Network Interface** kwenye kifaa. Huwezesha kupata kifaa hiki ndani ya mtandao na kukifikia ili kusambaza data. Kwa mfano, kipanga njia, seva, kituo cha kazi, kichapishi cha mtandao au hata kamera ya uchunguzi ina angalau IP Address yake yenyewe. IP Address hufanya **kuelekeza** kuwezekana, yaani, kuhamisha pakiti kutoka sehemu A hadi sehemu ya B, hata kama ziko mbali kimaumbile.


IP address zinaweza kupewa kwa njia kuu mbili:


- **Imetulia**: Imewekwa kwa mikono kwenye kifaa.
- **Inayobadilika**: Imetolewa kiotomatiki inapohitajika na seva ya DHCP (*Itifaki ya Usanidi ya Mwenyeji Dynamic*). DHCP hurahisisha usimamizi wa mtandao, na kuondoa hitaji la usanidi mwenyewe huku kuwezesha udhibiti sahihi kupitia uwekaji nafasi na muda wa kukodisha.


**Address za IPv4** zimeandikwa katika umbizo la **32-bit** lililogawanywa katika **baiti nne**. Kila baiti ina biti 8 na inawakilisha nambari ya desimali kutoka 0 hadi 255. Baiti 4 hutenganishwa kwa nukta ili kuunda nukuu wazi na inayosomeka.


mfano: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Kila biti katika baiti ina thamani (au "uzito"): sehemu ya mkono wa kushoto (iliyo muhimu zaidi) ina thamani ya 128, 64 inayofuata, kisha 32, 16, 8, 4, 2 na 1 kwa biti ya mkono wa kulia (kidogo muhimu zaidi). Kwa njia hii, uandishi wa binary hubadilishwa kuwa decimal kwa kuongeza rahisi ya uzito uliowekwa.


Jedwali hapa chini linaonyesha mawasiliano haya:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Ili kubadilisha binary kuwa desimali, ongeza uzani wa biti ambazo zimewekwa kuwa 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

IP Address inatambua **Network Interface** mmoja, si kifaa kizima. Gateway za port nyingi au ngome ina miingiliano mingi, kila moja ikiwa na IP Address yake. Interface moja inaweza hata kuwa na IP address kadhaa  (kwa mfano, kutumikia mitandao au huduma nyingi pepe).


Kila pakiti ya IP ina address mbili za IP kwenye kichwa chake:


- source  Address (inakotoka) (** mtumaji**)
- Address inakoenda (**mpokeaji**)

Routers husoma address hizi ili kubaini njia bora ya kutuma pakiti hadi ifike kulengwa. Bila sheria kali za kushughulikia, trafiki ya mtandao haikuweza kupitishwa kwa njia ipasavyo na muunganisho wa kimataifa wa mitandao haungewezekana.


IPv4 Address ina sehemu mbili:


- **NetID**: hutambua mtandao
- **HostID**: hutambua kifaa ndani ya mtandao huo

**Subnet Mask** huamua ambapo NetID inaishia na HostID huanza, ikibainisha ni biti ngapi zinafaa kwa kila sehemu. Kadiri NetID ilivyokuwa ndefu, ndivyo idadi ya subnets inavyokuwa kubwa zaidi, lakini idadi ya seva pangishi kwa kila neti ndogo hupungua ipasavyo.


Hapo awali, mitandao ya IPv4 iligawanywa katika **madarasa** matano: (A, B, C, D na E). Kila darasa linalingana na masafa mahususi ya NetID na linafafanua uzito usiobadilika:


- Darasa A: mitandao mikubwa sana yenye idadi kubwa ya wapangishi
- Darasa B: mitandao ya ukubwa wa kati
- Darasa C: mitandao midogo
- Daraja D: address zimehifadhiwa kwa utumaji anuwai (_multicast_)
- Daraja E: address za majaribio, hazitumiwi kwa anwani za kawaida



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Address Maalum:


- **Network Address**: Hutambua mtandao wenyewe (unaotumika katika majedwali ya kuelekeza).
- **Broadcast address**: Hutuma data kwa vifaa vyote kwenye subnet mara moja (biti zote za HostID zimewekwa 1).


Masafa yafuatayo yamehifadhiwa kwa matumizi ya ndani:


- **10.0.0.0/8** (Daraja la Kibinafsi A)
- **127.0.0.0/8** (mzunguko wa ndani au _loopback_)
- **172.16.0.0 hadi 172.31.255.255** (Daraja B la kibinafsi)
- **192.168.0.0 hadi 192.168.255.255** (Daraja la kibinafsi C)


Address **127.0.0.1** na, kwa ujumla zaidi, safu nzima ya 127.0.0.0/8 inatumika kwa majaribio ya ndani: ombi lolote linalotumwa kwake haliachi kamwe mashine. Hii ni muhimu kwa kuangalia kuwa huduma ya mtandao wa ndani inafanya kazi bila kuhusisha mtandao mpana.


Ili kutumia vyema nafasi ya Address, wasimamizi mara nyingi hugawanya mitandao kuwa **nyati ndogo** kwa kutumia barakoa ndogo au nukuu **CIDR** (_Classless Inter-Domain Routing_). CIDR inaruhusu usimamizi sahihi zaidi na husaidia kuepuka kupoteza anwani. Leo, CIDR ni muhimu kwa kurekebisha vyema safu za IP na kupunguza ukubwa wa jedwali za kuelekeza.


Katika mitandao ya kisasa, IP address kawaida huunganishwa na vitambulishi vingine:



- **Domain name** lililosajiliwa katika **DNS** (_Domain Name System_): Inahusisha IP ya nambari Address na jina linalofaa binadamu.
- **MAC Address**: kitambulisho halisi kilichochongwa kwenye kadi ya mtandao, kinachotumika kwa usafiri wa ndani (_Ethernet_). Wakati pakiti ya IP inahitaji kupitishwa kimwili, jedwali la ARP linalingana na IP Address na MAC Address ya lengwa.


Ili kukabiliana na upungufu wa IPv4 Address na kuongeza Layer ya usalama, mitandao mara nyingi hutumia tafsiri ya Address (_NAT_). NAT inaruhusu vifaa vingi vya kibinafsi kushiriki IP moja ya umma Address wakati wa kufikia Mtandao.


**Kumbuka**: Zana za Mfumo wa Uendeshaji za mtandaoni na zilizojengewa ndani, kama vile [Grenoble CRIC calculator](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), hurahisisha zaidi hesabu za subnet na barakoa.

Huduma hizi husaidia kupanga mgawanyiko wa mtandao kwa ufanisi.


Kwa kumalizia, matangazo ya Address yanasalia kuwa kazi ya vitendo ya kutuma ujumbe sawa kwa vifaa vyote vilivyounganishwa kwenye sehemu: hii inafanikiwa kwa kuweka biti zote katika sehemu ya HostID hadi 1 ili wapangishi wote walenge.



## Aina tofauti za IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



Anwani za IPv4 ziko katika kategoria kuu mbili: anwani za umma, zinazopatikana moja kwa moja kwenye Mtandao, na anwani za kibinafsi, zinazokusudiwa matumizi ya ndani ndani ya mtandao wa ndani.


IPv4 Address ya umma ni ya kipekee duniani kote na inaweza kubadilishwa kwenye Mtandao. Inatolewa na mamlaka rasmi na inahitajika kwa huduma zinazotazama umma kama vile tovuti, seva za barua pepe au miundombinu ya wingu.

Upekee wa ulimwenguni pote wa anwani hizi ni muhimu ili kuepuka migongano au migongano yoyote ya uelekezaji.


**IANA** (_Mamlaka ya Nambari Zilizogawiwa ya Mtandao_), inayofanya kazi chini ya **ICANN** (_Shirika la Mtandao la Majina na Nambari Zilizokabidhiwa_), hudhibiti usambazaji wa safu hizi za IP. Kwa maneno madhubuti, IANA inagawanya nafasi ya IPv4 katika vizuizi 256 vya ukubwa /8, kulingana na nukuu ya CIDR. Kila block inawakilisha zaidi ya anwani milioni 16.7 (2³² / 2⁸).


Vitalu hivi vya unicast Address vimekabidhiwa na IANA kwa **Regional Internet Registries** (RIRs). RIR hizi zina jukumu la kusambaza upya anwani katika ngazi ya kikanda, kulingana na mahitaji halisi ya watoa huduma, makampuni au tawala. Nafasi ya unicast Address inaenea kutoka kwa vizuizi **1/8 hadi 223/8**, huku sehemu zikiwa zimehifadhiwa kwa matumizi maalum (utafiti, uwekaji kumbukumbu, majaribio), au kugawiwa moja kwa moja kwa mtandao au RIR kwa ugawaji upya.


Ili kuangalia ni nani anamiliki IP ya umma ya Address, unaweza kushauriana na hifadhidata za RIR kwa kutumia amri ya **whois**, au kwa kutumia violesura vya wavuti vilivyotolewa na kila sajili. Zana hizi zinaweza kutumika kufuatilia Address hadi kwa shirika au mtoa huduma aliyeitangaza.


Kinyume chake, kuna anwani za kibinafsi za IPv4, jibu la vitendo kwa uhaba wa anwani za umma. Anwani hizi, ambazo haziwezi kubadilishwa kwenye Mtandao, zimehifadhiwa kwa mazingira ya ndani: mitandao ya ushirika, LAN za nyumbani, vituo vya data au makundi ya kompyuta. Si za kipekee duniani kote: mitandao mingi ya kibinafsi inaweza kutumia tena visanduku sawa vya IP bila kuingiliwa, mradi tu ibaki pekee au itumie kifaa cha kutafsiri cha mtandao cha Address kufikia intaneti.


Ili kuruhusu kifaa kilicho na IP ya faragha ya Address kufikia Mtandao, mitandao hutumia NAT (Tafsiri ya Mtandao wa Address). NAT hufanya kazi kwa kubadilisha kikamilifu Address ya kibinafsi na ya umma, kuwezesha kadhaa (au hata mamia) ya vifaa kushiriki IP moja ya umma ya Address. Njia hii huboresha matumizi ya nafasi ya IPv4 na pia huongeza Layer ya usalama kwa kuficha muundo wa mtandao wa ndani.


Aina nyingine maalum ni **anwani ambazo hazijabainishwa**. Nukuu ya IPv4 **0.0.0.0** au toleo lake la IPv6 **::/128** inamaanisha "hakuna Address mahususi". Address kama hiyo ni batili kama lengwa la mtandao wa Address, lakini inaweza kutumika ndani ya nchi na mwenyeji kuashiria "miingiliano yote" au "bado hakuna Address iliyokabidhiwa". Hii ni kawaida katika Assignment inayobadilika ya DHCP au kwa kusikiliza kwenye violesura vyote vya seva.


IPv6 pia inaauni ushughulikiaji wa faragha, lakini kiwango kwa ujumla kinapendekeza ushughulikiaji wa umma ili kuepuka kuweka safu nyingi za NAT. **Anwani za tovuti-eneo** (_tovuti-ya karibu_) za kitalu cha **fec0::/10** ziliacha kutumika na **RFC 3879** kwa sababu za uthabiti na za usalama. Nafasi zao zilibadilishwa na **Anwani za Kipekee za Mitaa** (_ULA_) zilizo katika eneo la **fc00::/7**. ULA huruhusu uundaji wa mitandao ya faragha ya IPv6 yenye uelekezaji safi wa ndani, kwa kutumia kitambulishi kilichozalishwa bila mpangilio cha biti 40 ili kuhakikisha upekee wa ndani.


Kuchoka kwa IPv4 kulithibitishwa rasmi mwaka wa 2011. Ili kuongeza muda wake wa kuishi, jumuiya ya Mtandao ilipitisha mikakati kadhaa:


- Uhamiaji wa taratibu hadi **IPv6**
- Matumizi makubwa ya **NAT**
- Sera kali za ugawaji kutoka kwa RIRs, zinazohitaji uhalalishaji sahihi na usimamizi wa mahitaji ya Address
- Urejeshaji wa vitalu vya Address ambavyo havijatumiwa au vilivyorejeshwa kwa hiari na makampuni


Hatua hizi zinaonyesha kwamba kushughulikia IP si tu changamoto ya kiufundi, lakini pia ni suala la utawala wa kimataifa, kiini cha upanuzi unaoendelea wa Mtandao.



## DNS, saraka ya Address


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Wacha tuwe waaminifu, wanadamu si wastadi wa kukariri mifuatano mirefu ya nambari, iwe katika mfumo wa binary au desimali. Changamoto hii inakuwa kubwa zaidi na anwani za IP, ambazo zinaweza kuwa ngumu na IP moja Address wakati mwingine inaweza kuficha anwani nyingi, haswa wakati mbinu kama NAT au upangishaji pepe unahusika.


Ili kurahisisha mambo, Programu ya Layer hutumia mfumo unaounganisha IP Address kwa jina la kimantiki, linaloweza kusomeka na binadamu. Hili ni jukumu la **DNS** (*Mfumo wa Jina la Kikoa*), saraka kubwa, ya daraja na inayosambazwa inayolingana na majina ya vikoa vinavyoweza kusomeka na anwani za IP. Mfumo unategemea seti ya itifaki na huduma. Programu inayotumika sana ya seva ya DNS ni **BIND** (_Berkeley Internet Name Domain_), kifurushi cha programu huria ambacho kinarejelea miundombinu mingi ya DNS ya Mtandao.


Wazo la msingi la DNS ni rahisi: kwa huduma yoyote iliyounganishwa, iwe tovuti, seva ya barua, au huduma nyingine ya mtandao, kuna rekodi inayoonyesha jina la kikoa kwa anwani moja ya IP au zaidi. Hii inafanya kazi katika pande mbili:


- Azimio la mbele: kutafsiri jina katika IP Address.
- Azimio la kubadilisha: kutafuta jina la kikoa linalohusishwa na IP Address iliyotolewa.

Hii hufanya ushughulikiaji wa mtandao utumike kwa wanadamu huku kuhifadhi vipanga njia sahihi kunahitaji kusogeza data kwa usahihi.


Jina la kikoa kila mara hupangwa kwa mpangilio, na kila ngazi ikitenganishwa na nukta: jina kamili linaitwa **FQDN** (_Fully Qualified Domain Name_). Sehemu ya kulia kabisa ni **TLD** (_Kikoa cha Kiwango cha Juu_) kama vile `.com`, `.org` au `.fr`. Sehemu ya kushoto-zaidi huteua seva pangishi, yaani, mashine au huduma mahususi iliyounganishwa na IP Address.


Mfumo wa DNS umeundwa kama **mti wa maeneo**. **eneo** ni sehemu ya nafasi ya majina ya kikoa inayodhibitiwa na seva mahususi ya DNS. Eneo moja linaweza kuwa na **vikoa vidogo** vingi, ambavyo vinaweza kukabidhiwa kwa maeneo mengine yanayodhibitiwa na seva tofauti. Wasimamizi wana jukumu la kudumisha kanda zao: kushughulikia masasisho, uwakilishi, na usimamizi wa jumla.


Muundo huu hauruhusu tu kuelekeza kwenye kikoa kikuu (k.m. `example.com`), lakini pia rekodi za kupanga vyema kwa wapangishi binafsi (`www`, `mail`, `ftp`, n.k.). Katika siku za awali za mtandao, upangaji ramani huu ulishughulikiwa na faili tuli kama (`/etc/hosts` kwenye mifumo ya Unix), lakini mbinu kama hiyo ilianza kutowezekana kwa Mtandao unaokua kwa kasi na uliounganishwa.


Ni muhimu kuelewa kwamba **server ya DNS** inaweza tu kutoa upeo mdogo. Kwa mfano, seva ya ndani ya kampuni ya DNS inaweza isipatikane moja kwa moja kutoka kwa Mtandao. Ikiwa DNS hii haijasanidiwa kusambaza hoja, au haina uhusiano unaoaminika na seva zingine, baadhi ya hoja zitashindwa: jina wala IP Address haiwezi kutatuliwa nje ya eneo lililobainishwa.


DNS pia ina jukumu katika uelekezaji wa barua pepe. Kwa mfano, rekodi ya **MX** (_Mail Exchange_) hubainisha seva za barua zinazowajibika kupokea barua pepe za kikoa fulani. Rekodi hizi hufafanua vipaumbele (sababu ya uzani) na suluhisho la kushindwa. Faili ya eneo la seva ya DNS lazima iwe na rekodi ya **SOA** (_Start of Authority_), ambayo huteua seva kama chanzo rasmi cha maelezo ya eneo hilo.


Shukrani kwa muundo wake wa hali ya juu, uliosambazwa, DNS inasalia kuwa msingi wa Mtandao, kuruhusu watumiaji kupata huduma kupitia majina ya wazi, ya kukumbukwa ya vikoa badala ya anwani ndefu za kiufundi za IP.


Katika sura inayofuata, tutachunguza dhana nyingine ya msingi: **Address za Ethernet**, pia hujulikana kama ** MAC address**, ambazo huhakikisha uwasilishaji wa data katika Layer halisi ya mitandao ya ndani.



## Kugundua address za Ethaneti na ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Ufafanuzi


Ili protocol ya uelekezaji wa data ifanye kazi kwa uhakika na kwa uthabiti, sehemu moja muhimu ni muhimu. Kama wanadamu, tunaweza kutambua mashine kwa urahisi kwa IP Address yake au kwa jina lake kupatikana kupitia DNS. Mashine, hata hivyo, lazima iweze kutambua bila utata kifaa lengwa ili kutoa pakiti. Ili kufanya hivyo, inategemea kitambulisho maalum cha maunzi, kinachotumiwa moja kwa moja na mtandao wake wa Interface: MAC Address (_Media Access Control_).


**Kumbuka**: Hii haina uhusiano wowote na "Physical Address" katika usanifu wa kumbukumbu. Katika kompyuta, kumbukumbu ya kimwili Address inahusu eneo maalum kwenye basi ya kumbukumbu, kinyume na Address ya kawaida inayosimamiwa na mfumo wa uendeshaji. MAC Address, kwa kulinganisha, inahusiana madhubuti na maunzi ya mtandao.


MAC Address imetolewa kwa kudumu na kwa kipekee na mtengenezaji vifaa vinavyotengenezwa. MAC Address inatambua kadi ya mtandao bila shaka iwe ni kompyuta, simu mahiri, kichapishi au kifaa kingine chochote kilichounganishwa. Tofauti na IP Address, ambayo inaweza kubadilika kwa nguvu (kupitia seva ya DHCP au usanidi wa mtu), MAC Address kwa kawaida husalia sawa katika maisha ya kifaa, isipokuwa ikiwa imebadilishwa kimakusudi.


Kila mtandao wa Interface, wenye waya au pasiwaya, una MAC Address yake. Address hii inatumika ndani ya kiungo cha data Layer (Layer 2 ya muundo wa OSI) ili kuingiza na kudhibiti maunzi ya Address katika kila fremu ya mtandao inayobadilishwa. Hii wakati mwingine hujulikana kama _Ethernet address au _UAA_ (_Universally Administered Address_). Imesawazishwa kwa urefu wa biti 48, au baiti 6, imeandikwa kwa nukuu hexadecimal, kwa ujumla katika umbo la baiti zinazotenganishwa na `:` au `-`.


Kwa mfano: `5A:BC:17:A2:AF:15`


Katika muundo huu, baiti tatu za kwanza humtambulisha mtengenezaji wa kadi ya mtandao: hii inajulikana kama **OUI** (*Organizationally Unique Identifier*). Viambishi awali hivi, vilivyotolewa na IEEE, vinatumika pia katika mifumo mingine ya kushughulikia maunzi, kama vile Bluetooth na LLDP, ili kuhakikisha upekee duniani kote.


### Kubadilisha MAC Address (MAC Spoofing)


Kinadharia, MAC Address imeundwa ili ibaki thabiti, lakini kuna njia za kuirekebisha, haswa ili kukidhi mahitaji fulani au kukwepa vikwazo fulani. Operesheni hii, ambayo mara nyingi hujulikana kama _spoofing MAC_, inahusisha kubadilisha maunzi asilia ya Address na thamani tofauti, iliyofafanuliwa katika kiwango cha programu. Baadhi ya mifumo ya uendeshaji huwezesha urekebishaji huu, hasa wakati Ethernet Address halisi haitumiwi moja kwa moja na kiendeshi.


Sababu za mabadiliko kama haya ni tofauti. Inaweza kuwa hitaji la programu fulani kuhitaji Ethernet Address mahususi ili kufanya kazi ipasavyo, au kutatua mgongano wa anwani zinazofanana kati ya vifaa viwili vinavyoshiriki mtandao mmoja wa ndani.


Kubadilisha MAC Address kunaweza pia kuchochewa na masuala ya faragha: kwa kuficha kitambulisho cha kipekee kilichochongwa kwenye kadi, watumiaji hupunguza uwezekano wa kifaa chao kufuatiliwa na mitandao au huduma za uchunguzi. Walakini, mazoezi haya sio bila matokeo. Kubadilisha MAC Address kunaweza kutatiza vifaa fulani vya kuchuja, au kuhitaji ngome kusanidiwa upya ili kuidhinisha maunzi mapya.


Baadhi ya mitandao, hasa Wi-Fi, hutumia kichujio cha MAC Address ili kuruhusu vifaa vilivyo na Address zilizoidhinishwa pekee. Ingawa hii inaongeza kiwango cha msingi cha udhibiti, sio salama peke yake. Mshambulizi anaweza kunasa MAC Address halali ambayo tayari imeidhinishwa kwenye mtandao na kuifanya ili kukwepa vikwazo. Kwa sababu hii, uchujaji wa MAC unapaswa kuunganishwa kila wakati na hatua kali za usalama.


### Mawasiliano ya MAC/IP


Ili mtandao wa ndani ufanye kazi kwa ufanisi, lazima kuwe na upangaji ramani wazi kati ya address halisi ( MAC address) na address za kimantiki (address za IP). Bila kiungo hiki, kompyuta inaweza kujua IP Address ya lengwa lakini haijui jinsi ya kutuma data kwake kwenye mtandao wa ndani.

Upangaji huu wa ramani unashughulikiwa kiotomatiki na ARP (_Address Resolution Protocol_).


Katika mazoezi, mtumiaji anapotaka kujua MAC Address inayolingana na IP mahususi Address, mtumiaji anaweza kutumia matumizi ya `arp`. Zana hii hukagua jedwali la ndani la mashine la ARP ili kuonyesha ulinganifu unaojulikana kati ya IP address na MAC address kwenye mtandao wa ndani. Kwa njia hii, inawezekana kuthibitisha haraka kiungo cha ufanisi kati ya tabaka za kimantiki na za kimwili.


Mfano wa vitendo: ikiwa unataka kuangalia ni kadi gani ya mtandao inayolingana na IP Address `192.168.1.5`, tumia amri ifuatayo:


```bash
arp –a 192.168.1.5
```


Matokeo yataonyesha Address (MAC) inayohusika, asili ya ingizo (tuli au inayobadilika) na Interface inayohusika.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Ni muhimu kukumbuka kuwa MAC Address na IP Address ni vitambulishi viwili tofauti kabisa, lakini vinakamilishana kwa karibu. MAC Address imechorwa kwa njia ya kipekee katika kila mtandao Interface na mtengenezaji na hutumiwa kutambua kifaa kwenye mtandao wa ndani. IP Address, kwa upande mwingine, ni Address ya kimantiki iliyokabidhiwa kwa nguvu au kwa kitakwimu, ikiruhusu mashine kujiunga na mtandao wa IP na pakiti za Exchange zaidi ya mtandao wake wa ndani.



- Mfano unaoonekana wa MAC Address:


![Image](assets/fr/032.webp)




- Mfano unaoonekana wa IP Address:


![Image](assets/fr/027.webp)



Katika mazingira ya ushirika, viwango hivi viwili vya kushughulikia haviwezi kufanya kazi tofauti. Kwa mfano, seva ya DHCP inapokabidhi IP Address kiotomatiki, MAC Address ya kifaa hutumika kama mahali pa kuanzia. Kompyuta hutuma ombi la utangazaji la DHCP iliyo na MAC Address yake ili seva iweze kuagiza IP inayopatikana Address kwa kifaa sahihi. Bila kitambulisho hiki cha maunzi, seva ya DHCP haingejua ni kifaa gani cha kuwasilisha Address kwa.


Kwa hivyo protocol ya ARP ni ya msingi: hutoa kiungo kati ya anwani za IP address halisi, kuwezesha mashine kutafsiri lengwa la kimantiki hadi mahali halisi halisi. Kompyuta inapohitaji kutuma pakiti kwa mashine iliyo kwenye mtandao huo huo, kwanza inatazama jedwali lake la ARP ili kuangalia kama MAC Address ya mpokeaji tayari inajulikana. Ikiwa sivyo, inatangaza ombi la ARP kwa wapangishi wote kwenye mtandao wa ndani. Mashine inayotambua IP inayolengwa Address katika ombi hili inajibu kwa kubainisha MAC Address yake. Kisha mtumaji anaandika jozi hii ya IP/MAC kwenye kashe yake ya ARP, ili kuepuka kurudia operesheni kila wakati ombi linapotumwa.


Jedwali hili la ARP hufanya kazi kama saraka ya ramani ndogo, iliyosasishwa kwa nguvu kwa njia sawa na vile DNS inahusisha majina ya vikoa na anwani za IP. Bila ARP, hakuna Exchange ya ndani ambayo ingewezekana, kwani kiungo cha data Layer kinahitaji kujua MAC Address ili kuambatanisha fremu za Ethaneti kwa usahihi.


Kinyume chake, itifaki ya RARP (_Reverse Address Resolution Protocol_) iliundwa kwa hali tofauti: kuwezesha mashine inayojua MAC Address yake pekee kugundua IP yake Address. Hii ilikuwa kesi ya kawaida kwa vituo vya zamani vya kazi bila diski ya ndani ya Hard, ambayo ilibidi ifungue mtandao na kuomba IP Address. RARP hatimaye ilibadilishwa na **BOOTP** na kisha **DHCP**, ambayo ni rahisi kunyumbulika zaidi na otomatiki.


Itifaki hizi za ushirika zina jukumu muhimu katika uelekezaji. Kipanga njia kimsingi ni mashine yenye miingiliano mingi ya mtandao, inayounganisha sehemu tofauti. Wakati kipanga njia kinapokea fremu, huichakata ili kutoa datagramu ya IP na huchunguza kichwa cha IP ili kubaini lengwa. Ikiwa lengwa liko kwenye mtandao uliounganishwa moja kwa moja, datagramu inawasilishwa moja kwa moja baada ya kusasisha kichwa. Ikiwa lengwa ni la mtandao mwingine, kipanga njia hutafuta jedwali lake la uelekezaji ili kutambua njia bora, au _next hop_, kuelekea unakoenda.


Hii hugawanya njia katika sehemu fupi, zinazoweza kudhibitiwa zaidi. Kila kipanga njia cha kati kinajua tu hatua inayofuata, si lazima mahali pa mwisho.


**Kikumbusho:** Uwasilishaji wa moja kwa moja hufanyika wakati mtumaji na mpokeaji wako kwenye mtandao mmoja wa kawaida. Vinginevyo, uwasilishaji sio wa moja kwa moja na hupitia ruta moja au zaidi.


Jedwali la uelekezaji, linalodhibitiwa na mtu (uelekezaji tuli) au kwa nguvu (uelekezaji unaobadilika), lina maelezo yanayohitajika ili kuamua njia ya kuchukua. Katika mitandao ndogo, usanidi wa tuli ni wa kutosha. Katika miundomsingi mikubwa, uelekezaji unaobadilika ni muhimu ili kurekebisha njia kiotomatiki wakati topolojia inapobadilika au kiungo kinaposhuka.


Jedwali la uelekezaji hufanya kama jedwali la ramani kati ya anwani za IP lengwa na lango zinazofuata. Kwa kawaida huhifadhi vitambulishi vya mtandao (_network ID_) badala ya kila seva pangishi Address, ambayo hupunguza ukubwa wake kwa kiasi kikubwa.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Kutumia maingizo haya, router inaweza kuamua haraka kupitia Interface na kwa nodi gani kila datagram inapaswa kutumwa. Ikiunganishwa na ARP kwa ajili ya kusuluhisha anwani za MAC zinazolingana, hii inahakikisha uhamishaji bora na wa kuaminika wa data kwenye mtandao.


Hatimaye, itifaki zinazobadilika za uelekezaji zinajumuisha viwango kama vile RIP (_Itifaki ya Taarifa ya Uelekezaji_), kulingana na algoriti ya umbali, na OSPF (_Open Shortest Path First_), ambayo hukokotoa njia fupi zaidi katika topolojia changamano. Itifaki hizi husasishwa kila mara kwa Exchange ili kuboresha njia, kupunguza gharama za uwasilishaji, na kuboresha ustahimilivu dhidi ya kukatika au msongamano.



## NAT: Tafsiri ya Address


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Ufafanuzi


Network Address Translation_ (NAT) ni mbinu iliyobuniwa hadi Address ya kupungua polepole kwa adsress zinazopatikana za IPv4. Iliyoundwa kama suluhisho la muda kabla ya kupitishwa kwa IPv6 kwa wingi, NAT iliwezesha makampuni na watu binafsi kuendelea kuunganisha idadi kubwa ya mashine huku wakitumia tu seti ndogo ya  IP address za umma.


**Kikumbusho muhimu:** hoja kutoka IPv4 hadi IPv6 kinadharia hutatua tatizo la uchovu kwa kupanua nafasi ya Address kutoka biti 32 hadi biti 128, kutoa karibu idadi isiyo na kikomo ya anwani (2^128). Katika mazoezi, hata hivyo, mpito bado haujakamilika, na NAT inabakia kutumika sana leo.


Kanuni ya NAT ni rahisi lakini yenye ufanisi mkubwa: badala ya kugawa IP ya kipekee ya umma Address kwa kila kifaa kwenye mtandao wa ndani, Address moja inayoweza kuendeshwa (au kundi ndogo la anwani) hutumiwa kwa vifaa vyote vya kibinafsi. Lango la NAT, ambalo mara nyingi huunganishwa kwenye kipanga njia au ngome, kisha hutafsiri kwa uthabiti IP ya ndani ya Address pamoja na maelezo yanayohitajika ili kuelekeza trafiki kwa njia ipasavyo kwa ulimwengu wa nje, na huhakikisha kuwa majibu yanarejeshwa kwa mtumaji asili.


Njia hii ina faida ya haraka: inaficha kabisa usanifu wa mtandao wa ndani. Kwa mtazamaji wa nje, maombi yote kutoka kwa vituo vya kazi, seva au vichapishaji yanaonekana kutoka kwa utambulisho sawa wa umma. Anwani za faragha, kwa kawaida huchukuliwa kutoka kwa safu zilizohifadhiwa (k.m. 192.168.x.x au 10.x.x.x), husalia zisizoonekana kwenye Mtandao.


Mbali na kushughulikia uhaba wa IPv4, NAT pia huimarisha usalama kwa kuunda kizuizi cha kwanza cha kimantiki kati ya mitandao ya ndani na ya umma. Mawasiliano ya ndani ambayo hayajaombwa huzuiwa kwa kawaida, kwa kuwa ni miunganisho inayoanzishwa kutoka ndani ya mtandao pekee ndiyo hufaidi tafsiri inayohitajika ili kupokea majibu.



![Image](assets/fr/035.webp)



### Aina za tafsiri


NAT inaweza kutekelezwa kwa njia tofauti ili kukidhi mahitaji maalum. Njia kuu mbili za uendeshaji ni tafsiri tuli na tafsiri yenye nguvu.


**Tafsiri tuli** huunda ramani isiyobadilika kati ya IP ya faragha Address na IP ya umma Address. Kila mashine ya ndani imeunganishwa kabisa na Address yake ya umma iliyojitolea. Kwa mfano, kifaa cha ndani kilichosanidiwa kuwa 192.168.20.1 kinaweza kuhusishwa na Address 157.54.130.1. Wakati pakiti inayotoka inaondoka kwenye mtandao wa ndani, kipanga njia hubadilisha chanzo cha pakiti Address na Address ya umma, na hufanya operesheni ya nyuma kwa trafiki inayoingia. Tafsiri hii ya pande mbili ni wazi kwa mtumiaji.


**Onyo:** Ingawa njia hii inatenga mtandao wa ndani, haisuluhishi uhaba wa IP address za umma, kwa kuwa bado unahitaji address nyingi za umma kama vile kuna mashine za kufichua. Kwa hivyo tafsiri tuli hutumika hasa wakati rasilimali fulani za ndani lazima zisalie kufikiwa kutoka nje (seva ya wavuti, seva ya barua...).


**Tafsiri yenye nguvu**, kwa upande mwingine, hutumia anwani nyingi za IP za umma. Mpangishi wa ndani anapoanzisha muunganisho, kipanga njia hukabidhi moja ya anwani hizi za umma kwa Address ya kibinafsi ya mwenyeji kwa muda wa kipindi. Kiungo ni 1-to-1, lakini cha muda: mara tu muunganisho unapoisha, Address ya umma inapatikana kwa kifaa kingine. Kwa hivyo NAT inayobadilika hupunguza idadi ya address za umma zinazohitajika wakati si mashine zote ziko mtandaoni kwa wakati mmoja, lakini bado inahitaji block ya address ya nje angalau kubwa kama idadi ya juu zaidi ya miunganisho ya wakati mmoja.


**Port Address Translation** (PAT), pia inajulikana kama *NAT overload* au *IP kujifanya*, inaenda hatua zaidi: vifaa vyote vya kibinafsi vinashiriki IP moja ya umma ya Address (au nambari ndogo sana). Ili kutofautisha vipindi, lango hurekebisha sio tu chanzo cha Address, lakini pia mlango wa chanzo. Huweka jedwali linalounganisha kila jozi ya *(faragha Address, bandari ya kibinafsi)* kwa jozi ya kipekee ya *(umma Address, bandari ya umma)*. Aina hii ya NAT hutumiwa katika takriban vipanga njia vyote vya nyumbani, ikiruhusu vifaa vingi (kompyuta, simu mahiri, vitu vilivyounganishwa, n.k.) kushiriki IP sawa ya umma ya Address, huku hudumisha mawasiliano ya kiowevu.


Kwa hivyo NAT huongeza muda wa maisha wa IPv4, huku ikiongeza Layer muhimu ya mgawanyo na usalama. Hata hivyo, jinsi upitishaji wa IPv6 unavyokua na nafasi yake kubwa ya Address inatumika sana, jukumu la NAT litapungua, ingawa kwa madhumuni ya upatanifu na udhibiti, bado litatumika katika baadhi ya mazingira kutenganisha na kuchuja trafiki.


### Utekelezaji wa NAT


Ili kuhakikisha utendakazi ufaao wa tafsiri ya Address, kipanga njia au lango la NAT lazima kiweke rekodi sahihi ya michoro iliyoanzishwa kati ya kila Address ya kibinafsi kwenye mtandao wa ndani na Address ya umma inayotumia kuwasiliana na ulimwengu wa nje. Maelezo haya yanahifadhiwa katika kile kinachojulikana kama "Jedwali la tafsiri la NAT", ambalo lina jukumu kuu katika kudhibiti trafiki ya mtandao.


Kila ingizo katika jedwali hili linaunganisha angalau jozi moja: IP ya ndani Address ya mashine ya kutuma na IP ya nje Address ambayo itafichuliwa kwenye Mtandao. Pakiti kutoka kwa mtandao wa kibinafsi inapotumwa hadi mahali pa umma, kipanga njia cha NAT hukatiza fremu, kuchanganua vichwa vya IP na TCP/UDP, kisha kuchukua nafasi ya chanzo cha kibinafsi cha Address na Address ya umma ya lango. Kwenye njia ya kurudi, lango lile lile linanasa pakiti inayoingia, hukagua jedwali la ramani na kufanya utendakazi wa kinyume ili kuelekeza mtiririko kwa IP ya awali ya ndani ya Address.


Kanuni hii tendaji ya utafsiri inategemea usimamizi sahihi wa jedwali: kila ingizo linasalia kuwa halali mradi tu kuna trafiki amilifu ya kulihalalisha. Baada ya muda unaoweza kusanidiwa wa kutotumika, ingizo litafutwa na linaweza kutumika tena kwa miunganisho mipya.


_Mfano wa jedwali la tafsiri lililorahisishwa la NAT:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Katika mfano huu, ikiwa hakuna pakiti imepitia kwa ingizo la pili kwa zaidi ya saa moja (sekunde 3,600), imetiwa alama kuwa inaweza kutumika tena. Kinyume chake, muda wa sifuri unaonyesha mawasiliano amilifu, ramani ikiwa imefungwa.


Ingawa NAT hufanya kazi kwa uwazi kwa matumizi mengi ya kawaida (kuvinjari kwa wavuti, barua pepe, kuhamisha faili, n.k.), inaweza kuleta changamoto za ziada kwa programu fulani za mtandao. Baadhi ya teknolojia hutegemea ubadilishanaji wa anwani za IP au bandari ndani ya pakiti ya malipo. Baada ya kupita lango la NAT, habari hii inakuwa haiendani.


Mifano ya kawaidac ya vikwazo ni pamoja na:


- Protocol ya peer yo peer (P2P), ambayo inahitaji miunganisho ya moja kwa moja kati ya vifaa, zimezuiwa na block cha NAT, kwa kuwa mashine zote za ndani zinashiriki IP sawa ya nje ya Address na haiwezi kufikiwa moja kwa moja bila usanidi maalum (kama vile *usambazaji wa bandari* au UPnP);
- protocol ya IPSec, inayotumiwa kulinda mawasiliano ya mtandao, husimba vichwa vya pakiti kwa njia fiche. Kwa sababu lazima NAT irekebishe vichwa hivi ili kuchukua nafasi ya anwani za IP, usimbaji fiche hufanya hili lisiwezekane bila mbinu za urekebishaji kama vile NAT-T (*NAT Traversal*);
- protocol  ya windows X, ambayo inaruhusu uonyeshaji wa mbali wa programu za picha kwenye Unix/Linux, hufanya kazi kwa njia ambayo seva ya X hutuma miunganisho ya TCP kwa wateja kikamilifu. Ugeuzi huu wa mwelekeo wa kawaida wa miunganisho unaweza kuzuiwa na NAT.


Kwa ujumla, protocol yoyote ambayo inajumuisha kwa uwazi IP address ya ndani ya katika upakiaji wa pakiti itaathiriwa, kwa kuwa Address hiyo haitalingana tena na Address halisi, inayoonekana kwenye mtandao baada ya tafsiri.


**Dokezo muhimu:** Kwa Address masuala haya, baadhi ya vipanga njia vya NAT hutoa _Deep Packet Inspection_ (DPI) au _Protocol Helpers_ , ambayo hukagua yaliyomo kwenye pakiti ili kutambua na kubadilisha kwa njia kubadilisha anwani au nambari za mlango ndani ya data ya programu. Hii inahitaji ujuzi wa kina wa umbizo la itifaki, na inaweza kuunda udhaifu wa usalama au kuongeza matumizi ya rasilimali.


**Tahadhari:** Ingawa NAT husaidia kuficha mtandao wa ndani na kudhibiti trafiki inayoingia, si badala ya ngome maalum ya kufyeka. Tafsiri pekee si kizuizi kamili cha usalama: lazima kila wakati ijazwe na sheria wazi za uchujaji ili kuzuia trafiki isiyoombwa au isiyotakikana.


_Kuonyesha jinsi hii inavyofanya kazi, zingatia mfano ufuatao:_



![Image](assets/fr/037.webp)



Katika hali hii, kituo cha kazi cha ndani kinaweza kufikia seva ya wavuti ya ndani kwa kuita URL `http://192.168.1.20:80`. Kubainisha lango ni hiari hapa, kwa kuwa `80` ndio lango la kawaida la HTTP. Kinyume chake, ikiwa ombi litaanzishwa kutoka nje, mtumiaji ataingiza Address ya umma `http://85.152.44.14:80`. Kipanga njia cha NAT hupokea ombi, hutazama jedwali lake la ramani, na hutafsiri kiotomatiki Address ya umma hadi ya faragha, ikielekeza upya muunganisho kwa `http://192.168.1.20:80`.


Kanuni hiyo hiyo inatumika kwa seva nyingine yoyote iliyoidhinishwa kupokea miunganisho ya intaneti, kama vile seva ya Extranet (saketi ya bluu kwenye mchoro).


**practical note:** katika mazingira yaliyoboreshwa, violesura vya mtandao vinavyoitwa _virbrX_ (kwa _Virtual Bridge X_) hutumiwa kwa kawaida. Madaraja haya pepe, yanayotolewa hasa na maktaba ya libvirt au hypervisor ya Xen, huunganisha mtandao pepe wa ndani wa mashine za wageni kwenye mtandao halisi huku ukitumia NAT. Kwa ujumla husanidiwa kupitia hati katika `/etc/sysconfig/network-scripts/`, kama inavyoonyeshwa hapa chini kwa `virbr0`:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Mara tu daraja la mtandaoni litakapowekwa, unahitaji kuwezesha uelekezaji wa IP na kusanidi tafsiri ya mlango na `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Kwa usanidi huu, trafiki inayotoka hupitishwa na tafsiri ya NAT inatumika, ikiruhusu mashine pepe kuwasiliana na ulimwengu wa nje bila kufichua anwani zao za ndani za IP moja kwa moja.


Katika sura inayofuata, tutaangalia kwa undani usanidi wa IP Address chini ya Linux, inayojumuisha mbinu rahisi na za juu zinazofaa kwa miktadha tofauti ya utawala.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Je, ninawezaje kusanidi mtandao na `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Usanidi wa kawaida


Baada ya kuangazia misingi ya kinadharia ya mtandao na kuelewa jinsi anwani za IP, vinyago, uelekezaji na tafsiri zinavyofanya kazi pamoja, ni wakati wa kuendelea na usanidi wa vitendo. Kwenye GNU/Linux, usanidi wa mtandao sasa unashughulikiwa kwa amri ya **`ip`** (_iproute2_ kifurushi), ambayo inachukua nafasi ya `ifconfig` ya zamani.


`ip` hukuruhusu kukabidhi au kubadilisha IP Address, kubadilisha barakoa, kuanzisha au kusimamisha Interface, au kuangalia hali yake wakati wowote.


**VIDOKEZO:** ili kuonyesha violesura vyote (vinatumika au la): `ip addr show`


Mfano: kukabidhi Address tuli na kuwezesha Interface


Ongeza Address `192.168.1.2/24` hadi Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Washa Interface:


```shell
ip link set dev eth0 up
```


Zima Interface sawa:


```shell
ip link set dev eth0 down
```


Onyesha hali ya Interface mahususi:


```shell
ip addr show dev eth2
```


**Kidokezo cha vitendo:** kwa `ip`, kuongeza Address ya ziada kwenye Interface hakuhitaji tena kiambishi cha `:1`. Ongeza tu mstari mwingine wa `ip addr ...`:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Maandishi ya uanzishaji: ifup / ifdown


Huduma za `ifup` na `ifdown` husoma faili za usanidi tuli kutoka `/etc/sysconfig/network-scripts/` (kwenye RHEL, CentOS, Rocky Linux, AlmaLinux...) au `/etc/network/interfaces` (kwenye Debian/Ubuntu) ili kuleta violesura juu au chini kwa njia safi.


```shell
ifup eth1
ifdown eth2
```


Faili za usanidi (kama RHEL):


- **/etc/sysconfig/network**: mipangilio ya kimataifa (NETWORKING, HOSTNAME, GATEWAY...).
- **ifcfg-**: mipangilio maalum kwa kila Interface.


Mfano tuli (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Mfano wa DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Muundo huu wa moduli bado ni halali na unaweza kujiendesha kwa urahisi kwenye mifumo ya sasa.


### Usanidi wa hali ya juu: kuunganisha


Katika mazingira ya kitaaluma, lengo ni kuhakikisha uendelevu wa huduma na/au kujumlisha kipimo data. Utaratibu wa *Kuunganisha* (au *kushirikiana* na _teamd_) hutimiza mahitaji haya: violesura kadhaa halisi hufanya kazi kama Interface moja ya kimantiki, ambayo mara nyingi huitwa `bond0` au `timu0`.



![Image](assets/fr/039.webp)



Masharti:


- Pakia moduli ya `bonding` (au tumia `teamd`);
- Kuwa na angalau violesura viwili vinavyopatikana.


#### Mbinu mbalimbali za kawaida za kuunganisha:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Inasanidi kwa kiungo cha `ip



- Lemaza miingiliano ya kimwili:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Unda Interface iliyounganishwa:


```shell
ip link add bond0 type bond mode balance-alb
```



- Sanidi chaguo baada ya kuunda


```shell
ip link set bond0 type bond miimon 100
```



- Agiza MAC na anwani za IP:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Ambatanisha violesura vya watumwa:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Rudisha kila kitu:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Kidokezo:** kumtenga mtumwa bila kuondoa dhamana: `kiungo cha ip weka eth1 nomaster`


#### Usanidi wa kudumu (RHEL-kama)


Unda faili tatu katika `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Kisha:


```shell
systemctl restart network
```


#### Secondary IP Address(lakabu la kisasa)


Ukiwa na `ip`, unaweza kuongeza Address ya pili kwa kifaa sawa:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Ili kufanya lakabu hii kuendelea baada ya kuwasha upya, ama ongeza `IPADDR2=...` / `PREFIX2=...` ya pili zuia hadi `ifcfg-eth0`, au uunde muunganisho mpya wa *NetworkManager* kupitia `nmcli`.


Shukrani kwa `ip` na amri zinazohusiana (`kiungo cha ip`, `ip addr`, `njia ya ip`), usanidi wa mtandao ni thabiti zaidi, unaweza kuandikwa na wazi. Kuunganisha ni sehemu muhimu ya usanifu wa upatikanaji wa juu, na kugawa anwani nyingi kwa Interface moja imekuwa rahisi zaidi.


Katika sura inayofuata, tutaangalia maalum na utekelezaji wa address ya IPv6.


# Anwani ya IPv6


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Viwango na ufafanuzi


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Sasa tunahamia kizazi kijacho cha IP address: protocol ya IPv6, ambayo ilijulikana kama IPng (_IP Next Generation_). Imeundwa ili kuondokana na mapungufu ya kimuundo ya IPv4, protocol hii inaleta usanifu uliopanuliwa wa kushughulikia, pamoja na uboreshaji mwingi wa kiufundi.


Motisha za kupitishwa kwa IPv6 ni tofauti, na mahitaji muhimu ya Address kwa mageuzi ya Mtandao. Kwanza, jukumu la IPv6 ni kusaidia ukuaji wa kasi wa idadi ya vifaa vilivyounganishwa (lengo lisiloweza kufikiwa na nafasi ndogo ya IPv4 ya Address). Pili, itifaki inalenga kupunguza ukubwa wa meza za uelekezaji, kufanya ubadilishanaji ufanisi zaidi na kupunguza mzigo wa kazi wa ruta kwa muda mrefu.


IPv6 pia inalenga kurahisisha vipengele fulani vya utunzaji wa pakiti, kuboresha mtiririko wa datagramu na kuboresha kasi ya uhamishaji kati ya mitandao. Kwa mtazamo wa usalama, vichwa vya AH/ESP vya protocol ya *IPsec* vimejumuishwa katika vipimo vya msingi, na nodi zote za IPv6 lazima ziweze kuvitumia (RFC 6434). Matumizi yao, hata hivyo, yanasalia kuwa ya hiari: ni juu ya msimamizi kuwawezesha kulingana na muktadha.


Malengo mengine ni pamoja na utunzaji sahihi zaidi wa aina za huduma, haswa kuhakikisha ubora bora wa programu za wakati halisi (VoIP, mkutano wa video, n.k.). IPv6 pia imeundwa ili kuruhusu udhibiti unaonyumbulika zaidi wa uhamaji: kifaa kinaweza kubadilisha sehemu za ufikiaji bila kubadilisha Address yake kwa njia inayoonekana na programu zingine.


Hatimaye, IPv6 iliundwa ili kuambatana na legacy protocols. Ingawa haioani moja kwa moja na IPv4, inasalia kushirikiana kikamilifu na itifaki za juu-Layer kama vile TCP, UDP, ICMPv6 na DNS, na pia itifaki za uelekezaji kama vile OSPF na BGP, kulingana na marekebisho fulani. Kwa udhibiti wa upeperushaji anuwai, IPv6 hutumia itifaki ya MLD (*Multicast Listener Discovery*), ambayo ni utendakazi sawa na IGMP katika mazingira ya IPv4.


### Kanuni za nukuu


Moja ya mabadiliko muhimu zaidi katika IPv6 ni umbizo la IP Address yenyewe. Kwa Address upungufu wa kudumu wa anwani za IPv4, urefu wa Address umeongezwa kutoka biti 32 hadi 128, hivyo 16 byte. Kwa nadharia, hii inatoa nafasi inayowezekana ya Address ya:


$3.4 \mara 10^{38}$$


Hii inahakikisha uwezo usio na kikomo kwa vifaa vyote vya sasa na vya baadaye.


IPv6 address zimeandikwa tofauti sana na nukuu ya desimali yenye nukta nundu zinazojulikana. IPv6 Address inaundwa na vikundi vinane vya 16-bit, vilivyoandikwa kwa heksadesimali na kutengwa na koloni `:`.


Kwa mfano:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Ili kurahisisha nukuu, sufuri zinazoongoza katika kila kikundi zinaweza kuachwa. Mfano hapo juu unakuwa:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Kwa kuongezea, mlolongo mmoja unaoendelea wa vikundi vya sifuri unaweza kubadilishwa na ::, kufupisha zaidi Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Onyo:** sheria hii ni kali: mfuatano mmoja tu wa sufuri mfululizo unaweza kubadilishwa na `::`. Ikiwa Address ina mfuatano wa sufuri nyingi, ile ndefu pekee ndiyo iliyofupishwa. Hii inahakikisha upekee na usomaji.

**Maelezo muhimu:** herufi ya `:`tv inayotumika kutlo ienganisha hexadecimal block inaweza kusababisha utata katika URL, kwa kuwa `:` pia inatumikagtgglife kuashitia lango la huduma. Ili kuepuka mkanganyiko, address za IPv6 katika URL lazima ziambatanishwe katika mabano ya mraba `[ ]`.


Mfano wa ufikiaji wa HTTP kwa mlango maalum wa Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Unapowakilisha IPv4 Address katika muktadha wa IPv6, unaweza kutumia nukuu mseto katika umbo la desimali yenye vitone, ikitanguliwa na`::`:


```
::192.168.1.5
```


Utangamano huu husaidia kurahisisha mpito kati ya itifaki hizo mbili kwa kuruhusu blocks za IPv4 kujumuishwa ndani ya nafasi ya IPv6 Address.


**Kumbuka:** Ili kusawazisha jinsi anwani zinavyoandikwa, RFC 5952 inafafanua umbizo la kisheria lenye sheria za ufupisho ili kuepuka uwakilishi mwingi wa Address sawa. Kufuata mapendekezo haya husaidia kupunguza tafsiri potofu na kuhakikisha usanidi thabiti wa mtandao.


### Aina za  IPv6 Address


IPv6 inatofautiana na mtangulizi wake kupitia aina mbalimbali za Address, kila moja iliyoundwa kwa matumizi mahususi, huku ikiruhusu uelekezaji rahisi na usimamizi wa mtandao. Kama ilivyo kwa IPv4, anwani zinaweza kuwa za kimataifa, za ndani, zimehifadhiwa au mahususi kwa mifumo fulani ya mpito.


IPv6 Address ambayo haijabainishwa inawakilishwa na `::` au, kwa uwazi zaidi, `::0.0.0.0`. Fomu hii maalum hutumiwa wakati wa upataji wa Address, au kama thamani chaguo-msingi ili kuonyesha kutokuwepo kwa Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *Kwenye LAN ya faragha, kiambishi awali cha `fd00::/8` kinapendekezwa kwa kuweka addresses za ndani ambazo haziwezi kubadilishwa kwenye Mtandao.*


#### Anwani zilizohifadhiwa


Masafa fulani ya IPv6 yamehifadhiwa wazi na haipaswi kutumiwa kama anwani za kimataifa. Wana madhumuni maalum ya kiufundi:


- `::/128`: **Address isiyobainishwa, ambayo haijatolewa kabisa kwa kifaa, lakini inatumiwa kama chanzo Address na mashine inayosubiri kusanidi.**
- `::1/128`: **_loopback_ Address**, sawa na `127.0.0.1` moja kwa moja katika IPv4, ambayo inaruhusu mashine kuwa Address yenyewe.
- `64:ff9b::/96`: Imehifadhiwa kwa ajili ya watafsiri wa itifaki ili kuwezesha muunganisho wa IPv4/IPv6, kama inavyofafanuliwa katika RFC 6052.
- `::ffff:0:0/96`: kizuizi cha uoanifu cha kuwakilisha IPv4 Address katika muundo mahususi wa IPv6, mara nyingi hutumiwa ndani na programu.



Blocks hizi zinahakikisha uoanifu na kuwezesha uhamishaji kati ya matoleo mawili ya protocol.


#### Global Unicast Addresses


Global Unicast Addresses zinajumuisha sehemu kubwa ya IPv6 inayoweza kupitika hadharani, ikiwakilisha takriban 1/8 ya nafasi ya Address. Tangu 1999, IANA imetenga blocks hizi, kama vile kiambishi awali `2001::/16`, katika vizuizi vya CIDR (kutoka `/23` hadi `/12`) kwa sajili za kikanda, ambazo kisha huzisambaza kwa watoa huduma na mashirika.


Baadhi ya masafa yana matumizi maalum yaliyoandikwa:



- `2001:2::/48`: **Imehifadhiwa kwa ajili ya majaribio ya utendaji na ushirikiano (RFC 5180).**
- `2001:db8::/32`: **Imehifadhiwa kwa hati na mifano (RFC 3849).**
- `2002::/16`: Inatumika kwa utaratibu wa 6to4, ambao huruhusu trafiki ya IPv6 kusafiri katika miundombinu ya IPv4 (inatumika wakati wa awamu ya mpito kati ya protocols hizo mbili).


**Kumbuka:** sehemu kubwa ya address za kimataifa bado hazijatumika, zikitumika kama hifadhi ya ukuaji wa Intaneti wa siku zijazo.


#### Unique Local Addresses (ULA)


Unique Local Addresses  (`fc00::/7`) ni IPv6 sawa na address za kibinafsi za IPv4 (RFC1918). Zinawezesha uundaji wa mitandao ya ndani iliyotengwa bila kuhatarisha migongano na anwani za umma. Kwa mazoezi, kiambishi awali kinachofaa ni `fd00::/8`, huku biti ya 8 ikiwa 1 ili kuonyesha matumizi ya ndani. Kila block ya ULA inajumuisha kitambulishi cha ulaghai cha 40-bit, kinachopunguza migongano ya Address wakati wa kuunganisha mitandao tofauti ya kibinafsi.


#### Link-Local Addresses


Link-Local Addresses
(`fe80::/64`) hutumiwa kwa mawasiliano ndani ya sehemu sawa ya Layer 2 (VLAN sawa au switch). Hazielezwi zaidi ya kiungo cha ndani. Kila mtandao wa Interface hutengeneza kiotomatiki kiungo-ndani Address, mara nyingi hutokana na MAC Address yake kwa kutumia mpango wa EUI-64.


**Kipengele maalum**: mashine ile ile inaweza kutumia kiungo sawa cha Address kwenye violesura vingi, lakini ni lazima Interface ibainishwe inapowasiliana ili kuepuka utata.


#### Multicast Address


Katika IPv6, utangazaji umebadilishwa na utangazaji anuwai, njia bora zaidi ya kuwasilisha pakiti kwa kikundi maalum cha wapokeaji. Masafa ya utangazaji anuwai yameainishwa na `ff00::/8`. Hizi ni pamoja na address kama `ff02::1`, ambayo inalenga node zote kwenye kiungo cha ndani. Ingawa inafaa, Address hii haipendekezwi tena kwa programu, kwani inaweza matangazo ya generate yasiyodhibitiwa.


Matumizi ya kawaida ya utangazaji anuwai ni _Neighbor Discovery Protocol_ (NDP), ambayo inachukua nafasi ya ARP katika IPv6. NDP hutumia address mahususi za upeperushaji anuwai, kama vile `ff02::1:ff00:0/104`, ili kugundua seva pangishi zingine zilizounganishwa kwenye kiungo sawa.


Kwa kuchanganya aina hizi za Address, IPv6 hutoa seti kamili ya chaguo ili kukidhi mahitaji ya uelekezaji wa kimataifa, mawasiliano ya ndani, uhamiaji wa IPv4/IPv6, na usanidi wa kifaa kiotomatiki, huku ikiboresha ufanisi wa utumaji.


### Upeo wa Address


Upeo wa IPv6 Address unafafanua kikoa haswa ambacho ni halali na cha kipekee. Kuelewa dhana hii ni ufunguo wa kusimamia uelekezaji wa pakiti na upangaji wa kimantiki wa mtandao wa IPv6. Anwani za IPv6 kwa ujumla huwekwa katika makundi matatu makuu kulingana na upeo na matumizi yao: unicast, anycast na multicast.


**Address za Unicast** ndizo zinazojulikana zaidi na zinajumuisha aina ndogo tofauti.

Hizi ni pamoja na _loopback_ (`::1`) Address, ambayo upeo wake ni mdogo kwa seva pangishi inayoitumia, na ambayo hutumika kupima rafu ya mtandao ndani bila kutuma trafiki kupitia mtandao halisi.

Link-Local Address (_link-local_), ambazo upeo wake umezuiliwa kwa sehemu moja ya mtandao: hutumiwa kwa mawasiliano ya moja kwa moja kati ya vifaa kwenye kiungo sawa cha kimwili au cha kimantiki (k.m. swichi moja au VLAN).

Hatimaye, Unique Local Addresses  (_ULA_, kwa _Anwani za Kipekee za Mitaa_) ni za ndani ya mtandao wa kibinafsi. Zinaweza kuelekezwa kati ya sehemu nyingi za kibinafsi lakini hazionekani kamwe kwenye Mtandao.


Kidhahania, address za IPv6 mara nyingi huwakilishwa kama muundo wa jozi ambapo nusu ya kwanza (biti 64 za kwanza) hutambulisha kiambishi awali cha mtandao, na nusu ya pili (pia biti 64) hutambulisha Interface ya kifaa kwenye mtandao huo kwa njia ya kipekee. Mgawanyiko huu hurahisisha usanidi wa kiotomatiki wa Address kupitia mitambo kama vile SLAAC (_Stateless Address Autoconfiguration_), ambayo huruhusu mashine kiotomatiki generate Address thabiti kulingana na MAC Address au kitambulishi cha bahati nasibu.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

Usanifu wa IPv6 unafuata mtindo wa ngazi ya kimataifa wa uelekezaji wa Mtandao wa leo. Kugawanya kiambishi awali huwezesha sajili za kikanda na waendeshaji mtandao kudhibiti ugawaji wa Address kwa njia iliyogatuliwa, huku ikihakikisha upekee wa kimataifa. Ndani ya mfumo huu mpangishi sawa anaweza kushikilia kwa wakati mmoja unicast Address ya kimataifa kwa mawasiliano ya intaneti na kiunganishi cha ndani cha Address kwa mwingiliano wa ndani, k.m. kwa ujirani wa karibu au kwa ujumbe wa kugundua kipanga njia.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Address za Anycast** zinawakilisha dhana ya kati ambayo hujengwa juu ya muundo wa unicast lakini inaweza kuwa kama utangazaji anuwai katika hali fulani. Address ya anycast ni, kimsingi, unicast Address iliyopewa miingiliano kadhaa iliyosambazwa kwenye nodi tofauti za mtandao. Pakiti inapotumwa kwa Address ya onyesho lolote, protocol ya IPv6 inalenga kuiwasilisha kwa mojawapo ya seva pangishi zinazoshiriki Address, ambayo kwa kawaida ndiyo iliyo karibu zaidi katika suala la topolojia ya uelekezaji. Mbinu hii huongeza kasi ya uchakataji wa hoja na kuboresha uthabiti wa huduma zinazosambazwa. Mfano wa kawaida ni seva za DNS za mizizi, ambapo anwani ya utumaji wowote huelekeza maswali kiotomatiki kwenye eneo la karibu la uwepo.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

Katika IPv6, **Multicast Address** huchukua nafasi ya utaratibu wa utangazaji, ambao ulionekana kuwa wa gharama kubwa sana na usiofaa kwa mtandao wa kimataifa. Address ya onyesho nyingi hutambua kundi la violesura, kwa kawaida kwenye seva pangishi nyingi, ambazo zingependa kupokea pakiti sawa kwa wakati mmoja.

Kila Address ya Multicast address inajumuisha sehemu maalum ya 4-bit _scope_, ambayo inafafanua kikomo cha kijiografia au kimantiki cha utangazaji:


- Upeo wa `1` unamaanisha kuwa pakiti ni ya kifaa cha ndani pekee.
- Upeo wa `2` huzuia pakiti kwa kiungo cha ndani: vifaa vyote vilivyo kwenye sehemu sawa halisi au ya mtandaoni vinaweza kuipokea.
- Upeo wa `5` huongeza ufikiaji wa tovuti, kwa kawaida mtandao mzima wa shirika.
- Upeo wa `8` huongeza ufikiaji kwa shirika, kuwezesha uwasilishaji kwenye subnets zote za huluki moja.
- Upeo wa `e` (14 katika hexadecimal) unaonyesha ufikiaji wa kimataifa, na kufanya kikundi cha utangazaji anuwai kupatikana kutoka mahali popote kwenye Mtandao ikiwa miundombinu ya uelekezaji itaitumia.


Muundo wa IPv6 multicast Address ni pamoja na:


- sehemu ya _Bendera_ (biti 4) inabainisha ikiwa kikundi ni cha kudumu au cha muda,
- uwanja wa _Scope_ (biti 4) unafafanua wigo,
- sehemu ya kitambulisho (biti 112) inayotambulisha nambari ya kikundi cha watangazaji anuwai.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Mfano unaojulikana wa upeperushaji anuwai wa IPv6 unaotumika ni _Neighbor Discovery Protocol_ (NDP). Badala ya kutumia ARP kama IPv4, NDP inategemea Multicast Address kama vile `ff02::1:ff00:0/104` kutangaza maombi ya ugunduzi wa jirani, ikilenga wapangishi husika pekee kwenye kiungo sawa.


Kwa kufafanua mawanda ya Address kwa usahihi, IPv6 huunda jinsi mtiririko wa data unavyotumwa, kupokelewa na kupitishwa. Uzito huu hufanya itifaki kuwa rahisi na bora zaidi katika kudhibiti mawasiliano ya ndani na kimataifa, huku ikiepuka hasara za utangazaji wa jumla.


## Address Assignment katika mtandao wa ndani


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


Katika sura hii, tutaangalia mojawapo ya vipengele vya vitendo zaidi vya utumiaji wa IPv6: kugawa IP address kwa wapangishaji kwenye mtandao wa ndani. Usanifu wa IPv6 umeundwa kwa ajili ya kunyumbulika, na kuruhusu kila kifaa kuwa na generate Address yake kiotomatiki, huku bado kikiruhusu usanidi kikamilifu unapohitajika.


Mtandao wa ndani wa IPv6 kwa utaratibu hugawanya Address katika sehemu mbili:


- bits 64 za kwanza zinawakilisha kiambishi awali cha subnet, kawaida hutolewa na router au mamlaka ya Address;
- biti 64 zilizosalia hutumiwa na mwenyeji kujitambulisha kwa njia ya kipekee kwenye sehemu hiyo.

Muundo huu hurahisisha sana ujumlishaji wa njia na usimamizi wa blocks za Address.


Mbinu mbili kuu hutumiwa kugawa physical address:


- usanidi wa mwongozo, ambapo msimamizi anabainisha kila Interface halisi ya Address;
- Usanidi otomatiki, ambapo vifaa vinazalisha au hupata address zao wenyewe kiotomatiki.


Katika usanidi wa mwongozo, msimamizi huweka IPv6 Address kamili kwa kila Interface. Thamani fulani zimesalia zimehifadhiwa:


- `::/128`: Address haijabainishwa, haijakabidhiwa kabisa ;
- `::1/128`: loopback Address (_loopback_), IPv4 sawa: `127.0.0.1`.


Tofauti na IPv4, hakuna dhana _broadcast_; "sifuri zote" au "zote" mchanganyiko katika sehemu ya mwenyeji hazina maana maalum.

Usanidi wa mwongozo bado ni muhimu katika mazingira yanayodhibitiwa lakini inakuwa vigumu kudumisha kwa kiwango.


Kwa usanidi otomatiki, kuna njia kadhaa:


- protocol ya **NDP** (_Neighbor Discovery Protocol_), iliyobainishwa na RFC4862, huwezesha usanidi wa kiotomatiki wa *bila utaifa*. Katika hali hii, mwenyeji hupokea kiambishi awali cha mtandao kutoka kwa kipanga njia cha ndani, na kukamilisha Address yenyewe na kitambulisho kulingana na MAC Address yake. Njia hii ni rahisi kupeleka, na hauhitaji seva kuu.
- Utekelezaji kama ule ulio katika Windows unaweza generate sehemu ya seva pangishi bila mpangilio ili kuboresha faragha kwa kuepuka kufichuliwa moja kwa moja kwa MAC Address. Kufichua MAC Address katika pakiti za IPv6 kunaweza kuibua wasiwasi wa faragha, kwani inaruhusu ufuatiliaji wa kifaa kwenye mitandao tofauti.
- protocol ya DHCPv6: Imefafanuliwa katika RFC3315 na sawa na DHCP inayotumiwa kwa IPv4, huwezesha usanidi unaodhibitiwa zaidi na kati, ikijumuisha usimamizi wa ukodishaji, chaguo za ziada (DNS, MTU...), na usajili wa hifadhidata. DHCPv6 inaweza kufanya kazi peke yake au pamoja na usanidi usio na uraia ili kutoa vigezo vya ziada bila kukabidhi IP Address yenyewe.


**Dokezo muhimu:** Katika mbinu ya msingi ya MAC, MAC Address inabadilishwa kuwa kitambulishi cha biti 64 kwa kutumia umbizo la EUI-64. Utaratibu huu unaingiza baiti `FF:FE` katikati ya MAC Address asili (katika biti 48), na inageuza biti ya 7 ili kuonyesha upekee wa kimataifa. Matokeo yake ni kitambulisho thabiti cha Interface, kinachotumiwa katika IPv6 Address kamili.


Hapa kuna mfano wa jinsi ya kubadilisha MAC Address kuwa EUI-64:


![Image](assets/fr/045.webp)



Hata hivyo, kutokana na wasiwasi unaoongezeka juu ya ufuatiliaji wa kifaa, mifumo ya uendeshaji ya kisasa (hasa Linux, Windows 10+, macOS, Android) sasa huwasha upanuzi wa faragha kwa chaguo-msingi. Hizi hutumia vitambulishi vinavyozalishwa nasibu vya Interface ambavyo husasishwa mara kwa mara kwa miunganisho inayotoka, huku vikiweka kitambulisho thabiti cha mawasiliano ya ndani (kama vile DNS au DHCPv6).


Kama ilivyo kwa DHCP katika IPv4, address za IPv6 zilizowekwa kiotomatiki zinaweza kuwa na muda wa maisha mbili, zinazofafanuliwa na vipanga njia au seva za DHCPv6:


- Muda wa maisha unaopendekezwa: baada ya kipindi hiki, Address inasalia kuwa halali, lakini haitumiki tena kuanzisha miunganisho mipya;
- **Muda halali wa maisha**: wakati huu unapoisha, Address imeondolewa kabisa kutoka kwa usanidi wa Interface.



Mfumo huu hufanya iwezekanavyo kusimamia mabadiliko ya mtandao kwa nguvu, kwa mfano, kuhakikisha mabadiliko ya laini kutoka kwa ISP moja hadi nyingine. Kwa kusasisha kiambishi awali kilichotangazwa na vipanga njia na kurekebisha rekodi za DNS sambamba, uhamishaji wa IPv6 unaweza kufanywa bila kukatizwa kwa huduma yoyote inayoonekana.


**Kidokezo:** Matumizi ya pamoja ya mizunguko ya maisha ya Address na DNS hurahisisha utekelezaji wa mkakati wa mpito polepole, ambapo miunganisho mipya huhamia topolojia mpya, huku miunganisho iliyopo ikiendelea hadi mwisho wake wa asili.


Kwa kifupi, IPv6 inatoa anuwai ya kunyumbulika kwa Address Assignment: usanidi wa mwongozo, usanidi wa kiotomatiki usio na uraia, DHCPv6, au kizazi bila mpangilio. EE kila mbinu huja na faida na vikwazo vyake, na inaweza kubadilishwa kulingana na kiwango kinachohitajika cha udhibiti, ukubwa wa mtandao, au mahitaji ya faragha.


## Inakabidhi vitalu vya IPv6 Address


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### usambazaji wa Address


Mpango wa ugawaji wa IPv6 Address umeundwa ili kutimiza malengo mawili: kuhakikisha upekee wa kimataifa wa Address na kuwezesha upangaji wa kimantiki unaopendelea ujumlishaji na kurahisisha majedwali ya kuelekeza.

Kama ilivyo kwa IPv4, *Internet Assigned Numbers Authority* (IANA) iko juu ya daraja hili. Inasimamia nafasi ya kimataifa ya unicast Address na kukabidhi vizuizi vya Address kwa sajili tano za kikanda za mtandao (_RIR_).


RIRs tano zilizopo ni:


- ARIN (Amerika ya Kaskazini),
- RIPE NCC (Ulaya, Mashariki ya Kati, Asia ya Kati),
- APNIC (Asia-Pasifiki),
- AFRINIC (Afrika),
- LACNIC (Amerika ya Kusini na Karibiani).


IANA hutenga blocks za IPv6 za ukubwa tofauti kwa kila RIR, kwa ujumla kati ya /23 na /12. Mbinu hizi hutoa kubadilika huku ikihakikisha uimara wa muda mrefu. RIRs, kwa upande wake, husambaza tena blocks hizi kwa Watoa Huduma za Mtandao (ISPs), mashirika makubwa na taasisi za umma.


Tangu 2006, kila RIR imepokea block ya IPv6 /12 kutoka kwa IANA, saizi isiyobadilika iliyoundwa ili kuhakikisha hifadhi thabiti na kubwa ya kutosha kwa ukuaji wa siku zijazo. RIRs kawaida hugawanya hizi katika /23, /26 au /29 vitalu. ISP mara nyingi hupokea blocks /32, ingawa ukubwa huu unaweza kutofautiana kulingana na ukubwa wa ISP na eneo la kijiografia. Kwa kawaida hutenga/48 vitalu kwa wateja. Kila /48 hutoa subneti 65,536 /64 tofauti (uwezo mkubwa ikilinganishwa na IPv4).


**Dokezo muhimu:** block /32 ina blocks ndogo 65,536 /48 haswa. Hii ina maana kwamba kila ISP inaweza kuhudumia makumi ya maelfu ya wateja bila kumaliza mgao wao. Shukrani kwa /48 yake, kila mteja atakuwa na nafasi kubwa ya kuunda mtandao wake wa ndani na sehemu nyingi /64 anavyotaka.


Kiwango cha kawaida cha ugawaji kinaonekana kama hii:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Kwa wingi huu wa anwani, NAT (*Network Address Translation*), ambayo ilikuwa muhimu katika IPv4 ili kukabiliana na uhaba wa Address, haihitajiki tena. Kila seva pangishi inaweza kuwa na Address ya umma ya kipekee, inayoweza kuendeshwa kimataifa, ikirahisisha muunganisho wa mwisho hadi mwisho na kufanya itifaki kama vile IPSec, VoIP, au miunganisho ya ndani iwe rahisi kutumia.


Kuangalia ni shirika gani IPv6 Address inamilikiwa, unaweza kutumia amri ya `whois` kuuliza hifadhidata za umma za RIR. Uwazi huu unawezesha kutambua shirika ambalo linamiliki kiambishi awali, ambacho kinaweza kuwa muhimu kwa mtandao, uchambuzi au madhumuni ya usalama.


### PA vs PI kushughulikia


Hapo awali, muundo wa ugawaji wa IPv6 ulitegemea tu vizuizi vya PA (*Provider Aggregatable*), ambayo ina maana iliyounganishwa na ISP. Katika muundo huu, shirika hupokea kiambishi awali chake kutoka kwa ISP wake, kumaanisha kuwa kubadilisha watoa huduma kunahitaji kuorodhesha miundo msingi yote.


Ingawa vipengele vya usanidi otomatiki vya IPv6 na muda wa kuishi wa Address hurahisisha uwekaji nambari tena, bado haufai kwa mashirika yaliyo na miundombinu muhimu au miunganisho ya watoa huduma wengi kwa mahitaji ya kutokuwa na uwezo.


Tangu 2009, sera za ugawaji zimeruhusu blocks za PI (*Provider Independent*). Vitalu hivi (kwa kawaida / 48 kwa ukubwa) vinatolewa moja kwa moja kwa kampuni au taasisi na RIR, bila kutegemea ISP yoyote. Mtindo huu unafaa haswa kwa mashirika yanayofanya mazoezi ya *multihoming*, (maana yake yameunganishwa na waendeshaji kadhaa kwa wakati mmoja). Kwa mfano, katika Ulaya, RIPE-512 inaeleza sera ya ugawaji wa PI.


### Nukuu ya mask ya subnet


Kama IPv4, IPv6 hutumia CIDR (*Classless Inter-Domain Routing*). Hii inajumuisha kuonyesha idadi ya biti zinazounda kiambishi awali baada ya Address, kwa kutumia herufi `/`.


Chukua mfano ufuatao:


```
2001:db8:1:1a0::/59
```


Hii inamaanisha kuwa biti 59 za kwanza zimewekwa na kutambua mtandao. Biti zote zilizosalia (hapa biti 69) zinaweza kutumika kutambua subnets au seva pangishi.


Kwa hivyo, nukuu hii inashughulikia address kutoka `2001:db8:1:1a0:0:0:0:0` hadi `2001:db8:1:1bf:ffff:ffff:ffff:ffff`.


Kwa hivyo, block hii inajumuisha seti ya subneti 8/64, kila moja ikiwa na uwezo wa kupangisha idadi kubwa ya vifaa.


Nukuu za CIDR huruhusu upangaji sahihi wa nafasi ya Address, kutoka kwa mitandao mikubwa hadi usanidi wa nyumbani na mazingira ya mtandaoni, na kuhimiza ujumlishaji wa njia, kupunguza upakiaji wa kipanga njia na kuboresha uboreshaji.


### IPv6 packets and headers.


Umbizo la pakiti za IPv6 hutofautiana na IPv4 kwa kuwa rahisi na kupanuka zaidi. Datagram ya IPv6 kila mara huanza na kichwa cha ukubwa usiobadilika cha baiti 40 kilicho na taarifa zote muhimu za uelekezaji. Mbinu hii iliyoratibiwa, ikilinganishwa na urefu wa kutofautisha wa vichwa vya IPv4 (kutoka baiti 20 hadi 60), huwezesha uchakataji wa pakiti kwa haraka na bora zaidi na vipanga njia.


Hata hivyo, IPv6 haiondoi utendakazi: badala ya kuunganisha sehemu nyingi za hiari kwenye kichwa kikuu, inaleta mfumo wa vichwa vya upanuzi, vinavyowekwa mara baada ya kichwa cha msingi. Vijajuu hivi vya hiari hufanya iwezekane kuongeza data au maagizo mahususi kwa utendakazi fulani, bila kulemea pakiti za kawaida bila lazima.


Baadhi ya vichwa vya upanuzi hufuata muundo uliowekwa, wakati vingine vinaweza kushikilia idadi tofauti ya chaguo. Katika Chaguzi hizi zimesimbwa kama `{Aina, Urefu, Thamani}` sehemu tatu:


- Sehemu ya "Aina" (1 byte) inaonyesha asili ya chaguo;
- Biti mbili za kwanza za "Aina" zinataja nini ruta zinapaswa kufanya ikiwa chaguo halijatambuliwa:
 - Puuza chaguo na uendelee matibabu,
 - Acha datagram,
 - Dondosha na utume hitilafu ya ICMP kwa chanzo.
 - Dondosha datagram bila taarifa (katika kesi ya pakiti za multicast).
- Sehemu ya "Urefu" (1 byte) inabainisha ukubwa wa uga wa "Thamani", kutoka kwa 0 hadi 255 ka;
- Sehemu ya "Thamani" ina data inayohusishwa na chaguo.


Huu hapa ni muhtasari wa aina tofauti za vichwa vya viendelezi vilivyofafanuliwa na IPv6.


#### Hop-by-Hop header 


Kichwa hiki, ikiwa kipo, kila mara huwekwa mara baada ya kichwa cha msingi. Ina maelezo ambayo lazima yachakatwa na kila kipanga njia kando ya njia ya pakiti, tofauti na vichwa vingine vingi, ambavyo kwa kawaida hushughulikiwa tu na nodi lengwa. Matumizi ya kawaida ni pamoja na kuashiria vigezo vya kimataifa au kuomba hatua mahususi za uchakataji kadiri pakiti inavyosafiri kupitia mtandao.


![Image](assets/fr/047.webp)


#### Inaelekeza header


Kijajuu cha uelekezaji kinabainisha orodha ya anwani za kati ambazo pakiti lazima ipitie. Kuna njia kuu mbili za uelekezaji:


- Uelekezaji madhubuti: njia halisi imefafanuliwa
- Uelekezaji uliolegea: hatua fulani tu za lazima zimebainishwa.


Sehemu nne za kwanza za kichwa hiki cha mizizi ni:


- **Kijajuu Kinachofuata**: hubainisha aina ya kichwa kinachofuata;
- **Aina ya Uelekezaji**: inafafanua mbinu ya uelekezaji (kawaida `0`);
- **Sehemu zilizoachwa**: idadi ya sehemu zilizosalia ili kuvuka ;
- **Address[n]**: orodha ya anwani za kati.


Sehemu ya "Sehemu Zilizosalia" huanza na jumla ya idadi ya sehemu zilizosalia na hupunguzwa kwa moja kwa kila mruko.


![Image](assets/fr/048.webp)


#### Kichwa cha kugawanyika (Fragment Header)


Katika IPv6, mwenyeji wa chanzo pekee ndiye anayeruhusiwa kugawanya datagramu, tofauti na IPv4 ambapo vipanga njia vinaweza pia kufanya hivyo. Ni lazima nodi zote za IPv6 ziwe na uwezo wa kushughulikia pakiti za angalau baiti 1280. Ikiwa kipanga njia kitakumbana na pakiti kubwa kuliko MTU ya kiungo kinachofuata, hutuma ujumbe wa *ICMPv6 Pakiti Kubwa Sana* kwenye chanzo, kisha hurekebisha ukubwa wa utumaji wake.


Kichwa cha kugawanyika kina sehemu zifuatazo:


- **Kitambulisho**: kitambulisho cha kipekee cha datagramu cha kuunganisha tena.
- **Fragment Offset**: nafasi ya kipande ndani ya datagram asili.
- **M flag**: inaonyesha ikiwa vipande zaidi vinafuata.


![Image](assets/fr/049.webp)


#### Kijajuu cha uthibitishaji Authentication Header (AH)


Kichwa hiki kimeundwa ili kulinda mawasiliano kwa kuthibitisha uhalisi wa mtumaji na uadilifu wa data. Inatumika kwa kawaida na protocol ya IPsec. Kwa kutumia msimbo wa uthibitishaji, mpokeaji anaweza kuthibitisha kwamba ujumbe unatoka kwa mtumaji anayetarajiwa na kwamba haujabadilishwa wakati wa usafirishaji.


Katika tukio la jaribio la ulaghai la kurekebisha, msimbo wa uthibitishaji hautalingana tena, na datagram inaweza kukataliwa. Utaratibu huu pia hulinda dhidi ya mashambulizi ya uchezaji wa marudio kwa kugundua urudufishaji ambao haujaidhinishwa.


![Image](assets/fr/050.webp)


#### Kijajuu cha Chaguo Lengwa (Destination Options Header)


Kichwa hiki kinakusudiwa tu kwa mpokeaji wa mwisho wa datagramu. Inaweza kutumika kuongeza chaguo au metadata mahususi kwa programu, bila kuzingatiwa na vipanga njia vya kati.


Hapo awali, hakuna chaguo kama hilo lililofafanuliwa katika protocol. Hata hivyo, kichwa hiki kilianzishwa wakati IPv6 ilipoundwa, ili kuruhusu viendelezi vya siku zijazo kuongezwa bila kurekebisha muundo wa jumla wa pakiti. Chaguo batili, kwa mfano, hutumika tu kuweka kichwa kwa wingi wa baiti 8 kwa madhumuni ya upatanishi wa kumbukumbu.


![Image](assets/fr/051.webp)


Muundo wa pakiti za IPv6 umejengwa kwa utengano wazi kati ya kichwa kidogo cha msingi na vichwa vya kiendelezi vya msimu. Usanifu huu unahakikisha utendakazi wa kawaida wa uchakataji na unyumbufu unaohitajika ili kuendeleza itifaki na kuunganisha usalama, uelekezaji changamano au mifumo ya ubora wa huduma, huku ikidumisha upatanifu na miundomsingi ya siku zijazo.


## Uhusiano kati ya IPv6 na DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


Katika mitandao ya kisasa, DNS (*Domain Name System*) hutafsiri majina ya vikoa kuwa  IP address ambazo mashine zinaweza kutumia. Kwa kuanzishwa kwa IPv6, DNS ilibidi ijibadilishe ili kutumia anwani za biti-128 huku ikidumisha upatanifu wa nyuma na IPv4. Kuishi huku ni muhimu hasa katika mazingira ya rafu mbili, ambapo matoleo yote mawili ya IP yanafanya kazi kwa wakati mmoja.


### Rekodi za DNS mahususi za IPv6


Ili kuhusisha jina la kikoa na IPv6 Address, DNS hutumia rekodi ya AAAA (*quad-A*), sawa na rekodi ya "A" ya address ya IPv4. Rekodi ya AAAA inaonyesha kwa uwazi jina la kikoa hadi IPv6 Address.

Mfano:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Rekodi hii inaonyesha kuwa kikoa `ipv6.mydmn.org` kinatatuliwa hadi IPv6 Address `2001:66c:2a8:22::c100:68b`. Inawezekana, na hata kupendekezwa kwa utangamano wa hali ya juu, kuhusisha jina la kikoa sawa na anwani kadhaa za IP, iwe IPv4 (kupitia rekodi A) au IPv6 (kupitia rekodi ya AAAA). Hii inaruhusu wateja wanaooana na IPv6 kupendelea IPv6, huku ikihakikisha kuwa wateja wa IPv4 pekee wanasalia kuungwa mkono.


Kwa kuongeza, DNS inasaidia azimio la kurudi nyuma, kumaanisha kuwa inaweza kutafuta jina la kikoa linalohusishwa na IP Address iliyotolewa. Kwa upande wa IPv6, operesheni hii hutumia rekodi za PTR zilizowekwa katika eneo la `ip6.arpa`. Ukanda huu umetengwa mahususi kwa azimio la kubadili nyuma la IPv6. Kwa IPv4, ni ukanda wa `in-addr.arpa`.


### Azimio la kurudi nyuma


Azimio la kubadilisha IPv6 Address linafuata mchakato mkali:

1) Panua Address iwe nukuu kamili ya heksadesimali (baiti 16, yaani tarakimu 32 za heksadesimali).

Mfano:


```shell
2001:66c:2a8:22::c100:68b
```


Inakuwa:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Badilisha mpangilio wa kila tarakimu ya heksadesimali (nibble), zitenganishe na vitone na uambatishe `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Muundo huu huhakikisha utazamaji sanifu, wa kipekee wa kinyume katika nafasi ya IPv6 Address.


**Tafadhali kumbuka**: Hoja za DNS zinaweza kusafiri kupitia IPv4 au IPv6. protocol ya usafiri iliyotumika haina athari kwa aina ya rekodi zilizorejeshwa.

Kwa mfano:


- Mteja aliyeunganishwa kupitia IPv6 anaweza kuomba rekodi ya IPv4.
- Mteja aliyeunganishwa kupitia IPv4 anaweza kuomba rekodi ya IPv6.

Seva ya DNS hujibu kwa urahisi na rekodi ilizonazo, bila kujali itifaki ya usafiri ya hoja.


Wakati jina la mpangishaji limechorwa kwa IPv4 na IPv6, chaguo ambalo Address itatumia linasimamiwa na RFC 6724, ambayo inafafanua algoriti ya uteuzi ya Address kulingana na vipengele kama vile upendeleo wa kiambishi awali, upeo na ufikivu. Kwa chaguomsingi, IPv6 inapendekezwa kwa ujumla isipokuwa kubatilishwa na mfumo au usanidi wa mtandao.


**Kikumbusho muhimu**: unapopachika IPv6 Address katika URL (*Uniform Resource Locator*), lazima iwekwe kwenye mabano ya mraba (`[]`). Hii huepuka mkanganyiko kati ya koloni (`:`) ndani ya IPv6 Address na koloni inayotenganisha jina la mpangishaji na mlango katika URL.


Mfano halali:


```shell
http://[2001:db8::1]:8080
```


Hii inahakikisha kuwa URL inachakatwa ipasavyo na vivinjari na seva za wavuti.


Kuunganisha IPv6 kwenye mfumo wa DNS kwa hivyo kunategemea aina mpya za rekodi, mbinu madhubuti ya utatuzi wa kinyume, na sheria sahihi za uteuzi na uumbizaji ili kuhakikisha upatanifu wa uelekezaji na uthabiti.


### Muhtasari wa sehemu


Katika sehemu hii, tuligundua kanuni za kimsingi za kushughulikia IPv6. Tulianza kwa kuchunguza muundo wa IPv6 Address: urefu wake wa 128-bit, nukuu ya heksadesimali, na sheria za kurahisisha zinazotumiwa kufupisha mfuatano unaorudiwa wa sufuri. Muundo huu huwezesha IPv6 kushinda vizuizi vya nafasi ya IPv4 ya Address, huku ikihakikisha uimara na daraja bora.


Kisha tukaangalia kategoria tofauti za IPv6 address: unicast, anycast na multicast, tukielezea upeo wao, matumizi ya kawaida na uwakilishi katika nafasi ya Address.


Kisha, tulikagua mbinu za kugawa address za IPv6 ndani ya mtandao wa ndani, iwe kwa kusanidi mwenyewe, kupitia protoe ya DHCPv6, au kwa kutumia mbinu za usanidi otomatiki zisizo na uraia kama zile zinazotolewa na NDP. Mbinu hizi huwezesha vifaa kiotomatiki kuzalisha Address yao wenyewe kutoka kiambishi awali iliyotolewa na MAC yao Address (kupitia EUI-64), huku ikitoa kubadilika katika masuala ya usimamizi wa maisha na faragha.


Pia tumeeleza kwa kina jinsi vitalu vya Address vinavyogawiwa, kuanzia IANA, ambayo huvisambaza kwa RIR tano (*Regional Internet Registry*), na kisha kwa ISPs, ambao huzisambaza tena kwa wateja wao kama nyavu ndogo (mara nyingi katika /48, ikiruhusu mitandao midogo 65536/64). Tofauti kati ya vizuizi vya _Provider Aggregatable_ (PA) na _Provider Independent_ (PI) husaidia kudhibiti _multihoming_ au matukio ya kubadilisha mtoa huduma.


Tuliona kuwa DNS imejirekebisha hadi IPv6 kwa kuanzishwa kwa rekodi ya AAAA, na kwamba mbinu za kurekebisha hali sasa zinategemea ukanda wa `ip6.arpa`. Muhimu zaidi, DNS inasalia kuwa huru kutokana na itifaki ya usafiri inayotumika (IPv4 au IPv6), kuhakikisha utangamano usio na mshono katika mazingira ya rafu mbili.


IPv6 kwa hivyo sio tu uboreshaji wa ziada juu ya IPv4, lakini muundo kamili wa mfumo wa kushughulikia, uliojengwa ili kukabiliana na changamoto za sasa na za baadaye za Mtandao wa kimataifa.


Katika sehemu ya mwisho ya kozi hii ya NET 302, tutaingia kwenye mazoezi na kuzingatia zana za uchunguzi wa mtandao.



# Zana za uchunguzi wa mtandao


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Zana za Network Access Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


Katika sura hii ya kwanza ya sehemu ya mwisho ya uchunguzi wa mtandao, tunazingatia zana za kuchambua ufikiaji wa mtandao wa Layer wa mfano wa TCP/IP. Layer hii inawajibika kwa mawasiliano ya moja kwa moja kati ya vifaa kwenye mtandao huo halisi, haswa kupitia matumizi ya anwani za MAC na violesura halisi vya mtandao kama vile kadi za Ethaneti au violesura vya Wi-Fi.


Lengo hapa ni kuwapa wasimamizi zana za vitendo za kukagua, kujaribu na kuboresha Layer hii muhimu ya muunganisho wa kiwango cha chini. Zana hizi zinaweza kutumika kuthibitisha utendakazi sahihi wa violesura, kutatua matatizo ya usanidi wa kadi ya mtandao, au kugundua hitilafu kama vile migongano, upotevu wa pakiti au hitilafu za viungo.


### Huduma za local IP/MAC


#### Chombo cha `Arp`


Mojawapo ya zana kongwe zaidi za utambuzi katika Ufikiaji wa Mtandao Layer ni amri ya `arp`. Ingawa inazidi kubadilishwa na njia mbadala za kisasa kama vile `ip neigh` (ambayo tutagundua hivi punde). `Arp` bado ipo kwenye mifumo mingi ili kuona au kuchezea akiba ya ARP (*Address Resolution Protocol*). Akiba hii huhifadhi michoro kati ya address za IP na  MAC address zinazojulikana ndani ya mashine. Kwa maneno mengine, inakuwezesha kuamua ambayo kimwili (MAC) Address inalingana na IP Address iliyotolewa kwenye mtandao wa ndani.


Katika mazoezi, mpangishi anapotaka kutuma pakiti kwa IP Address ndani ya subnet sawa, lazima kwanza ajue MAC Address ya mashine inayolengwa. Uchoraji huu wa ramani unashughulikiwa na ARP, ambayo hutangaza ombi kwenye mtandao wa ndani na kupokea jibu lililo na MAC Address inayolingana. Matokeo haya huhifadhiwa kwa muda kwenye jedwali la karibu linaloitwa "cache ya ARP", ili kuzuia kurudia maombi ya kila pakiti mpya.


Kuangalia yaliyomo kwenye cache hii na kuangalia maingizo yanayojulikana kwa mashine kwa sasa, tumia:


```bash
arp -a
```


Amri hii inaorodhesha mipangilio yote ya IP/MAC iliyosajiliwa ndani, katika violesura vyote. Kila mstari hutoa jina la mpangishi (ikiwa linaweza kutatuliwa), IP Address, MAC sambamba Address na Interface ambapo uchoraji wa ramani unazingatiwa.


Ili kuchuja onyesho kwa IP Address maalum , ieleze kwa urahisi:


```bash
arp -a 192.168.1.5
```


Hii hurahisisha kuangalia kama IP Address mahususi  iko kwenye akiba, ambayo inaweza kusaidia kutambua hitilafu za mawasiliano kati ya wapangishi wawili kwenye mtandao mmoja.


Vivyo hivyo, ili kuonyesha maingizo ya ARP pekee yanayohusiana na mtandao maalum wa Interface (kwa mfano kadi ya Ethernet iitwayo `eth0`), unaweza kutumia:


```bash
arp -a -i eth0
```


Hii ni muhimu hasa katika mazingira ya Interface mbalimbali (waya, wireless, VPN, n.k.), ambapo mpangishi mmoja anaweza kuwa na adapta kadhaa za mtandao.


Amri ya `arp` haina kikomo kwa matumizi ya kusoma tu. Inaweza pia kutumiwa kuhariri akiba ya ARP mwenyewe, kipengele muhimu sana katika hali fulani za kina za utatuzi au wakati wa kuiga hali mahususi. Kwa mfano, unaweza kuongeza mwenyewe ramani ya IP/MAC:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Amri hii huunda ingizo tuli katika jedwali la ndani la ARP, ikihusisha IP Address `192.168.1.7` na MAC Address `00:17:BC:56:4F:25` kwenye Interface `eth2`. Ikiwa hakuna Interface iliyobainishwa, mfumo huo unatumia kiotomatiki kwanza.


Unaweza pia kuondoa ingizo kutoka kwa kashe ya ARP, ama kurekebisha hitilafu au kulazimisha ugunduzi upya:


```bash
arp -d 192.168.1.7
```


Hii inafuta ingizo, na kuhakikisha kuwa jaribio linalofuata la mawasiliano litaanzisha ombi jipya la ARP.


**KUMBUKA**: Chaguo la kufuta pia linakubali jina la Interface, huku kuruhusu kulenga uondoaji wa ingizo mahususi kwa usahihi zaidi.


Kwa muhtasari, zana ya `arp` hutoa uchunguzi wa kiwango cha chini, muhimu sana katika mitandao ya ndani ambapo matatizo ya muunganisho yanaweza kufuatiliwa hadi kwenye azimio lisilo sahihi au la kizamani la Address. Hata hivyo, kwenye mifumo ya hivi majuzi, hasa yenye usambazaji wa kisasa wa Linux, zana hii inazidi kubadilishwa na amri ya `ip neigh`, kutoka kwa zana ya `iproute2`, ambayo inatoa utendakazi sawa katika mfumo uliounganishwa zaidi.


#### Chombo cha `Ip neigh`


Kwenye mifumo ya kisasa, hasa usambazaji wa Linux wa hivi majuzi, amri ya `ip neigh` ndiyo zana ya kwenda kwa kukagua na kudhibiti upangaji kati ya address za IP na MAC. Amri hii ni sehemu ya safu ya `iproute2`, ambayo inabadilisha hatua kwa hatua zana za zamani kama vile `arp`, ikitoa mfumo thabiti na unaonyumbulika zaidi wa uchunguzi kwenye kiungo cha data Layer.


Amri ya `ip neigh` inaulizia akiba ya jirani ya IP ya karibu, ambayo ni sawa na akiba ya ARP ya IPv4 na akiba ya NDP (_Neighbor Discovery Protocol_) ya IPv6. Akiba hii huhifadhi miunganisho inayojulikana kati ya anwani za IP (v4 au v6) na MAC address, pamoja na hali zao (sahihi, inasubiri, muda wake umeisha...).


Amri ya msingi ya kuonyesha kashe ni:


```bash
ip neigh
```


Hii hutoa orodha ya maingizo, inayoonyesha lengwa la IP Address, mtandao husika Interface, MAC Address husika (ikiwa inapatikana), na hali ya ingizo (k.m. `RECHABLE`, `STALE`, `DELAY`, `FAILED`...).


Pato la mfano:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Laini hii inaonyesha kuwa mashine inajua upangaji sahihi wa ramani kati ya IP Address `192.168.1.5` na MAC Address `00:17:BC:56:4F:25` kupitia Interface `eth0`.


Unaweza pia kuchuja maingizo kwa vigezo kama vile IP Address, Interface, au jimbo. Kwa mfano, kuuliza tu Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Au kuonyesha maingizo yote ya Interface `eth1`:


```bash
ip neigh show dev eth1
```


Zaidi ya kushauriana, `ip neigh` pia inaweza kutumika kuhariri akiba mwenyewe. Kwa mfano, kuongeza kiingilio tuli:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Hii inahusisha kabisa IP Address `192.168.1.7` na MAC Address iliyobainishwa kwenye Interface `eth1`. Chaguo la `nud permanent` (kwa _Neighbor Unreachability Detection_) huhakikisha kuwa ingizo halitabatilishwa kiotomatiki.


Kinyume chake, kufuta ingizo la kache:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Hii inalazimisha mfumo kusuluhisha tena uchoraji wa ramani wakati mwingine utakapowasiliana na hiyo Address.


**KUMBUKA**: Zana ya `ip neigh` inafanya kazi kwa IPv4 na IPv6. Kwa IPv4, inaingiliana na ARP; kwa IPv6, inaingiliana na NDP. Hii hutoa mbinu iliyounganishwa na thabiti ya kudhibiti mahusiano ya IP/MAC katika familia zote za itifaki, na kufanya `ip neigh` kuwa kiwango cha kisasa cha usimamizi wa jirani kwenye mifumo ya Linux.


### Zana za uchambuzi wa packets 


Ili kuchambua kwa kina kile kinachotokea kwenye mtandao wa kompyuta, wasimamizi wanahitaji zana ambazo zinaweza kunasa pakiti zilizobadilishwa kati ya mashine. Huduma mbili zinajitokeza kama vigezo: `tcpdump` na `Wireshark`. Zana hizi ni muhimu kwa kutambua tabia isiyo ya kawaida, kukagua ubadilishanaji wa protocol, au kusoma usalama wa mtandao kwa kukagua yaliyomo kwenye fremu.


#### `ttcpdump`: uchambuzi wa mstari wa amri


`tcpdump` ni zana yenye nguvu zaidi ya safu ya amri iliyoundwa ili kunasa na kuonyesha pakiti zinazosafiri kupitia mtandao wa Interface. Inafanya kazi kwa wakati halisi, na shukrani kwa muundo wake mwepesi, inaweza kutumika kwenye mifumo isiyo na picha ya Interface au kwa rasilimali ndogo. Inategemea maktaba ya `libpcap`, ambayo hutoa vipengele vya kukamata vya kiwango cha chini visivyotegemea maunzi.


Matumizi ya kawaida ya `tcpdump` ni kufuatilia shughuli za mtandao za sehemu ya mashine au mtandao, kuchuja pakiti kulingana na vigezo maalum. Matokeo yanaweza kuelekezwa kwenye faili, ikiruhusu trafiki kuhifadhiwa kwa uchanganuzi wa baadaye au kuchezwa tena katika zana nyingine, kama vile Wireshark.


Syntax ya amri ya jumla ni:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` huandika pakiti zilizonaswa kwa faili katika umbizo la `libpcap` (kiendelezi `.cap` au `.pcap`);
- `-i` hubainisha mtandao wa Interface wa kufuatilia (k.m. `eth0`, `wlan0`);
- `-s` huweka kiwango cha juu zaidi cha data iliyonaswa kwa kila pakiti. Kubainisha `0` kunasa pakiti zote;
- `-n` huzima DNS na azimio la jina la huduma, kuboresha utendaji.


Vichungi vya usemi mwishoni mwa amri vinakuwezesha kuzuia kunasa kwa kikundi kidogo cha trafiki.
Unaweza kuchanganya maneno `mwenyeji`, `bandari`, `src`, `dst`, n.k., ili kuboresha uteuzi.


Mfano: kunasa pakiti za HTTP (mlango 80) kwenda au kutoka kwa seva ya `192.168.25.24`, na kuzihifadhi katika faili ya `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Faili inayotokana inaweza baadaye kuchambuliwa katika zana ya picha au kuchezwa tena kwenye mfumo mwingine.


#### Wireshark: uchambuzi wa hali ya juu wa kuona (Advanced visual analysis)


Wireshark, ambayo zamani ilijulikana kama *Ethereal*, ni programu kamili ya uchanganuzi wa mtandao yenye Interface ya picha. Tofauti na `tcpdump`, hutoa taswira yenye muundo, ya kina ya pakiti, ikiwa ni pamoja na mgawanyo wa protocol, grafu za mtiririko, takwimu za trafiki na vichujio shirikishi. Pia inategemea `libpcap`, ambayo inamaanisha inaweza kufungua na kuchakata faili za kunasa zinazozalishwa na `tcpdump`.


Wireshark inapatikana kwenye mifumo mingi ya uendeshaji, ikiwa ni pamoja na Linux na Windows. Kuisakinisha kunahitaji haki za msimamizi ili kufikia violesura vya kunasa. Baada ya kuzinduliwa, unaweza kuchagua mtandao wa Interface kutoka kwa menyu ya *Nasa*. Kubofya *Anza* huanza kurekodi pakiti katika wakati halisi. Uonyesho umegawanywa katika paneli tatu:


- orodha ya viunzi vilivyokamatwa;
- maelezo ya protocol,
- data ghafi ya heksadesimali.



![Image](assets/fr/052.webp)



Wireshark hufaulu katika hali ambapo unahitaji kuchunguza tabia changamano ya protocol, kuunda upya vidadisi vya programu (kama vile kipindi cha HTTP au DNS), au nyakati za majibu ya huduma ya masomo. Pia inasaidia vichujio mahususi vya kuonyesha kwa kutumia sintaksia yake maalum (tofauti na ile ya `tcpdump`) ili kulenga pakiti husika pekee.


#### Zana za ziada


Ni muhimu kutambua kwamba `tcpdump` na Wireshark hazibadiliki: kila moja ina uwezo wake. `tcpdump` inafaa zaidi kwa mazingira ya safu ya amri, hati otomatiki na uingiliaji kati wa seva ya mbali, wakati Wireshark ni bora kwa uchanganuzi wa kina, shirikishi na wa elimu wa trafiki.


Zana hizi mbili zinaweza kuunganishwa: kunasa kunaweza kufanywa kwenye mfumo wa mbali kwa `tcpdump`, kisha faili ya `.cap` inahamishwa kwa uchambuzi na Wireshark kwenye mashine ya ndani. Njia hii hutumiwa sana katika mazoezi.


### Zana za uchambuzi wa Interface


Katika Layer ya Ufikiaji wa Mtandao, mara nyingi ni muhimu kuuliza na kusanidi miingiliano ya mtandao halisi ili kutambua hitilafu, kuboresha utendakazi, au kuthibitisha uadilifu wa muunganisho. Moja ya zana zenye nguvu zaidi zinazopatikana chini ya Linux kwa madhumuni haya ni `ethtool`, matumizi ya mstari wa amri ambayo sio tu hutoa maelezo ya kina ya kiufundi kuhusu Ethernet Interface, lakini pia inakuwezesha kurekebisha baadhi ya vigezo vyake kwa wakati halisi.


#### Tazama vipimo vya Interface


Element kuu ya `ethtool` ni uwezo wake wa kuuliza Interface na kuonyesha sifa zake za sasa. Hii hukuruhusu kuangalia:


- kasi ya kiungo (k.m. 100 Mbit/s, 1 Gbit/s au 10 Gbit/s);
- hali ya mazungumzo (nusu duplex au duplex kamili);
- ikiwa mazungumzo ya kiotomatiki yamewezeshwa;
- aina ya bandari (shaba, nyuzi, nk);
- hali ya kiungo (inafanya kazi au la);
- uwezo wa kutumia elements za kina kama vile *Wake-on-LAN*.


Taarifa hii ni muhimu sana kwa ajili ya kuchunguza matatizo yanayohusiana na muunganisho wa kimwili au mipangilio ya mazungumzo isiyolingana kati ya kadi ya mtandao ya seva pangishi na kifaa inachounganisha kwa (switch, router, nk.).


Ili kupata habari hii, endesha tu:


```bash
ethtool enp0s3
```


Amri hii hutoa ripoti ya kina kuhusu `enp0s3` Interface, mkataba wa kawaida wa kutaja majina kwenye mifumo inayotegemea CentOS au RHEL.



![Image](assets/fr/053.webp)



#### Badilisha kwa nguvu vigezo vya Interface


`ethtool` sio tu kwa uchunguzi: pia hukuruhusu kurekebisha vigezo fulani vya Interface bila kuwasha tena mashine. Hii inafanya uwezekano, kwa mfano, kulazimisha kasi ya kiungo maalum au kuwezesha vipengele kulingana na mahitaji ya mtandao wa ndani.


Chaguo la `-s` linatumika kusanidi vigezo kama vile:


- kasi ya kiungo (`kasi`), iliyowekwa wazi (k.m. 1000 kwa 1 Gbit/s);
- hali ya duplex (`duplex`), ama `nusu` au `kamili` ;
- kuwezesha au kulemaza mazungumzo ya kiotomatiki (`autoneg`);
- kuwezesha *Wake-on-LAN* (`wol`) ;
- aina ya bandari.


Mfano wa 1: wezesha mazungumzo ya kiotomatiki kwenye Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Mfano wa 2: washa kipengele cha *Wake-on-LAN* (ili kuruhusu mashine kuamka kwa mbali kupitia pakiti ya uchawi):


```bash
ethtool -s enp0s3 wol p
```


Katika mfano huu, chaguo la `p` linabainisha kuwa kuamka kutatokea pindi tu pakiti ya *Wake-on-LAN* itakapotambuliwa. Mipangilio hii mara nyingi hutumiwa katika mazingira ya biashara kufanya masasisho ya usiku mmoja au matengenezo ya mbali.


#### Ufungaji wa zana


Ni muhimu kutambua kwamba `ethtool` haijasakinishwa kila mara kwa chaguo-msingi. Kwenye usambazaji wa Red Hat/CentOS, inaweza kusanikishwa kwa amri:


```bash
yum install -y ethtool
```


Kwenye Debian na Ubuntu, amri sawa ni:


```bash
sudo apt install ethtool
```


**ONYO**: katika amri zote za `ethtool`, jina la mtandao Interface lazima libainishwe mara tu baada ya chaguo (kama `-s`). Hitilafu yoyote ya kisintaksia katika uwekaji wa vigezo itafanya amri kuwa batili au kutofanya kazi.



## Zana za network Layer


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Zana za uchambuzi wa trafiki


Katika uchunguzi wa mtandao, amri ya `ping` inasalia kuwa mojawapo ya zana rahisi lakini zenye nguvu zaidi za kujaribu muunganisho kati ya mashine mbili. Hukagua kama seva pangishi ya mbali inaweza kufikiwa kwa wakati fulani, huku pia ikitoa maelezo kuhusu muda wa kusubiri, uthabiti wa kiungo, na azimio la DNS.


Amri ya `ping` inategemea protocol ya ICMP (*Internet Control Message Protocol*). Mtumiaji anapotuma ombi `ping`, mfumo hutuma pakiti ya ICMP "Echo Request" kwa IP Address au jina la mpangishaji. Ikiwa mashine inayolengwa iko mtandaoni na njia ya mtandao ni halali, inajibu kwa pakiti ya "Echo Reply" ya ICMP. Utaratibu huu rahisi unaweza kutumika kupima muda wa kusubiri na kugundua matatizo ya muunganisho au utatuzi wa majina.


Mfano wa amri ya classic:


```bash
ping 172.17.18.19
```


Jibu la kawaida:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


Katika mfano huu, utatuzi wa jina umetekelezwa kiotomatiki: kikoa `mydmn.org` kinahusishwa na IP Address `172.17.18.19`, ikithibitisha kuwa azimio la DNS hufanya kazi ipasavyo. Amri pia hutoa maelezo ya kiufundi kama vile:


- nambari ya mfuatano wa iCMP (`icmp_seq`), muhimu kwa kuangalia mpangilio wa majibu;
- TTL (*Time-To-Live*), ambayo inaonyesha idadi ya humle iliyobaki kabla ya pakiti kutupwa;
- muda wa kwenda na kurudi/kuchelewa (`muda`), inavyoonyeshwa kwa milisekunde, ikitoa makadirio ya muda wa kusubiri wa kiungo.


#### Uchambuzi wa kina zaidi wa vigezo vya ICMP


TTL ni sehemu muhimu katika protocol ya IP. Kila datagramu inaanzishwa kwa thamani ya TTL na mtumaji (mara nyingi 64, 128 au 255). Kila kipanga njia kilicho kwenye njia kinapunguza thamani hii kwa 1. Ikiwa TTL itafikia 0 kabla ya kufika inakoenda, pakiti hutupwa na hitilafu ya ICMP inarejeshwa kwa mtumaji. Utaratibu huu huzuia loops zisizo na kikomo za uelekezaji.


Muda wa uenezi (*Round-trip delay / time*) hupima kuchelewa kwa pakiti kuondoka kwa mtumaji, kufikia lengo na kurudi. Kwa mazoezi, ucheleweshaji chini ya 200 ms unachukuliwa kuwa unakubalika kwa kiungo thabiti. Ucheleweshaji wa juu usio wa kawaida unaweza kuonyesha msongamano wa mtandao, uelekezaji usiofaa, au ubora duni wa kiungo.


#### Matumizi ya juu ya `ping`


`ping` hutoa chaguo za kuboresha majaribio na kuangalia tabia mahususi za mtandao.


Kutuma maombi ya utangazaji, unaweza kutumia chaguo `-b` kulenga wapangishaji wote kwenye mtandao mdogo:

```bash
ping -b 192.168.1.255
```


Hii ni muhimu kwenye mitandao ya ndani kugundua haraka vifaa vinavyofanya kazi au kujaribu jinsi mtandao unavyoshughulikia maombi ya matangazo. Hata hivyo, katika mipangilio mingi, routers na firewalls huzuia pings za matangazo ili kuzuia mashambulizi ya aina ya amplification.


Unaweza pia kutaja muda maalum kati ya maombi na chaguo `-i` (chaguo-msingi: sekunde 1):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Hii hutuma maombi 10 ya ICMP kwa vipindi vya sekunde 0.2. Jaribio kama hilo ni muhimu kwa kugundua kushuka kwa kasi kwa muda kwa muda mfupi au kwa kusisitiza kidogo kiungo cha kutathmini uthabiti wake.


### Zana za uchambuzi wa jedwali la uelekezaji


Amri ya `ip route`, sehemu ya `iproute2` suite, ndiyo zana inayopendekezwa na ya kawaida kwenye mifumo ya kisasa ya Linux kwa ajili ya kukagua na kudhibiti jedwali la kuelekeza la IP la kernel. Inachukua nafasi ya amri ya kizamani ya `njia`, ikitoa sintaksia iliyo wazi zaidi, uthabiti mkubwa zaidi, na usaidizi uliopanuliwa wa Elements za kisasa (IPv6, majedwali mengi, nafasi za majina, n.k.).


#### Inaonyesha jedwali la uelekezaji


Ili kuonyesha jedwali la sasa la uelekezaji:


```bash
ip route show
```


Pato hili huorodhesha njia zote zinazojulikana kwa kernel, ambayo ni, njia ambazo pakiti zinazotoka huchukua kulingana na marudio yao.


Pato la mfano:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Kila mstari unawakilisha njia. Sehemu kuu ni pamoja na:


- **chaguo-msingi**: njia chaguo-msingi, inayotumiwa wakati hakuna njia mahususi inayolingana.
- **kupitia**: lango linalotumiwa kufikia lengwa.
- **dev**: mtandao wa Interface uliotumika.
- **proto**: jinsi njia iliundwa (mwongozo, DHCP, kernel, nk).
- **metric**: gharama ya njia, inayotumika kuweka kipaumbele njia nyingi zinazowezekana.
- **upeo**: upeo wa njia (k.m. `kiungo` kwa njia iliyounganishwa moja kwa moja).
- **src**: chanzo cha IP Address kinachotumika kwa pakiti zinazotoka kwenye Interface hii.


#### Kuongeza na kufuta njia


Unaweza pia kurekebisha jedwali la uelekezaji kwa nguvu, kwa mfano kwa kuongeza au kuondoa njia tuli.


Kuongeza njia tuli:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Hii husanidi njia kuelekea mtandao wa `192.168.1.0/24`, kupitia lango la `192.168.1.1` kwenye Interface `eth0`.


Ondoa njia hii:


```bash
ip route del 192.168.1.0/24
```


Amri hii inafuta njia iliyoainishwa hapo awali.


#### Amri muhimu


Hapa kuna vibadala muhimu vya uchanganuzi au uandishi:


- `njia ya ip -4`: inaonyesha njia za IPv4 pekee;
- `njia ya ip -6`: inaonyesha njia za IPv6 pekee;
- `Jedwali kuu la orodha ya njia`: linaonyesha jedwali kuu la kuelekeza (thamani chaguo-msingi);
- `ip route pata <Address>`: onyesha ni Interface gani na lango la pakiti ya Address iliyotolewa.


Mfano:


```bash
ip route get 8.8.8.8
```


Hii inaonyesha njia kamili ambayo pakiti inaweza kuchukua kufikia `8.8.8.8`.


### Zana za kufuatilia


Mojawapo ya zana bora zaidi za kuchanganua njia iliyochukuliwa na pakiti za IP kati ya seva pangishi chanzo na lengwa lengwa ni amri ya `traceroute`. Inaonyesha, hatua kwa hatua, njia inayofuatwa na pakiti na kutambua ruta za kati wanazopitia. Katika tukio la hitilafu ya kiungo cha mtandao au kukatika kwa huduma, `traceroute` husaidia kubainisha eneo mahususi la tatizo.


Kama ilivyo kwa amri ya `ping`, lengo linaweza kubainishwa kwa jina lake la kikoa lililohitimu kikamilifu (FQDN) au kwa IP Address yake. Kwa mfano:


```bash
traceroute mydmn.org
```


#### Kanuni ya uendeshaji


`traceroute` inategemea sehemu ya TTL (*Time To Live*) katika kichwa cha pakiti za IP. Kama ilivyoelezwa hapo awali, uwanja huu ni kihesabu kilichopunguzwa na kila kipanga njia kwenye njia. Wakati TTL inafikia sifuri, pakiti inatupwa, na router inarudi ujumbe wa ICMP "Muda Uliopita" kwa mtumaji. Utaratibu huu huzuia vitanzi visivyo na kikomo katika tukio la kupotosha.


`traceroute` inachukua fursa ya tabia hii kuweka ramani ya router kati ya mtumaji na mpokeaji:


- Kwanza hutuma mfululizo wa pakiti za UDP (kawaida tatu), na TTL ya 1. Kipanga njia cha kwanza hukutana na TTL ya 0 hivyo hutupa pakiti na kisha kujibu kwa ujumbe wa ICMP, kufichua IP  Address yake na wakati wa majibu.
- Ifuatayo, inatuma safu nyingine ya pakiti na TTL ya 2, ikifunua kipanga njia cha pili.
- Mchakato unajirudia hadi unakoenda kufikiwa, wakati ambapo mwenyeji hujibu kwa ujumbe wa Lango la ICMP Usioweza kufikiwa, kuonyesha kwamba mwisho umefikiwa.


Kwa chaguo-msingi, `traceroute` hutumia pakiti za UDP zinazotumwa kwa milango isiyotumika (kawaida kuanzia 33434), lakini pia inaweza kusanidiwa kutumia ICMP (kama `ping`) au hata TCP, kulingana na mifumo au vibadala vya amri.


Pato la mfano:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Kila mstari unalingana na router iliyopitiwa, na hadi vipimo vya muda vitatu (katika milliseconds) vinavyoonyesha muda wa safari ya kwenda na kurudi kwa router hiyo. Thamani hizi husaidia kutathmini utendakazi wa kila sehemu ya mtandao.


#### Tafsiri ya matokeo


Ikiwa router haijibu au kuchuja ujumbe wa ICMP, nyota `*` zitaonyeshwa badala ya muda wa kujibu. Hii inaweza kuonyesha:


- ukuta unaozuia majibu ya ICMP,
- kifaa kilichosanidiwa kutojibu, au
- suala la muunganisho wa muda njiani.


Kwa hivyo, `traceroute` haitambui tu njia iliyopitishwa lakini pia inaangazia sehemu za kusubiri au kukatizwa kwa njia isiyo ya kawaida.


Kwenye baadhi ya mifumo, amri sawa ya `tracepath` inaweza kutumika, ambayo haihitaji upendeleo wa mizizi. Kwa IPv6, tumia `traceroute6` au `tracepath6`.


Mfano wa ufuatiliaji wa IPv6:


```bash
traceroute6 ipv6.google.com
```


### Zana za kuangalia miunganisho inayotumika


Ili kutambua miunganisho amilifu ya mtandao na kufuatilia shughuli za mtandao kwenye mfumo wa Linux, amri `ss` (fupi kwa _socket statistics_) ndiyo zana ya kisasa ya marejeleo. Sehemu ya 'iproute2` suite, inachukua nafasi ya `netstat` ambayo imepitwa na wakati sasa, ikitoa utendaji bora na matokeo sahihi zaidi.


`ss` huonyesha miunganisho inayotumika ya TCP na UDP, milango ya kusikiliza, address za karibu na za mbali, hali za muunganisho na michakato inayohusiana.


#### Matumizi ya jumla


Inapoendeshwa bila chaguo, amri `ss` huonyesha miunganisho amilifu ya TCP. Sintaksia ya msingi:


```bash
ss [options]
```


Chaguzi zingine za kawaida za uchanganuzi wa kusafisha:


- `-t`: onyesha miunganisho ya TCP pekee;
- `-u`: onyesha miunganisho ya UDP pekee;
- `-l`: onyesha soketi za kusikiliza pekee;
- `-n`: zima azimio la jina (IPs ghafi na nambari za mlango);
- `-p`: onyesha kila michakato inayohusiana na tundu (PID na jina la programu),
- `-a`: onyesha miunganisho yote, ikijumuisha isiyotumika,
- `-s`: onyesha takwimu za soketi za kiwango cha juu.


#### Uchunguzi wa kesi


Kuonyesha miunganisho yote inayotumika kwa kutumia bandari ya TCP 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Hii inaonyesha miunganisho amilifu ya TCP inayohusisha mlango wa 80. Majimbo kama vile `SIKILIZA`, `IMESTABISHWA`, `TIME-WAIT` huonyesha hali ya sasa ya kila Exchange.


Pato la mfano:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Kuonyesha miunganisho yote ya mtandao na michakato inayohusiana:


```bash
ss -tulnp
```


Ili kupata muhtasari wa jumla wa matumizi ya socket:

```bash
ss -s
```


Ili kuchuja miunganisho ya UDP pekee:

```bash
ss -unp
```


Amri hizi ni muhimu sana kwa kugundua miunganisho ya kutiliwa shaka, milango ya kusikiliza isiyotarajiwa au kufuatilia shughuli za huduma mahususi.


## Transport na zana za juu za Layer


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Zana za kuuliza za DNS


Katika tabaka za juu za muundo wa TCP/IP, haswa kwenye Programu ya Layer, ni muhimu kuelewa jinsi azimio la jina linavyofanya kazi. Zana za uulizaji wa DNS hukuruhusu kuangalia kama jina la kikoa linahusishwa kwa usahihi na IP Address, na pia kusaidia kutambua matatizo ya seva ya DNS kama vile usanidi usiofaa, ucheleweshaji wa uenezi au kutopatikana. Zana hizi ni muhimu kwa msimamizi yeyote wa mtandao au mtumiaji yeyote anayetaka uelewa wa kina wa ubadilishanaji wa DNS katika mazingira ya IP.


#### Amri ya `nslookup`


Zana rahisi zaidi ya uulizaji wa DNS ni `nslookup`. Hutuma swali kwa seva ya DNS na kurudisha IP Address inayohusishwa na jina la Domain (au kinyume chake). Kwa chaguo-msingi, inauliza seva ya DNS iliyosanidiwa ya mfumo, lakini pia unaweza kutaja seva moja kwa moja kwenye amri.


Mfano wa uchunguzi wa moja kwa moja:

```bash
nslookup mydmn.org
```


Kuuliza seva maalum ya DNS:

```bash
nslookup mydmn.org 192.6.23.4
```


Ombi linauliza seva ya DNS katika `192.6.23.4` kutatua jina `mydmn.org`. Hii ni muhimu sana ili kuangalia kama seva fulani ya DNS inatambua jina la kikoa au kuthibitisha kuwa seva inafanya kazi ipasavyo.


#### Amri ya `chimba`


`dig` (*Domain Information Groper*) ni zana ya kisasa zaidi, kamili na inayoweza kunyumbulika kuliko `nslookup`. Inaauni maswali changamano na hutoa maelezo ya kina kuhusu mchakato wa utatuzi, safu ya seva zinazohusika, aina ya rekodi iliyorejeshwa (A, AAAA, MX, TXT, n.k.), na hitilafu zozote zinazopatikana.


Mfano wa swali la msingi:

```bash
dig mydmn.org
```


Kuuliza seva maalum ya DNS:

```bash
dig @192.6.23.4 mydmn.org
```


Amri hii hukagua upatikanaji wa rekodi ya DNS kwenye seva fulani.

Moja ya faida kuu za `dig` ni kwamba inaonyesha maelezo ya jibu la DNS, na kuifanya kuwa muhimu sana kwa kuchunguza makosa ya usanidi.


#### Usanidi wa mikono wa visuluhishi vya DNS


Wakati mwingine ni muhimu kubatilisha seva za DNS zinazotumiwa ndani ya nchi, kwa mfano, katika mazingira ya majaribio au kulazimisha matumizi ya seva maalum. Hili linaweza kufanywa kwa kuhariri faili ya `/etc/resolv.conf`, ambayo inafafanua mipangilio ya mfumo wa utatuzi wa DNS.


Mfano wa usanidi:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Sehemu ya `tafuta` inabainisha kikoa cha kuambatisha kiotomatiki wakati wa kusuluhisha majina mafupi.
- Maingizo ya `nameserver` yanafafanua seva za DNS za kutumia, kwa mpangilio wa kipaumbele.


Kwenye usambazaji wengi wa kisasa (hasa wale wanaotumia `systemd-resolved`), mabadiliko ya `/etc/resolv.conf` ni ya muda na yanaweza kufutwa wakati kuwashwa upya au kuunganisha tena mtandao. Mbinu zaidi za kudumu ni pamoja na kutumia `resolvconf`, `systemd-resolved`, au kurekebisha usanidi wa *NetworkManager*.


#### Amri ya `mwenyeji`


Zana nyingine rahisi lakini yenye ufanisi ya DNS ni `mwenyeji`. Hutatua majina ya vikoa kuwa address za IP (au kinyume) na inaweza kusaidia kutambua hitilafu za DNS au usanidi usiofaa kwenye mtandao wa Interface.


Mifano:

```bash
host mydmn.org
```


Utafutaji wa nyuma:

```bash
host 192.6.23.4
```


`owner` ni rahisi sana kwa ukaguzi wa haraka, haswa inapotumika katika hati za safu ya amri.


Maswali yanayorudiwa au ya kina kwa seva za DNS za watu wengine bila ruhusa yanaweza kufasiriwa kama majaribio ya kuingiliwa au shughuli hasidi. Zikitumiwa vibaya, au dhidi ya mitandao usiyodhibiti, amri hizi zinaweza kufanana na uchunguzi wa uchunguzi tena, ambao mara nyingi huwa hatua ya kwanza katika shambulio. Daima zuia matumizi yao kwa mazingira unayosimamia au ambapo una idhini ya wazi.


### Zana za Kuchanganua Mtandao


Unapofuatilia au kupata mtandao wa eneo au eneo pana, ni muhimu kutambua vifaa vinavyotumika na huduma zinazofichua. Hivi ndivyo zana ya `nmap` (*Network Mapper*) hufanya.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Tunakuletea `nmap`


`nmap` inaruhusu uchanganuzi unaolengwa wa seva pangishi moja au zaidi ili kugundua milango iliyo wazi, huduma zinazopatikana (HTTP, SSH, DNS, n.k.), na wakati mwingine hata aina ya mfumo wa uendeshaji unaotumika. Shukrani kwa chaguo zake nyingi, `nmap` hutoa muhtasari sahihi wa uso wa kukaribia aliye na mtandao, muhimu wakati wa ukaguzi au ugumu wa awamu za usimamizi wa miundombinu.


Kama tu amri ya `owner`, `nmap` haipaswi kamwe kutumika kwenye mitandao au miundomsingi usiyomiliki, au bila idhini ya wazi. Uchanganuzi wa bandari ambao haujaidhinishwa unaweza kualamishwa kama majaribio mabaya ya upelelezi, mara nyingi hutambuliwa na mifumo ya usalama (firewalls, IDS/IPS), na inaweza hata kusababisha matokeo ya kisheria.


#### Matumizi ya msingi


Ili kuchanganua seva pangishi na kutazama bandari zake wazi:

```bash
nmap 192.168.0.1
```


Amri hii huchanganua milango 1000 ya kawaida kwenye seva pangishi `192.168.0.1` na kuonyesha huduma zinazofikiwa na itifaki zilizotumika. Ikiwa azimio la DNS limesanidiwa, unaweza pia kutumia jina la mpangishaji badala ya IP Address.


#### Kamilisha kuchanganua mtandao


Moja ya faida za `nmap` ni uwezo wake wa kuchanganua anuwai nzima ya anwani kwa amri moja. Hii inafanya iwe rahisi, kwa mfano, kuhesabu haraka mashine zote zinazotumika kwenye mtandao:


```bash
nmap 192.168.0.0/24
```


Katika hali hii, wapangishi wote katika safu `192.168.0.0` hadi `192.168.0.255` wataulizwa. Kwa kila IP Address, matokeo yanaorodhesha bandari zilizo wazi, hali yao (wazi, iliyochujwa, nk), na, inapowezekana, jina la huduma inayofanana.



![Image](assets/fr/055.webp)



Msimamizi anaweza kutegemea `nmap` kwa kazi kadhaa:


- **Kugundua seva pangishi zinazotumika**: tambua ni mashine zipi zinazojibu ndani ya subnet;
- **Orodha ya huduma**: hakikisha ni bandari zinazohitajika pekee ndizo zinazofikiwa (kanuni ya upendeleo mdogo);
- **Ukaguzi wa kufuata**: linganisha bandari zilizo wazi dhidi ya sera ya usalama ya shirika;
- **Kinga ya hatari**: tambua huduma zisizo salama au zilizopitwa na wakati zinazoendeshwa kwenye mashine muhimu.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Mchakato wa zana za kuhoji


Kwa uchanganuzi wa kina wa michakato inayotumika na faili zilizofunguliwa, haswa katika muktadha wa mtandao, wasimamizi wa Linux mara nyingi hutumia amri ya `lsof` (*Orodha Fungua Faili*). Licha ya jina lake, `lsof` sio tu kwa faili za jadi: kwenye mifumo ya UNIX, kila kitu kinachukuliwa kuwa faili, pamoja na soketi za mtandao, vifaa na njia za mawasiliano.


Chombo hiki kwa hiyo hutoa mtazamo wa sehemu mbalimbali wa mfumo kwa kuunganisha michakato inayotumika, bandari za mtandao wazi, faili zilizopatikana, na watumiaji wanaohusika.


#### Uchambuzi wa mtandao na `lsof`


Chaguo la `-i` huzuia utoaji kwa miunganisho ya mtandao (TCP, UDP, IPv4, au IPv6). Hii hurahisisha kuona ni michakato gani inayowasiliana kwenye mtandao:


```bash
lsof -i
```


Amri hii inaorodhesha michakato yote inayoendeshwa kwa kutumia tundu la mtandao, inayoonyesha mlango unaotumika, itifaki (TCP/UDP), hali ya muunganisho, pamoja na PID na mtumiaji husika.


#### Kuchuja kwa IP Address au port


Unaweza kuboresha utafutaji kwa kubainisha IP Address na mlango, kutenga mtiririko fulani wa mtandao. Kwa mfano, kuangalia kipindi cha SMTP (port 25) na mwenyeji maalum:


```bash
lsof -n -i @192.168.2.1:25
```


Hii itaonyesha tu miunganisho amilifu ya mtandao iliyo na seva pangishi `192.168.2.1` kwenye mlango wa 25, muhimu kwa kutambua shughuli zinazotiliwa shaka au masuala ya mtiririko wa SMTP.


#### Ufuatiliaji wa ufikiaji wa kifaa


Nguvu nyingine ya `lsof` ni kufuatilia faili maalum kama vile sehemu za diski. Kwa mfano, kuangalia ni michakato gani imefungua faili kwenye `/dev/sda1`:


```bash
lsof /dev/sda1
```


Hili linafaa wakati jaribio la kuteremsha halitafaulu kwa sababu kifaa bado kinatumika, au wakati wa kuchunguza ni programu zipi zinazofikia kizigeu.


#### Uchambuzi mtambuka: mchakato na mtandao


Chaguzi zinaweza kuunganishwa kwa maarifa sahihi. Kwa mfano, kuona bandari zote za mtandao zikifunguliwa na mchakato na PID 1521:


```bash
lsof -i -a -p 1521
```


Chaguo la `-a` linaingiliana na vigezo (`-i` na `-p`), likizuia pato kwa miunganisho ya mtandao pekee ya mchakato huo.


#### Ufuatiliaji wa watumiaji wengi


`lsof` pia inaweza kutumika kuchanganua shughuli za watumiaji maalum, kuorodhesha faili zote ambazo wamefungua, kuchujwa kwa hiari na PID:


```bash
lsof -p 1521 -u 500,phil
```


Hii inaonyesha faili au miunganisho ya mtandao inayotumiwa na mtumiaji `phil` au UID 500, iliyodhibitiwa kuchakata 1521.


### Muhtasari wa Sehemu


Katika sehemu hii ya mwisho, tumechunguza zana mbalimbali muhimu za kuchunguza, kuchanganua, na kusimamia mitandao ya kompyuta. Ukiwa umeundwa kuzunguka safu za muundo wa TCP/IP, utafiti huu haufafanui tu jinsi mawasiliano ya mtandao hufanya kazi lakini pia huanzisha mbinu madhubuti ya kutambua, kutenga na kutatua masuala yanayoweza kutokea.


Zana hizi huwapa wasimamizi seti madhubuti ya viunzi vya kiufundi kufuatilia afya ya mtandao, kuchanganua trafiki, miunganisho ya ukaguzi na kuingilia kati haraka vifaa au huduma mbovu.


#### Network Access Layer


Zana zinazotoa mwonekano wa moja kwa moja katika violesura na fremu:


- **arp / ip neigh**: kagua na urekebishe akiba ya ARP/NDP ili kuangalia au kusahihisha miunganisho ya IP-MAC;
- **tcpdump**: kunasa pakiti ya mstari wa amri, inaweza kuchujwa na kusafirishwa nje;
- **Wireshark**: uchanganuzi wa pakiti za picha na usimbaji wa kina wa protocol;
- **ethtool**: uliza na urekebishe vigezo vya kimwili vya kadi ya Ethernet (kasi, duplex, WoL, nk).


#### Network Layer


Zana za kutathmini muunganisho wa IP, uelekezaji, na trafiki ya pakiti:


- **ping**: uwezo wa kufikiwa na kipimo cha kusubiri kwa kutumia ICMP;
- **njia ya ip**: kagua na urekebishe jedwali la uelekezaji ili kudhibiti njia za pakiti;
- **traceroute**: kitambulisho cha hop-by-hop cha vipanga njia kando ya njia ya kuelekea lengwa;
- **ss**: orodha ya kina ya soketi za TCP/UDP na michakato inayohusiana (mrithi wa netstat).


#### Tabaka za Usafiri na Maombi


Zana za utambuzi wa huduma na michakato:


- **nslookup / dig / jeshi **: Maswali ya DNS ili kuthibitisha azimio la jina na kuchambua rekodi;
- **nmap**: chunguza bandari zilizo wazi na huduma wazi ili kutathmini eneo la mashambulizi;
- **lsof**: orodhesha faili na socket zilizofunguliwa na michakato, mfumo wa kuunganisha na shughuli za mtandao.


Kujua zana hizi, kila moja ikilinganishwa na hatua mahususi ya muundo wa TCP/IP, huwezesha mbinu ya kimbinu: kuanzia Layer halisi, kusonga kupitia uelekezaji, na hadi huduma za programu. Msururu huu wa utaalamu huwapa wasimamizi uwezo wa kutambua, kulinda na kuboresha miundombinu yao, kuhakikisha utendakazi na upatikanaji wa mtandao.


# Sehemu ya mwisho


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Ukaguzi na Ukadiriaji


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Uchunguzi wa mwisho


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Hitimisho


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>
