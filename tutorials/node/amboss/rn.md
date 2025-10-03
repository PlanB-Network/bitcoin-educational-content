---
name: Ambosi
description: Gutohoza no gusuzuma Lightning Network.
---

![cover](assets/cover.webp)



Lightning Network ni Layer y’amasezerano ya Bitcoin, yateguwe ahanini mu guteza imbere kwemera kwishura kwa Bitcoin ku musi ku musi mu kwongera umuvuduko wo gukora igikorwa cose. Hashingiwe ku ngingo ngenderwako y’ugusenyura ubutegetsi, Lightning Network igizwe n’ibihimba (ordinateri zikoresha ubuhinga bwa Lightning) zimenyeshanya amakuru hagati y’abandi, zigatanga amakuru (ukwishura n’ukugenzura ukwishyura).



https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Nk’uko biri ku ruzitiro rwa mbere, vyacitse ngombwa ko abakoresha bamenya amakuru n’aho urubuga ruri, kugira ngo bishobore kworohereza amasano hagati y’ibice no kugabanya ingorane y’amahera ishobora gushika muri rusangi mu rubuga. Nkako, kuri Lightning Network, turasaba ko umuntu yishura amahera makeyi cane kuruta ayo umuntu akoresha ku ruhererekane rwa Bitcoin.



Ni vyiza kumenya ko ata node zose za Lightning ziboneka ku rubuga rwa Amboss.



Nka [Ikibanza ca Mempool](https://Mempool.ikibanza), itanga amakuru ngirakamaro ku ruhererekane nyamukuru rw'amasezerano ya Bitcoin, kuva mu 2022 [Amboss](https://amboss.ikibanza) itanga amakuru ku :





- Ivyuma biri kuri Lightning Network.
- Inzira zo kwishura n'ubushobozi bwo kwishura
- Lightning Network gutera imbere mu gihe
- Imibare ku bihembo vyo gutanga ama node ku vyerekeye ivyo wishyura.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Muri iyi nyigisho, tuzogutwara mu rugendo rwo kuri iyi platform, ariyo nzira y’ingenzi ku bakoresha Lightning Network, abashaka gufatanya node yabo kugira ngo bagure urubuga, n’ibindi.




## Rondera babiri



Kimwe mu ntumbero z’urubuga rwa Amboss ni ugutuma ama node atandukanye ari muri iyo nzira ashobora guhuza no guhanahana amakuru. Ku rupapuro rw’intango rw’urubuga, urashobora kurondera izina ry’urudodo usanzwe uzi, canke ukaronka urudodo ruvuye mu bitabo vya Lightning bikundwa cane ukoresha.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Kuri paji y'intango, uzosanga kandi uturongo twashizwe mu migwi hakurikijwe :




- Ugutera imbere kw’ubushobozi: ubwinshi bwa Bitcoin bujanye n’urufunguzo rwa bose rw’uruzitiro n’umubare wose uboneka mu mihora yarwo yose.
- Iterambere ry’imirongo: umubare w’amahuza mashasha n’izindi nzira ziri mu rubuga.
- Ugukundwa kw’urudodo: ni kangahe urudodo rukoreshwa.



![nodes](assets/fr/03.webp)



Guhitamwo urudodo rwiza rwo gufatanya rero biva ku kugenzura ibi bikurikira:





- Kumenya neza ko iyo node ifise umubare uhagije w’ama bitcoins; uko ubushobozi bw’urudodo bugenda buragwira, niko n’amahera y’ama bitcoins ushobora kwishura arushirizaho.





- Kumenya neza ko iyo node ifise umubare munini w’amahuza no gufungura imirongo n’izindi node ziri mu rubuga.





- Raba neza ko iyo node ikora kandi iguma ishimwa n’urunganwe rwayo mu kugenzura umubare w’imirongo mishasha; uko iyo node ifungura imirongo mishasha, ni ko ishimwa cane n’izindi node ziri mu rubuga.



Umaze kuronka urudodo rwiza, fyonda ku izina ryarwo kugira ngo ushire kuri paji y'amakuru y'urudodo.



Kuri iyi Interface, mu gusuzuma Timestamp y’umurongo mushasha waremwe, uzoronka ikimenyetso c’igikorwa c’iyi node. Uzosanga kandi amakuru yerekeye ubushobozi bw'imirongo y'iyi node: aya makuru ni ngirakamaro nimba ushaka gukoresha n'umwete iyi node kugira ngo ukore ivyo wishura.




![node_info](assets/fr/04.webp)



Mu gice c'ibubamfu, uzosanga ibindi bisobanuro ku bijanye n'aho iyo node iri. Nk'akarorero, ushobora kubona :




- Urufunguzo rwa bose: ikimenyetso kiri munsi y'izina ry'urudodo.
- Igihugu c’iyi node.




![channels](assets/fr/05.webp)



Iyi Interface ikubwira ihuriro Address ry'iyi node: ifata uburyo `pubkey@ip:port`. Mu karorero kacu, dushaka gufatanya n'urudodo rufise :




- Urufunguzo rwa bose `urufunguzo rwa bose` ni: `035e4ff418bfc226`
- iP Address: '170,75,163,209'
- Icibutso: `9735`



![geoinfo](assets/fr/06.webp)



Mu gice ca **Imirongo**, uzobona urutonde rw'imirongo yuguruye n'uburyo iyo node ihuriye n'izindi node ziri mu rubuga. Kuri iyi Interface, amakuru menshi ni ngirakamaro kugira ngo twemeze ko iyo node ihuye n’ivyo dukeneye canke ko ari iyo kwizigirwa:





- Incoming ratio**: Amahera node izogusaba ku miliyoni yose ya Satoshi ironka, bivanye n’umurongo wahisemwo.
- Igitigiri (ibice ku miliyoni)** : kigereranya umubare w’ama Satoshi ku miliyoni y’ibice iyo node izogusaba iyo ufashe ingingo yo kwishura biciye kuri imwe mu nzira zayo. Reka tuvuge ko ufashe ingingo yo kwishura `10_000 Sats` biciye ku muhora ufise igipimo ca ppm `500 Sats`, uzobwirizwa kwishura urudodo `10_000 * 500 / 1_000_000` satoshis, bingana na GW-2` `5.
- Igitigiri kinini** : Igitigiri kinini iyi node iguha uburenganzira bwo guca muri imwe muri izo nzira.



Mu kuraba imbonerahamwe iri muri iyi Interface, urashobora kandi kuronka ayo makuru yose ku nzira ihuriyeko.



![channels_info](assets/fr/07.webp)



Mu gice ca **Ikarita y'imirongo**, urashobora kubona ukuntu imirongo itandukanye iri kuri iyi node igabanywa n'ubushobozi bwayo. Ushobora guhindura ingingo ngenderwako zo gukwiragiza zigaragazwa mu guhitamwo imwe mu mahitamwo ari ku rutonde ruja hasi iburyo.



![cha_maps](assets/fr/08.webp)



Igice ca **Imirongo yugarijwe** gishira hamwe imirongo yose ya kera y'uruzitiro hakurikijwe ubwoko bw'ugufunga:




- Gufungana**: bigereranya amasezerano y’ababiri, bakoresha urufunguzo rwabo rw’ibanga kugira ngo bashire umukono ku gikorwa kigaragaza ugufunga umuyoboro n’ugusangira amafaranga asigaye muri wo .
- **Ugufunga ku nguvu**: bigereranya ugufunga bukwi na bukwi, ku ruhande rumwe kw’igice kimwe c’umuyoboro. Ubwo bwoko bwo gufunga ntibubereye, kuko Lightning Network ari umurongo ushingiye ku gihano: iyo ugerageje guhenda uburinganire bw’umurongo, ushobora gutakaza uburinganire bwawe bwose buri muri uwo muhora.



![closed](assets/fr/09.webp)



Uronke amakuru ku mafaranga y'urugendo kugira ngo ushire amahera yawe biciye ku nzira iri ku nzira ukoresha



![fees](assets/fr/10.webp)



## Amakuru y'urubuga



Amboss ntiyibanda gusa ku makuru y’abagize urubuga, ariko kandi n’ingene urubuga ubwarwo rumeze.



Mu gice ca **Imibare**, munsi y'ibubamfu "Ivyiyumviro", uzosanga igicapo kigaragaza ubushobozi bwo kwishura neza nk'uko bigenda ku giciro c'ukwishurwa.



Nkako, uzobona ko igicapo kiriko kiragabanuka kubera ko, uko amahera wishura agenda arushirizaho, ni ko ugira amahirwe make yo kubona iyo nsiguro igenda. Ivyo vyerekana ingorane nyayo y’amahera kuri Lightning Network. Nk’akarorero, amahera yawe y’amasatoshi `10_000` arafise amahirwe `79%` yo gukorwa. Ku rundi ruhande, ku kwishura `3_000_000` satoshis ufise amahirwe makeyi atari munsi ya `13%` yo kuroranirwa.



![network](assets/fr/11.webp)



**Imibare y'urubuga** iraguha uburenganzira bwo kugaragaza imibare ya :




- Inzira zo kwishura
- Uturongo
- Ubushobozi
- Amafaranga
- Ugutera imbere kw’imirongo.



![network_stat](assets/fr/12.webp)



Mu **Imibare y'isoko**, **Ibisobanuro vy'Itegeko** bigufasha kubona ivyipfuzo vy'amahera kuri Lightning Network. Iyi graphe irashobora kandi kwerekana imihora ikenewe cane kandi/canke ifise ubushobozi bwinshi.



![markets](assets/fr/13.webp)




## Ibikoresho



Amboss itanga ibikoresho vyinshi bigufasha gutuma ubushakashatsi bwawe n’ibikorwa vyawe bigenda neza.



### Lightning Network gusobanura



Iki gikoresho ahanini gifise inshingano yo kuguha amakuru y’imiterere y’umuravyo Invoice, umuravyo Address canke URL y’umuravyo.



Ku rupapuro rw'intango, mu gice ca **Ibikoresho**, shiramwo Lightning Address yawe, nk'akarorero.



![decoder](assets/fr/14.webp)



Muri iyi decodeur, ushobora kuronka amakuru nk'aya :




- urufunguzo rwa bose rw'urudodo rujanye n'umuravyo wawe Address;
- Igihe co guhera kw’igitabu ca Invoice kivuye kuri Address yawe;
- Ivyo ushobora gutanga n’ivyo ushobora gutanga;
- Igikoresho ca Nostr gifitaniye isano na Address yawe, nimba Nostr ikoreshwa kuri iyi nzira.



![decode](assets/fr/15.webp)



### Magma IA



Tora igikoresho gishasha cashizwe ahabona na Amboss kugira ngo ushobore gucunga neza amahuzu yawe n’ibihimba vya Lightning Network. Magma AI ikoresha ubwenge bukorano bwihariye kugira ngo yibande ku ngorane ihambaye: guhitamwo neza ama node yo gufatanya na yo.



![magma](assets/fr/16.webp)



### Satoshi igiharuro



Raba igiciro ca Bitcoin kiriho ubu mu mafaranga y’igihugu cawe (EUR / USD). Ku rupapuro rw’intango, koresha igiharuro ca satoshis kugira ngo umenye igiciro c’isoko kiriho ubu.



![calculator](assets/fr/17.webp)




Ubu waragendeye vyose ibiranga urubuga n’ibikoresho vyo gusesangura. Turagusavye uronke aha hepfo ingingo yacu ku bijanye n’indege Bitcoin **Mempool.space**.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f