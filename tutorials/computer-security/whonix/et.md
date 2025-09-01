---
name: Whonix
description: Säilitage oma privaatsust ja konfidentsiaalsust.
---

![cover](assets/cover.webp)



**Whonix** on **Debianil** põhinev Linuxi distributsioon, mis on loodud pakkuma keskkonda, mis ühendab endas **turvalisuse**, **anonüümsuse** ja **privaatsuse**. See on kergesti õpitav ja ühildub erinevate liideste (virtuaalmasinad, Qubes OS, Live-režiim), sisaldab vaikimisi võrguliikluse marsruutimist **Tori** kaudu, **dopeltõrjeseina** (üks tulemüür väravas ja teine tööjaamas), **täielikku kaitset IP/DNS-leviku eest** ja vahendeid, mis aitavad tõhusalt varjata teie tegevust võrgu vaatlejate, sealhulgas teie Interneti-teenusepakkuja eest. **Whonix** on rohkem kui lihtsalt anonüümne süsteem, see on täielik turvaline arenduskeskkond.



## Miks valida Whonix?





- Tasuta**: Whonix on avatud lähtekoodiga süsteem, mis on litsentseeritud täiesti tasuta. Seda arendatakse avatud lähtekoodiga, aktiivse ja läbipaistva kogukonnaga.
- Privaatsus, turvalisus ja anonüümsus**: Whonixi peamine eesmärk on pakkuda üliturvalist keskkonda, kus kõik teie andmed on kaitstud ja teie suhtlus Tor-võrgu kaudu krüpteeritud.
- Lihtne kasutada**: Whonix pakub intuitiivset, eelkonfigureeritud graafilist Interface, mis sobib isegi algajatele kasutajatele. Täiustatud kaitsest kasu saamiseks ei pea olema ekspert.
- Ideaalne keskkond turvaliseks arendamiseks**: Whonix võimaldab teil programme arendada, testida, auditeerida või käivitada, ilma et te kunagi paljastaksite oma tegelikku IP Address või paljastaksite oma sirvimis- või võrgukommunikatsiooniharjumusi.
- Ühekordsed seansid ja Live-režiim**: Whonixi saab käivitada Live-režiimis või ühekordsete masinate kaudu (nt **Qubes OS** kaudu), mis võimaldab kriitilisi ülesandeid täita ilma püsivaid jälgi jätmata, kui seanss on lõppenud.
- Suhteliselt lihtne paigaldus**: Kiireks paigaldamiseks virtuaalmasinatesse (VirtualBox, KVM, Qubes) tarnitakse kasutusvalmis kujutised. Süsteem on dokumenteeritud ja seda uuendatakse regulaarselt.



## Paigaldamine ja konfigureerimine



Enne Whonixi installeerimise juurde asumist on oluline märkida, et see distributsioon **ei ole veel ametlikult saadaval** põhisüsteemina, mida saab paigaldada otse Hard plaadile (paljasmetalli režiimis). Teisisõnu, te **ei saa Whonixi veel installida klassikalise põhiliseks operatsioonisüsteemiks**, nagu Ubuntu või tavaline Debian.



Siiski on saadaval mitu väljaannet, mis võimaldavad Whonixi kasutada **volatiilselt** (Live-režiim, ajutised seansid) või **püsivalt** (virtuaalmasinate või Qubes OS-i integreerimise kaudu).



Pikaajalise ja stabiilse kasutamise puhul on **virtualiseerimine praegu ainus ametlikult soovitatav meetod**. Whonixi saab käivitada **VirtualBoxi** abil (Whonix-Gateway ja Whonix-Workstation) või integreerida seda süsteemi nagu **Qubes OS**. Selles õpetuses keskendume VirtualBoxi installeerimisele.



### Eeltingimused



Enne Whonixi paigaldamist virtuaalses režiimis veenduge, et teie masin vastab minimaalsetele tehnilistele nõuetele. Virtualiseerimine nõuab teatud ressursse, mida kõik arvutid ei suuda pakkuda. Seetõttu on oluline, et teie protsessor toetaks virtualiseerimistehnoloogiat (Intel VT-x või AMD-V) ja et see valik oleks BIOSis/UEFIs lubatud.



Siin on soovitatavad tehnilised andmed, et Whonixi kasutamine oleks sujuv ja stabiilne:





- Juhusjuurdepääsu mälu (RAM)**: soovitatakse tungivalt vähemalt **8 GB**. Mida rohkem RAM-i on, seda rohkem ressursse saate eraldada virtuaalmasinatele (Gateway ja Workstation), mis parandab jõudlust.
- Vaba kettaruum**: palun lubage vähemalt 30 GB vaba kettaruumi**. See hõlmab ruumi, mis on vajalik kahe virtuaalse masina, süsteemifailide ja mis tahes andmete või vahekokkuvõtete jaoks.
- Protsessor**: soovitatav on protsessor, millel on vähemalt **4 füüsilist tuuma** (8 loogilist niiti), eriti kui soovite paralleelselt kasutada teisi teenuseid või tööriistu.



### Lae alla Whonix



Whonix on saadaval mitmes versioonis, sõltuvalt sellest, millises keskkonnas soovite seda kasutada. Enamiku kasutajate jaoks (Windows, Linux või MacOs) on VirtualBoxi väljaanne kõige lihtsamini seadistatav. Image saab alla laadida otse [ametlikust veebisaidist](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **ei ühildu** MacBookidega, mis kasutavad Apple Silicon protsessoreid (ARM-arhitektuur).



## VirtualBoxi paigaldamine



Whonixi käivitamiseks on vaja **hüperviisorit** nagu VirtualBox, Qubes või KVM.



Kui olete faili alla laadinud, installige see nagu mis tahes muu tarkvara. Võtke vastu vaikimisi valikud, kui teil ei ole erinõudeid. Kas olete eksinud? Vaadake meie VirtualBoxi kasutamise juhendit.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Whonixi importimine



Kui VirtualBox on installeeritud, saate importida varem alla laaditud Whonixi `.ova` failid (`Whonix-Gateway-Xfce.ova` ja `Whonix-Workstation-Xfce.ova`).



Avage VirtualBox, seejärel klõpsake **Fail → Import appliance**.


Valige vastav `.ova` fail (alustage väravast).



![0_03](assets/fr/03.webp)



Valige asukoht, kuhu Whonixi virtuaalse masina failid salvestatakse.



![0_04](assets/fr/04.webp)



Nõustuge kasutustingimustega, seejärel käivitage import ja oodake, kuni protsess on lõppenud.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonixi konfiguratsioon



Enne Whonixi käivitamist on oluline kohandada mõningaid **süsteemi seadeid**, et tagada parem jõudlus:



Valige virtuaalmasin **Whonix-Workstation-Xfce**, seejärel klõpsake **Konfigureerimine**.



![0_06](assets/fr/07.webp)



Minge vahekaardile **Süsteem**, kus vaikimisi RAM-i eraldus on 2048 MB. Soovitame seda **tõsta 4096 MB-ni (4 GB)**, et suurendada sujuvust, eriti kui kavatsete avada mitu rakendust või töötada pikkade seansside ajal. Gateway võib jääda 2048 MB juurde, kui te ei kasuta paralleelselt palju Tor-ühendusi.



![0_08](assets/fr/08.webp)



### Whonixiga alustamine



Selleks, et Whonix töötaks korralikult ja turvaliselt, **peate järgima järgmist käivitamisjärjekorda**:



Kõigepealt käivitage **Whonix-Gateway-Xfce** masin. See masin vastutab kogu liikluse suunamise eest läbi **Tor** võrgu. Kui värav ei tööta, ei suunata mingit liiklust Tori kaudu ja te kaotate anonüümsuse.



![0_09](assets/fr/09.webp)



Kui Gateway on täielikult käivitunud (näete, et Tor on ühendatud), saate käivitada **Whonix-Workstation-Xfce**, mis ühendub automaatselt Gateway kaudu.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Süsteemi uuendamine



Sisestage terminali, sisestage järgmine käsk, et uuendada pakettide nimekirja:



```shell
sudo apt update
```



Seejärel käivitage järgmine käsk, et paigaldada olemasolevad uuendused:



```shell
sudo apt full-upgrade
```



## Avasta Whonix



**Whonix** on süsteem, mis on loodud pakkuma **turvalist**, **anonüümset** ja **konfidentsiaalset** arvutikeskkonda, mis sobib ideaalselt internetis surfamiseks ilma teie identiteeti või andmeid ohustamata. Selle saavutamiseks on kaasas hulk kasulikke igapäevaseid rakendusi, mis on loodud teie digitaalse turvalisuse tugevdamiseks kohe alguses.


### KeepassXC



**KeePassXC** on Whonixi integreeritud paroolihaldur. See võimaldab teil **luua, salvestada ja hallata** oma paroole turvaliselt, ilma et peaksite neid kõiki käsitsi meeles pidama. Paroolid salvestatakse **krüpteeritud andmebaasi**, mis on kaitstud põhiparooliga.



### Tor brauser



**Tor Browser** on Whonixi vaikimisi veebibrauser. See tugineb **Tor** võrgule, mis suunab teie liikluse läbi mitmete releede üle maailma, mis teeb teie tegeliku IP Address tuvastamise praktiliselt võimatuks.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** on kerge ja kiire Bitcoin Wallet, mis on eelinstalleeritud Whonixile, et võimaldada teil hallata **krüptovaluutatehinguid** anonüümselt. See ei lae alla kogu Blockchain, vaid kasutab vajaliku teabe saamiseks kaugservereid, mistõttu on see palju kergem kui täielik Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix on midagi enamat kui lihtsalt operatsioonisüsteem: see on tõeline **turvaline keskkond**, mis on loodud teie anonüümsuse, privaatsuse ja tundliku tegevuse kaitsmiseks. Tänu Toril põhinevale arhitektuurile, arukale partitsioneerimisele Gateway ja Workstationi vahel ning eelinstalleeritud tööriistadele, nagu Tor Browser, KeePassXC ja Electrum, pakub see võtmetähtsusega lahendust kõigile, kes soovivad **onüümselt sirvida**, **tööd turvaliselt** või **käsitseda konfidentsiaalseid andmeid**.



Unix-süsteemi turvalisuse tugevdamiseks vaadake meie õpetust oma masina auditeerimise kohta: kontrollige, kas teie operatsioonisüsteemis on turvaauke, ja veenduge, et teie andmed ei ole ohustatud.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af