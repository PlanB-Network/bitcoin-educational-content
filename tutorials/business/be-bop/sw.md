---
name: kuwa-BOP
description: Mwongozo wa vitendo wa kuchuma mapato kwa biashara yako na be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** ni jukwaa la biashara ya mtandaoni lililoundwa kwa ajili ya wajasiriamali wanaotaka kuuza mtandaoni na nje ya mtandao, kwa uhuru kamili, huku wakikubali malipo katika Bitcoin, kupitia akaunti ya benki na kwa Pesa. Suluhisho hilo pia ni muhimu kwa aina yoyote ya shirika linalotaka kukusanya michango au kuchuma mapato kwa shughuli zake mbalimbali.



Suluhisho ni rahisi, nyepesi na ya uhuru. Inawezesha kuundwa kwa duka la mtandaoni, hata katika mazingira ambapo huduma za kifedha za jadi ni chache au hazipo. Hakika, **be-BOP** imeundwa ili kufanya kazi kwa ufanisi ikiwa na au bila ufikiaji wa benki, kwa kutumia Bitcoin kama miundombinu ya malipo.



Katika somo hili, tutakuchukua hatua kwa hatua kupitia:





- Unda duka lako la kwanza mtandaoni ukitumia **be-BOP**
- Binafsisha onyesho lako na bidhaa zako
- Sanidi njia za malipo zinazopatikana
- Elewa mbinu bora za kuuza kwa ufanisi mtandaoni na **be-BOP**



Mafunzo haya hayahitaji ujuzi wa hali ya juu wa kiufundi. Inalenga wasanidi programu na pia mafundi, wafanyabiashara, vyama vya ushirika au wajasiriamali wanaotaka kuanza biashara ya kidijitali kwa njia huru na thabiti.



## Masharti ya kusakinisha be-BOP kwenye seva yako mwenyewe



Kabla ya kuanza kusakinisha be-BOP, hakikisha kuwa una miundombinu ifuatayo ya kiufundi. Elements hizi ni muhimu kwa jukwaa kufanya kazi ipasavyo:



### Hifadhi inayolingana na S3



be-BOP hutumia mfumo wa kuhifadhi kudhibiti faili (kama vile picha za bidhaa). Hii inahitaji ufikiaji wa huduma ya S3, kama vile:





- [MinIO](https://min.io/) iliyopangishwa yenyewe
- Amazon S3 (AWS)
- Hifadhi ya Kitu cha Scaleway



Utahitaji kusanidi ndoo na kutoa habari ifuatayo:





- S3_BUCKET**: jina la ndoo
- S3_ENDPOINT_URL**: kiungo cha kufikia huduma yako ya S3
- S3_KEY_ID** na S3_KEY_SECRET: misimbo yako ya ufikiaji
- S3_REGION**: eneo la huduma yako ya S3



### Hifadhidata ya MongoDB katika hali ya ReplicaSet



be-BOP hutumia MongoDB kuhifadhi, mtumiaji, bidhaa na data zingine.



Una chaguzi mbili:





- Sakinisha MongoDB ndani ya nchi na **Modi ya ReplicaSet imewezeshwa**
- Tumia huduma ya mtandaoni kama **MongoDB Atlas**



Utahitaji vigezo vifuatavyo:





- MONGODB_URL**: muunganisho wa hifadhidata Address
- MONGODB_DB**: jina la hifadhidata



## Mazingira ya Node.js



be-BOP inafanya kazi na Node.js. Hakikisha kuwa umewasha toleo la **Node.js** la 18 au toleo jipya zaidi na **Corepack** (inahitajika ili kudhibiti wasimamizi wa vifurushi kama vile pnpm). Amri ya kukimbia ni `corepack enable`



### Git LFS imewekwa



Rasilimali zingine (kama vile picha kubwa) zinasimamiwa kupitia Git LFS (Hifadhi Kubwa ya Faili). Hakikisha una Git LFS iliyosanikishwa kwenye mashine yako na amri ya `git lfs install`. Masharti haya yanapowekwa, uko tayari kuendelea hadi hatua inayofuata: kupakua na kusanidi be-BOP.



**Kumbuka:** Mwongozo wa kiufundi wa utumiaji wa programu unapatikana katika mafunzo tofauti.



## Kuunda akaunti ya Msimamizi Bora



Mara ya kwanza be-BOP inazinduliwa, akaunti ya **Msimamizi Mkuu** inaundwa. Akaunti hii ina uidhinishaji wote unaohitajika ili kudhibiti utendaji wa ofisi ya nyuma. Ili kuunda akaunti, fuata hatua hizi:





- Nenda kwa `yoursiteweb/admin/login`
- Unda akaunti ya msimamizi mkuu na kuingia salama na nenosiri



Akaunti hii itakupa ufikiaji wa utendakazi wote wa nyuma wa ofisi. Mara baada ya kuundwa, unaweza kuingia kwa kuingiza jina lako la mtumiaji na nenosiri.



![login](assets/fr/001.webp)



## Usanidi na usalama wa Ofisi ya Nyuma



Kabla ya kusanidi muunganisho wako wa Interface wa ofisi ya nyuma, unahitaji kuunda Hash ya kipekee. Hii hutoa ulinzi dhidi ya watendaji hasidi wanaojaribu kuiba kiungo cha muunganisho kwa msimamizi wako wa Interface.



Ili kuunda Hash, nenda kwa `/admin/Settings`. Katika sehemu iliyowekwa kwa usalama (k.m. "Admin Hash"), fafanua mfuatano wa kipekee (Hash). Baada ya kusajiliwa, URL ya ofisi ya nyuma itarekebishwa (k.m. `/admin-yourhash/login`) ili kudhibiti ufikiaji kwa watu ambao hawajaidhinishwa.



![hash-login](assets/fr/002.webp)



2.2. Washa hali ya matengenezo (ikiwa ni lazima)



Bado iko /admin/Settings, (Mipangilio> Jumla kupitia Interface) angalia chaguo la "wezesha hali ya matengenezo" chini ya ukurasa.



![maintenance-mode](assets/fr/003.webp)



Ikihitajika, unaweza kubainisha orodha ya anwani za IPv4 zilizoidhinishwa (zinazotenganishwa na koma) ili kuwezesha ufikiaji wa ofisi ya mbele wakati wa matengenezo. Ofisi ya nyuma inabaki kupatikana kwa wasimamizi.



![ip-bebop](assets/fr/004.webp)



## Mpangilio wa mawasiliano



Ili kuwezesha be-BOP kutuma arifa (k.m. kwa maagizo, usajili au ujumbe wa mfumo), unahitaji kusanidi angalau njia moja ya mawasiliano. Chaguzi mbili zinapatikana: barua pepe (SMTP) au Nostr.



### Usanidi wa SMTP (barua pepe)



be-BOP inaweza kutuma barua pepe kupitia seva ya SMTP. Utahitaji kitambulisho halali cha SMTP, ambacho mara nyingi hutolewa na huduma ya barua pepe (k.m. Mailgun, Gmail, n.k.).



Hapa ndio unahitaji kujua:



SMTP_HOST: Seva ya SMTP Address (k.m. smtp.mailgun.org)



SMTP_PORT: bandari ya kutumia (mara nyingi 587 au 465)



SMTP_USER: jina lako la mtumiaji (kwa kawaida barua pepe ya Address)



SMTP_PASSWORD: nenosiri lako au ufunguo wa API



SMTP_FROM: barua pepe ya Address ambayo itaonekana kama mtumaji




### Usanidi wa Nostr



be-BOP hukuwezesha kutuma arifa kupitia itifaki ya Nostr, miundombinu ya utumaji ujumbe iliyogatuliwa. Ili kufanya hivyo, unahitaji generate au Supply ufunguo wa kibinafsi wa Nostr (NSEC). Unaweza generate ufunguo huu moja kwa moja kupitia be-BOP's Interface, katika sehemu iliyowekwa kwa Nostr. Wakati Elements hizi zimesanidiwa ipasavyo, be-BOP itaweza kutuma ujumbe na arifa kiotomatiki kwa watumiaji wako.



## Mbinu za malipo zinazooana



be-BOP inaoana na suluhu kadhaa za malipo, zinazokuruhusu kuwapa wateja wako unyumbulifu zaidi. Hivi ndivyo unavyohitaji ili kusanidi njia ya malipo inayokufaa zaidi.



### Bitcoin Onchain



be-BOP inakuwezesha kukubali malipo ya Bitcoin moja kwa moja kwenye Blockchain (On-Chain), kwa urahisi na kwa usalama.



**Hatua za usanidi:**





- Nenda kwenye menyu ya **Mipangilio ya Malipo**
- Bofya kwenye **Bitcoin Nodeless** ili kufikia vigezo vya malipo vya On-Chain.
- Kamilisha nyanja zifuatazo:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Kidokezo:** Ili kupata ufunguo wako uliopanuliwa wa umma (Zpub), unaweza kuangalia mipangilio ya kina ya Bitcoin Wallet yako (Sparrow wallet, BlueWallet, Specter, n.k.). Hakikisha Wallet yako **sio ya kusoma pekee** ikiwa unakusudia kutumia historia ya muamala.



### Lightning Network



be-BOP pia inaweza kukubali malipo ya papo hapo ya Bitcoin kwa Lightning Network. Chaguzi mbili za usanidi zinapatikana kwa sasa:



**Phoenixd**



Nenda kwenye menyu ya `Mipangilio ya Malipo`, bofya `Phoenixd`



![phoenixd](assets/fr/006.webp)



Kisha utahitaji kuingiza **nenosiri au uthibitishaji wa token** unaokuunganisha kwenye mfano wako wa Phoenixd, mandharinyuma iliyotengenezwa na Acinq ambayo inakuruhusu kudhibiti malipo ya Lightning ukitumia nodi yako mwenyewe, lakini bila ugumu wa kudhibiti njia za malipo.



**Swiss Bitcoin Pay**



Iwapo hutaki kudhibiti eneo la Umeme mwenyewe, **Swiss Bitcoin Pay** ni suluhisho lililo tayari kutumia, na rahisi kusanidi ambalo linafaa kwa kuanza kukubali malipo ya Radi bila miundombinu changamano.



Hatua za usanidi:





- Katika menyu ya "Mipangilio ya Malipo", bofya `Swiss Bitcoin Pay`
- Ingia katika akaunti yako ya Uswizi ya Bitcoin Pay (au uunde ikiwa bado huna).
- Weka Ufunguo wa API unaotolewa na Swiss Bitcoin Pay, kisha ubofye "Hifadhi"



Baada ya kusanidiwa, be-BOP itaweka ankara za generate kiotomatiki kwa wateja wako, na utapokea malipo moja kwa moja kwenye akaunti yako ya Uswizi ya Bitcoin Pay. Suluhisho hili ni bora kwa watumiaji ambao wanataka kuepuka utata wa kiufundi wa nodi ya kibinafsi wakati wa kukubali malipo ya haraka, ya gharama nafuu.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Mbali na Bitcoin, be-BOP pia hukuruhusu kukubali malipo ya pesa taslimu kupitia PayPal, suluhisho la kimataifa linalojulikana na linalotumika sana.



Hatua za usanidi:





- Nenda kwenye menyu ya `Mipangilio ya Malipo`
- Bonyeza kwa `PayPal
- Katika akaunti yako ya Paypal (sehemu ya msanidi programu), weka `Kitambulisho cha Mteja` na `Siri`
- Chagua sarafu unayochagua (k.m. **USD**, **EUR**, **XOF**, n.k.)
- Bonyeza kwa `save



![paypal](assets/fr/008.webp)



**Kumbuka:** Lazima uwe na akaunti ya biashara ya PayPal kwa generate vitambulishi hivi. Unaweza kuzipata kupitia tovuti ya [msanidi programu] (https://developer.paypal.com)



### SumUp



Programu sasa inaunganisha suluhisho la malipo la **SumUp**, kukuwezesha kukubali malipo ya kadi ya mkopo kwa urahisi, usalama na kwa ufanisi. Ili kufaidika na utendakazi huu, usanidi wa awali unahitajika. Hapa kuna hatua za kufuata, zilizoorodheshwa kwa utekelezaji wazi na unaoendelea:





- Anza kwa kuweka **Ufunguo wako wa API**, ufunguo wa siri uliotolewa na SumUp ulipofungua akaunti yako ya msanidi programu. Inaanzisha muunganisho salama kati ya akaunti yako ya SumUp na programu.
- Jaza sehemu ya `Msimbo wa Biashara` kwa msimbo wa kipekee unaotambulisha biashara yako ndani ya jukwaa la SumUp. Nambari hii ni muhimu kwa kuhusisha miamala na biashara yako.
- Katika sehemu ya `Sarafu`, chagua sarafu kuu unayotumia kwa shughuli zako za ununuzi (k.m. **EUR**, **USD**, **CDF**, n.k.).
- Mara sehemu zote zimejazwa kwa usahihi, bofya kitufe cha `Hifadhi` ili kuhifadhi mipangilio yako. Kisha mfumo utaanzisha kiungo na akaunti yako ya SumUp, na programu yako itakuwa tayari kukubali malipo.



![payment-sumup](assets/fr/009.webp)



Baada ya usanidi huu, muunganisho wa **SumUp** utafanya kazi na utafanya kazi, kukuwezesha kutoa pesa haraka na kufuatilia miamala yako moja kwa moja kutoka kwa programu.



### Mstari



be-BOP pia inatoa ushirikiano kamili na **Stripe**, mojawapo ya mifumo maarufu ya malipo ya mtandaoni. Stripe hukuruhusu kukubali malipo ya mtandaoni kupitia kadi ya mkopo, Wallet ya dijiti na njia zingine kadhaa za malipo. Hivi ndivyo jinsi ya kuiwasha:





- Ingiza **kitufe cha siri** kilichotolewa kwenye dashibodi ya Stripe.
- Kamilisha sehemu ya **Ufunguo wa Umma**, inayotolewa pia na Stripe.
- Chagua **sarafu kuu**.
- Hifadhi usanidi, kisha ubofye `Hifadhi`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Tafadhali kumbuka:** Ni muhimu kujua utaratibu wa VAT unaotumika katika shughuli yako (k.m.: uuzaji chini ya VAT katika nchi ya muuzaji, msamaha chini ya uhalali, au uuzaji kwa kiwango cha VAT cha nchi aliko mnunuzi) ili kusanidi kwa usahihi chaguo za ankara katika **be-BOP**.



## Usanidi wa sarafu



**be-BOP** inatoa usimamizi wa hali ya juu wa sarafu na inatumika kwa mazingira ya sarafu nyingi na mahitaji mahususi ya uhasibu. Ili kuhakikisha uthabiti katika shughuli za kifedha na kuripoti, ni muhimu kusanidi ipasavyo sarafu tofauti zinazotumika katika mfumo. Hapa kuna hatua za kufuata kwa usanidi huu:





- Chagua **sarafu kuu** (`Fedha kuu`)
- Chagua `Fedha ya pili
- Bainisha **sarafu ya marejeleo** (`Fedha ya marejeleo ya bei`)
- Onyesha `Fedha ya Uhasibu



Baada ya sarafu zote kusanidiwa kwa usahihi, programu huhakikisha ubadilishaji wa moja kwa moja na sahihi wa shughuli za sarafu nyingi, huku ikidumisha uthabiti wa uhasibu.



![settings-currencies](assets/fr/011.webp)



## Usanidi wa ufikiaji wa uokoaji kupitia barua pepe au Nostr



Bado katika `/admin/settings`, kupitia **ARM** moduli, hakikisha kwamba akaunti ya msimamizi mkuu inajumuisha **barua pepe ya Address** au **baa ya kurejesha akaunti**, hivyo kuwezesha utaratibu ukisahau nenosiri lako.



![settings-users](assets/fr/012.webp)



## Mipangilio ya lugha



Programu hutoa uwezo wa lugha nyingi kukabiliana na hadhira ya kimataifa na kuboresha uzoefu wa mtumiaji. Ili kuamilisha utendakazi wa lugha nyingi, ni muhimu kusanidi lugha zinazopatikana na kufafanua **lugha chaguo-msingi**.



![settings-languages](assets/fr/13.webp)



## Interface na usanidi wa Kitambulisho katika be-BOP



**be-BOP** huwapa wabunifu zana zote wanazohitaji ili kuunda tovuti. Hatua ya kwanza ni kufungua sehemu ya `/Msimamizi > Bidhaa > Muundo` katika mipangilio. Anza kwa kusanidi **Upau wa Juu**, Upau wa Urambazaji** na **Nchi**.



### Le Juu Bar



Usanidi wa **Upau wa Juu** hukuwezesha kubinafsisha utambulisho unaoonekana wa programu yako kwa kuonyesha maelezo muhimu moja kwa moja kutoka mstari wa kwanza wa Interface. Hii huimarisha utambuzi wa chapa na hutoa muktadha wazi kwa watumiaji.



#### Hatua za usanidi:





- Katika sehemu ya `Jina la Biashara`, weka jina la kampuni, shirika au bidhaa yako. Jina hili litaonekana juu ya Interface na litawakilisha utambulisho wako mkuu wa kuona.
- Onyesha kichwa cha tovuti**: kichwa kilichochaguliwa kinapaswa kutoa muhtasari wa madhumuni ya jukwaa. Kichwa hiki kinaweza kuonekana kwenye kichwa au kwenye kichupo cha kivinjari.
- Ongeza maelezo ya Tovuti**: hapa ndipo unapoandika maelezo mafupi ya mpango wako. Maelezo haya husaidia kuweka zana kwa watumiaji muktadha na pia inaweza kutumika kwa madhumuni ya SEO.



Baada ya maelezo haya kuingizwa, **Upau wa Juu** utaonyesha uwasilishaji wazi, wa kitaalamu na thabiti wa suluhisho lako.



#### Viungo kwenye Upau wa Juu



Sehemu ya `Viungo` ya Upau wa Juu hukuruhusu kuongeza njia za mkato kwa kurasa muhimu katika programu yako au kwenye tovuti za nje. Viungo hivi vinaonyeshwa moja kwa moja kwenye Upau wa Juu, na kuwapa watumiaji wako ufikiaji wa haraka na uliopangwa.



#### Hatua za usanidi:





- Ingiza jina la kiungo (Nakala)**: katika sehemu ya `Maandishi`, weka jina au lebo ya kiungo jinsi itakavyoonekana (k.m. Nyumbani, Anwani, Usaidizi...).
- Onyesha kiungo Address (Url)**: katika sehemu ya `Url`, weka Address kamili ya ukurasa lengwa (wa ndani au nje).
- Ongeza viungo vingine ikihitajika**: kila mstari wa usanidi hukuruhusu kuongeza kiungo cha ziada kwa kutumia sehemu za `Maandishi` na `Url`.
- Hifadhi viungo**: viungo vyote vikishawekwa, bofya kitufe cha "Ongeza upau wa juu" ili kuvihifadhi.



Usanidi huu hukuruhusu kutoa urambazaji wazi, wa maji na unaoweza kufikiwa kupitia sehemu tofauti za tovuti yako au kwa nyenzo za ziada.



![settings-topbar](assets/fr/014.webp)



### Baa ya La Nav



Sehemu ya **Upau wa Urambazaji** hukuruhusu kusanidi menyu kuu ya usogezaji ya be-BOP, kwa kawaida iko kando au juu ya Interface. Menyu hii inawaongoza watumiaji kwa kurasa na utendaji mbalimbali wa programu. Usanidi wa kiungo ni rahisi na angavu. Hivi ndivyo inavyofanya kazi:





- Ingiza jina la kiungo (`Nakala`)**: kwenye mstari wa usanidi, anza kwa kujaza sehemu ya `Nakala`. Hii inalingana na jina la kiungo kinachoonyeshwa kwenye upau wa kusogeza (mifano: *Dashibodi*, *Watumiaji*, *Mipangilio*...).
- Ingiza kiungo Address (`Url`)**: karibu na sehemu ya `Nakala`, utapata sehemu ya `Url`. Katika uwanja huu, ingiza Address ya ukurasa ambao kiungo kinapaswa kuelekeza upya. Hii inaweza kuwa njia ya ndani au kiungo cha ukurasa wa nje.
- Ongeza viungo vingi ikihitajika**: chini ya mstari wa kwanza, sehemu mpya za `Maandishi` na `Url` zinapatikana kwa kuongeza viungo vingi inavyohitajika. Kila mstari unawakilisha kiungo cha ziada cha kusogeza.
- Hifadhi viungo**: mara tu unapoingiza Elements zote, bofya kitufe cha `Ongeza upau wa nav` ili kuhifadhi na kuonyesha matokeo katika upau wa kusogeza.



Usanidi huu unaruhusu uundaji mzuri wa ufikiaji wa sehemu tofauti za programu, kuboresha ergonomics na uzoefu wa mtumiaji.



![navbar](assets/fr/015.webp)



### Kijachini



Sehemu ya **Chini** hukuwezesha kubinafsisha sehemu ya chini ya ukurasa wa programu yako, na kuongeza maelezo au viungo muhimu. Kabla ya kusanidi viungo, anza kwa kuwezesha chaguo maalum:





- Washa onyesho la lebo ya "Powered by be-BOP "**: washa kitufe cha `Onyesha Inaendeshwa na be-BOP` ili kuonyesha lebo hii kwenye kijachini.
- Ingiza jina la kiungo (`Nakala`)**: jaza sehemu ya `Nakala`, ambayo inalingana na maneno ya kiungo kwenye kijachini (mifano: *Masharti*, *Faragha*, *Mawasiliano*...).
- Onyesha kiungo Address (`Url`)**: katika sehemu ya `Url`, weka Address ya ukurasa unaolengwa (wa ndani au wa nje).
- Ongeza viungo zaidi ikihitajika**: tumia mistari ya ziada kuunda viungo vingi unavyopenda.
- Hifadhi viungo**: bofya kitufe cha "Ongeza kiungo cha chini" ili kuhifadhi viungo.



![footer](assets/fr/016.webp)



### Ubinafsishaji unaoonekana



**⚠️ Usisahau kuweka nembo za mandhari mepesi na meusi, pamoja na aikoni, kupitia** `Msimamizi > Bidhaa > Picha`.



Hivi ndivyo jinsi ya kubinafsisha mwonekano na mwonekano wa tovuti yako:



#### Nenda kwenye sehemu ya Picha



Menyu `Msimamizi` > `Merch` > `Picha`.



#### Ongeza picha mpya



Bofya kwenye `Picha Mpya`.



#### Chagua faili ya ndani



Bofya kwenye `Chagua Faili`, kisha uchague picha kutoka kwenye diski yako ya Hard.



#### Chagua faili ya kuleta



Bofya mara mbili kwenye picha itakayoletwa (nembo nyepesi, nembo ya giza au favicon).



#### Kutaja picha



Jaza sehemu ya `Jina la picha`.



#### Ongeza picha



Bofya `Ongeza` ili kukamilisha uletaji.



![pictures](assets/fr/017.webp)



### Mpangilio wa Kitambulisho cha Muuzaji



#### Mipangilio ya utambulisho



Inapatikana kupitia `Msimamizi > Kitambulisho` (au `Mipangilio > Kitambulisho`), sehemu hii hukuruhusu kusanidi maelezo ya usimamizi na kisheria ya kampuni yako.



#### Taarifa za kisheria





- Jina la biashara**: jina rasmi la kampuni.
- Kitambulisho cha biashara**: kitambulisho halali au nambari ya usajili (RCCM, SIRET...).



#### Biashara Address





- Mtaa**: posta Address (mitaani, nambari...).
- Nchi**: nchi.
- Jimbo**: mkoa au mkoa.
- Mji**: mji.
- Msimbo wa eneo**: msimbo wa posta.



#### Maelezo ya mawasiliano





- Barua pepe**: barua pepe ya kitaalamu Address.
- Simu**: nambari ya simu ya kampuni.



#### Akaunti ya benki





- Jina la mwenye akaunti**: jina la mwenye akaunti.
- Mmiliki wa akaunti Address**: Address ya mmiliki.
- IBAN**: Nambari ya Akaunti ya Benki ya Kimataifa.
- BIC**: Msimbo wa SWIFT/BIC.



![bank-account](assets/fr/019.webp)



#### Bili





- Bofya kwenye `Jaza na taarifa kuu za duka` ili kujaza data mapema.
- Taarifa ya mtoaji aliye juu sana**: sehemu ya maelezo ya kisheria/kodi inayoonekana kwenye ankara.
- Bofya `Sasisha` ili kuhifadhi mabadiliko.



**Kumbuka:** unaweza pia kuingiza maelezo ya ziada yatakayoonyeshwa kwenye Invoice, kulingana na mahitaji yako.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Duka la kimwili Address



Kwa wale walio na duka halisi, ongeza Address mahususi kamili katika `Msimamizi > Mipangilio > Utambulisho` au sehemu maalum. Hii itaiwezesha kuonyeshwa kwenye hati rasmi na katika sehemu ya chini ikiwa ni lazima.



![seller-id](assets/fr/021.webp)



## Usimamizi wa Bidhaa



### Kutengeneza bidhaa mpya



Nenda kwa `Msimamizi > Bidhaa > Bidhaa` ili kuongeza au kurekebisha bidhaa. Jaza sehemu zifuatazo:



#### Taarifa za msingi





- Jina la Bidhaa**: jina la bidhaa (k.m. *BOP T-shirt edition limited*).
- Slug**: Kitambulisho cha URL bila nafasi (k.m. `tshirt-bop-edition-limitee`).
- Lakabu** *(si lazima)*: ni muhimu kwa kuongeza haraka kwa kikapu kupitia sehemu maalum.



![product-config](assets/fr/028.webp)



#### Kuweka bei





- Bei Kiasi**: bei ya bidhaa (k.m. `25.00`).
- Sarafu ya Bei**: sarafu (EUR, USD, BTC, n.k.).
- Bidhaa maalum**:
  - hii ni bidhaa ya bure.
  - hii ni bidhaa ya kulipa-unachotaka.



#### Chaguzi za bidhaa





- Bidhaa moja (`iliyojitegemea`)**: nyongeza moja tu inawezekana kwa kila agizo (k.m. mchango, tikiti ya kuingia).
- Bidhaa zenye tofauti**:
  - Usiangalie `Inayojitegemea`.
  - Angalia `Bidhaa ina tofauti nyepesi (hakuna tofauti ya hisa)`.
  - Ongeza:
    - Jina** (k.m. *Ukubwa*),
    - Thamani** (k.m.: S, M, L, XL),
    - Tofauti za bei** ikitumika (k.m.: `+2 USD` kwa XL).



![product-details](assets/fr/029.webp)



## Usimamizi wa hisa



### Chaguo za kina wakati wa kuunda bidhaa (Hifadhi, Uwasilishaji, Tikiti, n.k.)



#### Bidhaa yenye hisa chache



Ikiwa bidhaa yako haipatikani kwa idadi isiyo na kikomo, angalia `Bidhaa ina hisa chache`. Hii huwasha ufuatiliaji wa kiotomatiki wa idadi iliyobaki. Pindi kisanduku hiki kikishawekwa alama, sehemu inaonekana kuonyesha **hisa inayopatikana**.



Mfumo unasimamia:





- Hifadhi iliyohifadhiwa** → bidhaa kwenye vikapu bado hazijalipwa
- Hisa inauzwa** → bidhaa ambazo tayari zimenunuliwa



**Muda wa kuhifadhi kikapu**: Mteja anapoongeza bidhaa kwenye kikapu chake, "imehifadhiwa" kwa muda mfupi. Unaweza kurekebisha wakati huu katika: `Msimamizi > Sanidi > Uhifadhi wa rukwama` (thamani katika dakika)



#### Bidhaa itawasilishwa?



Angalia `Bidhaa ina kipengele halisi ambacho kitasafirishwa kwa Address` ya mteja. Hii ni muhimu kwa bidhaa zote kutumwa kimwili (vitabu, t-shirt, nk.)



#### Chaguzi zingine





- Tikiti**: weka tiki ikiwa bidhaa ni tikiti ya tukio
- Kuhifadhi**: angalia ikiwa hii ni nafasi ya kuhifadhi (k.m.: kipindi, miadi)



![product-options](assets/fr/030.webp)



### Mipangilio ya Kitendo (chini)



Sehemu hii huamua **wapi** na **jinsi** bidhaa inaweza kutazamwa na kununuliwa:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Angalia tu vituo unavyotaka kutumia.



## Uundaji na ubinafsishaji wa kurasa na wijeti za CMS



### Kurasa za lazima za CMS



Nenda kwa `Msimamizi > Bidhaa > CMS`. Utaona orodha ya kurasa zilizopo na unaweza kuongeza mpya kwa **Ongeza ukurasa wa CMS**.



Kurasa za CMS ni muhimu kwa:





- Wajulishe wageni wako (k.m. masharti ya matumizi)
- Zingatia sheria (k.m. sera ya faragha)
- Eleza vipengele fulani vya duka (k.m. ukusanyaji wa IP, 0% ya VAT)



Unaweza kuongeza kurasa zingine kama inavyohitajika:





- Kuhusu sisi / Sisi ni nani
- Tusaidie / Michango
- Maswali Yanayoulizwa Mara kwa Mara
- Wasiliana
- nk.



**Kidokezo: Bofya kwenye kila kiungo au ikoni ili kurekebisha **maudhui**, **kichwa**, au **mwonekano wa seo** wa kila ukurasa.



### Mpangilio na mchoro wa Elements



Nenda kwa: `Msimamizi > Bidhaa > Muundo`. Unaweza kubinafsisha taswira ya Elements ya tovuti yako:



![product-options](assets/fr/032.webp)



#### Upau wa Juu





- Rekebisha au ufute viungo (EX: NYUMBANI, KUHUSU SISI,...)
- Urambazaji kati ya sehemu muhimu za tovuti



#### Navbar (upau kuu wa kusogeza)





- Wasilisha katika eneo la kijivu chini ya bar ya juu
- Ina ufikiaji wa haraka wa: `Config`, `Mipangilio ya Malipo`, `Muamala`, `Udhibiti wa Njia`, `Wijeti`, n.k.
- Wakurugenzi pekee



#### Kijachini





- Inaweza kuhaririwa kutoka kwa `Msimamizi > Bidhaa > Mpangilio`
- Ina: maelezo ya mawasiliano, viungo muhimu, arifa za kisheria..



#### Customize taswira



Nenda kwa: `Msimamizi > Bidhaa > Picha`



Unaweza:





- Badilisha **nembo kuu**
- Rekebisha au ongeza mpangilio **picha**



#### Maelezo ya tovuti



Pia inaweza kubadilishwa katika `Picha`, hukuruhusu kuonyesha **muhtasari au kauli mbiu** katika kichwa au kijachini, kulingana na mandhari.



**Kumbuka:** hii hukuruhusu kurekebisha mwonekano kwa utambulisho wa chapa yako (kielimu, kibiashara au jumuiya).



### Kuunganisha wijeti kwenye kurasa za CMS



Wijeti** huboresha kurasa zako za CMS kwa kutumia Elements inayobadilika au inayoonekana.



#### Uundaji wa Wijeti



Nenda kwa: `Msimamizi > Wijeti`



Mifano ya wijeti zinazopatikana:





- Changamoto**: changamoto au misheni
- Lebo**: kategoria au maneno muhimu
- Vitelezi**: majukwaa ya picha
- Specifications**: Specifications tables
- Fomu**: fomu (mawasiliano, maoni, n.k.)
- Muda uliosalia**: vipima muda
- Matunzio**: matunzio ya picha
- Ubao wa wanaoongoza**: viwango vya watumiaji



![widgets](assets/fr/033.webp)



#### Ujumuishaji katika kurasa za CMS



Tumia **njia fupi** katika maudhui ya kurasa zako za CMS:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Vigezo vya sasa**:





- `slug`: kitambulisho cha wijeti ya kipekee
- `onyesha=img-1`: picha mahususi ya bidhaa
- `upana`, `urefu`, `fit`: vipimo na mtindo wa picha
- kucheza kiotomatiki=3000`: muda katika ms kati ya slaidi mbili



**Faida**:





- Rahisi kuingiza (nakili na ubandike)
- Nguvu: marekebisho yoyote kwenye wijeti yanaonyeshwa kiotomatiki
- Hakuna msanidi anayehitajika



## Usimamizi wa agizo na kuripoti



### Ufuatiliaji wa agizo



Ili kuona na kudhibiti maagizo ya awali, nenda kwa: `Msimamizi > Muamala > Maagizo`



Hapa utapata **orodha kamili ya maagizo ** iliyowekwa kwenye tovuti yako.



![orders](assets/fr/034.webp)



#### Taswira na utafutaji



Interface hukuruhusu kutafuta na kuchuja maagizo kulingana na vigezo kadhaa:





- Nambari ya agizo: nambari ya agizo
- lakabu ya bidhaa: kitambulisho cha bidhaa au jina
- Maana ya malipo": njia ya malipo iliyotumiwa (kadi, crypto, n.k.)
- `Barua pepe`: barua pepe ya mteja



Vichujio hivi hurahisisha utafutaji wa haraka na usimamizi unaolengwa.



#### Maelezo ya kila agizo



Kwa kubofya agizo, unaweza kufikia faili kamili iliyo na:





- Bidhaa zilizoagizwa
- Taarifa za mteja
- Uwasilishaji wa Address (ikiwa inatumika)
- Vidokezo vyovyote vinavyohusiana na agizo



#### Vitendo vinavyowezekana kwa agizo



Unaweza:





- Thibitisha agizo (ikiwa linasubiri)
- Ghairi agizo (ikitokea tatizo au ombi la mteja)
- Ongeza **lebo** (za shirika la ndani)
- Ongea / ongeza **maelezo ya ndani**



**Kumbuka:** sehemu hii ni muhimu kwa ugavi mzuri na mahusiano ya wateja.



### Kuripoti na kuuza nje



Ili kufikia takwimu za mauzo na malipo:


msimamizi > Mipangilio > Kuripoti



![reporting](assets/fr/035.webp)



Hapa utapata muhtasari wa biashara yako, kwa njia ya **ripoti za kila mwezi na za mwaka**.



#### Ripoti maudhui



Ripoti zimegawanywa katika sehemu:





- Maelezo ya Agizo**: idadi ya maagizo, hali (imethibitishwa, imeghairiwa, inasubiri), mageuzi
- Maelezo ya Bidhaa**: bidhaa zinazouzwa, kiasi, bidhaa maarufu
- Maelezo ya Malipo**: kiasi kilichokusanywa, uchanganuzi kwa njia ya malipo



#### Usafirishaji wa data



Kila sehemu inajumuisha kitufe cha **Hamisha CSV**, kinachokuruhusu:





- Pakua data katika umbizo la CSV
- Zifungue katika Excel, Majedwali ya Google, n.k.
- Kuhifadhi kumbukumbu kwa matumizi ya usimamizi au uhasibu
- Zitumie kwa ripoti za ndani



**Kumbuka:** bora kwa ufuatiliaji wa utendaji, uhasibu na mawasilisho.



## Usanidi wa Nostr Messaging (si lazima)



![nostr-config](assets/fr/036.webp)



Jukwaa linaauni itifaki ya **Nostr** kwa utendakazi fulani wa hali ya juu:





- Arifa za ugatuzi
- Ingia bila nenosiri
- Utawala wa mwanga wa Interface



### Inazalisha na kuongeza kitufe cha kibinafsi cha Nostr



Nenda kwa:


admin > Usimamizi wa Njia > Nostr





- Bofya kwenye **Unda nsec** ikiwa huna.
- Mfumo unaweza generate moja kwa moja.
- Vinginevyo, unaweza kutumia ufunguo uliopo (k.m. kutoka Damus au Amethisto).



Inayofuata:





- Nakili kitufe cha `nsec`
- Iongeze kwenye faili yako ya `.env.local` (au `.env`): ``` env NOSTR_PRIVATE_KEY=YourNsecIciKey



### Vipengele vilivyoamilishwa na Nostr



Baada ya kusanidiwa, vitendaji kadhaa vinapatikana:



**Arifa kupitia Nostr**





- Tuma arifa kwa maagizo, malipo au matukio ya mfumo
- Kwa wasimamizi au watumiaji



**Utawala wa mwanga wa Interface**





- Inapatikana kupitia mteja wa Nostr
- Huwasha usimamizi wa haraka, unaotumia simu ya mkononi



**Muunganisho bila nenosiri**





- Ingia kwa kiungo salama (kutumwa kupitia Nostr)
- Usalama mkubwa wa mtumiaji na unyevu



## Ubunifu na ubinafsishaji wa mada



Ili kurekebisha mwonekano wa duka lako kwa hati yako ya picha, nenda kwa: `Msimamizi > Bidhaa > Mandhari`



Hapa utapata chaguo zote za **kuunda** na **kusanidi** mandhari maalum.



### Kuunda mandhari



![theme](assets/fr/037.webp)



Wakati wa kuunda au kurekebisha mada, unaweza kufafanua:





- Rangi**: kwa vitufe, mandharinyuma, maandishi, viungo, n.k.
- Fonti**: chaguo la aina za maandishi kwa mada, aya, menyu
- Mitindo ya picha**: mipaka, kando, nafasi, maumbo ya kuzuia



### Sehemu zinazoweza kubinafsishwa



Kila sehemu ya tovuti inaweza kubadilishwa kwa kujitegemea:





- Kichwa**: upau wa kusogeza wa juu
- Mwili**: maudhui kuu
- Kijachini**: chini ya ukurasa



**Kumbuka:** uzito huu unahakikisha uwiano kati ya taswira za tovuti na utambulisho wa chapa yako.



### Uwezeshaji wa mandhari



Mara tu mada imesanidiwa:





- Bonyeza kwa **Hifadhi **
- Iwashe kama **mandhari kuu** ya duka



**Kumbuka:** mandhari amilifu ndiyo yatakayoonekana kwa wageni.



## Inasanidi violezo vya barua pepe



Mfumo hukuruhusu kubinafsisha barua pepe zinazotumwa kwa watumiaji kiotomatiki. Nenda kwa: `Msimamizi > Mipangilio > Violezo`



![emails-templates](assets/fr/038.webp)



### Kuunda / kuhariri violezo



Kila barua pepe (uthibitisho wa agizo, nenosiri lililosahaulika, n.k.) ina:





- Mada**: mada ya barua pepe (k.m. "Agizo lako limeidhinishwa")
- Mwili wa HTML**: Maudhui ya HTML yanaonyeshwa kwenye barua pepe



**Kumbuka:** unaweza kuingiza maandishi, picha, viungo, n.k., inavyohitajika.



### Kutumia vigezo vinavyobadilika



Ili kufanya barua pepe ziwe na nguvu, weka vigeu kama vile:





- `{orderNumber}}`: nafasi yake kuchukuliwa na nambari halisi ya agizo
- `{invoiceLink}}`: kiungo cha Invoice
- `{websiteLink}}`: URL ya tovuti yako



**Kumbuka:** lebo hizi hubadilishwa kiotomatiki zinapotumwa.



### Vidokezo vya juu





- Unda barua pepe ambazo **jibu** kwa usomaji rahisi kwenye vifaa vya mkononi
- Ongeza **vifungo vya kitendo** (lipa, pakua, fuatilia agizo)
- Jaribu barua pepe zako kwa kujitumia kabla ya kuchapishwa



## Inasanidi lebo maalum na wijeti



### Usimamizi wa lebo



Lebo zinaweza kutumika kutengeneza na kuboresha maudhui yako. Ili kuzifikia: `Msimamizi > Wijeti > Tag`



![tags-config](assets/fr/039.webp)



### Kuunda lebo



Kamilisha nyanja zifuatazo:





- Jina la lebo**: jina la lebo limeonyeshwa
- Slug**: kitambulisho cha kipekee (hakuna nafasi au lafudhi)
- Tag Familia**: vikundi vya lebo kwa kategoria



![targsconfig](assets/fr/040.webp)



#### Familia zinazopatikana:





- waumbaji`: waandishi au watayarishaji
- wauzaji reja reja: wauzaji au sehemu za mauzo
- `Muda`: vipindi au tarehe
- matukio: matukio yanayohusiana



### Sehemu za hiari



Sehemu hizi zinaweza kutumika kuimarisha lebo kana kwamba ni ukurasa wa maudhui:





- Kichwa
- Manukuu
- Maudhui mafupi**
- Maudhui kamili** (kwa Kifaransa)
- CTA** (vifungo vya kitendo)



### Kwa kutumia vitambulisho



Lebo zinaweza kuwa:





- Imetengwa kwa bidhaa
- Imeunganishwa kwenye kurasa za CMS zenye lebo: [Tag=slug?display=var-1]



## Usanidi wa faili zinazoweza kupakuliwa



Ili kutoa hati zinazoweza kupakuliwa kwa wateja wako: `Msimamizi > Bidhaa > Faili`



### Inaongeza faili



1. Bofya kwenye **Faili mpya**


2. Taarifa:




   - Jina la faili** (k.m. *Mwongozo wa usakinishaji*)
   - Faili ya kupakia** (PDF, picha, Neno...)



**Kumbuka:** ikiongezwa, jukwaa hutengeneza kiotomatiki **kiungo cha kudumu**.



### Kwa kutumia kiungo



Kiungo hiki kinaweza kuingizwa kwenye:





- Ukurasa wa CMS** (kama kiungo cha maandishi au kitufe)
- **mteja wa barua pepe** (kupitia kiolezo)
- **Jedwali la bidhaa** (k.m. upakuaji mwenyewe)



Ni bora kwa kutoa *miongozo ya mtumiaji, miongozo ya kiufundi, laha za bidhaa...* bila hitaji la upangishaji wa nje.



## Nostr-bot



Jukwaa linatoa muunganisho wa hali ya juu na itifaki ya **Nostr**, kupitia roboti otomatiki.



Nenda kwa: Usimamizi wa nodi> Nostr



### Sifa kuu



#### Usimamizi wa relay





- Ongeza au ondoa **relay** zinazotumiwa na roboti
- Boresha **kufikia** na **kutegemewa** kwa ujumbe uliotumwa



#### Ujumbe otomatiki wa utangulizi





- Washa ujumbe otomatiki kwenye **maingiliano ya mtumiaji wa kwanza**
- Inafaa kwa:
  - Kuwasilisha huduma yako
  - Tuma kiungo muhimu (k.m. Maswali Yanayoulizwa Mara kwa Mara, mawasiliano, agizo)



#### Uthibitishaji wa `npub yako





- Ongeza **nembo** na **jina la umma**
- Unganisha kwa **kikoa cha wavuti kilichothibitishwa**
- Huboresha uaminifu na utambuzi wa utambulisho wako wa Nostr



### Kesi za utumiaji wa Nostr-bot





- Inakutumia **uthibitisho wa agizo** kwako
- Jibu la kiotomatiki kwa **matukio (k.m. mpangilio mpya)**
- Kuunda **maingiliano ya wateja yaliyogatuliwa**



## Inapakia sana lebo za tafsiri



be-BOP ni ya lugha nyingi (FR, EN, ES...), lakini unaweza kurekebisha tafsiri kulingana na mahitaji yako.



Ili kufanya hivyo, nenda kwa: `Mipangilio > Lugha`



### Inapakia na kuhariri



Faili za tafsiri ziko katika JSON. Unaweza:





- Pakua ** faili za lugha
- Rekebisha** maandishi yaliyopo
- Ongeza** tafsiri zako mwenyewe



Unganisha kwa faili asili:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Mfano:** badilisha `Ongeza kwenye rukwama` kwa `Ajouter au panier` au `Acheter`.



## Kazi ya Pamoja na Sehemu ya Uuzaji (POS)



### Usimamizi wa haki za mtumiaji na ufikiaji



#### Kuunda majukumu



Nenda kwa: `Msimamizi > Mipangilio > ARM`



Bofya **Unda jukumu** ili kuunda jukumu (k.m. `Msimamizi Mkuu`, `POS`, `Kikagua tikiti`).



Kila jukumu lina:





- andika ufikiaji**: ufikiaji wa kuandika
- ufikiaji wa kusoma**: ufikiaji wa kusoma
- ufikiaji uliokatazwa**: sehemu interdites



#### Uundaji wa mtumiaji



Katika menyu ile ile `Msimamizi > Mipangilio > ARM`, ongeza mtumiaji na:





- kuingia
- pak
- urejeshaji wa barua pepe
- (si lazima) `recovery npub` kwa muunganisho kupitia Nostr



Weka jukumu lililobainishwa hapo awali.



![pos-users](assets/fr/045.webp)



Watumiaji wa kusoma tu** wataona menyu katika *italiki* na hawataweza kurekebisha maudhui.



## Usanidi wa Sehemu ya Uuzaji (POS).



### Kukabidhi jukumu la POS



Ili kumpa mtumiaji idhini ya kufikia POS, weka jukumu la `Hatua ya Uuzaji (POS)` katika: `Msimamizi > Config > ARM`



Anaweza kuunganisha kupitia URL salama: `/pos` au `/pos/touch`



### Vipengele maalum vya POS



Be-BOP inatoa Interface iliyojitolea kwa mauzo ya kimwili (duka, tukio, nk.).



#### Kuongeza haraka kupitia lakabu



Katika `/gari`, uga hukuruhusu kuongeza bidhaa:





- Kwa kuchanganua **msimbo upau** (ISBN, EAN13)
- Kwa kuweka ** lakabu ya bidhaa** wewe mwenyewe



**Kumbuka:** bidhaa huongezwa kiotomatiki kwenye kikapu.



#### Njia za malipo



POS inasaidia:





- Aina
- Kadi ya mkopo
- Lightning Network (crypto)
- Wengine kulingana na usanidi



Chaguzi mbili za hali ya juu zinapatikana:





- Msamaha wa VAT**: unatumika kwa uhalalishaji (NGOs, wageni...)
- Punguzo la zawadi**: punguzo la kipekee kwa maoni ya lazima



#### Onyesho la upande wa mteja



URL `/pos/session` imekusudiwa kwa **skrini ya pili** (HDMI, kompyuta kibao...):



Bango:





- Bidhaa zinaendelea
- Jumla ya kiasi
- Njia ya malipo
- Punguzo limetumika



**Kumbuka:** mteja hufuata agizo moja kwa moja, huku muuzaji akilirekodi kwenye `/pos`.



### Muhtasari wa POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Asante kwa kufuatilia mafunzo haya kwa makini.