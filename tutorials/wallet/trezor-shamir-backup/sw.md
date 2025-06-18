---
name: Hifadhi Nakala ya Trezor Shamir
description: Vifungu vya kushiriki mara moja na vya kushiriki vingi vya Mnemonic kwenye Trezor
---
![cover](assets/cover.webp)



*Salio la picha: [Trezor.io](https://trezor.io/)*



## Chaguo mpya za chelezo kwenye Trezor



Tangu 2023, Trezor imekuwa ikitoa umbizo jipya la hifadhi rudufu inayoitwa ***Hifadhi Nakala ya Shiriki Moja***, ikichukua nafasi ya mbinu ya msingi ya BIP39 inayopatikana kwenye portfolio nyingi. Tofauti na vishazi vya kimapokeo vya Mnemonic vyenye maneno 12 au 24, umbizo hili jipya linatokana na kishazi kimoja cha maneno 20 kinachotokana na kiwango kilichotengenezwa na SatoshiLabs: **SLIP39**. Kusudi ni kuboresha uimara na usomaji wa chelezo, huku kuwezesha uhamiaji laini hadi muundo wa chelezo uliosambazwa.



Muundo huu uliosambazwa unaitwa ***Hifadhi Nakala nyingi za kushiriki***. Inategemea kanuni hiyo hiyo, lakini badala ya kutoa kifungu kimoja cha Mnemonic, inaigawanya katika vipande kadhaa vinavyoitwa *** hisa ***, ambayo kila moja ni maneno ya Mnemonic kwa haki yake mwenyewe. Ili kurejesha kwingineko, idadi fulani ya *hisa* hizi (iliyofafanuliwa na *kizingiti*) lazima iunganishwe tena. Kwa mfano, katika mpango wa 3-kati-5, *hisa* 3 zozote kati ya 5 zitarejesha kwingineko. Tafadhali kumbuka kuwa mfumo wa chelezo uliosambazwa wa Trezor ni tofauti na pochi za Multisig. Ili kutumia bitcoins zako, Hardware Wallet Trezor yako pekee inahitajika. Sahihi moja tu inahitajika. Usambazaji unatumika tu katika kiwango cha maneno ya Mnemonic, yaani chelezo.



![Image](assets/fr/01.webp)



Mfumo huu hutatua tatizo la hatua moja ya kushindwa kwa maneno ya Mnemonic bila hasara zinazohusiana na kusimamia Multisig au passphrase BIP39. Mchakato wa kurejesha hautegemei tena kipande kimoja cha habari, lakini kwa kadhaa, na faida iliyoongezwa ya shukrani ya uvumilivu wa hasara kwa kizingiti.



Watumiaji ambao wameunda jalada kwa kutumia *Hifadhi Nakala ya Shiriki Moja* wanaweza kubadili hadi *Hifadhi Nakala nyingi za Kushiriki* wakati wowote bila kulazimika kuhamisha jalada lao. Anwani na akaunti zinazopokea zitasalia kuwa sawa. Mfumo wa *Shiriki nyingi* huathiri tu hifadhi rudufu, huku kwingineko iliyosalia ikiwa haijabadilishwa.



Hifadhi Nakala ya Ushiriki mwingi* inapatikana kwenye Trezor Model T, Safe 3 na Safe 5. Kipengele hiki hakitumiki na Trezor Model One.



**Dokezo muhimu:** Mfumo wa Trezor wa *Shiriki nyingi* ni salama kwa njia fiche, kwani hutumia *mpango wa Kushiriki Siri ya Shamir* kwa usambazaji. Tunashauri sana dhidi ya kutumia mfumo sawa na wewe mwenyewe, kwa kugawanya maneno ya kawaida ya Mnemonic wewe mwenyewe. Ni mazoea mabaya ambayo huongeza sana hatari ya wizi na upotezaji wa bitcoins zako, kwa hivyo usifanye hivyo. Neno la kawaida la Mnemonic limehifadhiwa kwa ukamilifu.



## Kushiriki kwa Siri ya Shamir katika SLIP39



Utaratibu wa kriptografia unaotokana na hifadhi rudufu za *Kushiriki kwa wingi* kwenye Trezor ni *Mpango wa Kushiriki kwa Siri wa Shamir* (SSSS). Kanuni yake ni kama ifuatavyo: habari ya siri (katika kesi hii, seed ya kwingineko) inabadilishwa kuwa polynomial ya hisabati. Pointi kadhaa za polynomial hii huhesabiwa, ambayo kila moja inakuwa sehemu. Siri ya asili inajengwa upya na tafsiri ya polynomial, kwa kukusanya idadi ndogo ya pointi (kizingiti).



Hakuna habari ya siri inayoweza kutolewa kutoka kwa idadi ya hisa chini ya kizingiti, ikihakikisha usalama kamili wa kinadharia wa habari ya siri. Kwa maneno mengine, hata mshambuliaji aliye na nguvu isiyo na kikomo ya kompyuta hawezi kukisia seed ikiwa kizingiti hakijafikiwa.



SLIP39 hutumia mpango huu kusambaza kwingineko ya seed. Kila hisa ni sentensi ya maneno 20, iliyojengwa kutoka kwa orodha ya maneno 1024 (tofauti na orodha ya BIP39).



## Kuweka Hifadhi Nakala ya Kushiriki nyingi kwenye Trezor



Wakati wa kuunda kwingineko yako kwenye Trezor, una chaguzi tatu tofauti:




- Tumia kifungu cha kawaida cha BIP39 Mnemonic cha maneno 12 au 24;
- Tumia maneno ya sehemu moja ya Mnemonic (SLIP39);
- Sanidi vifungu vingi vya maneno ya Mnemonic katika Ushiriki mwingi (SLIP39).



Ukichagua kifungu cha maneno ya SLIP39 Mnemonic ya kushiriki-Single, utaweza kupata toleo jipya la Shiriki nyingi baadaye bila kulazimika kuweka upya kwingineko. Kwa upande mwingine, ukianza na kwingineko ya kawaida ya BIP39 (maneno ya maneno 12- au 24), hutaweza kuibadilisha moja kwa moja hadi Sehemu nyingi. Itabidi uunde kwingineko mpya ya Ushirikiano Wengi kutoka mwanzo na kuhamisha fedha zako kutoka kwingineko ya zamani hadi mpya kupitia shughuli moja au zaidi za Bitcoin. Hii ni operesheni ngumu zaidi na ya gharama kubwa. Ikiwa ungependa kufanya uhamaji huu, ninapendekeza ununue Trezor mpya ya Hardware Wallet ili kuepuka kuingia kwenye seed yako kwenye programu ya kwingineko.



Katika somo hili, kwanza tutaangalia jinsi ya kusanidi Ushiriki mwingi wakati wa kuunda kwingineko, kisha, katika sehemu inayofuata, tutaona jinsi ya kubadilisha Ushiriki Mmoja hadi Ushiriki mwingi kwenye kwingineko iliyopo.



Iwapo unahitaji usaidizi kuhusu usanidi wa awali wa kifaa chako, pia tuna mafunzo ya kina kwa kila modeli ya Trezor:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Kwenye kwingineko mpya



Sasa umekamilisha usanidi wa awali wa Trezor yako na uko tayari kuunda kwingineko. Katika Trezor Suite, bofya kitufe cha "*Unda Wallet* mpya".



![Image](assets/fr/02.webp)



Chagua chaguo la "*Hifadhi Nakala nyingi", kisha ubofye "*Unda Wallet*".



![Image](assets/fr/03.webp)



Kubali sheria na masharti kwenye Trezor yako na uthibitishe uundaji wa kwingineko.



![Image](assets/fr/04.webp)



Katika Trezor Suite, bofya "*Endelea kuhifadhi nakala*".



![Image](assets/fr/05.webp)



Soma maagizo kwa uangalifu, yathibitishe, kisha ubofye "*Unda nakala rudufu ya Wallet*".



![Image](assets/fr/06.webp)



Kwa maelezo zaidi kuhusu njia sahihi ya kuhifadhi na kudhibiti vifungu vyako vya Mnemonic, ninapendekeza sana kufuata mafunzo haya mengine, hasa kama wewe ni mwanzilishi:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Kwenye Trezor, chagua jumla ya idadi ya hisa unazotaka kusanidi. Mipangilio ya kawaida ni 2-de-3 na 3-de-5. Kwa mfano huu, nitaunda 2-de-3, kwa hivyo nitachagua hisa 3. Kila hisa itawakilisha maneno 20 ya Mnemonic.



*Kwa watumiaji 5 Salama, ingawa skrini itasema "*Gusa ili kuendelea*", utahitaji kutelezesha kidole juu ili kuthibitisha.



![Image](assets/fr/07.webp)



Kisha uthibitishe kizingiti, yaani, idadi ya hisa zinazohitajika ili kurejesha upatikanaji wa Wallet na bitcoins zilizomo.



![Image](assets/fr/08.webp)



Trezor itaunda hisa zako mbalimbali (maneno ya Mnemonic) kwa kutumia jenereta yake ya nambari nasibu. Hakikisha hutazamwa wakati wa operesheni hii. Andika maneno yaliyotolewa kwenye skrini kwenye nyenzo ya asili ya chaguo lako. Ni muhimu kuweka maneno kwa nambari na kwa mpangilio.



Ninapendekeza kwamba uandikie kila hisa kwenye chombo tofauti na udhibiti kwa uangalifu hifadhi yao ili kuepuka kadhaa kupatikana katika sehemu moja. Kwa mfano, kwa usanidi wa 2-kati-3 kama yangu, chaguo moja litakuwa kuweka hisa moja nyumbani kwangu, nyingine na rafiki ninayemwamini, na ya mwisho kwenye sefu ya benki. Uchaguzi wa maeneo ya kuhifadhi utategemea mkakati wako wa usalama wa kibinafsi.



Unaweza kuona sehemu ya juu ya skrini ambayo unatazama kwa sasa.



bila shaka, hupaswi kamwe kushiriki maneno haya kwenye Mtandao, kama ninavyofanya katika mafunzo haya. Mfano huu Wallet itatumika kwenye Testnet pekee na itafutwa mwishoni mwa mafunzo.**_



![Image](assets/fr/09.webp)



Ili kuendelea na maneno yanayofuata, bofya sehemu ya chini ya skrini. Unaweza kurudi nyuma kwa kuteleza chini. Mara tu unapoandika maneno yote, weka kidole chako kwenye skrini ili kuendelea na sehemu inayofuata, na kurudia operesheni.



![Image](assets/fr/10.webp)



Mwishoni mwa kila rekodi ya kushiriki, utaombwa kuchagua maneno katika maneno yako ya Mnemonic ili kuthibitisha kuwa umeyaandika kwa usahihi.



![Image](assets/fr/11.webp)



Na ndivyo ilivyo, umefaulu kuweka nakala rudufu yako kwa kutumia chaguo la Kushiriki Multi. Sasa unaweza kuendelea na maagizo mengine ya usanidi.



### Kwenye kwingineko iliyopo ya kushiriki moja



Iwapo tayari una Trezor Wallet iliyo na hifadhi rudufu ya sehemu moja (maneno ya SLIP39 Mnemonic, si maneno ya kawaida ya BIP39), na ungependa kuboresha upatikanaji na usalama wa chelezo yako ya Wallet, unaweza kusanidi mfumo wa kushiriki zaidi bila kulazimika kuhamisha bitcoins zako.



Ili kufanya hivyo, unganisha na ufungue Hardware Wallet yako. Katika Trezor Suite, nenda kwa Mipangilio.



![Image](assets/fr/12.webp)



Nenda kwenye kichupo cha "*Kifaa*".



![Image](assets/fr/13.webp)



Kisha bofya kwenye "* Unda Hifadhi Nakala ya Kushiriki nyingi *".



![Image](assets/fr/14.webp)



Soma maagizo, kisha ubofye kwenye "*Unda Hifadhi Nakala ya Ushiriki Wengi*".



![Image](assets/fr/15.webp)



Kisha utahitaji kuingiza maneno yako ya sasa ya Mnemonic (shiriki-moja) kwenye skrini yako ya Trezor. Chagua idadi ya maneno (chaguo-msingi ni 20).



![Image](assets/fr/16.webp)



Kisha utumie kibodi ya skrini ya Trezor ili kuweka kila neno la maneno yako ya sasa ya Mnemonic.



![Image](assets/fr/17.webp)



Kisha unaweza kuchagua usanidi wa Hifadhi Nakala yako ya Kushiriki nyingi kwa kufuata maagizo yaliyotolewa katika sehemu iliyotangulia.



![Image](assets/fr/18.webp)



Mara tu unapounda Hifadhi Nakala yako ya Ushiriki mwingi, utahitaji kuamua cha kufanya na maneno yako ya asili ya Mnemonic ya Ushiriki Mmoja. Kwa vile kwingineko ya Bitcoin inabaki vile vile, kifungu hiki cha maneno kitaruhusu ufikiaji wake kila wakati. Hii itategemea mkakati wako wa usalama, lakini kwa ujumla, inashauriwa kuharibu kifungu hiki ili kuondoa hatua hii moja ya kutofaulu, ambayo ndio lengo haswa la Hifadhi nakala rudufu. Ukiamua kuiharibu, hakikisha unafanya hivyo kwa usalama, kwani **bado inatoa ufikiaji wa bitcoins zako**.



Hongera, sasa umeboresha utumiaji wa Hifadhi Nakala za Kushiriki Moja na Ushiriki mwingi kwenye pochi za maunzi za Trezor. Ikiwa ungependa kupeleka usalama wako wa Wallet hatua zaidi, angalia mafunzo haya kwenye kaulisiri za BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Ikiwa umepata mafunzo haya kuwa ya manufaa, ningeshukuru ikiwa utaacha kidole gumba cha Green hapa chini. Jisikie huru kushiriki nakala hii kwenye mitandao yako ya kijamii. Asante sana!



## Rasilimali za ziada





- [SLIP-0039: Kushiriki kwa Siri ya Shamir kwa Misimbo ya Mnemonic](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Hifadhi Nakala nyingi kwenye Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Kushiriki kwa siri kwa Shamir](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).