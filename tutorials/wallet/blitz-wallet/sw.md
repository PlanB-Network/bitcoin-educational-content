---
name: Blitz Wallet
description: Pochi ya Bitcoin rahisi zaidi.
---

![cover](assets/cover.webp)

Uzoefu wa mtumiaji ni moja ya mambo muhimu wakati wa kuchagua pochi ya Bitcoin. Katika mafunzo haya, tunakuonyesha Blitz Wallet, pochi inayoweka urahisi katikati ya mbinu yake: shukrani kwa kuunganishwa kwa itifaki ya **Spark**, Blitz inakupa moja ya pochi za Bitcoin rahisi na kamili zaidi sokoni, yenye malipo ya papo hapo na bila usimamizi wa kiufundi.

## Blitz Wallet ni nini?

Blitz Wallet ni pochi ya Bitcoin ya **self-custodial** na **open source**, inayozingatia uhuru wako na uzoefu wa mtumiaji laini na rahisi.

[Blitz Wallet](https://blitz-wallet.com/) ni programu ya simu inayopatikana kwenye Android (Play Store) na iOS (App Store).

Tofauti na pochi za Lightning za jadi ambazo zinahitaji kudhibiti njia za malipo na ukwasi wa kuingia, Blitz Wallet inategemea **itifaki ya Spark** kuondoa ugumu huu wa kiufundi. Matokeo: malipo ya papo hapo tangu satoshi ya kwanza iliyopokelewa, bila usanidi wowote wa awali. Lengo la Blitz ni kufanya malipo ya bitcoin kuwa rahisi kama programu ya kawaida ya malipo, bila kuathiri kamwe self-custody ya fedha zako.

Blitz Wallet pia inasaidia **anwani zinazosomeka** katika muundo wa `mtumiaji@kikoa.com` (kupitia LNURL), ambayo inaruhusu kutuma bitcoin kwa urahisi kama barua pepe, bila kuhitaji kushughulikia invoices ndefu au QR codes kwa kila muamala.

## Kuelewa itifaki ya Spark

Kabla ya kuendelea na mazoezi, ni muhimu kuelewa teknolojia inayofanya Blitz Wallet kufanya kazi chini ya uso: **itifaki ya Spark**.

### Spark ni nini?

Spark ni itifaki ya safu ya juu ya open source iliyojengwa juu ya Bitcoin, iliyotengenezwa na timu ya Lightspark. Inaruhusu kufanya muamala wa papo hapo na kwa gharama ndogo, huku ikihifadhi self-custody ya bitcoin zako.

Tofauti na Lightning Network ambayo inategemea **njia za malipo** kati ya pande mbili, Spark inatumia teknolojia inayoitwa **statechain** (mnyororo wa hali). Kanuni ya msingi ni ifuatayo: badala ya kusogeza bitcoin kwenye blockchain kwa kila muamala, Spark inahamisha **haki ya kutumia** kutoka kwa mtumiaji mmoja kwenda mwingine, bila harakati yoyote on-chain.

### Inafanyaje kazi?

Ili kuelewa Spark kwa njia rahisi, hebu tufikirie kwamba kutumia bitcoin kwenye Spark kunahitaji kukamilisha fumbo lenye vipande viwili:
- Kipande kimoja kinashikiliwa na mtumiaji (kwa mfano, Alice).
- Kipande kingine kinashikiliwa na kundi la waendeshaji linaloitwa **Spark Entity (SE)**.

Ni mchanganyiko wa vipande viwili vinavyolingana pekee ndio unaoruhusu kutumia bitcoin.

Alice anapotaka kutuma bitcoin zake kwa Bob, hivi ndivyo inavyotokea: fumbo jipya linaundwa kwa pamoja kati ya Bob na SE. Fumbo linabaki na umbo lile lile, lakini vipande vinavyounda vinabadilika. Sasa, ni kipande cha Bob kinacholingana na kile cha SE. Kipande cha zamani cha Alice kinakuwa kisichotumika, kwa sababu SE imeharibu kipande chake kinacholingana. Umiliki wa bitcoin umebadilika mikono, **bila muamala wowote kwenye blockchain**.

Bob anaweza kurudia mchakato huo huo kutuma bitcoin hizi kwa Carol, na kadhalika. Kila uhamisho unafanya kazi kwa kubadilisha vipande vya fumbo, si kwa harakati ya fedha on-chain.

### Kwa nini ni salama?

Swali halali linatokea: nini kinatokea ikiwa SE haiharibu kweli kipande chake cha zamani?

Spark Entity si chombo kimoja: ni kundi la waendeshaji huru. Kipande cha SE kamwe hakishikiliwi na mwendeshaji mmoja. Kubadilisha fumbo kunahitaji ushirikiano wa waendeshaji kadhaa. Inatosha kwamba **mwendeshaji mmoja awe mkweli** wakati wa uhamisho ili kuzuia kuwezesha tena fumbo la zamani. Hakuna mwendeshaji yeyote aliye peke yake anayeweza kwa siri kuhifadhi fumbo la zamani linalofanya kazi au kuliunda tena baadaye.

Zaidi ya hayo, Spark inajumuisha utaratibu wa kutoka kwa upande mmoja: unaweza daima kupata bitcoin zako on-chain bila ushirikiano wa SE. Utaratibu huu wa dharura ni sehemu muhimu ya usanifu wa Spark, na unahakikisha kwamba huwi tegemezi kamwe kwa mtandao kupata fedha zako.

### Spark dhidi ya Lightning Network

Spark na Lightning hazishindani: ni **zinazokamilishana**. Blitz Wallet inaunganisha zote mbili, ambayo inakuruhusu kunufaika na faida za kila moja.

|                               | **Spark**                    | **Lightning Network**  |
| ----------------------------- | ---------------------------- | ---------------------- |
| **Teknolojia**                | Statechains (minyororo ya hali) | Njia za malipo      |
| **Usimamizi wa njia**         | Hauhitajiki                  | Inahitajika            |
| **Ukwasi wa kuingia**         | Hauhitajiki                  | Inahitajika            |
| **Muamala wa papo hapo**      | Ndiyo                        | Ndiyo                  |
| **Self-custody**              | Ndiyo                        | Ndiyo                  |
| **Uoanifu wa Lightning**      | Ndiyo (kupitia atomic swaps) | Asili                  |

Lightning Network inabaki kuwa itifaki bora kwa malipo ya papo hapo, lakini inaweka vikwazo vya kiufundi (usimamizi wa njia, ukwasi wa kuingia, nodi mkondoni...) ambavyo vinaweza kuzuia waanziaji. Spark inaondoa vikwazo hivi huku ikibaki kuwa inaendana na Lightning.

## Ufungaji na usanidi

Katika mafunzo haya, tunategemea toleo la Android la Blitz Wallet, lakini michakato yote iliyowasilishwa hapa chini pia inatumika kwenye iOS.

![installation](assets/fr/01.webp)

Blitz Wallet ikiwa ni pochi ya self-custody, una chaguo kati ya **kuunda pochi mpya** au **kuingiza maneno ya kurejesha** (maneno 12 au 24) ya pochi iliyopo.

Hapa, tunaanza na kuunda pochi mpya. Pata hapa chini mapendekezo yetu kuhusu kuhifadhi maneno yako ya kurejesha:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **MUHIMU**: Maneno haya 12 au 24 ya kurejesha ni **ufunguo pekee wa kufikia bitcoin zako**. Blitz ni pochi ya self-custodial: si Blitz wala Spark hawana ufikiaji kwa maneno yako ya kurejesha wala fedha zako. Ukipoteza maneno haya, utapoteza kabisa ufikiaji kwa bitcoin zako. Usiyashiriki na mtu yeyote: yeyote anayemiliki anaweza kutumia bitcoin zako.

Kisha unda **PIN** ili kulinda ufikiaji wa pochi yako.

![setup-wallet](assets/fr/02.webp)

## Kuanza na Blitz

Kufanya muamala na Blitz ni rahisi zaidi kuliko pochi nyingi nyingine za Bitcoin. Kiolesura ni kidogo na kinazingatia vitendo vitatu vikuu: kutuma, kuskanisha na kupokea.

### Kupokea bitcoin

Ili kupokea bitcoin kwenye pochi yako ya Blitz, bonyeza ikoni ya **"Mshale chini"** (↓), ingiza kiasi katika satoshi unachotaka kupokea, ongeza maelezo ya hiari, kisha pochi itaunda invoice ambayo unaweza kushiriki na mtumaji wako.

⚠️ **KUMBUKA**: Satoshi (au "sat") ni kitengo kidogo zaidi cha bitcoin: **1 bitcoin = 100 000 000 satoshi**.

Moja ya sifa za kipekee za Blitz Wallet ni kwamba inasaidia mitandao na itifaki kadhaa za mfumo wa ikolojia wa Bitcoin:

- **Lightning Network**: Moja ya safu za juu za Bitcoin inayoruhusu kufanya malipo madogo papo hapo kwa ada ndogo sana. Bora kwa kiasi kidogo cha kila siku.

- **Bitcoin (on-chain)**: Blockchain kuu ya itifaki ya Bitcoin, inayofaa kwa muamala wa kiasi kikubwa ambapo usalama wa juu na uhakika ni vipaumbele.

- **Liquid Network**: Sidechain (mnyororo sambamba) wa Bitcoin ulioendelezwa na Blockstream, unaoruhusu muamala wa haraka na wa siri kwa kutumia Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Kwa chaguo-msingi, Blitz inaunda invoice ya Lightning, lakini unaweza kuchagua mtandao ambao unataka kupokea satoshi zako kwa kubonyeza kitufe cha **"Choose format"**.

![receive-sats](assets/fr/03.webp)

### Kuunda anwani

Blitz Wallet inarahisisha kutuma bitcoin mara kwa mara kupitia mfumo wake wa anwani.

Katika menyu ya **Contacts**, unaweza kurekodi majina ya watumiaji wa Blitz au anwani za Lightning (LNURL) ambazo unashirikiana nazo mara kwa mara.

Hivyo utaweza kutuma satoshi kwa anwani hizi kwa mibofyo michache, bila kuhitaji kuskanisha QR code au kuingiza kwa mkono anwani kila wakati.

### Kutuma bitcoin

Mbali na njia za kawaida za kutuma bitcoin (kuskanisha QR code, kuingiza anwani kwa mkono), Blitz inatoa chaguzi kadhaa za vitendo:

- **Kutoka kwa picha** (*From Image*): Ingiza QR code kutoka kwa galeri yako ya picha.
- **Kutoka kwa ubao wa kunakili** (*From Clipboard*): Bandika anwani au invoice iliyonakiliwa awali.
- **Kuingiza kwa mkono** (*Manual Input*): Ingiza moja kwa moja anwani ya Bitcoin, invoice ya Lightning au anwani inayosomeka (kwa mfano `mtumiaji@walletofsatoshi.com`).
- **Kutoka kwa anwani zako**: Chagua mpokeaji aliyesajiliwa awali ili kutuma kwa mibofyo michache.

Katika menyu ya **Wallet**, bonyeza kitufe cha **"Mshale juu"** (↑), chagua njia yako ya kutuma, ingiza kiasi cha kutuma, ongeza maelezo na uthibitishe muamala.

Kiasi cha chini cha kufanya kutuma kwa sasa ni **satoshi 1 000**.

![send-bitcoin](assets/fr/05.webp)

## Duka la Blitz

Zaidi ya shughuli za kuhamisha bitcoin, Blitz Wallet inajumuisha duka ambalo unaweza kutumia bitcoin zako kununua huduma za kidijitali moja kwa moja kutoka kwa programu.

Kutoka kwa menyu kuu, bonyeza kichupo cha **Store** ili kufikia duka. Pia utapata ufikiaji kwa jukwaa la **Bitrefill** ambalo linaruhusu kununua kadi za zawadi kutoka kwa maelfu ya wafanyabiashara duniani kote, moja kwa moja kwa bitcoin.

- **Akili bandia**: Fikia modeli za hivi karibuni za AI ya kuzalisha (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) na ulipe mikopo yako moja kwa moja kwa satoshi. Vifurushi kadhaa vinapatikana kulingana na mahitaji yako (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **SMS zisizo na jina**: Tuma na pokea SMS popote duniani bila kufichua nambari yako ya simu ya kibinafsi. Huduma hii inalipwa kwa satoshi kwa kila ujumbe uliotumwa.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Linda faragha yako mtandaoni kwa kujisajili kwa usajili wa VPN WireGuard (wa kila wiki, kila mwezi au kila robo), unaolipwa kwa bitcoin moja kwa moja kutoka duka la Blitz. Utahitaji tu kupakua programu ya mteja wa WireGuard kwenye kifaa chako ili kufurahia.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet nyuma ya pazia: kwenda mbali zaidi

Nyuma ya urahisi wa kutumia Blitz Wallet kuna usanifu wa kiufundi uliofikirika vizuri unaochanganya safu kadhaa za mfumo wa ikolojia wa Bitcoin.

### Ugawaji wa salio lako

Blitz Wallet inasimamia salio lako kwa uwazi kwa kugawanya fedha zako kati ya itifaki tofauti kulingana na mahitaji. Salio lako linapokuwa chini ya satoshi 500 000, Blitz inatumia **Liquid Network** na atomic swaps ili kukupa uzoefu laini na kuruhusu muamala kwenye Lightning Network hata kwa kiasi kidogo.

Mbinu hii inahakikisha uanzishaji rahisi kwa watumiaji wapya, bila wao kuhitaji kuelewa taratibu za msingi. Unaweza kuona ugawaji wa salio lako kati ya safu tofauti katika menyu ya **Mipangilio > Balance Info**.

![balance](assets/fr/09.webp)

### Hali ya Lightning (ya hiari)

Kwa chaguo-msingi, Blitz Wallet inatumia Liquid Network na itifaki ya Spark kukupa uzoefu laini bila usanidi wa kiufundi. Hata hivyo, Blitz inakupa uwezekano wa kuwezesha **hali ya Lightning** ambayo itafungua moja kwa moja njia ya malipo utakapofikia salio la **satoshi 500 000** (0.005 BTC).

Ili kuwezesha hali ya Lightning, nenda kwenye **Mipangilio**, kisha katika sehemu ya **Mipangilio ya Kiufundi**, bonyeza chaguo la **Node Info**.

![enable-lightning](assets/fr/10.webp)

Shukrani kwa itifaki ya Spark, kuwezesha huku ni **kwa hiari**: Spark tayari inaruhusu kufanya malipo yanayoendana na Lightning bila kuhitaji kufungua njia au kudhibiti ukwasi wa kuingia. Hali ya Lightning ya asili inabaki kuwa muhimu kwa watumiaji wa hali ya juu wanaotaka kuwa na nodi yao ya Lightning iliyounganishwa ndani ya programu.

### Kituo cha mauzo (PoS)

Blitz Wallet inajumuisha kipengele cha **kituo cha mauzo** kinachowapa wafanyabiashara uwezo wa kukubali malipo kwa bitcoin moja kwa moja kutoka kwa programu.

Katika menyu ya **Mipangilio > Point-of-sale**, unaweza kusanidi:

- Kitambulisho cha kipekee cha duka lako
- Sarafu ya ndani ya fiat ya kuonyesha bei
- Maagizo kwa wafanyakazi wako
- Chaguo la bakshishi kwa wateja wako

Wateja wako wanahitaji tu kuskanisha QR code iliyoundwa ili kufanya malipo yao kwa bitcoin, papo hapo.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Rasilimali zilizotumika kuandika mafunzo haya:
- Blog ya [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
