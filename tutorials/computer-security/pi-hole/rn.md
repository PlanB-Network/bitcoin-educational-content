---
name: Pi-Hole
description: Uwubuza kwamamaza ku rubuga rwawe rwose
---
![cover](assets/cover.webp)



___



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Florian Duchemin vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Birashoboka ko hari ivyo bahinduye mu canditswe c’intango.*



___



## I. Ugushikiriza



Twese twabikoze igihe nyene dutangura gukoresha umucukumbuzi dukunda cane: gushiramwo **adblocker** (umucukumbuzi w’amatangazo). Ariko rero, iyo ukoresheje umucukumbuzi wa TV canke igikoresho ca Android, n’ibindi... Biragoye gato kuronka ikintu gikora. Kandi nimba hari ibikoresho birenze kimwe mu nzu, heza, ubwirizwa gusubiramwo igikorwa ku mucukumbuzi wese!



Muri iyi nyigisho, tugiye gutorera umuti ikibazo coroshe**: gutanga ikintu co gukingira amatangazo ku mashini zose ziri ku rubuga rwacu maze tuyicunge hagati.**



Kugira ivyo tubishikeko, tuzokoresha igikoresho cakozwe ku bw’iyo ntumbero: **Pi-Hole**



Pi-Hole ni ikinogo ca DNS. Izokoresha ibisabwa vya DNS vyakozwe n’ibikoresho vyawe kugira ngo yemeze canke yanke uruja n’uruza, gutyo ikurinde amaderesi n’ibibanza bizwi ko bitanga amatangazo, porogarama mbi n’ibindi.



DNS ni Sisitemu y'Izina ry'Ikibanza. None izina ry’itongo ni iki? Erega, "it-connect.fr" ni akarorero kamwe gusa. Izina ry'indangarubuga ni ikimenyetso kidasanzwe c'umutungo umwe canke myinshi, akenshi igenzurwa n'ikigo kimwe.



Izina ry'imashini hamwe n'izina ry'indangarubuga ryitwa FQDN ku *Izina ry'indangarubuga ryuzuye*. Bigufasha gushika ku mashini yihariye mu "kuyihamagara" gusa. Nk'akarorero, iyo wanditse "www.trucmachin.com", uba uriko uhamagara imashini "www", iri mu rwego rwa "trucmachin.com".



Keretse ko mudasobwa zacu zitatahura ururimi rw’umuntu, ivyo zitahura vyose ni binaire, rero zikeneye IP Address, ni ukuvuga inomero ya telefone, kugira zishike ku rubuga.



Rero igihe cose winjije izina ry’urubuga mu mucukumbuzi wawe, canke ukanda kuri link, mudasobwa yawe irabanza gusaba server ya DNS IP Address ihuye n’iryo zina.



**Pi-Hole izoheza igenzure ivyo bisabwa (hari amajana buri musi!) maze ihite ibuza ivyo bizwi ko bikira amatangazo canke mbere amadosiye y’ububisha**



## II. Gushiramwo umwobo wa Pi



Kubera izina nka Pi-Hole, woshobora kwiyumvira neza ko ukeneye Raspberry-Pi... Ariko ivyo si ukuri rwose. **Pi-Hole ishobora gushirwa kuri mudasobwa yose ya Linux (Debian, Fedora, Rocky, Ubuntu, n'ibindi)**



Ku rundi ruhande, urakeneye kuzirikana ko **iki gikoresho kizobwirizwa gukora amasaha 24 ku musi kubera imvo yoroshe: nta DNS, nta Internet!** Raspberry rero ni iciyumviro ciza, kuko hafi nta nguvu ikoresha.



Kugira ngo ushiremwo, ushobora gusa kwifatanya n'imashini yawe ya Linux biciye kuri SSH hanyuma winjize itegeko rikurikira nka "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Iciyumviro**: mu bihe bisanzwe, si vyiza "gutera" script utabanje kumenya ico ikora. Niba utazi neza, genda kuri iyo paji ifise umucukumbuzi canke ushireko ibirimwo nk’idosiye.
>


> **Iciyumviro: kuri verisiyo ntoya za Debian 11, Curl ntishirwamwo, rero ukeneye kuyishiramwo n'amaboko ukoresheje ** `apt-get install curl` **itegeko imbere yo kwandika itegeko riri hejuru.**

Igihe inyandiko imaze gukora, urutonde rw'ibigeragezo ruzokorwa, kandi ugushiraho ubwakwo kuzokwitwararika:



![Image](assets/fr/019.webp)



Gushiramwo umwobo wa Pi



Igihe installation irangiye, uzoja kuri iyi skrini:



![Image](assets/fr/020.webp)



Igikoresho co gutangura Pi-Hole



> **Iciyumviro**: nimba uriko urakoresha DHCP ku mashine yawe, uzoronka ubutumwa bwo kugabisha kuri ivyo. Ego ni ko, kugira ngo ukoreshe neza, turagusavye cane guha IP idahinduka ku mashini yawe.

Ukurikije iyi screen, uzoronka ubutumwa buke bw’amakuru, hanyuma uzojanwa ku muhinga w’ivy’imiterere, azobanza kukubaza server ya DNS Pi-Hole izorungikira ibisabwa. Ku ruhande rwanje, nahisemwo Quad9, ifise itegeko ry’ubuzima bwite bw’abakoresha.



![Image](assets/fr/021.webp)



Ihitamwo rya DNS - Pi-Umwobo



> **Iciyumviro: nimba uri muri sosiyete, amahirwe ni uko server yawe ya DNS ubu ari umugenzuzi w'itongo rya Active Directory. Ariko ntuhagarike umutima, ushobora mu nyuma gutanga umurongo w'ivyangombwa ku rwego rw'itongo uhisemwo. Mu bisanzwe, uzoshobora guhindura igisabwa cose kijanye n'indangarubuga yawe kuri server yawe ya DNS.**

Uzobona ko amahitamwo amwe amwe arimwo amahitamwo ya DNSSEC. Mu bisanzwe, umurongo wa DNS nta mutekano ufise (ntiwakozwe n’ivyo mu muzirikanyi ico gihe). DNSSEC itorera umuti ico kibazo mu kwongerako Layer y’umutekano biciye mu gupfuka no gusinya ku bimenyetso, nk’uko vyasiguwe mu kiganiro gihuye: [Umutekano wa DNS](https://www.it-connect.fr/security-dns-doh-quest-ce-le-dns-over-https/)



Igikoresho cose co guhagarika amatangazo cizigira urutonde rumwe canke nyinshi kugira ngo gikore akazi kaco. Pi-Hole izana n’urutonde rumwe nk’urugero, rero uruhitemwo wongereko izindi mu nyuma.



![Image](assets/fr/022.webp)



Ikibazo kije ku rubuga rwa Interface, gushiramwo ni ubusabe, kuko igikoresho gifise umurongo waco w’amabwirizwa yo gucunga no kubona. Ariko iyi Interface iraryoshe cane kandi ikozwe neza, rero ndabagira inama yo kuyishiramwo igihe kimwe:



![Image](assets/fr/023.webp)



Niba uriko urashiraho Pi-Hole ku mashini isanzwe ifise server y'urubuga, urashobora kwishura "oya" ku kibazo gikurikira. Ariko rero, urabona ko PHP n’ibice vyinshi bisabwa kugira ngo ivyo bikore. Ahandiho, **lighttpd izoshirwamwo n'ibice vyose bikenewe**.



![Image](assets/fr/024.webp)



Uca ubazwa nimba wipfuza kwandika ibisabwa na DNS. **Niba ushaka kubika amateka, shira ibi kuri yego; ahandi ho, shiraho ibi kuri oya, ariko uzotakaza bimwe mu bikorwa** (raba igicapo gikurikira).



![Image](assets/fr/025.webp)



Ku rubuga rwayo rwa Interface, Pi-Hole ikoresha igikorwa cayo bwite citwa FTLDNS, gitanga API kandi kigatanga imibare iva ku bisabwa vya DNS. Iyi nzira ishobora kubamwo uburyo bwa "ubuzima bwite" bupfuka ivyicaro bisabwa, abakiriya bari inyuma y'ivyo bisabwa, canke vyose. Handy nimba ushaka gukora monitoring utahungabanya ubuzima bwite bw’abantu, canke gusa nimba ushaka kwubahiriza amabwirizwa yerekeye iyo gukoresha ku rubuga rwa bose.



![Image](assets/fr/026.webp)



Guhitamwo ubuzima bwite



Iki kibazo ca nyuma kimaze kwishurwa, inyandiko izokora ivyo itegekanijwe: gukuraho ububiko bwa GitHub no gutunganya Pi-Hole. Inyuma y'ugushiraho, incamake izogaragara n'amakuru ahambaye:



![Image](assets/fr/027.webp)



Incamake y'ugushiraho



Niwibuke ijambobanga ry’urubuga rwa Interface n’amakuru y’urubuga. Ubu ni igihe co gutunganya igikorwa ca DHCP aho turi ubu.



## III. Itunganywa rya DHCP



Kugira ngo Pi-Hole ikore, ikeneye "gutorera umuti" ibisabwa vya DNS biva ku bakiriya, rero bategerezwa kumenya ko ari we bobirungikira. Hari uburyo bwinshi bwo kubikora:





- Guhindura imiterere ya DNS muri server yawe ya DHCP (nk'akarorero Agasanduku kawe)
- Zima iyi server maze ukoreshe iyatanzwe na Pi-Hole
- Guhindura n'amaboko igikoresho cose kugira ngo ukoreshe Pi-Hole nka DNS



Jewe ubwanje ndahitamwo umuti wa mbere. Amahirwe ni **ufise server ya DHCP aho uri** (kenshi na kenshi ni box yawe). Rero ntaco bimaze kwibabaza.



Nk’uko hariho ubushobozi bwinshi, hagati y’amasandugu y’abakozi batandukanye (ivyo ntazi kuri vyose) n’abafise router yabo, sinzotanga screenshot y’ivyo bihinduka. Uko biri kwose, uzokenera kuja ku mirongo ya DHCP maze uhindure umurongo wa "DNS" kugira ngo ushiremwo IP Address ya Pi-Hole yawe.



Ivyo bimaze gukorwa, nimba hari ibikoresho vyari vyarafunguwe mbere, bizoba vyagumye bifise amategeko ya kera, rero uzokenera gusubira gutangura igisabwa co guhindura.



Ku bibanza vy'akazi vya Windows, n'itegeko:



```
ipconfig /renew
```



Ku kibanza c'akazi ca Linux:



```
dhclient
```



Ku bindi bikoresho vyose, bitegerezwa kuzimwa no gusubira gucana.



Rero bakwiye kuronka amaparametere akwiye, kugira ngo basuzume:



```
ipconfig /all
```



Mu kibanza ca DNS, ushobora kugira Address ya Pi-Hole yawe, mu gihe canje 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Gukoresha urubuga rwa Interface Pi-Hole



Kugira ngo uburongozi bube bworoshe, **Pi-Hole** iraronka inyungu ku rubuga rwa Interface Interface rwateguwe neza. Ikoreshwa neza kandi irashikira, iragufasha:





- Raba umubare w'ibisabwa, ibisabwa vyabujijwe, n'ibindi mu gihe nyaco.
- Gucungera urutonde rwawe rwera n'urw'umwirabura
- Kwongera ivyinjijwe bitahinduka, amazina y'ibanga, n'ibindi.
- Kwongerako urutonde
- N’ibindi bikorwa vyinshi!



Ku ruhande rwanje, ngiye kwongerako urutonde rw’ababuza. Nk’uko twabibonye haruguru, urutonde rumwe gusa ni rwo rwashizweho igihe kimwe na Soft. Hariho urutonde rwinshi rw'imbuga z'amatangazo, ariko ni vyiza guhitamwo n'imiburiburi rumwe rwihariye ku gihugu ubamwo.Rumwe mu rutonde ruzwi cane ni **EasyList**, kandi rumwe muri zo ni rwihariye ku Bufaransa: [Urutonde-Rworoshe-UrutondeFR](https://raw.githubusercontent.com/urupfubybandaid/piholeparser/umukuru/Urutonde-Rwo-Rwiyandikisha/Urutonde-Rwirabura Rwasesanguwe/Urutonde-Rworoshe-FR.txt)



Kugira ngo wongereko, banza wihuze n'umuyobozi wa Interface: **http://<ip_du_PiHole>/umuyobozi**



Ijambobanga ry'umuyobozi ryaramaze gusohoka (raba ifoto y'iherezo ry'ugushiraho), rero ico ukeneye gukora n'ukurishiramwo kugira ngo ushikire Interface:



![Image](assets/fr/030.webp)



Interface ivuye mu mwobo wa Pi



Turashobora kubona nk’akarorero ko hari abakiriya babiri bahuye na Pi-Hole, ko yakoze ibisabwa 442 kandi ko 8 muri ivyo vyabujijwe. Ivyo bishushanyo birashobora kuba isoko ryiza ry’amakuru cane cane mu bijanye n’umwuga.



Wongereko urutonde rwacu, genda kuri "**Uburongozi bw'Itsinda**" na "**Urutonde rw'Ivyiyumviro**":



![Image](assets/fr/031.webp)



Turashobora kubona urutonde rwacu rwa mbere "**StevenBlack**", kugira ngo twongereko iryacu, ukope link naguhaye haruguru ukayishira mu kibanza "**Address**", ku bijanye n'insobanuro, mpitamwo gushiramwo izina ry'urutonde:



![Image](assets/fr/032.webp)



Kwongera urutonde muri Pi-Hole



Igisigaye ni ugukanda kuri "**Add**" kugira ngo uyishiremwo. Kugira ngo tuyikoreshe, dukeneye gutera intambwe y'inyongera yo "kugabisha" Pi-Hole ngo yifate kuri uru rutonde. Kugira ngo ubikore:





- Ukoreshe umurongo w'amabwirizwa yubatswemwo
- Canke urubuga rwa Interface



Jewe ubwanje nahisemwo iya kabiri, kuko iyo waravye neza, uruja n'uruza rw'inyandiko ya PHP ikora ivy'uguhindura ruri kuri page turiko (ijambo "online"). Rero ivyo ubwirizwa gukora n'ukuyikandako, bizogutwara kuri paji ifise uburyo bumwe gusa:



![Image](assets/fr/033.webp)



Paje izokwerekana igisubizo c'inyandiko iyo imaze kurangira, bisobanura ko urutonde rwafashwe mu muzirikanyi (kiretse ubutumwa bw'ikosa bugaragajwe, birashoboka).



Nk’uko vyamenyeshejwe mu ntango y’iyi nyigisho, Pi-Hole iragufasha kandi **guhagarika ama domains azwi ko akwiragiza malware. Kugira ngo ukomeze iki kintu, ndagusavye kandi wongereko urutonde rw’indangarubuga ruhora ruvugururwa rutangazwa na Abuse.ch**, ruzokomeza cane umutekano w’urubuga rwawe, ruboneka kuri [iyi Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Ushobora, vy'ukuri, kwongerako urutonde urwo ari rwo rwose wibaza ko rukenewe, canke gucunga urutonde rwawe rw'umwirabura n'amaboko biciye ku rutonde rw'umwirabura.



## V. Ibigeragezo vya Pi-Hole



None ko vyose biri mu kibanza, ico ubwirizwa gukora n’ukugerageza umuti kugira ngo umenye neza ko ukora neza.



Nk’akarorero, nzogerageza gushika ku rubuga *http://admin.gentbcn.org/* ruri ku rutonde rwa Abuse.ch kuko ruzwi ko rwakira porogarama mbi:



![Image](assets/fr/034.webp)



Biragaragara ko hari aho nabujijwe. Kugira ngo tumenye neza ko ari Pi-Hole yakoze akazi, turashobora gusuzuma igitabo c'ibibazo mu rubuga rwa Interface "Igitabo c'ibibazo" kugira ngo turabe ko ari igice kivuye mu rutonde:



![Image](assets/fr/035.webp)



## VI. Iciyumviro



Muri iyi nyigisho, twakweretse ingene woshiraho server ya DNS idakuraho gusa amatangazo menshi kugira ngo ushobore gusura, ariko kandi yongerako **Layer y’umutekano mu kubuza ivy’ubusuma n’ivy’ubusuma**.



Vyose ni ubuntu kandi birahenda iyo bishizwe kuri Raspberry-Pi (mu bijanye n’ugukoresha amashanyarazi).