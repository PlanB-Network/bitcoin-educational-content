---
name: Ivyo kurya
description: Ubuhinga bwo gukoresha bworoshe bwatunganijwe neza ku mashini zidakora neza. N'uguhitamwo kwiyakira
---

![cover](assets/cover.webp)



Mu bihugu bitagira ubuhinga, amabara nk’aya `Odroid`, `Raspberry Pi`, `Orange Pi` canke `Radxa`, ntazwi cane. Ariko umuntu ategerezwa gusa kuraba hanze mu nzego z’ubuhinga, kugira ngo asange ko mudasobwa **SBC**--zubatswe ku rupapuro rumwe, akenshi zikaba ari ntoyi cane ugereranije n’amadasobwa akoreshwa cane--zicika ivy’agaciro, nk’infashanyo y’umugambi uwo ari wo wose w’umuntu ku giti ciwe.



Izo ni orodinateri zikoreshwa mu buryo butandukanye cane. Ivyiza ni uko bashobora kwakira ama distribution ya Linux, akenshi ahindurwa kugira ngo akore neza kuri izo mashini zidafise ubushobozi bwinshi.



**DietPi ntaco ihindura**: ni uburyo bwo gukoresha bushingiye kuri Debian, butunganijwe kugira ngo bube bworoshe uko bishoboka kwose kandi bugatuma mbere n'iyikora bike cane `SBC` yihuta cane. Yahinduwe kuva kuri Debian12 Bookworm gushika kuri Debian13 Trixie nk'uko iyi nyigisho yariko irandikwa, ubu irafasha kandi SBCs zishingiye ku nzira yuguruye `RISC-V`. DietPi ni ikintu ciza cane kivumbuwe gikwiriye kwigwa cane.



## Inkomezi



Ivyo si "ibisanzwe" vya Debian ku bipande bitobito vy'ubwoko bwa Raspberry. IvyokuryaPi ni:




- Itunganijwe neza kubera umuvuduko n’umuco**: a [kugereranya n’ibindi bikoresho vya Debian vya SBC](https://dietpi.com/blog/?p=888), DietPi iraremereye muri vyose. Ishusho ya DietPi ISO ipima munsi ya 1 GB, ni yo ntoyi cane mu zigenewe ibigereranyo vya kera vya Raspberry canke Orange PI (nk’akarorero). Ivyo bisabwa ku bikoresho vya RAM na CPU ni bike cane, ku buryo yama ironka ivyiza kuruta ibindi vyose mu bipande, mbere n’ivya kera.
- Ivyuma vyubatswemwo n’ababishiramwo**: Amabwirizwa yihariye afasha abakoresha kugenzura ibikoresho vya sisitemu hamwe n’ibikorwa vy’ubuhinga bwo gushiramwo no gutanguza porogarama, guhindura verisiyo, gukora amakopi, no kugenzura amakuru yose.
- Umuryango ukomeye, wibanda ku kugerageza**: [inyigisho](https://dietpi.com/forum/c/community-tutorials/8) n’imigambi iva mu muryango wa DietPi, ni vyiza cane kugira ngo ushobore guhumekerwa na porogarama ushobora gushiramwo ukoresheje gukanda rimwe, ushimira DietPi.



**Gucapura igice cose muri SBC yawe ntivyigeze vyoroha**.



## Ukwikoresha kwiyakira


Ushaka kugerageza server yawe bwite kugira ngo ukoreshe inyishu ziteye imbere z’uruja n’uruza, canke ibikoresho vyo guteza imbere ubuhinga bwawe bwa Bitcoin? DietPi ishobora kuba ariyo muti mwama murondera. Naho abantu benshi bazi gucunga ibikorwa remezo vyabo bwite no gukoresha ama server atunganijwe neza kandi akinzwe, DietPi ni intambwe ibereye ku bashaka gutangura kuva ku ntango.



Aho gukora n'amaboko ibikorwa vyose bikomeye igikorwa nk'ico gisaba, DietPi iraguha uburenganzira bwo kuvyubaka ukoresheje `umupfumu` n'umurongo wayo bwite w'amabwirizwa. Aha ushobora kugerageza igicu cawe bwite, _smart home_ gucunga ibikoresho, gukora backups vy’ubuhinga bwa none na crontab, hamwe n’ibindi bisubizo biteye imbere.



![img](assets/en/01.webp)



## Gushiramwo



### Gukurura



DietPi itanga amashusho atagira uko angana y’ISO, kugira ngo uturire ubuhinga bwo gukoresha ku bikoresho vyinshi bitandukanye. Bimwe bishigikiwe gusa: ISO ya Raspberry PI5 iracari mu bigeragezo, nk’akarorero, ariko urashobora kuronka ata gukeka iyo ibereye urubaho rwawe.



Ku bw'iyi nzira nahisemwo kuyishira ku mukiriya mutoyi, rero ihitamwo ryagiye kuri _PC/VM_ hanyuma kuri _Native PC_. Hariho amashusho abiri ya ISO y’ivyo bikoresho, atandukanye mu bijanye n’ugukura kw’ivyo bikoresho. Imashini yakoreshejwe mu nyigisho ni iya kera cane, rero amahitamwo yagiye kuri _BIOS/CSM_ version. Niba ufise imashini nshasha, verisiyo ibereye ishobora kuba `UEFI`.



![img](assets/en/02.webp)



Uzoshika kuri paji irimwo `ishusho y'uwushizeho`, `sha256` na `Imikono`.



![img](assets/en/03.webp)



Tegura ububiko mu `nzu` ya mudasobwa yawe ya misi yose, kugira ngo ushobore gukuraho amadosiye akenewe, ukoresheje `wget`.



![img](assets/en/04.webp)



Urufunguzo rwa bose rw’umuhinguzi rwasaba ubushakashatsi bukeyi, ariko ushobora kururonka kuri iyi nzira: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Suzuma ibirimwo mu bubiko na `ls -la` hanyuma ushire urufunguzo rwa MichaIng mu rufunguzo rwawe, na `gpg --import`.



### Gusuzuma no guca ibibatsi



Ubwa nyuma, igice ndababwira cane: menya neza ukuri kw’ivyo mwaronse kandi mugiye gushiramwo kuri SBC yanyu.



![img](assets/en/06.webp)



Niba kandi ufise igisubizo ca `Good signature` n'ivyo nyene bigenzura Hash n'itegeko rya sha256sum, urashobora gukomeza gucapura ISO ku nkoni ya USB. Koresha amaporogarama nka Whale Etcher kugira ngo ukore ivyo.



![img](assets/en/07.webp)



## Gushiramwo DietPi



![img](assets/en/09.webp)



Kwimurira flash drive ku gikoresho kizokwakira DietPi maze utangure gushiramwo ubuhinga bwo gukoresha lime Green. Muri iki gikorwa turiko turakoresha umukiriya mutoyi afise 16 GB ya RAM, 128 GB SSD y’ubuhinga bwo gukoresha, n’idisiki ya kabiri y’amakuru y’1 TB. Ivyo gushiramwo vyatwaye iminota itarenga 30, ariko nimba uzoba uriko urakoresha Raspberry nk’akarorero, ibikoresho bishobora kuba bike kandi bikatwara igihe kirekire. Uzokwerekwa ingene bigenda mu gihe co gushiramwo.



![img](assets/en/08.webp)



Kubera ko yagenewe Raspberries n'ibindi nk'ivyo, kamere nyakuri ya DietPi ni ivyo bita `headless` installation, ata bidukikije vy'ibishushanyo kandi n'uburyo bwo gushika ku `shsh'. Mu nzira ahubwo uzobona ibidukikije vy'ibishushanyo, LXDE kugira ngo ube ukuri.



Muri iyi ntambwe uzosabwa kandi guhitamwo umucukumbuzi w’urubuga ushaka gukoresha ku buryo busanzwe, hagati ya Chromium na Firefox. Ivyo vyose bikora neza; nta n’imwe muri izo nzira zidasanzwe zibuza, uretse ivyo wewe ubwawe ukunda.



Mu mpera, uwugushiramwo ashobora kukubaza nimba ushaka gushiramwo porogarama iyo ari yo yose isanzwe, ariko hano **ndaguhanura ko utagira ico ushiramwo imbere y'igihe**. Ukwiye kumenya ko inyuma y’iyi ntambwe, uzosabwa guhindura amajambo y’ibanga y’abakoresha babiri, kubera imvo z’umutekano. Ikiruta vyose uzosabwa **gushinga `Ijambobanga rya Porogaramu y’Isi Yose (GSP)`**, ivyo bizotuma ushobora gukoresha porogaramu zitandukanye mu buryo bugenzurwa. **Niwakuraho porogaramu iyo ariyo yose mu gihe co gushiramwo OS, ata `GSP` set, izoguma hafi idashobora gushikwako**. Uzobwirizwa kubikuraho no kubisubiramwo umaze gushinga `Ijambobanga rya Porogarama y'Isi yose`: rero, **ntihagire ico ushiramwo kugira ngo wirinde gukora kabiri**. (Ivyo bitera ingorane birashoboka, si 100% vy’ukuri).



Ivyo biheze n’ugusaba gukoresha DietPi-Survey, igikorwa co gukusanya amakuru gikoreshwa mu gufasha mu gutegura ubuhinga bwo gukoresha. Dukurikije urubuga, ugukusanya amakuru birakora iyo ukuye porogarama iyo ari yo yose mu bikoresho vy’ubuhinga bwa none bitangwa na DietPi, canke iyo ushize ku yindi porogarama. Umuntu wese afise uburenganzira bwo kwinjira (_Opt IN_) canke gusohoka (_Opt OUT_).



![img](assets/en/23.webp)



Iyo uhejeje gushiramwo no gusubira gufungura, DietPi yerekana ku rubuga uko uyishiraho. Ku nyigisho, nk'uko vyavuzwe, nahisemwo ibidukikije vy'ibishushanyo `LXDE`. Ku biro nasanze inzira ngufi yo gutangura `htop` na terminal yuguruye.



![img](assets/en/10.webp)



### "Ibikoresho" bivuye kuri sisitemu



Nimwibagire porogarama nyinshi mukoresha ku gutanga Linux-DietPi ni nziza cane, mwasize nke cane. Ubwirizwa gushiramwo amabwirizwa menshi n'amaboko, ariko nimba uriko uragerageza gusa, n'uhangane n'ikigeragezo maze ugerageze gushiramwo ubuhinga bwa DietPi mu kigeragezo.



Nta gukeka ko ari terminal ari co gikoresho ca mbere c’ingirakamaro co gutangura gukoresha ubuhinga bwawe bushasha, kandi irafunguka ubwayo igihe cose uyifunguye.



![img](assets/en/11.webp)



Ku mugaragaro w'iherezo, uzosanga urutonde rw'amabwirizwa abanzirizwa na `dietpi-` aserukira [ibikoresho](https://dietpi.com/docs/dietpi_tools/) vy'iyi sisitemu:




- `dietpi-launcher`: kugira ngo ugere kuri sisitemu ikoreshwa, umucungerezi wa dosiye, n'ibindi
- `dietpi-Software`: igereranya igikoresho ushobora gushiramwo porogaramu zose zisanzwe ziri muri suite
- `dietpi-config`: kugira ngo ushikire imiterere ya sisitemu, mbere n'iyo iteye imbere cane.



![img](assets/en/14.webp)



### Gusubiza inyuma



Gukora backup ya server ni urutonde umuyobozi wa sisitemu akwiye kwitega kuva atanguye.



Na DietPi hariho itegeko rya `dietpi-Backup`, iryo ndagusavye gutohoza kugira uronke umuti mwiza: rigufasha gushinga ububiko busanzwe, bwo kwongerako canke butazokwongerwa bivanye n’ibikoresho bikoreshwa, n’amahitamwo yose yo guhindura urutonde.



![img](assets/en/22.webp)



Hitamwo aho ububiko buja, nk'akarorero iyindi disiki, mu gutangura `dietpi-Drive_Manager` kugira ngo ushireko umuvuduko w'aho ububiko buja maze ukoreshe kuri iyi nzira.



## Gutunganya



Kwiyakira ni ikintu ciza umuntu wese ashobora gukora, yaba uwushaka kumenya vyinshi canke uwufise igishika gusa. Ariko rero, gukura no gutunganya server birimwo ingorane zimwe zimwe zidasanzwe z’ubuhinga. Aho niho **ukworohereza kwa DietPi** kwinjira, bikagufasha gutunganya uburyo bujanye n’ivyo ukeneye mu ntambwe nkeyi zoroshe.



![img](assets/en/24.webp)



Ivy'ishimikiro n'ivy'imbere, vyose biri ku rutoke rwawe muri Interface imwe iboneka n'itegeko:



```imiterere y'ivyo kurya


sudo dietpi-imiterere


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


porogaramu ya sudo dietpi


```