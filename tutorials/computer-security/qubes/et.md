---
name: Qubes
description: Mõistlikult turvaline operatsioonisüsteem.
---

![cover](assets/cover.webp)



Qubes OS on vaba, avatud lähtekoodiga operatsioonisüsteem, mis on mõeldud kasutajatele, kes peavad turvalisust oma prioriteetide seas esmatähtsaks. Selle eripära põhineb lihtsal, kuid radikaalsel ideel: selle asemel, et käsitleda arvutit kui tervikut, jagatakse selle kasutamine sõltumatuteks osakondadeks, mida nimetatakse **_qubes_**.



Iga qube toimib kui **isoleeritud virtuaalne keskkond**, millel on konkreetne usaldustase ja funktsioon. Seega isegi kui rakendus on ohustatud, jääb rünnak ainult selle qube'ile, mõjutamata ülejäänud süsteemi.



> Kui te suhtute tõsiselt turvalisusesse, on Qubes OS parim operatsioonisüsteem, mis praegu saadaval on. - **Edward Snowden**.

Qubes OS-i paigaldamine nõuab siiski rohkem ettevalmistusi kui tavalise operatsioonisüsteemi paigaldamine. See eeldab teatud riistvara eeltingimuste kontrollimist, virtualiseerimise põhitõdede mõistmist ja teistsuguse kogemuse aktsepteerimist, kus iga igapäevane ülesanne mõeldakse eraldiseisvana. Kuid kui Qubes OS on kord kasutusele võetud, pakub see töökindlat raamistikku, mis muudab teie igapäevase suhtlemise arvutiga ümber. Selles õpetuses selgitame, kuidas Qubes OS töötab ja kuidas seda hõlpsasti oma süsteemi paigaldada.



## Kuidas Qubes OS töötab?



Qubes OS põhineb jaotuse põhimõttel. Selle asemel, et kasutada ühte süsteemi, tugineb see **Xen** hüperviisorile, et luua isoleeritud virtuaalmasinad, mida nimetatakse qubes'iks. Iga qube on pühendatud konkreetsele ülesandele või usalduse tasemele (töö, isiklik sirvimine, pangandus jne). Selline eraldatus tagab, et ükskõik milline kompromiss ühes qube'is ei saa levida teistesse, toimides nagu mitu sõltumatut arvutit ühes masinas.



Kasutajat Interface haldab keskne turvaline domeen nimega **dom0**. See domeen on Internetist täielikult isoleeritud, mistõttu on see süsteemi süda. Kuigi dom0 kuvab aknaid ja menüüsid, toimub rakenduste tegelik täitmine vastavates qubes.



## Erinevad qubes'i tüübid



Dom0 ümber keerlevad eri tüüpi qubes, millel kõigil on väga spetsiifiline roll.





- **AppVM** kasutatakse igapäevaste rakenduste käivitamiseks: kasutaja saab seega eraldada oma tööalased e-kirjad veebis sirvimisest või pangatoimingutest, kusjuures mõlemad keskkonnad on üksteisest täiesti sõltumatud.





- Need AppVMid põhinevad omakorda **TemplateVMidel**, mis on tsentraliseeritud mallid tarkvara paigaldamiseks ja uuendamiseks, kõrvaldades vajaduse hallata iga qube eraldi.



Qubes OS integreerib ka virtuaalmasinad, mis on spetsialiseerunud **süsteemi teenustele**.





- **NetVM** haldab otse **võrguseadmeid** ja tagab ühenduse Internetiga. Sageli on nad seotud **FirewallVMidega**, mis sekkuvad, et **filterdada liiklust** ja piirata teiste qubide kokkupuudet.





- ServiceVM-idel on sarnane roll näiteks USB-seadmete haldamisel, alati sama loogika alusel: isoleerida kõige riskantsemad komponendid, et vähendada ründepinda.



Lõpuks pakub Qubes OS juhuslike või riskantsete ülesannete jaoks **DisposableVM**. Need efemeersed qubes luuakse jooksvalt, et **avada kahtlane dokument** või **külastada kahtlane sait**, ning kaovad sulgemisel täielikult, kustutades kõik jäljed ja takistades püsivaid rünnakuid.



### Turvalise kopeerimise mehhanism (qrexec)



Qubide vaheline teabevahetus põhineb **qrexecil**, mis on VMidevaheline sidesüsteem, mis on loodud turvalisuse tagamiseks. Selle asemel, et lasta qubidel vabalt suhelda, kehtestab qrexec **spetsiifilised reeglid**: fail, mis kopeeritakse ühest AppVMist teise, või tekst, mis edastatakse lõikelaua kaudu, läbib alati kanali, mida süsteem jälgib ja valideerib. Sel viisil kontrollitakse isegi lihtsat kopeerimist ja kleepimist, et vältida pahavara levikut.



### Ketta haldamine



Qubes OS kasutab salvestusruumi haldamiseks geniaalset süsteemi. TemplateVM-id sisaldavad ühist tarkvarabaasi, samas kui AppVM-id lisavad ainult oma isiklikud andmed ja spetsiifilised failid. See vähendab kettaruumi kasutamist ja hõlbustab globaalseid uuendusi. DisposableVM-id kasutavad seevastu ajutisi mahte, mis sulgemisel täielikult kaovad. See mudel ei taga mitte ainult suuremat turvalisust, vaid ka tõhusat ressursihaldust.



## Miks valida Qubes OS?



Qubes OSi eelised seisnevad eelkõige selle ainulaadses turvamudelis. Selle lähenemisviisi keskmes on killustatus, mis kaitseb kasutajat, isoleerides iga ülesande eraldi virtuaalmasinatesse. Praktiliselt võib nakatunud e-kiri või pahatahtlik veebisait ohustada ainult ühte qube'i, jättes ülejäänud süsteemi ja teie isiklikud andmed täielikult kaitstuks. Selline arhitektuur piirab märkimisväärselt keerulisi rünnakuid, mis tavalises süsteemis võiksid vabalt levida.



Qubes OS pakub ka täielikku läbipaistvust ja kontrolli teie digitaalse keskkonna üle. Te teate täpselt, millisel tarkvaral on juurdepääs millisele ressursile, olgu selleks siis võrk, USB-seade või muud tundlikud komponendid. Süsteem integreerib vaikimisi täiustatud turvaelemendid, näiteks täieliku ketta krüpteerimise, ja hõlbustab anonüümsete teenuste, näiteks Whonixi operatsioonisüsteemi kasutamist.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Selle asemel, et püüda luua läbimatu süsteem, keskendub Qubes OS vastupanuvõimele: see kapseldab kahjustused kompromissi korral, vähendades riski ülejäänud süsteemile. Selline pragmaatiline lähenemine teeb Qubes OSi eelistatud valikuks kasutajatele, kellel on kõrged turvanõuded või kes soovivad säilitada maksimaalset kontrolli oma digitaalse elu üle.



## Qubes OS paigaldamine



Enne Qubes OS-i paigaldamist on oluline veenduda, et teie riistvara vastab miinimumnõuetele, kuna süsteem tugineb virtualiseerimisele, et isoleerida qubes. Peamised komponendid, mida tuleb kontrollida, on :




- **Protsessor**: 64-bitine protsessor, mis ühildub riistvaralise virtualiseerimisega (Intel VT-x või AMD-V).
- RAM: vajalik on vähemalt 8 GB, kuid soovitame mitme qubi samaaegseks kasutamiseks 16 GB või rohkem RAMi.
- **Salvestusruum**: vähemalt 36 GB, ideaalis 128 GB SSD-plaadil, et saavutada optimaalne jõudlus.



Qubes OS-i paigaldamiseks laadige alla ametlik ISO-kujutis Qubes OS [ametlik kodulehekülg](https://www.qubes-os.org/downloads/). Oluline on kontrollida ISO-formaadi terviklikkust, kasutades selleks ettenähtud GPG-allkirju, et tagada, et faili ei ole võltsitud ja et allalaadimine on turvaline.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Kui ISO on kontrollitud, peate looma käivitatava paigalduskandja, tavaliselt USB-pulga. Selleks laadige alla ja installige tarkvara, näiteks **Rufus** Windowsis või **Etcher** Windowsis, Linuxis või macOSis. Need tööriistad võimaldavad teil ISO-d USB-pulgale kopeerida, nii et see oleks käivitatav.



Enne paigaldamise alustamist on vaja konfigureerida arvuti **BIOS või UEFI** nii, et see **lubib virtualiseerimise** ja lubab USB-st käivitamist. Sõltuvalt teie masina mudelist võib olla vajalik **välja lülitada turvaline käivitamine**, kuna Qubes OS ei pruugi selle valikuga käivituda.



![0_02](assets/fr/02.webp)



Kui need tingimused on täidetud, taaskäivitage arvuti ja sisenege BIOS/UEFIsse, vajutades kohe **Esc**, **Del**, **F9**, **F10**, **F11** või **F12** (sõltuvalt tootjast). Käivitamismenüüst valige USB-mälu kui alglaadimisseade, et käivitada Qubes OS-i paigaldus.



**Start-up ekraan**


USB-mälupulgalt käivitamisel viiakse teid otse **GRUB** menüüsse, kus saate valida toimingu, mida soovite teha. Kasutades klaviatuuri nooleklahve, valige "Install Qubes OS" ja vajutage "Enter".



![0_03](assets/fr/03.webp)



**Valik keel** :



Kui paigaldamine algab, tuleb kõigepealt **valida teie konfiguratsioonile sobiv keel** ja **piirkondlik variant**. Sellega tagatakse, et süsteem ja paigaldusvalikud kuvatakse õigesti teie eelistatud keeles.



![0_04](assets/fr/04.webp)



**Parameetrite konfiguratsioon** :



Selles etapis peate enne installimise käivitamist oma masinas konfigureerima mitu Elements.



![0_05](assets/fr/05.webp)



**Klaviatuuri paigutus** :



Klõpsake valikul **Klaviatuur**, seejärel valige arvutile **vastav paigutus**. Kui olete oma valiku teinud, klõpsake **Terminated**, et liikuda edasi järgmise sammu juurde.



**Valik sihtkoha** :



Valige valik "Installeerimise sihtkoht", et valida ketas, millele soovite Qubes OS-i paigaldada. Vaikimisi toimub partitsioneerimine automaatselt, mis võimaldab teil eemaldada kõik andmed kettalt ja paigaldada süsteem sellele. Saate siiski valida **Customized** või **Advanced Customization**, et teha kohandatud partitsioneerimine. Seejärel klõpsake nuppu "Valmis". Süsteem palub teil määrata **salasõna**, mis toimib teie andmete krüpteerimiseks Layer turvasüsteemina. Valige kindlasti keeruline ja unikaalne parool.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Valige kuupäeva ja kellaaja formaat** :


Klõpsake valikut Kellaaeg ja kuupäev, seejärel valige oma geograafiline tsoon. Samuti saate valida oma eelistatud ajaformaadi: 24h või 12h.



![0_08](assets/fr/08.webp)



**Kasutajakonto loomine** :


Klõpsake **Loo kasutaja**, et luua oma **esimene konto**, mis võimaldab teil Qubes OS-i sisse logida.



![0_09](assets/fr/09.webp)



**Activate root account** :


Saate ka **võimaldada root-konto**, määrates administreerimiseks eraldi salasõna.



![0_10](assets/fr/10.webp)



Kui need seaded on tehtud, klõpsake protsessi alustamiseks nuppu **Start installation**.



![0_11](assets/fr/11.webp)



Oodake **paigaldamise lõppu**, seejärel klõpsake **süsteemi taaskäivitamine**, et lõpetada paigaldus ja käivitada Qubes OS.



![0_12](assets/fr/12.webp)



**Lisakonfiguratsioon** :


Pärast taaskäivitamist palub Qubes OS teil **eelistatud mallide ja qubes'i konfiguratsiooni** lõpule viia. Sisestage ketta krüpteerimiseks määratud parool.



![0_13](assets/fr/13.webp)



Seejärel valige esmalt **TemplateVM**, mida soovite paigaldada. Levinud valikud on **Debian 12 Xfce**, **Fedora 41 Xfce** ja **Whonix 17**, kusjuures viimast soovitatakse kasutamiseks, kui on vaja **anonüümsust ja võrguturvet**. Samuti saate määrata **default template**, mis on aluseks uute **AppVMide** loomisel.



![0_14](assets/fr/14.webp)



Jaotises **Main configuration** saate valida, kas luua automaatselt olulised süsteemi qubes nagu **sys-net**, **sys-firewall** ja **default DisposableVM**. Soovitatav on lubada valik **sys-firewall ja sys-usb ühekordselt kasutatav**, et piirata seadme ja võrgu kokkupuudet kompromissi korral. Samuti saate luua vaikimisi **AppVMs**, näiteks **personal**, **work**, **untrusted** ja **vault**, et korraldada oma tegevusi vastavalt nende usaldusastmele.



![0_15](assets/fr/15.webp)



Qubes OS võimaldab teil luua ka **qube, mis on pühendatud USB-seadmetele** (sys-usb) ja konfigureerida **Whonix Gateway ja Workstation qubes**, et turvata oma side Tor-võrgu kaudu. Edasijõudnud kasutajatele võimaldab jaotis **Advanced configuration** luua **LVM thin pool**, et tõhusalt hallata kettaruumi qubes'i vahel.



Kui kõik need valikud on konfigureeritud, klõpsake **Täielik** ja seejärel **Konfigureerimise lõpetamine**. Oodake, kuni süsteem rakendab need seaded. Seejärel palutakse teil **sisselogida oma kasutajakontole** ja teie Qubes OS keskkond on kasutusvalmis, turvaline ja korralikult isoleeritud teie erinevate tegevuste jaoks.



![0_17](assets/fr/17.webp)



Teie operatsioonisüsteem on nüüd paigaldatud ja kasutusvalmis.



![0_18](assets/fr/18.webp)



## Loo oma süsteemi qube



Qube'i loomiseks hallatakse protsessi tööriistaga **Qube Manager**, mis on kättesaadav menüüst Start. Tööriista aknas klõpsake lihtsalt ikoonil **Create qube**, et avada uus konfiguratsiooniaken. Esmalt sisestage oma qube'ile nimi, näiteks "perso-web" või "work", et tuvastada selle kasutusotstarve.



Järgmisena valite selle **Tüübi**, tavaliselt **AppVM** rutiinsete ülesannete jaoks või **DisposableVM** ajutiseks kasutamiseks. Väga oluline on valida **Template**, millel teie qube põhineb, näiteks "fedora-39" või "debian-12", sest see annab operatsioonisüsteemi ja tarkvara. Samuti määrate **NetVM**, mis on qube, mis vastutab internetiühenduse eest, vaikimisi **sys-firewall**.



Lõpuks, pärast salvestusruumi suuruse ja vajaduse korral RAM-i kohandamist, käivitatakse loomise protsess lihtsa klõpsuga nupule **OK**. Kui protsess on lõpetatud, on teie uus qube nimekirjas nähtav ja kasutusvalmis.



Kokkuvõtteks võib öelda, et Qubes OS ei ole tavaline operatsioonisüsteem, vaid tipptasemel turvalahendus, mis mõtleb ümber personaalarvuti arhitektuuri. Selle lähenemisviis, mis põhineb virtualiseerimise kaudu toimuval eraldamisel ja eraldamisel, pakub võrratut kaitset kõige keerukamate ohtude eest. Segmenteerides töökeskkonna iga ülesande jaoks spetsiaalseteks qubedeks, tagab see, et pahavara ei saa levida ja ohustada kogu süsteemi.



Olenemata sellest, kas teil on vaja turvaliselt veebis surfata, kaitsta tundlikku teavet või töötada erineva usaldustasemega, pakub Qubes OS vastupidavat ja läbipaistvat raamistikku. Kui võtate kasutusele head tavad ja kasutate täielikult selle funktsioone, on teil **digitaalne kindlus**, mis on kohandatud kaasaegsetele ohtudele. Lisateave oma andmete ja privaatsuse kaitsmise kohta.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1