---
name: Mpango wa urithi Bitcoin
description: Jinsi ya kuhamisha bitcoins kwa wapendwa wako
---

![cover](assets/cover.webp)



Usambazaji wa bitcoins unawakilisha changamoto kubwa ya kiufundi ambayo wamiliki wengi hupuuza. Tofauti na mali za benki za kitamaduni, ambapo taasisi ya kifedha inaweza kuwasilisha fedha hizo kwa wamiliki halali, Bitcoin inafanya kazi bila wapatanishi. Wapendwa wako hawataweza kamwe kupata fedha zako bila taarifa muhimu za kiufundi, bila kujali uhalali wao wa kisheria.



Mafunzo haya yanakuongoza katika uundaji wa mpango wa kiufundi wa urithi. Utajifunza jinsi mifumo ya on-chain ya uwasilishaji otomatiki inavyofanya kazi, jinsi ya kurekodi usanidi wako, na jinsi ya kuchagua suluhisho sahihi ili kuhakikisha kuwa urithi wako wa Bitcoin unaendelea kufikiwa na wapendwa wako.



## Kwa nini mpango wa urithi wa kiufundi ni muhimu



Bitcoin inategemea kanuni ya msingi ya usimbaji fiche: yeyote anayeshikilia funguo za kibinafsi anadhibiti fedha. Uhuru huu unakuwa udhaifu mkubwa wakati mmiliki anapotea bila kusambaza taarifa muhimu.



Mpango wa urithi wa Bitcoin lazima utimize malengo mawili yanayoonekana kupingana: kuruhusu wapendwa wako kupata fedha zako wakati utakapofika, huku ukimzuia mtu mwingine yeyote kuzipata mapema. Usawa huu maridadi unategemea uwezo asilia wa programu wa Bitcoin.



Ugumu wa kiufundi huongeza ugumu zaidi. Warithi wako watalazimika kubadilisha dhana kama vile misemo ya urejeshaji, maelezo ya kwingineko, au njia za uundaji. Bila maandalizi ya kutosha, hata mrithi mwenye nia njema ana hatari ya kufanya makosa yasiyoweza kurekebishwa.



## Jinsi urithi wa on-chain unavyofanya kazi



Bitcoin hutumia lugha yake ya uandishi wa hati ili kusimba masharti ya matumizi moja kwa moja katika miamala. Urithi wa on-chain hutumia uwezo huu wa upangaji programu kuunda njia mbadala za urejeshaji zinazoamilishwa kiotomatiki.



### Muda wa Kufungwa



Kufunga kwa muda ndio utaratibu wa msingi wa urithi wa Bitcoin. Huwezesha fedha kufungwa hadi sharti la muda litimizwe.



**CLTV (CheckLockTimeVerify)**: Muda huu kamili unaangalia kwamba muda maalum (tarehe au urefu wa kizuizi) umefikiwa kabla ya kuidhinisha matumizi. Kwa mfano, "fedha hizi zinaweza kutumika tu baada ya kizuizi 900000" au "baada ya Januari 1, 2026". Faida ya CLTV ni kwamba inaruhusu ucheleweshaji mrefu (miaka kadhaa), lakini tarehe hiyo imewekwa na inatumika sawa kwa UTXO zote kwenye jalada. Ili kudumisha udhibiti wa fedha zako, lazima uunda jalada jipya mara kwa mara lenye tarehe ya mwisho wa matumizi iliyoongezwa na uhamishe fedha zako kwake.



**CSV (CheckSequenceVerify)**: Muda huu wa kawaida unathibitisha kwamba idadi fulani ya vitalu imepita tangu UTXO ilipoundwa. Kwa mfano, "fedha hizi zinaweza kutumika vitalu 52560 (~mwaka 1) tu baada ya kupokelewa". Faida ya CSV ni kwamba kila UTXO ina kaunta yake huru. Kila wakati unapofanya muamala, UTXO zilizoundwa hivi karibuni huweka kikomo chao cha muda. Hata hivyo, kikomo cha kiufundi cha vitalu 65535 (~ miezi 15 ya juu) huzuia muda unaowezekana. Mbinu hii ni ya kawaida zaidi kwa matumizi ya kila siku, kwani shughuli yako ya kawaida husukuma nyuma tarehe za mwisho kiotomatiki.



### Njia nyingi za matumizi



Kwingineko ya urithi huchanganya njia kadhaa za matumizi katika kila anwani:





- Njia kuu**: Mmiliki anaweza kutumia pesa zake wakati wowote akiwa na ufunguo wake mkuu, bila vikwazo vya muda.
- Njia(njia) ya kurejesha data**: Funguo moja au zaidi mbadala zinaweza kutumia pesa tu baada ya muda uliowekwa kupita.



Kila muamala unaofanywa na mmiliki "huburudisha" UTXO, na kuunda matokeo mapya yenye muda wa kuweka upya. Utaratibu huu unahakikisha kwamba mradi tu mmiliki anaendelea kufanya kazi, njia za urejeshaji hazifanyi kazi kamwe.



### Hati Ndogo na Taproot



**Miniscript** ni lugha iliyopangwa iliyoundwa na Andrew Poelstra, Pieter Wuille na Sanket Kanjalkar ambayo hurahisisha kuandika na kuchanganua hati changamano za Bitcoin. Inakuwezesha kutunga masharti ya matumizi yanayoweza kusomeka na kuthibitishwa, muhimu kwa usanidi wa urithi unaohusisha funguo nyingi na muda wa kufunga.



**Taproot** (iliyoamilishwa mnamo Novemba 2021) inaboresha kwa kiasi kikubwa urithi wa on-chain. Shukrani kwa muundo wake wa mti (MAST), ni hali ya matumizi tu inayotumika ndiyo inayofunuliwa kwenye blockchain. Ikiwa mmiliki anatumia fedha zake kawaida, hali ya urithi hubaki bila kuonekana. Usiri huu pia hupunguza gharama za miamala kwa njia changamano.



## Umuhimu muhimu wa maelezo



Kwa jalada la zamani, kifungu cha urejeshaji (seed) hakitoshi kurejesha ufikiaji wa fedha. **kielezi** kinakuwa kipengele muhimu.



Kielezi ni mfuatano unaoelezea kwa undani muundo wa kwingineko: funguo za umma zinazohusika, hali ya matumizi, njia za uondoaji, na muda uliowekwa. Hapa kuna mfano uliorahisishwa:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Maelezo haya yanasema: "ama ufunguo mkuu unaweza kutumia mara moja, au ufunguo wa kurejesha unaweza kutumia baada ya vitalu 52560".



Hebu tuchambue mfano huu:




- `wsh()` : Hati ya Shahidi Hash, inaonyesha aina ya anwani (P2WSH)
- or_d()`: "au" sharti lenye tawi chaguo-msingi
- pk([alama ya vidole/njia]xpub...)`: Ufunguo mkuu wa umma wenye alama za vidole na njia ya uondoaji
- na_v()`: "na" hali inayochanganya ufunguo wa kurejesha na muda wa kufunga
- `older(52560)`: Muda wa kufuli wa vitalu 52560



**Bila kielezi, hata kwa vifungu vyote vya urejeshaji, warithi wako hawataweza kujenga upya jalada hilo.** Jalada la kawaida linaweza kurejeshwa tu kutoka seed kwa sababu linafuata njia sanifu za uondoaji (BIP44, BIP84). Jalada la zamani, kwa upande mwingine, hutumia hati maalum ambazo haziwezi kukisiwa. Hifadhi nakala rudufu ya kielezi (au faili ya usanidi inayosafirishwa na programu yako) lazima iambatane na vifungu vya urejeshaji katika mpango wako wa urithi.



## Vipengele vya hati vya mpango wa urithi



Zaidi ya mifumo ya kiufundi, mpango wa zamani unaofaa unategemea nguzo tatu za uandishi wa hati.



### Barua ya urithi



Barua hii ya kibinafsi ndiyo sehemu ya kuanzia mpango wako. Imeandikwa kwa ajili ya warithi wako, inaelezea muktadha na tahadhari zinazopaswa kuchukuliwa.



Barua yako lazima ijumuishe sheria dhahiri za usalama:




- Usikimbilie, chukua muda kujifunza kabla ya kuhamisha fedha
- Kamwe usiwasilishe neno kamili la kupona kwa mtu mmoja
- Kamwe usiingize kifungu cha urejeshaji kwenye programu au kompyuta ambayo haijathibitishwa
- Jihadhari na matapeli na watu wanaotoa msaada bila kuombwa
- Tafuta ushauri wa angalau watu wawili unaowaamini kabla ya kufanya uamuzi wowote



Barua hii pia ina maelezo ya mawasiliano ya mthibitishaji wako na eneo la wosia wako. Haipaswi kamwe kuwa na manenosiri au misemo ya kurejesha pesa.



### Saraka ya anwani zinazoaminika



Hakuna mrithi anayepaswa kukabiliana na urejeshaji wa bitcoin peke yake. Saraka hii inaorodhesha watu ambao wanaweza kutoa usaidizi wa kiufundi au kisheria.



Kwa kila mtu unayewasiliana naye, andika: jina kamili, uhusiano na wewe, jukumu katika mpango, kiwango cha uaminifu, ujuzi wa Bitcoin, na maelezo kamili ya mawasiliano. Kanuni ya msingi: warithi wako wanapaswa kushauriana na angalau watu wawili tofauti kabla ya kufanya uamuzi wowote muhimu.



### Hesabu ya mali ya Bitcoin



Sehemu hii inaorodhesha bitcoin zako zote na taarifa za kiufundi zinazohitajika ili kuzirejesha.



Kwa kila kwingineko, hati:




- Aina ya kwingineko**: vifaa, programu, usanidi (sig moja, sig nyingi, legacy)
- Mahali pa kifaa**: eneo halisi la vifaa vya wallet
- Eneo la faili la Descriptor/usanidi**: muhimu kwa jalada za hali ya juu
- Mahali pa kifungu cha urejeshaji**: tofauti na kielezi
- Misimbo ya ufikiaji**: ambapo PIN na manenosiri huhifadhiwa
- Ucheleweshaji uliowekwa**: wakati njia za kurejesha zinapowashwa



## Suluhisho za kiufundi zinapatikana



Vifurushi kadhaa vya programu hutekeleza mifumo ya urithi ya on-chain. Kila moja ina sifa zake za kiufundi.



### Liana



Liana ni programu ya kompyuta (Linux, macOS, Windows) inayotumia Miniscript kuunda jalada zenye njia za urejeshaji zilizopangwa kwa wakati. Mradi huu umetengenezwa na Wizardsardine, iliyoanzishwa kwa ushirikiano na Antoine Poinsot (mchangiaji wa Bitcoin Core).



**Usanifu wa kiufundi**: Liana huunda kwingineko za P2WSH (asili ya SegWit) kwa chaguo-msingi, huku usaidizi wa Taproot ukipatikana kulingana na utangamano wa vifaa vyako vya wallet. Usanifu huo unategemea njia kuu na njia moja au zaidi za urejeshaji. Kielezi kilichozalishwa husimba masharti yote na lazima kihifadhiwe.



**Vizuizi vya muda vilivyotumika**: Liana hutumia vizuizi vya muda vinavyohusiana (CSV), vilivyopunguzwa hadi vitalu 65535 (~ miezi 15). Ili kudumisha udhibiti, lazima ufanye muamala wa kuonyesha upya kabla ya muda wa kufunga muda kuisha.



**Ujumuishaji wa vifaa vya wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY, na vifaa vingine vinaoana kwa ajili ya kusaini miamala.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper ni programu ya simu (iOS, Android) inayochanganya multisig na timelocks kupitia "Enhanced Vaults". Mbinu ya simu yenye mwongozo jumuishi inafanya iweze kufikiwa na watumiaji wachache wa kiufundi.



**Usanifu wa kiufundi**: Vaults Zilizoboreshwa hutumia Miniscript kuunda usanidi wa multisig ambapo funguo za ziada huamilishwa baada ya ucheleweshaji uliobainishwa. Ufunguo wa Urithi huongeza kwenye akidi iliyopo, huku Ufunguo wa Dharura ukiweza kukwepa multisig kabisa.



**Vifungo vya muda vilivyotumika**: Bitcoin Keeper hutumia vifungo vya muda kamili (CLTV), vinavyoruhusu muda wa kuongoza kwa zaidi ya miezi 15. Tarehe ya uanzishaji imewekwa katika uundaji wa wallet na inatumika kwa UTXO zote. Programu inajumuisha kitendakazi cha "kurekebisha" ambacho hudhibiti kiotomatiki usasishaji: mtumiaji hufuata tu hatua zilizoongozwa, bila kulazimika kuunda wallet mpya mwenyewe.



**Vipengele vya ziada**: Nyaraka za urithi zilizojumuishwa, Pochi za Canary ili kugundua maelewano muhimu, na kuonyesha upya vikumbusho.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Urithi



Heritage ni programu ya kompyuta ya mezani inayotumia hati za Taproot kusimba masharti ya urithi. Matumizi ya Taproot hutoa usiri ulioimarishwa, kwa kuwa njia zisizotumika hubaki hazionekani kwenye blockchain.



**Usanifu wa kiufundi**: Kila anwani ya Urithi huunganisha njia kuu na njia mbadala kwa kila mrithi, pamoja na muda unaoendelea. Muundo wa kihierarkia hufanya iwezekane kufafanua nakala rudufu ya kibinafsi akiwa na miezi 6 na warithi wa familia akiwa na miezi 12-15.



**Njia za matumizi**: Toleo la kujitegemea lenye nodi yako mwenyewe (bila malipo) au huduma inayosimamiwa inayoongeza vikumbusho na arifa kwa warithi (0.05%/mwaka).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Mchakato wa kupona kwa mrithi



Kuelewa mchakato wa kupona husaidia kuandaa mpango mzuri. Hapa kuna hatua za kiufundi ambazo mrithi atahitaji kufuata.



### Mahitaji ya kurejesha



Mrithi anahitaji:


1. **Faili ya maelezo au usanidi** wa jalada asilia (JSON au umbizo la maandishi, kulingana na programu)


2. **Kifungu chake cha urejeshaji** (kile kinachohusishwa na ufunguo wake wa urithi, kwa kawaida maneno 12 au 24)


3. **Programu inayooana** (Liana, Bitcoin Keeper, Heritage, au Sparrow/Specter kwa maelezo ya kawaida)


4. **Muunganisho kwenye nodi ya Bitcoin** ili kuangalia hali ya muda wa kufunga na kutangaza muamala



### Hatua za kupona



1. **Sakinisha programu** kwenye kifaa salama na usanidi muunganisho kwenye mtandao wa Bitcoin (nodi ya kibinafsi au seva ya Electrum)


2. **Ingiza kielezi** ili kujenga upya muundo wa kwingineko. Programu itabadilisha kiotomatiki anwani zote zinazotumika kuwa generate


3. **Rejesha ufunguo wa urithi** kutoka kwa kifungu cha urejeshaji. Programu itahakikisha kwamba ufunguo huu unalingana na mojawapo ya funguo zilizoidhinishwa katika maelezo


4. **Sawazisha kwingineko** ili kugundua UTXO zote na masharti ya matumizi yake


5. **Angalia muda wa kufunga muda**: programu itaonyesha kwa kila UTXO ikiwa njia ya kurejesha data inafanya kazi


6. **Unda muamala wa kurejesha** kwa anwani inayodhibitiwa pekee na mrithi (ikiwezekana wallet mpya)


7. **Saini na utangaze** muamala kwenye mtandao wa Bitcoin



Ikiwa muda wa kufunga haujaisha, mrithi atalazimika kusubiri. Programu itaonyesha tarehe au kizuizi ambacho urejeshaji unawezekana. Katika kipindi hiki cha kusubiri, fedha hubaki salama kwenye blockchain.



### Mambo ya kuzingatia kwa mrithi



Mrithi lazima azingatie hasa:




- Angalia uhalisi wa programu iliyopakuliwa** (checksums, sahihi)
- Kamwe usishiriki neno lako la kurejesha uwezo** na mtu yeyote anayetoa msaada
- Wasiliana na angalau watu wawili unaowaamini** kabla ya kufanya uponaji
- Hamisha fedha kwenye jalada rahisi** ambalo anadhibiti kikamilifu baada ya kurejesha pesa.



## Mbinu bora



### Mgawanyiko wa taarifa



Usihifadhi taarifa zote mahali pamoja. Kielezi lazima kitenganishwe na vifungu vya urejeshaji, ambavyo hutenganishwa na misimbo ya PIN. Usambazaji huu unachanganya ufikiaji wa mshambuliaji huku ukibaki unapatikana tena na warithi wako halali.



### Vipimo vya kupona



Kabla ya kuweka pesa nyingi, jaribu mchakato mzima wa urejeshaji kwa kiasi kidogo. Thibitisha kwamba unaweza kurejesha kwingineko kutoka kwa maelezo na vifungu vya urejeshaji kwenye kifaa tupu. Andika hatua kwa warithi wako.



### Matengenezo ya muda



Panga kuburudisha muda wako wa kufunga muda kabla ya muda wake kuisha. Kwa muda wa kufunga muda wa miezi 12, fanya muamala kila baada ya miezi 9-10. Programu kwa kawaida hutoa vikumbusho au vipengele vya kuburudisha kiotomatiki.



### Sasisho la mpango



Usanidi wako wa Bitcoin hubadilika. Kila mabadiliko muhimu (jalada jipya, marekebisho ya tarehe za mwisho, nyongeza ya mrithi) lazima yaonekane katika hati zako. Anzisha utaratibu wa ukaguzi wa kila mwaka.



## Kuchagua mbinu yako



Chaguo kati ya suluhisho tofauti hutegemea wasifu wako wa kiufundi na mahitaji yako mahususi.



**Liana** inafaa kwa watumiaji wa kompyuta za mezani wanaopendelea programu huria yenye udhibiti kamili kupitia nodi yao wenyewe. Usanidi unabaki kupatikana kutokana na kiolesura kinachoongozwa. Muda unaofungwa (CSV) hurahisisha matengenezo, kwani shughuli zako za kawaida huchelewesha muda uliopangwa kiotomatiki. Kizuizi: ucheleweshaji wa juu wa takriban miezi 15 (vizuizi 65535).



**Bitcoin Keeper** inalenga watumiaji wa simu wanaotafuta kiolesura angavu chenye hati zilizounganishwa. Programu hii inatoa aina mbili za ufunguo maalum: Ufunguo wa Urithi (ambao huongeza idadi ya watu wanaohitajika) na Ufunguo wa Dharura (ambao hupita kabisa). Muda kamili wa kufunga (CLTV) huruhusu muda wa kuongoza kwa zaidi ya miezi 15, huku kipengele cha urekebishaji jumuishi kikirahisisha uboreshaji. Mpango wa Diamond Hands hufungua vipengele vya hali ya juu vya zamani.



**Urithi** unalenga watumiaji wa kiufundi wanaothamini usiri wa Taproot na urithi wa kihierarkia pamoja na ucheleweshaji unaoendelea. Muundo wa mti wa Taproot huficha hali za urithi wakati wa miamala ya kawaida, na kufichua tu hali inayotumika wakati wa urejeshaji.



Suluhisho zote tatu zina kitu kimoja kinachofanana: zinahitaji kusasisha mara kwa mara ili kuzuia uanzishaji wa njia za kurejesha mapema. Kizuizi hiki ni bei na dhamana ya urithi usioaminika wa on-chain. Panga vikumbusho vya mara kwa mara na ufanye matengenezo haya kuwa sehemu ya utaratibu wako wa usimamizi wa Bitcoin.



## Hitimisho



Mpango wa kiufundi wa zamani wa Bitcoin unachanganya mifumo ya kriptografia (timelocks, Miniscript, Taproot) na nyaraka kali. Pochi za hali ya juu hukuruhusu kutuma bitcoin zako kiotomatiki baada ya kipindi cha kutofanya kazi, bila kuingilia kati kwa mtu mwingine.



Vipengele muhimu vya kuwapa warithi wako ni: maelezo au faili ya usanidi, kifungu chao cha urejeshaji, maagizo ya kina ya urejeshaji, na maelezo ya mawasiliano ya watu wenye uwezo ambao wanaweza kuwasaidia.



Anza kwa kuchagua suluhisho la kiufundi linalofaa wasifu wako, jaribu kwa kiasi kidogo, kisha uandike yote katika mpango uliopangwa. Ugumu wa awali unahakikisha kwamba mali zako za Bitcoin zitapitishwa kwa siri kamili.



## Rasilimali



### Kiolezo cha mpango wa urithi





- [Kiolezo cha Mpango wa Urithi wa Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Kiolezo cha Nyaraka cha Plan ₿ Academy



### Marejeleo ya kiufundi





- [BIP-65: OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Vipimo vya muda kamili (CLTV)
- [BIP-112: OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Vipimo vya muda unaotumika (CSV)
- [Marejeleo ya Hati Ndogo](https://bitcoin.sipa.be/miniscript/) - Nyaraka rasmi za Hati Ndogo na Pieter Wuille



### Tovuti rasmi za suluhisho





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Urithi Wallet](https://btc-heritage.com/) - Crypto7