---
name: BitBanana
description: Kidhibiti cha rununu cha nodi yako ya Umeme
---

![cover](assets/cover.webp)



Katika somo hili, utajifunza jinsi ya kusakinisha na kusanidi BitBanana kwenye Android ili kudhibiti nodi yako ya Umeme kutoka kwa simu yako mahiri. Tutaona jinsi ya kuunganisha programu kwenye miundombinu yako iliyopo (Umbrel, RaspiBlitz, myNode, au nodi yoyote ya LND/Core Lightning), kufanya malipo ya Radi, kudhibiti vituo vyako ukiwa mbali, kuona mapato yako ya uelekezaji, na kuhifadhi nakala za usanidi wako. Pia utajifunza kuhusu mbinu bora za usalama za kulinda ufikiaji wa nodi yako, na jinsi inavyolinganishwa na Zeus, mbadala maarufu.



## Tunakuletea BitBanana



BitBanana ni programu huria ya simu ya Android inayogeuza simu mahiri yako kuwa dashibodi kamili kwa udhibiti wa mbali wa nodi yako ya Umeme. Tofauti na pochi za umeme, ambazo hupachika nodi ya ndani kwenye simu, BitBanana inachukua falsafa ya 100% ya udhibiti wa mbali: programu haina satoshi na inaunganisha tu kwa miundombinu yako iliyopo.



Iliyoundwa na Michael Wünsch chini ya leseni ya MIT, maombi huhakikisha uwazi kamili na sifuri ukusanyaji wa data ya kibinafsi na miundo iliyothibitishwa inayoweza kuzaa tena. BitBanana kwa asili hutumia LND na Core Lightning kupitia URI za kawaida (`lndconnect://` na `clngrpc://`), ikirahisisha kwa kiasi kikubwa usanidi wa awali. Programu pia inatambua LndHub na Nostr Wallet Connect kwa watumiaji wasio na nodi ya kibinafsi, ingawa njia hizi hufanya kazi kwa uangalifu na utendakazi mdogo.



Kiolesura hutoa ufikiaji kamili wa vipengele vyote muhimu vya nodi zako: kutuma na kupokea malipo (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), usimamizi wa kituo cha umeme (kufungua, kufunga, kurekebisha ada, kusawazisha upya), udhibiti wa juu wa sarafu na usimamizi wa minara. BitBanana pia hutekelezea tabaka kadhaa thabiti za usalama: kufuli kwa kibayometriki, hali ya siri, PIN ya Dharura, na usaidizi wa asili wa Tor ili kuficha miunganisho.



## Majukwaa na usakinishaji unaoungwa mkono



### Ufungaji



BitBanana inapatikana kwa Android 8.0 au matoleo mapya zaidi. Programu haipo kwenye iOS, na hakuna toleo lililopangwa. Kizuizi hiki kinafafanuliwa na historia ya mradi: BitBanana ndiye mrithi wa moja kwa moja wa Zap Android, iliyotengenezwa hapo awali na Michael Wünsch, ambaye aliamua kuendelea na kazi yake chini ya chapa yake mwenyewe. Zap ilikuwa familia ya programu tofauti (Zap Android, Zap iOS, Zap Desktop) iliyotengenezwa na wachangiaji tofauti kwa misingi tofauti ya misimbo. BitBanana inatafuta tawi la Android pekee.



Kwa kuongezea, mfumo ikolojia wa iOS unawasilisha vikwazo muhimu vya udhibiti na kiufundi kwa programu zisizodhibitiwa za Umeme. Mnamo 2023, Apple ilikataa sasisho la Zeus kwa "ukiukaji wa leseni", na mnamo 2024, Phoenix Wallet iliondoka kwenye Duka la Programu la Merika kutokana na kutokuwa na uhakika wa udhibiti kuhusu watoa huduma wa Umeme. Vikwazo hivi hufafanua kwa nini watengenezaji wengi wa Radi wanapendelea Android, ambayo inatoa sera iliyo wazi zaidi kwa programu zisizodhibiti.



Mbinu tatu za usakinishaji zinapatikana kwa Android: Duka la Google Play (usakinishaji 5000+, masasisho ya kiotomatiki), F-Droid (miundo inayoweza kurudiwa, uthibitishaji wa msimbo wa chanzo), au APK ya mwongozo kutoka GitHub.



![BitBanana](assets/fr/01.webp)



Tovuti rasmi ya bitbanana.app (kushoto) inajivunia "Kujitunza kwa 100% na ukusanyaji wa data ZERO". Skrini ya kati inaonyesha chaguo tatu za upakuaji: F-Droid (inapendekezwa), Google Play, na APK. Skrini iliyo upande wa kulia inaonyesha ruhusa ya arifa za arifa za malipo.



Programu inaomba ruhusa: mtandao (muunganisho wa nodi), kamera (misimbo ya QR), NFC (LNURL), huduma za usuli (arifa), bayometriki (usalama), na WireGuard VPN. Hakuna vifuatiliaji, ukusanyaji wa data sufuri. Washa nenosiri au kufunga kwa kibayometriki ili kupata ufikiaji salama.



## Usanidi wa awali



### Kuunganisha kwa node ya LND



Ili kuunganisha BitBanana kwenye nodi yako ya LND (Umbrel, RaspiBlitz, myNode), pata `lndconnect` URI au msimbo wa QR ulio na anwani, cheti cha TLS na macaroon ya uthibitishaji.



Kwa somo hili, tunatumia nodi ya LND kupitia mwavuli. Kwa maelezo zaidi, tafadhali tazama mafunzo yetu maalum:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Kwenye programu ya Njia ya Umeme, fikia menyu iliyo upande wa juu kulia na uchague "Unganisha wallet".



![BitBanana](assets/fr/04.webp)



Chagua **gRPC (Tor)** ili kuunganisha kupitia Tor (inapendekezwa). Msimbo wa QR na maelezo (Host .onion, Port 10009, Macaroon) huonyeshwa.



![BitBanana](assets/fr/02.webp)



Katika BitBanana, bonyeza "CONNECT NODE", changanua msimbo wa QR au ubandike URI. Idhinisha ufikiaji wa kamera, kisha uangalie anwani ya .onion inayoonyeshwa kabla ya kuthibitisha.



** Muunganisho wa Umeme wa Msingi **



Ukitumia Core Lightning (CLN) badala ya LND, mchakato utasalia kuwa sawa, na URI `clngrpc://` iliyo na cheti cha pamoja cha TLS. Core Lightning asilia inaweza kutumia BOLT12 (ofa), kuwezesha ankara zinazoweza kutumika tena na malipo ya mara kwa mara hayapatikani kwenye LND.



**Muunganisho bila nodi ya kibinafsi (LNbits/imepangishwa)**



Ikiwa huna nodi ya Umeme, BitBanana inaweza kuunganisha kwa huduma zinazopangishwa kupitia LndHub (itifaki inayotumiwa na BlueWallet na LNbits) au Nostr Wallet Connect (NWC). Tafadhali kumbuka: njia hizi zinafanya kazi katika hali ya uhifadhi (huduma hupangisha pesa zako) na utendakazi mdogo. Hutaweza kudhibiti vituo au kusanidi ada za uelekezaji, na utaweza kutuma na kupokea malipo ya Umeme pekee.



Kwa maelezo zaidi kuhusu LNbits au Nostr Wallet Connect, tafadhali soma mafunzo yetu mbalimbali:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Matumizi ya kila siku



### Interface kuu



Skrini ya kwanza huonyesha salio lako la Umeme, na menyu iliyo juu kushoto ikipeana ufikiaji wa sehemu zifuatazo: Vituo, Uelekezaji, Saini/Thibitisha, Nodi, Anwani, Mipangilio, Hifadhi Nakala. Aikoni ya saa (juu kulia) inafungua historia ya muamala. Vifungo vya "Tuma" na "Pokea" chini hukuruhusu kutuma na kupokea satoshi zako.



![BitBanana](assets/fr/05.webp)



### Umeme na malipo ya on-chain



![BitBanana](assets/fr/10.webp)



**Tuma malipo:** Bonyeza kitufe cha "Tuma" kutoka kwenye skrini ya kwanza. Skrini ya malipo (kushoto) hukupa kubandika anwani au data ya malipo kwenye sehemu ya "Address au data ya malipo", na kichanganuzi cha QR juu kulia kwa misimbo ya kuchanganua. Unaweza pia kuchagua anwani iliyohifadhiwa katika sehemu ya Anwani ili kuepuka kulazimika kuchanganua kila wakati.



BitBanana inatambua kwa akili miundo yote ya malipo: ankara za kawaida za Umeme (mistari ya herufi inayoanza na `lnbc`), Lightning Address (muundo wa barua pepe kama vile `utilisateur@domaine.com`), misimbo ya lipa ya LNURL kwa malipo yanayobadilika, toa LNURL kwa kutoa pesa, na hata ufunguo wa Keysend wa malipo ya umma moja kwa moja. Programu hutekeleza maazimio muhimu ya LNURL kiotomatiki chinichini.



Baada ya ankara kupakiwa, BitBanana huonyesha maelezo kamili: kiasi kamili, makadirio ya ada za uelekezaji, maelezo ya malipo (ikiwa yametolewa na mpokeaji), na tarehe ya mwisho wa matumizi ya ankara. Baada ya uthibitisho, malipo yatapitishwa kupitia chaneli zako za Umeme. Kisha unaweza kutazama njia iliyochukuliwa hop by hop na gharama zinazolipwa katika maelezo ya muamala.



**Pokea malipo:** Bonyeza kitufe cha "Pokea". Kiteuzi (skrini ya kulia) hukuwezesha kuchagua kati ya Umeme (malipo ya papo hapo kupitia chaneli zako) na On-Chain. Kwa risiti ya umeme, weka kiasi unachotaka katika satoshis (au acha saa 0 ili kuunda ankara isiyo na kiasi maalum ili mlipaji akamilishe), na uongeze maelezo ya hiari ili yaonekane kwenye ankara. BitBanana hutengeneza ankara ya Umeme papo hapo yenye msimbo wa QR ili kuchanganua. Unaweza pia kunakili ankara kama maandishi na kuituma kwa barua pepe. Mara tu malipo yanapopokelewa, arifa kutoka kwa programu inakuarifu na muamala huonekana mara moja kwenye historia pamoja na maelezo yake yote.



### Njia na uelekezaji



![BitBanana](assets/fr/06.webp)



Sehemu ya "Vituo" huonyesha uwezo wako wa kutuma/kupokea na kuorodhesha vituo vyako kwa ishara za kipekee. Kila chaneli inaonyesha mgawanyiko wake wa ukwasi kati ya salio la ndani na la mbali. Gusa kituo kwa maelezo kamili na vitendo (kufunga, kubadilisha ada za uelekezaji). Nukta tatu zilizo juu kulia hupeana ufikiaji wa chaguo la "Rebalance" ili kusawazisha ukwasi wa vituo vyako. Kitufe cha "+" hufungua kituo kipya.



Sehemu ya Uelekezaji (skrini ya kati) inaonyesha mapato ya usambazaji kulingana na kipindi (1D, 1W, 1M, 3M, 6M, 1Y) ikiwa na historia ya kina ya mbele ili kuboresha mkakati wako.



Saini/Thibitisha (skrini ya kulia) hukuruhusu kusaini/kuthibitisha ujumbe kwa njia fiche ili kuthibitisha udhibiti wa nodi.



### Multi-nodes na vigezo



![BitBanana](assets/fr/07.webp)



**Dhibiti Nodi**: huorodhesha nodi zako, na vitufe vya kuongeza wewe mwenyewe, kuchanganua QR, au kugeuza kati ya nodi. Hasa, unaweza kuanzisha aina tofauti za uunganisho kwenye node sawa: LAN, VPN au Tor.



**Dhibiti Anwani**: huhifadhi anwani zako za Umeme kwa malipo ya haraka.



**Mipangilio**: geuza kukufaa sarafu, lugha, ishara. Sehemu ya Usalama na Faragha: Kufuli ya Programu (PIN/bayometriki), Ficha salio (hali ya siri), Tor (kuficha utambulisho wa IP). Usanidi wa maneno ya bei, vichunguzi vya kuzuia, wakadiriaji wa ada maalum.



## Faida na mapungufu



**Mambo muhimu:**




- Jumla ya uhamaji: dhibiti nodi yako ya Umeme kutoka popote
- Utendaji kamili: malipo (LNURL, Lightning Address, BOLT 12), usimamizi wa chaneli, udhibiti wa sarafu, minara, nodi nyingi
- Usalama: PIN/bayometriki, hali ya siri, PIN ya Dharura, Tor asili, kuzuia picha za skrini
- Bure, chanzo wazi (MIT), tume sifuri, ukusanyaji wa data sifuri



**Mapungufu:**




- Inahitaji nodi ya Umeme inayotumika (au LNbits katika hali ya uhifadhi)
- Hakuna toleo la iOS lililopangwa
- Kupata ufikiaji wa simu ni muhimu (msimamizi wa macaroon = ufikiaji kamili wa nodi)



## Mbinu bora



**Usalama:**




- Washa kifunga PIN/kibayometriki (huzuia ufikiaji usioidhinishwa wa nodi)
- Sanidi PIN ya Dharura (hufuta data nyeti ikiwa kuna shinikizo)
- Kamwe usishiriki URI yako ya kuingia au macaroon
- Hali ya siri katika mazingira ya uhasama



**Ingia:**




- VPN mesh (Tailscale, ZeroTier): maelewano bora kati ya kasi na usalama
- Tor: usiri wa kiwango cha juu, utulivu wa hali ya juu
- Clearnet: epuka isipokuwa lazima (ya kufichua IP, bandari wazi)



### Hifadhi nakala na urejeshaji



Hatimaye, kuna menyu ya "Chelezo", ambayo hukuwezesha kuhifadhi usanidi wako kwa ajili ya kuhamisha simu au kusakinisha upya.



![BitBanana](assets/fr/08.webp)



**Muhimu:** Hifadhi rudufu HAINA seed au chelezo za chaneli (ya kufanya kwenye nodi). Ina: usanidi wa nodi (anwani, vyeti, macaroons), maandiko, mawasiliano, vigezo. Kitufe cha kurejesha hukuruhusu kuleta nakala rudufu iliyopo. Uthibitishaji unahitajika kabla ya kuhifadhi.



![BitBanana](assets/fr/09.webp)



Ingiza nenosiri la usimbaji fiche (skrini ya kulia). Mfumo hufungua kiteuzi cha faili (skrini ya kushoto) ili kuhifadhi `BitBananaBackup_2025-XX-XX.dat`. Uthibitishaji "Hifadhi nakala imeundwa".



**Usalama:** Hifadhi nakala rudufu iliyosimbwa (wingu la kibinafsi, USB, NAS). Usishiriki kamwe faili au manenosiri. Jaribio la kurejesha mara kwa mara. Hifadhi rudufu hurejesha miunganisho, si fedha.



## BitBanana vs Zeus: Kuna tofauti gani?



Ikiwa unachunguza programu za simu za kudhibiti nodi ya Umeme, unaweza kukutana na Zeus, mbadala maarufu wa BitBanana. Tofauti na BitBanana, ambayo inalenga pekee udhibiti wa kijijini wa nodi iliyopo, Zeus inachukua mbinu ya kina zaidi, ikitoa njia mbili za uendeshaji: nodi ya Umeme iliyopachikwa moja kwa moja kwenye programu (modi iliyopachikwa na LND iliyounganishwa) na unganisho la mbali kwa nodi ya nje, kama BitBanana.



Utendaji huu wa pande mbili hufanya Zeus kuvutia haswa kwa wanaoanza wanaotaka kujaribu Umeme bila miundombinu yoyote ya hapo awali. Hali iliyopachikwa huwezesha uanzishaji mara moja kwa nodi kamili ya rununu, wakati watumiaji wa hali ya juu wanaweza kubadili hadi muunganisho wa mbali mara tu nodi zao za kibinafsi zitakaposanidiwa. Zeus pia inasaidia LND na Core Radi kwa unganisho la mbali, kama vile BitBanana.



Faida nyingine kuu ya Zeus ni upatikanaji wake kwenye mfumo mtambuka (iOS na Android), ilhali BitBanana inasalia kuwa msingi wa Android pekee. Zeus pia hujumuisha miundombinu ya Olympus LSP ili kuwezesha upokeaji wa malipo ya Radi kupitia chaneli zinazoingia kwa wakati, mfumo wa Sehemu za Uuzaji kwa wafanyabiashara, na utendakazi jumuishi wa kubadilishana ili kudhibiti ukwasi.



Hata hivyo, BitBanana huhifadhi uwezo wake mahususi: kiolesura rahisi zaidi, kilichorahisishwa zaidi, matumizi bora ya mtumiaji (UX) kutokana na umakini wake wa kipekee wa udhibiti wa mbali, na mbinu ya elimu yenye maelezo ya muktadha. Zeus hutoa utendaji zaidi, lakini kwa gharama ya interface ngumu zaidi. Programu bado inafaa kwa watumiaji wanaotaka kudhibiti nodi kutoka kwa mbali pekee, bila utendakazi wa uhifadhi.



Ili kujua zaidi kuhusu Zeus, angalia mafunzo yafuatayo:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Hitimisho



BitBanana hugeuza simu yako mahiri ya Android kuwa dashibodi kamili ya Umeme, inayotoa uhamaji usio na kifani kwa waendeshaji wa nodi. Programu inashughulikia utendakazi wote: malipo (miundo yote), usimamizi wa chaneli, udhibiti wa sarafu, minara ya kutazama, nodi nyingi, na usalama ulioimarishwa (PIN/bayometriki, Tor, PIN ya Dharura).



BitBanana ikiwa ni mamlaka kamili, haikusanyi data yoyote na haiathiri usiri wala udhibiti wa pesa zako. Msimbo wa chanzo huria (MIT) huhakikisha uwazi.



## Rasilimali



### Nyaraka rasmi




- [Tovuti ya BitBanana](https://bitbanana.app)
- [Kamilisha hati](https://docs.bitbanana.app)
- [Msimbo wa chanzo wa GitHub](https://github.com/michaelWuensch/BitBanana)



### Ufungaji




- [Duka la Google Play](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)