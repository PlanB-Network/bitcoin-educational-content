---
name: Dana Wallet
description: Jalada la chini kabisa la Silent Payments (BIP-352)
---

![cover](assets/cover.webp)



Matumizi tena ya address za Bitcoin ni mojawapo ya vitisho vya moja kwa moja kwa usiri wa mtumiaji. Mpokeaji anaposhiriki address moja ili kupokea malipo mengi, mwangalizi yeyote anaweza kufuatilia miamala yote husika na kuunda upya historia yao ya fedha. Tatizo hili linaathiri hasa waundaji wa maudhui, wafadhili au wanaharakati wanaotaka kuonyesha hadharani address ya michango bila kuathiri faragha yao au ya wafadhili wao.



Dana Wallet hujibu tatizo hili kwa suluhisho la kifahari: Silent Payments. wallet hii isiyo na kiwango cha chini, ya chanzo huria, iliyozinduliwa mwaka wa 2024, inazalisha address tuli inayoweza kutumika tena huku ikihakikisha kwamba kila malipo yanayopokelewa yanaishia kwenye address tofauti kwenye blockchain. Mtumaji hahitaji mwingiliano wa awali na mpokeaji, na hakuna mwangalizi wa nje anayeweza kuunganisha shughuli za kibinafsi pamoja. Kwenye blockchain, malipo haya yanaonekana kama shughuli za kawaida kabisa za Taproot.



Dana Wallet inapatikana kwenye Mainnet na Signet, lakini wasanidi bado wanaiona kuwa ya majaribio na kupendekeza usiweke pesa ambazo hauko tayari kupoteza. Katika somo hili, tutatumia toleo la Saini kugundua Silent Payments bila kuhatarisha pesa zozote halisi.



## Dana Wallet ni nini?



### Falsafa na malengo



Dana Wallet inatumia mbinu ya "SP-first": wallet inazalisha address za Silent Payments pekee, na inakubali malipo ya aina hii pekee. Hutaweza kuunda address ya kawaida ya Bitcoin (legacy address, SegWit au kiwango cha Taproot) ukitumia programu hii. Kizuizi hiki cha kimakusudi hukuruhusu kuzingatia kikamilifu kujifunza BIP-352 protocol bila kukengeushwa na vipengele vingine. Kiolesura kisicho na vitu vingi kwa makusudi kinapendelea urahisi wa matumizi kuliko wingi wa chaguo, na kufanya zana kupatikana hata kwa watumiaji wapya kwa dhana za usiri za on-chain.



Mradi huu ni chanzo huria kabisa, umetengenezwa na Flutter kwa kiolesura cha simu na Rust kwa mantiki ya ndani ya cryptography. Usanifu huu unachanganya hali ya utendakazi ya mtumiaji na utendakazi bora zaidi kwa shughuli za utambazaji wa kina.



### Silent Payments hufanyaje kazi?



Silent Payments (BIP-352) yanatokana na utaratibu wa kisasa wa cryptography kwa kutumia Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Mpokeaji hutengeneza address tuli (kuanzia `sp1...` kwenye mainnet au `tsp1...` kwenye Saini) inayojumuisha funguo mbili tofauti za umma: ufunguo wa kuchanganua ($B_{scan}$) ili kugundua malipo yanayoingia, na ufunguo wa kutumia ($B_{spend}$) ili kutumia pesa zilizopokelewa. Utenganisho huu unawezesha kuweka ufunguo wa kutumia kwenye maunzi ya wallet huku ukitumia kitufe cha kutambaza kwenye kifaa kilichounganishwa.



Mtumaji anapotaka kufanya malipo, wallet yake huchanganya jumla ya funguo za faragha za ingizo lake na ufunguo wa uchanganuzi wa umma wa mpokeaji ili kukokotoa siri ya ECDH iliyoshirikiwa. Siri hii hutoa "tweak" ya cryptography ambayo, ikiongezwa kwa ufunguo wa matumizi wa mpokeaji, huunda address ya kipekee ya Taproot kwa muamala huu.



Mpokeaji anaweza kutoa tena hesabu hii kwa kutumia ufunguo wake wa kuchanganua faragha na vitufe vya umma vinavyoonekana katika shughuli ya ununuzi (Diffie-Hellman hisabati mali). Hii humwezesha kutambua na kutumia pesa bila mwingiliano wowote wa awali na mtumaji.



Mbinu hii inatoa faida kadhaa:




- **Usiri wa mpokeaji**: kila malipo huishia katika address tofauti
- **Usiri wa mtumaji**: hakuna kitambulisho endelevu kinachounganisha malipo
- **Hakuna server ya mtu wa tatu**: protocol inafanya kazi kwa uhuru
- **Miamala isiyooweza kutofautishwa**: Silent Payments zinaonekana kama miamala ya kawaida ya Taproot



Drawback kuu ni gharama ya skanning: mpokeaji anapaswa kuchambua kila muamala mpya wa Taproot ili kugundua wale waliokusudiwa kwake.



Iwapo ungependa kupata maelezo zaidi kuhusu utendakazi wa kiufundi wa Silent Payments, tunapendekeza kozi ya BTC204 kuhusu usiri katika Bitcoin, inayojumuisha sura inayohusu Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Mifumo inayotumika



Dana Wallet inapatikana kama programu ya Android. APK inaweza kupakuliwa kupitia hazina maalum ya F-Droid iliyotolewa na wasanidi programu, kupitia Obtainium, au moja kwa moja kutoka GitHub. Kwa watumiaji wa Linux, inawezekana kitaalam kuunda programu ya Flutter ya eneo-kazi.



Programu haipatikani kwenye iOS au kupitia maduka rasmi (Google Play, App Store), ikionyesha hali yake ya majaribio na umakini wake kwa hadhira ya kiufundi.



## Ufungaji



### Masharti muhimu



Ili kusakinisha Dana Wallet kwenye Android, utahitaji kifaa cha Android kilicho na chaguo la "Vyanzo Visivyojulikana" katika mipangilio ya usalama. Hakuna akaunti au usajili unaohitajika.



### Ongeza amana ya F-Cold



Njia inayopendekezwa ni kuongeza hazina ya Dana Wallet iliyojitolea ya F-Droid. Nenda kwenye `fdroid.silentpayments.dev` ambapo utapata kiungo cha hazina na msimbo wa QR wa kuchanganua. Hifadhi kwa sasa inatoa maombi 3: toleo la Mainnet, Maendeleo na Saini.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Ufungaji kupitia F-Droid



Fungua programu ya F-Droid kwenye kifaa chako cha Android, kisha ufikie Mipangilio kupitia ikoni iliyo chini kulia. Chagua "Hazina" ili kudhibiti vyanzo vya programu. Bonyeza kitufe cha "+" ili kuongeza hazina mpya, kisha uchanganua msimbo wa QR au ubandike kiungo cha `https://fdroid.silentpayments.dev/fdroid/repo`. Mara tu hazina imeongezwa, utaona matoleo matatu ya Dana Wallet yanapatikana. Chagua "Dana Wallet - Alamisho" na ubofye "Sakinisha".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Usanidi wa awali



### Uundaji wa kwingineko



Katika uzinduzi wa kwanza, Dana Wallet huonyesha skrini ya kukaribisha inayotambulisha dhamira yake: "Tuma na upokee michango bila watu wa kati". Bonyeza "Anza" ili kuendelea. Skrini inayofuata inawasilisha faida tatu muhimu za programu:




- **Michango isiyo na bidii**: anza kupokea michango kwa sekunde
- **Faragha kwa chaguomsingi**: hakuna haja ya server au miundombinu changamano
- **Uzoefu kama wa barua pepe**: tuma na upokee bitcoin kwa urahisi kama barua pepe



Unaweza kuchagua kati ya "Rejesha" ili kurejesha kwingineko iliyopo au "Unda mpya wallet" ili kuunda mpya. Bonyeza "Unda wallet mpya".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Programu kisha hutoa kifungu cha uokoaji, ambacho unapaswa kuandika kwa uangalifu kwenye nyenzo ya kimwili. Hata kwa pesa za majaribio zisizo na thamani halisi, tumia mbinu bora za kuhifadhi nakala.



### Interface na vigezo



Mara tu kwingineko imeundwa, unachukuliwa kwenye interface kuu, imegawanywa katika tabo mbili: "Transact" na "Settings".



Kichupo cha **Muamala** huonyesha salio lako la bitcoin (na ubadilishaji wake kuwa dola), orodha ya miamala ya hivi majuzi, na vitufe viwili vya kitendo: "Lipa" ili kutuma pesa, na kitufe cha kupokea (ikoni ya kupakua).



Kichupo cha **Mipangilio** hutoa chaguzi nne:




- **Onyesha kifungu cha maneno cha seed**: huonyesha maneno yako ya kurejesha akaunti kwa ajili ya uhifadhi
- **Badilisha sarafu ya fiat**: badilisha sarafu ya kuonyesha (USD kwa chaguo-msingi)
- **Weka url ya nyuma**: sanidi URL ya server ya Blindbit (tazama sehemu inayofuata)
- **Futa wallet**: inafuta kabisa wallet kutoka kwa kifaa



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Server ya Blindbit



Dana Wallet hutumia server ya kuorodhesha inayoitwa **Blindbit** ili kugundua Silent Payments. Kuelewa jinsi inavyofanya kazi ni muhimu kwa kutathmini muundo wa uaminifu wa programu.



**Kwa nini tunahitaji server?**



Ili kugundua Silent Payments, wallet yako lazima ichanganue kinadharia miamala yote ya Taproot katika kila block na kufanya hesabu ya cryptography (ECDH) kwa kila moja. Kwenye simu ya rununu, operesheni hii itakuwa ya kimahesabu sana na ya kutumia kipimo data.



Server ya Blindbit hutatua tatizo hili kwa kuhesabu awali data ya kati (inayoitwa "tweaks") kwa miamala yote ya Taproot. wallet yako kisha inapakua marekebisho haya (baiti 33 kwa kila ununuzi) na kufanya hesabu ya mwisho **ndani** ili kuangalia kama malipo ni yako.



**Siri iliyohifadhiwa**



Tofauti na server ya kawaida ya Electrum ambapo unafichua address zako, server ya Blindbit haijui ni malipo gani ni yako. Inatoa data sawa kwa watumiaji wote, na ni simu yako ambayo hufanya uthibitishaji wa mwisho. Kwa hivyo usiri wako unahifadhiwa kupitia server.



**Server chaguo-msingi**



Dana Wallet hutumia server ya umma `silentpayments.dev/blindbit/signet` (kwa Saini) au `silentpayments.dev/blindbit/mainnet` (kwa Mainnet). Unaweza kubadilisha URL hii katika mipangilio ikiwa unapangisha server yako mwenyewe.



**Pandisha server yako ya Blindbit**



Kwa watumiaji wanaotaka uhuru kamili, inawezekana kupangisha server yao ya Blindbit Oracle. Hii inahitaji:




- Full node ya Bitcoin **isiyo na tai** (isiyo ya pruned)
- Inasakinisha Blindbit Oracle (inapatikana kwenye GitHub: `setavenger/blindbit-oracle`)
- Takriban. 10 GB ya nafasi ya ziada ya disk
- Ujuzi wa kiufundi (Mkusanyiko wa Nenda, usanidi wa server)



Hakuna programu iliyopakiwa bado inayopatikana kwa Umbrel au Start9. Ufungaji kwa sasa unabaki kuwa wa mwongozo. Huu ni uga ulio katika mageuzi ya kila wakati, na suluhu zinazoweza kufikiwa zaidi zinaweza kujitokeza katika siku zijazo.



## Matumizi ya kila siku



### Kupokea fedha



Ili kupokea bitcoin, bonyeza kitufe cha kupokea (ikoni ya kupakua) kutoka kwa skrini kuu. Dana Wallet kisha inaonyesha address yako kamili ya Silent Payments katika umbizo `tsp1q...` kwenye Alamisho. Interface inatoa chaguzi kadhaa:




- **Onyesha msimbo wa QR**: huonyesha msimbo wa QR wa address yako kwa uchanganuzi kwa urahisi
- **Shiriki**: shiriki address kupitia programu za simu yako
- **Nakili**: address ya nakala kwenye ubao wa kunakili



Kama inavyoonyeshwa kwenye skrini, unaweza kushiriki address hii hadharani kwenye mitandao yako ya kijamii bila kuhatarisha faragha yako.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Ili kupata pesa zako za majaribio kwa mara ya kwanza kwenye Saini, tumia bomba maalum la Silent Payments yanayopatikana katika `silentpayments.dev/faucet/signet`. Nakili address yako `tsp1...`, ibandike katika sehemu iliyotolewa kwenye bomba, kisha uthibitishe ombi. Subiri block  ikue mined (kama dakika 10 kwenye Saini).



### Tuma malipo



Ili kutuma pesa, bonyeza kitufe cha "Lipa" kutoka skrini kuu. Skrini ya "Chagua wapokeaji" inaonekana ikiwa na chaguo tatu za kubainisha mpokeaji:




- Weka maelezo ya malipo wewe mwenyewe
- **andika kutoka ubao wa kunakili**: bandika address kutoka kwa ubao wa kunakili
- **Changanua Msimbo wa QR**: changanua msimbo wa QR ulio na address



Mara tu address ya mpokeaji imethibitishwa, skrini ya "Ingiza kiasi" hukuwezesha kuingiza kiasi kitakachotumwa kwa satoshi. Salio lako linalopatikana linaonyeshwa kwa marejeleo. Bonyeza "Nenda kwenye uteuzi wa ada" ili kuendelea.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Skrini inayofuata inaonyesha viwango vitatu vya malipo, kulingana na uharaka unaohitajika:




- **Haraka** (dakika 10-30): ada ya juu kwa uthibitisho wa haraka
- **Kawaida** (dakika 30-60): gharama za wastani
- **Polepole** (saa 1+): ada ya chini zaidi kwa miamala isiyo ya dharura



Baada ya kuchagua kiwango cha ada, "Tayari kutuma?" skrini ya uthibitishaji ni muhtasari wa maelezo yote: address lengwa, kiasi, muda uliokadiriwa na ada ya muamala. Angalia maelezo haya kwa uangalifu, kisha ubonyeze "Tuma" ili kutuma muamala.



Mara baada ya kutumwa, muamala huonekana kwenye historia yako na hali ya "Haijathibitishwa" hadi ijumuishwe kwenye kizuizi. Salio lako linasasishwa ipasavyo.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Faida na mapungufu



### Vivutio





- **Kialimu**: kiolesura kilichorahisishwa kinacholenga kujifunza Silent Payments
- **Bidirectional**: inasaidia kutuma na kupokea, tofauti na portfolios zingine
- **Chanzo-wazi**: nambari inayoweza kukaguliwa kikamilifu kwenye GitHub
- **Faucet** iliyowekwa wakfu: hurahisisha kupata ufadhili wa majaribio
- **Bila akaunti**: hakuna usajili au data ya kibinafsi inahitajika



### Vikwazo vya kuzingatia





- **Majaribio**: programu ambayo haijakaguliwa, tumia kwa tahadhari kwenye Mainnet
- **Mfumo mdogo**: hasa Android, hakuna toleo la iOS
- **Utendaji uliopunguzwa**: hakuna udhibiti wa sarafu, hakuna akaunti ndogo, hakuna Umeme
- **Uchanganuzi wa kina**: utambuzi wa malipo hutumia rasilimali muhimu



## Mbinu bora



### Usalama wa seed



Hata kwa majaribio ya Signet yenye asili zisizo na thamani, shughulikia maneno yako ya kurejesha akaunti kwa uzito. Tumia chaguo la "Onyesha maneno ya seed" katika mipangilio ili uandike kwa makini. Kama suala la mazoezi mazuri, dumisha wallets tofauti kabisa za Signet na Mainnet: usiwahi kutumia seed iliyoundwa kwa majaribio kwenye wallet inayokusudiwa kupokea pesa halisi.



### Onyo kuhusu hali ya majaribio



Dana Wallet bado inachukuliwa kuwa ya majaribio na watengenezaji wake. Kama wanavyosema wazi: "Usitumie pesa ambazo hauko tayari kupoteza". Kwa madhumuni ya kujifunza, chagua toleo la Saini. Ikiwa unatumia toleo la Mainnet, jizuie kwa kiasi cha token.



### Hifadhi nakala na urejeshaji



Urejeshaji wa hazina ya Silent Payments unahitaji wallet inayooana na BIP-352 protocol. Wallet ya kawaida haiwezi kuchanganua blockchain ili kutambua UTXO zako za Silent Payments. Weka Dana Wallet ikiwa bado imesakinishwa au tumia chaguo la Rejesha mwanzoni mwa uzinduzi ili kurejesha wallet iliyopo



## Kulinganisha na BIP-47 na PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Silent Payments huondoa shughuli ya arifa ya BIP-47 kwa gharama ya skanisho ghali zaidi. PayJoin hutatua tatizo tofauti (uwiano wa pembejeo) na inaweza kuunganishwa na Silent Payments.



## Hitimisho



Dana Wallet ni zana muhimu ya kielimu kwa kujifunza kuhusu Silent Payments katika mazingira yasiyo na hatari. Mbinu yake nyepesi hukuruhusu kuelewa taratibu za msingi za BIP-352 protocol bila kukengeushwa na vipengele visivyo vya lazima. Kwa kufanya majaribio kwenye Signet, utaimarisha uelewa wako wa vitendo kuhusu teknolojia hii yenye matumaini kwa usiri wa muamala wa Bitcoin.


Silent Payments zinawakilisha hatua muhimu ya kusonga mbele katika kupatanisha urahisi wa kutumia na kuheshimu faragha. Shauku ya jumuiya na miunganisho ya kwanza kwenye wallets mbalimbali (Cake Wallet, BitBox02, BlueWallet ya kutuma) inaelekeza kwenye siku zijazo ambapo kuchapisha address ya mchango hakutahatarisha tena faragha ya kifedha ya mmiliki wake.



## Rasilimali



### Nyaraka rasmi




- Dana Wallet GitHub hazina: https://github.com/cygnet3/danawallet
- Amana ya F-Cold: https://fdroid.silentpayments.dev
- Tovuti ya jumuiya ya Silent Payments: https://silentpayments.xyz
- Specification za BIP-352: https://bips.dev/352



### Zana za mtihani wa saini




- Silent Payments za Faucet: https://silentpayments.dev/faucet/signet
- Kichunguzi cha Saini ya Mempool: https://mempool.space/signet



### Server ya Blindbit (inayojipangisha yenyewe)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle
