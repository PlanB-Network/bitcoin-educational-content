---
name: Dana Wallet
description: Jalada la chini kabisa la Malipo ya Kimya (BIP-352)
---

![cover](assets/cover.webp)



Matumizi tena ya anwani za Bitcoin ni mojawapo ya vitisho vya moja kwa moja kwa usiri wa mtumiaji. Mpokeaji anaposhiriki anwani moja ili kupokea malipo mengi, mwangalizi yeyote anaweza kufuatilia miamala yote husika na kuunda upya historia yao ya fedha. Tatizo hili linaathiri hasa waundaji wa maudhui, wafadhili au wanaharakati wanaotaka kuonyesha hadharani anwani ya michango bila kuathiri faragha yao au ya wafadhili wao.



Dana Wallet hujibu tatizo hili kwa suluhisho la kifahari: Malipo ya Kimya. wallet hii isiyo na kiwango cha chini, ya chanzo huria, iliyozinduliwa mwaka wa 2024, inazalisha anwani tuli inayoweza kutumika tena huku ikihakikisha kwamba kila malipo yanayopokelewa yanaishia kwenye anwani tofauti kwenye blockchain. Mtumaji hahitaji mwingiliano wa awali na mpokeaji, na hakuna mwangalizi wa nje anayeweza kuunganisha shughuli za kibinafsi pamoja. Kwenye blockchain, malipo haya yanaonekana kama shughuli za kawaida kabisa za Taproot.



Dana Wallet inapatikana kwenye Mainnet na Signet, lakini wasanidi bado wanaiona kuwa ya majaribio na kupendekeza usiweke pesa ambazo hauko tayari kupoteza. Katika somo hili, tutatumia toleo la Saini kugundua Malipo ya Kimya bila kuhatarisha pesa zozote halisi.



## Dana Wallet ni nini?



### Falsafa na malengo



Dana Wallet inatumia mbinu ya "SP-kwanza": wallet inazalisha anwani za Malipo ya Kimya pekee, na inakubali malipo ya aina hii pekee. Hutaweza kuunda anwani ya kawaida ya Bitcoin (zamani, SegWit au kiwango cha Taproot) ukitumia programu hii. Kizuizi hiki cha kimakusudi hukuruhusu kuzingatia kikamilifu kujifunza itifaki ya BIP-352 bila kukengeushwa na vipengele vingine. Kiolesura kisicho na vitu vingi kwa makusudi kinapendelea urahisi wa matumizi kuliko wingi wa chaguo, na kufanya zana kupatikana hata kwa watumiaji wapya kwa dhana za usiri za on-chain.



Mradi huu ni chanzo huria kabisa, umetengenezwa na Flutter kwa kiolesura cha simu na Rust kwa mantiki ya ndani ya kriptografia. Usanifu huu unachanganya hali ya utendakazi ya mtumiaji na utendakazi bora zaidi kwa shughuli za utambazaji wa kina.



### Malipo ya Kimya hufanyaje kazi?



Malipo ya Kimya (BIP-352) yanatokana na utaratibu wa kisasa wa kriptografia kwa kutumia Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Mpokeaji hutengeneza anwani tuli (kuanzia `sp1...` kwenye mainnet au `tsp1...` kwenye Saini) inayojumuisha funguo mbili tofauti za umma: ufunguo wa kuchanganua ($B_{scan}$) ili kugundua malipo yanayoingia, na ufunguo wa kutumia ($B_{spend}$) ili kutumia pesa zilizopokelewa. Utenganisho huu unawezesha kuweka ufunguo wa kutumia kwenye maunzi ya wallet huku ukitumia kitufe cha kutambaza kwenye kifaa kilichounganishwa.



Mtumaji anapotaka kufanya malipo, wallet yake huchanganya jumla ya funguo za faragha za ingizo lake na ufunguo wa uchanganuzi wa umma wa mpokeaji ili kukokotoa siri ya ECDH iliyoshirikiwa. Siri hii hutoa "tweak" ya kriptografia ambayo, ikiongezwa kwa ufunguo wa matumizi wa mpokeaji, huunda anwani ya kipekee ya Taproot kwa shughuli hiyo.



Mpokeaji anaweza kutoa tena hesabu hii kwa kutumia ufunguo wake wa kuchanganua faragha na vitufe vya umma vinavyoonekana katika shughuli ya ununuzi (Diffie-Hellman hisabati mali). Hii humwezesha kutambua na kutumia pesa bila mwingiliano wowote wa awali na mtumaji.



Mbinu hii inatoa faida kadhaa:




- Usiri wa mpokeaji**: kila malipo huishia katika anwani tofauti
- Usiri wa mtumaji**: hakuna kitambulisho endelevu kinachounganisha malipo
- Hakuna seva ya mtu wa tatu**: itifaki inafanya kazi kwa uhuru
- Shughuli zisizoweza kutofautishwa**: Malipo ya Kimya yanaonekana kama miamala ya kawaida ya Taproot



Drawback kuu ni gharama ya skanning: mpokeaji anapaswa kuchambua kila shughuli mpya ya Taproot ili kugundua wale waliokusudiwa kwake.



Iwapo ungependa kupata maelezo zaidi kuhusu utendakazi wa kiufundi wa Malipo ya Kimya, tunapendekeza kozi ya BTC204 kuhusu usiri katika Bitcoin, inayojumuisha sura inayohusu Malipo ya Kimya:



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




- Michango isiyo na bidii**: anza kupokea michango kwa sekunde
- Faragha kwa chaguomsingi**: hakuna haja ya seva au miundombinu changamano
- Uzoefu kama wa barua pepe**: tuma na upokee bitcoins kwa urahisi kama barua pepe



Unaweza kuchagua kati ya "Rejesha" ili kurejesha kwingineko iliyopo au "Unda mpya wallet" ili kuunda mpya. Bonyeza "Unda wallet mpya".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Programu kisha hutoa kifungu cha uokoaji, ambacho unapaswa kuandika kwa uangalifu kwenye nyenzo ya kimwili. Hata kwa pesa za majaribio zisizo na thamani halisi, tumia mbinu bora za kuhifadhi nakala.



### Interface na vigezo



Mara tu kwingineko imeundwa, unachukuliwa kwenye interface kuu, imegawanywa katika tabo mbili: "Transact" na "Settings".



Kichupo cha **Muamala** huonyesha salio lako la bitcoin (na ubadilishaji wake kuwa dola), orodha ya miamala ya hivi majuzi, na vitufe viwili vya kitendo: "Lipa" ili kutuma pesa, na kitufe cha kupokea (ikoni ya kupakua).



Kichupo cha **Mipangilio** hutoa chaguzi nne:




- Onyesha kifungu cha maneno cha seed**: huonyesha maneno yako ya kurejesha akaunti kwa ajili ya uhifadhi
- Badilisha sarafu ya fiat**: badilisha sarafu ya kuonyesha (USD kwa chaguo-msingi)
- Weka url ya nyuma**: sanidi URL ya seva ya Blindbit (tazama sehemu inayofuata)
- Futa wallet **: inafuta kabisa wallet kutoka kwa kifaa



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Seva ya Blindbit



Dana Wallet hutumia seva ya kuorodhesha inayoitwa **Blindbit** ili kugundua Malipo yako ya Kimya. Kuelewa jinsi inavyofanya kazi ni muhimu kwa kutathmini muundo wa uaminifu wa programu.



**Kwa nini tunahitaji seva?



Ili kugundua Malipo ya Kimya, wallet yako lazima ichanganue kinadharia miamala yote ya Taproot katika kila block na kufanya hesabu ya kriptografia (ECDH) kwa kila moja. Kwenye simu ya rununu, operesheni hii itakuwa ya kimahesabu sana na ya kutumia kipimo data.



Seva ya Blindbit hutatua tatizo hili kwa kuhesabu awali data ya kati (inayoitwa "tweaks") kwa shughuli zote za Taproot. wallet yako kisha inapakua marekebisho haya (baiti 33 kwa kila ununuzi) na kufanya hesabu ya mwisho **ndani** ili kuangalia kama malipo ni yako.



**Siri iliyohifadhiwa**



Tofauti na seva ya kawaida ya Electrum ambapo unafichua anwani zako, seva ya Blindbit haijui ni malipo gani ni yako. Inatoa data sawa kwa watumiaji wote, na ni simu yako ambayo hufanya uthibitishaji wa mwisho. Kwa hivyo usiri wako unahifadhiwa kupitia seva.



**Seva chaguo-msingi



Dana Wallet hutumia seva ya umma `silentpayments.dev/blindbit/signet` (kwa Saini) au `silentpayments.dev/blindbit/mainnet` (kwa Mainnet). Unaweza kubadilisha URL hii katika mipangilio ikiwa unapangisha seva yako mwenyewe.



**Pandisha seva yako ya Blindbit**



Kwa watumiaji wanaotaka uhuru kamili, inawezekana kupangisha seva yao ya Blindbit Oracle. Hii inahitaji:




- Nodi kamili ya Bitcoin **isiyo na tai** (isiyo ya pruned)
- Inasakinisha Blindbit Oracle (inapatikana kwenye GitHub: `setavenger/blindbit-oracle`)
- Takriban. 10 GB ya nafasi ya ziada ya diski
- Ujuzi wa kiufundi (Mkusanyiko wa Nenda, usanidi wa seva)



Hakuna programu iliyopakiwa bado inapatikana kwa Umbrel au Start9. Ufungaji unabaki kuwa mwongozo kwa wakati huu. Huu ni uga katika mageuzi amilifu, na suluhu zinazoweza kufikiwa zaidi zinaweza kutokea katika siku zijazo.



## Matumizi ya kila siku



### Kupokea fedha



Ili kupokea bitcoins, bonyeza kitufe cha kupokea (ikoni ya kupakua) kutoka kwa skrini kuu. Dana Wallet kisha inaonyesha anwani yako kamili ya Malipo ya Kimya katika umbizo `tsp1q...` kwenye Alamisho. Interface inatoa chaguzi kadhaa:




- Onyesha msimbo wa QR**: huonyesha msimbo wa QR wa anwani yako kwa uchanganuzi kwa urahisi
- Shiriki**: shiriki anwani kupitia programu za simu yako
- Nakili**: anwani ya nakala kwenye ubao wa kunakili



Kama inavyoonyeshwa kwenye skrini, unaweza kushiriki anwani hii hadharani kwenye mitandao yako ya kijamii bila kuhatarisha faragha yako.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Ili kupata pesa zako za majaribio kwa mara ya kwanza kwenye Saini, tumia bomba maalum la Malipo ya Kimya linalopatikana katika `silentpayments.dev/faucet/signet`. Nakili anwani yako `tsp1...`, ibandike katika sehemu iliyotolewa kwenye bomba, kisha uthibitishe ombi. Subiri kizuizi kichimbwe (kama dakika 10 kwenye Saini).



### Tuma malipo



Ili kutuma pesa, bonyeza kitufe cha "Lipa" kutoka skrini kuu. Skrini ya "Chagua wapokeaji" inaonekana ikiwa na chaguo tatu za kubainisha mpokeaji:




- Weka maelezo ya malipo wewe mwenyewe
- Bandika kutoka ubao wa kunakili**: bandika anwani kutoka kwa ubao wa kunakili
- Changanua Msimbo wa QR**: changanua msimbo wa QR ulio na anwani



Mara tu anwani ya mpokeaji imethibitishwa, skrini ya "Ingiza kiasi" hukuwezesha kuingiza kiasi kitakachotumwa kwa satoshi. Salio lako linalopatikana linaonyeshwa kwa marejeleo. Bonyeza "Nenda kwenye uteuzi wa ada" ili kuendelea.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Skrini inayofuata inaonyesha viwango vitatu vya malipo, kulingana na uharaka unaohitajika:




- Haraka** (dakika 10-30): ada ya juu kwa uthibitisho wa haraka
- Kawaida ** (dakika 30-60): gharama za wastani
- Polepole** (saa 1+): ada ya chini zaidi kwa shughuli zisizo za dharura



Baada ya kuchagua kiwango cha ada, "Tayari kutuma?" skrini ya uthibitishaji ni muhtasari wa maelezo yote: anwani lengwa, kiasi, muda uliokadiriwa na ada ya muamala. Angalia maelezo haya kwa uangalifu, kisha ubonyeze "Tuma" ili kutuma muamala.



Mara baada ya kutumwa, muamala huonekana kwenye historia yako na hali ya "Haijathibitishwa" hadi ijumuishwe kwenye kizuizi. Salio lako linasasishwa ipasavyo.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Faida na mapungufu



### Vivutio





- Kialimu**: kiolesura kilichorahisishwa kinacholenga kujifunza Malipo ya Kimya
- Bidirectional**: inasaidia kutuma na kupokea, tofauti na portfolios zingine
- Chanzo-wazi**: nambari inayoweza kukaguliwa kikamilifu kwenye GitHub
- Faucet** iliyowekwa wakfu: hurahisisha kupata ufadhili wa majaribio
- Bila akaunti **: hakuna usajili au data ya kibinafsi inahitajika



### Vikwazo vya kuzingatia





- Majaribio**: programu ambayo haijakaguliwa, tumia kwa tahadhari kwenye Mainnet
- Mfumo mdogo**: hasa Android, hakuna toleo la iOS
- Utendaji uliopunguzwa**: hakuna udhibiti wa sarafu, hakuna akaunti ndogo, hakuna Umeme
- Uchanganuzi wa kina**: utambuzi wa malipo hutumia rasilimali muhimu



## Mbinu bora



### Usalama wa seed



Hata kwa majaribio ya Signet yenye asili zisizo na thamani, shughulikia maneno yako ya kurejesha akaunti kwa uzito. Tumia chaguo la "Onyesha maneno ya seed" katika mipangilio ili uandike kwa makini. Kama suala la mazoezi mazuri, dumisha pochi tofauti kabisa za Signet na Mainnet: usiwahi kutumia seed iliyoundwa kwa majaribio kwenye wallet inayokusudiwa kupokea pesa halisi.



### Onyo kuhusu hali ya majaribio



Dana Wallet bado inachukuliwa kuwa ya majaribio na watengenezaji wake. Kama wanavyosema wazi: "Usitumie pesa ambazo hauko tayari kupoteza". Kwa madhumuni ya kujifunza, chagua toleo la Saini. Ikiwa unatumia toleo la Mainnet, jizuie kwa kiasi cha token.



### Hifadhi nakala na urejeshaji



Urejeshaji wa hazina ya Malipo ya Kimya unahitaji wallet inayooana na itifaki ya BIP-352. wallet ya kawaida haiwezi kuchanganua blockchain ili kupata Malipo yako ya Kimya ya UTXO. Weka Dana Wallet ikiwa imesakinishwa au tumia chaguo la "Rejesha" mwanzoni mwa uzinduzi ili kurejesha wallet iliyopo.



## Kulinganisha na BIP-47 na PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Malipo ya Kimya huondoa shughuli ya arifa ya BIP-47 kwa gharama ya skanisho ghali zaidi. PayJoin hutatua tatizo tofauti (uwiano wa pembejeo) na inaweza kuunganishwa na Malipo ya Kimya.



## Hitimisho



Dana Wallet ni zana muhimu ya kielimu ya kujifunza kuhusu Malipo ya Kimya katika mazingira yasiyo na hatari. Mbinu yake ndogo hukuruhusu kuelewa taratibu za kimsingi za itifaki ya BIP-352 bila kukengeushwa na vipengele vya pili. Kwa kufanya majaribio na Signet, utakuza uelewa wa vitendo wa teknolojia hii ya kuahidi kwa usiri wa shughuli ya Bitcoin.



Malipo ya Kimya yanawakilisha hatua muhimu ya kusonga mbele katika kupatanisha urahisi wa kutumia na kuheshimu faragha. Shauku ya jumuiya na miunganisho ya kwanza kwenye pochi mbalimbali (Keki Wallet, BitBox02, BlueWallet ya kutuma) inaelekeza kwenye siku zijazo ambapo kuchapisha anwani ya mchango hakutahatarisha tena faragha ya kifedha ya mmiliki wake.



## Rasilimali



### Nyaraka rasmi




- Dana Wallet GitHub hazina: https://github.com/cygnet3/danawallet
- Amana ya F-Cold: https://fdroid.silentpayments.dev
- Tovuti ya jumuiya ya Malipo ya Kimya: https://silentpayments.xyz
- Vipimo BIP-352: https://bips.dev/352



### Zana za mtihani wa saini




- Malipo ya Kimya ya Faucet: https://silentpayments.dev/faucet/signet
- Kichunguzi cha Saini ya Mempool: https://mempool.space/signet



### Seva ya Blindbit (inayojipangisha yenyewe)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle