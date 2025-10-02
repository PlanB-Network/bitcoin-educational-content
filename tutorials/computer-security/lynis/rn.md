---
name: Lynis
description: Gukora igenzura ry'umutekano w'imashini ya Linux na Lynis
---
![cover](assets/cover.webp)



___



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Fares CHELLOUG vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Birashoboka ko hari ivyo bahinduye mu canditswe c’intango.*



___



## I. Ugushikiriza



**Muri iyi nyigisho, turaza kwiga ingene twokora igenzura ry'umutekano ku mashini ya Linux dukoresheje Lynis! Ku batazi** Lynis, **ni umurongo mutoyi w'amabwirizwa uzosuzuma uko server yawe ikora maze ugatanga impanuro zo gutuma umutekano w'imashini yawe urushiriza kuba mwiza.**



Lynis ni igikoresho gifunguye kivuye muri CISOFY, ishirahamwe ryitaho **ugusuzuma no gukomeza ubuhinga**. Niba ushaka gutera imbere mu gukomeza Linux n’ibikorwa vy’abantu benshi (SSH, Apache2, n’ibindi), Lynis ni umufasha wawe! Lynis ntakubwira gusa ivyo bigenda nabi, ariko kandi aratanga impanuro zo kukwereka inzira nziza (kandi akagukiza umwanya).



**Lynis** ikorana n'ibikoresho vyinshi vya Linux, harimwo: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis igenewe abakoresha Linux / UNIX, ariko kandi irahuye na **macOS**. Ivyihuta cane gushiramwo, nta n'uburongozi bw'abavyifatamwo ku rugero rwa package.



Ikoreshwa mu bintu bitandukanye:





- Igenzura ry'umutekano
- Igerageza ryo kwubahiriza amategeko (PCI, HIPAA na SOX)
- Imiterere ya sisitemu ikomeye
- Gutahura ubugoyagoye



Ico gikoresho gikoreshwa cane n’abantu benshi, harimwo abarongozi ba sisitemu, abagenzuzi b’ivy’ubuhinga bwa none n’abahinga mu vy’ubuhinga bwa none. Ku bijanye n’isesengura, igikoresho gishingiye ku ngingo ngenderwako nka **Ikigereranyo ca CIS, NIST, NSA, OpenSCAP** no ku mpanuro zizwi zivuye kuri **Debian, Gentoo, Red Hat**.



Umugambi uraboneka kuri iyi Address kuri **Github**:





- [GitHub - Lynis] (Ubuhinga bwa none)
- [Kura Lynis kuri CISOFY]



Muri iyi nyigisho y’intambwe ku yindi, ngiye **gukoresha VPS ikoresha Debian 12** kandi ngiye kwibanda ku gice ca SSH, kuko noshima kugenzura uko giteye no kugitera imbere.



## II. Gukuraho no gushiramwo



Hari uburyo bwinshi bwo gukura no gushiramwo Lynis. Hitamwo iyo ukunda mu rutonde ruri aha hepfo.



### A. Gushiramwo bivuye mu bubiko bwa Debian



Ubu buryo bwo gushiramwo buraguha uburenganzira bwo gukoresha itegeko **lynis** uri aho hose kuri sisitemu, bitandukanye n'ugushiramwo kuva ku nkomoko, aho ukeneye kuba uri mu bubiko.



Huza na server yawe biciye kuri SSH hanyuma winjize amabwirizwa akurikira kugira ngo ushiremwo Lynis:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Ivyo nivyo uronka:



![Image](assets/fr/024.webp)



### B. Kuva ku rubuga rwemewe



Ushobora kandi kuyikura ku rubuga rwa Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Ivyo nivyo uronka:



![Image](assets/fr/032.webp)



Ibikurikira, tuzofungura ububiko dukoresheje itegeko rikurikira:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Ivyo nivyo uronka:



![Image](assets/fr/020.webp)



Reka tuje kuri dosiye ya **lynis**:



```
cd lynis
```



Turashobora kugenzura ivyahinduwe dukoresheje iri tegeko rikurikira:



```
./lynis update info
```



Ivyo nivyo uronka:



![Image](assets/fr/023.webp)



### C. Gukura kuri GitHub



Tuzokura **Lynis** mu bubiko bwa GitHub, dukoresheje itegeko rikurikira (*git* itegerezwa kuba iri ku mashine yawe):



```
git clone https://github.com/CISOfy/lynis.git
```



Ivyo nivyo uronka:



![Image](assets/fr/060.webp)



## III. Gukoresha Lynis



Lynis ariho ku mashine yacu, rero reka twige uko tuyikoresha!



### A. Ivy'ingenzi bigenzura n'amahitamwo



Kugira ngo ugaragaze amabwirizwa ariho, ushiremwo gusa iri tegeko rikurikira:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



Ivyo nivyo uronka:



![Image](assets/fr/039.webp)



Kandi uraronka n’amahitamwo akurikira:



![Image](assets/fr/040.webp)



Kugira ngo ugaragaze amabwirizwa yose ariho, shiramwo itegeko rikurikira:



```
sudo lynis show
```



Ivyo nivyo uronka:



![Image](assets/fr/022.webp)



Niba wifuza kugaragaza amahitamwo yose, utegerezwa kwinjiza:



```
sudo lynis show options
```



Ivyo nivyo uronka:



![Image](assets/fr/021.webp)



Mu bindi bice vy’iki kiganiro, turaza kwiga ingene twokoresha uburyo bumwebumwe.



### B. Gukora igenzura rya sisitemu



Tugiye gusaba **Lynis** gusuzuma system yacu, agaragaze ivyo vyatunganijwe neza n'ivyo vyoshobora gutera imbere. Kugira ngo ubikore, shiramwo itegeko rikurikira:



```
sudo lynis audit system
# ou
./lynis audit system
```



Ku mburabuzi, iyo utarinjiye nk'umuzi igihe ukoresha iri tegeko, igikoresho kizokorana n'uburenganzira bw'ukoresha yinjiye ubu. Hari ibigeragezo bitazokorwa muri iki gihe:



![Image](assets/fr/052.webp)



Aha niho ibipimo bitazokorwa muri ubu buryo:



![Image](assets/fr/051.webp)



Itegeko rihejeje gushirwa mu ngiro, isesengura riratangura. Rindira gato gusa.



Mu mpera z'igenzura, ubona ibi (turashobora kubona ko **Lynis** yamenye neza **Debian 12** system kandi azokoresha **Debian plugin** mu gusesangura):



![Image](assets/fr/017.webp)



Inyuma y’aho, Lynis azotanga urutonde rw’ingingo zihuye n’ivyo vyose yasuzumye kuri sisitemu yacu. Ivyo bitunganijwe hakurikijwe ivyiciro, nk’uko tuzobibona. Ni vyiza kandi kumenya ko kode y'ibara ikoreshwa mu kugaragaza impanuro:





- Umutuku** ku Elements ihambaye canke ibikorwa vyiza bitubahirijwe (akarorero, umuzigo ubuze), ni ukuvuga ko umukozi wawe atayubaha iyi ngingo
- Umuhondo** ku vyiyumviro canke kwubahiriza igice c'impanuro (reka tuvuge ko ari ugushirwako kwubahiriza ingingo yerekanwa n'iri bara (itari imbere))
- Green** ku ntumbero aho imiterere ya server yawe ihuye
- Umweru**, iyo utagira aho ubogamiye



Aha, turabona ko Lynis asaba gushiramwo **fail2ban**:



![Image](assets/fr/057.webp)



Mu gice ca "**Boot na services**", turabona ko uburinzi bw'ibikorwa biciye kuri *systemd* bwoshobora guterwa imbere. Ku ruhande rwiza, Grub2 iriho kandi nta ngorane ziriho ku vyerekeye uruhusha kuri:



![Image](assets/fr/029.webp)



Hanyuma ufise ibice vya "**Kernel**" na "**Ukwibuka n'Imigenderanire**":



![Image](assets/fr/037.webp)



Inyuma y'aho, igice ca "**Abakoresha, Amatsinda n'Ivyemezo**". Ico gikoresho kitumenyesha imburi ku burenganzira bw'ububiko "**/etc/sudoers.d**". Kugeza ubu, ntituzi vyinshi, ariko tuzoshobora kubona impanuro iyo ari yo mu mpera y’isesengura.



![Image](assets/fr/049.webp)



Ehe ivyo ushobora gusanga mu bice vya "**Ibikoko", "Ibikoresho vy'amadosiye", na "Ibikoresho vya USB "**. Mu bindi, turashobora kubona ko hariho ivyiyumviro ku bijanye n’aho umuntu yoshira ibintu be n’uko ubu ibikoresho vya USB vyemewe kuri iyo mashini.



![Image](assets/fr/048.webp)



Inyuma y'aho, ibice: "**Ibikorwa vy'amazina", "Ivyambu n'amapaki", "Imirongo".** Birerekana aha ko amapaki atagikoreshwa yoshobora gusukurwa kandi ko ata n'imwe ishobora gucungera ivyagezwe vy'ubuhinga.



![Image](assets/fr/058.webp)



Turashobora kubona ko uruhome rw’umuriro rukora (kandi egome, hariho iptables!). Ikindi, turashobora kubona ko yasanze amategeko atakoreshwa kandi ko hariho umukozi w’urubuga rwa Apache.



![Image](assets/fr/055.webp)



Ivyo bikurikirwa no gusuzuma urubuga ubwarwo, kuko iyo serivisi yamenyekanye.



Turashobora kubona ko yabonye amadosiye y'imiterere ya **Nginx**, kandi ko ku gice ca SSL/TLS, **amadosiye y'imiterere** atunganijwe hakoreshejwe umurongo w'amategeko woba udatekanye. Ku rundi ruhande, nk’uko Lynis abivuga, ugucungera ibiti ni ukuri.



![Image](assets/fr/038.webp)



Ivyo bikoresho vya SSH biri kuri server yanje ya VPS. Ivyo itunganijwe birasesangurwa na Lynis. Bitegerezwa kuvugwa ko umutekano wa SSH ushobora gutera imbere bitagoranye! Tuzogaruka muri ivyo mu buryo burambuye nitwamara kuronka impanuro.



![Image](assets/fr/026.webp)



Aha niho hari ibice **"Ifashanyo ya SNMP", "Ibikoresho vy'amakuru", "PHP", "Ifashanyo ya Squid", "Ibikorwa vya LDAP", "Ivyanditswe n'amadosiye "**.



Hariho iciyumviro kimwe gihambaye cane ku bijanye no gucunga ibitabo: biraremeshwa cane ko udabika ibitabo gusa aho hantu ku mashini yawe. Iyo iyo mashini yononekaye n’umuntu ayitera, birashoboka ko yogerageza gukuraho ibimenyetso vyiwe... Rero turakeneye gukura hanze ivyo bipande.



![Image](assets/fr/050.webp)



Aha, dufise igenzura ry’ibikorwa bishobora guhungabana, gucunga konti, ibikorwa vyategekanijwe n’uguhuza NTP.vyerekanwa ko urugero ruri hasi ku gice c’ibendera n’ikimenyetso: ivyo biratahurwa, iyo ugaragaje verisiyo ya sisitemu, bitanga ikimenyetso ku muntu ashobora gutera. Iyi ni yo nzira y'imbere.



Vyoba vyiza hakoreshejwe **auditd** kugira ngo hagire ama logs mu gihe habayeho isesengura rya **forensic**. **NTP** nayo irasuzumwa, kuko kugira ngo urondere neza amakuru, ni vyiza kugira ubuhinga ku gihe, ivyo bikaba vyorosha ugushaka.



![Image](assets/fr/036.webp)



Lynis aca araba Elements y’ubuhinga bwa none, ubuhinga bwo gukoresha ibintu mu buryo bw’impwemu, ibikoresho n’imirongo y’umutekano. Hari ibice bimwebimwe biri ubusa kubera ko ata n’imwe ihuye n’imashini isesengurwa. Ariko rero, turashobora kubona ko mfise ivyemezo bibiri vya SSL vyaheze kandi nta **SELinux** nakoresheje.



![Image](assets/fr/027.webp)



Aha na ho nyene hariho aho twokwongereza: nta gikoresho co kurwanya virusi canke kurwanya porogarama mbi, kandi turafise ivyiyumviro ku vyerekeye uruhusha rwa dosiye.



![Image](assets/fr/028.webp)



Inyuma y'aho, Lynis yibanda ku gukomeza imiterere y'umurongo wa Linux (harimwo amategeko y'uruganda rwa IPv4), hamwe n'ugucungera ububiko bw'imashini ya Linux "Ingoro".



![Image](assets/fr/035.webp)



Twarashitse ku mpera y’isesengura... Iyi ngingo ya nyuma yerekana ko tworonka vyose tworonka mu kugira ClamAV kuri iyi mashini.



![Image](assets/fr/030.webp)



## IV. Impanuro



Inyuma y’igenzura, ni igihe co gusoma no gusuzuma ivyifuzo. Aho niho turonkera impanuro n’insobanuro z’ikigeragezo cose cakozwe na Lynis.



Fata nk’akarorero impanuro za SSH. **Ku ciyumviro cose, uzosangamwo parametere nziza n'uruja n'uruza ruzosigura ingingo y'umutekano ** Ni wewe uzofata ingingo, bivanye n'aho ukoresha n'ingene ukoresha.



Reka turabe ingero nkeyi z'impanuro zisubiramwo ingingo zashizwe ahabona mu gihe cose c'igenzura...



### A. Ingero z'impanuro





- Nk'uko twabibonye mbere, NTP irahambaye ku bitabo vy'igihe:



![Image](assets/fr/043.webp)





- Lynis kandi asaba gushiramwo **apt-listbugs** kugira ngo ubone amakuru ku bibazo bikomeye mu gihe co gushiramwo **apt.**



![Image](assets/fr/041.webp)





- Ico gikoresho kidusaba gushiramwo **needrestart kugira ngo dushobore** kugira ngo turabe ibikorwa bikoresha verisiyo ya kera y'ububiko bw'ibitabu kandi bikeneye gusubira gutangura.



![Image](assets/fr/054.webp)





- Iki ciyumviro kivuga ko woshiramwo **fail2ban** kugira ngo uhagarike abashitsi bananirwa kwemeza (cane cane brute force).



![Image](assets/fr/044.webp)





- Kugira ngo dukomeze ibikorwa vya sisitemu, aradusaba gukoresha itegeko ry’ubururu ku gikorwa cose kiri ku mashine yacu.



![Image](assets/fr/056.webp)





- Asaba gushinga amatariki y’iherezo ry’amajambo banga yose ya konti yose akinzwe.



![Image](assets/fr/031.webp)





- Iki ciyumviro kirasaba gushinga agaciro gatoyi n'agaciro kanini k'imyaka y'ijambobanga. Mu bindi, ivyo bizotuma amajambo y’ibanga ahindurwa ubudasiba.



![Image](assets/fr/042.webp)





- Turahimiriza gukoresha imigabane itandukanye, kugira ngo ugabanye ingaruka z'ingorane z'umwanya kuri disiki ku migabane imwe.



![Image](assets/fr/047.webp)





- Iyi mpanuro isaba guhagarika ububiko bwa USB n'umurongo w'umuriro kugira ngo amakuru ntasohoke



![Image](assets/fr/033.webp)





- Kugira ngo ushitse kuri iyo mpanuro, ushobora gushiramwo gusa no gutunganya **ugusubiramwo-utagira uwubicungera**, nk'akarorero.



![Image](assets/fr/053.webp)



### B. Gushiramwo amapaki y'impanuro



Kugira ngo dutere imbere mu bijanye n’imiterere ya system, tugiye gushiramwo amapaki amwe amwe ku mashini: amwe amwe asabwa na Lynis, ayandi jewe ubwanje ndasaba.



Uzogira urufatiro rwiza wokorerako, igihe cose uzomara umwanya mutoyi ubitunganya. Kugira ngo ubikore, raba urubuga rwa IT-Connect, ibindi biganiro biri ku rubuga n’inyandiko z’ibikoresho.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Amakuru amwe amwe yerekeye amapaki yashizweho:





- Clamav** ni umuti urwanya umugera.
- unattend-upgrades** izogufasha gucunga ivyahinduwe ubwawe mbere no gusubira gufungura imashini canke gusukura ubwawe amapaki ya kera, birashobora guhindurwa bimwe bishitse.
- rkhunter** ni ikintu kirwanya imizi gicapura sisitemu ya dosiye yawe.
- Fail2ban** izoshingira ku madosiye yawe y'inyandiko bivanye n'ivyo uyiha ngo isome kandi izokorana na **iptables**, nk'akarorero kubuza ama IP addresses agerageza "brute force" server yawe muri SSH.



### C. Impanuro ku bijanye na SSH



Reka turabe impanuro za SSH. Biri aha hepfo. Ntuhagarike umutima, tuzoca tubasigurira ingene wokwongerera ubushobozi iyo configuration.



![Image](assets/fr/034.webp)



Reka twihweze neza **SSH** yanje y'ubu muri:**/n'ibindi/ssh/sshd_config**



![Image](assets/fr/018.webp)



Ivyo bikoresho bivugwa aha hepfo birashobora gutunganirizwa neza, ariko bikaguha urufatiro rwiza. *Mumenye ko nakuyeho ibivugwa vyinshi kugira ngo bishobore gusomwa neza*.



Tuzo:





- Guhindura icuma co guhuza SSH (wibagire 22)
- Yongera urugero rw'amajambo y'ibitabo, kuva kuri **INFO gushika kuri VERBOSE**
- Gushinga **Igihe c'Ubuntu bwo Kwinjira** ku **Iminota 2**



Iyo ata makuru y’ihuriro yinjijwe mu minota ibiri, ihuriro riracika.





- Gukoresha **uburyo bukomeye**



Igaragaza nimba "sshd" ikwiye gusuzuma uburyo na nyen'amadosiye y'ukoresha hamwe n'ububiko bw'inzu bw'ukoresha imbere yo kwemeza ihuriro. Ivyo ni vyiza cane, kuko rimwe na rimwe abashasha basiga mu mpanuka ububiko bwabo canke amadosiye yabo ashobora gushikirwa na bose. Ivyashizweho ni "egome".





- Gushinga **Ibikorwa vy'uburenganzira** kuri 3



Ivyo bigereranya umubare w'ibigeragezo vy'ukwemeza vyananiwe imbere y'uko ubutumwa bufunga.





- Gushinga **Ibihe vyinshi** kuri 2



Ivyo bigereranya umubare munini w’ibiganiro bibera icarimwe.





- Gushoboza kwemeza urufunguzo rwa bose



```
PubkeyAuthentication yes
```





- Gumana ijambobanga ry'ukwemeza:



```
PasswordAuthentication yes
```



Kubuza amajambobanga y'ubusa n'ukwemeza **Kerberos**, hamwe n'ukwemeza **umuzi utaziguye**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Raba neza ko ufise "**PermitRootLogin no", nimba ingana na "egome", ni "ikibi gikomeye"**.





- Kubuza guhindura inzira y'ihuriro rya TCP



```
AllowTcpForwarding no
```



Igaragaza nimba TCP ihindura inzira yemerewe, na "egome" nk'ivyashizweho mburabuzi. Iyumvire: guhagarika TCP redirects ntivyongera umutekano iyo abakoresha bafise uburenganzira bwo gukoresha shell, kuko bashobora gushinga ibikoresho vyabo vyo guhindura.





- Kubuza X11 guhindura inzira



```
X11Forwarding no
```



Igaragaza nimba X11 redirects zemewe, na "oya" nk'ivyashizweho mburabuzi. Iyumvire: naho X11 redirects yoba yazimye, ivyo ntivyongera umutekano, kuko abakoresha bashobora gushinga redirects zabo. X11 guhindura inzira irazima iyo **UseLogin** yatowe.





- Gushinga igihe co guhanahana amakuru hagati y'umukiriya na sshd



```
ClientAliveInterval  300
```



Isobanura igihe co guhera mu masegonda, inyuma y'aho, iyo ata makuru yakiriwe n'umukiriya, serivisi ya sshd yohereza ubutumwa busaba inyishu ku mukiriya. Ku mburabuzi, iyi nzira iteguwe kuri "0", bisobanura ko ubu butumwa butarungikwa ku mukiriya. Verisiyo ya 2 yonyene y'umurongo wa SSH ni yo ishigikira iyo nzira.



```
ClientAliveCountMax 0
```



Dushingiye ku [inyandiko (*urupapuro rw'umuntu*) rwa sshd](https://www. n'igihe ubutumwa bwo guhagarika bwarungitswe, **sshd** iraca umukiriya maze igahagarika ikiganiro. Ni ngombwa kumenya ko ubutumwa bwo guhagarika butandukanye cane n'uburyo bwo guhagarika **KeepAlive** (hasi Ubutumwa bwo guhagarika ubufatanye bwoherezwa biciye mu nzira y'ububisha, kandi rero ntibushobora gukoreshwa na TCP). **KeepAlive** ni ubuhendanyi uburyo bwo gufata ihuriro burakenewe iyo umukiriya canke umukozi akeneye kumenya nimba ihuriro ritagira ico rikora."





- Buza amakuru gutangazwa mu guhagarika **motd, ibendera, lastlog**



```
PrintMotd no
```



Igaragaza nimba sshd ikwiye kwerekana ibiri muri dosiye "/etc/motd" igihe umukoresha yinjira mu buryo bwo gukorana. Ku sisitemu zimwe zimwe, ibi birimwo bishobora kandi kugaragazwa n'igikoko, biciye ku /etc/profile canke dosiye isa. Agaciro mburabuzi ni "egome".



```
Banner none
```



Birabereye kumenya yuko mu bihugu bimwebimwe, kohereza ubutumwa imbere y’uko umuntu yemezwa bishobora kuba ari ikintu gikenewe kugira ngo umuntu akingirwe n’amategeko. Ibiri muri dosiye yatanzwe birungikirwa uwukoresha ari kure imbere y'uko uruhusha rwo guhuza rutangwa. Iyi nzira ikeneye gutunganirizwa, kuko nta butumwa buzogaragara.



Mu mashusho, ivyo bitanga:



![Image](assets/fr/019.webp)



### D. Amanota y'igenzura



Ubwa nyuma, ntitwibagire gusuzuma **amanota y'igenzura rya Lynis**! Turabona ko **amanota yanje yo gukomera ari 63** kandi ko dosiye ya raporo ishobora kurabwa muri "**/var/log/lynis-raporo.dat**". Hariho kandi dosiye "**/var/igitabo/lynis.igitabo**".



**Mu yandi majambo, uko amanota aba menshi niko bigenda neza!** Ukeneye rero gukora ku ntunganyo yawe kugira ngo ushikire amanota menshi ashoboka, mu gihe ureka imashini yawe n’ibikorwa vyawe bikora neza (bisobanura gukora ivyigwa vy’imikorere).



![Image](assets/fr/046.webp)



Reka turabe ivyo vyavuyemwo kuri server yanje ya kabiri, aho namaze umwanya mutoyi nkora! Ni ibisanzwe rero ko amanota ari menshi (**76**).



![Image](assets/fr/045.webp)



## V. Lynis gutegura ivy'ubuhinga



**Lynis** nayo itanga uburenganzira bwo gukora amasheki yayo biciye ku gikorwa categekanijwe. Hariho mu vy'ukuri **"--cronjob "** uburyo, buzokoresha ibigeragezo vyose vya Lynis ataco bikeneye kwemeza canke igikorwa c'umukoresha. Ushobora rero gukora script izokoresha **Lynis** maze ugashira igisohoka muri dosiye ifise ikidodo c'igihe iriko izina rya server ivugwa. Aha niho dosiye y'ubwo bwoko ushobora gushiramwo muri dosiye */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



**"AUDITOR_NAME "** umuhinduzi ni umuhinduzi gusa tuzoshiraho mu **"--umugenzuzi "** amahitamwo ya **Lynis** kugira ngo iri zina rigaragare muri raporo:



![Image](assets/fr/059.webp)



Turagiye kandi gukora ibihinduka bikeyi bizodufasha kwitunganya neza, nk’izina ry’umushitsi n’itariki yo kwita raporo no kuyishirako ikidodo c’igihe, n’inzira ija muri dosiye dushaka gushiramwo raporo zacu.



## VI. Iciyumviro



Lynis ni igikoresho gikora cane kizogufasha kuzigama umwanya no gukora neza igihe ushaka kumenya vyinshi ku bijanye n’ingene server ya Linux imeze, cane cane mu bijanye n’umutekano. Ariko rero, ntimwibagire ko uguhindura kwose kugomba kugeragezwa imbere y’uko gukoreshwa mu guhingura, muzirikana uko mukoresha n’aho biherereye.



Kumbure ntuzokoresha iyo ntunganyo nyene kuri VPS yerekanwa kuri Net, aho ukeneye gusa guhuza SSH imwe (kuko ari wewe wenyene uhuza), bitandukanye n'i **bastion** canke **scheduler** izokenera gukubita **SSH.** guhuza



Iyo umaze kuronka configuration igubereye mu bijanye no gukomera, ni vyiza ko ukoresha igikoresho co kwikoresha kugira ngo ntusubire gukora ibikorwa n’amaboko, kuko ivyo vyogutwara umwanya kandi bishobora gutuma haba amakosa. Nk'akarorero, ushobora gukoresha **: Igipupe, Umutetsi, Ansible, n'ibindi...**



Ntimwibagire kuvugana n’imigwi yanyu imbere y’uko mushira mu ngiro: mukeneye kubamenyesha igituma muriko muragira ayo mahinduka, ntimubabwire gusa ko muriko murayagira. Mu mpera, intumbero izoba iyo gutanga ingeso nziza, kandi ivyo bizokwongereza amahirwe yawe yo kuroranirwa.



Ubwa nyuma, urashobora kandi kugereranya **Lynis** n’ibindi bikoresho, muri vyo harimwo vyinshi. Niba ushaka kuja mu burongozi buhurikiye hamwe mu gihe uguma ufise inkomoko yuguruye, ndagusavye igikoresho [Wazuh] (https://wazuh.com/).



**Iyi nyigisho iraheze, mwinovore na Lynis!**