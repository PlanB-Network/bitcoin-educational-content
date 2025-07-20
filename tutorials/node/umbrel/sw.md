---
name: Mwavuli
description: Gundua na usakinishe Umbrel - Njia yako ya Bitcoin na seva ya nyumbani
---

![cover](assets/cover.webp)



## Utangulizi



### Nodi ya Bitcoin ni nini?



Nodi ya Bitcoin ni kompyuta inayoshiriki katika mtandao wa Bitcoin kwa kuendesha programu ya Bitcoin Core au mteja mbadala. Jukumu lake ni muhimu kwa uendeshaji na usalama wa mtandao:





- Hifadhi ya Blockchain**: Hudumisha nakala kamili, iliyosasishwa ya Blockchain Bitcoin
- Uthibitishaji wa muamala**: huthibitisha kila shughuli na kuzuia kulingana na sheria za itifaki
- Usambazaji wa habari**: Hushiriki miamala na vizuizi vipya na nodi zingine
- Ujenzi wa Makubaliano**: Huchangia katika matumizi ya sheria za mtandao



Kuendesha nodi yako ya Bitcoin ni hatua muhimu kuelekea uhuru wa kifedha, ikitoa faida kadhaa muhimu:





- Usiri**: Shiriki miamala yako bila kufichua maelezo yako kwa washirika wengine
- Upinzani wa udhibiti**: Hakuna mtu anayeweza kukuzuia kutumia Bitcoin
- Uthibitishaji wa kujitegemea**: Hakuna haja ya kuamini nodi za watu wengine ili kuthibitisha miamala yako
- Ujenzi wa Makubaliano**: Changia katika matumizi ya sheria za mtandao za Bitcoin
- Usaidizi wa mtandao**: Kuwa mshiriki hai katika usambazaji na ugatuaji wa mtandao



### Umbrel: Suluhisho rahisi la kuendesha nodi ya Bitcoin



Umbrel ni mfumo wa uendeshaji wa chanzo huria ambao hurahisisha usakinishaji na usimamizi wa nodi ya Bitcoin. Pia hubadilisha kompyuta yako kuwa seva ya kibinafsi na ya kibinafsi, na kuifanya iwe rahisi kukaribisha :





- Nodi kamili ya Bitcoin
- Bitcoin maombi muhimu (Electrs, Mempool.space)
- Huduma zingine za kibinafsi (hifadhi ya wingu, utiririshaji, VPN, n.k.)



Kwa kutumia Interface mtumiaji wake maridadi na angavu, Interface, Umbrel hufanya huduma zinazojiendesha zipatikane na wote, huku ikihifadhi udhibiti kamili wa data yako.



## Chaguzi za ufungaji wa mwavuli



Umbrel hutoa njia mbili kuu za kutumia suluhisho lao: chaguo la turnkey (Umbrel Home) na toleo la bure la chanzo cha wazi (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Nyumba ya Umbrel: Suluhisho la turnkey



Umbrel Home ni seva ya nyumbani iliyosanidiwa mapema, iliyoundwa mahsusi kwa matumizi bora. Suluhisho hili la vifaa vyote kwa moja ni pamoja na:



**Sifa za vifaa**




- Kichakataji cha utendakazi wa hali ya juu kilichoboreshwa kwa upangishaji wa kibinafsi
- Hifadhi ya SSD ya kasi ya juu iliyosakinishwa mapema
- Mfumo wa baridi wa utulivu
- Compact, kubuni kifahari
- Bandari za USB na Ethaneti zilizounganishwa



**Faida za kipekee**




- Usakinishaji wa programu-jalizi: chomeka na uende
- Usaidizi wa malipo kwa usaidizi wa kujitolea
- Uhakikisho wa sasisho otomatiki
- Kichawi cha uhamiaji kilichojumuishwa
- Udhamini kamili wa vifaa
- Usaidizi kamili kwa utendaji wote



**Bei**: €399 (bei inaweza kutofautiana kulingana na msimu)



### UmbrelOS: Toleo la chanzo huria



UmbrelOS ni toleo la bure, la chanzo huria cha mfumo wa uendeshaji wa Umbrel. Suluhisho hili linalonyumbulika hukuruhusu kutumia maunzi yako mwenyewe huku ukinufaika na vipengele muhimu vya Umbrel.



**Faida**




- Bila malipo kabisa
- Fungua msimbo wa chanzo unaoweza kuthibitishwa
- Uhuru wa kuchagua
- Chaguzi za ubinafsishaji wa hali ya juu



**Majukwaa yanayotumika**




- Raspberry Pi 5: Suluhisho maarufu na la bei nafuu
- Mifumo ya X86: Kwa Kompyuta za kawaida au seva
- Mashine pepe: Kwa majaribio au matumizi kwenye miundombinu iliyopo



**Mapungufu




- Usaidizi wa jumuiya pekee
- Baadhi ya vipengele vya kina vimehifadhiwa kwa Umbrel Home
- Usanidi wa awali wa kiufundi zaidi
- Utendaji hutegemea vifaa vilivyochaguliwa



Toleo hili ni bora kwa:




- Watumiaji wa kiufundi
- Wale ambao tayari wana vifaa vinavyoendana
- Watu wanaotaka kujifunza na kufanya majaribio
- Watengenezaji wanaotaka kuchangia mradi huo



Viungo rasmi vya ufungaji:




- [Usakinishaji kwenye Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Usakinishaji kwenye mifumo ya x86 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Usakinishaji wa mashine pepe](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



Katika somo hili, tutazingatia kusakinisha UmbrelOS kwenye Raspberry Pi 5, lakini kanuni za msingi zinabaki sawa kwa majukwaa mengine.



## Kufunga Umbrel OS kwenye Raspberry Pi 5



### Vipengele vinavyohitajika



Kwa ufungaji huu utahitaji:





- Raspberry Pi 5 (GB 4 au 8 GB RAM)
- Nguvu rasmi ya Raspberry Pi Supply (muhimu kwa utulivu!)
- Kadi ya MicroSD (kiwango cha chini cha GB 32)
- Kisomaji cha kadi ya microSD
- SSD ya nje ya kuhifadhi data
- Kebo ya Ethaneti
- Kebo ya USB ya kuunganisha SSD



### Hatua za ufungaji



**Pakua UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Tembelea [tovuti rasmi](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Pakua toleo la hivi karibuni la UmbrelOS la Raspberry Pi 5



**Balena Etcher** usakinishaji



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Pakua na usakinishe [Balena Etcher](https://www.balena.io/etcher/) kwenye kompyuta yako



**Kutayarisha kadi ya microSD**



![Insertion carte microSD](assets/fr/03.webp)




- Ingiza kadi yako ya microSD kwenye kisomaji cha kadi ya kompyuta yako



**Picha inamulika**



![Flashage UmbrelOS](assets/fr/04.webp)




- Uzinduzi Balena Etcher
- Chagua picha ya UmbrelOS iliyopakuliwa
- Chagua kadi yako ya microSD kama unakoenda
- Bonyeza "Flash!" na subiri mchakato ukamilike
- Ondoa kadi kwa usalama



**usakinishaji wa kadi ya microSD



![Installation microSD](assets/fr/05.webp)




- Ingiza kadi ya microSD kwenye Raspberry Pi 5 yako



**Muunganisho wa pembeni**



![Connexion périphériques](assets/fr/06.webp)




- Unganisha SSD ya nje kwenye mlango unaopatikana wa USB
- Unganisha kebo ya Ethaneti kati ya Pi na kipanga njia chako



**Washa



![Démarrage du Pi](assets/fr/07.webp)




- Unganisha nguvu rasmi ya Raspberry Pi Supply
- Subiri dakika chache ili mfumo uanze



**Ufikiaji wa kwanza**



![Accès interface web](assets/fr/08.webp)




- Kwenye kifaa kilichounganishwa kwenye mtandao huo huo, fungua kivinjari chako
- Fikia tovuti ya Umbrel ya Interface kwa: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Ikiwa `umbrel.local` haifanyi kazi, utahitaji kupata IP Address ya Raspberry Pi yako kwenye mtandao wa ndani. Unaweza:




- Angalia Interface ya kipanga njia chako
- Kutumia kichanganuzi cha mtandao kama nmap
- Tumia amri ya `arp -a` kwenye terminal ya kompyuta yako



## Hatua ya kwanza kwenye Umbrel



Mara tu Mwavuli wako unapoanzishwa na kupatikana kupitia kivinjari chako, fuata hatua hizi ili kuanza:



### Usanidi wa awali



**Fungua akaunti yako**



![Création compte](assets/fr/10.webp)




- Chagua jina la mtumiaji
- Weka nenosiri salama
- Utahitaji kitambulisho hiki ili kufikia Mwavuli wako



** Uthibitisho wa akaunti



![Confirmation compte](assets/fr/11.webp)




- Bofya "Inayofuata" ili kufikia dashibodi yako



**Ugunduzi wa Interface**



![Interface Umbrel](assets/fr/12.webp)




- Fikia Hifadhi ya Programu ya Umbrel
- Gundua programu nyingi zinazopatikana
- Wacha tuanze kwa kusakinisha programu muhimu za Bitcoin



### Inasakinisha programu za Bitcoin



**Njia ya Bitcoin**



![Bitcoin Node](assets/fr/13.webp)




- Programu ya kwanza kusakinisha
- Pakua na uangalie Blockchain Bitcoin nzima



**Wapiga kura**



![Installation Electrs](assets/fr/14.webp)




- Seva ya umeme ya kuunganisha pochi za Bitcoin
- Hulandanisha na nodi yako ya Bitcoin



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Onyesho la Interface la Blockchain
- Hufuatilia miamala na vizuizi kwa wakati halisi



## Kufuatilia shughuli na Mempool.space



Mempool.space ni mgunduzi wa chanzo huria wa Blockchain ambaye hutoa taswira ya wakati halisi ya mtandao wa Bitcoin. Inakuwezesha kufuatilia miamala yako na kuelewa jinsi miamala inavyoenea kwenye mtandao.



### Kuelewa Mempool na uthibitisho



"Mempool" (dimbwi la kumbukumbu) ni kama chumba cha kawaida cha kusubiri ambapo miamala yote ambayo haijathibitishwa ya Bitcoin huhifadhiwa kabla ya kujumuishwa kwenye kizuizi. Hivi ndivyo muamala unavyochakatwa:



1. **Tangaza**: Unapotuma muamala, inatangazwa kwanza kwenye mtandao wa Bitcoin


2. **Kusubiri katika Mempool**: Kusubiri kuchaguliwa na Miner kwa misingi ya gharama


3. **Uthibitisho wa kwanza**: Mtoto mdogo hujumuisha kwenye kizuizi (Uthibitisho wa kwanza)


4. **Uthibitisho wa ziada**: Kila block mpya inayochimbwa baada ya ile iliyo na muamala wako kuongeza uthibitisho



Idadi iliyopendekezwa ya uthibitishaji inategemea kiasi:




- Kwa kiasi kidogo: uthibitisho 1-2 unaweza kutosha
- Kwa kiasi kikubwa: uthibitisho 6 kwa ujumla huchukuliwa kuwa salama sana



### Gundua Interface kutoka Mempool.space



1. **Ukurasa wa nyumbani** unakupa muhtasari wa mtandao wa Bitcoin:




   - Vitalu vilivyochimbwa hivi karibuni
   - Makadirio ya gharama kwa vipaumbele tofauti
   - Hali ya sasa ya Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Tafuta muamala**: Ili kufuatilia muamala mahususi, bandika kitambulisho chake (txid) kwenye upau wa kutafutia ulio juu ya ukurasa.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Changanua maelezo ya muamala



Mara tu muamala wako utakapopatikana, Mempool.space hukuletea uchambuzi kamili:



1. **Taarifa muhimu** :




   - Hali (imethibitishwa au la)
   - Gharama zilizolipwa (katika Sats/vB)
   - Muda uliokadiriwa wa uthibitishaji



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Muundo wa muamala** :




   - Uwakilishi unaoonekana wa pembejeo na matokeo
   - Orodha ya kina ya anwani zinazohusika
   - Kiasi kilichohamishwa



3. **Data ya kiufundi** :




   - Uzito wa manunuzi
   - Ukubwa pepe
   - Muundo na toleo lililotumika
   - Metadata nyingine mahususi



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Faida za kutumia Mempool.space kwenye Umbrel



1. **Usiri**: Maombi yako yanapitia nodi yako mwenyewe


2. **Uhuru**: Hakuna haja ya kutegemea huduma ya mtu wa tatu


3. **Kuegemea**: Upatikanaji wa data hata wakati vivinjari vya umma vimepungua



Ukiwa na programu hii, unaweza kufuatilia shughuli zako kwa ufanisi, kuelewa jinsi ada huathiri kasi ya uthibitishaji, na kupata ufahamu bora wa jinsi mtandao wa Bitcoin unavyofanya kazi.



## Kuunganisha Wallet Bitcoin kwenye nodi yako



### Usanidi wa elektroni



**Muunganisho wa ndani



![Connexion locale](assets/fr/18.webp)




- Kwa matumizi kwenye mtandao wako wa karibu
- Haraka na rahisi kusanidi



** Muunganisho wa mbali kupitia Tor**



![Connexion Tor](assets/fr/19.webp)




- Ili kufikia nodi yako kutoka popote
- Salama zaidi na ya faragha



### Kuunganishwa na Sparrow Wallet



**Ufikiaji wa vigezo



![Paramètres Sparrow](assets/fr/20.webp)




- Fungua Sparrow Wallet
- Nenda kwa Mapendeleo > Seva
- Bonyeza "Rekebisha muunganisho uliopo"



** Chaguo la aina ya unganisho



Sparrow inatoa njia tatu za uunganisho:



***Seva ya Umma***




- Muunganisho kwa seva za umma (k.m. blockstream.info, Mempool.space)
- Rahisi lakini faragha kidogo



***Bitcoin Core***




- Uunganisho wa moja kwa moja kwa node ya Bitcoin
- Binafsi lakini polepole



***Elektroni ya kibinafsi***




- Unganisha kwenye seva yako ya Electrs
- Inachanganya usiri na utendaji



** Mipangilio ya Electr**



Chagua aina ya muunganisho wako kwa kutumia maelezo yaliyoonyeshwa kwenye programu ya Electrs tuliyoona hapo awali:



Katika visa vyote viwili, acha chaguo za "Tumia SSL" na "Tumia proksi" bila kuchaguliwa.



**Muunganisho wa ndani


Mpangishi: umbrel.local


Nambari ya bandari: 50001



**Muunganisho wa mbali (Tor)**


Mpangishi : [yako-Address-vitunguu]


Nambari ya bandari: 50001



Muunganisho wa Tor ni muhimu ikiwa unataka kufikia nodi yako nje ya mtandao wako wa karibu.



![Configuration connexion](assets/fr/21.webp)


Kwa maelezo zaidi kuhusu programu ya Sparrow Wallet, tuna mafunzo ya kina :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Hitimisho



Umbrel yako sasa iko tayari kutumika. Unashiriki kikamilifu katika mtandao wa Bitcoin huku ukiwa na udhibiti kamili wa data yako. Jisikie huru kuchunguza programu nyingine nyingi zinazopatikana katika Duka la Programu la Umbrel ili kupanua uwezo wa seva yako ya nyumbani.



## Rasilimali muhimu



### Nyaraka rasmi




- [Tovuti Rasmi ya Mwavuli](https://umbrel.com)
- [Hati za mwavuli](https://github.com/getumbrel/umbrel/wiki)
- [Mwavuli wa Duka la Programu](https://apps.umbrel.com)



### Maombi ya Bitcoin




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Wachaguzi](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### Jumuiya




- [Mwavuli wa Jukwaa](https://community.getumbrel.com)
- [Mwavuli wa GitHub](https://github.com/getumbrel)
- [Mwavuli wa Twitter](https://twitter.com/mwavuli)