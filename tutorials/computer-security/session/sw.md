---
name: Session
description: Tuma ujumbe uliosimbwa kwa njia fiche, si metadata
---
![cover](assets/cover.webp)



Session ni programu ya ujumbe iliyosimbwa kwa njia fiche iliyoundwa mnamo 2020, iliyoundwa ili kutoa kiwango cha juu cha usiri kuliko ujumbe wa kawaida. Ilianzishwa kwanza na *Oxen Privacy Tech Foundation*, kisha na *Session Technology Foundation*.



Kipindi kina sifa za kiufundi zinazovutia: usimbaji fiche kutoka mwisho hadi mwisho, mtandao uliogatuliwa uliopangwa ili kuhakikisha upatikanaji na upungufu, na uelekezaji wa vitunguu ulioongozwa na Tor. Pia, tofauti na WathsApp au Signal, ambayo inahitaji nambari ya simu kwa usajili, Kipindi hakiulizi taarifa za kibinafsi (hakuna nambari, hakuna barua pepe, jozi ya funguo za siri).



Kipindi hukuwezesha kutuma ujumbe, faili, ujumbe wa sauti, simu za sauti, pamoja na vikundi vya hadi wanachama 100 (na jumuiya zaidi ya hapo), huku ukipunguza uvujaji wa metadata.



![Image](assets/fr/01.webp)



Kipindi kinalenga zaidi ya yote kwa watumiaji wanaoweka usiri katika moyo wa vipaumbele vyao. Huduma hii ya kutuma ujumbe inawakilisha njia mbadala ya WhatsApp, yenye usanifu ulioundwa kustahimili miundo ya kisasa ya uchunguzi.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Usimbaji fiche kutoka mwisho hadi mwisho*



## Sakinisha programu ya Kipindi



Kipindi kinapatikana kwenye mifumo yote. Unaweza kupakua programu moja kwa moja kutoka kwa duka la programu ya simu yako:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [Duka la Programu](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



Kwenye Android, inawezekana pia [kusakinisha kupitia APK](https://github.com/session-foundation/session-android/releases).



Katika mafunzo haya, tutaangazia toleo la simu ya mkononi, lakini tafadhali kumbuka kuwa [matoleo ya kompyuta yanapatikana pia](https://getsession.org/download) (MacOS, Linux na Windows). Baadaye, tutaangalia jinsi ya kusawazisha akaunti kwenye vifaa vingi.



## Fungua akaunti kwenye Kipindi



Wakati wa uzinduzi wa kwanza, bofya "*Fungua akaunti*".



![Image](assets/fr/02.webp)



Chagua jina la kuonyesha kwa wasifu wako. Hili linaweza kuwa jina bandia au jina lako halisi.



![Image](assets/fr/03.webp)



Kisha utalazimika kuchagua kati ya njia mbili za usimamizi wa arifa:





- Hali ya haraka ("**Firebase Cloud Messaging/Apple Push Notification Service**"): hukuwezesha kupokea arifa za ujumbe katika muda halisi, kutokana na huduma za arifa zinazotolewa na Google au Apple (kulingana na mfumo wako). Ili hili lifanye kazi, IP yako Address na kitambulisho cha kipekee cha arifa hutumwa kwa Google au Apple, na Kitambulisho cha akaunti ya Session pia kimesajiliwa na seva ya STF (kupitia Tor). Hali hii inahusisha (inakubalika kidogo) udhihirisho wa metadata, lakini haiathiri maudhui ya ujumbe au waasiliani, na hairuhusu shughuli yako halisi kufuatiliwa. Kwa hivyo, hali hii ina ufanisi zaidi katika suala la uitikiaji, lakini inategemea muundo msingi na haina ufanisi kidogo katika suala la usiri.





- Hali ya polepole (**upigaji kura wa usuli**): programu ya Kipindi inasalia amilifu chinichini, mara kwa mara inapiga kura kwenye mtandao kwa ujumbe mpya. Mbinu hii inahakikisha usiri mkubwa kuliko ule wa kwanza, kwani hakuna data inayotumwa kwa seva za watu wengine; si Google, Apple au seva za STF zinazopokea taarifa yoyote. Kwa upande mwingine, hali hii ina vikwazo viwili: arifa zinaweza kuchelewa (hadi dakika kadhaa), na matumizi ya nishati kwa ujumla ni ya juu kutokana na shughuli za maombi chinichini.



![Image](assets/fr/04.webp)



Sasa umeunganishwa kwenye programu ya Kipindi na unaweza kuanza kubadilishana ujumbe.



![Image](assets/fr/05.webp)



## Hifadhi akaunti yako ya Kipindi



Jambo la kwanza la kufanya kabla ya kuanza kutumia Kipindi ni kuhifadhi akaunti yako ili uweze kuirejesha ukipoteza kifaa chako. Ili kufanya hivyo, bofya kitufe cha "*Endelea*" karibu na "*Hifadhi nenosiri lako la kurejesha akaunti*".



![Image](assets/fr/06.webp)



Kisha kipindi kitaonyesha maneno ya Mnemonic. Nakili kwa uangalifu na uiweke mahali salama. Fungu hili la maneno hutoa ufikiaji kamili kwa akaunti yako ya Kipindi, kwa hivyo ni muhimu kutolifichua. Utaihitaji ili kufikia akaunti yako kwenye kifaa kingine, hasa ikiwa simu yako ya sasa itapotea au kubadilishwa.



![Image](assets/fr/07.webp)



Kifungu hiki cha maneno hufanya kazi kwa njia sawa na vifungu vya Mnemonic vinavyotumiwa katika portfolios za Bitcoin. Kwa hivyo ninapendekeza uangalie mafunzo haya mengine, ambayo ninaelezea mbinu bora za kuhifadhi maneno ya Mnemonic:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tafadhali kumbuka**: Tofauti na vishazi vya Mnemonic vinavyotumika kwenye jalada la Bitcoin, kwenye Kipindi, **lazima uhifadhi kila neno kwa ukamilifu**. Barua 4 za kwanza hazitoshi!



## Kuanzisha programu ya Kikao



Ili kufikia mipangilio ya programu, bofya kwenye picha yako ya wasifu iliyo juu kushoto mwa Interface. Hapa ndipo unaweza kuongeza picha ya wasifu.



![Image](assets/fr/08.webp)



Katika menyu ya "*Faragha*", unaweza kuwezesha au kuzima vipengele mbalimbali (tahadhari, vingine vinaweza kufichua IP yako Address). Pia ninapendekeza kuwezesha chaguo la "*Funga Programu*", ambayo inahitaji uthibitishaji ili kufikia programu.



![Image](assets/fr/09.webp)



Katika menyu ya "*Arifa*", utapata chaguo kati ya "*Hali ya Haraka*" na "*Hali ya polepole*" (angalia sehemu za awali za mafunzo). Unaweza pia kubinafsisha arifa ili ziendane na mapendeleo yako.



![Image](assets/fr/10.webp)



Hatimaye, nenda kwenye menyu ya "*Muonekano*" ili kurekebisha Interface kulingana na ladha yako. Menyu ya "*Nenosiri la Urejeshi*" hukuruhusu kupata maneno yako ya Mnemonic ikiwa ungependa kuhifadhi nakala mpya.



![Image](assets/fr/11.webp)



## Kutuma ujumbe na Kipindi



Ili kuwasiliana na watu wengine, bofya kitufe cha "**" kwenye ukurasa wa nyumbani.



![Image](assets/fr/12.webp)



Chaguzi kadhaa zinapatikana. Ikiwa ungependa kuunda au kujiunga na kikundi, chagua "*Unda Kikundi*" au "*Jiunge na Jumuiya*".



![Image](assets/fr/13.webp)



Ikiwa unataka mtu akuongeze kama mtu unayewasiliana naye, unaweza kumfanya achanganue Kitambulisho chako cha Kipindi kama msimbo wa QR.



![Image](assets/fr/14.webp)



Ili kutuma kuingia kwako kwa mbali, bofya "*Alika Rafiki*". Kisha unaweza kunakili Kitambulisho chako cha Kipindi na kukituma kupitia njia nyingine ya mawasiliano. Unaweza pia kupata maelezo haya kwa kubofya picha yako ya wasifu kutoka kwa ukurasa wa nyumbani.



![Image](assets/fr/15.webp)



Ikiwa una Kitambulisho cha Kipindi cha mtu mwingine na ungependa kukiongeza, bofya kwenye "*Ujumbe Mpya*".



![Image](assets/fr/16.webp)



Kisha unaweza kubandika kitambulisho chake katika maandishi, au uchanganue moja kwa moja ikiwa unayo kama msimbo wa QR.



![Image](assets/fr/17.webp)



Kisha tuma ujumbe wa awali kwa mtu huyu.



![Image](assets/fr/18.webp)



Mara tu mtu huyo atakapokubali ombi lako, utaona jina lake la mtumiaji likionekana, na utaweza kuzungumza naye kwa uhuru.



![Image](assets/fr/19.webp)



## Sawazisha programu ya Eneo-kazi



Ili kusawazisha akaunti yako kwenye kompyuta yako, unahitaji kusakinisha programu. [Ipakue kutoka kwa tovuti rasmi](https://getsession.org/download). Ninakushauri uangalie uhalisi na uadilifu wake kabla ya kuiweka.



![Image](assets/fr/20.webp)



Wakati wa uzinduzi wa kwanza, bofya "*Nina akaunti*".



![Image](assets/fr/21.webp)



Weka kishazi chako cha Mnemonic, ukihakikisha kuwa umeacha nafasi kati ya kila neno.



![Image](assets/fr/22.webp)



Sasa unaweza kufikia mazungumzo yako kutoka kwa kompyuta yako.



![Image](assets/fr/23.webp)



Hongera, sasa umepata mkazo wa kutumia ujumbe wa Session, njia mbadala bora ya WathsApp!



Pia ninapendekeza somo hili lingine, ambalo ninawasilisha Threema, mbadala mwingine wa kuvutia wa programu yako ya kutuma ujumbe:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74