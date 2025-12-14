---
name: VirtualBox
description: Shiraho VirtualBox kuri Windows 11 maze ureme VM yawe yambere
---
![cover](assets/cover.webp)



___



*Iyi nyigisho ishingiye ku bintu vy’umwimerere vya Florian Burnel vyasohowe kuri [IT-Connect](https://www.it-connect.fr/). Uruhusha [CC KURI-NC 4.0](ku rubuga rwacu/uruhusha/ku-NC/4.0/). Birashoboka ko hari ivyo bahinduye mu canditswe c’intango.*



___




## I. Ugushikiriza



Muri iyi nyigisho, tuzomenya ingene twoshira VirtualBox kuri Windows 11 kugira ngo dukore imashini zitaboneka, haba ku gukoresha Windows 10, Windows 11, Windows Server canke gukoresha Linux (Debian, Ubuntu, Kali Linux, n’ibindi).



Iyi nyigisho y’intango ya VirtualBox izogufasha gutangura n’iyi nzira y’ubuhinga bwa none yateguwe na Oracle, ikaba ari ubuntu. Mu nyuma, izindi nyigisho zizoshirwa kuri Internet kugira ngo zigufashe kumenya neza iyo nkuru.



Ku bijanye no guhindura ikibanza co gukoreramwo mu buryo bw’ukuri, haba ku ntumbero zo kugerageza nk’igice c’umugambi canke mu gihe c’inyigisho zawe z’ubuhinga bwa none, VirtualBox ni umuti mwiza. Ni n’ubundi buryo bwo gusubirira ibindi bisubizo nka Hyper-V, bishizwe muri Windows 10 na Windows 11 (na Windows Server), n’Igikoresho co Gukoreramwo ca VMware (gishobora kwishurwa) / Igikoresho co Gukoreramwo ca VMware (kikoreshwa ku buntu ku muntu ku giti ciwe).



Ivyo nkora: **ikibanza co gukoreramwo ca Windows 11 aho ngiye gushiramwo VirtualBox**, ariko ushobora gushiramwo VirtualBox kuri Windows 10 (canke verisiyo ya kera), no kuri Linux. Ku bijanye n’amamashini y’ivy’impwemu, VirtualBox ifasha ubuhinga bwinshi, harimwo Windows (nk’akarorero, Windows 10, Windows 11, Windows Server 2022, n’ibindi), Linux (Debian, Rocky Linux, Ubuntu, Fedora, n’ibindi), BSD (PfSense) na macOS.



## II. Gukuraho akazu k'ibintu vy'ukuri kuri Windows 11



Kugira ngo ubone VirtualBox kugira ngo uyishire ku mashini ya Windows, hariho Address imwe gusa nziza: [urubuga rwemewe rwa VirtualBox](https://www.virtualbox.org/wiki/Ivyo ushobora gukuraho) mu gice ca "**Ivyo ushobora gukuraho**". Fyonda gusa kuri "Windows hosts" kugira utangure gukuraho iyi executable, ikaba irenga gato 100 MB mu bunini.



![Image](assets/fr/025.webp)



## III. Gushiramwo agasanduku k'ukuri kuri Windows 11



### A. Gushiramwo agasanduku k'ukuri



Gushiramwo **VirtualBox** biragoye, kandi uburyo bwo kubikora ni bumwe ku verisiyo zose za Windows. Tangana n'ugutanguza VirtualBox uherutse gukuraho, hanyuma ukande kuri "**Ibikurikira**".



![Image](assets/fr/026.webp)



Iyi installation irashobora guhindurwa, ariko ndagusavye gushiramwo ibiranga vyose: ni ko biri ku guhitamwo mburabuzi. Mu ishusho iri musi, urashobora kubona Elements zitandukanye, harimwo:





- Ubufasha bwa USB bwa VirtualBox** kugira ngo VirtualBox ishobore gufasha ibikoresho vya USB
- VirtualBox Bridged Network** kugira ngo ushiremwo ubufasha bw'urubuga mu buryo bwa "Ikiraro" (imashini y'urubuga ishobora kwifatanya n'urubuga rwawe rwo mu karere)
- VirtualBox Host-Only Network** kugira ngo ushiremwo ubufasha bw'urubuga mu buryo bwa "Host-Only" (imashini ishobora gusa kuvugana n'umushitsi wawe wa Windows 11 n'izindi mashini zisanzwe muri ubu buryo)



Fyonda "**Ibikurikira**" kugira ngo ukomeze.



![Image](assets/fr/001.webp)



Fyonda kuri "**Ego**", uzirikane ko **urubuga ruzohagarara umwanya muto ku mashine yawe ya Windows 11**, mu gihe VirtualBox ikora ihinduka ry'urubuga kugira ngo ifashe ubwoko butandukanye bw'urubuga, harimwo n'uburyo bwa Bridge.



![Image](assets/fr/002.webp)



Uhejeje kwemeza, gushiramwo bizotangura... Hanyuma hazoboneka itangazo ry'uko "**Ushaka gushiramwo iyi porogarama y'igikoresho?**". Suzuma "**Igihe cose wizere porogaramu iva kuri Oracle Corporation**" hanyuma ukande "**Shiramwo**". VirtualBox mu vy’ukuri ikeneye gushiramwo abashoferi benshi kuri mudasobwa yawe.



![Image](assets/fr/003.webp)



Ivyo gushiramwo ubu birarangiye! Suzuma amahitamwo "**Tangira Oracle VM VirtualBox 6.1.34 inyuma yo gushiramwo**" hanyuma ukande "**Fyonda**" kugira ngo utangure porogaramu.



![Image](assets/fr/004.webp)



### B. Wongereko ivyungura



Naho uri ku rubuga rwemewe rwa VirtualBox (raba urubuga rwa mbere), urashobora gukuraho urubuga rwemewe, rushobora gushikwako munsi y'igice ca "**Urupapuro rwo kwagura rwa VirtualBox 6.1.34 Oracle VM**" ukanda ku rubuga rwa "**Ibikoresho vyose bishigikiwe**". Iyi pack izogufasha kwongerako ibindi bikoresho kuri VirtualBox: si ngombwa ko uyishiramwo, ariko birashobora kuba ngirakamaro! Nk’akarorero, harimwo ugushigikira USB 3.0 muri VMs, ugushigikira webcam n’ugushiramwo amakuru kuri disk.



Ugurure VirtualBox, ukande kuri "**Dosiye**" hanyuma ukande kuri "**Imiterere**" mu rutonde.



![Image](assets/fr/005.webp)



Fyonda kuri "**Extensions**" ibubamfu (1), hanyuma ukande kuri buto ya "**+**" iri iburyo (2) kugira ngo **ushiremwo ivyuma vy'ivyagutse vya VirtualBox** uherutse gukuraho (3).



![Image](assets/fr/006.webp)



Wemeze ukanda kuri buto ya "**Gushiramwo**".



![Image](assets/fr/007.webp)



Fyonda "**OK**": ubu urutonde rw'ivyagutse rwemewe rwashizwe ku nkuru yawe ya VirtualBox!



![Image](assets/fr/008.webp)



Reka tugende ku kurema imashini yacu ya mbere y’ubuhinga bwa none.



## IV. Gukora VirtualBox VM yawe yambere



Kugira ngo ureme imashini nshasha kuri VirtualBox, ushobora gufyonda kuri buto ya "**New**" kugira ngo utangure umuhinga wo kurema VM. Kubera ko ari ubwa mbere mutanguye VirtualBox, ndashaka kubabwira ibindi bisobanuro bikeyi ku bijanye na Interface n’izindi buto.





- Amagenamiterere**: imiterere rusangi ya VirtualBox (ububiko bwa VM, ubuyobozi bwo guhindura, ururimi, imihora ya NAT, ivyungura, n'ibindi)
- Import**: kwinjiza igikoresho c'ukuri mu buryo bwa OVF
- Gusohora**: kwohereza hanze imashini y'ukuri iriho mu buryo bwa OVF kugira ngo ureme igikoresho c'ukuri
- Yongera**: yongera imashini isanzwe ku rutonde rwawe rwa VirtualBox, mu buryo busanzwe bwa VirtualBox (.vbox) canke uburyo bwa XML



Ibubamfu, igice ca "**Ibikoresho**" gitanga uburenganzira bwo gukoresha **ibikorwa biteye imbere, cane cane mu gucunga urubuga rw'ivy'impwemu, ariko no mu gucunga ububiko bwa VM**. Munsi y'inyandiko "**Ibikoresho**", imashini zawe zizokwongerwa mu nyuma.



![Image](assets/fr/009.webp)



### A. Uburyo bwo kurema VM



**Nk’ukwibutsa, VirtualBox ifasha ubuhinga bwinshi bwo gukoresha, harimwo Windows, Linux na BSD.** Muri aka karorero, ngiye gukora imashini y’ubuhinga bwa none ya Windows 11. Hariho ivyicaro vyinshi bikwiye kwuzuzwa:





- Izina**: izina ry'imashini y'ukuri (iri ni ryo zina rizogaragara muri VirtualBox)
- Dosiye y'imashini**: aho wobika imashini y'ukuri, uzi ko dosiye ntoyi iriko izina rya VM izoremwa aha hantu
- Ubwoko**: ubwoko bwa sisitemu ikoresha, bivanye n'ivyo ushaka gushiramwo
- Verisiyo**: verisiyo ya sisitemu wipfuza gushiramwo, muri iki gihe Windows 11, rero "**Idirisha11_64**"



Fyonda "**Ibikurikira**" kugira ngo ukomeze.



![Image](assets/fr/010.webp)



Bivanye n'uburyo bwo gukoresha wahisemwo mu ntambwe ibanza, **VirtualBox itanga impanuro ku bikoresho vyo guha imashini y'ukuri**. Aha, turiko turavuga RAM wipfuza guha VM. Reka twiyumvire ko ari 4 GB, kuko ivyo vy’ukuri ni vyiza kuri Windows 11, ariko nimba ufise uburyo buke, vuga 2 GB aho kubikoresha. **Bandanya**.



**Iciyumviro**: ibikoresho vyagenewe imashini y'ivy'impwemu birashobora guhindurwa mu nyuma.



![Image](assets/fr/011.webp)



Ku bijanye na disiki ya Hard y'ukuri, turiko turatangura kuva ku ntango, rero turakeneye guhitamwo "**Rema disiki ya Hard y'ukuri ubu**" kugira ngo VM ibe n'ahantu ho kubika kugira ngo ishiremwo ubuhinga bwo gukoresha no kubika amakuru. Fyonda kuri "**Rema**".



![Image](assets/fr/012.webp)



VirtualBox ishigikira uburyo butatu butandukanye bw’ama disk Hard, ivyo bikaba ari itandukaniro rikomeye ugereranije n’ibindi bisubizo nka VMware na Hyper-V. Hariho uburyo butatu bwo guhitamwo:





- VDI**, uburyo buzwi bw'agasanduku k'ibintu
- VHD**, ari yo nzira yemewe ya Hyper-V, naho nyene uburyo bushasha bwa VHDX bukoreshwa cane muri iyi misi .
- VMDX** ni uburyo buzwi bwa VMware ku bikoresho vyose vya VMware na VMware ESXi



Kugira ngo ureme imashini y'ukuri izokoreshwa gusa kuri iyi VirtualBox, hitamwo "**VDI**". Ku rundi ruhande, nimba iyo disiki ya Hard y’ukuri izofatanywa n’umushitsi wa Hyper-V mu nyuma, vyoshobora kuba vyiza utanguye n’uburyo bwa VHD kugira ngo ntube ubwirizwa kuyihindura. Fyonda kuri "**Ibikurikira**".



![Image](assets/fr/013.webp)



**Disiki y'ukuri ishobora kuba ihinduka canke idahinduka mu bunini**. Iyo ari dynamic, dosiye iserukira **disiki y'ukuri (aha dosiye .vdi) izokura uko amakuru yandikwa kuri disiki** gushika ishitse ku bunini bwayo burengeye, ariko ntizogabanuka iyo amakuru asubiwemwo. Ku rundi ruhande, iyo ari ingano idahinduka, **umwanya wose wo kubika uca uhabwa ubwo nyene (kandi rero urabikwa)**, ivyo bikaba bituma habaho ibikorwa vyinshi gatoyi, ariko bifata igihe kirekire iyo disiki y’ukuri iremwe ubwa mbere.



Ku bwanje, ku mashini zigerageza zikoresheje VirtualBox, mbona ko uburyo bwa "**Dynamically allocated**" buhagije.



![Image](assets/fr/014.webp)



**Intambwe ikurikira ni ugusobanura ubunini bwa disiki y'ukuri**, uzirikana ko ku buryo busanzwe, iyo disiki izobikwa mu bubiko bwa VM (ivyo bishobora guhindurwa kuri iyi ntambwe). Narerekanye ubunini bwa 64 GB kugira ngo buhure n’ibisabwa na Windows 11, ariko aha na ho, ubunini butoyi bwoshobora guhabwa. Fyonda kuri "**Rema**" kugira ngo ureme VM!



![Image](assets/fr/015.webp)



Muri iki gihe, VM iri mu rutonde rwacu, iratunganijwe, ariko ubuhinga bwo gukoresha ntibushizwemwo. Turakeneye guheza gutunganya VM imbere yo kuyitangura.



### B. Gutanga ishusho ya ISO kuri VirtualBox VM



Kugira ngo dushiremwo Windows 11, canke uwundi murongo uwo ari wo wose, turakeneye amasoko yo gushiramwo. Akenshi, dukoresha ishusho ya disiki mu buryo bwa ISO kugira ngo dushiremwo ubuhinga bwo gukoresha. **Ni ngombwa gushiramwo ishusho ya Windows 11 ISO mu gikoresho ca DVD ca VM yacu.**



Fyonda kuri VM iri mu rutonde rwa VirtualBox (1), hanyuma ukande kuri buto ya "**Itunganywa**" (2), itanga uburenganzira bwo gushika ku ntumbero rusangi y'iyi mashini y'ukuri. Iyi menyu ikoreshwa mu gucunga ibikoresho (nk'akarorero, kwongera RAM, gutunganya CPU, n'ibindi). Fyonda kuri "**Storage**" ibubamfu (3), kuri DVD drive aho handitse "**Empty**" muri ako kanya (4) hanyuma ukande ku kimenyetso gifise ishusho ya DVD (5) na "**Hitamwo dosiye ya disiki**".



![Image](assets/fr/016.webp)



Hitamwo ishusho ya ISO ya sisitemu ushaka gushiramwo, hanyuma ukande OK. Ivyo nivyo mbona:



![Image](assets/fr/017.webp)



Gumana mu gice ca "**Configuration**" ca VM, ndacari n'ibintu bikeyi vyo gusigura.



### C. Ihuriro ry'urubuga rwa VM



Genda ku gice ca "**Reseau**" kiri ibubamfu. Iki gice kigufasha gucunga urubuga rw’imashini y’ivy’impwemu: umubare w’imirongo y’urubuga rw’ivy’impwemu (gushika kuri 4 kuri VM), MAC Address, n’uburyo bwo gushika ku rubuga (NAT, gushika ku kiraro, urubuga rw’imbere, n’ibindi). **Niba ushaka ko imashini yawe y'ivy'impwemu ishobora gukoresha Internet, hitamwo "NAT" canke "Bridge Access "**, ariko ubu buryo bwa kabiri busaba ko server ya DHCP ikora ku rubuga rwawe, canke uzobwirizwa guhindura IP Address n'amaboko.



Iciyumviro: Nzogaruka ku gice c’urubuga mu buryo burambuye mu kiganiro kigenewe.



![Image](assets/fr/018.webp)



### D. Umubare w'ibikoresho vy'ubuhinga bwa none



Cokimwe na mudasobwa y’umubiri, imashini y’umubiri ikeneye RAM, disiki Hard n’umurongozi kugira ngo ikore. Igihe twarema VM, ushobora kuba warabonye ko umupfumu atashizemwo ivy’ugutunganya processeur. Ariko rero, ivyo bishobora gutunganirizwa igihe cose biciye ku nzira ya "**System**", hanyuma "**Processor**", aho ushobora guhitamwo umubare w'ibikoresho vy'ubuhinga.



Iciyumviro: uburyo bwa "**Gushoboza VT-x/AMD-v nested**" burakenewe ku bijanye n'ugukoresha ivy'ukuri.



Mu gihe canje, imashini y'ivy'impwemu ifise ibikoresho 2 vy'impwemu:



![Image](assets/fr/019.webp)



**Ntukekeranye kuraba ibindi bice vyo muri menyu y'imiterere.**



### E. Gutangura mbere no gushiramwo OS



Kugira ngo utangure imashini y'ivy'impwemu, uyihitemwo gusa mu rutonde maze ukande kuri buto ya "**Start**". Idirisha rya kabiri rizofunguka, ritanga inyishu y’ivyo VM ibona.



![Image](assets/fr/020.webp)



Ouch, mbona ikosa ribi cane kandi imashini yanje y’ukuri ntizotangura! Ikosa ni "Kwinjira vyananiwe ku mashini y'ukuri..." n'ibi bikurikira:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Nkako, ivyo ni ibisanzwe kuko **igikoresho co guhindura ibintu mu buryo bw’impwemu ntigikora kuri mudasobwa yanje**! Kugira ngo ukosore iyo ngorane, ukeneye gusubira gufungura mudasobwa yawe kugira ngo uyigere kuri BIOS maze ushobore gukoresha virtualization.



![Image](assets/fr/021.webp)



Nta kurindira, ndasubira gufungura mudasobwa yanje maze **nkanda urufunguzo rwa "SUPPR" kugira ngo nshobore gushika muri BIOS** (urufunguzo rushobora guhinduka bivanye n'imashini, kandi rushobora kuba F2, nk'akarorero) rwa motherboard yanje ya ASUS. Kugira ngo ukoreshe ubuhinga bwo gukoresha ibintu vy'ukuri, "SVM Mode" itegerezwa gukoreshwa mu gihe canje. Aha na ho, kuva ku motherboard imwe uja ku yindi, kuva ku muhinguzi umwe uja ku wundi, izina rirashobora guhinduka. Rondera igikorwa kivuga kuri **AMD-V** (ku gikoresho ca AMD) canke **Intel VT-x** (ku gikoresho ca Intel).



![Image](assets/fr/022.webp)



Ivyo bimaze gushika, ubike ivyo wahinduye maze wongere utangure imashini y’umubiri... Ubu, **VirtualBox irashobora gutangura imashini y’umubiri** maze igashiramwo ishusho ya Windows ISO kugira ngo ushiremwo ubuhinga bwo gukoresha! 🙂



![Image](assets/fr/023.webp)



Ku nzira yacu y’umubiri ya Windows 11, aho VirtualBox ishizwe, turashobora kubona ko dosiye y’imashini y’umubiri ya Windows 11 irimwo amadosiye atandukanye.





- Dosiye **VBOX** (mu buryo bwa XML) ihuye n'imiterere ya VM (RAM, CPU, n'ibindi)
- Dosiye **VBOX-PREV** ni ububiko bw'imiterere ya kera
- Dosiye **VDI** ihuye na disiki ya Hard mu buryo bw’inguvu, rero ubu ni 13 GB gusa, mu gihe ubunini bwayo burengeye ari 64 GB .
- Dosiye **NVRAM** irimwo ubuzima bwa BIOS bw'imashini y'ukuri, bungana n'ububiko butahinduka bw'imashini y'umubiri .



![Image](assets/fr/024.webp)



## V. Insozero



**VirtualBox ubu irakora ku mashine yacu y'umubiri y'i Windows 11! Igisigaye ni ukuvyungukirako tukagira amashini y’ivy’impwemu!** Nzogaruka ku gushiramwo Windows 11 muri VirtualBox VM mu kindi kiganiro. Ku bijanye na Windows 10, Server ya Windows canke itangazo rya Linux (Ubuntu, Debian, n’ibindi), reka gusa tubayobore!