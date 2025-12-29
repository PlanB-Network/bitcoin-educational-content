---
name: Urithi
description: Kwingineko ya Bitcoin yenye utaratibu jumuishi wa urithi kupitia hati za Taproot
---

![cover](assets/cover.webp)



Kutoa bitcoins iwapo mtu atakufa au hawezi kufanya kazi ni changamoto kubwa kwa mmiliki yeyote wa mali ya crypto. Bila mpango unaofaa wa urithi, mali hizi haziwezi kurejeshwa kwa wapendwa wako.



Heritage hutoa jibu la kifahari kwa kutekeleza utaratibu wa kubadili mtu aliyekufa moja kwa moja kwenye blockchain ya Bitcoin. wallet hii huria huwezesha masharti ya mfuatano wa on-chain kusanidiwa: ikiwa mmiliki hatafanya miamala zaidi kwa kipindi fulani, funguo mbadala zilizoteuliwa mapema zinaweza kutoa fedha hizo.



## Urithi ni nini?



Heritage ni kwingineko ya Bitcoin inayojumuisha utaratibu wa urithi kupitia hati za Taproot. Iliyotengenezwa chini ya leseni ya MIT na Jérémie Rodon, programu hii huria inahakikisha uwazi na uimara.



Heritage hutumia hati za Taproot zilizosimbwa katika anwani za Bitcoin. Kila UTXO inaunganisha aina mbili za masharti ya matumizi:





- Njia kuu**: Mmiliki anaweza kutumia bitcoin zake wakati wowote akiwa na ufunguo wake mkuu
- Njia mbadala**: Kwa kila mrithi aliyeteuliwa, hati huchanganya ufunguo wake wa umma na muda uliowekwa



Kila muamala wa mmiliki huahirisha kiotomatiki tarehe ya uanzishaji wa vifungu vya urithi. Katika tukio la kutofanya kazi kwa muda mrefu (kifo, kutoweza kufanya kazi), hali hiyo husababishwa kiotomatiki.



## Huduma ya kitamaduni (hiari)



Heritage inatoa chaguzi mbili za matumizi:



**Ifanye mwenyewe (bila malipo)**: Programu huria pekee. Unasimamia kila kitu kwa uhuru ukitumia nodi yako mwenyewe. Chaguo hili hutoa ufikiaji wa chelezo uliojengewa ndani, urithi uliojengewa ndani na udhibiti wa kipekee wa bitcoin zako. Hata hivyo, unahitaji kuunda arifa zako mwenyewe (kalenda, vikumbusho) ili usisahau kusasisha muda wako wa kufungwa, na hakuna arifa otomatiki kwa warithi wako.



**Tumia huduma (0.05% kwa mwaka)** : Huduma ya btc-heritage.com inaongeza vipengele ili kurahisisha usimamizi:




- Vikumbusho otomatiki kabla ya tarehe zako za mwisho kuisha
- Arifa za kiotomatiki kwa warithi ili kuwaongoza katika mchakato wa kurejesha
- Usaidizi wa kipaumbele
- Usimamizi rahisi wa maelezo



Ada: 0.05% ya kiasi kinachosimamiwa kwa mwaka, kiwango cha chini cha 0.5 mBTC/mwaka. Mwaka wa kwanza bila malipo.



Huduma hii bado haijahifadhiwa: funguo zako za kibinafsi hazitoki kamwe kwenye kifaa chako. Heritage haiwezi kufikia pesa zako.



## Urithi wa CLI



Kwa watumiaji wa hali ya juu wanaopendelea kifaa cha kuendeshea kompyuta, Heritage hutoa kifaa cha mstari wa amri (CLI) kwa ajili ya udhibiti wa chembechembe na uendeshaji wa mashine yenye pengo la hewa.



![Page Heritage CLI](assets/fr/03.webp)



Nyaraka kamili za CLI zinapatikana katika [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Hapa utapata maagizo ya kupakua, kuunganisha kwenye huduma, kuunda pochi (zilizo na Ledger au funguo za ndani), kusimamia warithi na miamala.



Mafunzo haya yanalenga programu ya Kompyuta ya Mezani, ambayo inapatikana kwa watumiaji wengi zaidi.



## Eneo-kazi la Urithi



Heritage Desktop ni programu ya michoro yenye kiolesura angavu kinachomwongoza mtumiaji katika kila hatua ya mchakato wa usanidi.



### Pakua



Nenda kwenye [btc-heritage.com](https://btc-heritage.com) na ubofye "Pakua programu".



![Page d'accueil Heritage](assets/fr/01.webp)



Chagua toleo linalolingana na mfumo wako wa uendeshaji (Linux 64bits au Windows 64bits). Binari hazijasainiwa kidijitali, jambo ambalo linaweza kusababisha maonyo ya usalama.



![Page de téléchargement](assets/fr/02.webp)



### Usakinishaji kwenye Linux



Kwenye Linux, programu inasambazwa katika umbizo la AppImage. Kabla ya kuiendesha, unahitaji kusakinisha utegemezi wa `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Kisha fanya faili iweze kutekelezwa na uiendeshe:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Uzinduzi wa kwanza



Katika uzinduzi wa kwanza, mchawi wa uanzishaji unakupa chaguo tatu:



![Onboarding initial](assets/fr/05.webp)





- Sanidi Wallet** ya Urithi: Unda wallet mpya ukitumia mpango wa urithi
- Rithi bitcoin**: Rejesha bitcoin kama mrithi
- Gundua peke yangu**: Gundua vipengele bila usaidizi



Chagua "Sanidi Wallet ya Urithi" ili kuunda wallet yako ya kwanza.



### Muunganisho wa mtandao wa Bitcoin



Chagua jinsi ya kuunganisha kwenye mtandao wa Bitcoin:



![Choix connexion](assets/fr/06.webp)





- Kutumia Huduma ya Urithi**: Miundombinu inayosimamiwa, rahisi zaidi kwa warithi
- Kutumia nodi yangu mwenyewe**: Unganisha kwenye nodi yako mwenyewe ya Bitcoin Core au Electrum



Kwa mafunzo haya, tunatumia nodi yetu wenyewe.



### Usimamizi wa funguo za kibinafsi



Chagua jinsi ya kudhibiti funguo zako za faragha:



![Gestion des clés](assets/fr/07.webp)





- Ukiwa na Kifaa cha Vifaa cha Ledger**: Usalama wa hali ya juu ukiwa na vifaa vya wallet (inapendekezwa)
- Hifadhi ya ndani yenye nenosiri**: Funguo zilizohifadhiwa ndani zenye ulinzi wa nenosiri
- Rejesha wallet** iliyopo: Rejesha kutoka seed iliyopo



### Usanidi wa nodi



Ikiwa unatumia nodi yako mwenyewe, programu inakuongoza kupitia usanidi wake. Hakikisha nodi yako ya Bitcoin au Electrum ni:




- Imewekwa na inaendeshwa
- Imesawazishwa na mtandao wa Bitcoin
- Imesanidiwa kukubali miunganisho ya RPC (kwa Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Bonyeza "Nodi yangu ya Bitcoin inafanya kazi" wakati nodi yako iko tayari.



### Paneli ya hali



Bonyeza "Hali" kwenye kona ya juu kulia, kisha "Fungua Usanidi" ili kufikia vigezo vya muunganisho.



![Panneau Status](assets/fr/09.webp)



Weka URL ya seva yako ya Electrum (k.m. `umbrel.local:50001` ikiwa unatumia Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Uundaji wa wallet



Mara tu muunganisho utakapoanzishwa, bofya "Unda Wallet" kwenye kichupo cha WALLETS.



![Créer wallet](assets/fr/11.webp)



Kidirisha ibukizi kinaelezea usanifu uliogawanyika wa Heritage:



![Architecture split](assets/fr/12.webp)



1. **Mtoa Huduma Muhimu (Nje ya Mtandao)**: Hudhibiti funguo zako za kibinafsi na kusaini miamala. Inaweza kuwa programu ya Ledger au wallet.


2. **Wallet Mtandaoni**: Hushughulikia usawazishaji na mtandao wa Bitcoin, uundaji wa anwani na utangazaji wa miamala.



Jaza fomu ya uundaji:



![Formulaire création wallet](assets/fr/13.webp)





- Jina la Wallet**: Jina la kipekee la kutambua wallet yako
- Mtoa Huduma Funguo**: Chagua Hifadhi ya Funguo ya Karibu kwa mafunzo haya
- Mpya/Rejesha**: Chagua "Mpya" hadi generate na seed mpya
- Idadi ya Maneno**: Maneno 24 yanapendekezwa kwa usalama wa hali ya juu



Ingiza nenosiri thabiti na uchague chaguo za Wallet Mtandaoni:



![Options Online Wallet](assets/fr/14.webp)





- Nodi ya Eneo**: Inatumia nodi yako ya Electrum au Bitcoin Core
- Huduma ya Urithi**: Inatumia huduma ya Urithi (inapendekezwa kwa kazi za arifa)



Bonyeza "Unda Wallet" ili kukamilisha uundaji.



### Interface kutoka wallet



wallet yako sasa imeundwa. Kiolesura huonyesha:



![Interface wallet](assets/fr/15.webp)





- Mizani
- Vitufe vya TUMA na UPOKEE
- Historia ya miamala
- Historia ya usanidi wa urithi
- Anwani za wallet



### Kuunda warithi



Nenda kwenye kichupo cha "WARITHI" ili kuunda warithi wako.



![Page Heirs](assets/fr/16.webp)



Kidirisha ibukizi cha taarifa kinaelezea:




- Warithi ni funguo za umma za Bitcoin zinazohusiana na watu binafsi
- Kila mrithi ana msemo wake wa kukumbuka
- Mrithi wa kwanza anapaswa kuwa "Nyumba ya Kuhifadhi" kwako mwenyewe (ikiwa utapoteza wallet yako kuu)



#### Uundaji wa mrithi mbadala



Bonyeza "Unda Mrithi" na uipe jina "Hifadhi Rudufu".



![Création héritier Backup](assets/fr/17.webp)



Kidirisha ibukizi kinaelezea kwa nini sentensi ya maneno 12 bila passphrase ni salama kwa warithi:


1. **Hakuna ufikiaji wa haraka**: Funguo za warithi haziwezi kufikia fedha hadi muda wa kufunga utakapoisha


2. **Ugunduzi wa maelewano**: Ikiwa mtu atafikia kifungu cha maneno, unaweza kusasisha usanidi wa Heritage


3. **Upatikanaji wa muda mrefu**: passphrase inaweza kusahaulika baada ya miaka mingi



Sanidi mrithi:



![Configuration héritier](assets/fr/18.webp)





- Mtoaji wa Funguo**: Hifadhi ya Funguo ya Karibu
- Mpya**: Tengeneza seed mpya
- Idadi ya Maneno**: Maneno 12



Malizia uundaji:



![Finalisation héritier](assets/fr/19.webp)





- Aina ya Mrithi**: Ufunguo wa Umma Uliopanuliwa
- Hamisha hadi Huduma**: Hiari, huwezesha arifa otomatiki ya warithi



Mrithi wa Backup sasa ameundwa:



![Héritier créé](assets/fr/20.webp)



#### Kuhifadhi msemo wa mnemonic wa mrithi



Bonyeza kwenye mrithi wa chelezo kisha kwenye "Onyesha Mnemonic":



![Afficher mnemonic](assets/fr/21.webp)



**MUHIMU: Andika maneno haya 12 na uyaweke mahali salama. Hii ndiyo ufunguo wa kurejesha pesa.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Kuondoa seed kutoka kwa programu



Ukishaandika kifungu cha maneno, fikia vigezo vya mrithi (aikoni ya cogwheel):



![Paramètres héritier](assets/fr/23.webp)



Tumia "Strip Heir Seed" kuondoa ufunguo wa faragha kutoka kwa programu. Thibitisha kwamba umehifadhi kifungu cha maneno.



![Strip Heir Seed](assets/fr/24.webp)



Hii ni hatua ya usalama: ni ufunguo wa umma pekee unaobaki katika programu, wa kutosha kusanidi urithi.



#### Uumbaji wa mrithi wa pili



Rudia mchakato huo ili kuunda mrithi wa pili (k.m. "Satoshi"). Sasa utakuwa na warithi wawili:



![Deux héritiers](assets/fr/25.webp)





- Hifadhi nakala rudufu**: Ufunguo wako wa dharura wa kibinafsi
- Satoshi**: Mrithi aliyeteuliwa



### Usanidi wa urithi



Rudi kwenye wallet yako na ubofye aikoni ya Mipangilio:



![Paramètres wallet](assets/fr/26.webp)



Katika sehemu ya "Usanidi wa Urithi", bofya "Unda":



![Heritage Configuration](assets/fr/27.webp)



Weka mipaka ya muda kwa kila mrithi:



![Configuration délais](assets/fr/28.webp)





- Hifadhi Nakala**: Siku 180 (miezi 6) - Tarehe ya Kukomaa: 2026-06-18
- Satoshi**: Siku 455 (miezi 15) - Tarehe ya Kukomaa: 2027-03-20



**Muhimu**: Kila mrithi lazima awe na ucheleweshaji mrefu zaidi kuliko ule wa awali. Mrithi wa kwanza (Nakala Rudufu) atakuwa na ufikiaji wa fedha kwanza.



Pia sanidi:



![Configuration finale](assets/fr/29.webp)





- Tarehe ya Marejeleo**: Tarehe ya kuanza kuhesabu nyakati za malipo
- Ucheleweshaji wa Kiwango cha Chini cha Ukomavu**: Ucheleweshaji wa kiwango cha chini baada ya muamala (siku 10 zinapendekezwa)



Bonyeza "Unda" ili kuthibitisha usanidi.



Usanidi wa Urithi sasa unafanya kazi:



![Configuration active](assets/fr/30.webp)



Inaonyesha warithi wote wawili wakiwa na tarehe zao za mwisho na tarehe za mwisho wa matumizi.



### Vielezi vya kuhifadhi



**Muhimu**: Hifadhi maelezo yako ya wallet. Bila hayo, hata kwa msemo wa kukumbuka, urejeshaji wa fedha hauwezekani.



Bonyeza "Vielezi vya Hifadhi Nakala":



![Bouton Backup](assets/fr/31.webp)



Hifadhi faili ya JSON iliyo na maelezo yako ya Bitcoin:



![Backup descripteurs](assets/fr/32.webp)



Faili hii inapaswa kupitishwa kwa warithi wako, pamoja na vifungu vyao vya kumbukumbu.



### Pokea bitcoins



Bonyeza "POKEA" ili upate anwani ya mapokezi ya generate:



![Recevoir bitcoins](assets/fr/33.webp)



Hongera! Heritage Wallet yako iko tayari kupokea bitcoins. Kila anwani inayozalishwa inajumuisha kiotomatiki masharti yako ya Heritage.



Baada ya kupokea muamala, salio lako husasishwa:



![Solde mis à jour](assets/fr/34.webp)



Historia inaonyesha muamala na usanidi unaohusiana wa Urithi.



---

## Kupona kutoka kwa mrithi



Mara tu muda uliowekwa utakapopita, mrithi anaweza kurejesha fedha hizo.



### Masharti ya awali



Mrithi anahitaji:


1. Kifungu chake cha maneno 12 cha kumbukumbu


2. Faili ya nakala rudufu ya maelezo ya wallet (JSON) asilia



### Kuunda Mrithi Wallet



Katika kichupo cha "URITHI", dirisha ibukizi linakukumbusha masharti haya:



![Page Heir Wallets](assets/fr/35.webp)



**Tafadhali kumbuka**: Bila faili ya nakala rudufu ya maelezo, ufikiaji wa fedha HAUWEZEKANI, hata kwa kifungu sahihi cha kumbukumbu.



Bonyeza "Unda Mrithi Wallet":



![Créer Heir Wallet](assets/fr/36.webp)



Tafadhali jaza fomu:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Mrithi Wallet Jina**: Jina la kumtambulisha mrithi huyu wallet
- Mtoaji wa Funguo**: Hifadhi ya Funguo ya Karibu
- Rejesha**: Chagua chaguo hili ili kuingiza kifungu cha maneno kilichopo



Ingiza maneno 12 ya kifungu cha kumbukumbu cha mrithi na usanidi Mtoaji wa Urithi:



![Entrée mnemonic](assets/fr/38.webp)





- Mtoa Huduma wa Urithi**: "Mtaa" ili kutumia nodi yako mwenyewe pamoja na faili ya chelezo



Pakia faili ya chelezo ya JSON na ubofye "Unda Mrithi Wallet":



![Chargement backup](assets/fr/39.webp)



### Mrithi wa Interface Wallet



Mrithi Wallet ameundwa. Hapo awali, ikiwa muda wa utekelezaji bado haujaisha, hakuna urithi unaopatikana:



![Pas d'héritage disponible](assets/fr/40.webp)



Mara tu ucheleweshaji utakapopita na fedha zikisawazishwa na mtandao wa Bitcoin, zinaonekana katika orodha ya urithi:



![Héritage disponible](assets/fr/41.webp)



Kiolesura kinaonyesha:




- Aina ya ufunguo na alama ya vidole
- Jumla ya fedha zinazoweza kurithiwa
- Kiasi cha sasa kinachoweza kutumika (0 kimekamilishwa ikiwa muda wa matumizi haujaisha)
- Tarehe za kukomaa na kuisha kwa muda wake



Tarehe ya kukomaa inapofikiwa, kitufe cha "Tumia" huhamisha bitcoins hadi wallet ya kibinafsi.



---

## Mbinu bora



### Vielezi vya kuhifadhi



Vielezi vya wallet ni muhimu kwa ajili ya kujenga upya anwani zako za Urithi. **Bila vielezi, hata kwa msemo wako wa kukumbuka, hutaweza kupata pesa zako.



### Usalama wa ufunguo





- Tumia Ledger kwa ufunguo mkuu ikiwezekana
- Kamwe usihifadhi sentensi za warithi mahali pamoja na zako
- Sambaza taarifa katika vyombo vya habari na maeneo mengi



### Nyaraka kwa ajili ya wapendwa wako



Andika maelekezo yaliyo wazi yanayoelezea kila hatua ya mchakato wa kupona. Warithi wako wanaweza wasijue Bitcoin wakati muhimu.



## Njia mbadala



Suluhisho zingine zipo ili kudhibiti upitishaji wa bitcoin zako, ikiwa ni pamoja na Liana na Bitcoin Keeper. Utapata mafunzo yetu hapa chini:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Hitimisho



Heritage hukuruhusu kupanga urithi wako wa Bitcoin kwa njia huru kupitia programu ya Kompyuta ya Mezani. Utekelezaji unahitaji kuzingatia kwa makini muda unaofaa na kulinda siri. Usisahau kuwapa warithi wako:




- Kifungu chao cha maneno 12 cha kumbukumbu
- Faili ya nakala rudufu ya maelezo
- Maagizo ya kurejesha



## Rasilimali





- [Tovuti rasmi ya Urithi](https://btc-heritage.com)
- [Nyaraka CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)