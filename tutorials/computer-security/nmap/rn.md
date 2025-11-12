---
name: Nmap
description: Master Nmap ku ikarita y'urubuga no gupima ubugoyagoye
---

![cover](assets/cover.webp)



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Mickael Dorigny vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Hariho ivyo bahinduye mu canditswe c’intango.*



___



Ikaze muri iyi nyigisho y’intango ya Nmap, yagenewe umuntu wese yipfuza kumenya neza iki gikoresho gikomeye co gupima urubuga. Intumbero ni ukuguha ubumenyi bw’ishimikiro ukeneye kugira ngo ukoreshe neza Nmap ku musi ku musi.



Nmap ni igikoresho gishobora gukoreshwa mu buryo bwinshi, gikoreshwa cane n’abahinga mu vy’ubuhinga bwa none, urubuga n’umutekano wo kuri internet mu gupima indwara, kuvumbura urubuga no kugenzura umutekano. Iyi nyigisho igenewe abashasha muri ivyo bikorwa kandi bipfuza kwiga ivy’ishimikiro vya Nmap. Ubumenyi bw’ishimikiro bw’uburongozi bwa sisitemu n’urubuga burakenewe.



Uzokwiga ivy’ishimikiro vya Nmap, ingene wokora port scans, kumenya abashitsi bakora ku rubuga, kumenya verisiyo za service n’imirongo y’ibikorwa, gukora vulnerability scans, n’ibindi vyinshi. Igice cose kirimwo insobanuro zitomoye be n’ingero ngirakamaro zigufasha kumenya neza gukoresha Nmap mu bihe bitandukanye.



Iyi nyigisho izohera, uzoba ufise ugutahura gukomeye kwa Nmap kandi uzoba ushobora kuyikoresha neza kugira ngo utere imbere mu mutekano no mu gucunga imihora yawe. Nimwinovore ivyo musoma.



## 1 - Intangamarara ya Nmap: Nmap ni iki?



### I. Ugushikiriza



Muri iki gice ca mbere, turaza kuraba igikoresho co gupima urubuga rwa Nmap. Turaza kuraba urufunguruzo Elements ukeneye kumenya ku bijanye n’iki gikoresho n’ingene gikora muri rusangi. Ivyo bizodufasha gutahura neza inyigisho isigaye.



### II. Gutangaza igikoresho ca Nmap



Nmap, ku _Network Mapper_, ni igikoresho c'ubuntu, gikoreshwa mu **kuvumbura urubuga, gukora ikarita no kugenzura umutekano**. Ishobora kandi gukoreshwa mu bindi bikorwa nk’**ugukora urutonde rw’urubuga, gupima canke kugenzura**.



Ishobora kumenya nimba abashitsi ku rubuga rwagenewe bakora kandi bashobora gushikwako, ni ibihe bikorwa vy’urubuga bigaragazwa, ni ibihe verisiyo n’ubuhinga bukoreshwa, n’ayandi makuru ngirakamaro yo gusesangura. Nmap ishobora gukoreshwa mu gucapura igikorwa kimwe ku mashini yihariye, canke mu bice binini vy’urubuga, gushika kuri Internet yose.



Inkomezi za Nmap ni nyinshi:





- Ikomeye kandi ishobora guhinduka**: Nmap ishobora gupima imihora minini kandi ikoresha ubuhinga bwo kumenya buteye imbere. Ishigikira UDP, TCP, ICMP, IPv4 na IPv6, kandi ishobora gukora ugutahura verisiyo, gupima ubugoyagoye canke gukorana n’amasezerano. Ubwubatsi bwayo ni ubw’ibice, cane cane kubera inyandiko za NSE (Nmap Scripting Engine), tuzozirabira mu nyuma muri iyi nyigisho.
- Ukworohereza gukoresha**: inyandiko zizwi ni nyinshi kandi ziri ku rugero rwo hejuru. Hariho kandi ibikoresho vyinshi vyo mu kibano bishobora kugufasha gutangura.
- Ugukundwa n'ubuzima buramba**: Nmap yabaye igikoresho co gukoresha mu gisata cayo kuva mu 1998. Verisiyo iriho ubu, mu gihe c'iyi nkuru nshasha, ni 7.95. Naho hariho ibindi bikoresho vy’ibikorwa vyihariye, Nmap iguma ari ikintu gikenewe mu gukora ikarita y’urubuga no gusesangura.



**Nmap ku ma cinema**



Nmap ni kimwe mu bikoresho bikeyi vy’umutekano vyaronse izina ryiza cane mu bantu bose. Iboneka muri film _Matrix Reloaded_, mu gice c’ikigereranyo aho Ubutatu buyikoresha kugira ngo yinjire muri sisitemu:



![nmap-image](assets/fr/01.webp)



matrix: Igishushanyo casubiwemwo kirimwo Nmap



Araboneka kandi mu bindi bikorwa vy’amasanamu.



**Inyishu**



Nk’umuyobozi wa sisitemu hanyuma nkaba umugenzuzi w’umutekano wo kuri internet n’umugenzuzi w’ivy’umutekano wo kuri internet, **ndakoresha Nmap hafi ku musi ku musi** kandi **ndayisaba** ubudasiba** abarongozi ba sisitemu bipfuza gukomeza ububasha bwabo ku mihora no kwongereza ubushobozi bwabo bwo gupima indwara.



### III. Ibikorwa vyo ku rwego rwo hejuru



Nmap iraboneka kuri Linux, Windows na macOS. Ahanini yanditswe mu rurimi rwa C, C++ na Lua (ku nyandiko za NSE). Ikoreshwa cane cane ku murongo w'amabwirizwa, naho nyene hariho n'ibishushanyo nka Zenmap. Ariko rero, turaguhanura cane gutangura n’umurongo w’amabwirizwa kugira ngo utahure neza ingene ukora.



Akarorero koroshe:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Iri tegeko rizosigurwa mu buryo burambuye mu nyuma. Muri iyi nyigisho, tuzoba turiko turakoresha Nmap kuri Linux, ariko ikoreshwa ryayo rirasa n’iry’izindi sisitemu. Mu nsi ya Windows, Nmap yizigira ububiko bw'ibitabu bwa **Npcap** (busubirira WinPcap ubu itagikoreshwa) kugira ngo ifate no gutera amapakete y'urubuga.



Nmap ikoreshwa nk'ibisanzwe, nka `ls` canke `ip`. Ibintu bimwe bimwe biteye imbere bishobora gusaba uburenganzira bwo hejuru, kuko igikoresho rimwe na rimwe gikoresha amapakete mu buryo butamenyerewe kugira ngo kivyure inyishu zidasanzwe ku mirongo y’intumbero (cane cane ku bijanye n’ugukoresha canke kumenya ubugoyagoye).



### IV. Ingaruka zo gukoresha Nmap



Imbere yo gukoresha Nmap, ni ngombwa kumenya ingaruka zishobora kugira ku nzira n'imirongo:





- Ishobora kohereza **ibihumbi canke mbere amamiliyoni y’amapakete** mu gihe gito, bishobora kwuzuza ibikorwa remezo bimwe bimwe vy’urubuga.
- Ishobora generate **amapakete atari meza canke atari mu rugero**, bishobora guhungabanya ibikoresho bimwebimwe (na cane cane ubuhinga bw’inganda).
- Ishobora gutuma haba **inyifato imeze nk’iy’igitero**, ishobora gutuma habaho imburi mu mirongo y’umutekano (firewalls, IDS/IPS, n’ibindi).



Muri rusangi, **Nmap ni igikoresho kivuga cane**, kuko gitanga uruja n’uruza rwinshi kugira ngo umuntu akuremwo amakuru menshi ashoboka. Ni vyiza rero gutahura neza ingene ikora imbere y’uko uyikoresha ku bidukikije bikomeye canke ku bidukikije bikora.



### V. Insozero



Iki gice kiratanga Nmap n’ibintu nyamukuru biyiranga. Twarabonye ko ari igikoresho gihambaye, gikomeye kandi gishobora guhinduka co gukora ikarita y’urubuga. Twaraganiriye kandi ingene ikora n’ivyo ukwiye kwirinda igihe uyikoresha, kugira ngo utegure urutonde rw’ibice bikurikira vy’inyigisho.



## 2 - Kubera iki ukoresha Nmap?



### I. Ugushikiriza



Muri iki gice, turaza kuraba ingene igikoresho co gupima urubuga rwa Nmap gikoreshwa cane. Tuzobona ko ari igikoresho gikoreshwa cane mu bihe vyinshi no mu mirimo myinshi, kandi ko kugifise mu gasandugu kawe k’ibikoresho no kumenya uko wogikoresha neza ari ubuhinga ngirakamaro ata gukeka.



### II. Gukoresha Nmap mu gupima no kugenzura



Nmap ishobora gukoreshwa mu gupima urubuga, kandi, mu buryo bwagutse, mu gukurikirana. Mu buryo bumwe nyene ping ishobora gukoreshwa mu kumenya nimba abashitsi babiri bariko baravugana, Nmap ishobora gukoreshwa mu kumenya ningoga nimba umushitsi ariko arakora, canke nimba igikorwa kinaka kiriko kirakora. Turashimira [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilities/ "Nmap"), turashobora kuronka amakuru nyayo yerekeye igihe c'inyishu y'umushitsi, inzira ifatwa n'amapakete, inyishu itangwa n'igikorwa kinaka, n'ibindi.



Itegeko n'igisubizo bikurikira birashobora gukoreshwa, nk'akarorero, kugira ngo umenye ningoga nimba umukozi w'urubuga ku nzira **192.168.1.18** akora kandi yishura neza:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Koresha Nmap kugira ngo ubone uko urubuga rumeze kuri server iri kure.*



Rero, gukoresha Nmap birarenga "ikigeragezo ca ping" kizwi cane mu gihe c'ibihe vyo gukosora canke gupima. Tuzobona mu nyuma ko hari uburyo bwinshi bukoreshwa na Nmap kugira ngo umenye service iriko iratega yompi ku port imwe, harimwo na verisiyo yayo.



### III. Gukoresha Nmap ku ikarita y'urubuga



Nk'Umuhinguzi w'Ikarita y'Urusobe_, ikarita y'urusobe ni yo ntumbero nyamukuru y'iki gikoresho. Ishobora gukoreshwa mu rubuga rw'aho hantu, canke mu rubuga rwinshi, subnets na VLANs, kugira ngo ushire urutonde rw'abashitsi bose n'ibikorwa vyose bishobora gushikwako. Nmap ituma iki gikorwa cihuta cane kandi kikaba ciza kurusha uburyo bwose bwo gukoresha amaboko.



Nk'akarorero, itegeko rikurikira rishobora gukoreshwa mu kumenya ningoga abashitsi bakora ku rubuga **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Iciyumviro: uburyo bwa `-sP` buratagikoreshwa kandi bwasubiriwe na `-sn`.*



![nmap-image](assets/fr/03.webp)



*Gukoresha Nmap kugira ubone abashitsi bashobora gushikwako ku rubuga*



Tuzobona mu nyuma ko hari uburyo bwinshi bukoreshwa na Nmap kugira ngo hamenyekane nimba umushitsi ashobora gufatwa nk'uwukora, naho yoba atagira a priori yerekana ibikorwa vyose.



### IV. Gukoresha Nmap gusuzuma politike yo kuyungurura



Nmap irafise akamaro ko kuba iy’ukuri: ibiva muri yo bituma bishoboka gushinga intahe ku bintu vy’ukuri, bitandukanye n’inyandiko iyo ari yo yose y’ubwubatsi canke politike yo kuyungurura. Ni igikoresho nyamukuru co gusuzuma ubushobozi bwo gucapura amakuru, kuko bigufasha **kugenzura nimba politike yo kuyungurura iriko irashirwa mu ngiro**.



Mu nzira y’amashirahamwe, ingendo nziza itegeka ko ubuhinga bugabanywa hakurikijwe uruhara rwabwo, uburemere bwabwo canke aho buri. Amategeko yo kuyungurura (kenshi ashirwa mu ngiro biciye ku bihome vy’umuriro) ategerezwa kubuza guhanahana amakuru hagati y’ibice. Ariko ivyo bikoresho akenshi biragoye kandi birashobora gutera amakosa.



Rero, kugira ngo umuntu yemeze ko iyo politike yubahirijwe, nta kintu kiruta ikigeragezo nyaco. Nk’akarorero, urashobora kugenzura ko ibikorwa vy’uburongozi bihambaye (SSH, WinRM, MSSQL, MySQL, n’ibindi) bidashobora gushikwako bivuye mu karere k’abakoresha.



Ikoreshwa rya **Nmap mu kugerageza politike yo kuyungurura** rikwiye kuba ry'urutonde imbere y'uko iyo politike ishirwa mu bikorwa. Ikibabaje ni uko iyo nkuru kenshi irengagizwa.



Mu bumenyi mfise, amakosa menshi yo gutunganya ibintu aragenda ataboneka iyo ata bipimo vy’ukwemeza bihari. Ikosa ryoroshe mu rutonde rwa IP canke ukugenzura amategeko birashobora gusiga akarere kavugwa ko kari ukwako gashobora gushikirwa n’ingorane.



### V. Gukoresha Nmap mu kugenzura umutekano no kugerageza kwinjira



Nmap ifise **ibintu vyinshi vy’ingirakamaro vyo gusuzuma umutekano**, kugerageza kwinjira (pentests), kandi ikibabaje n’abatera.



Ibikorwa vyo kuvumbura urubuga ni ngirakamaro ku muterabwoba, akeneye gutahura topologie y’urubuga inyuma y’ugusenyuka kwa mbere. Ariko Nmap itanga vyinshi kuruta ivyo: ishiramwo moteri y’inyandiko, **vyinshi muri vyo bikaba vyerekeye gutahura ubugoyagoye**.



Nk'akarorero, iri tegeko rishobora gukoreshwa mu kugenzura nimba igikorwa ca FTP cemera guhuza ata mazina, ataco ukeneye guhuza n'amaboko:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Gukoresha inyandiko ya NSE kugira ngo usuzume ko FTP itazwi biciye kuri Nmap.*



Gutahura ubugoyagoye bwa Nmap ni imwe mu ntambwe za mbere mu gusuzuma canke mu kugerageza kwinjira. Bigufasha kumenya ningoga ingingo zimwezimwe zigoyagoya no gutuma utwigoro twawe two gusesangura tugenda neza.



Ariko mwirinde: **ibikoresho vyo gupima ubugoyagoye birafise aho bigarukira**. Nmap ipfuka gusa igice c'iterabwoba, kandi ntiyizera ko ubuhinga butekanye iyo ata ngorane zibonetse. Ni ngombwa rero **gutahura ingene inyandiko zakoresheje igikorwa** ntitwizigire gusa urubanza rwazo.



### VI. Iciyumviro



Twarabonye ko kumenya neza Nmap bishobora gukora ibikorwa vyinshi, kuva ku gupima no kugenzura gushika ku gukora ikarita, gusuzuma politike y’umutekano no gupima ubugoyagoye. Mu gice gikurikira, tuzomanuka ku nitty-gritty maze dushiremwo Nmap.




## 3 - Gushiramwo no gutunganya Nmap



### I. Ugushikiriza



Muri iki gice, tuzomenya ingene twoshiramwo igikoresho co gupima urubuga rwa Nmap kuri Linux na Windows OS. Mu mpera z'iki gice, tuzogira ivyo dukeneye vyose kugira ngo dutangure gukoresha Nmap ku bice vyo muri kazoza. Ubwa nyuma, turaza kubona uduteka twoshobora gusaba iyo dukoreshejwe be n’igituma.



### II. Gushiramwo Nmap munsi ya Linux



Nmap yari yagenewe gukoreshwa ku bikoresho vya GNU/Linux. Nk'inyishu, kandi kubera ubuzima bwayo buramba n'ukumenyekana kwayo, uzoyisanga mu bubiko bwose buzwi bw'ibitabu bikuru vya Unix. Muri iyi nyigisho, nzoba ndiko nkoresha ubuhinga bwo gukoresha bushingiye kuri Debian [Kali Linux]("Kali Linux"). Ariko ushobora kuyikoresha mu buryo bumwe nyene buva kuri Debian ya kera, CentOS, Red Hat canke ikindi cose!



Munsi ya Debian, kugira ngo ugenzure ko Nmap iriho mu bubiko bwawe, ushobora gukoresha itegeko rikurikira:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Inyishu aha yerekana neza ko iyo "nmap" iriho mu bibanza vy'ububiko (aha, ivyo vya Kali [Linux] Kuva ubu, urashobora gushiramwo Nmap biciye ku mategeko asanzwe yo gushiramwo, ntaco kigukurako intwaro muri iki gihe 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Kugira ngo tumenye ko Nmap yashizweho neza, tuzokwerekana verisiyo yayo:



```
nmap --version
```



Ehe igisubizo citezwe:



![nmap-image](assets/fr/05.webp)



igisubizo co kwerekana verisiyo ya Nmap iriho ubu._



Zirikana ukuntu muri iki kigaragaza hariho ububiko bw'ibitabo bwa "libpcap" (_Isoko ry'ibitabu ry'amapakete_) na verisiyo yayo. Ikoreshwa na Wireshark, "libpcap" ikoreshwa na Nmap mu guhingura no gukoresha amapakete no kwumviriza uruja n'uruza rw'urubuga.



### III Gushiramwo Nmap kuri Windows



Kugira ngo ushire kuri sisitemu ikoresha Windows, tangura ukura binary ku rubuga rwemewe (kandi nta wundi!):





- Paje yo gukuraho Nmap ku rubuga rwemewe: [https://nmap.org/gukuraho.html#amadirisha](https://nmap.org/gukuraho.html#amadirisha)




Uzoca ukenera gukuraho ibiharuro bibiri vyitwa `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



nmap y'ugushiraho Windows kuri paji yo gukuraho



Uhejeje kugira iyo binary kuri system yawe, uyikoreshe gusa kugira ngo ushiremwo Nmap. Iyi ni ugushiraho gugororotse, kandi ushobora gusiga amahitamwo yose nk'aya mbere.



Iciyumviro canje ni ugukuraho akazu ka "zenmap (GUI Frontend)". Iyi ni graphical Interface ya Nmap ntakoresha kandi ntazoyivuga muri iyi nyigisho, ariko ntutinye kuyigerageza umaze kumenya neza igikoresho c'umurongo w'amabwirizwa wa Nmap!



![nmap-image](assets/fr/07.webp)



Gukuraho Zenmap iyo ushizeho Nmap kuri Windows



Inyuma y'iherezo ry'ugushiraho Nmap, hashirwaho ugushiraho ubwa kabiri: ukwo kw'isomero rya "Npcap":



![nmap-image](assets/fr/08.webp)



gushiramwo ububiko bw'ibitabu bwa "Npcap" igihe ushiramwo Nmap munsi ya Windows



Iryo ni ryo soko Nmap yizigira mu gucunga itumanaho ry’urubuga, ni ukuvuga kwubaka, kohereza no kwakira amapakete y’urubuga. Kumbure waramaze guhura n’iri soko ry’ibitabu nimba ukoresha Wireshark kuri Windows, kuko na ryo nyene rirayikoresha kandi risaba ko uyishiramwo.



Nk'uko biri kuri Linux, ushobora kwemeza ko Nmap ishizweho mu gufungura Itegeko canke Itegeko [Powershell] (https:



```
nmap --version
```



Ehe igisubizo citezwe:



![nmap-image](assets/fr/09.webp)



igisubizo co kwerekana verisiyo ya Nmap iriho ubu._



Nmap ubu iri kuri Windows. Ushobora kuyikoresha mu buryo bumwe nyene n’ubwo kuri Linux, ukurikije iyi nyigisho.



### IV. Uburenganzira bwo mu karere busabwa gukoresha Nmap



Ariko rero, iyo ukoresheje Nmap, **mbega birakenewe kugira uburenganzira bwo mu karere bushizwe hejuru kuri sisitemu?** Inyishu ni: **bivana**.



Mu buryo bwayo bw'ishimikiro, ni ukuvuga ata kuja kure cane mu gukoresha amahitamwo yayo, Nmap ntibisaba uburenganzira bw'agaciro. Ariko rero, uzoca ubona vuba ko ari vyiza gukoresha Nmap mu gihe c'agaciro ("umuzi" munsi ya Linux, "umuyobozi" canke ikingana na co munsi ya Windows) kugira ngo ushobore kuyikoresha ku buryo bushitse, mu kaga ko kuronka ubutumwa bw'ikosa nk'ubu:



![nmap-image](assets/fr/10.webp)



ubutumwa bw'ikosa munsi ya Linux igihe amahitamwo ya Nmap asaba uburenganzira bw'umuzi._



Yaba kuri Linux canke kuri Windows, hariho ibintu vyinshi aho Nmap izogusaba uburenganzira bwo gukoresha. Imvo nyamukuru ni izi (urutonde rudaheza):





- Kubaka amapakete y'urubuga "raw"**: Nmap ishobora gukoresha uburyo bwinshi bwo gupima, harimwo no gukoresha amapakete n'ubwubatsi buteye imbere. Ivyo ni ko bigenda, nk’akarorero, iyo dushaka gukora TCP SYN scans, zidatera iteka *Three-way handshake* ya kera y’uguhanahana TCP. Kugira ngo ivyo bishoboke, Nmap ikeneye gukoresha ibindi bikorwa bitari ivyo bikomoka ku mirongo y'ibikorwa, bizi gusa kwubahiriza imigenzo myiza mu guhanahana amakuru ku rubuga (ihamagara amasomero ya "Npcap" na "libcap" twabonye haruguru). Ni kubera ko Nmap idakora ibintu mu buryo "busanzwe" ko ishobora gukura amakuru amwamwe yerekeye OSes, services n'ubugoyagoye bumwe bumwe.





- Umviriza uruja n’uruza rw’urubuga**: bimwe mu mahitamwo ya Nmap asaba ko yumviriza urubuga kugira ngo ibone amakuru amwamwe. Ico gikorwa kibonwa ko ari ikintu gihambaye kuri sisitemu zikoreshwa, kuko kigufasha no kwumviriza amakuru y’ibindi bikoresho biri kuri iyo sisitemu. Nka kumwe kwa Wireshark, Nmap irakeneye uburenganzira bwihariye kugira ngo ikore ivyo, ivyo bikaba vyoroshe kuronka mu kuba mu gihe c’uburenganzira.





- Gutega yompi ku bikoresho vy’agaciro**: ku bikoresho vy’ubuhinga, ibikoresho kuva kuri 0 gushika kuri 1024 (TCP hamwe na UDP) bivugwa ko ari ivy’agaciro, ni ukuvuga ko mu buryo bumwe canke bundi bigenewe gukoreshwa mu buryo bwihariye cane kandi rero bikaba birindwa. Naho iyo ari imvo imwe imwe idakoreshwa muri iki gihe, biracari ngombwa ko umuntu agira uburenganzira bumwe bumwe bwo kwumviriza kuri ivyo bivuko, ivyo Nmap ishobora gukora bivanye n’ingene izokoreshwa.





- Kurungika amapakete ya UDP:** Na vyo nyene, kwumviriza porogarama y’urubuga ku bibanza vya UDP (protocole itagira igihugu) bisaba uburenganzira bw’agaciro ku mirongo y’ibikorwa. Igihe rero c’agaciro kizokenerwa nimba wipfuza gukora igipimo ca UDP, ico Nmap izobwirizwa kwumviriza inyishu kugira ngo isesengure inyishu z’ibipimo vyayo.




Kugira ngo tuvuge neza, birashoboka, n’imiburiburi munsi ya Linux, gukoresha Nmap n’ibikorwa vyayo vyose n’amahitamwo yayo ata root mu vy’ukuri. Ivyo bishikwako mu guha _ubushobozi_ bubereye ku bibiri. Ariko rero, ivyo bisaba gukoresha neza kandi bishobora kutaba vyiza nk’ugukoresha Nmap ataco uhinduye n’uburenganzira. Vyongeye, ubu buryo ntibusanzwe kandi burashobora gutera ingorane z’umutekano iyo butunganijwe nabi.



Ariko rero, iki ni ugutandukana gatoyi n’inyigisho yacu ya Nmap, rero tuzoyiheba ubu.



Ku bindi bice vy'iyi nyigisho, wiyumvire ko Nmap yama ikoreshwa nk'"umuzi" (ivuye mu gikoko nk'"umuzi" canke biciye ku itegeko rya "sudo"), canke mu gice c'umuyobozi kiri munsi ya Windows, naho ivyo bitagaragajwe. Ahandi ho, woshobora kubona itandukaniro ritoyi ariko rigaragara n’inyigisho.



### V. Insozero



Ni vyo! Nmap ubu yashizwe kuri sisitemu yacu kandi yiteguye gukoreshwa, nta yindi nzira isaba. Iki gice kirasozera intangamarara n’ugushikiriza Nmap. Nizigiye ko vyatumye akanwa kanyu gatera amazi, kandi ko mufise umushasharo wo gutangura kwimenyereza.



Ku bijanye n’ibintu bikomeye cane, ubu turafise iciyumviro ciza c’ico igikoresho co gukora ikarita ca Nmap ari co be n’ingene gikoreshwa cane, hamwe n’aho kigarukira. Reka tugende!




## 4 - TCP na UDP icuma gikoreshwa na Nmap



### I. Ugushikiriza



Muri iki gice, tuzomenya ingene twokora ivy’ugupima port vyacu vya mbere dukoresheje igikoresho co gupima urubuga rwa Nmap. Turabona ingene twoyikoresha mu gukora urutonde rw’ibikorwa vy’urubuga vyerekanwa ku nzira y’umushitsi, haba hakoreshejwe amasezerano ya TCP canke UDP.



Kuva ubu, wibuke gucapura gusa abashitsi mu bidukikije bigenzurwa ufise uruhusha rutomoye.





- Nk’ukwibutsa: [Itegeko ry’Igihano: Igice ca III: Ibitero ku buryo bwo gutunganya amakuru bwikoresha]




**Nimba udafise iyo gutanga**, ndagusavye inyishu zikurikira z'ubuntu, arivyo gusa!





- [Guca mu gasandugu](https://app.hackthebox.com/ "Guca mu gasandugu"): Urubuga rwo kwimenyereza gutera, Hack The Box iguma itanga ubuhinga bushobora gutera uko ubona ko bikwiye. Amajana menshi y’ama sisitemu araboneka, ariko ikidengeri gishasha c’amamashini 20 kiratangwa ku buntu umwaka wose, umuntu ashobora kugishikako biciye kuri OpenVPN VPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub"): Iyi nzira itanga ubuhinga bwinshi bushobora guhungabana, bushobora gukoreshwa biciye ku VirtualBox (na yo ni umuti w’ubuntu) canke ubundi buryo. Iyo umaze gukuraho, nta VPN ikenewe - vyose ni ivy’aho hantu.




Kandi, urafise umwidegemvyo wo **gukora imashini y’ivy’impwemu** kuri sisitemu yawe ukunda cane maze ukayishirako ibikorwa bitandukanye nk’intumbero z’igerageza. Inyungu hano izoba ari uko uzoshobora kandi kubona ibiriko biraba ku ruhande rwa server mu gihe c’ugupima, cane cane na Wireshark, kandi ufise ukuboko mu ruhome rw’umuriro rwo mu karere igihe tuzokora ivyigwa biteye imbere cane.



Reka tugire ivyo gukora!



### II. Gupima ivyuho vya TCP vy'umushitsi biciye kuri Nmap



#### A. Igikoresho ca mbere ca TCP gicapura na Nmap



Ubu tugiye gukora ama scans yacu ya mbere biciye kuri Nmap. Intumbero yacu hano ni yoroshe: turashaka kumenya ibikorwa vyerekanwa na server y’urubuga twahejeje gushiramwo, kugira ngo turabe nimba hari ikintu tutari twiteze, nk’ibikorwa vy’uburongozi bidakwiye gushikwako, canke ibikorwa vyerekanwa vy’icuma c’ikoreshwa twiyumvira ko ryacitse.



Mu karorero kanje, umushitsi azosuzumwa afise IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Ehe rero igisubizo gishoboka. Turabona Nmap ya kera igaruka ifise amakuru menshi:



![nmap-image](assets/fr/11.webp)



ibisubizo vy'isuzuma ryoroshe rya TCP ryakozwe na Nmap._



Turavye ningoga iki ciyumviro, turatahura ko ivyuho TCP/22 na TCP/80 bishobora gushikira kuri iyi host.



Ku mburabuzi, kandi iyo utayibwiye, Nmap izocapura gusa ivyicaro vya TCP.



#### B. Gutahura ivyavuye mu gupima Nmap yoroshe



Ariko rero, reka tugende intambwe imbere kugira ngo dutahure ico gisohoka: umurongo wose urahambaye, ubwa mbere kumenya ivyo biheze gukorwa, ubwa kabiri ni ugusobanura neza ibivuye mu gupima ubwavyo.



Umurongo wa mbere ni ikintu cibutsa verisiyo n'itariki (ni ngirakamaro mu gushiramwo no kubika mu bubiko!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Umurongo wa kabiri werekana intango y'ibisubizo vy'isuzuma ry'umushitsi "debian.home (192.168.1.19)". Aya makuru azoba ngirakamaro igihe tuzotangura gucapura abashitsi benshi igihe kimwe:



```
Nmap scan report for debian.home (192.168.1.19)
```



Umurongo wa gatatu utubwira ko umushitsi ariko aravugwa ari "Hejuru", ni ukuvuga ko akora:



```
Host is up (0.00022s latency).
```



Ubwa nyuma, Nmap iratumenyesha ko 998 TCP ports zamenyekanye ko zifunze zitagaragara muri:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Ivyo bidukiza hafi imirongo 1.000 y'isohoka isa n'iyi:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Urakoze cane kubera yatuzigamye ivyo!



Kuki 998 "vyafunze" ivyicaro? Kwongerako ivyuho 2 vyuguruye bituma haba 1000, kandi uwo niwo mubare w'ivyuho Nmap izocapura mu miterere yayo y'imbere, atari ivyuho 65535 vya TCP biriho! Tuzobona mu nyuma ko ivyo bishobora guhindurwa vyose kandi vyoroshe. Ariko iyo umushitsi afise igikorwa co kwumviriza ku kivuko kidasanzwe, iki gipimo "ca mbere" ntikizogihishura.



Dukurikije aya makuru, turabona ikintu gishimishije cane: imeza itunganijwe hakurikijwe inkingi zitatu "PORT - STATE - SERVICE":





- Inkingi ya mbere "PORT" yerekana gusa icuma/umurongo ugenewe, kandi birahambaye hano kuraba nimba ari icuma ca TCP (`<icuma>/tcp`) canke UDP (`<icuma>/udp`).





- Inkingi ya "STATE" yerekana uko igikorwa c'urubuga cavumbuwe kuri iki kivuko kiri kandi kigenwa na Nmap ishingiye ku nyishu yaronswe. Ibi bishobora kuba "bifunguye", "bifunze", "biyunguruwe" canke "bitazwi". Tuzobona mu nyuma ingene Nmap itandukanya izo leta zitandukanye.





- Inkingi ya "SERVICE" yerekana igikorwa kigaragazwa ku cambu kivugwa. Ariko rero, urabona ko tutakoresheje uburyo bwo kuvumbura ibikorwa bikora hano. Nmap yishingikiriza ku nsiguro y'aho hantu hagati y'icuma/amasezerano n'igikorwa civugwa ko gihawe: dosiye "/etc/services"




Niwaraba dosiye "/etc/services" kuri sisitemu ya Linux, uzosanga "icuma/umurongo - igikorwa" isa n'iyo yerekanwa na Nmap:



![nmap-image](assets/fr/12.webp)



gukuraho ibirimwo muri dosiye "/n'ibindi/ibikorwa" biri munsi ya Linux._



Ni ngombwa gutahura ko, ubu, Nmap ataco yakoze co kuvumbura ibikorwa bikora. Nk’akarorero, ntivyari gushobora kumenya igikorwa ca SSH kiri inyuma y’icuma ca TCP/80 iyo biba ari uko bimeze. Ni co gituma akamaro ko kumenya gukoresha uburyo bwiza - biriko biraza vuba!



Kumenya gusobanura igisohoka ca Nmap ni igice gihambaye co kumenya neza igikoresho. Inkuru nziza ni uko iyo nzira izoba ahanini imwe, uko ukoresha uburyo bwose.



#### C. Munsi y’igipfukisho: isesengura ry’urubuga biciye kuri Wireshark



Niwaraba neza ibiriko biraba ku rubuga Interface rw’umushitsi ariko arapima server, canke ku rwa server ubwayo, ibikorwa vya Nmap bizotomoka cane. Ivyo nivyo tuzokora hano.



Ivyo nshobora kukwereka hano ni igice gusa c’ivyo biboneka muri Wireshark. Niba ushaka kuja kure, ntutinye gukora network capture wewe nyene mu gihe c’ugucapura, hanyuma ugaca mu vyo vyafashwe.



Muri iki kigeragezo, umurongo wanje wo gupima (192.168.1.18) n’umurongo wanje wo gupima (192.168.1.19) bari ku rubuga rumwe rw’aho hantu.



Nmap itangura no kumenya nimba umushitsi w’intumbero akora ku rubuga rw’aho hantu mu kurungika ubusabe bwa ARP. Iyo ironse inyishu, iramenya ko umushitsi ariko arakora maze igatangura gupima urubuga rwayo:



![nmap-image](assets/fr/13.webp)



_Igisabwa ca ARP casohowe na Nmap kugira ngo hamenyekane nimba umushitsi w'intumbero ariho ku rubuga rw'aho hantu._



Iyo umushitsi azosuzumwa ari ku rubuga rwa kure, Nmap itangura yohereza ubusabe bwa ping maze igerageza gushika kuri bimwe mu bibanza bikunda gushirwa ahabona (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



Igisabwa ca ping casohowe na Nmap kugira ngo umenye nimba umushitsi w'intumbero ashobora gushikwako ku rubuga rwa kure



Iyo ironse inyishu kuri kimwe muri ivyo bigeragezo, ibona ko iyo ntumbero ikora.



Nmap imaze kubona ko intumbero yayo ikora, izogerageza gutorera umuti izina ryayo ry’indangarubuga n’umukozi wa DNS atunganijwe ku ikarita y’urubuga:



![nmap-image](assets/fr/15.webp)



Igisubizo ca dNS ku ntego yo gupima Nmap



Ubu Nmap yamenye intumbero yayo kandi izi ko ikora, itangura gupima port yayo ya TCP:



![nmap-image](assets/fr/16.webp)



tCP SYN gutanga amapakete n'ukwakira RST/ACK mu gihe c'ugupima Nmap



Kugira ngo ubikore, izo, kuri buri port ya TCP iri mu rutonde rwayo rwa mbere, **yohereze amapakete ya TCP SYN maze irindire inyishu**. Mu gicapo kiri hejuru, iraronka amapakete ya TCP RST/ACK avuye kuri server ya scanner, bisobanura "genda, ntaco ubona hano" - mu yandi majambo, izo ports zirafunze. Nk’uko twabibonye mu ciyumviro, ivyo ni ko bizoba ku bivuko vyinshi vyasuzumwe. Uretse ibintu bibiri:



![nmap-image](assets/fr/17.webp)



inyishu ku mpapuro za TCP SYN zoherejwe ku cambu 22, zikora ku ciyumviro co gupima



Mu gicapo kiri hejuru, turabona umuzigo wa TCP SYN/ACK woherejwe n’umushitsi w’intumbero. Ico kivuko kirakora kandi kigaragaza igikorwa. Nmap yemera ko yakiriye inyishu, hanyuma igahagarika ihuriro (TCP RST/ACK). **Uko niko vyamenye ko port TCP/22 ikora**.



Twarabonye hano ko Nmap yubaha "Ugufatanya ibiganza mu nzira zitatu" iyo ikora scanner y'urubuga rwa TCP. Kubera imvo z’ubushobozi, birashoboka ko umuntu ayisaba kudasubiza ivyo server igaruka, gutyo akazigama amapakete ibihumbi vyinshi igihe ariko arasuzuma urubuga runini. Ariko tuzorabira kuri ayo mahitamwo n’ivyo gutuma ibintu bigenda neza mu nyuma mu nyigisho.



Ubu turafise iciyumviro ciza c’ingene twokora TCP scan n’ivyo mu vy’ukuri bishika iyo ikozwe. Twarabonye kandi ko, ku buryo busanzwe, Nmap ikora igikorwa co gupima ivyuma vya TCP ku mubare muto w'ivyuma.



### III. Gupima ivyuho vya UDP na Nmap



#### A. Icyuho ca mbere ca UDP gicapura na Nmap



None reka turabe ingene twocapura ama ports ya UDP y’umushitsi. Nk’uko twabibonye, ​​ku buryo busanzwe Nmap izokwama isuzuma ivyuho vya TCP. Ivyo bishobora gusobanura ko twobura amakuru menshi iyo tutabizi.



Nk’ukwibutsa, ku bijanye n’iki kigeragezo, umurongo wanje wo gupima (192.168.1.18) n’umurongo wanje wo gupima (192.168.1.19) bari ku rubuga rumwe rw’aho hantu.



```
nmap -sU 192.168.1.19
```



Aha, igisubizo kironswa gifise uburyo bumwe n'ubwo bwo gupima TCP, ariko ibikorwa bikora vyerekanywe biri muri `<port>/UDP`, nk'uko bisabwa!



![nmap-image](assets/fr/18.webp)



igisubizo c'isuzuma ryoroshe rya UDP ryakozwe na Nmap._



Ihitamwo "-sU" rikoreshwa mu kubwira Nmap ko ushaka gukora kuri UDP, aho gukora kuri TCP nk'uko biri mbere.



Mu nzira, uzobona ko Nmap isaba uburenganzira bwa "root" ku bipimo vya UDP, nk'uko vyavuzwe mbere mu nyigisho.



iciyumviro: Kuva mu verisiyo za nyuma za Nmap, vyama ari vyiza gukoresha UDP scans n'uburenganzira bw'umuyobozi kugira ngo ubone ibisubizo vyizewe, kuko bimwe bimwe bisaba gushika ku nzira y'urubuga._



UDP scans zishobora gutwara igihe kirekire cane (amasegonda 1100 kugira ngo ukore scanner 1000 ports mu karorero kanje), kubera ukubura "Three Way Handshake" muri UDP, bisobanura ko Nmap izotegerezwa gusubira ku mpapuro zose za UDP zoherejwe, kandi izomenya ko port ari "ifunze" gusa iyo ata certa timein ( returnn). Iyi nyishu iva ku bashitsi ba scanner ntitunganijwe kandi akenshi iragabanywa mu bijanye n’umubare w’inyishu ku segonda, kugira ngo umuntu yirinde ibitero bimwebimwe vy’ugukomeza. Ivyo bitandukanye na TCP, aho haba inyishu ihita ivuye ku mushitsi ya scanner, yaba port yuguruye canke yugarijwe. Tuzobona mu nyuma ingene twobigira neza.



Ingorane ya kabiri kuri UDP ni **uko ama services adahora yishura ku mapaquets yinjira**, vyoroshe cane kuko ivyo ntivyama bikenewe kandi ni ingingo ya UDP. Iyo ari uko bimeze, kandi ata ICMP "port unreachable" yakiriwe, iyo serivisi irashirwako ikimenyetso c'uko "ifunguye|iyunguruwe" na Nmap, nk'uko vyerekanwa ku gicapo kiri hejuru.



#### B. Munsi y’igipfukisho: isesengura ry’urubuga biciye kuri Wireshark



Nk’uko biri ku bijanye n’ugupima kwacu kwa TCP, reka twihweze neza ibiba ku rugero rw’urubuga mu gihe c’ugupima UDP dukoresheje isesengura rya Wireshark. Inyifato ya Nmap mu kumenya nimba umushitsi akora ni imwe.



Itandukaniro ryonyene ry'ukuri iyo uriko urapima UDP ni uko Nmap itazorindira "Gufatanya ibiganza mu nzira zitatu", kuko ubu buryo butaboneka muri UDP (stateless protocol):



![nmap-image](assets/fr/19.webp)



uDP itanga amapakete n'ukwakira ICMP (icuma ntikigera) mu gihe c'ugupima Nmap



Turashobora kubona ku gicapo kiri hejuru ko Nmap izorungika amapakete menshi ya UDP, kandi ikaronka kuri menshi muri yo amapakete ya ICMP "Ico umuntu aja (Port unreachable)" mu kwishura. Ivyo ni ibisanzwe, kuko ari inyishu ibereye isobanurwa na [RFC 1122]("RFC 1122") iyo icuma ca UDP kidashobora gushikwako:



![nmap-image](assets/fr/20.webp)



gukura muri RFC 1122._



Reka twihweze neza iyi nkuru ya Wireshark, yerekana **ibintu bitatu bishoboka** muri UDP:



![nmap-image](assets/fr/21.webp)



urubuga rwo gufata mu gihe c'ugupima UDP ku bibanza bitandukanye bikoresheje Nmap._



Ivyo bibazo bitatu ni ibi bikurikira:





- Exchange ya mbere igizwe n’amapakete no. 3, 4 na 8, 9. Nmap yohereza amapakete ya UDP ku nzira ya SNMP ya kera rero **yubaka amapakete yubahiriza amategeko imbere y'igihe**. Ica ironka inyishu iva kuri server (amapakete no. 8 na 9). Igisubizo: Nmap yararonse inyishu, serivisi "irafunguye".





- Exchange ya kabiri igizwe n'amapakete 6 na 7. Nmap yohereza amapakete ya UDP "ataco amaze" (ata n'imiterere y'amasezerano) ku kivuko UDP/165, maze ikaronka amapaki ya ICMP mu kwishura: "Ico kijako ntikishikako (Ikivuko ntikishobora gushikwako)". Igisubizo: Nmap yaronse inyishu (itari nziza), umushitsi ari hejuru, ariko igikorwa yagerageje gushikako ntikikora kuri iki kivuko, kizoshirwako ikimenyetso c'uko "kifunze".





- Exchange ya nyuma igizwe n’ipaki no. 12: Nmap yohereza "ubusa" umuzigo wa UDP ku cambu UDP/1235. Nta n’inyishu, mbere n’ukwanga kugaragara kuvuye ku mushitsi ya scanner. Igisubizo: Nmap ishira ikimenyetso ku port nk'"open|filtered", kuko idashobora kumenya nimba ivyo biterwa n'ukubaho kw'uruhome rw'umuriro, rwatunganijwe kugira ngo ntirwishure, canke ku gikorwa ca UDP gikora kidasubiza inyishu uko biri kwose (si ngombwa muri UDP).




Ehe igisubizo kigaragazwa na Nmap ikurikije ibi bihe bitatu:



![nmap-image](assets/fr/22.webp)



ibisubizo bishoboka vy'isuzuma rya UDP ryakozwe biciye kuri Nmap._



Ubu turafise iciyumviro ciza c’ingene twokora UDP scan n’ivyo mu vy’ukuri bishika iyo ikozwe. Kugeza ubu twamaze gukoresha Nmap mu buryo bworoshe cane, tutafashe ingingo vy’ukuri y’ivyo bikoresho vyo gucapura, ariko ivyo biriko birahinduka!



### IV. Gutunganya neza icambu gicapura na Nmap



#### A. Kwibutsa inyifato ya Nmap



Nk’uko twabibonye, ​​Nmap ubwayo ihitamwo umubare n’ibibanza vyo gucapura iyo utavuze amahitamwo. Iyi ni yo "default" ikoreshwa na Nmap iyo utayibwiye neza ico ikora. Ivyo bihitamwo mburabuzi vyagenewe gutanga iciyumviro c'ivyambu nyamukuru vyerekanwa, ivyo bikaba bitorwa hakurikijwe incuro z'ivyambu vyerekanywe (ivyambu bikunze kugaragara canke bikunda gukoreshwa) aho guhitamwo mu buryo bw'imibare (ivyambu 1, 2, 3, n'ibindi) kandi no kwirinda gutangura gupima ivyambu bishoboka 65535 vy'ivyambu bishoboka iyo udasobanura app worpri too long and "mburabuzi" gukoresha ikibazo.



**Ivyo bivuko bitorwa gute?**



Ivyo bibanza 1000 bicapuwe mu buryo busanzwe bitorwa hakurikijwe incuro bishika. Ivyo biharuro bicungiwe na Nmap kandi bikavugururwa mu buryo bumwe n’ubwo binary ubwayo n’inyandiko zayo (modules). Ushobora kubona iyi mibare wewe nyene muri dosiye "/usr/imigabane/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



vyakuwe muri dosiye "/usr/imigabane/nmap/nmap-ibikorwa"._



Aha, mu nkingi ya gatatu, turabona ibimeze nk’ibishoboka (hagati ya 0 na 1) canke ugusangira kw’ijanisha. Iyi ni incuro z’ugushika kw’ibarabara/amasezerano yose. Turashobora kubona ko ivyuma bizwi cane (FTP, SSH, TELNET na SMTP muri iki gice) bifise agaciro kanini cane kuruta ibindi.



#### B. Sobanura neza ivyicaro vy'intumbero vy'isuzuma rya Nmap



Ariko rero, mw’isi nyakuri, twoshobora gukenera gucapura gusa icambu kinaka, canke ivyicaro vyinshi, canke urutonde rw’ivyambu bimwebimwe. Nmap ituma vyoroha gukora ivyo nyene, mu buryo bumwe ku bipimo vya UDP na TCP.



**Scan port yihariye biciye kuri Nmap**



Niba twipfuza gucapura icuma kimwe, atari 1000, dushobora gusobanura iki kivuko biciye ku mahitamwo ya Nmap "-p" canke "--port":



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Ivyo bizotuma iyo scanner yihuta cane kandi Nmap izotanga gusa amapakete akenewe kugira ngo imenye nimba umushitsi akora, hanyuma imenye nimba icuma cavuzwe gishobora gushikwako. Ivyo birazigama umwanya nimba ushaka gusa gukora igerageza ryihuse kugira ngo urabe nimba urubuga rwo ku rubuga rwawe rw’iyerekanwa rukiriho.



**Scan ports nyinshi ukoresheje Nmap**



Mu buryo nk'ubwo, turashobora gusobanura ivyuho vyinshi kuri Nmap, dukoresheje uburyo bumwe kandi tugafatanya ivyuho vyavuzwe n'agacamuzingi:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Utitaye ku rutonde, Nmap izosuzuma ivyo bibanza vyose, kandi ivyo gusa biri ku nzira y'umushitsi. Uzobona mu gisohoka ca Nmap ko **itubwira neza ivyicaro vyose n'aho bimeze**, naho vyoba "bifunze". Udakunze inyifato mburabuzi, aho iki gisohoka cose cari gutwara umwanya munini cane:



![nmap-image](assets/fr/24.webp)



*Igisubizo c'isuzuma rya Nmap TCP ku bibanza vyerekanwa.*



**Scan urutonde rw'ivyambu**



Niba umubare w'ibibanza wipfuza gucapura ari munini cane, ushobora kubisobanura ukurikije urutonde, nk'akarorero:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Ego cane, urashobora guvanga no guhuza uko ubona bikwiye, nk’akarorero:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**TCP na UDP icuma co gupima**



Ushobora kandi gukora UDP na TCP scans igihe kimwe, ku bibanza vyatowe:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Uzobona muri aka karorero ka nyuma ko hariho "U:" kugira ngo yerekane icuma ca UDP na "T:" kugira ngo yerekane icuma ca TCP. Aha niho hari igisubizo gishoboka c'ubwo bwoko bw'ugupima:



![nmap-image](assets/fr/25.webp)



*Igisubizo c'isuzuma ry'icuma ca TCP na UDP hakoreshejwe Nmap.*



None iyo ni uburyo bushimishije bwo guhindura ama scans yawe!



**Gusuzuma ivyicaro vyose**



Ubwa nyuma, birashoboka gusobanura ibice binini cane canke bito kuri Nmap. Twarabonye ko urutonde rwa mbere rwatowe na Nmap rurimwo 1000 ports. Turashobora kandi gusaba ivyicaro 100 vy'imbere bikunda gukoreshwa cane, canke 200 vy'imbere, dukoresheje uburyo bwa "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Ubwa nyuma, turashobora kuyisaba gucapura ivyuho vyose bishoboka (vyose 65535), dukoresheje ikimenyetso "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Ivyo vya nyuma bizofata igihe kirekire cane cane na UDP, ariko uzoba uzi neza ko utazobura ivyuho vyuguruye.



*Iciyumviro: Ihitamwo "-p-" ni uburyo bwiza bwo gucapura ivyuho vyose vya TCP. Ku bijanye n’ugupima UDP, ni vyiza ko ugabanya umubare w’ibibanza kubera imvo z’ubushobozi, kuko gupima ibibanza vyose vya UDP bishobora gutwara igihe kirekire cane.*



Mu nyuma mu nyigisho, tuzobona ingene twotuma umuvuduko w’ibipimo vya Nmap bigenda neza kugira ngo bihure n’ivyo dukeneye, ivyo bizoba ngirakamaro cane cane ku bipimo ku bibanza vyose vya TCP na UDP.



### V. Insozero



Muri iki gice, twamaze kuronka imyimenyerezo y'amaboko, rero ubu turazi **ingene dukoresha Nmap mu buryo bw'ishimikiro kugira ngo dusuzume ivyuho vya TCP na UDP vy'umushitsi**. Twaravye kandi mu buryo burambuye ibiriko biraba ku rugero rw'urubuga n'ingene Nmap imenya nimba icuma ca TCP canke UDP gikora canke kitakora**. Ubwa nyuma, turazi ingene twohitamwo neza ivyuho dushaka gucapura n'ivyo **ivyo amahitamwo ya Nmap akora mu vy'ukuri**. Mu bikurikira, tuzosubira gukoresha ubwo bumenyi maze tubukoreshe mu gupima urubuga rwose, harimwo no gukora ikarita y’isi yose no kuvumbura urubuga.




## 5 - Ikarita y'urubuga n'ukuvumbura hakoreshejwe Nmap



### I. Ugushikiriza



Muri iki gice, tuzokwiga ingene wokoresha igikoresho co gupima urubuga rwa Nmap kugira ngo ukore ikarita y’urubuga rwawe. Turabona ingene bishobora gukora neza muri iki gikorwa, biciye mu mahitamwo yavyo atandukanye. Ubwa nyuma, turaza kuraba uburyo butandukanye bwo gusobanura intumbero z’ibipimo vyacu kuri Nmap.



Cane cane, tuzoba turiko turakoresha ivyo twize mu gice ca mbere ku bijanye n’ingene Nmap imenya nimba umushitsi akora kandi ashobora gushikirwa.



Nk’uko vyavuzwe mu ntangamarara ya Nmap, iyi ni Network Mapper. Nk'uko biri, ni igikoresho ciza co gukora urutonde rw'abashitsi bashobora gushikirwa ku rubuga, baba abo mu karere canke abo kure.



**Igaruka ry'umwanditsi:**



Nkako, nk’umugenzuzi w’umutekano wo kuri internet n’umupentester, ndakoresha Nmap mu buryo butunganye igihe nkora ivyigwa vyo kwinjira mu mutima kugira ngo menye aho ndi, ababanyi banje bari ku rubuga rw’aho hantu n’izindi nzira zishobora gushikwako, hamwe n’imirongo iri kuri zo. Intumbero yanje ni yoroshe: gukora ikarita y’urubuga, kumenya ubunini bw’urutonde rw’amakuru na cane cane gucapura aho rwotera.



Ikarata y’urubuga irashobora kandi kuba ngirakamaro mu bijanye no gupima urubuga, kugenzura, gukora ikarita y’itunga (woba vy’ukuri uzi neza ko IS yawe igizwe gusa n’ibiri muri Active Directory canke mu GLPI/OCS Inventory yawe? Bishobora kandi gukoreshwa mu kumenya ko Shadow IT iri muri sisitemu yawe y’amakuru.



### II. Gukoresha Nmap mu gupima urutonde rw'urubuga



#### A. Kuvumbura urubuga rukoresheje ubuhinga bwa Nmap



Ubu rero twokwipfuza gutera imbere maze tugasuzuma urubuga rwacu rwose rwo mu karere. Nta kintu coba coroshe kuruta: ico dukeneye gukora n'ugusubira gukoresha amabwirizwa twabonye mu gice ca mbere, ariko tugaragaze CIDR aho gukoresha IP Address yoroshe.



CIDR (**Inzira y'Imirongo idafise Ivyiyumviro**) ni ikimenyetso "ca kera" co kugaragaza urutonde rw'urubuga n'urugero rwarwo (ukoresheje igipfukisho). Nk'akarorero, "192.168.0.0/24" ni "ubuhinduzi" bw'inyandiko y'icumi "255.255.255.0".



Kugira ngo ukoreshe Nmap mu kugaragaza CIDR, dushobora kuyikoresha gutya:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Birashoboka kandi, nk'uko biri ku vyambu mu gice ca mbere, kugaragaza abashitsi benshi, imihora myinshi, canke urutonde:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Aha niho akarorero k'ibisubizo twoshobora kuronka iyo dukoresheje scanner ku rubuga:



![nmap-image](assets/fr/26.webp)



ibisubizo vya Nmap scan ku ikarita y'imihora myinshi



Cane cane, turabona abashitsi benshi bakora, kandi igice cose c'abashitsi gitangura n'umurongo nk'uyu:



```
Nmap scan report for <name> (<IP>)
```



Ivyo bituma tubona neza uwo mushitsi ibi bikurikira vyerekeye. Umurongo wa nyuma nyene na wo nyene urahambaye:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Turazi ko, ku nzira zasuzumwe, Nmap yabonye abashitsi 5 bakora.



#### B. Munsi y’igipfukisho: isesengura ry’urubuga biciye kuri Wireshark



Ubu tugiye kuraba neza ibiba ku rugero rw’urubuga mu gihe c’ukuvumbura urubuga gukorwa biciye ku Nmap.



Nk’uko twabibonye mu gice ca mbere, ku buryo busanzwe Nmap izokoresha umurongo wa ARP kugira ngo imenye ko hariho abashitsi ku rubuga rw’aho hantu:



![nmap-image](assets/fr/27.webp)



aRP amapakete yafashwe igihe usuzuma urubuga rwo mu karere ukoresheje Nmap n'amahitamwo yayo mburabuzi



Gutyo irashobora kumenya hafi abashitsi bose bari ku rubuga rwo mu karere, kubera ko inyishu y’ikibazo ca ARP muri rusangi itangwa n’abashitsi bose bakora kuri urwo rubuga kandi ntibisa n’ibiteye amakenga mu buryo na bumwe.



Ku nzira zo kure, Nmap ikoresha ubuhinga buhurikiye hamwe:



![nmap-image](assets/fr/28.webp)



iCMP na TCP amapakete yafashwe igihe ukoresha urubuga rwo kure ukoresheje Nmap n'amahitamwo yayo mburabuzi



Kugira ngo tuvuge neza, Nmap ikoresha ICMP echo packet (ikibazo ca kera co gukora ping) n’i ICMP Timestamp, akenshi ikoreshwa mu kubara ibihe vy’uguca kw’amapakete. Irizigiye kuronka inyishu ku bashitsi ku nzira za kure.



Ariko hariho n'ibindi birenze ivyo. Ushobora kubona mu gicapo ca Wireshark kiri hejuru ko amapakete ya **TCP SYN** yoherezwa mu buryo butunganye ku bibanza vya TCP/443 vy’umushitsi wese ashobora kuba ku nzira zizosuzumwa, hamwe n’amapakete ya **TCP ACK** ku bibanza vya TCP/80.



**Kubera iki wohereza amapakete ya TCP ku vyambu nk'igice c'ukuvumbura urubuga?**



Kwohereza umuzigo wa SYN ku kivuko gitanzwe bituma Nmap **menya nimba igikorwa kiriko kiratega yompi kuri ico kivuko**. Iyo umushitsi yishuye ku mpapuro za SYN zifise paketi ya SYN/ACK, ivyo vyerekana ko zikora kandi ko hari igikorwa kiriko kiratega yompi kuri iyo port. Nmap rero iragerageza amahirwe yayo kuri iyi serivisi, **naho ata n’inyishu ku ping yaronswe**.



Kwohereza ACK packet ku port yatanzwe bituma Nmap **menya nimba hariho uruhome rw'umuriro kuri uwo mushitsi**. Iyo umushitsi yishuye ku mpapuro za ACK n’impapuro ya RST (Reset), ivyo vyerekana ko hariho uruhome rw’umuriro kumbure kuri uwo mushitsi kandi rukabuza uruja n’uruza rutasabwe. Uwo mushitsi rero arahemukira kuba ari ku rubuga, naho yoba ataco yishuye ku bindi bisabwa.



Ariko rero, birahambaye kumenya ko gutahura uruhome rw’umuriro hakoreshejwe ubu buhinga bishobora kutaba ari ivyo kwizigirwa ata gatotsi mu bihe vyose. Hari abashitsi bashobora gutanga inyishu za generate RST kubera izindi mpamvu zitari ukubaho kw’uruhome rw’umuriro, nk’ibikorwa vyihariye canke imiterere y’uburyo bwo gukoresha. Ikindi, ibihome vy’umuriro vy’ubu birashobora gutunganirizwa kugira ngo ntivyishure ku kugerageza kuvumbura kw’ubwo bwoko.



Ubu twaciye kure cane kandi turashobora gukora ubuvumbuzi bw’ishimikiro bw’urubuga. Ubu tugiye kuraba izindi nzira nkeyi zizotuma tugira ububasha bwinshi ku nyifato ya Nmap.



### III. Kuvumbura urubuga ata gucapura kw'icuma na Nmap



Nk’uko mushobora kuba mwabibonye, ​​ku buryo busanzwe Nmap **ikora port scan ikurikije ukuvumbura kwayo kw’umushitsi akora**, ivyo bikaba vyongera amapakete menshi cane kandi bitegerezwa inyishu ku scan yacu. Niba ufise abashitsi 5 ku rubuga rwawe, Nmap izogerageza gusuzuma uko ama ports agera ku 5.000 ameze, ivyo bizotwara igihe kirekire.



Ariko rero, birashoboka gukoresha amahitamwo ya Nmap kugira ngo ukore **ukuvumbura gusa abashitsi bakora** ku rubuga, ata kuvumbura ibikorwa vyabo.



Niba dushaka gusa kumenya abashitsi bashobora gushikirwa, ata makuru yose ku bikorwa n'ibibanza bashira ahabona, rero turashobora gukoresha uburyo bwa "-sn" kugira ngo dukore **ugupima gusa dukoresheje ICMP Echo (ping) na ARP requests**. Mu yandi majambo, guhagarika gupima port yose:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Aha niho hari igisubizo c'ukuvumbura urubuga rwa Nmap rwakozwe ata gupima port:



![nmap-image](assets/fr/29.webp)



Inyishu y'ukuvumbura urubuga ata gupima port na Nmap.



Twaramaze kuvuga ingorane zishobora kubaho mu gukoresha ICMP yonyene ku kuvumbura abashitsi (ku mihora iri kure). Ni co gituma Nmap nayo ikoresha ubuhinga bukeyi bushobora guhemukira ukubaho kw’uruhome rw’umuriro canke igikorwa kidasanzwe ku bashitsi. Dufashijwe n’amahitamwo, turashobora gusubira gukoresha ayo mayeri mbere tukayagura, tutabwirizwa gusubira gutangura n’ugupima port yuzuye y’umushitsi wese yavumbuwe.



Kugira ngo ivyo tubikore, tuzokoresha amahitamwo ya "-PS" (TCP SYN) na "-PA" (TCP ACK), ivyo bizotuma dushobora gusobanura ivyicaro twipfuza kwifatanya navyo nk'igice c'ukuvumbura kwacu kw'abashitsi, hamwe n'amahitamwo ya "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Iyi scan iramaze gutuma ukuvumbura kw'abashitsi kuba kwuzuye gatoyi kuruta uko biri ku mahitamwo y'imbere.



Turatangura kuronka amabwirizwa yuzuye cane, dukoresheje uburyo bwinshi. Ivyo ni kubera ko tuzi ingene Nmap ikora n'imipaka y'amahitamwo yayo, bishobora rimwe na rimwe gutuma dutakaza umwanya canke tukabura Elements ihambaye. Iyo ni yo ntumbero yose yo gufata umwanya wo kuyimenya neza!



Kugira ngo usobanure neza amahitamwo y'itegeko ryacu rya nyuma:





- "`-sn`: ibuza gupima icuma kuri buri mushitsi akora yavumbuwe na Nmap.





- "`-PP`: ishoboza ICMP echo (ping scan) ku kuvumbura umushitsi.





- "`-PS <PORT>`": yohereza TCP SYN packet ku port(s) vyerekanwa kugira ngo umenye igikorwa cose gikora kigaragaza ukubaho kw'umushitsi ataco yishuye ku ping.





- "`-PA <PORT>`": yohereza TCP ACK packet ku port(s) yerekanwa kugira ngo umenye uruhome rw'umuriro rwose rukora rugaragaza ukubaho kw'umushitsi atasubije kuri ping.




Mu karorero kari hejuru, ndasobanura ivyicaro mbona ko ari vyo bigaragara cane mu mirongo yanje ya Nmap ku bijanye n'uburyo bwa "-PS". Ivyo bibanza bitandukanye bizoca bigeragezwa kuri buri host, atari kugira ngo turabe nimba service bakira ikora vy’ukuri, ariko kugira ngo turabe nimba ivyo bituma tubona host itasubije ICMP Echo yacu mu gihe ikiriko irakora (biciye mu nyishu iva kuri service canke firewall y’umushitsi).



Ehe ivyo ushobora kubona mu gufata urubuga rwafashwe mu gihe c'ivyo bipimo, muri iki gihe ni igice ku nzira imwe:



![nmap-image](assets/fr/30.webp)



amapakete yoherejwe na Nmap mu gihe c'ukuvumbura urubuga rwo hejuru, ata gupima icuma



Turabona amapakete yacu ya TCP SYN, ACK yacu ya TCP ku cambu TCP/80 n’ijwi ryacu rya ICMP. Nmap izokora ivyo bipimo vyose kuri buri mushitsi agenderewe n’itohoza ryacu ry’ubuvumbuzi bw’urubuga.



### IV. Gukoresha dosiye y'itunga ry'intumbero na Nmap



Gusobanura intumbero birashobora kwihuta kwemeza ko bigoranye mu buryo bw’amakuru y’ubuzima nyakuri, rimwe na rimwe bushobora kuba bugizwe n’imirongo amajana canke amajana, imirongo mito mito n’imirongo mito mito. Ni co gituma vyoroshe gukoresha dosiye nk'inkomoko ya Nmap kuruta kuyisobanura imwe imwe ku murongo w'amabwirizwa.



Kugira utangure, rema dosiye yoroshe irimwo ikintu kimwe ku murongo:



![nmap-image](assets/fr/31.webp)



dosiye irimwo intumbero imwe (umushitsi canke urubuga) ku murongo



Ibikurikira, dushobora gukoresha amahitamwo yose ya Nmap twabonye gushika ubu maze tugasobanura "-iL <inzira/dosiye>" amahitamwo:



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap izoca ishiramwo muri scan yayo ivyifuzo vyose biri muri dosiye yacu.



Niba ushaka kumenya neza ko intumbero zawe zose zizofatwa mu mutwe, ushobora gukoresha uburyo bwa "-sL -n". Nmap izoheza isobanure gusa CIDRs n'abashitsi bari muri dosiye maze ikugaragarize, ata n'amapakete yohereje ku rubuga:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Ivyo bituma urutonde rw’abashitsi bazosuzumwa ruba urwo ukuri.



Impanuro ya nyuma ihambaye nshaka kubasangiza ni iyo **gukuraho umushitsi canke urubuga nk'igice c'ugupima**. Ivyo bishobora kuba ngombwa mu bihe bitari bike, cane cane nimba dushaka kumenya neza ko **igice gihambaye c’urutonde rw’amakuru kitahungabanywa canke ngo gihungabanizwe n’ibipimo vyacu**.



Ingero zikunda gushika z’ivyo bikenewe ni igihe ishirahamwe rifise ibikoresho vy’inganda (PLC) canke vy’ubuvuzi. Mwene ivyo bikoresho rimwe na rimwe birahinguwe nabi, kandi ntibigenewe na gato kwakira amapakete atari meza, canke menshi cane. Kubera imvo zigaragara z’ukuboneka canke ingorane z’ubudandaji/abantu, ni vyiza ko zikurwa mu bipimo.



Kugira ngo dukureho aderesi za IP canke imihora mu bipimo vyacu, dushobora gukoresha uburyo bwa Nmap "--exclude", nk'akarorero:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



Muri aka karorero, ndiko ndasuzuma urubuga "192.168.1.0/24" ariko ntashizemwo umushitsi "192.168.1.140" uri ng'aho. Nta mapakete azorungikwa na Nmap kuri uyu mushitsi. Ikindi kigereranyo n'ugukuraho urubuga ruto:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Nanje nyene ndacapura urubuga runini "10.0.0.0/16", ariko urubuga "10.0.100.0/24" ntiruzocapura. Na none, ndagusavye gukoresha uburyo bwa "-sL -n" kugira ngo ubone neza cane abashitsi bazocapurwa n'abazokurwa mu gucapurwa, cane cane iyo uriko urakorera mu gihe gikomeye.



### V. Kuvumbura urubuga no gupima icuma



Ubu turashobora gufatanya ivyo twize muri iki gice n’ivyo twize mu gice ca mbere ku bijanye n’amahitamwo yo gupima port. Ku mburabuzi, twabonye ko Nmap izocapura 1000 ports zikunda gukoreshwa cane ku host yose ikora ibona. Twarabonye ingene twokwirinda iyo nyifato iyo tutayishaka, ariko turashobora kuyigenzura bimwe bishitse, mbere tukayigwiza iyo ihuye n’ivyo dukeneye.



Nk'akarorero, itegeko rikurikira rizosuzuma ko hariho igikorwa co kwumviriza ku port TCP/22 kuri buri nzira ya scanner:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap izobanza gukora ubushakashatsi ku rubuga kugira ngo ibone urutonde rw'abashitsi bakora, kandi kuri buri wese muri bo, isuzume ko hariho igikorwa ku port TCP/22.



Mu buryo nk'ubwo, turashobora gukora scanner yuzuye y'ibibanza vyose vya TCP ku nzira yose y'umushitsi yavumbuwe ku rubuga rwa "192.168.0.0/24", tutarimwo umushitsi "192.168.0.4" nk'akarorero:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Ufise umwidegemvyo wo gufatanya amahitamwo yose twize gushika ubu kugira ngo ahure n’ivyo ukeneye.



### VI. Iciyumviro



Muri iki gice, twabonye ingene dukoresha Nmap kugira ngo dukoreshe ikarita y’urubuga dukoresheje uburyo butandukanye. Ubu turafise ugutahura neza kw’intumbero z’ibipimo vyacu, hamwe n’inyifato y’ibipimo vy’ivyambu vya Nmap n’uburyo bwo kuvumbura abashitsi. Kandi ikiruta vyose, turazi inyifato n’imipaka ya Nmap, n’ingene twokoresha amahitamwo yayo nyamukuru kugira ngo tugende kure.



Mu gice gikurikira, turaza kuraba uburyo n’uburyo bwo kumenya amaverisiyo y’ibikorwa n’imirongo y’ibikorwa vya scanner na Nmap.




## 6 - Gutahura serivisi n'uburyo bwo gukoresha na Nmap



### I. Ugushikiriza



Muri iki gice, tuzokwiga ingene dukoresha Nmap kugira ngo tubone kandi tumenye neza verisiyo z’ibikorwa n’imirongo y’ibikorwa ikoreshwa n’abashitsi ba scanner. Turaza kuraba mu buryo burambuye ingene Nmap irangura ico gikorwa, hamwe n’aho igikoresho kigarukira kugira ngo dutahure neza no gusobanura ivyavuyemwo.



Nk’uko twabibonye mu bice vya kera vy’iyi nyigisho, ku buryo busanzwe, Nmap ntizoraba kugira ngo ibone igikorwa kigaragara ku bibanza isuzuma kandi ibona ko vyuguruye. Rero iyo uriko wumviriza urubuga ku port TCP/22, Nmap izobandanya kuvuga ko yuguruye, ariko nk'umurongo wa `SSH`. Ivyo ni kubera ko ikoresha [urutonde rw'amakuru](https://www.it-connect.fr/inyigisho-z'uburongozi/ububiko/bdd/) yo mu karere ka sisitemu yawe kugira ngo irondere isano hagati y'icuma/umurongo n'izina ry'igikorwa (dosiye `/etc/services/`).



Mu bihe vyinshi, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnérabilités/) izoguha amakuru akwiriye, kuko ari gake cane mu bidukikije vy’ubuhinga bwo gukora ibintu nk’ivyo. Ariko rero, ibintu bisigaye bizoba ari ibintu aho igikorwa ca kera ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, n’ibindi) kigaragazwa ku nzira itari iya kera (nk’akarorero 2022 ku gikorwa ca SSH), muri ico gihe i ma’ fints a local data N ntibihuye n’ukuri, kandi uzobura amakuru ahambaye.



Ikintu ciza, Nmap itanga uburyo n’uburyo bwo kumenya neza igikorwa nyaco coshobora kuba cihishije inyuma y’icuma kigutse. Mbere irafise urutonde rw’ibibazo n’imikono kugira ngo imenye ubuhinga nyabwo n’amaverisiyo. Uretse ibikorwa, Nmap irashobora kandi kumenya ubuhinga bukoreshwa n’uburyo bukoreshwa.



Ivyo ni vyo tuzoba turiko turaraba muri iki gice.



### II. Uko womenya ubuhinga canke verisiyo



#### A. Kwibutsa ingene womenya ubuhinga canke verisiyo



Kumenya ubuhinga na verisiyo birimwo kugarura izina rya serivisi, CMS, porogarama canke porogarama yumviriza ku cambu kigenewe. Nk’akarorero, urubuga rurongowe na CMS (`WordPress`), rurongowe na serivisi y’urubuga (`Apache`, IIS, Nginx) kandi rurongowe na server (Linux canke Windows). Ariko none womenya gute ko ari uruhe rubuga ruriko rurakora?



Uburyo bwa kera bwo kumenya ayo makuru ni _banner grabbing_, bugizwe gusa no kumenya aho iyo serivisi ivugwa yerekana ayo makuru no gusoma amakuru. Kenshi cane, mu gutunganya canke gutunganya, ibikorwa vyerekana izina ryavyo mbere n’ivyo bikoreshwa nk’inyishu ya mbere inyuma y’uguhuza.



![nmap-image](assets/fr/32.webp)



kugaragaza verisiyo igihe nyene ihuriro rya TCP rishinzwe na serivisi ya FTP



Aha turabona ko guhuza TCP yoroshe n'iyi serivisi biciye kuri `telnet` bivamwo umuzigo wa TCP urimwo ubuhinga bwayo na verisiyo yayo.



Umaze kuronka iciyumviro c’ubwoko bw’igikorwa uriko urakora, urashobora kandi kohereza amabwirizwa canke ibisabwa vyihariye kuri ico gikorwa kugira ngo ukuremwo amakuru. Ivyo bisabwa/amabwirizwa birashobora kandi gutumwa ataco bizi (ataco umuntu azi neza ko ari ubwoko bwiza bw’igikorwa), mu cizigiro c’uko kimwe muri vyo kizotuma haba inyishu iva ku gikorwa kivugwa.



Mu bindi bihe, biteye imbere cane, birakenewe kohereza amapakete yihariye kugira ngo bitere inyishu, nk’ikosa, rizotanga amakuru arambuye yerekeye verisiyo canke ubuhinga bukoreshwa.



Nk’uko mushobora kubibona, Nmap izokoresha ubu buhinga bwose kugira ngo igerageze kandi imenye ubwoko nyabwo bw’igikorwa gicumbikiwe ku cambu, hamwe n’izina ry’ubuhinga bwaco n’uburyo bwaco.



#### B. Gutahura amatohoza ya Nmap n'ibihuye



Kugira ngo ukore ivyo vyose ku port yose ya scanner, Nmap ikoresha urutonde rw'amakuru rwo mu karere ruhora ruvugururwa (nk'uko nyene binary canke modules zayo). Iyi ni dosiye y'inyandiko y'imirongo ibihumbi vyinshi: `/usr/gusangira/nmap/nmap-service-probes`.



Iyi dosiye igizwe n'ibintu vyinshi, vyose bitunganijwe bishingiye ku ngingo ngenderwako zibiri:





- I `Probe`: iyi ni insobanuro y'ipakete Nmap izorungika mu kugerageza gutuma habaho inyishu iva ku gikorwa kizomenyekana. Wiyumvire nk'ukugerageza kw'impumyi nka _Hello? Ikimenyetso ca Guten? Mwaramutse? Um... Buenos kumbure?_. Igihe nyene iyo serivisi igenewe kwakira itohoza itahura (ni ukuvuga kuvuga porotokole ibereye), izokwishura Nmap, iyo serivisi izoca igira ivyemezo vy’ubwoko bwa serivisi ari yo.





- Match": izo ni imvugo zisanzwe Nmap ikoresha ku nyishu yaronswe. Niba kohereza ubusabe bwa HTTP GET vyatumye haba inyishu iva kuri serivisi, izokoresha amajambo asanzwe menshi kuri iyi nyishu kugira ngo imenye ko hariho, nk'akarorero, ijambo `Apache`, `Nginx`, IIS`, `Mi.




Hariho n'ayandi mabwirizwa makeyi ku bibazo vyihariye, ariko ayahambaye yo gutahura ingene Nmap ikora no guhindura ikoreshwa ryayo ni aya. Kugira ngo iki gice c'inyigisho kibe nyaco, ng'akarorero:



![nmap-image](assets/fr/33.webp)



akarorero k'itohoza muri dosiye ya Nmap `/usr/gusangira/nmap/nmap-ibikorwa-itohoza`



Mu murongo wa mbere w'aka karorero, turabona Probe yoroshe gutahura yitwa `GetRequest`. Iyi ni ipaki ya TCP irimwo ubusabe bwa HTTP GET ku muzi wa serivisi y'urubuga hakoreshejwe HTTP/1.0, ikurikiwe n'umurongo w'ifunguro n'umurongo w'ubusa.



Umurongo wa `ports` ubwira Nmap ku port yo koherezako iyi Probe. Ivyo bituma ushobora gushiramwo imbere ibizame kandi ukazigama umwanya.



Ubwa nyuma, turafise ingero zibiri z'`uguhuza`. Irya mbere, nk'akarorero, rizoshira mu rutonde rwa serivisi y'urubuga rwa scanner nk'`ajp13` nimba imvugo isanzwe iri muri uyu murongo ihuye n'inyishu ya serivisi yaronse.



Kugira ngo ushobore gutahura uko ama Probes ashobora gusa, ng’uru urutonde rw’ama Probes uzosanga muri iyi dosiye (hari 188 yose hamwe igihe nandika iyi nyigisho).



![nmap-image](assets/fr/34.webp)



akarorero k'Ibipimo vyinshi bikoreshwa na Nmap kandi biri muri dosiye `/usr/share/nmap/nmap-service-ibipimo`._



Ivyo bibiri vya mbere (vyitwa `NULL` na `GenericLines`) birahambaye cane hano, kuko birungika gusa umuzigo wa TCP utagira ikintu canke uwurimwo umurongo. Ibikorwa vya server akenshi vyimenyesha neza neza igihe nyene umuntu abona ko hariho uruja n’uruza, ata gikorwa, itegeko canke igisabwa kivuye ku mukiriya.



Ehe ikibazo c'umukino ugoranye cane:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Invugo nyayo isanzwe iri hano hagati ya `m|` na `|`, igabanya invugo isanzwe yose muri iyi dosiye. Turagusavye ufate umwanya wo gusoma aka karorero kose. Uzobona ihitamwo mu mvugo isanzwe: `([\d.]+)`, ikoreshwa mu gutandukanya verisiyo. Aka karorero kandi gasobanura izindi Elements nk'izina ry'igicuruzwa `p/nginx/`, verisiyo yagaruwe `v/$1/` na CPE ifise verisiyo `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Common Platform Enumeration) ni uburyo bwo kwandika busanzwe bukoreshwa mu kumenya no gusobanura porogarama n’ibikoresho. Ubu buryo burashoboza gucunga neza cane ubushobozi bwo guhungabana n’imiterere y’umutekano, kandi ikiruta vyose uburyo bumwe bwo kubiserukira, uko igicuruzwa coba ari ikihe. Aha hari ingero zibiri za CPE: `cpe:/o:microsoft:amadirisho_8.1:r1` na `cpe:/a:apache:http_server:2.4.35`



Aha turabona neza ubwoko bwavyo `o` ku OS, `a` ku bikorwa, umucuruzi, igicuruzwa, na verisiyo.



Rero, mu gihe _bihuye_ n'imwe muri izo mvugo zisanzwe, ntituzoronka izina rya serivisi gusa, ariko kandi n'uburyo bwayo na CPE nyayo, bikaba vyoroshe kuronka CVE zigira ingaruka kuri iyi verisiyo. Uzosanga aya makuru mu gisohoka ca Nmap, kandi uzobona ko ari ngirakamaro cane ku zindi ntumbero tuzovuga mu bice bikeyi.



Inyuguti nyayo ya _matches_ na, muri rusangi, y'amabwirizwa ari muri dosiye `/usr/share/nmap/nmap-service-probes` ntihagarara aho, kandi ishobora gusa n'iyigoye cane nimba utamenyereye gukoresha Nmap n'ibisubizo vyayo. Ariko rero, ukwiye kuguma wibuka ukubaho kwayo n’ingene ikora muri rusangi, ivyo bizokugirira akamaro mu nyuma igihe wipfuza gutahura canke gukosora igisubizo, guhindura igicapo canke mbere gutanga umusanzu mu gutegura Nmap.



### III. Gukoresha Nmap kugira ngo ubone verisiyo



Ubu tugiye gukoresha ubu buhinga bwose bukomeye bwa _Probe_ na _Match_ biciye ku mahitamwo yoroshe: `-sV`. Ivyo bibwira Nmap gusa: gerageza kumenya neza neza ibikorwa n'amaverisiyo y'ivyambu washizeho nk'ibifunguye.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Aha niho akarorero kuzuye k'ivyavuye muri iryo tegeko:



![nmap-image](assets/fr/35.webp)



ibisubizo vy'ukumenya verisiyo ya Nmap y'ibikorwa vyerekanwa ku rubuga



Aha turabona ko Nmap yashoboye kumenya verisiyo zose z'ibikorwa vy'urubuga vyashizwe ahabona n'iyi ntumbero, kandi igaragaza ayo makuru mu nkingi nshasha ya `VERSION`. Birashoboka kubona amakuru nyayo, mbere no gushika kuri sisitemu ikoresha, nimba ayo makuru ari igice c'umukono wagaruwe.



Kugira ngo dutahure mu buryo burambuye ibiba mu gihe c'ugupima ubugoyagoye, turashobora gukoresha uburyo bwa `--version-trace`. Ibi bizotanga uburyo bwo gukosora, vyerekana _Itohoza_ ryatumye bimenyekana:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Ivyo bizotuma tugira amakuru menshi yo gutoranya. Gerageza kumenya imirongo itangura na `Igikorwa co gupima Hard gihuye`. Uzoca ubona imirongo nk'iyi:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Turashobora kubona neza _Probes_ zakoreshejwe mu kumenya ubuhinga na verisiyo (muri iki gihe `NULL` na `GetRequest` _Probes_), hamwe n'amakuru yaronswe.



### IV. Kumenya neza ibipimo no kumenya neza



Ubu tugiye gusubira ku mabwirizwa ari muri dosiye `/usr/share/nmap/nmap-service-probes` tutaravye mbere:



![nmap-image](assets/fr/36.webp)



amabwirizwa y'amatohoza `ubuke' muri `/usr/gusangira/nmap/nmap-service-amatohoza`._ dosiye



Iri tegeko rikoreshwa mu kwerekana ubuke (i.e. imbere/ibishoboka) bifitaniye isano n'_Itohoza_. Iyi notation kuva kuri 1 gushika kuri 9 iragufasha kugenzura ukuntu isesengura rikorwa na Nmap ryuzuye igihe wohereje _Probes_. Mu nzira ya "notation" ya Nmap, rarity ya 1 itanga amakuru mu bihe vyinshi cane, mu gihe rarity ya 8 canke 9 igereranya ikibazo kidasanzwe cane, kidasanzwe ku ntunganyo canke igikorwa kidasanzwe kiboneka.



Kugira ngo bisobanuke neza, mu gihe c'imbere, Nmap izorungika kuri buri serivisi kugira ngo imenyekane _Probes_ zifise rarity kuva kuri 1 gushika kuri 7. Kugira ngo ubone iciyumviro ciza c'ugusangira kwa _Probes_ ku _rarity_, ng'iyi igiharuro cazo:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Bishobora gusa n’ibihushanye n’ivyo umuntu abona, hariho `rarity` 8 na 9 kuruta ibindi. Ivyo ni kubera ko rarity 1 Probes ari generic kandi zikora mu bihe vyinshi, ataco zitwaye (wibuke `NULL` Probe yohereza gusa umuzigo wa TCP utagira ikintu). Mu gihe ama Probes akomeye cane ari hafi y’iyidasanzwe ku gikorwa cose.



Niba twipfuza gukoresha n'amaboko ama Probes twipfuza gukoresha mu gupima verisiyo yacu, dushobora gukoresha uburyo bwa `--version-intensity`. Dore ingero zibiri:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Kugira ngo duheze kuri iyi nkuru, ng'aka karorero ka _Probe_ 9 na 8:



![nmap-image](assets/fr/37.webp)



ingero z'Itohoza ku gake 8 na 9 muri dosiye `/usr/gusangira/nmap/nmap-service-itohoza`._



Izo _Probes_ zibiri zitahura ama server ya Quake1 na Quake2 (umukino wa videwo). Birashimishije ku ruhande rw’ugukumbura, ariko ntibishoboka ko vyogira akamaro kanini mu buzima bwa misi yose.



Bivanye n'ivyo ukeneye kugira ngo ukore neza canke wihute, wibuke ko iyo ngingo ngenderwako y'ubukene` iriho kandi ishobora kugira ico ikoze ku ciyumviro.



### V. Gukoresha Nmap kugira ngo umenye uburyo bwo gukoresha



Ubu turaza kuraba ingene Nmap ishobora kudufasha kumenya uburyo bwo gukoresha abashitsi basuzumwe kandi bamenye ku rubuga. Kugira ngo ubikore, koresha uburyo bwa Nmap `-O` (ku `OS Scan`).



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Ehe akarorero k’ivyo vyavuyemwo. Aha, Nmap itubwira ko bishoboka ko ari Linux OS, kandi ikaduha imibare itandukanye yerekeye verisiyo yayo nyayo.



![nmap-image](assets/fr/38.webp)



kumenya ubushobozi bwo kumenya uburyo bwo gukoresha na Nmap



Kugira ngo ivyo bishoboke, Nmap izokoresha ubuhinga bwinshi bukora mu buryo busa cane na _Probes_ na _Matches_ ku bijanye n’ubuhinga n’ugutahura verisiyo. Itandukaniro rikomeye ni uko Nmap izokoresha neza "urugero ruto" rw'ibipimo vya ICMP, TCP, UDP n'ibindi bipimo. Aha hari ingero zibiri z'ikigeragezo co kumenya sisitemu ikoresha Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



ingero z'ibipimo vyakozwe na Nmap kugira ngo imenye Windows 11 OS



Reka tuvyiyumvire, ivyo bipimo biragoye cane gusobanura, kandi ntituzogerageza kubitahura mu buryo bwimbitse mu bijanye n’inyigisho y’intango ya Nmap. Niba ushaka kwimba cane mu ciyumviro, dosiye irimwo aya makuru ni `/usr/share/nmap/nmap-os-db`.



Ariko rero, urakeneye kumenya ko gutahura OS ari ikintu gishoboka gishingwa na Nmap kuruta ikintu kidakeka.



### VI. Iciyumviro



Muri iki gice, twarize ingene twokoresha amahitamwo ya Nmap yo kumenya ubuhinga, verisiyo n’imirongo y’ibikorwa vy’abashitsi n’ibikorwa vya scanner. Ubu turatahura neza ingene Nmap igenda mu kuronka ayo makuru kure. Twarasubiyemwo kandi uburyo bwo gucunga amajambo menshi n’ukuri kw’ibipimo, hamwe n’aho igikoresho gishobora gushika kuri ivyo bintu.



Mu gice gikurikira, tuzomenya ingene dukoresha inyandiko za NSE za Nmap kugira ngo dukore isesengura ry’umutekano w’urutonde rwacu rw’amakuru. Fata umwanya wo gusubira gusoma ibice vya nyuma nimba ukeneye, kandi ntukekeranye kwimenyereza no kwinjira mu mara y’ico gikoresho wewe nyene kugira ngo umenye neza ivyo twize gushika ubu.




## 7 - Isesengura ry'umutekano: kumenya aho umuntu ashobora guhungabana



### I. Ugushikiriza



Muri iki gice, tuzokwiga ingene dukoresha igikoresho co gupima urubuga rwa Nmap kugira ngo tumenye no gusuzuma ubugoyagoye ku ntumbero z’ugupima kwacu. Cane cane, turaza kuraba uburyo butandukanye bwo gukora ico gikorwa, no kwiga imipaka y’ubushobozi bw’ico gikoresho kugira ngo dushobore gutahura neza no gusobanura neza ivyo kivamwo.



Muri iki gice ca mbere, turaza kuraba igikoresho ca Nmap co gupima ubugoyagoye, maze turabe ingene twokoresha uburyo bw’ishimikiro bwo kumenya ubugoyagoye. Mu bice bikurikira, turaza kwihweza neza ingene iyo nzira ikora, n’ingene ishobora guhindurwa.



### II. Gukoresha Nmap kugira ngo umenye ubugoyagoye



Ubu turashaka gukoresha igikoresho co gupima urubuga rwa Nmap kugira ngo tumenye aho ubugoyagoye buri mu bikorwa no mu mirongo y’amakuru yacu. Ivyo bisigura ko uretse kumenya abashitsi bakora, guharura ibikorwa vyerekanwa no kumenya verisiyo n’ubuhinga, Nmap izorondera aho ishobora guhungabana.



Kugira ngo ivyo bishoboke, Nmap yizigira inyandiko za NSE (_Nmap Scripting Engine_), zishobora kubonwa nk’ibice bishobora gutuma habaho uburyo bwo kugerageza.



Hamwe n’amahitamwo akwiye, tuzosaba Nmap gukoresha inyandiko zayo zitandukanye za NSE kuri buri serivisi yavumbuwe, bidushoboze kuvumbura:





- Amakosa yo gutunganya ;





- Ibindi n'ibindi biteye imbere cane vya verisiyo na OS vyavumbuwe ;





- Ivyiyumviro bizwi bishobora gutuma umuntu agira ingorane (CVEs) ;





- Ivyerekana intege nke ;





- Ikiranga Elements c'indwara y'umugera wa malware ;





- Guhakana ubushobozi bwo gukora ;





- N'ibindi.




Nk’uko mubibona, inyandiko za NSE ziragwiza cane ubushobozi bwa Nmap mu bijanye n’ibikorwa vy’urubuga ishobora gukora. Kandi ivyo kugira ngo bakore ibikorwa biteye imbere cane kuruta uko vyari bimeze kera. Inkuru nziza ni uko, nk’uko bisanzwe, ivyo bintu bishobora gukoreshwa gusa biciye ku mahitamwo no mu gihe c’imbere. Ivyo ni vyo tuzobona mu nyuma.



### III. Akarorero k'ugupima ubugoyagoye



Ivyanditswe vya NSE birashobora gukoreshwa iyo ukoresheje Nmap kugira ngo ukore scanner port imwe ku host, ibikorwa vyose biri kuri iyo host canke ibikorwa vyose vyabonetse ku nzira nyinshi. Turashobora rero gukoresha amahitamwo tugiye kubona mu bihe vyose twize gushika ubu.



Kugira ngo dushobore gupima ubugoyagoye biciye mu gupima Nmap, dukeneye gukoresha uburyo bwa `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Ibuka ko ku buryo busanzwe, iyo ataco uvuze, Nmap izoca gusa ku nzira 1000 zisanzwe. Ntizomenya ubugoyagoye ku bivuko vy’agatangaza cane ivyo ushaka gushiramwo bishobora gushirwa ahabona.



Imbere yo gukoresha iyo nzira kuri sisitemu y’amakuru y’ibikorwa, ndagutumiye ngo ukomeze gusoma inyigisho. Mu bice bikurikira, turaza kuraba ingene twogenzura neza ingaruka n’ubwoko bw’ibipimo bizokorwa.



Mu gusubira gukoresha ivyo twize mbere, turashobora, nk’akarorero, kurushiriza gutahura no gupima ivyicaro vyose vya TCP vy’intumbero:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Ehe igisubizo c'isuzuma rya Nmap hakoreshejwe inyandiko za NSE:



![nmap-image](assets/fr/40.webp)



akarorero k'ibisubizo vy'ugupima ubugoyagoye ku mushitsi biciye kuri Nmap._



Aha turabona ukuntu amakuru y’inyongera y’inyungu yerekanwa mu bijanye n’isesengura ry’ubugoyagoye:





- Servisi ya FTP ishobora gukoreshwa ata wuzi, kandi ntiyikingiwe n'ukwemeza. Inyandiko ya NSE ishinzwe ivyo kugenzura iratubwira gutyo, kandi mbere yerekana igice c’imiterere y’igiti c’igikorwa ca FTP. Aha turabona ko dufise uburenganzira bwo gushika ku bubiko bwa `C` bwa Windows system!





- Inyandiko ya NSE ishinzwe gukuraho urubuga rwo ku rubuga rwo hejuru yerekana umutwe w’urupapuro, bikaduha iciyumviro ciza c’ico urubuga rwakira.





- Turafise kandi isesengura ritoyi ry'imiterere y'ibikorwa vya SMB (inyandiko `smb2-igihe`, `smb-uburyo-bw'umutekano` na `smb2-uburyo-bw'umutekano`). Amakuru yerekanwa mu buryo butandukanye gatoyi, inyuma y’igisubizo c’ugupima urubuga, kugira ngo yorohe gusoma. Cane cane, ayo makuru yerekana ko ata mikono ya SMB Exchange iriho. Ubu bugoyagoye bw’imiterere butuma iyo ntumbero ikoreshwa mu gitero ca SMB Relay, akaga gakomeye k’umutekano gakoreshwa kenshi mu bigeragezo vy’ugutera/ugutera kuri interineti.




Ego ni ko, ako ni akarorero kamwe gusa. Nmap ifise inyandiko za NSE ku bikorwa vyinshi, zigamije guhungabana cane. Ivyo bintu bishoboka tuzovyihweza neza mu kigabane gikurikira.



Kugira ngo dusozere iyi ntangamarara y’ugupima ubugoyagoye, ng’iyi itegeko ryuzuye ryo kuvumbura urubuga, gupima icuma ca TCP, verisiyo n’ugupima ubugoyagoye:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Ehe itegeko ritangura gusa n'ibintu vy'ukuri vy'ikoreshwa rya Nmap!



### IV. Gutahura aho Nmap igarukira mu gupima ubugoyagoye



Reka tuvyisobanure neza: Nmap ntishobora gukora ikigeragezo c’ukwinjira mu buryo bushitse mu bijanye n’amakuru yawe, canke kwigana igikorwa ca Red Team. Iriko imipaka myinshi ukwiye kumenya nimba udashaka kugira inyiyumvo y’ikinyoma y’umutekano:





- Igikoresho gifise aho kigarukira**: naho inyandiko za NSE za Nmap zifise ububasha, igikoresho cazo co kugerageza gishobora kuba gito ugereranyije n’ibindi bikoresho vyihariye vyo kuvumbura ubugoyagoye. Hariho ingorane zishobora kutavugwa n’inyandiko za NSE zihari, nk’ingorane za Active Directory, gushikiriza amakuru y’agaciro canke ibintu biteye imbere cane vy’ibikorwa vy’urubuga bishobora guhungabana.





- Ubugoyagoye bw’ubugoyagoye**: ubwoko bumwe bumwe bw’ubugoyagoye bushobora kugora kumenya hakoreshejwe inyandiko za NSE kubera ubugoyagoye bwabwo. Nk’akarorero, ubugoyagoye busaba gukorana n’igikorwa co kure bushobora kutamenyekana neza na Nmap (nk’uko bigenda ku ruhusha rwinshi mu gusangira dosiye canke akaga ko kugenzura uruhusha mu gukoresha urubuga).





- Passive detection**: Nmap yibanda canecane ku bipimo bikora kugira ngo imenye aho ishobora guhungabana, ivyo bisigura ko ishobora kutamenya neza aho ishobora guhungabana ata gushinga ubucuti bukorana n’abayikira. Ivyiyumviro bitagaragara mu gihe c’ugupima bishobora rero gutakara (nk’uko bigenda iyo umuntu ateye kode mu gikorwa co ku rubuga).





- Ivyiyumviro bishasha**: [urutonde rw’amakuru] rwa Nmap rw’inyandiko za NSE ruguma rutera imbere, ariko hashobora kubaho ugucererwa hagati yo kuvumbura ubugoyagoye bushasha bujanye n’inyandiko ya Np. Ivyo bishobora gutuma Nmap idashobora kwama iri ku rugero rwo hejuru n’ibintu bishasha bishobora gutuma umuntu agira ingorane.





- Ivyiza vy’ibinyoma n’ibibi vy’ibinyoma**: nk’uko bigenda ku gikoresho cose c’umutekano, inyandiko za NSE za Nmap zirashobora gutanga ivyiza vy’ibinyoma (imburi z’ibinyoma z’ubugoyagoye) canke ivyiza vy’ibinyoma (ubugoyagoye nyabwo butabonetse). Ivyo ni ikintu co kwibuka igihe usesangura ibisubizo vya Nmap.




Ni ngombwa rero gutahura ivyo Nmap ikora n’ivyo idakora, kandi nk’uko nyene ukamenya gusobanura ivyavuyemwo. Cane cane, twabonye muri iyi nyigisho yose ko amahitamwo y’imbere ashobora kudutuma tubura Elements ihambaye ishobora gupfukurwa hakoreshejwe twitonze.



Waba uri umuyobozi w’umurongo w’urubuga, umuhinga mu vy’umutekano canke mbere CISO, gukoresha Nmap biguha icegeranyo c’ingene umutekano w’umurongo w’amakuru uri. Iyi ni intambwe ya mbere ihambaye mu gucungera ubuhinga, bushobora gukorwa ubudasiba n’umugwi w’abahinga mu vy’ubuhinga bwa none. Ariko rero, ntibikwiye gusubirira ubufasha n’impanuro z’abahinga [mu vy’umutekano wo kuri interineti] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), bazoshobora guhishura intege nke mu buryo burambuye cane kuruta Nmap.



### V. Insozero



Muri iki gice ca mbere c’Icigwa ca 3, twashizeho ubuhinga bwo gupima ubugoyagoye biciye ku Nmap. Ubu turazi ingene twokoresha uburyo nyamukuru bwo gukora ico gikorwa, ariko kandi turazi n’aho uwo mwimenyerezo ugarukira. Mu gice gikurikira, tuzoba turiko turihweza neza iyo nzira, dukoresheje inyandiko za NSE kugira ngo twongere ububasha bwa Nmap incuro cumi.



## 8 - Gukoresha inyandiko za NSE za Nmap



### I. Ugushikiriza



Muri iki gice, turaza kuraba mu buryo bwimbitse inyandiko za NSE (_Nmap Scripting Engine_). Cane cane, turaza kuraba igituma ari kimwe mu bintu bikomeye bikomeye vy’iki gikoresho, ingene bikora n’ingene umuntu yocapura no gukoresha inyandiko nyinshi zihari.



Iki gice gikurikira inyigisho iheruka, aho twize ingene twokoresha ubuhinga bwo gupima ubugoyagoye bwa Nmap mu buryo bw’ishimikiro. Ubu tuzoca twihweza neza ingene [Nmap](https://www.it-connect.fr/cours/) ikora muri ivyo, kugira ngo dushobore kwongera gukora ibipimo vy’ukuri kandi bigenzurwa.



### II. Iciyumviro c'inyandiko za Nmap NSE



Ivyanditswe vya NSE vya Nmap bigufasha kwagura ubushobozi bwayo mu buryo bushobora guhinduka cane. Binditswe mu rurimi rwa LUA, ururimi rw’inyandiko rworoshe gukoresha no kuronka kuruta ururimi rwa C canke C# rukoreshwa na Nmap. Inyungu yo gukoresha inyandiko ya LUA na Nmap aho gukoresha igikoresho kihagaze ni uko bituma dushobora kwungukira ku muvuduko wa Nmap wo gukora n’ibintu bisanzwe (host, port na version discovery, n’ibindi).



Izo nyandiko zitunganijwe hakurikijwe ivyiciro, kandi inyandiko imwe ishobora kuba iri mu vyiciro birenze kimwe:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Mu buryo bw’ubuhinga, ivyiciro inyandiko irimwo vyerekanywe ata guca ku ruhande muri kode yayo.



![nmap-image](assets/fr/41.webp)



Ivyiciro vy'inyandiko za nSE `ftp-anon`._



Aka karorero kerekana igice c'itegeko ry'inyandiko ya NSE `ftp-anon.nse`, iyo ishirwa mu ngiro ryayo twabonye mu gice ca mbere.



### III. Urutonde rw'inyandiko za NSE zihari



Ku mburabuzi, inyandiko za NSE za Nmap ziri mu bubiko bwa `/usr/share/nmap/scripts/`, ata n'imiterere y'igiti canke uburongozi bwihariye. Aha niho hari incamake y'ibirimwo muri ubu bubiko:



![nmap-image](assets/fr/42.webp)



gukuraho ibirimwo `/usr/share/nmap/inyandiko/` ububiko burimwo inyandiko za NSE._



Ubu bubiko burimwo inyandiko zirenga 5.000 za NSE. Akenshi, igice ca mbere c'izina ry'inyandiko kirimwo porotokole canke urutonde rurimwo. Ivyo bituma dushobora gutoranya urutonde, nk'akarorero, nimba twipfuza gutoranya inyandiko zose zigenewe serivisi ya FTP:



![nmap-image](assets/fr/43.webp)



urutonde rw'inyandiko za NSE Nmap zifise amazina atangura na `ftp-`._



Nmap ntabwo itanga vy’ukuri uburyo bwo gucapura no gutanga urutonde rw’inyandiko zayo za NSE; ushobora gukoresha itegeko `--script-help` ukurikiwe n'izina ry'urutonde canke ijambo:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Ariko rero, igisohoka kizoba izina ry'inyandiko yose n'insobanuro yayo, ivyo bikaba bitari vyiza iyo ubushakashatsi buzanye inyandiko amajana n'amajana:



![nmap-image](assets/fr/44.webp)



igisubizo co gukoresha itegeko rya Nmap `--inyandiko-imfashanyo`



Mu vyiyumviro vyanje, uburyo bwiza cane ni ugukoresha amabwirizwa ya Linux ya kera mu bubiko bwa `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Ushobora gusoma kode y’ibice bikubwira, kugira ngo utahure neza ingene inyandiko ya NSE ikora.



### IV. Gukoresha inyandiko za NSE za Nmap



Ubu tugiye kwiga ingene twokora vulnerability scans mu guhitamwo neza inyandiko za NSE dukunda.



#### A. Hitamwo inyandiko hakurikijwe urutonde



Kugira ngo dutangure, turashobora guhitamwo gukora inyandiko zose ziri mu rwego runaka. Turakeneye kwerekana uru rwego canke ibi vyiciro kuri Nmap n'impamvu `--inyandiko <urutonde>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Iri tegeko rya mbere ringana n'itegeko rya `nmap -sC`. Ku mburabuzi, Nmap izohitamwo inyandiko mu rwego rwa `mburabuzi`, ariko ivyo ni kubera gusa impaka. Itegeko rikurikira, nk'akarorero, rizokoresha inyandiko zose ziri mu rwego rwa `kuvumbura`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Nk’uko twabibonye, ​​hariho ivyiciro bituma dushobora kumenya ningoga ivyo inyandiko za NSE zijanye n’ivyo zikora (`discovery`, `vuln`, exploit`), mu gihe izindi zisobanura urugero rw’akaga, ukumenya canke ugushikama kw’ikigeragezo cakozwe. Niba turi mu gihe gikomeye kandi tutagira ugutahura neza ibikorwa bitandukanye bikorwa n'uguhitamwo kwacu kw'inyandiko, turashobora guhitamwo gufatanya ivyo twahisemwo kugira ngo duhitemwo gusa izo nyandiko ziri mu rwego rwa `kuvumbura` n'urw'umutekano`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Niba ushaka gukuraho inyandiko mu mice ya `dos` na `intrusive`, ushobora gukoresha iyi nkuru ikurikira:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Urashobora kubona ko gusobanura ivyangombwa vyo gukuraho nk’uko vyavuzwe haruguru bizotuma hakoreshwa ibindi vyiciro vyose bitakuwemwo mu buryo butomoye. Kugira ngo tube abagororotsi, twoshobora gusobanura, nk’akarorero:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Aha hari ingero zimwe zimwe z’ingene wofata inyandiko za NSE hakurikijwe urutonde, cane cane iyo ukoresheje Nmap mu gusesangura ubugoyagoye mu bihe vy’ubuzima nyakuri.



#### B. Hitamwo inyandiko nk'igice



Turashobora kandi guhitamwo gukora ikigeragezo kimwe kidasanzwe mu gihe c’isesengura, ikigeragezo gihuye n’inyandiko ya NSE. Kugira ngo ivyo tubikore, dukeneye kugaragaza izina ry'inyandiko mu `-inyandiko <izina>`. Gufata akarorero k'inyandiko ftp-anon.nse:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Turaheza tukagira igisubizo nyaco cane:



![nmap-image](assets/fr/45.webp)



igisubizo co gukoresha inyandiko ya NSE `ftp-anon` ku cambu ca FTP biciye kuri Nmap._



Turabona igisubizo co gukoresha inyandiko `ftp-anon` ku cambu 21, kandi nta kindi kivuko, kuko twasobanuye uburyo bwa `-p 21`. Twari gushobora kandi gukora igikorwa co gupima port y'ishimikiro, dukora inyandiko ya `ftp-anon` NSE gusa ku bikorwa vya FTP vyavumbuwe:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Gutyo, Nmap na yo nyene yari gukora iki kigeragezo c’uguhuza ata mazina iyo ironka igikorwa ca FTP ku kindi kivuko.



Kugira ngo ubone insobanuro ngufi y'ico inyandiko ya NSE ikora, ushobora gukoresha uburyo `--script-help` bwavuzwe haruguru:



![nmap-image](assets/fr/46.webp)



gufasha kugaragaza igisubizo c'inyandiko ya NSE `sshv1`._



Muri make, na none turashobora gusubira gukoresha uburyo bwose bwo kuvumbura urubuga, ibikorwa, ama verisiyo n’ubuhinga twakoresheje gushika ubu!



#### C. Gucungera imvo z'inyandiko



Mu gihe co gukoresha Nmap, uzohura n’inyandiko zimwe zimwe za NSE zisaba ivyiyumviro vy’injiza kugira ngo zikore neza. Ubu turaza kuraba ingene twotanga imvo kuri izo nyandiko biciye ku mahitamwo ya Nmap.



Nk'akarorero, reka dufate inyandiko `ssh-brute`, ishobora kugufasha gukora igitero c'inguvu z'ubunyamaswa kuri serivisi ya SSH.



Igitero c’inguvu z’agahomerabunwa ca kera gishingiye ku kugerageza amajambo y’ibanga menshi (rimwe na rimwe amamiliyoni) kugira ngo umuntu agerageze kwemeza ko ari we afise konti yihariye. Mu kugerageza amajambo y’ibanga menshi cane, uwo muterabwoba arabesha ku bijanye n’uko uwo muntu yakoresheje ijambobanga ry’intege nke mu nkoranyamagambo y’amajambo y’ibanga yakoreshejwe mu gutera.



Iyi nyandiko ifise amahitamwo "ya mbere", twoshobora guhindura kugira ngo ihure n'ivyo dufise. Mu bijanye n’iki gitero, nk’akarorero, turashobora guha Nmap urutonde rw’abakoresha n’inkoranyamagambo y’ijambobanga izokoreshwa. Nk’uko ndabizi, ntibishoboka gutanga urutonde rw’ibintu bisabwa kugira ngo umuntu akore inyandiko, rero uburyo bwo kwizigirwa cane ni ugusura urubuga rwemewe rwa Nmap. Ihuza ry'inyandiko z'inyandiko ya NSE rishobora kuronswa mu kwishura ku mahitamwo ya `--script-help`:



![nmap-image](assets/fr/47.webp)



igisubizo co kwerekana imfashanyo y'inyandiko ya NSE `ssh-brute` n'ihuriro kuri nmap.org._



Mu gufyonda ku nzira yerekanwa, dushika kuri iyi paji y’urubuga [https://nmap.org/):



![nmap-image](assets/fr/48.webp)



urutonde rw'imvo zishobora gushikirizwa inyandiko ya NSE `ssh-brute` ya Nmap



Aha turabona neza imvo zishobora gukoreshwa, izo nyamukuru mu vyo dukora ni `passdb` (dosiye irimwo urutonde rw'amajambo y'ibanga) na `userdb` (dosiye irimwo urutonde rw'abakoresha). Ivyo bitabo aha vyerekeye amasomero yo mu mutima ya Nmap, kuko ubu buryo bw’inguvu z’ibikoko n’amahitamwo ajanye navyo bihurizwa hamwe kugira ngo bikoreshwe mu buryo bumwe mu nyandiko nyinshi (`ssh-brute`, `mysql-brute`, `mssql-brute`, n’ibindi) kandi rero bizogira imvo zimwe canke zike:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Nk'uko ushobora kubibona muri iri tegeko rya nyuma, turashobora gusobanura imvo zikenewe ku nyandiko ya Nmap dukoresheje `--scripts-args urufunguzo=agaciro,urufunguzo=agaciro`. Aha niho hari igisubizo gishoboka c'igisohoka ca Nmap igihe ukora inguvu z'ubukazi za SSH biciye ku nyandiko ya `ssh-brute` NSE:



![nmap-image](assets/fr/49.webp)



igisubizo c'ugushirwa mu ngiro kwa SSH biciye kuri Nmap._



Nk'uko ushobora kubibona, amakuru akomoka ku nyandiko za NSE abanza `NSE: [izina ry'inyandiko]` mu gisohoka gikorana (igisohoka c'iherezo), bikaba bituma vyoroha kuyaronka. Mu kwerekana ibisubizo vya Nmap bisanzwe, dufise gusa incamake yerekana nimba ibimenyetso bigoyagoya vyavumbuwe canke bitavumbuwe (harimwo n’amajambo y’ibanga, wibuke).



Kugira ngo ibintu bigende intambwe imbere, no kwibutsa ko ivyo vyose bishobora gukoreshwa mu kwongera ku mahitamwo yose twamaze kuraba, ng’iri itegeko rizovumbura `10.10.10.0/24` urubuga, scanner 2000 service services zikunda gukoreshwa cane ku ports za TCP brute na FTP campai:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Uyu ni akarorero kamwe gusa k’inyandiko nyinshi ziriho be n’uburyo zishobora gukoreshwa. Ariko ubu turafise iciyumviro ciza c’ingene twomenya neza inyandiko za NSE, nimba zisaba imvo n’imvano n’ingene twozirungika kuri Nmap.



### V. Insozero



Muri iki gice, twarize ingene twokoresha inyandiko za NSE za Nmap kugira ngo dukore ibikorwa bitandukanye. Ndagutumiye gufata umwanya wo kuvumbura ivyiciro bitandukanye vy’inyandiko n’inyandiko ubwazo, kugira ngo ubone gusa ingene ibigeragezo bishobora gukora.



Mu bice vyinshi ubu, twama twirundanira uburyo bwo kuvumbura, gupima no kubara buteye imbere cane canke buke. Ubu, ukwiye kuba uzi ko igisohoka ca Nmap n'ibisubizo vyerekana bitangura kuba vyinshi cane, rimwe na rimwe mbere bikaba vyinshi cane ku bijanye n'iherezo ryacu. Mu gice gikurikira, tuzokwiga ingene twomenya neza iyo nkuru, cane cane mu kuyibika mu madosiye mu buryo butandukanye.






## 9 - Gucungera amakuru y'isohoka rya Nmap




### I. Ugushikiriza



Muri iki gice, turaza kuraba igisohoka ca Nmap, na cane cane uburyo butandukanye bwo guhindura igisohoka. Turabona ko Nmap ishobora gutanga uburyo bwinshi bwo gusohora kugira ngo bujane n’ivyo umuntu akeneye bitandukanye, kandi ko ivyo navyo ari bimwe mu bintu bikomeye bikomeye vy’iki gikoresho.



Ku mburabuzi, Nmap itanga ivyerekanwa vy’ido n’ido vy’ivyavuye mu bipimo n’ibipimo ikora. Ivyo birimwo abashitsi n’ibikorwa vyasuzumwe, ivyo vyabonetse ko bishobora gushikwako, ivyerekeye ivyambu vyuguruye, uko bimeze n’ingene bimeze. Ikindi, amakuru y’inyandiko za NSE na yo araboneka mu gisohoka c’iherezo. Ariko rero, ico gisohoka gishobora guca gihinduka kinini ningoga, mbere n’aho amakuru yoba afise uburyo butomoye, ivyo bikaba bishobora gutuma bigorana kuronka amakuru nyayo mu bisubizo.



### II. Kumenya neza imiterere y'isohoka rya Nmap



#### A. Bika ibisubizo vya scanner muri dosiye y'inyandiko



Kugira ngo ibintu vyorohe, [Nmap](https://www.it-connect.fr/cours/nmap-ikarita-y’ugupima-ibishobora guhungabana/) ituma vyoroha cane kubika umusaruro wayo muri dosiye y’inyandiko. Ivyo bishobora kuba ngirakamaro mu gushiramwo ububiko, kugereranya n’ibindi bigeragezo, ariko kandi no gusesangura iki gisohoka hakoreshejwe ibikoresho vyihariye vyo gutunganya amajambo canke indimi zo kwandika, nk’umwandiko wa Sublime, [PowerShell] kubika igisohoka ca Nmap muri dosiye y'inyandiko, dushobora gukoresha `-oN <izina rya dosiye>` ("N" muri "ibisanzwe"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Nta gitangaje rero, kuko Nmap izokwerekana igisohoka cayo gisanzwe mu terminal yacu, ariko kandi muri dosiye yatanzwe.



#### B. generate Nmap isohoka mu buryo bupfutse



Hariho kandi uburyo bwa kabiri bwo gusohora mu buryo bw'"inyandiko" bushobora gusobanurwamwo n'umuntu: uburyo bwa "greppable".



Iyi nzira yaremewe gutanga "ibonezo" y'igisohoka ca Nmap, itunganijwe mu buryo bwo kworohereza ugutunganya kwayo n'ibikoresho nka `grep`. Reka turabe akarorero k'ubwo bwoko bw'isohoka:



![nmap-image](assets/fr/50.webp)



nmap urubuga rwa scan n'isohoka mu buryo "bushobora gufatwa"._



Aha, nakoze ivy'ukuvumbura urubuga hamwe n'ugupima urubuga n'ugusesangura ubuhinga n'amaverisiyo ku rubuga /24, hanyuma nkabika igisohoka muri dosiye mu buryo bwa "greppable". Nheza n'idosiye irimwo imirongo 2 ku mushitsi akora:





- Umurongo wa mbere umbwira ko umushitsi nk’uwo ari _Up_;





- Umurongo wa kabiri umbwira ivyuho vyasuzumwe, uko bimeze n'ubuhinga n'amakuru y'ubuhinga bwa none vyaronswe mu buryo bwihariye cane: `<ivyuho>/<imiterere/<amasezerano>//<service>//<verisiyo>/,`




Ukwo guhindura amajambo n'umurongo udahinduka bituma umuntu ashobora gukora vyihuse n'ibikoresho vyo gukora amajambo nka `grep`, canke indimi zo kwandika no gukora porogarama. Itegeko rikurikira, nk'akarorero, riramfasha kuronka amakuru yerekeye umushitsi `10.10.10.5` mu gihe c'ugupima cane gukorwa na Nmap igisohoka caco coba kigoye gusesangura:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Ku rundi ruhande, ndashobora kandi gutanga urutonde rw’abashitsi bose bafise port 21 yuguruye, kuko ports na IP biri ku murongo umwe:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Kugira ngo generate iyo nkuru, dukeneye gukoresha `-oG <izina rya dosiye>.gnmap` ("G" muri "grep"). Kubera akamenyero, nkoresha `.gnmap` extension hano kuri dosiye nk'iyo, ariko ntutinye gukoresha iyo ukunda yose:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Iyi nzira ishobora gukoreshwa mu bintu bitandukanye kandi ni ngirakamaro cane cane mu kwandika/gutoranya vyihuta. Naho biri ukwo, biriko biraheba kugira ngo bifashe uburyo tuzobona mu nyuma.



iciyumviro: uburyo bwa `-oG` bwaciwe kuva kuri Nmap 7.90. Irashobora gukoreshwa kugira ngo ihuze. Ishobora gukoreshwa ku ntumbero z'uguhuza, ariko ni vyiza ko ukoresha XML canke uburyo busanzwe ku bijanye n'iterambere ryose canke gusesangura kwikora._



#### C. Ubuhinga bwa XML ku gisohoka ca Nmap



Igishushanyo ca nyuma gikwiriye kuvugwa muri iyi nyigisho ni XML. Ubu butandukanye n’ibindi bibiri vyabanje, ubu ntibwagenewe gusomwa n’abantu, ahubwo bwagenewe gusomwa n’ibindi bikoresho canke inyandiko.



XML (_Ururimi rw'Ikimenyetso_) ni ururimi rwo gushiramwo amakuru rukoreshwa mu kubika no gutwara amakuru, rutanga imiterere y'uburongozi biciye ku bimenyetso vy'abantu.



Muri Nmap, uburyo bwa XML burakoreshwa mu generate raporo zitomoye ku bipimo vyakozwe, harimwo amakuru ku bashitsi, ivyuho n’ibigoyagoya vyabonetse, hamwe n’amakuru y’inyongera atagaragara mu gisohoka ca Nmap gisanzwe.



Kugira ngo generate dosiye y'isohoka mu buryo bwa XML, dukeneye gukoresha uburyo bwa `-oX` ("O" kuva kuri "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Igisubizo ni igisohoka ca Nmap mu terminal yawe, hamwe na dosiye mu buryo bwa XML mu bubiko bwawe.



Ego ni ko, uburyo bwa XML ntibwagenewe gusomwa no gusobanurwa n’abantu. Naho biri ukwo, nimba ushaka gukora inyandiko canke isesengura ry’ivyuma kuri iyi nzira y’isohoka rya Nmap, uracari ukeneye kugira iciyumviro c’ibimenyetso n’imiterere ikoreshwa. Nk'akarorero, ng'iki igice c'ibirimwo muri dosiye ya XML yaremwe na Nmap, yerekana ibisubizo vy'ugupima umushitsi 1:



![nmap-image](assets/fr/51.webp)



akarorero k'inyandiko ya XML y'umushitsi 1 mu gihe c'isuzuma rya Nmap



Hariho amakuru menshi hano, kandi turakunda cane cane ivyicaro bibiri vyuguruye:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Turatahura ko iyo nzira izotuma vyoroha gusesangura ibisubizo, kuko amakuru yose atunganijwe neza mu buryo bwihariye, bufise izina canke akaranga. Cane cane, turasanga amakuru tutari bwigere tubona: ni CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Twaravuze muri make CPE mu gice ca 2 c’igice ca 2, kandi ayo makuru agenwa mu mikino mu gihe co kumenya verisiyo. Nmap ikoresha ubuhinga bwayo, ubuhinga n’uburyo bwo kumenya verisiyo kugira ironke CPE ijana.



Ivyo bituma dushobora gusubira gukoresha ayo makuru n’ibiharuro be n’ibikoresho biyakoresha. Ndiko ndiyumvira cane cane urutonde rw’amakuru rwa NVD, ruvuga ku ma CVE. Ku CVE yose, irimwo ama CPE yashikiwe n’ubugoyagoye. Aha ni akarorero ka CVE yerekeye `a:microsoft:amakuru_ya_internet:7.5` kuva ku rutonde rw'amakuru rwa NVD:



![nmap-image](assets/fr/52.webp)



kubaho kwa CPE mu ndondoro ya CVE mu rutonde rw'amakuru rwa NVD



Ubu turatahura neza ivyiza vy’iyi nzira, itanga urutonde rw’amakuru rutomoye cane kandi irimwo amakuru yose yegeranywa canke atunganijwe na Nmap.



Nk’uko bigaragara, ndabika mu buryo butunganye amasanamu yanje ya Nmap mu buryo bwose butatu icarimwe. Ivyo bishobozwa n'ihitamwo rya `-oA <izina>` ("A" kuri "Vyose"), rizokora dosiye `<izina>.nmap`, dosiye `<izina>.xml` na dosiye `<izina>.gnmap`. Uko niko ndazi neza ko ataco nzobura igihe nzoba nkeneye gusubira ku vyo nabonye.



Ukoresheje izo nzira zitatu, ushobora kugira ivyo ukeneye vyose kugira ngo ubike maze amaherezo ukoreshe ibisubizo vya Nmap mu buryo bwikora. Tuzosubira gukoresha uburyo bwa XML mu gice gikurikira, nitwabona gukoresha Nmap n’ibindi bikoresho vy’umutekano.



#### III. Gutanga raporo ya HTML ivuye mu gupima Nmap



Uburyo bwa XML buratanga ubushobozi bwinshi, n’ubwo gukora nk’ishimikiro ryo gutanga raporo mu buryo bwa HTML, bizotuma umuntu abona neza cane.



Kugira ngo duhindure dosiye ya Nmap mu buryo bwa XML mu rupapuro rw'urubuga, tuzokoresha igikoresho ca `xsltproc`, ico tuzokenera gushiramwo mbere:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Igihe iki gikoresho kimaze gushirwamwo, gusa ugihe dosiye ya XML izohindurwa n'izina rya raporo ya HTML izosohoka:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Ivyo bizotuma igicapo cacu cose gitunganijwe neza, mbere n’amabara makeyi be n’amahuza ashobora gufyondwa mu rutonde rw’ibirimwo!



![nmap-image](assets/fr/53.webp)



gukura muri raporo y'ibara rya Nmap mu buryo bwa HTML yakozwe na xsltproc._



Mu kuvuga muri rusangi, dosiye ya XML yabitswe na Nmap irimwo ivyerekanwa ku yindi dosiye iri mu buryo bwa XSL:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Guhindura muri HTML rero ni igikorwa gitangwa kandi kiroroshwa na Nmap, `xsltproc` ari igikoresho gisanzwe kandi cemewe co gukora ico gikorwa (kitava mu gikoresho ca Nmap).



XSLT (_Impinduka z'ururimi rw'imirongo y'imirongo_) ni igice ca XSL gishobora gutuma amakuru ya XML yerekanwa kuri paji y'urubuga maze "agahindurwa", bihuye n'imirongo ya XSL, mu makuru asomwa, afise imiterere mu buryo bwa HTML.



inkomoko: [ubufasha.adobe.com/](ubufasha.adobe.com/fr/umuhinguzi w'indoto/ukoresha/xml-xslt.html)_



Urugero rw'amakuru muri raporo rungana n'urwo mu buryo bwa XML bwa Nmap kandi ruri hejuru y'urw'isohoka ry'iherezo ry'iherezo (_interactive output_).



### IV. Gucungera urugero rw'amajambo ya Nmap



Ubu turaza kuraba uburyo bukeyi bwo gukoresha Debugger Nmap canke bwo gukurikirana ingene itera imbere.



Ihitamwo rya mbere dukwiye kuvuga ni ihitamwo rya `-v`, ryongera amajambo ya Nmap. Akira akarorero:



![nmap-image](assets/fr/54.webp)



Igisohoka ca nmap gikoresheje amahitamwo ya `-v`._



Ku scanner yibanda ku bashitsi benshi n’ivyambu, igisohoka ca terminal kizoba kigoye gukoreshwa kubera ubwinshi bw’amakuru yerekanwa. Kubera iyo mpamvu, iyi nzira ikwiye gukoreshwa hamwe n'ihitamwo ryabonetse mbere, rituma ushobora kubika igisohoka ca Nmap muri dosiye. Amakuru yerekeye ikoreshwa ry'amajambo menshi ntazoshirwa muri iyi dosiye y'isohoka. Nk’uko ushobora kubibona mu karorero kari hejuru, iyo verbosité iratuma ukurikirana ibikorwa vya Nmap n’ivyo ivumbura mu buryo butomoye kandi butaziguye. Ku bipimo vy’igihe kirekire aho amakuru yerekanwa ashobora guteba kuza, ivyo bituma umuntu adashobora kutabona neza igikorwa ca Nmap kiriko kirakorwa ubu no kumenya ko ibintu biriko biratera imbere kandi biriko biratera imbere ku rugero rungana iki. Kugira ngo wongere ubwinshi bw'amajambo, ushobora gukoresha uburyo bwa `-vv`.



Kugira ngo ukomeze gukurikirana igikorwa ca Nmap mu gihe co gupima, ushobora gukoresha uburyo bwa `--packet-trace`. Na `-v` option, turonka urutonde rw'ivyambu vyose vyuguruye vyavumbuwe na Nmap, mu gihe n'iyi nzira, turonka umurongo w'inyandiko ku mpapuro zose zoherejwe ku port. Ivyo bitanga umusaruro w'amajambo menshi cane, ariko bishobora gukurikirana mu buryo burambuye igikorwa ca Nmap, ng'akarorero:



![nmap-image](assets/fr/55.webp)



gukurikirana mu buryo burambuye ibikorwa vya Nmap biciye ku `--packet-trace`._



Na none, aya makuru ntazokwandikwa muri dosiye y'isohoka yasohowe na Nmap iyo hakoreshejwe amahitamwo `-oN`, `-oG`, `-oX` canke `-oA`.



Ubwa nyuma, Nmap nayo itanga uburyo bubiri bwo gukosora: `-d` na `-dd`. Aya mahitamwo yitwararika nk'amahitamwo y'amajambo `-v`, ariko yongerako ayandi makuru y'ubuhinga, nk'incamake y'ibipimo vy'ubuhinga mu ntango y'ugupima:



![nmap-image](assets/fr/56.webp)



Amahitamwo y'igihe yerekanwa mu kugaragaza gukosora kwa Nmap



Mu bice bikurikira, turaza kuraba amahitamwo ya "Igihe" arivyo n'igituma bibereye kuyamenya.



Ubwa nyuma, nimba ushaka gusa kugira icegeranyo c'ishimikiro, c'ivy'ubuhinga bwa Nmap, ushobora gukoresha uburyo bwa `--stats-every 5s`. "5s" aha bisigura amasegonda 5 kandi ushobora guhindurwa kugira ngo bihure n'ivyo ukeneye. Iyi ni incuro tuzoronka inyishu zivuye kuri Nmap ku bijanye n’ingene itera imbere:



![nmap-image](assets/fr/57.webp)



amakuru yerekanwa n'ihitamwo rya Nmap `--imibare-buri`



Cane cane, turashobora kuronka ijana kw'ijana ry'iterambere, hamwe n'ikimenyetso c'inzira irimwo: inzira yo kuvumbura abashitsi biciye ku [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), inzira yo kuvumbura ivyuho vya TCP vyerekanwa, n'ibindi.



Ariko rero, Nmap ntabwo ari nziza cane mu kugereranya igihe igikorwa kizomara, n’aho nyene kubera ko itamenya imbere y’igihe ingene izobwirizwa gucapura abashitsi n’ibikorwa vyinshi.



### V. Insozero



Muri iki gice, twaravye uburyo bwinshi bwo kubika ibisubizo vya Nmap scan mu buryo butandukanye bwa dosiye. Ivyo bizodufasha cane, nk’uko mu bihe vy’ukuri, ibivuye mu gucapura bishobora gutwara imirongo amajana canke mbere ibihumbi! Twarabonye kandi ingene twokwongera urugero rw’amajambo ya Nmap kugira ngo tubone gukosora canke kugira ngo turonke raporo y’iterambere ry’ugupima.



Uburyo bwa XML buzoba ngirakamaro cane mu gice gikurikira, aho tuzorabira ibikoresho bike bishobora gukorana n'ibisubizo vya Nmap.




## 10 - Gukoresha Nmap n'ibindi bikoresho vy'umutekano



### I. Ugushikiriza



Muri iki gice, turaza kuraba bimwe mu bikoresho vya kera vya Nmap n’ibindi bikoresho vy’umutekano vy’ubuntu n’ivy’inkomoko yuguruye. Cane cane, tuzokoresha ivyo twize mu bice vyabanje kugira ngo turushirizeho kwongereza ububasha n’ubushobozi bwa Nmap.



Ubushobozi bwo kubika ibisubizo vya Nmap scan muri XML bituma amakuru ahura n'ibindi bikoresho vyinshi. Kubera ko hafi indimi zose zo gukora porogarama n’izo kwandika muri iki gihe zifise amasomero ashobora gusesangura XML, ivyo bituma vyoroha cane gukora ayo makuru. Ibikoresho bitari bike, cane cane ivyo vyerekeye umutekano w’ibitero, birafise ibikorwa vyo gukora uburyo bwa XML bwakozwe na Nmap. Reka tuvyihweze neza.



Ngiye kuvuga ibikoresho bikeyi bitera ubwoba ntadondora vy’ukuri ingene bikoreshwa canke ingene bikora. Nzokwibaza ko umusomyi amenyereye ikoreshwa ryavyo ry’ishimikiro kandi ko risanzwe rikora. Iki gice kizoba gishimishije cane abahinga mu vy’umutekano wo kuri interineti (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), abantu bari mu mahugurwa canke abafashe ingingo yo kwihweza cane iyo nkuru.



### II. Kuzana ibisubizo vya Nmap muri Metasploit



Igikoresho ca mbere tugiye kuraba co gusubira gukoresha amakuru ya Nmap mu bushakashatsi bw’umutekano n’ubugoyagoye ni Metasploit.



Metasploit ni uburyo bwo gukoresha no gutera. Ni umuti w’ubuntu kandi ni igikoresho cemewe kirimwo umubare munini w’ibice vyanditswe muri Ruby canke Python. Ivyo bituma ubugoyagoye bushobora gukoreshwa, ibitero bishobora gukorwa, inzugi z’inyuma zishobora guterwa, guhamagara bishobora gucungirwa (C&C canke Communication and Control functions) n’ibindi vyose bishobora gukoreshwa mu buryo bumwe.



Cane cane, iyo nzira izwi cane kandi ikoreshwa cane ishobora gukorana na postgreSQL [urutonde rw’amakuru](https://www.it-connect.fr/cours-tutoriels/uburongozi-uburongozi/ububiko/bdd/) aho abashitsi, ivyambu, ibikorwa, amakuru y’ukwemeza n’ibindi bibikwa.





- Ivyanditswe vyemewe vya Metasploit: [inyandiko.metasploit.com/](inyandiko.metasploit.com/)




Aha niho Nmap n’isohoka ryayo bishika, kuko uburyo bwa XML bw’isohoka rya Nmap bushobora kwinjizwa mu buryo bworoshe mu rutonde rwa Metasploit kugira ngo buzuze urutonde rwayo rw’abashitsi n’ibikorwa, bishobora rero gutorwa ningoga nk’intumbero z’iki canke ico gitero.



Igihe nari mu gipfukisho canje ca Metasploit, ntangura gukora ahantu ho gukorera, ubwoko bw’ahantu bwihariye ku bidukikije vyanje vy’uwo musi:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Igihe ikibanza canje co gukoreramwo kimaze kuremwa, turakeneye kwemeza ko guhanahana amakuru n'urutonde rw'amakuru bikora:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Ubwanyuma, dushobora gukoresha itegeko rya Metasploit `db_import` kugira ngo twinjize igishushanyo cacu ca Nmap mu buryo bwa XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Ehe igisubizo co gushitsa aya mabwirizwa yose:



![nmap-image](assets/fr/58.webp)



kwinjiza Nmap mu buryo bwa XML mu bubiko bw'amakuru bwa Metasploit



Aha urashobora kubona ko host yose izana, hamwe n’ibikorwa vyayo. Aya makuru ashobora rero kugaragazwa biciye ku itegeko `ibikorwa` canke `ibikorwa -p <port>` ku bikorwa vyihariye:



![nmap-image](assets/fr/59.webp)



Urutonde rw'ibikorwa vyazanywe bivuye muri dosiye ya XML mu bubiko bw'amakuru bwa Metasploit



Ubwa nyuma, turashobora gusubira gukoresha ayo makuru mu buryo bwihuse kandi bworoshe mu kiganiro biciye ku mahitamwo ya `-R`, azohindura urutonde rw'ibikorwa vyaronswe nk'inyungu y'amabwirizwa ya `RHOSTS`, akoreshwa mu kugaragaza intumbero z'igitero kizokorwa. Aha ni akarorero n'umurongo wa `ssh_login`, ushoboza gukora igitero c'inguvu z'agahomerabunwa ku bikorwa vya [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



koresha `ibikorwa -R` uburyo bwo kwinjiza ibikorwa vyerekanwa nk'intumbero y'igitero



Iyi ni akarorero gatoyi gusa k’ivyo bishobora gukorwa n’amakuru ya Nmap muri Metasploit, ariko iraguha iciyumviro gitoyi c’ingene ayo makuru ashobora gusubira gukoreshwa mu buryo bwihuse kandi bworoshe nk’igice c’ikigeragezo co kwinjira, gupima ubugoyagoye canke igitero co kuri internet. Ni vyiza kandi kuvuga ko Nmap ishobora gukoreshwa ataco ihinduye kuva kuri Metasploit kugira ngo yinjize ibisubizo mu rutonde rw'amakuru (itegeko `db_nmap`), ikindi ciyumviro gishimishije co gushikiriza!



### III. Gukoresha Nmap n'igikoresho co gupima urubuga rwa Aquatone



Igikoresho ca kabiri nshaka gutanga muri iki gice ku bijanye no gusubira gukoresha ibisubizo vya Nmap ku bijanye n’umutekano w’ibitero n’isesengura ry’ubugoyagoye ni Aquatone.



Aquatone ni igikoresho co gupima urubuga gikoreshwa mu gupima neza ibikorwa vy’urubuga ku rubuga. Itanga ibikorwa vy’ubuhinga buhanitse vyo kuvumbura ibikorwa vy’urubuga, kumenya ivy’intara, gusuzuma ivyuho no gufata urutoke rw’ibikorwa vy’urubuga. Vyose vyerekanwa mu buryo butomoye kandi butomoye muri HTML, JSON na raporo z’inyandiko kugira ngo bishobore gusesangura umutekano w’urubuga.



Nk’uko biri kuri Metasploit, Aquatone irashobora gukora ataco ihinduye ku buryo bwa XML bwa Nmap maze ikabukoresha nk’intumbero yo gupima. Cane cane, ishobora gukura gusa abashitsi n’ibikorwa vy’inyungu (ibikorwa vy’urubuga) mu makuru yose raporo ya Nmap ishobora kubamwo.





- Ihuza ry'ibikoresho: [Github - Igikoresho c'amazi]( https://github.com/igikoresho c'amazi)




Kugira ngo ukoreshe igisohoka ca XML ca Nmap na Aquatone, wohereze gusa dosiye ya XML mu muyoboro uzokoreshwa na Aquatone. Akira akarorero:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Aho Aquatone mu bisanzwe ikora port discovery ku bashitsi kugira ironke ibikorwa vy’urubuga, muri iki gihe izokwizigira gusa ibivuye muri Nmap, yamaze gukora iyo nzira, gutyo izigame umwanya:



![nmap-image](assets/fr/61.webp)



gukoresha ibisubizo vya Nmap mu buryo bwa XML na `aquatone`._



Kugira ngo mumenye, ng’iki igice ca raporo yasohowe na Aquatone:



![nmap-image](assets/fr/62.webp)



akarorero ka raporo y'amazi



Ku bwanje, kenshi nkoresha Aquatone kugira ngo nshobore kubona ningoga ubwoko bw’imbuga ziri ku rubuga, cane cane kubera ubuhinga bwayo bwo gufata amafoto.



Aha na ho, kugira raporo yuzuye ya Nmap mu buryo bwa XML birazigama umwanya kandi bikaba vyoroha gusubira gukoresha mu kindi gikoresho.



### IV. Iciyumviro



Izo ngero zibiri zirerekana neza ko uburyo bwa XML bwa Nmap butuma ibindi bikoresho bishobora gukoresha neza ibivuye muri yo, kuko ari uburyo bw’amakuru butunganijwe kandi bworoshe gukoresha. Hariho n’ibindi bikoresho vyinshi bishobora gukora ivyo bisubizo, nk’ibikoresho vy’ugutanga raporo vyikora, ibishushanyo vyerekana canke ibikoresho bikomeye cane, vy’ubuhinga bwo gupima ubugoyagoye.



Birumvikana, urashobora kandi gutegura inyandiko zawe n’ibikoresho vyawe muri Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/uburongozi-bw’inyandiko/inyandiko/powershell/) canke urundi rurimi urwo ari rwo rwose rufise ububiko bw’ibitabu vy’ugusesangura XML kugira ngo ukoreshe kandi wongere ukoreshe amakuru y’ibisubizo vya fi Nmap uko ubona.



Iki gice kiratujana ku mpera y’inyigisho ku gukoresha neza Nmap, cane cane ku bijanye no gupima ubugoyagoye biciye mu nyandiko za NSE.



Igice gikurikira c’inyigisho kizoba kijanye n’ibindi, mu bindi, ku bikorwa vyiza vy’inyongera, vy’ubuhinga n’impanuro ku bijanye n’ibipimo vyihariye Nmap ishobora gukora. Turaza kandi kuraba uburyo bwo gutuma ubuhinga bwo gupima bugenda neza, bukaba ari ngirakamaro canecane igihe umuntu ariko arapima imihora minini.




## 11 - Kunoza ubushobozi bwo gupima urubuga



### I. Ugushikiriza



Muri iki gice, tuzokwiga ingene twotuma umuvuduko w’ibipimo vy’urubuga bikoreshwa na Nmap bigenda neza hakoreshejwe uburyo butandukanye bwihariye. Cane cane, tuzomenya vyinshi ku mikorere y'imbere ya Nmap, kuva ku burongozi bwa _timeout_ gushika ku miterere y'igikoresho yabitswe imbere.



None ko twabonye neza ibiranga Nmap, reka tuje ku bijanye n’ico gikoko n’ububasha bwaco. Nimba warakoresheje ico gikoresho ku mbuga nini, kumbure warabonye ko ama scanner amwamwe ashobora gutwara igihe kirekire, naho ico gikoresho gifise ububasha. Kandi n’impamvu nziza: itegeko ryoroshe rya `nmap` rifise amahitamwo makeyi rishobora generate amamiliyoni y’amapakete yibanda ku bihumbi amajana vy’imirongo n’ibikorwa bishobora gukoreshwa.



Ikindi, ibikoresho bimwe bimwe vy’urubuga bishobora gutegeka n’ibigirankana igipimo gitoyi (umubare w’amapakete ku segonda), mu kaga ko kwanka amapakete yawe canke gukumira IP yawe Address kubera imvo z’umutekano.



Bivanye n’aho ibintu biri, vyoshobora kuba vyiza tugerageje no gutuma ivyo vyose bigenda neza, nk’uko tuzobibona muri iki kigabane.



Uko biri kwose, ushobora kugenzura agaciro ka mbere k'ibipimo tugiye kuraba, hamwe n'uko amahitamwo ugiye gukoresha yashizwe mu ngiro neza, biciye ku gukosora kwa Nmap (amahitamwo `-d` yabonetse mu kigabane c'imbere):



![nmap-image](assets/fr/63.webp)



reba amahitamwo y'igihe biciye ku mahitamwo ya Nmap `-d`._



### II. Gucungera umuvuduko w'ibipimo vya Nmap



#### A. Gucungera uguhuza



Ku mburabuzi, Nmap ikoresha uguhuza mu bipimo vyayo kugira ngo bibe vyiza, kandi amaparametere yose ikoresha arashobora guhindurwa biciye ku mahitamwo atandukanye. Ariko rero, ibintu bikenewe guhindura ivyo bipimo ni bike cane, rero ntituzovyinjiramwo mu buryo burambuye muri iyi nyigisho:





- `--min-umugwi w'abashitsi/max-umugwi w'abashitsi <ubunini>`: ubunini bw'imigwi y'abashitsi ihuye.





- `--min-uguhuza/max-uguhuza <numprobes>`: uguhuza kw'Ibipimo.





- `--ugucererwa-gupima/--ugucererwa-gupima-kurengeye <igihe>`: itunganya ugucerezwa hagati y'Ibipimo.




Menya gusa ko zihari kandi zishobora gukoreshwa.



#### B. Gucungera umubare w'amapakete ku segonda



Ku mbuga, Nmap ubwayo itunganya umubare w’amapakete ku segonda yohereza hakurikijwe inyishu y’urubuga. Ariko birashoboka guhatira iyo nzira mu gusobanura agaciro kanini na/canke gatoyi ko gukurikira mu bijanye n'umubare w'amapakete ku segonda. Iyi nzira ikoreshwa hakoreshejwe amahitamwo `--min-rate <umubare>` na `--max-rate <umubare>` aho `umubare` ugereranya umubare w'amapakete ku segonda. Akarorero:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Ivyo bituma ushobora guhindura umuvuduko w’ivyo ukoresha bivanye n’ivyo ukeneye, kugira ngo wihutishe igikorwa canke ugabanye uburebure bw’ivyo ukoresha. Ico gihe ca nyuma (guhagarika umuvuduko w’ibipimo) ni co kizogushikana kuri ayo mahitamwo, cane cane iyo ushikiwe n’uguhagarara kw’urubuga igihe ukoresha Nmap (ivyo bikaba ari bike cane).



### III. Gucungera ukunanirwa kw'ihuriro n'igihe co guhera



Iyindi parametere dushobora gukina nayo kugira ngo dutere imbere umuvuduko w'ibipimo vya Nmap (canke twizeze ko ukuri gukomeye) ni _timeout_ na _retry_.



Ku _timeouts_, iki ni **igihe co guhera c'inyishu** inyuma y'aho Nmap izohagarika kurindira inyishu maze ibone ko serivisi canke umushitsi adashobora gushikwako. Ku _retry_, uwu ni **umubare w'ibigeragezo bikurikirana ku gikorwa** Nmap izokora imbere yo gutera intambwe.



Nk'uko biri ku guhuza, _timeout_ na _retry_ uburongozi bushobora gukoreshwa ku nzira z'umushitsi canke z'ukuvumbura:





- `--min-rtt-igihe/max-rtt-igihe/intango-rtt-igihe <igihe>`: igaragaza igihe co kugaruka ca Exchange. Na none, iyo parametere mu vy’ukuri iraharurwa kandi igahindurwa ku nzira mu gihe c’ugupima. Ntibishoboka ko uzokenera kuyikoresha, kuko Nmap ibara iki gihe ku nzira bivanye n’ingene urubuga ruvyifatamwo.





- `--max-retries <umubare>`: igabanya umubare w'ibisubirwamwo vy'impapuro mu gihe co gupima icuma. Ku mburabuzi, Nmap ishobora kugera ku 10 retries ku gikorwa kimwe, cane cane iyo ibonye latency canke gutakaza ku rugero rw'urubuga, ariko kenshi na kenshi kimwe gusa ni co gikorwa.





- `--host-timeout <time>`: igaragaza igihe kinini Nmap izomara ku nzira y'umushitsi ku bikorwa vyayo vyose, harimwo no gupima icuma, kumenya ibikorwa, n'ibindi bikorwa vyose bijanye n'uwo mushitsi. Iyo iki gihe c'iherezo kirenze ata n'inyishu canke **uguheza ibikorwa**, Nmap izoheba uwo mushitsi ata n'imwe yerekanye ibisubizo biyireba, maze igende ku yindi ikurikira mu rutonde rwayo. Ivyo bigufasha kugenzura umwanya munini Nmap imara ku nzira y’umushitsi, ukirinda gufatwa n’umushitsi w’umunyaruyeri no gutuma igihe cose co gupima kigenda neza.




Mu bikorwa vyanje vya misi yose, nkoresha `--max-retries` na `--host-timeout` amahitamwo kugira ngo nkoreshe neza ibipimo vyanje:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Ibi bipimo bitanga uburyo bwo guhindura inyifato yo gupima ku bikenewe vyihariye n'imibereho y'urubuga. Ariko rero, urakeneye kumenya ingaruka zavyo ku bijanye n’umuzigo ku bashitsi ba scanner be n’ugutakaza ukuri gushobora kubaho.



### IV. Gukoresha imiterere yateguwe



Amahitamwo atandukanye twabonye muri iki gice arashobora gukoreshwa umwe umwe canke nk’igice c’imiterere yiteguye itangwa na Nmap. Ihitamwo rishoboza izo _ibigereranyo_ (ibigereranyo vy'imiterere) gukoreshwa ni `-T <umubare>` canke `-T <izina>`. Hariho 5 zikoreshwa _ibigereranyo_ ingero:



```
-T<0-5>: Set timing template (higher is faster)
```



Ku mburabuzi, Nmap ikoresha _igishushanyo_ 3 (_ibisanzwe_), ivyo muri rusangi bihagije.



Ku ruhande rwanje, muri rusangi nkora mu bihe aho nkeneye kwihuta cane (mu gihe nguma ntunganye uko bishoboka kwose) kandi kenshi nkoresha uburyo bwa `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Ehe ivyo amakuru y'ugukosora y'iyi scanner atwereka:



![nmap-image](assets/fr/64.webp)



gukoresha `-T4` gutegura mu gihe co gupima Nmap



### V. Insozero



Muri iki gice, twaravye ubuhinga n’uburyo butandukanye ushobora gukoresha kugira ngo ushobore gucunga ububasha bwa Nmap, ubukazi n’ubushobozi bwayo. Aya mahitamwo ni ngirakamaro cane cane iyo uriko uracapura amarezo manini, kandi gake cane kubera intumbero zo kwiba.



Mu gice gikurikira, turaza kuraba uburyo bwiza bukeyi bwo gukoresha Nmap no kumenya ko ataco ikora.




## 12 - Umutekano w'amakuru n'ibanga igihe ukoresha Nmap



### I. Ugushikiriza



Muri iki gice, turaza kuraba ingendo nziza zitari nke zo gukurikiza ku bijanye n’umutekano, kandi ikiruta vyose, ibanga ry’amakuru akoreshwa, atunganywa kandi abikwa na Nmap.



Ikoreshwa rya Nmap mu rwego rw’amakuru rishobora kwihuta gushirwa mu rutonde rw’igikorwa co gutera isoni. Ku bw’ivyo, hariho ingingo zitari nke zikenewe gufatwa kugira ngo umuntu akore bishingiye ku mategeko, mu gihe ariko aratanga umutekano w’ivyo umuntu yipfuza, amakuru yashizwe hamwe be n’uburyo bukoreshwa mu gupima.



### II. Kuronka uruhusha rukwiye



Imbere yo gucapura urubuga canke ubuhinga, nurabe neza ko uronse uruhusha rukwiye. Gupima uburyo bwo gupima ubugoyagoye (`NSE scripts`) ata ruhusha bishobora kuba bitemewe n’amategeko, kandi bishobora kugira ingaruka zijanye n’amategeko, cane cane iyo umutekano w’uburyo bw’amakuru utari mu bikorwa vyawe vy’ubutegetsi.





- Nk’ukwibutsa: [Itegeko ry’Igihano: Igice ca III: Ibitero ku buryo bwo gutunganya amakuru bwikoresha]




### III. Gukingira amakuru y'agaciro



Ivyo Nmap itanga bishobora gufatwa nk’ibiteye ubwoba cane cane iyo birimwo amakuru yerekeye intege nke ziri mu nzira y’amakuru yoshobora gukoreshwa n’umuntu atera. Ariko kandi iyo bireba uburyo budashobora gushikirwa na bose (nk’uburyo bw’amakuru buhambaye, bw’inganda, bw’ubuvuzi canke [ububiko] bw’amakuru (https://www.it-connect.fr/cours-tutoriels/uburyo-bw’uburongozi/autres/sauvegarde/)).



Twarabonye kandi ko, bivanye n’inyandiko za NSE zakoreshejwe, ibisubizo vy’ugupima kwa NSE kwa [Nmap](https://www.it-connect.fr/cours/) na vyo nyene bishobora kubamwo ibimenyetso.



Gutyo, umuntu w’umunyaruyeri ashobora kuronka ivyo bimenyetso vy’ivyo bipimo azoba afise ku ruhande ikarata y’urutonde rw’amakuru be n’ubutunzi bw’amakuru y’ubuhinga, ataco we ubwiwe yakoze, afise ingorane yo gufatwa.



Ni ngombwa rero kwitwararika kudakorakoranya canke kubika amakuru y’agaciro mu buryo butabereye igihe ukoresha Nmap, harimwo, ariko bitagarukiye kuri, ibi bikurikira:





- Gushiramwo amakuru y’isohoka: niba ukeneye kubika canke gutanga ibisubizo vy’ibipimo vyawe vya Nmap, urabe ko uyashiramwo amakuru kugira ngo ukinge ibanga ry’amakuru. Ivyo bizotuma umuntu adashobora gufata amakuru y’agaciro ata wemerewe. Ivyiza ni uko amakuru akwiye gushirwa mu buryo bw’ibanga akimara kuva muri sisitemu ikoreshwa mu gukora scanner (ububiko bwa ZIP bushizwe mu buryo bw’ibanga bufise ijambobanga rikomeye ni intango nziza cane).





- Gushinga ubugenzuzi bwo kwinjira: urabe neza ko abantu bemerewe bonyene ari bo bashobora gushika ku bisubizo vy’ibipimo vyawe vya Nmap aho bizobikwa. Gushinga uburyo bukwiye bwo kugenzura amakuru y’agaciro kugira ngo umuntu ntayaronke ata wemerewe.





- Ukwiyubara igihe ukoresha amakuru: igihe utanga, ukopa canke ukora amakuru y’ibarabara, urabe neza ko ugucungera neza umutekano w’amakuru. Ivyo bisigura: ntuzireke ziryamye hirya no hino mu bubiko bwa `Download` bw’ikibanza co gukoreramwo gihuye na Internet, ntuzireke zica muri dosiye yawe yo mu mutima ya HTTP Exchange, ntusige Notepad yawe yuguruye utapfunze ikibanza co gukoreramwo mu gihe c’akaruhuko kawe k’ifunguro rya sasita, n’ibindi.




### IV. Gucungera ibipimo vy'ubukazi



Nk'uko twabibonye muri iyi nyigisho yose, Nmap ishobora kuba ivuga cane ku rugero rw'urubuga. Ishobora kandi kohereza amapakete atagira uburyo bwiza, kandi adakurikiza cane imiterere y’amasezerano mu bipimo vy’urubuga n’amapakete itanga. Ivyo bikorwa vyose birashobora kugira ingaruka ku mirongo ngenderwako n’ibikorwa bimwebimwe, rimwe na rimwe bikagera ku rugero rwo gutuma uburyo n’ubuhinga n’urubuga bikora nabi canke bikazura.



Kugira ngo wirinde ibintu vyose bishobora gushika, urakeneye kumenya neza inyifato ya Nmap no kumenya ingene woyihuza n’aho ikoreshwa, biciye ku mahitamwo atandukanye yavuzwe muri iyi nyigisho. Ntituzokoresha Nmap mu buryo bumwe ku buryo bumwe ku bijanye n’amakuru arimwo [ibikoresho] vy’inganda (https://www.it-connect.fr/actualites/actu-materiel/) nk’uko biri mu rubuga rw’abakoresha rugizwe n’urubuga rwa Windows rukingiwe n’uruhome rw’umuriro rwo mu karere canke mu rubuga rw’imbere.



Nizere ko amasomo atandukanye ari muri iyi nyigisho yakugishije ingene womenya neza no gusuzuma inyifato ya Nmap, ariko uburyo bwiza bwo kwiga ni ugukora. Rero urabe neza ko umenyereye amahitamwo ya Nmap uzoba uriko urakoresha.



### V. Gukingira uburyo bwo gupima



Mu gice ca mbere, twabonye ko kenshi, Nmap ikeneye gukoreshwa nk'umuzi` canke umuyobozi w'aho hantu. Ivyo ni kubera ko ikora ibikorwa vy’urubuga, rimwe na rimwe ku rugero ruto cane, biciye mu masomero y’urubuga, asaba uruhusha rwo hejuru kandi ruteye akaga mu bijanye n’ugushikama kw’urubuga canke ibanga ry’ibindi bikoresho.



Ivyo bituma Nmap ishobora kubonwa nk’igice gihambaye c’urutonde rwashizweko. Raba neza ko ukoresha verisiyo nshasha ya Nmap, kuko verisiyo za kera zishobora kubamwo ubugoyagoye buzwi bw’umutekano. Niwakoresha verisiyo igezweho, urashobora kugabanya ingorane zijanye n’ugukoresha ico gikoresho.



Niba wahisemwo gukoresha Nmap atari biciye mu gihe nk'umuzi`, ariko mu guha uburenganzira bwihariye umukoresha afise uburenganzira kugira ngo agire vyose akeneye gukoresha Nmap (`sudo` canke _ubushobozi_), menya neza ko Nmap ishobora gukoreshwa nk'igice c'ugushira hejuru uburenganzira:



![nmap-image](assets/fr/65.webp)



gushirwa hejuru kw'uburenganzira bwa Nmap biciye kuri `sudo`._



Aha, ndiko nkoresha itegeko rya Nmap biciye muri `sudo`, ariko ivyo biramfasha kuronka igikoko gikorana nk'`umuzi` kuri sisitemu, ivyo bikaba bitari intumbero y'intango.



Ni vyiza cane kandi gushiramwo Nmap ku bikoresho bitagenewe gukora ama scans y'urubuga. Ndiko ndiyumvira cane cane ama server canke ama stations y’akazi. Ku ruhande rumwe, ivyo vyokwongerako uburyo bwo gutera hejuru, ariko ikiruta vyose vyotuma uwutera ashobora gukoresha igikoresho co gutera ata nkomanzi.



Ubwa nyuma, umutekano w’uburyo bukoreshwa mu gupima utegerezwa gushirwaho mu buryo bwagutse, kugira ngo ubwabwo ntibube umuvuduko wo kwinjira canke gusohoka kw’amakuru. Nk’umuyobozi wa sisitemu, ni vyiza gukoresha sisitemu yihariye, vyiza cane ifise ubuzima buke, aho gukoresha ikibanza cawe co gukoreramwo.



### VI. Iciyumviro



Mu gusozera, urabe neza ko umenye neza Nmap imbere yo kuyikoresha mu buzima nyakuri canke mu bikorwa vy’ubuhinga, kandi ube maso igihe ukora no gucunga ibiva muri yo. Vyoba ari ikibabaje gutera ingorane, gusohora amakuru canke kworohereza ugusenyera ku mugozi umwe, mu gihe uburyo bwa mbere bugamije gutuma umutekano w’ishirahamwe ryawe utera imbere.



## 13 - Ivyuma bikoreshwa na TCP: SYN, Guhuza na FIN



### I. Ugushikiriza



Muri iki gice n’igikurikira, tuzokwihweza neza ubwoko butandukanye bw’ibipimo vya TCP biri muri Nmap, dutanguriye ku bikoreshwa cane: SYN, Connect na FIN scans.



Nk'uko mushobora kuba mwabibonye, ​​Nmap itanga uburyo bwinshi bwo gupima TCP:



![nmap-image](assets/fr/66.webp)



ubuhinga bwo gupima buboneka muri Nmap._



Iciyumviro kiri aha ni ugusigura bumwe muri ubwo buryo, kugira ngo ushobore gutahura ukuntu butandukanye, akamaro kabwo n’aho bugarukira. Uzobona ko, bivanye n’aho uvuga canke ivyo ushaka kumenya, ari vyiza guhitamwo uburyo bumwe canke ubundi.



### II. TCP SYN scanner canke "Igice c'ugufungura scanner



Ubwoko bwa mbere bw'isuzuma rya TCP tugiye kuraba ni `Isuzuma rya TCP SYN`, rizwi kandi nka `Isuzuma ry'Igice Gifunguye`. Niba wibuka ama scanners y’urubuga twakoze inyuma y’ama scanners yacu ya mbere y’icuma, ubu ni bwo bwoko bw’ama scanners bukoreshwa ku buryo busanzwe na [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilities/) iyo ikoreshejwe n’uburenganzira bw’umuzi.



Impinduro izogufasha gutahura ingene iyo scanner ikora. Nkako, TCP SYN scan izorungika umuzigo wa TCP SYN ku port yose igenewe, ari wo muzigo wa mbere woherejwe n’umukiriya (uwo asaba gushinga uruja n’uruza) nk’igice c’umuzigo uzwi cane _Three way handshake_ TCP. Mu bisanzwe, iyo port yuguruye kuri server y’intumbero, hariho service iriko irakora inyuma yayo, server izogarukana ipakete ya TCP SYN/ACK kugira ngo yemeze SYN y’umukiriya no gutangura ihuriro rya TCP. Iyi nyishu ifata uburyo bw’ipakete ya TCP ifise amabendera ya SYN na ACK ashizwe kuri 1, bikadushoboza kwemeza ko icuma kifunguye kandi kijana ku gikorwa.



Ku rundi ruhande, iyo icuma gipfutse, umukozi azotwoherereza `TCP` packet ifise amabendera ya RST na ACK ashizwe kuri 1 kugira ngo ahagarike igisabwa co guhuza, rero tuzomenya ko ata serivisi isa n'iyikora inyuma y'iki kivuko:



![nmap-image](assets/fr/67.webp)



tCP SYN Gupima inyifato y'ikigereranyo c'ivyambu vyuguruye n'ivyugarijwe



Kugira ngo mbone neza `TCP SYN Scan`, nakoze scanner ya port TCP/80 ku host yari ifise server y'urubuga ikora kuri iyo port. Gukoresha urubuga rwo gupima na Wireshark, turashobora kubona uruja n'uruza rukurikira (inkomoko y'ugupima: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



urubuga rwafashwe mu gihe ca TCP SYN scanner ku cambu kifunguye



Ku murongo wa mbere, turabona ko inkomoko y'ibarabara iriko irarungika umuzigo wa TCP ku kwakira `10.10.10.203` ku cambu TCP/80. Muri iyi paketi ya TCP, ibendera rya SYN rishirwa kuri 1 kugira ryerekane ko ari igisabwa co gutangura guhuza TCP.



Hanyuma, ku murongo wa kabiri, turabona ko iyo ntumbero yishura n'i `TCP SYN/ACK`, bisobanura ko yemera gutanguza ihuriro rero ikakira imigende ku port TCP/80. Turashobora rero gufata ingingo y’uko port TCP/80 yuguruye kandi ko hariho umukozi w’urubuga kuri umukozi wa scanner.



Uwo mushitsi wacu aca arungika ipakete ya RST kugira ngo afunge uruja n’uruza, ivyo bikaba bituma uwo mushitsi ya scanner adaguma afise uruja n’uruza rwa TCP rwuguruye arindiriye inyishu. Mu gihe co gupima ku bibanza vyinshi, kudafunga amahuzu ya TCP vyoshobora gutuma umuntu yanka gukoresha, bikaba vyuzuye umubare w’amahuzu arindiriye kwishurwa ko umukozi ashobora kubungabunga (raba [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



Muri Wireshark, uzoshobora kubona uko amabendera ya TCP ameze ku kigeragezo cose dukora. Ivyo bizokwerekana nimba iyo paketi ari SYN, SYN/ACK, ACK, n'ibindi:



![nmap-image](assets/fr/69.webp)



reba amabendera ya TCP muri Wireshark (TCP SYN hano)



Ku rundi ruhande, narakoze ikigeragezo kimwe hagati y’izo mashini zibiri, ariko ubu ndiko ndapima icuma ca TCP/81 ata n’imwe ikora (inkomoko y’ugupima: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



urubuga rwafashwe mu gihe c'isuzuma rya TCP SYN ku cambu gifunze



Igikoresho ca scanner kigarura `TCP RST/ACK` mu kwishura `TCP SYN` yanje iyo icuma kitafunguye.



Nk'uko vyavuzwe, iyo ukoresheje Nmap uvuye ku nzira y'uburenganzira, TCP SYN Scan ni uburyo mburabuzi, kandi ishobora guhatirwa biciye ku `-sS` (`scan SYN`) uburyo:



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




`TCP SYN Scan` ni yo ikoreshwa cane kubera imvo z'umuvuduko. Ku rundi ruhande, ukunanirwa kw’umukiriya gusozera _Three Way Handshake_ (ni ukuvuga kutarungika ACK inyuma ya server SYN/ACK) bishobora gusa n’ibiteye amakenga iyo bibonwa incuro nyinshi cane kuri server canke bivuye ku nzira imwe ku rubuga. Nkako, inyifato isanzwe y'umukiriya amaze kwakira umuzigo wa TCP SYN/ACK mu kwishura kuri TCP SYN ni ukurungika `ukwemera` (ACK) hanyuma agatangura Exchange.



Naho biri ukwo, iratanga scanner yihuta gatoyi, kuko itababazwa no kohereza ACK ku nyishu nziza yose. Ivyiza vya SYN Scan ni umuvuduko wayo, kuko harungikwa ipakete imwe gusa ku kivuko cose kugira ngo gicapurwe, bikaba bituma habaho amahirwe menshi yo kumenya.



Ikindi, TCP SYN scan irashobora kumenya nimba icuma gicunzwe (kirindwa) n’uruhome rw’umuriro. Nkako, uruhome rw’umuriro ruri imbere y’umushitsi w’intumbero rushobora kumenyekana biciye ku kuntu rwitwararika iyo rwakiriye umuzigo wa TCP SYN ku cambu gikwiye gukingira. Ntizokwishura gusa. Ariko nk’uko twabibonye, ​​muri ivyo vyose (icuma gifunguye canke gipfutse), hari inyishu ivuye ku mushitsi. Iyi nyifato ya gatatu izokwerekana ko hariho uruhome rw’umuriro hagati y’umushitsi ya scanner n’imashini ikoresha scanner. Ehe igisubizo Nmap ishobora kugaruka iyo icuma gicunzwe n'uruhome rw'umuriro:



![nmap-image](assets/fr/71.webp)



nmap igaragaza iyo uscama icuma cayunguruwe



Iyo dukoze igikorwa co gufata urubuga ku gihe co gupima, turashobora kubona ko ata n’inyishu itangwa:



![nmap-image](assets/fr/72.webp)



urubuga rwafashwe mu gihe ca TCP SYN scanner ku cambu cayunguruwe n'uruhome rw'umuriro



Itandukaniro hagati y’icuma gipfutse n’icuma gicunzwe ni iri: icuma gicunzwe ni icuma kirindwa n’uruhome rw’umuriro, mu gihe icuma gipfutse ni icuma ata serivisi iriko irakorako kandi rero kidashobora gukora amapakete yacu ya TCP. Hari ubwoko bw’ugupima TCP, nk’ugupima TCP SYN, burashobora kumenya nimba icuma cacunzwe, mu gihe ubundi bwoko bw’ugupima butashobora.



### III. TCP Guhuza scan canke gufungura scan



Ubwoko bwa kabiri bw'isuzuma rya TCP ni `isuzuma ry'ihuriro rya TCP`, rizwi kandi nka _Isuzuma ry'ugufungura ryose_. Ikora nk'uko TCP SYN scan ikora, ariko ubu igarukana `TCP ACK` inyuma y'inyishu nziza ivuye kuri server (SYN/ACK). Ni co gituma yitwa `Full Open', kuko uruja n'uruza rufungurwa rwose kandi rugatangura ku nzira yose yuguruwe mu gihe co gupima, gutyo bikaba vyubahiriza TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



tCP Huza Scan inyifato y'ikigereranyo c'ivyambu vyuguruye n'ivyugarijwe



Ehe ivyo ushobora kubona bica ku rubuga mu gihe ca `TCP Connect scan` bishingiye ku port yuguruye:



![nmap-image](assets/fr/74.webp)



guhobera urusobe rw'amakuru mu gihe c'ugupima TCP Connect kugira ngo ubone icuma gifunguye



Turashobora kubona ko umuzigo wa mbere wa TCP woherejwe ari `TCP SYN` woherejwe n’umukiriya, maze umukozi azoca yishura n’ijambo `TCP SYN/ACK`, vyerekana ko icuma gifunguye kandi gifise igikorwa gikora. Kugira ngo wigane umukiriya yemewe inzira yose, Nmap izoca yohereza `TCP ACK` kuri server. Ku rundi ruhande, iyo uriko urasuzuma icuma gipfutse:



![nmap-image](assets/fr/75.webp)



urubuga rwafashwe mu gihe c'ugupima TCP guhuza n'icuma gipfutse



Zirikana ko inyishu ya server ku mpapuro zacu za `SYN` ari kandi mpapuro za `TCP RST/ACK`, rero turashobora gufata ingingo y'uko icuma gipfutse kandi ko ata mirimo iriko irakora kuri co.



Iyo ukoresheje Nmap, `-sT` (`gupima guhuza`) ikoreshwa mu gukora gupima guhuza TCP. Urashobora kubona ko iyo Nmap ikoreshejwe kuva mu gihe kitagira uburenganzira, ubu ni uburyo bwo gupima TCP:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



`TCP Connect Scan` yigana igisabwa c'ihuriro ry'ukuri, n'inyifato isa cane n'iy'umukiriya wa lambda, rero biragoye kubona scan ku mubare w'ibibanza ugabanutse. Ariko rero, iragenda buhoro, kuko itanguza bimwe bishitse uruja n’uruza rwose rwa TCP ku bibanza vyuguruye vy’imashini ya scanner.



Igikoresho co gupima Nmap c’ibivuko 10.000 kizoguma gishobora kumenyekana bitagoranye iyo hashizweho ubuhinga bwo kumenya no kurinda abaje mu rubuga (IDS, IPS, EDR). Iyo umuterabwoba ashaka kuguma afise urutonde ruto, azokunda kwibanda ku mubare mutoyi w’ibibanza vyatoranijwe neza, nka 445 (SMB) canke 80 (HTTP), akenshi bifungurwa ku ma server kandi bikaba bigaragaza ubugoyagoye rusangi.



Kubera ko TCP Connect Scan yiteze inyishu muri ivyo bihe vyose, irashobora kandi kumenya ko hariho uruhome rw’umuriro rushobora kuba ruriko ruracungera ivyuho ku nzira y’umushitsi.



### IV. TCP FIN gupima canke "Gupima mu buryo bwihishije



`TCP FIN Scan`, izwi kandi nka _Stealth Scan_, ikoresha inyifato y'umukiriya ahagarika uruja n'uruza rwa TCP kugira ngo amenye icuma kigutse.



Mu TCP, iherezo ry’ikiganiro bisigura kohereza umuzigo wa TCP ufise ibendera rya FIN rishizwe kuri 1. Muri Exchange isanzwe, umukozi arahagarika guhanahana amakuru yose n’umukiriya (nta n’inyishu). Iyo server idafise ubufatanye bwa TCP n'umukiriya, izorungika `RST/ACK`. Turashobora rero gutandukanya ivyuho vyuguruye n'ivyugarijwe mu kohereza amapakete ya `TCP FIN` ku vyuho vyinshi:



![nmap-image](assets/fr/76.webp)



tCP FIN scan inyifato y'ikigereranyo c'ivyambu vyuguruye n'ivyugarijwe



Nasubiye gufata urubuga mu gihe ca _Stealth scan_ kandi ibi nivyo ubona iyo port ya scanner yuguruye:



![nmap-image](assets/fr/77.webp)



urubuga rwo gufata mu gihe c'ugupima TCP FIN ku cambu kifunguye



Turashobora kubona ko umukiriya yohereza ipakete imwe canke zibiri kugira ngo ahagarike uruja n’uruza rwa TCP kandi ko umukozi ntaco yishuye. Iremera gusa iherezo ry’uguhuza maze igahagarika guhanahana amakuru.



Ehe ivyo tubona ubu iyo dusuzumye icuma gipfutse:



![nmap-image](assets/fr/78.webp)



urubuga rwafashwe mu gihe c'itohoza rya TCP FIN ku cambu gifunze



Turabona ko server irungika `TCP RST/ACK` packet, rero hariho itandukaniro mu nyifato hagati y'icuma gifunguye n'icafunze, kandi turashobora gutanga urutonde rw'ivyambu vyuguruye kuri server mu kohereza packet ya TCP FIN. Ukoresheje Nmap, `-sF` (`gupima FIN`) ikoreshwa mu gukora TCP FIN Scan:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan ntikora ku bashitsi ba Windows, kuko OS ikunda kwirengagiza amapakete ya TCP FIN iyo yoherejwe ku bibanza bitafunguye. Rero iyo ukoresheje TCP FIN Scan ku host ya Windows, uzobona ko ports zose zipfutse.



Ni co gituma bihambaye kumenya uburyo bwinshi bwo gupima, no gutahura itandukaniro riri hagati yavyo.



Kubera ko muri ivyo vyose TCP FIN itazorindira inyishu, ntizoshobora kumenya ko hariho uruhome rw’umuriro hagati y’umushitsi w’intumbero n’inkomoko y’ugupima.



Aha ni akarorero k'igisubizo ca TCP FIN ca Nmap:



![nmap-image](assets/fr/79.webp)



ibisubizo vy'isuzuma rya TCP FIN ryakozwe na Nmap._



Nkako, ukudasubiza kw'umushitsi ku cambu gitanzwe bishobora gusobanura ko cambu gicunguruwe, ariko kandi ko kifunguye kandi gikora.



Iyi scan yitwa "stealth", kuko idatuma generate igira uruja n'uruza rwinshi kandi muri rusangi ntituma umuntu yinjira mu bikoresho vy'ubuhinga. Ishobora gukoreshwa mu kuvumbura mu buryo bw’ubukerebutsi ivyuho biri ku rubuga ata n’imwe itera inkengeri. Ariko nk’uko twabibonye haruguru, ubushobozi bwayo burashobora guhinduka bivanye n’uburyo bugenewe, nk’uko nyene ubukerebutsi bwayo bushobora guhinduka bivanye n’ingene ibikoresho vy’umutekano vyubatswe.



### V. Insozero



Ivyo ni vyinshi ku gice ca mbere mu bice bibiri ku bwoko butandukanye bwa TCP scan itangwa na Nmap! Mu gice gikurikira, turaza kuraba ubwoko bwa XMAS, Null na ACK TCP scan, bukora mu buryo butandukanye kugira ngo bumenye ama ports yuguruye ku host.





## 14 - Ivyuma bipima biciye kuri TCP: XMAS, Ubusa na ACK



### I. Ugushikiriza



Muri iki gice, tuzobandanya gutohoza uburyo butandukanye bwo gupima TCP butangwa na Nmap. Aha turaza kuraba uburyo bwa `XMAS`, `Null` na `ACK`, bukoresha ibiranga TCP kugira ngo bubone amakuru ku bibanza n'ibikorwa vyuguruye ku ntumbero yatanzwe.



### II. TCP XMAS gupima



XMAS Scan TCP ni ikintu kidasanzwe gatoyi kuko idashobora kwigana inyifato isanzwe y’ukoresha canke y’imashini ku rubuga na gato. Nkako, XMAS Scan izorungika amapakete ya TCP afise amabendera `URG` (Ivyihutirwa), `PSH` (Isunika), na `FIN` (Irangije) ashizwe kuri 1, kugira ngo irengere inkuta zimwe zimwe z’umuriro canke uburyo bwo kuyungurura.



Izina XMAS rikomoka ku kuba kubona ayo mabendera ariho ari ikintu kidasanzwe. Iyo amabendera yose atatu ashizwe icarimwe mu mpapuro za TCP, asa n'igiti ca Noweli caka:



![nmap-image](assets/fr/80.webp)



tCP amabendera akoreshwa mu gupima XMAS



Tutagiye mu ndondoro ku ruhara rw'ayo mabendera hano, birahambaye kumenya ko iyo wohereje ipakete ifise ayo mabendera atatu akoreshwa, igikorwa gikora inyuma y'icuma c'intumbero ntikizogarura amapakete yose. Ku rundi ruhande, iyo port ifunze, tuzoronka umuzigo wa TCP RST/ACK. Ubu tuzoshobora gutandukanya inyifato y'icuma gifunguye n'icafunze igihe dutanga urutonde rw'icuma ku mashini:



![nmap-image](assets/fr/81.webp)



tCP XMAS Scan inyifato y'ikigereranyo c'ivyambu vyuguruye n'ivyugarijwe



Naho nyene ukurikije iyo nzira nyene, gupima urubuga ku port TCP/80 y'umushitsi afise umukozi w'urubuga akora yerekana inyifato ikurikira iyo ubonye port yuguruye (inkomoko y'ugupima `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



urubuga rwafashwe mu gihe c'ugupima TCP XMAS ku cambu kifunguye



Turashobora kubona ko inkomoko y’ibarabara yohereza amapakete abiri ya TCP XMAS (afise amabendera `FIN`, `PSH` na `URG` ashizwe kuri 1) kugira ngo yakira `10.10.10.203` kandi ko ata n’imwe igaruka kuva ku ntumbero, vyerekana ko icuma kifunguye. Ku rundi ruhande, iyo ukora `TCP XMAS Scan` ku cambu gipfutse, igisubizo gikurikira kiraboneka:



![nmap-image](assets/fr/83.webp)



urubuga rwafashwe mu gihe c'ugupima TCP XMAS ku cambu gifunze



Inyishu ku mpapuro zacu za TCP rero ni `TCP RST/ACK`, yerekana ko icuma gipfutse. Kugira ngo ukoreshe ubu buhinga na Nmap, `-sX` (`gupima XMAS`) ihitamwo riguha uburenganzira bwo gukora TCP XMAS Scan:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Ni vyiza kumenya ko TCP XMAS scan idashobora kumenya ibihome vy’umuriro bishobora kuba biri hagati y’ico ushaka n’imashini y’ugupima, bitandukanye n’ubundi bwoko bumwe bumwe bw’ugupima nka TCP SYN canke Connect. Nkako, uruhome rw’umuriro rukora hagati y’abashitsi babiri ruzotuma ata TCP igaruka iyo icuma c’intumbero kiyunguruwe (ni ukuvuga kirindwa n’uruhome rw’umuriro). Iyo rero ataco yishuye, ntibishoboka rero kumenya nimba ico kivuko kirindwa n’uruhome rw’umuriro canke kifunguye kandi gikora. Ushobora kandi kumenya ko, cokimwe n’ugupima TCP FIN, hariho porogarama canke ubuhinga bumwebumwe nka Windows bushobora guhindura ibivuye muri ubwo bwoko bw’ugupima.



iciyumviro: ugushigikira XMAS/FIN/NULL scans ku verisiyo za Windows ziherutse gusohoka biracari bike, kandi ibisubizo bishobora kuba bidahuye kuri ubwo bwoko bw'intumbero. (Ivugurura 2025)_



### III. TCP ubusa gupima



Mu buryo butandukanye n’ugupima TCP XMAS, TCP Null scan izorungika amapakete ya TCP scan afise amabendera yose ashizwe kuri 0. Ivyo navyo ni inyifato itazokwigera iboneka mu Exchange isanzwe hagati y’amamashini, kuko kohereza amapakete ya TCP ata bendera bitavugwa muri RFC idondora porotokole ya TCP. Ni co gituma bishobora kumenyekana bitagoranye.



Nka TCP XMAS scan, iyo scan ishobora guhungabanya ibihome bimwe bimwe canke ibice bimwe bimwe vy'ukuyungurura, bigatuma amapakete ashobora guca muri:



![nmap-image](assets/fr/84.webp)



tCP Null Scan inyifato y'ikigereranyo c'ivyambu vyuguruye n'ivyugarijwe



Ehe ivyo ushobora kubona ku rubuga mu gihe c'ugupima TCP Null ku port yuguruye:



![nmap-image](assets/fr/85.webp)



urubuga rwafashwe mu gihe ca TCP Null scan ku cambu kifunguye



Igikoresho co gupima cohereza umuzigo utagira ibendera (`[<Nta>]` muri Wireshark) ata n'inyishu ivuye kuri server. Ku rundi ruhande, iyo icuma c'intumbero gipfutse:



![nmap-image](assets/fr/86.webp)



urubuga rwafashwe mu gihe ca TCP Null scanner ku cambu gifunze



Kugira ngo ukore igikorwa co gupima TCP ubusa na Nmap, koresha gusa `-sN` (`gupima ubusa`) uburyo:



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Kubera ko inyishu iyo port yuguruye n’igihe uruhome rw’umuriro rukora (nta n’inyishu ya server muri ivyo bibiri) ari imwe, TCP Null scan ntishobora kumenya ko hari uruhome rw’umuriro. Ikindi, iyo firewall ishobora mbere kubesha igisubizo mu gutanga iciyumviro c’uko port yuguruye, kuko idasubiza amapakete ya TCP ata mabendera, naho port iyunguruwe. Aya ni amakuru ahambaye yo kumenya igihe ukoresha ibipimo bidashobora gutandukanya hagati y’icuma gifunguye n’icacunzwe (kikingiwe n’uruhome rw’umuriro), nk’ibipimo vya `TCP Null`, `XMAS` canke `FIN`, kugira ngo bigume bihuye mu gusobanura ibisubizo vyaronswe.



### IV. TCP ACK gupima



Igikoresho ca TCP ACK gikoreshwa mu kumenya ko hariho uruhome rw’umuriro ku ntumbero canke hagati y’intumbero n’inkomoko y’isuzuma.



Udakunze ibindi bipimo, igipimo ca TCP ACK ntikigerageza kumenya ivyuho vyuguruye ku nzira, ahubwo kigerageza kumenya nimba uburyo bwo kuyungurura bukora, bwishura ku vyuho vyose `vyayunguruwe` canke `bitayunguruwe`. Ivyiyumviro bimwe bimwe vya TCP, nka `TCP SYN` canke `TCP Connect`, bishobora gukora vyose igihe kimwe, mu gihe ibindi, nka `TCP FIN` canke `TCP XMAS`, bidashobora kumenya ko hariho ukuyungurura na gato. Ni co gituma TCP ACK scan ishobora kuba ngirakamaro:



![nmap-image](assets/fr/87.webp)



tCP ACK Gupima inyifato y'ikigereranyo c'ivyambu vyayunguruwe n'ibitayunguruwe



Tuzokoresha uburyo bwa Nmap `-sA` kugira ngo dukore ubwo bwoko bw'ugupima. Ehe igisubizo ca TCP ACK scan nimba icuma cacunzwe, ni ukuvuga kibujijwe kandi kirindwa n'uruhome rw'umuriro:



![nmap-image](assets/fr/88.webp)



nmap yerekana mu gihe c'Isuzuma rya TCP ACK._



Akarorero k'igisubizo ku mushitsi afise uruhome rw'umuriro n'uwutagira. Nmap igarura `yayunguruwe` ku vyambu TCP/80 na TCP/81 vy'umushitsi `10.10.10.203`. Ku bijanye n’isesengura ry’urubuga biciye kuri Wireshark, inyifato ni iyi:



![nmap-image](assets/fr/89.webp)



urubuga rwafashwe mu gihe ca TCP ACK scanner ku cambu kitayunguruwe n'uruhome rw'umuriro



Imashini y’intumbero ntaco igarura iyo hariho uruhome rw’umuriro.



Kugira ngo utangure iki gipimo na Nmap, koresha `-sA` (`igipimo ACK`) uburyo:



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Insozero



Twaravye uburyo butatu butandukanye bwo gucapura biciye kuri TCP uretse ubwo twamaze gushikirizwa. Ubwo buryo butandukanye buzokoreshwa mu bihe vyihariye cane, cane cane mu bigeragezo vyo kwinjira mu gihugu canke ibikorwa vy’Ikigo Gitukura, aho ivyiyumviro vy’ubukerebutsi biriho.



## 15 - Nmap CheatSheet - Incamake y'amabwirizwa y'inyigisho



### I. Ugushikiriza



Aha niho hari incamake ngufi y'amabwirizwa menshi ya Nmap n'ingene ikoreshwa, kugira ngo ushobore kuyaronka ningoga no kuyasubira gukoresha mu gukoresha kwa misi yose.



### II. Nmap: Urupapuro rw'ubuhendanyi IT-Ihuza



Ehe urupapuro rw'ubuhendanyi rw'amabwirizwa yashikirijwe. Iyi paji ituma vyoroha kuronka ikoreshwa rya Nmap risanzwe.





- Gupima icambu




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Kuvumbura abashitsi bakora




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



iciyumviro: Ihitamwo rya `-sP` ryamaze imyaka myinshi ritagikoreshwa kandi rikwiye gusubirizwa na `-sn`. (Ivugurura 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Kumenya verisiyo




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Ivyanditswe vya NSE: kurondera ubugoyagoye




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Ubuyobozi bw'igisohoka ca Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Gutuma ibikorwa bigenda neza




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Ubwoko bwa TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Nizigiye ko aya mabwirizwa muzosanga ari ngirakamaro. Ntukibagire guhindura intumbero y’ibipimo vyawe n’aho uri no kuraba inyandiko zizwi kugira ngo umenye neza ibipimo vyakozwe.



### III. Iciyumviro



Inyigisho ya Nmap ubu iraheze. Ubu urafise ibintu vy’ishimikiro ukeneye kugira ngo ukoreshe ico gikoresho gikomeye kandi gikomeye. Turaguhanura cane kwimenyereza ku bidukikije bigenzurwa (Hack The Box, VulnHub, imashini zitaboneka) imbere y’uko ukoresha mu gukora.



Hari vyinshi bikiriho vyo gutohoza ku bijanye n’ingene ico gikoresho gikora imbere be n’ibintu biteye imbere birimwo. Ariko rero, kumenya neza amabwirizwa n’ivyiyumviro vyerekanwa ngaha bizokuronsa ubushobozi bwo gukoresha Nmap wizigiye kandi ufise akamaro.