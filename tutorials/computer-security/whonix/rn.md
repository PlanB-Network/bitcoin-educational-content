---
name: Whonix
description: Zigama ubuzima bwite bwawe n’ibanga ryawe.
---

![cover](assets/cover.webp)



**Whonix** ni umurongo wa Linux ushingiye kuri **Debian**, wagenewe gutanga ibidukikije bihuza **umutekano**, **ukutamenyekana** na **ubuzima bwite**. Biroroshe kwiga, kandi bihuye n’ibikoresho bitandukanye (amamashini y’ivy’impwemu, Qubes OS, uburyo bwo kubaho), birimwo n’inzira y’uruja n’uruza rw’urubuga biciye ku **Tor**, **uruhome rw’umuriro rubiri** (uruhome rw’umuriro rumwe ku Muryango n’urundi ku Kibanza c’Akazi), **uburinzi bushitse ku bijanye n’ugusohoka kwa IP/DNS** serly harimwo n’ubuhinga bwawe bwo gukingira IP/DNS** n’ibikoresho vyawe. Ibirenze gusa ubuhinga butazwi, **Whonix** ni ikibanza c’iterambere gitekanye.



## Ni kuki uhisemwo Whonix?





- Ku buntu**: Cokimwe n’ibindi bikoresho vyinshi vya Linux, Whonix ni ubuhinga bufunguye bufise uruhusha rwo gukora ku buntu. Iteguwe mu buryo bufunguye, ifise umuryango ukora kandi uboneye.
- Ubuzima bwite, umutekano n’ukutamenyekana**: Intumbero ihambaye ya Whonix ni ugutanga ikibanza gifise umutekano mwinshi cane, aho amakuru yawe yose akinzwe kandi n’ivy’itumanaho ryawe bikaba bishizwe mu nzira y’ubuhinga bwa Tor.
- Biroroshe gukoresha**: Whonix itanga igishushanyo Interface gisanzwe, gisanzwe, kibereye mbere n’abakoresha bashasha. Ntibikenewe kuba umuhinga kugira ngo wungukire ku kurindwa guteye imbere.
- Ibidukikije vyiza vyo guteza imbere mu mutekano**: Whonix iragufasha gutegura, kugerageza, gusuzuma canke gukoresha porogarama utarigeze uhishura IP yawe nyayo Address canke ngo ugaragaze ingeso zawe zo gusura canke guhanahana amakuru ku rubuga.
- Ivyigwa bikoreshwa rimwe gusa n’uburyo bwo gukora**: Whonix ishobora gutangura mu buryo bw’ubuzima canke biciye ku mashini zikoreshwa rimwe (nk’akarorero biciye ku **Qubes OS**), bikaba bishoboza ibikorwa bihambaye gukorwa ata n’ibimenyetso bihoraho bisigaye iyo igihe kirangiye.
- Gushiramwo biroroshe cane**: Amashusho yiteguye gukoreshwa aratangwa kugira ngo ashirwemwo vyihuse mu mashini zitaboneka (VirtualBox, KVM, Qubes). Ubuhinga burandikwa kandi bugahora buvugururwa.



## Gushiramwo no gutunganya



Imbere yo gutera imbere ku gushiramwo Whonix, ni ngombwa kumenya ko iyo nzira **itaraboneka ku mugaragaro** nk'uburyo nyamukuru bushobora gushirwaho ataco buvuze kuri disiki ya Hard (mu buryo bw'ivyuma bitagira ikintu). Mu yandi majambo, **ntushobora gushiramwo Whonix nk'uburyo bwo gukoresha bwa kera**, nka Ubuntu canke Debian isanzwe.



Ariko rero, hariho insiguro nyinshi, zituma Whonix ikoreshwa **volatile** (Uburyo bubaho, ibiganiro vy’igihe gito) canke **bihoraho** (biciye mu mashini zitaboneka canke mu gushiramwo muri Qubes OS).



Ku bijanye n'ikoreshwa ry'igihe kirekire, ridahinduka, **ugukoresha ubuhinga bwa none ni bwo buryo bwonyene bwemewe**. Ushobora gukoresha Whonix ukoresheje **VirtualBox** (Irembo rya Whonix n'Ikibanza c'Ibikorwa ca Whonix) canke ukayishira muri sisitemu nka **Qubes OS**. Muri iyi nyigisho, tuzokwibanda ku gushiramwo VirtualBox.



### Ibisabwa



Imbere y’uko ushobora gushiramwo Whonix mu buryo bw’ivy’ubuhinga, urabe neza ko imashini yawe ihuye n’ibisabwa vy’ubuhinga bikeyi. Gukoresha ibintu mu buryo bw’ingurukanabumenyi bisaba ibintu bimwebimwe bitari mudasobwa zose zishobora gutanga. Ni ngombwa rero ko processeur yawe ishigikira ubuhinga bwo guhindura ibintu mu buryo bw’impwemu (Intel VT-x canke AMD-V), kandi ko iyo nzira ikoreshwa muri BIOS/UEFI.



Aha niho hari ivyiza vyerekeye ubumenyi bubereye kandi bushikamye na Whonix:





- Ubuhinga bwo kwibuka (RAM)**: ni **8 GB** nivyo bikenewe cane. Uko ugira RAM nyinshi niko ushobora gutanga amafaranga menshi ku mashini zikora (Gateway na Workstation), bigatuma ukora neza.
- Imyanya iriho kuri disiki**: usabwe kwemera nibura 30 GB y'umwanya kuri disiki y'ubuntu**. Ivyo birimwo umwanya usabwa ku mashini zibiri zisanzwe, amadosiye ya sisitemu n’amakuru yose canke amafoto.
- Processeur**: processeur ifise nibura **4 physique cores** (8 logical threads) ni ngirakamaro, cane cane iyo ushaka gukoresha izindi serivisi canke ibikoresho bihuye.



### Gukuraho Whonix



Whonix iboneka mu mice myinshi, bivanye n’ubwoko bw’ibidukikije ushaka kuyikoreshamwo.Ku bakoresha benshi (Windows, Linux canke MacOs), imice ya VirtualBox ni yo yoroshe gushinga. Ushobora gukura iyo shusho kuri [urubuga rwemewe](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **ntihuye** na MacBooks zikoresha ibikoresho vya Apple Silicon (ubwubatsi bwa ARM).



## Gushiramwo agasanduku k'ukuri



Kugira ngo ukoreshe Whonix, uzokenera **umugenzuzi w'ibintu vyinshi** nka VirtualBox, Qubes canke KVM.



Umaze gukuraho iyo dosiye, uyishiremwo nk’uko wobigira ku yindi porogarama yose. Wemere amahitamwo y’imbere kiretse ufise ibisabwa vyihariye. Mbega warazimiye? Raba uburongozi bwacu bwo gukoresha VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Kuzana Whonix



Igihe VirtualBox imaze gushirwamwo, ushobora kwinjiza amadosiye ya Whonix `.ova` waronse mbere (`Irembo rya Whonix-Xfce.ova` na `Ikibanza c'Ibikorwa-Xfce.ova`).



Ugurure VirtualBox, hanyuma ukande kuri **Dosiye → Igikoresho co kwinjiza**.


Hitamwo dosiye `.ova` ihuye (tangura n'Irembo).



![0_03](assets/fr/03.webp)



Hitamwo aho amadosiye y'imashini y'ukuri ya Whonix azobikwa.



![0_04](assets/fr/04.webp)



Wemere amabwirizwa y'ikoreshwa, hanyuma utangure kwinjiza ibintu hanze maze urindire ko igikorwa kirangira.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Itunganywa rya Whonix



Imbere yo gutangura Whonix, birahambaye ko uhindura **imiterere ya sisitemu** kugira ngo ukore neza:



Hitamwo **Whonix-Ikibanza c'Akazi-Xfce** imashini y'ivy'impwemu, hanyuma ukande kuri **Itunganywa**.



![0_06](assets/fr/07.webp)



Genda kuri **System**, aho RAM igenewe 2048 MB. Turagusavye **wongera ukagera kuri 4096 MB (4 GB)** kugira ngo ushobore gukoresha neza, cane cane iyo ushaka gufungura porogarama nyinshi canke gukora mu bihe birebire. Iryo rembo rishobora kuguma kuri 2048 MB, kiretse iyo ukoresha amahuzu menshi ya Tor mu buryo bumwe.



![0_08](assets/fr/08.webp)



### Gutangura na Whonix



Kugira ngo Whonix ikore neza kandi itekanye, **utegerezwa gukurikiza uru rutonde rwo gutangura**:



Mbere, tangura imashini ya **Whonix-Irembo-Xfce**. Iyi mashini ni yo ishinzwe gutuma amakuru yose agenda biciye ku rubuga rwa **Tor**. Iyo ata gateway ikora, nta n’uruja n’uruza ruzoca muri Tor kandi uzotakaza amazina.



![0_09](assets/fr/09.webp)



Igihe Irembo rizoba ryatanguje neza (uzobona Tor ihuriweko), ushobora gutangura **Whonix-Workstation-Xfce**, izokwifatanya ubwayo biciye ku Rembo.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Kuvugurura sisitemu



Injira muri terminal, shiramwo itegeko rikurikira kugira ngo uhindure urutonde rw'amapaki:



```shell
sudo apt update
```



Hanyuma ukoreshe itegeko rikurikira kugira ngo ushiremwo ivyagezwe biriho:



```shell
sudo apt full-upgrade
```



## Vumbura Whonix



**Whonix** ni ubuhinga bugenewe gutanga **umutekano**, **utamenyekana** n’ibanga** ry’ubuhinga bwa none, ryiza cane mu gukoresha Internet ataco bihungabanya ku bijanye n’akaranga kawe canke amakuru yawe. Kugira ngo ivyo bishoboke, izana n’ibikoresho vyinshi vy’ingirakamaro vya misi yose vyagenewe gukomeza umutekano wawe wo kuri interineti kuva mu ntango.


### Gukomeza XC



**KeePassXC** ni umucungerezi w'ijambobanga rya Whonix. Iragufasha **guhingura, kubika no gucunga** amajambo y'ibanga yawe mu buryo butekanye, utabwirizwa kuyazirikana yose n'amaboko. Amajambo banga abikwa mu **ububiko bw'amakuru bufise amakuru apfutse**, akinzwe n'ijambobanga ry'umukuru.



### Mucukumbuzi wa Tor



**Umucukumbuzi wa Tor** ni umucukumbuzi w'urubuga rwa Whonix. Ishingiye ku rubuga rwa **Tor**, ruhindura uruja n'uruza rwawe biciye mu nzira nyinshi kw'isi yose, bikaba bigoye kumenya IP yawe nyayo Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Umuyagankuba Bitcoin Wallet.



**Electrum** ni Bitcoin Wallet yoroshe kandi yihuta, ibanza gushirwa kuri Whonix kugira ngo ushobore gucungera **amafaranga y’amahera** ata wuzi. Ntiyikurako Blockchain yose ariko ikoresha ama server yo kure kugira ngo ironke amakuru akenewe, ivyo bikaba bituma iyoroshe cane kuruta Wallet yuzuye.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix ni ikintu kirenze ubuhinga bwo gukoresha gusa: ni **ikibanza c’ukuri gitekanye** gigenewe kurinda ubutamenyekana bwawe, ubuzima bwite bwawe n’ibikorwa vyawe vy’agaciro. Kubera ubuhinga bwayo bushingiye kuri Tor, ugucapura kw’ubwenge hagati ya Gateway na Workstation, n’ibikoresho vyashizweho mbere nka Tor Browser, KeePassXC na Electrum, itanga umuti w’urufunguzo ku muntu wese yipfuza **gusoma ata wuzi**, **gukora mu mutekano** canke **gufata con.fi



Kugira ngo ukomeze umutekano wawe kuri sisitemu yawe ya Unix, raba inyigisho yacu ku bijanye no kugenzura imashini yawe: suzuma ko ata myobo y’umutekano iri muri sisitemu yawe y’ibikorwa maze urabe neza ko amakuru yawe atagira ico akora.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af