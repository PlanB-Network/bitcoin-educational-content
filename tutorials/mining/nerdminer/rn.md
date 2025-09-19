---
name: Nerdminer
description: Tangira Mining Bitcoin ufise amahirwe yo gutsinda hafi 0
---

![cover](assets/cover.webp)

## Itunganywa rya NerdMiner yawe v2.


Muri iyi nyigisho, tuzokuyobora mu ntambwe zikenewe kugira ngo ushireho NerdMiner_v2, ari co gikoresho c'ubuhinga (ESP-32 S3) kigenewe Bitcoin Mining.

Biragaragara ko ububasha bwo gukoresha ubuhinga bwa none bw’ico gikoresho butashobora guhangana n’ubuhinga bwa ASIC bw’abacukuzi b’amabuye y’agaciro b’abahinga canke b’abahinga. Naho biri ukwo, NerdMiner ni igikoresho ciza cane co kwigisha kugira ngo Bitcoin Mining ibe ikintu gifatika. Kandi n’uwuzi, n’amahirwe (menshi), woshobora gusanga ububiko n’impera ijana na bwo. Ku bashaka kumenya, tuzobibona mu gice ca [Igereranyo ry’ubushobozi bwo gutsinda](#igereranyo-de-la-probabilité-de-gain). Ku bijanye n’inguvu zikoreshwa, NerdMiner ikoresha 0.5W; kugira ngo tugereranye, itara ry’umuco w’izuba rikoresha incuro 20 kuruta.


Imbere yo guca mu ntambwe zitandukanye, reka dushire ku rutonde ibikoresho bikenewe kugira ngo tuyikore:



- a [Iyerekanwa rya Lilygo S3](https://lilygo.cc/ibicuruzwa/iyerekanwa-t-s3)
- a [Ububasha bwa USB-C Supply]
- a 3D case: nimba ufise icapa rya 3D, urashobora gukuraho [dosiye ya 3D](dosiye y’ibicapo 3D] ahandi ho ushobora kuyigura kuri [Silexperience kuri interineti ububiko] (urubuga rw'ubumenyi bw'ivy'ubuhinga bwa none/NerdMiner_V2-urupapuro rwa 544379757).
- PC ifise umucukumbuzi wa Chrome
- ihuriro rya interineti
- a Bitcoin Address.


Ushobora kandi kugura ikintu ca NerdMiner cakozwe imbere y’igihe ku baguzi benshi nka:



- [Ibikoresho/ibicuruzwa/umunyabwenge-Miner?_pos=1&_psq=umunyabwenge&_ss=e&_v=1.0)
- [Umuhinguzi w'ibice] (https: iduka ry'ibice/)


Mbere, turabona ingene twoca flash iyo software kuri ESP-32 S3, hanyuma turabe ingene twoyisubiramwo kugira ngo duhindure urubuga rwa wifi. Izo ntambwe ni iz'abakoresha Windows, nimba ukoresha Linux OS, usabwe gukora [intambwe z'intango](#etapes-intango-gusuka-abakoresha-linux) kugira ngo wemerere kwemerwa na ESP-32 S3 na sisitemu yawe.


**Gushiramwo porogaramu ya NerdMiner_v2** biroroshe cane kubera gukoresha webflasher.


## Intambwe ya 1: Gutegura Webflasher


Ubwa mbere, ukeneye kuja ku [muco wo kuri interineti wa NM2] (https).


Hanyuma uhitemwo porogarama ihuye na ESP-32 yawe. Akenshi ni yo isanzwe: T-Display S3. Hanyuma ukande kuri "Flash".


**Iciyumviro⚠️ :** ni vyiza ko ukoresha umucukumbuzi wa Chrome - kuko wemerera, ku buryo busanzwe, gukoresha flash no gushika ku bibanza vyawe vya USB.


![image](assets/webflasher.webp)


## Intambwe ya 2: Gufatanya ESP-32


Iyo webflasher imaze gutangura, idirisha rizofunguka ryerekana ama ports atandukanye ya USB yemerwa n’umucukumbuzi.

Ushobora rero gufatanya ESP-32 yawe, hanyuma port nshasha izogaragara (muri iki gihe, ni port ttyACM0). Ubwirizwa rero kuyihitamwo hanyuma ukande kuri "connect".


![image](assets/flasher-port-serial.webp)


Iyo porogarama izoca ija kuri ESP32 yawe mu masegonda makeyi.


![image](assets/NM2-sucessfully-installed.webp)


## Intambwe ya 3: Itunganywa rya NerdMiner


Ivyo gutunganya NerdMiner yawe bizokorwa biciye kuri telefone ngendanwa canke kuri mudasobwa.

Gukoresha WiFi no kwifatanya n'urubuga rwa NerdMinerAP rwo mu karere. Niba ukoresha telefone ngendanwa, urubuga rwo guhindura ibintu ruzokwifungura. Ahandi ho, wandike Address 192.168.4.1 mu mucukumbuzi.

Hanyuma uhitemwo "Gutegura WiFi".


Ubu ushobora gutunganya NerdMiner yawe.

Ubwa mbere, tangura ukoresheje urubuga rwawe rwa WiFi mu guhitamwo izina ry’urubuga rwawe maze winjize ijambobanga ry’urubuga rwawe.


Hanyuma ushobora guhitamwo Mining pool ushaka kwifatanyamwo. Nkako, birasanzwe mu gisata ca Bitcoin Mining gukoranya ubushobozi bwo gukoresha ubuhinga bwa none kugira ngo wongere amahirwe yo kuronka igice muri Exchange co gusangira impembo bihuye n’ivyo Hashrate yatanze.

Ku ba NerdMiners, ushobora guhitamwo kwifatanya na kimwe muri ibi bidengeri:


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

Umaze guhitamwo ikidengeri cawe, ukeneye kwinjira muri Bitcoin Address yawe kugira ngo uronke impembo mu gihe (mu buryo budasanzwe) hoba hariho ivyuma.


Kandi, uhitemwo isaha yawe kugira ngo NerdMiner ishobore kwerekana isaha neza.

Ubu ushobora gukanda kuri "bika".


![image](assets/wifi-configuration.webp)


Urakoze cane, ubu uri mu mugwi wa Bitcoin Mining!


## Ibikorwa vya NerdMiner


Porogaramu ya NerdMinerv2 ifise amashusho 3 atandukanye, ushobora kuyabona ukanda kuri buto iri hejuru iburyo bw’ishusho yawe:



- Igishushanyo nyamukuru kiratanga uburyo bwo kuronka imibare ya NerdMiner yawe.
- Igishushanyo ca kabiri kiratanga uburyo bwo kubona isaha, Hashrate yawe, igiciro ca Bitcoin, n’uburebure bw’ibarabara.
- Igishushanyo ca gatatu kiratanga uburyo bwo kuronka imibare iri ku rubuga rwa Bitcoin Mining rwo kw’isi yose.

![image](assets/NM2-screens.webp)


Niba ushaka gusubira gufungura NerdMiner yawe, nk’akarorero kugira ngo uhindure urubuga rwa WiFi, ukeneye gukanda buto yo hejuru mu masegonda 5.


Gukanda buto yo hasi rimwe bizokuzimya NerdMiner yawe. Gukanda kabiri bizohindura uko igicapo kigaragara.


### Intambwe z'intango ku bakoresha Linux


Aha niho intambwe Chrome ishobora gukoresha kugira ngo imenye port yawe ya serial kuri Linux.


1. Menya neza icambu gifitaniye isano:



- Huza ESP-32 yawe na mudasobwa yawe.
- Gufungura iterefone.
- Injira itegeko rikurikira kugira ngo ubone urutonde rw'ivyambu vyose:
  - `ubutumwa | gushimira tty`
  - canke `ls /iterambere/tty*`
- Kugira ngo umenye neza port, urashobora gukomeza mu gukuraho mu gusubiramwo itegeko ata ESP-32 ihuriweko.


2. Guhindura uruhusha rw'icuma gifitaniye isano:



- Ku mburabuzi, gushika ku nzira z'uruhererekane bishobora gusaba uruhusha rw'imizi, rero tuzozigira ziboneke mu kwongerako umukoresha wawe ku mugwi wa `dialout`.
  - `sudo usermod -a -G ivuga IZINA_RYAWE`, usubirize `IZINA_RYAWE` n'izina ryawe.
  - hanyuma usohoke maze usubire kwinjira nk'uyu mukoresha, canke wongere utangure sisitemu kugira ngo umenye neza ko amahinduka y'umugwi agira ico akoze.


Ubu ESP-32 yawe yemewe na sisitemu yawe, urashobora gusubira ku [ntambwe ya mbere](#etape-1-ugutegura-du-webflasher) kugira ngo ushireho porogarama.


## Iciyumviro


Kandi ng’aho ni ho ufise! NerdMiner_v2 yawe ubu iratunganijwe kandi yiteguye gukoreshwa.


Mining nziza kandi amahirwe abe ku ruhande rwawe!


### Gupima ubushobozi bwo gutsinda


Reka twinovore tugereranye ubushobozi bwo gutsinda Block reward. Ico kigereranyo kizoba ari ikintu gikomeye kandi kirondera gusa kuronka urutonde rw’ubunini bw’ibishoboka.

Ico kigega NerdMiner ashobora gufatanya naco ni "solo Mining pool" gusa bisigura ko ico kigega kitafatanya Hashrate y'abacukuzi bose bahuye ahubwo gikora gusa nk'umuhuzabikorwa.

None reka twiyumvire ko NerdMiner yacu ifise Hashrate ingana na 45kH/s.


Kumenya ko umubare wose wa Hashrate ari nk’ibice 450 EH/s (canke 4,5 x 10^20 hashes ku segonda), turashobora kubona ko ubushobozi bwo kuronka igice gikurikira ari 1 muri miliyari 100 z’amamiliyaridi, ivyo bikaba ari ibintu bidashoboka cane cane cane. Rero uretse kuba igikoresho co kwigisha n’ikintu co kumenya, NerdMiner ishobora gukora nk’itike ya loteri muri Bitcoin Mining ku giciro c’amashanyarazi co ku ruhande ca 0.5 W--naho nk’uko twabibonye, ​​ubushobozi bwo gutsinda ari buke cane. Yamara, kubera iki utorwanya amahirwe yawe?


### Ibindi bisobanuro


Aha hariho amahuza nimba ushaka gusoma vyinshi ku bijanye n’ico kibazo:



- [Umucukuzi_v2 urupapuro rw'umugambi] (http://github.com/Ikigo/Umucukuzi_v2)
- [Inyandiko zuzuye z'abacukuzi b'amabuye y'agaciro] (inyandiko.