---
name: Whonix
description: Sačuvajte svoju privatnost i poverljivost.
---

![cover](assets/cover.webp)



**Whonix** je Linux distribucija zasnovana na **Debianu**, dizajnirana da pruži okruženje koje kombinuje **sigurnost**, **anonimnost** i **privatnost**. Laka za učenje i kompatibilna sa različitim interfejsima (virtuelne mašine, Qubes OS, Live mod), podrazumevano uključuje rutiranje mrežnog saobraćaja preko **Tor-a**, **dupli firewall** (jedan firewall na Gateway-u i drugi na Workstation-u), **potpunu zaštitu protiv IP/DNS curenja** i alate za efikasno maskiranje vaše aktivnosti od mrežnih posmatrača, uključujući vašeg ISP-a. Više od samo anonimnog sistema, **Whonix** je kompletno sigurno razvojno okruženje.



## Zašto izabrati Whonix?





- Besplatno**: Kao većina Linux distribucija, Whonix je open-source sistem licenciran potpuno besplatno. Razvija se kao open source, uz aktivnu i transparentnu zajednicu.
- Privatnost, bezbednost i anonimnost**: Glavni cilj Whonix-a je da ponudi ultra-bezbedno okruženje, u kojem su svi vaši podaci zaštićeni, a vaše komunikacije šifrovane putem Tor mreže.
- Lako za korišćenje**: Whonix nudi intuitivan, unapred konfigurisan grafički Interface, pogodan čak i za početnike. Nema potrebe da budete stručnjak da biste imali koristi od napredne zaštite.
- Idealno okruženje za siguran razvoj**: Whonix vam omogućava da razvijate, testirate, proveravate ili pokrećete programe bez otkrivanja vašeg pravog IP Address ili izlaganja vaših navika pretraživanja ili mrežne komunikacije.
- Raspršive sesije i režim uživo**: Whonix se može pokrenuti u režimu uživo ili putem raspršivih mašina (npr. putem **Qubes OS**), omogućavajući obavljanje kritičnih zadataka bez ostavljanja trajnih tragova nakon završetka sesije.
- Relativno jednostavna instalacija**: Gotove slike su dostupne za brzu instalaciju u virtuelnim mašinama (VirtualBox, KVM, Qubes). Sistem je dokumentovan i redovno ažuriran.



## Instalacija i konfiguracija



Pre nego što pređete na instalaciju Whonix-a, važno je napomenuti da ova distribucija **još uvek nije zvanično dostupna** kao glavni sistem koji se može direktno instalirati na Hard disk (u bare metal režimu). Drugim rečima, **još uvek ne možete instalirati Whonix kao klasičan host operativni sistem**, poput Ubuntu-a ili standardnog Debian-a.



Međutim, dostupno je nekoliko izdanja, što omogućava da se Whonix koristi **volatile** (Live mod, privremene sesije) ili **persistent** (putem virtuelnih mašina ili integracije u Qubes OS).



Za dugotrajnu, stabilnu upotrebu, **virtualizacija je trenutno jedini zvanično preporučeni metod**. Možete pokrenuti Whonix koristeći **VirtualBox** (Whonix-Gateway i Whonix-Workstation) ili ga integrisati u sistem kao što je **Qubes OS**. U ovom vodiču, fokusiraćemo se na instalaciju putem VirtualBox-a.



### Preduslovi



Pre nego što možete instalirati Whonix u virtuelnom režimu, uverite se da vaš računar ispunjava minimalne tehničke zahteve. Virtuelizacija zahteva određene resurse koje ne mogu svi računari da ponude. Stoga je neophodno da vaš procesor podržava tehnologiju virtuelizacije (Intel VT-x ili AMD-V), i da je ova opcija omogućena u BIOS/UEFI.



Evo su preporučene specifikacije za glatko i stabilno iskustvo sa Whonix-om:





- Random Access Memory (RAM)**: preporučuje se minimum od **8 GB**. Što više RAM-a imate, to više resursa možete dodeliti virtuelnim mašinama (Gateway i Workstation), poboljšavajući performanse.
- Dostupni prostor na disku**: molimo omogućite najmanje 30 GB slobodnog prostora na disku**. Ovo uključuje prostor potreban za dve virtuelne mašine, sistemske fajlove i sve podatke ili snimke.
- Procesor**: preporučuje se procesor sa najmanje **4 fizičke jezgre** (8 logičkih niti), posebno ako želite da pokrećete druge usluge ili alate paralelno.



### Preuzmi Whonix



Whonix je dostupan u nekoliko izdanja, u zavisnosti od tipa okruženja u kojem želite da ga koristite. Za većinu korisnika (Windows, Linux ili MacOs), VirtualBox izdanje je najlakše za postavljanje. Možete preuzeti sliku direktno sa [zvanične veb stranice](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **nije kompatibilan** sa MacBook računarima koji koriste Apple Silicon procesore (ARM arhitektura).



## Instaliranje VirtualBox-a



Da biste pokrenuli Whonix, trebat će vam **hipervizor** kao što su VirtualBox, Qubes ili KVM.



Kada preuzmete datoteku, instalirajte je kao i bilo koji drugi softver. Prihvatite podrazumevane opcije osim ako nemate specifične zahteve. Da li ste se izgubili? Pogledajte naš vodič za korišćenje VirtualBox-a.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Uvoz Whonix



Kada je VirtualBox instaliran, možete uvesti Whonix `.ova` datoteke koje ste ranije preuzeli (`Whonix-Gateway-Xfce.ova` i `Whonix-Workstation-Xfce.ova`).



Otvorite VirtualBox, zatim kliknite na **File → Import appliance**.


Odaberite odgovarajuću `.ova` datoteku (počnite sa Gateway).



![0_03](assets/fr/03.webp)



Izaberite lokaciju gde će Whonix virtuelna mašina biti sačuvana.



![0_04](assets/fr/04.webp)



Prihvatite uslove korišćenja, zatim pokrenite uvoz i sačekajte da se proces završi.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix konfiguracija



Pre nego što pokrenete Whonix, važno je prilagoditi neka **sistemska podešavanja** kako biste osigurali bolju performansu:



Odaberite virtuelnu mašinu **Whonix-Workstation-Xfce**, zatim kliknite na **Konfiguracija**.



![0_06](assets/fr/07.webp)



Idite na karticu **System**, gde je podrazumevana dodela RAM-a 2048 MB. Preporučujemo da je **povećate na 4096 MB (4 GB)** radi veće fluidnosti, posebno ako nameravate da otvorite više aplikacija ili radite u dugim sesijama. Gateway može ostati na 2048 MB, osim ako ne koristite mnogo Tor konekcija paralelno.



![0_08](assets/fr/08.webp)



### Početak sa Whonix



Da bi Whonix radio ispravno i sigurno, **morate pratiti ovaj redosled pokretanja**:



Prvo, pokrenite mašinu **Whonix-Gateway-Xfce**. Ova mašina je odgovorna za usmeravanje celog saobraćaja kroz **Tor** mrežu. Bez pokrenutog gateway-a, nijedan saobraćaj neće biti usmeren preko Tor-a i izgubićete anonimnost.



![0_09](assets/fr/09.webp)



Kada je Gateway potpuno pokrenut (videćete da je Tor povezan), možete pokrenuti **Whonix-Workstation-Xfce**, koji će se automatski povezati putem Gateway-a.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Ažuriranje sistema



Uđite u terminal, unesite sledeću komandu da ažurirate listu paketa:



```shell
sudo apt update
```



Zatim pokrenite sledeću komandu da instalirate dostupna ažuriranja:



```shell
sudo apt full-upgrade
```



## Otkrijte Whonix



**Whonix** je sistem dizajniran da obezbedi **sigurno**, **anonimno** i **poverljivo** računarsko okruženje, idealno za surfovanje Internetom bez ugrožavanja vašeg identiteta ili podataka. Da bi to postigao, dolazi sa brojnim korisnim svakodnevnim aplikacijama dizajniranim da ojačaju vašu digitalnu sigurnost od samog početka.


### KeepassXC



**KeePassXC** je Whonix-ov integrisani menadžer lozinki. Omogućava vam da **kreirate, čuvate i upravljate** vašim lozinkama na siguran način, bez potrebe da ih sve pamtite ručno. Lozinke su sačuvane u **šifrovanoj bazi podataka**, zaštićenoj glavnom lozinkom.



### Tor Pregledač



**Tor Browser** je podrazumevani veb pregledač Whonix-a. Oslanja se na **Tor** mrežu, koja preusmerava vaš saobraćaj kroz nekoliko releja širom sveta, čineći gotovo nemogućim identifikovanje vašeg pravog IP Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** je lagan i brz Bitcoin Wallet, unapred instaliran na Whonix-u kako bi vam omogućio anonimno upravljanje **kriptovalutnim transakcijama**. Ne preuzima ceo Blockchain već koristi udaljene servere za dobijanje potrebnih informacija, što ga čini mnogo lakšim od punog Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix je više od operativnog sistema: to je pravi **siguran okruženje** dizajniran da zaštiti vašu anonimnost, vašu privatnost i vaše osetljive aktivnosti. Zahvaljujući svojoj arhitekturi zasnovanoj na Tor-u, inteligentnoj podeli između Gateway-a i Workstation-a, i unapred instaliranim alatima kao što su Tor Browser, KeePassXC i Electrum, nudi rešenje spremno za upotrebu za svakoga ko želi da **pretražuje anonimno**, **radi sigurno** ili **rukuje poverljivim podacima**.



Da biste ojačali svoju sigurnost na Unix sistemu, pogledajte naš vodič o reviziji vašeg računara: proverite sigurnosne rupe u vašem operativnom sistemu i osigurajte da vaši podaci nisu ugroženi.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af