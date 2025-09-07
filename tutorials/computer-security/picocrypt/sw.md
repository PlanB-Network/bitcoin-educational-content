---
name: Picocrypt
description: Zana huria ya kusimba data yako kwa njia fiche
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian BURNEL yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Mabadiliko yamefanywa kwa maudhui asili.*



___



## I. Uwasilishaji



Katika somo hili, tutakuwa tukiangalia Picocrypt, programu rahisi, nyepesi na bora ya usimbaji fiche wa data iliyo na usalama wa hali ya juu.



Inafaa kwa **faili za usimbaji fiche**, unaweza kuitumia kulinda **data kwenye kompyuta yako, kwenye kifimbo cha USB**, lakini pia data iliyohifadhiwa kwenye Wingu. Kwa mfano, unaweza kusimba data kwa njia fiche na kuihifadhi kwenye **Microsoft OneDrive, Hifadhi ya Google, iCloud au Dropbox**, ingawa kwa kusudi hili napendelea kipande kingine cha programu ambacho kitawasilishwa katika makala yajayo.



Unaweza pia kuitumia unapohitaji **kushiriki data na mtu mwingine**: shukrani kwa Picocrypt na ufunguo wa kusimbua, wataweza kusimbua data kwenye mashine zao. Kwa hivyo ikiwa akaunti au kompyuta yako imeathiriwa, data yako inalindwa.



Ili kufuata mradi wa Picocrypt, kuna Address moja tu:





- [Picocrypt kwenye GitHub](https://github.com/Picocrypt/Picocrypt)



**chanzo huria na wazi**, PicoCrypt inapatikana kwa **Windows,** **Linux** na **macOS**. Kwenye Windows, unaweza kuisakinisha kwenye mashine yako mwenyewe au kutumia toleo linalobebeka.



## II. Picocrypt, programu huria ya usimbaji fiche



Programu ya usimbaji ya Picocrypt** inajiwasilisha kama **mbadala** kwa suluhu zingine zinazojulikana kama vile **VeraCrypt** na **Cryptomator** (*iliyoundwa kusimba data kwenye mazingira ya Wingu*), au **AxCrypt**. Kwa njia, kwenye GitHub rasmi ya Picocrypt, unaweza kupata kulinganisha na washindani wengine:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Chanzo: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt ni **nyepesi sana**, ina uzito wa **MB*3 tu, na haihitaji kusakinishwa: ni **programu inayobebeka** yenye manufaa ya kutohitaji haki za msimamizi! Walakini, haipuuzi usalama, kwani inategemea **algorithms thabiti na ya kuaminika**:





- XChaCha20** algoriti ya usimbaji fiche
- Utendakazi wa ufunguo wa kupita **Argon2**



Zaidi ya faida zilizotajwa hapo juu, kinachovutia sana ni ** urahisi wa matumizi **!



Inahitaji jambo moja tu: **ukaguzi wa nambari **, lakini hiyo imepangwa, kama unaweza kuona kutoka kwa jedwali la kulinganisha hapo juu (mstari wa mwisho). Lakini kwa kuwa ni chanzo wazi, hakuna kitu cha kukuzuia kutazama msimbo wake wa chanzo.



Hata ingawa inalinganishwa na BitLocker kwenye jedwali lililo hapo juu, **kwa maoni yangu BitLocker na Picocrypt zimekusudiwa kwa matumizi tofauti**: BitLocker kwa usimbaji wa sauti kamili (ile ya Windows, kwa mfano) na Picocrypt kwa kusimba muundo wa mti au "Hifadhi" -nafasi ya kuhifadhi.



## III. Kwa kutumia Picocrypt



Kwa onyesho hili, mashine ya Windows 11 itatumika.



### A. Kusimba data kwa kutumia Picocrypt



Kwanza kabisa, unahitaji kupakua Picocrypt.exe kutoka kwa GitHub rasmi ([tazama ukurasa huu](https://github.com/Picocrypt/Picocrypt/releases)).



Fungua programu ili kuonyesha Interface yake ya chini kabisa kwenye skrini. Ili kusimba data kwa njia fiche, iwe **faili, faili kadhaa au folda**, kwa urahisi **buruta na kuidondosha kwenye Interface** ya Picocrypt. Hii itachagua data itakayosimbwa.



![Image](assets/fr/020.webp)



Kisha, kwa usimbaji fiche wa data, unaweza kufikia chaguo kadhaa, ikiwa ni pamoja na ufunguo wa usimbuaji. Inaweza kuwa **nenosiri thabiti** au **ufunguo wa usimbaji fiche katika mfumo wa faili muhimu**, au **zote mbili**. Ikiwa tutachukua mfano wa nenosiri, una chaguo kati ya kuunda nenosiri lako mwenyewe, au kuzalisha nenosiri kwa Picocrypt.



Nenosiri hili lazima liwe na nguvu, kwani linaweza kutumika kusimbua data. Iandike chini ya "**Nenosiri**" na "**Thibitisha Nenosiri**", kisha ubofye "**Simba kwa njia fiche**" ili kusimba data kwa njia fiche! Kabla ya hapo, unaweza kubofya kitufe cha "**Badilisha**" karibu na "**Hifadhi towe kama**" ili kubainisha saraka ya towe.



**Kumbuka**: ili kutumia ufunguo katika umbizo la faili, bofya "**Unda**" upande wa kulia wa "**Faili muhimu**" ili kuunda ufunguo. Kisha uchague kwa kubofya "** Hariri**" na kuburuta na kudondosha faili muhimu kwenye eneo linalofaa.



![Image](assets/fr/019.webp)



Faili mbili zilizochaguliwa ** zimesimbwa kwa njia fiche na kuwekwa pamoja** katika faili "**Encrypted.zip.pcv**", kwa kuwa **PCV** ni kiendelezi kinachotumiwa na Picocrypt. Faili hii ya ZIP haisomeki kutokana na usimbaji fiche. Ili kuzuia faili zilizochaguliwa zisikusanywe pamoja katika faili moja ya ZIP iliyosimbwa kwa njia fiche, unahitaji kuangalia chaguo la "**Recursively**", ili kuwe na faili nyingi zilizosimbwa kama vile kuna faili zinazopaswa kusimbwa.



Ili kufikia data yetu, tunahitaji kusimbua kwa kutumia Picocrypt.



![Image](assets/fr/023.webp)



Kabla ya kuzungumza juu ya usimbuaji wa data, hapa kuna habari kuhusu baadhi ya chaguo zinazopatikana:





- Hali ya Paranoid**: tumia kiwango cha juu zaidi cha usalama kinachotolewa na Picocrypt. Chombo hiki kitatumia algoriti kadhaa za usimbaji fiche (XChaCha20 na Serpent) na HMAC-SHA3 badala ya BLAKE2b kwa uthibitishaji wa data.
- Reed-Solomon**: tumia *Reed-Solomon* misimbo ya kurekebisha makosa ili kuwezesha urekebishaji wa makosa kwenye data iliyoharibika. Hii hukuruhusu kuauni kiwango cha ufisadi cha karibu 3% ya faili yako.
- Gawanya katika vipande** au **gawanya katika sehemu kadhaa**: ikiwa unasimba faili kubwa kwa njia fiche, unaweza kuomba Picocrypt iligawanye katika sehemu kadhaa. Hii inaweza kurahisisha kuhamisha faili.
- Finya faili** au **Finya faili**: finya faili ili kupunguza ukubwa wa faili zilizosimbwa.
- Faili zilizofutwa ** au **Fichiers supprimés**: futa faili za chanzo ili kuweka toleo lililosimbwa pekee



### B. Kusimbua data kwa kutumia Picocrypt



Ikiwa unahitaji kusimbua data, sio ngumu zaidi kuliko kuisimba kwa njia fiche. Fungua kwa urahisi Picocrypt na **buruta na udondoshe faili ya PCV ili kusimbwa**. Kisha ingiza nenosiri na/au chagua faili muhimu kabla ya kubofya "** Decrypt**".



![Image](assets/fr/021.webp)



Toleo lisilosimbwa la kumbukumbu ya ZIP ya "Encrypted.zip" sasa inaniruhusu kurejesha faili zangu mbili katika maandishi wazi!



![Image](assets/fr/022.webp)



## IV. Hitimisho



**Umeonywa: Picocrypt ni rahisi sana kutumia, na inafanya kazi! Ingawa Interface ni ndogo, inajumuisha chaguzi muhimu sana za kubinafsisha usimbaji fiche! Na kwa kuwa inapatikana katika toleo linalobebeka, unaweza kwenda nayo popote unapoenda, ili uweze kusimbua data yako kwa kujiamini**



Hakikisha kuwa unatumia manenosiri thabiti ili kulinda data, na ukitumia faili muhimu, ni lazima ukumbuke kuihifadhi, vinginevyo hutaweza tena kusimbua kontena la PCV linalozalishwa na Picocrypt. Hatimaye, unapaswa kujua kwamba pia kuna [toleo la CLI](https://github.com/Picocrypt/CLI) (yenye vipengele vichache) ambalo hukuwezesha kuendesha Picocrypt kutoka kwa safu ya amri: hapa tena, Picocrypt inafungua mlango wa uwezekano mpya.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5