---
name: Electrum Airgap
description: Hatua ya kwanza kuelekea usalama, cold wallet na Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



Katika somo hili nitaeleza jinsi ya kutengeneza kifaa chako cha kwanza cha kusaini kwenye airgap, kikitengwa na mtandao, hata bila kuwa na Hardware Wallet maalum. Unachohitaji ni kuwa na kompyuta mbili zinazopatikana:




- kifaa cha zamani cha kilichokatishwa kabisa kutoka kwenye mtandao;
- kompyuta unayotumia kila siku.



Usanidi huu unaruhusu kiwango kikubwa cha usalama kuliko `Hot Wallet` ya kawaida: kompyuta ya zamani--bila muunganisho wa mtandao--ndio mlinzi wa funguo zako za faragha, ambazo hazijafichuliwa kamwe kwenye mtandao, lakini huhifadhiwa nje ya mtandao ("airgap" au "Cold").



Badala yake, utaweka maonyesho ya Wallet ("kutazama tu") kwenye kompyuta yako ya kila siku, ambayo imeunganishwa kwenye mtandao na ambayo unaweza, kwa mfano, kuangalia mizani na kuandaa shughuli za kupokea.



## Wallet Airgap: Nini na Jinsi



Kwa kutekeleza hatua katika mwongozo huu, tutasakinisha Software Wallet Electrum mbili kwenye kompyuta mbili tofauti na hatimaye kuunda Wallet mbili zilizo na vitufe tofauti: Wallet airgap itatumia safu nzima ya Wallet HD, huku onyesho la Wallet litatolewa kwa ufunguo mkuu wa umma.



Wallet hizi mbili zitakuwa, kwa njia zote, tofauti sana kutoka kwa kila mmoja. Kitu pekee ambacho watakuwa nacho kwa pamoja, kama tutakavyoona, ni anwani:




- gW-13 kwenye kompyuta ya airgap inaweza tu kusaini lakini, kukatwa kutoka kwa mtandao, haijui usawa na anwani zinazotumiwa;
- Wallet kwenye kompyuta ya kila siku itaweza tu kuandaa na kueneza shughuli, bila kuwa na uwezo wa kuondoa matumizi, kwa kutokuwepo kwa funguo za kibinafsi.



## Maandalizi ya Awali



Ili kupakua Electrum, ninapendekeza ufuate hatua za kwanza kwenye somo hili:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Baada ya kupakua kila mara thibitisha toleo kabla ya kulisakinisha, kisha endelea na usanidi wa "Seva Moja", kama utakavyopata katika sehemu ya usaidizi, chini ya `Anza na Dummy Wallet`.



Operesheni ya usanidi wa "Seva Moja" ni muhimu tu kwa Wallet iliyowekwa kwenye kompyuta ya kila siku, kwani kompyuta nyingine itakuwa nje ya mtandao daima.



Shughuli zifuatazo zinahusisha kufanya mazoezi kwenye kompyuta mbili tofauti (na Wallet), kwa urahisi na kuzingatia-nilichagua kuweka nafasi ya anga ya Wallet yenye mandhari nyepesi, huku onyesho la Wallet lina mandhari meusi.



## Uundaji wa Airgap ya Wallet



Baada ya kupakua na kuthibitisha upakuaji wa Electrum, chukua nakala ya inayoweza kutekelezwa na uilete kwenye kompyuta yako nje ya mtandao. Kisha uzindua na usakinishe Electrum.



Bofya mara mbili ili kuanza Electrum: kompyuta ambapo utatumia Wallet hii iko nje ya mtandao, puuza mipangilio ya mtandao na uende kwenye uundaji wa Wallet ambayo, katika mwongozo huu, tutaita `airgap`.



![image](assets/en/01.webp)



Chagua _Wallet ya kawaida_.



![image](assets/en/02.webp)



Na kisha chagua _Create new seed_ ili kuwa na programu ya generate the Mnemonic.



![image](assets/en/03.webp)



Nakili kwa usahihi maneno 12 ya generate kutoka kwa Electrum hadi kwenye usaidizi wa karatasi na uendelee na hatua ya uthibitishaji, ukiingiza tena maneno kwa mpangilio wakati Electrum inapoiomba.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Baada ya uundaji wa Wallet kukamilika, weka nenosiri changamano (`Strong`) ili kusimba faili ya Wallet kwa njia fiche kwenye kifaa cha airgap. Hatua hii ni nyeti sana na ni muhimu, kwani nenosiri lililochaguliwa sasa, huzuia ufikiaji wa Wallet ambayo ina uwezo wa kutoweka, kuwa na uwezo wa kutumia shughuli za kusaini pesa.



![image](assets/en/06.webp)



Kwa kubofya _Finish_ Wallet inafafanuliwa na inaonekana kwenye skrini. Bila shaka, kiashiria cha uunganisho wa mtandao, yaani, dot ya rangi kwenye kona ya chini ya kulia, ni nyekundu, kwani kompyuta imekatwa na hairuhusu Wallet kufichua funguo za mtandaoni.



![image](assets/en/07.webp)



## Uundaji wa Wallet wa Taswira



Kwa kuwa Wallet yako ina funguo za faragha za nje ya mtandao, unahitaji kusanidi onyesho la Wallet, au `watch-only`, ambalo litakuruhusu kuona salio, na pia kuandaa miamala ya kupokea risiti ili kuendelea kukusanya Sats kwa usalama.



Kutoka kwa Wallet iliyo kwenye kifaa cha nje ya mtandao, chagua _Wallet_ -> _Maelezo_ menyu



![image](assets/en/08.webp)



Dirisha lenye maelezo yako yote ya Wallet litaonekana, ambapo unaweza kuangalia `njia ya utokaji` na `alama kuu ya vidole`, kwa mfano kuziweka alama kando ya maneno katika sentensi ya Mnemonic (inapendekezwa sana).



![image](assets/en/09.webp)



Kumbuka kwamba unachukua data hii kutoka kwa kompyuta ambayo haijaunganishwa, kwa hivyo itabidi unakili/ubandike `zpub` kwenye faili ya maandishi na uihifadhi kwenye kijiti cha usb.



Sasa unaweza kuhamia kwenye kompyuta iliyounganishwa kwenye mtandao, ili kuzindua Electrum na kuunda Wallet mpya.



Kutoka kwa menyu ya _Faili_, chagua _Mpya/Rejesha_.



![image](assets/en/10.webp)



Wallet mpya ni ya kutazama tu, kwa hivyo kwa mwongozo huu tutaiita `kutazama tu`.



![image](assets/en/12.webp)



Kwenye skrini inayofuata chagua _Standard wallet_ na uendelee kwa kubofya _Next_.



![image](assets/en/13.webp)



Katika kuchagua `Keystore` kuwa mwangalifu: kuunda onyesho la Wallet chagua _Tumia kitufe kikuu_. Kisha endelea na _Next_.



![image](assets/en/14.webp)



Bandika hapa `zpub` iliyonakiliwa kutoka kwa Wallet nje ya mtandao na ambayo umeleta kwenye kompyuta hii kupitia usb media.



![image](assets/en/15.webp)



Hitimisha kwa kuweka nenosiri dhabiti la Wallet hii pia, ikiwezekana kuwa tofauti na lile lililochaguliwa kwa Cold yake inayolingana.



Utaona onyesho la Wallet linaonekana, na onyo. Ujumbe unakukumbusha kuwa hii ni Wallet ya kuonyesha pekee na kwamba huwezi, nayo, kutumia pesa zinazohusiana.



**Kumbuka Vizuri**: **kwa hivyo utahitaji kuwa na funguo za faragha kila wakati ili kuondoa UTXO za Wallet** hii. Ukiwa na mfumo mzuri wa chelezo, haitakuwa vigumu kwako kubaki umiliki kamili wa Bitcoins zako.



![image](assets/en/16.webp)



Onyo hili litaonekana kila mara unapofungua Wallet hii. Bofya _Ok_ na tuendelee hadi hatua ya uthibitishaji.



## Uthibitishaji wa Wallet Mbili



Kama tulivyojifunza mwanzoni mwa mwongozo huu, Wallet airgap na onyesho lake la Wallet ni portfolios mbili ambazo zina fani tofauti lakini **zinashiriki anwani sawa**.



Ikiwa tunatazama Wallet mbili kwa upande, kwa kuibua tunagundua kuwa kwenye nafasi ya hewa ya Wallet kuna alama ya "seed", wakati kwenye saa-pekee haipo. Hata maelezo haya yatakusaidia kukumbuka kuwa onyesho la Wallet Wallet haina funguo za kibinafsi.



![image](assets/en/17.webp)



Ili kufanya ukaguzi sahihi wa kwanza, hata hivyo, chagua katika Wallet zote menyu ya `Anwani`: kwa kuwa zinashiriki anwani sawa, orodha ya anwani inapaswa kufanana kwa zote mbili.



![image](assets/en/18.webp)



âš ï¸ **ANGALIZO**: **hakuwezi kuwa na msingi wa kati; anwani lazima ziwe sawa. Ikiwa ni tofauti, ni muhimu kufuta kazi yote iliyofanywa hadi sasa na kuanza tena **.



Sasa unaweza kuendelea kufanya ukaguzi mbili tofauti. Kwanza, jaribu kufuta Wallet mbili na kuzirejesha kutoka mwanzo, kila moja kwenye kompyuta inayofaa. Iwapo utaendelea kufanya uthibitishaji huu, taratibu za kuonyesha Wallet ni sawa na zile zilizoelezwa hapo juu.



Kwa Wallet airgap, hata hivyo, kwenye skrini ya `keystore` itabidi uchague _tayari nina Seed_ na uweke maneno kwa kuyanakili kutoka kwenye nakala yako ya karatasi.



Baada ya jaribio la "hakuna mzigo" limekwisha, unaweza kujaribu kufanya shughuli ya kiasi kidogo na kuitumia mara moja.



## Miamala ya Kupokea na Kutumia



Ili kuanza kutumia Airgap yako ya Electrum, unaweza kufanya muamala wa risiti kwa kiasi kidogo, kisha uitumie kuelekea Address yako mwenyewe. Kisha unaweza kujitambulisha na utaratibu, kuthibitisha kuwa una udhibiti kamili wa fedha.



**Kumbuka**: Sipendekezi uweke kiasi kikubwa cha fedha kwenye Wallet kabla ya kuwa na uhakika kwamba unaweza kufanya shughuli zote kwa urahisi.



Hatua zilizoelezwa hapo chini zinaweza, kwa mtazamo wa kwanza, kuonekana kuwa ngumu. Usiruhusu hili likukatishe tamaa: unapokuwa umewajaribu mara ya kwanza, utaona kwamba watachukua dakika chache tu kukamilisha.



Ili kupokea pesa, lazima utumie onyesho la Wallet lililo kwenye kompyuta yako iliyounganishwa kwenye mtandao. Kutoka kwenye menyu ya `Pokea` bofya _Unda ombi_ ili kuwa na Electrum generate ya kwanza inayopatikana ya Address na uitumie kututumia Satss chache.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Baada ya shughuli hiyo kuenezwa unaweza kuona kuwa-kama ilivyo kawaida- inaonekana tu kwenye onyesho la Wallet na si kwenye nafasi ya anga ya Wallet.



![image](assets/en/21.webp)




Baada ya muamala wako kupokea uthibitisho fulani, unaweza kuandaa gharama na hivyo kujaribu utaratibu wa kutia sahihi kutoka kwa Wallet nje ya mtandao. Kisha tayarisha muamala kwenye saa pekee na ubonyeze _Preview_ ili kuikagua


![image](assets/en/22.webp)



Unapata dirisha la juu la ununuzi ambapo unaweza kuona kwamba:




- muamala haujatiwa saini (`Hali: Haijatiwa saini);
- Amri za `Saini` na `Tangaza` zimezuiwa.



Kitu pekee unachoweza kufanya ni kusafirisha muamala kama ulivyo, kuipeleka kwa Wallet airgap na kusaini.



Tambulisha kiendeshi cha USB flash kwenye kompyuta yako na, kutoka kwenye menyu iliyo chini kushoto, chagua _Shiriki_.



![image](assets/en/23.webp)



Baada ya hapo chagua _Hifadhi kwa faili_.



![image](assets/en/24.webp)



Hifadhi muamala kwenye kifimbo cha usb.



Utagundua kuwa Electrum inaipa faili jina lenye tarakimu za kwanza za transaction ID, na kiendelezi cha faili ni `.PSBT`, kumaanisha `Partially Signed Bitcoin Transaction`.



Chapa midia kwa faili `.PSBT` na uiunganishe na kompyuta nje ya mtandao.



Kutoka kwa Wallet airgap, sasa chagua menyu ya _Tools_, kisha _Pakia muamala_ na ufuate Kutoka faili_.



![image](assets/en/25.webp)



Ukiwa na kidhibiti faili, chagua `.PSBT` kutoka eneo lake.



![image](assets/en/29.webp)



Programu ya kompyuta ya nje ya mtandao itafungua kiotomatiki kidirisha cha juu cha muamala, sawa kabisa na jinsi ulivyoiona kwenye onyesho la Wallet. Hali ni `Haijasainiwa`, lakini tofauti ni kwamba amri ya `Ishara` hapa inafanya kazi. Na hiyo ndio hasa utalazimika kutekeleza.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Kwa kuwa sasa muamala umetiwa saini, kumbuka kuwa Wallet yako iko kwenye mashine ya nje ya mtandao. Kwa hivyo-hata ukiona amri ya `Broadcast` inafanya kazi-Wallet yako haitaweza kueneza muamala kwa mtandao wa Bitcoin.



Unachohitaji kufanya sasa ni kurudia utendakazi wa kusafirisha muamala uliotiwa saini kwenye kijiti cha usb, ili uweze kuiingiza kwenye kompyuta iliyounganishwa kwenye mtandao na kuieneza.



Kutoka kwenye menyu ya chini kushoto, chagua _Shiriki_ tena kisha _Hifadhi kwenye faili_.



![image](assets/en/28.webp)



Sasa faili ina kiendelezi tofauti: **badala ya `.PSBT` sasa muamala una kiendelezi `.txn`**. Kuanzia sasa hivi ndivyo Electrum itakuruhusu kutambua miamala iliyotiwa saini kutoka kwa wale ambao hawajasaini.



![image](assets/en/30.webp)



Kwa uenezi wa mwisho wa shughuli, chukua fimbo ya usb nje ya kompyuta ya nje ya mtandao na uiingiza kwenye kompyuta iliyounganishwa kwenye mtandao.



Kutoka kwa saa pekee, rudia utaratibu wa kuingiza, yaani, kutoka kwa menyu ya _Tools_ chagua _Pakia muamala_ na hatimaye _Kutoka kwenye faili_.



![image](assets/en/31.webp)



Electrum itakufungulia dirisha la muamala, tofauti kabisa na lile lililoonyeshwa hapo awali kwenye Wallet hii, kwa kuwa sasa imetiwa saini (`Hali: Imetiwa Saini`) na amri ya `Broadcast` kupatikana.



Operesheni ya mwisho unayohitaji kufanya ni hii tu:



![image](assets/en/32.webp)



## Hitimisho



Majaribio yako sasa yamekamilika. Ikiwa ulifuata mwongozo na kupata matokeo sawa, umeunda Wallet Cold na Electrum, kwenye kompyuta mbili tofauti, ambazo unaweza kutumia kwa mtindo wa airgap kuhifadhi Bitcoins zako.



Vitu pekee ambavyo utalazimika kuzingatia kwa karibu ni viwili:


1) **kamwe usitumie airgap ya Wallet kwa Address za kupokea za generate**. Kwa kuwa iko nje ya mtandao, itakupa Address ya kwanza kila wakati, ambayo inalingana na ile uliyotumia kufanya muamala wa majaribio;



![image](assets/en/33.webp)



_Kama unavyoona kwenye picha iliyo hapo juu, Wallet ya nje ya mtandao haijui historia yake ya Address. Ni kipofu kabisa katika suala hili. **Kazi pekee inayoweza kukufanyia ni kuhifadhi funguo zako za nje ya mtandao na kutia sahihi katika miamala yako**_.



2) Tumia kiendeshi cha USB flash kilichotolewa kwa madhumuni haya tu, **usitumie njia unayotumia mara kwa mara**. Zana za kila siku zina uwezekano mkubwa wa kushambuliwa na mtandao, na bila kukusudia, unaweza kushambulia hata kompyuta unayoweka ikiwa imetenganishwa na mtandao. Kijiti cha USB ambacho unatumia kwa madhumuni haya pekee kina fursa chache sana za kuwasiliana na Kompyuta yako mtandaoni, hasa ikiwa wewe ni mtu anayeendesha gari ambaye huhitaji kutumia, hivyo kupunguza uwezekano wa kupokea na kusambaza virusi, programu hasidi, n.k.
