---
name: Macadamia Wallet
description: Cashu mobile wallet kwa malipo ya BTC bila majina na ya papo hapo
---

![cover](assets/cover.webp)



Macadamia Wallet ni wallet ya simu ya iOS inayotumia itifaki ya Cashu, mfumo wa Chaumian ecash unaowezesha malipo ya Bitcoin yasiyoweza kufuatiliwa kabisa. Shukrani kwa blind signatures, hakuna mwangalizi anayeweza kuunganisha amana zako na matumizi yako, na hivyo kutoa kiwango cha faragha kinachofanana na pesa taslimu.



Katika somo hili, tutaangalia jinsi ya kusakinisha na kusanidi Macadamia, kufanya miamala yako ya kwanza ya Cashu (Mint, Send, Receive, Melt), na kudhibiti mint nyingi ili kupata pesa zako.



## Macadamia Wallet ni nini?



### Cashu Protocol



Cashu hutumia saini za upofu zilizovumbuliwa na David Chaum: unaweka bitcoin na server ya "mint", ambayo hutoa tokeni sawa katika satoshis. Mint husaini ishara hizi bila kuona maudhui yao, na hivyo kufanya kuwa vigumu kuunganisha token kwa mtumiaji. Mabadilishano ni off-chain, peer-to-peer, na hayaeleweki kabisa - hata mint haiwezi kufuatilia ni nani anamlipa nani.



Macadamia ni chanzo huria cha wallet iOS kilichotengenezwa katika Swift/SwiftUI. Inafanya kazi bila akaunti au KYC, tokeni zako huhifadhiwa ndani na zinalindwa na maneno ya seed. Msimbo unaweza kukaguliwa kwenye GitHub na tokeni zinaweza kushirikiana na wallets zingine za Cashu (Minibits, Cashu.me).



### Mfano wa uhifadhi na maelewano



**Muhimu**: Cashu hufanya kazi kwa modeli ya uangalizi. Tokeni ni ahadi za kulipa (IOUs) zinazoungwa mkono na akiba ya Bitcoin ya mint. Ikiwa mint itatoweka, ishara zako zinapoteza thamani yao. Haya ni maelewano ya usiri wa hali ya juu.



Tumia Macadamia kama wallet halisi: kiasi kidogo pekee. Sambaza pesa zako juu ya mint kadhaa ili kupunguza hatari.



## Sifa kuu



Macadamia inatekeleza shughuli nne za kimsingi za protocol ya Cashu. **Mint** hubadilisha satoshi zako kuwa tokeni kupitia ankara ya Umeme. **Tuma** hukuwezesha kutuma tokeni bila malipo kupitia msimbo wa QR au kiungo, off-chain kabisa. **Pokea** hukuwezesha kupokea tokeni au ankara ya generate ya Umeme. **Melt** hulipa ankara ya umeme kwa kuharibu tokeni zako.



wallet inasaidia usimamizi wa minara nyingi kwa wakati mmoja. Unaweza kubadilisha ishara kati ya mint tofauti kupitia Lightning.



## Mifumo inayotumika



Macadamia inapatikana tu kwenye iOS 17 au matoleo mapya zaidi kwa iPhone na iPad. Programu asilia ya Swift/SwiftUI inatoa muunganisho bora zaidi na mfumo ikolojia wa Apple.



Cashu protocol inahakikisha ushirikiano kati ya wallet. Unaweza kurejesha maneno yako ya seed katika programu zingine kama vile Minibits kwenye Android au Nutstash kwenye eneo-kazi.



Toleo la sasa linasambazwa kupitia TestFlight. Tumia kiasi kidogo tu na toleo hili la beta.



## Ufungaji



Macadamia inapatikana kwa sasa kupitia TestFlight, programu ya Apple ya majaribio ya beta. Hivi ndivyo jinsi ya kuisakinisha:



### Usakinishaji kupitia TestFlight



**Hatua ya 1: Pakua TestFlight**



Ikiwa tayari huna programu ya TestFlight kwenye kifaa chako, tafuta "TestFlight" katika App Store na uisakinishe. TestFlight ni programu rasmi ya Apple ya kujaribu matoleo ya beta ya programu za iOS.



**Hatua ya 2: Jiunge na mpango wa beta wa Macadamia** (kwa Kifaransa)



TestFlight inaposakinishwa, fuata kiungo hiki cha mwaliko kutoka kwa iPhone au iPad yako: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Kiungo kitafungua TestFlight kiotomatiki na kukupa kusakinisha Macadamia Wallet. Gusa "Kubali" kisha "Sakinisha" ili kuanza upakuaji. Programu ina uzito wa takriban megabaiti kumi na inachukua sekunde chache tu kusakinisha.



![Installation TestFlight](assets/fr/01.webp)



### Taarifa muhimu kuhusu matoleo ya beta



Macadamia bado iko katika awamu hai ya maendeleo. Matoleo ya TestFlight husasishwa mara kwa mara na huenda yakaanzisha vipengele vipya au kurekebisha hitilafu. Walakini, kama ilivyo kwa toleo lolote la beta, utendakazi unaweza kutokea. **Tunapendekeza sana utumie kiasi kidogo tu**, ambacho unakubali kinaweza kupotea iwapo kutatokea tatizo la kiufundi.



Macadamia haikusanyi data yoyote ya mtumiaji kulingana na sera ya faragha iliyoonyeshwa. Hakikisha umeangalia kuwa msanidi ni cypherbase UG wakati wa kusakinisha.



## Usanidi wa awali



Katika uzinduzi wa kwanza, Macadamia hutoa sentensi ya BIP-39 ya maneno 12. Ziandike mahali salama - kamwe kama picha ya skrini. Maneno haya hukuruhusu kuunda tena wallet yako na kutumia tokeni zako.



![Configuration initiale](assets/fr/02.webp)



Fuata hatua nne: karibu, ukubali masharti, hifadhi sentensi ya seed, na uthibitisho wa mwisho.



![Interface principale](assets/fr/03.webp)



Mara tu usanidi utakapokamilika, Macadamia inatoa tabo kuu tatu. **Wallet** huonyesha salio lako na historia ya muamala. **Minti** hukuwezesha kudhibiti seva zako za Cashu. **Mipangilio** inatoa ufikiaji wa mipangilio na maneno yako ya seed.



![Ajout d'un mint](assets/fr/04.webp)



Sasa unahitaji kusanidi mint, yaani, seva ya Cashu ambayo itatoa ishara zako. Nenda kwenye kichupo cha "Minti", gusa "Ongeza URL mpya ya Mint", na uweke anwani ya mnanaa uliochagua (k.m. mint.cubabitcoin.org). Angalia bitcoinmints.com au cashu.space kwa minti maarufu ya umma. Thibitisha minti pekee ambayo umeangalia sifa zao, kwa kuwa watakuwa na ulinzi wa satoshis zako.



## Matumizi ya kila siku



### Uundaji wa ishara mpya (Mint)



Ili kulisha Macadamia yako ya wallet na ecash, unahitaji kufanya operesheni ya "Mint" (kuunda ishara). Gusa "Pokea", kisha uchague chaguo la "Lightning". Weka kiasi unachotaka (k.m. 1000 sats), chagua mnanaa utakaotumika, kisha generate Lightning Invoice.



![Opération Mint](assets/fr/05.webp)



Lipa Lightning Invoice inayozalishwa na wallet yako ya kawaida (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Tokeni za Cashu huonekana papo hapo kwenye salio lako baada ya malipo.



### Tuma ishara



Ili kutuma tokeni za Cashu kwa mtumiaji mwingine, gusa kitufe cha "Tuma" kwenye skrini kuu, kisha uchague "Ecash". Weka kiasi kitakachotumwa (k.m. 50 sats) na uongeze memo ya maelezo ikihitajika.



![Envoi Ecash](assets/fr/07.webp)



Shiriki msimbo wa QR au maandishi yaliyotolewa kupitia iMessage, signal au Telegram. Mpokeaji anadai pesa hizo papo hapo na bila malipo.



### Pokea ishara



Ili kupokea tokeni za Cashu zilizotumwa na mtumiaji mwingine, gusa "Pokea" kisha uchague "Ecash". Changanua msimbo wa token QR au ubandike kiungo cha token ulichopokea.



![Réception Ecash](assets/fr/08.webp)



Gusa "Redeem" ili kudai token.



### Malipo ya Lightning (Melt).



Ili kulipa Lightning Invoice kwa tokeni zako za Cashu, gusa "Tuma" kisha uchague "Umeme". Bandika ankara ya BOLT11 unayotaka kulipa.



![Paiement Lightning](assets/fr/11.webp)



Minti huharibu tokeni zako na kutekeleza malipo ya Lightning. Kwa hivyo unaweza kulipia huduma yoyote ya Lightning huku ukihifadhi jina lako la kutokujulikana.



### Badilisha kati ya mints



Unapopokea ishara kutoka kwa mint ambayo haujasanidi, Macadamia inakupa chaguzi kadhaa za kudhibiti ishara hizi.



![Swap inter-mints](assets/fr/09.webp)



Ongeza mnanaa mpya au ubadilishe tokeni kwa mnanaa uliopo. Kubadilishana hutumia Lightning kama daraja ili kuhamisha pesa zako bila kujulikana.



### Usimamizi wa hali ya juu wa mint nyingi



Macadamia inatoa zana za kisasa za kudhibiti minti nyingi kwa wakati mmoja na kugawa pesa zako kimkakati.



![Gestion multi-mints](assets/fr/10.webp)



"Sambaza Pesa" husambaza salio lako kiotomatiki kulingana na asilimia (k.m. 50/50). "Uhamisho" huruhusu uhamishaji wa mikono kati ya mint ili kubadilisha hatari zako.



## Faida na mapungufu



**Mambo muhimu** :





- **Usiri wa juu zaidi**: Shughuli zisizoweza kufuatiliwa, hata kwa mint. Hakuna metadata ya blockchain, ubadilishanaji wa peer-to-peer  bila kufuatilia.
- **Haraka na bila malipo**: Uhamisho wa papo hapo bila malipo ndani ya mint, bora kwa malipo madogo.
- **Mwingiliano**: tokeni sanifu za Cashu kwa matumizi na pochi zingine zinazooana (Minibits, Nutstash).
- **Urahisi**: Asili ya Interface iOS inapatikana kwa wanaoanza huku ikisalia kukaguliwa (chanzo huria).



**Vikwazo** :





- **Muundo wa uhifadhi**: uaminifu wa mint unahitajika. Ikiwa mint itatoweka, ishara zako zinapoteza thamani yao.
- **iOS pekee**: Hakuna toleo la Android/desktop. Ushirikiano wa Cashu huruhusu ufikiaji kupitia wallet zingine, lakini matumizi bora zaidi yanasalia kuwa iOS.
- **Utegemezi wa mint**: Mint nje ya mtandao = haiwezi kufanya miamala inayohitaji uingiliaji kati wake (Mint, Melt).
- **Teknolojia inayoibuka** : Ukuzaji unaoendelea, hitilafu zinazowezekana, viwango vinavyobadilika.



## Mbinu bora





- **Tengeneza minti yako**: Sambaza chipsi zako kwenye minti kadhaa maarufu ili kupunguza hatari.
- **Kiasi kikomo**: Tumia Macadamia kama wallet halisi kwa malipo ya kila siku, si kama salama.
- **Linda seed** yako: Weka kifungu chako cha maneno 12 kwenye karatasi mahali salama. Jaribio la kurejesha mara kwa mara.
- **Angalia minti**: Pata ushauri wa cashu.space na vikao vya jumuiya kabla ya kuongeza mnanaa. Chagua zile zilizo na wakati mzuri na sifa dhabiti.
- **VPN au Tor**: Ficha IP yako na VPN/Tor ili kuongeza faragha ya mtandao.
- **Jiunge na jumuiya**: Vikundi vya Telegram/Discord Cashu kwa masasisho, mapendekezo madogo na mbinu bora zaidi.



## Hitimisho



Macadamia Wallet huleta sifa za pesa halisi kwa Bitcoin ya dijiti. Kwa kuchanganya saini za upofu za Chaum na Umeme, inatoa suluhisho la kifahari kwa usiri wa shughuli. Kiolesura chake asili cha iOS hufanya teknolojia ya kisasa ya kriptografia kufikiwa huku ikisalia kuwa chanzo huria na inaweza kushirikiana na mfumo ikolojia wa Cashu.



Mtindo wa ulezi unadai umakini na mazoea mazuri ya usalama. Ikitumiwa kwa njia ipasavyo, Macadamia inakuwa zana muhimu sana ya malipo ya kila siku inayohitaji kutokujulikana, inayosaidia wallets zisizo na dhamana kwa akiba.



## Rasilimali



### Nyaraka rasmi




- Tovuti rasmi: [macadamia.cash](https://macadamia.cash)
- Maswali Yanayoulizwa Mara kwa Mara ya Macadamia: [macadamia.cash/faq](https://macadamia.cash/faq)
- Msimbo wa chanzo wa GitHub: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Nyaraka za Cashu




- Hati za kiufundi: [docs.cashu.space](https://docs.cashu.space)
- Orodha ya minti ya umma: [bitcoinmints.com](https://bitcoinmints.com)
- Tovuti rasmi ya itifaki: [cashu.space](https://cashu.space)



### Jumuiya




- Kikundi cha Cashu cha Telegraph: [t.me/cashu_ecash](https://t.me/cashu_ecash)
