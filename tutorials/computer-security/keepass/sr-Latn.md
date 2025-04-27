---
name: KeePass
description: Kako postaviti lokalni menadžer lozinki?
---
![cover](assets/cover.webp)


U digitalnom dobu, moramo upravljati mnoštvom online naloga koji pokrivaju različite aspekte naših svakodnevnih života, uključujući bankarstvo, finansijske platforme, emailove, skladištenje fajlova, zdravlje, administraciju, društvene mreže, video igre, itd.


Da bismo se autentifikovali na svakom od ovih naloga, koristimo identifikator, često email Address, praćen lozinkom. Suočeni sa nemogućnošću pamćenja velikog broja jedinstvenih lozinki, mogli bismo biti u iskušenju da ponovo koristimo istu lozinku ili da malo modifikujemo zajedničku osnovu kako bismo je lakše zapamtili. Međutim, ove prakse ozbiljno ugrožavaju bezbednost vaših naloga.


Prvi princip koji treba slediti za lozinke je da ih ne koristite ponovo. Svaki online nalog treba da bude zaštićen jedinstvenom i potpuno različitom lozinkom. Ovo je važno jer, ako napadač uspe da kompromituje jednu od vaših lozinki, ne želite da ima pristup svim vašim nalozima. Imati jedinstvenu lozinku za svaki nalog izoluje potencijalne napade i ograničava njihov domet. Na primer, ako koristite istu lozinku za platformu za video igre i za vaš email, i ta lozinka bude kompromitovana putem phishing sajta povezanog sa platformom za igre, napadač bi tada lako mogao da pristupi vašem emailu i preuzme kontrolu nad svim vašim drugim online nalozima.


Drugi suštinski princip je jačina lozinke. Lozinka se smatra jakom ako je teško probiti je metodom grube sile, tj. pogađanjem kroz pokušaje i greške. To znači da vaše lozinke moraju biti što nasumičnije, duge i uključivati raznovrsne karaktere (mala slova, velika slova, brojeve i simbole).


Primena ova dva principa bezbednosti lozinki (jedinstvenost i robusnost) može biti teška u svakodnevnom životu, jer je gotovo nemoguće zapamtiti jedinstvenu, nasumičnu i jaku lozinku za sve naše naloge. Tu na scenu stupa menadžer lozinki.


Menadžer lozinki generiše i sigurno čuva jake lozinke, omogućavajući vam pristup svim vašim online nalozima bez potrebe da ih pojedinačno pamtite. Potrebno je da zapamtite samo jednu lozinku, glavnu lozinku, koja vam daje pristup svim sačuvanim lozinkama u menadžeru. Korišćenje menadžera lozinki poboljšava vašu online sigurnost jer sprečava ponovnu upotrebu lozinki i sistematski generiše nasumične lozinke. Ali takođe pojednostavljuje vašu svakodnevnu upotrebu naloga centralizovanjem pristupa vašim osetljivim informacijama.

U ovom vodiču ćemo naučiti kako postaviti i koristiti lokalni menadžer lozinki kako bismo poboljšali vašu online sigurnost. Ovdje ću vas upoznati sa KeePass-om. Međutim, ako ste početnik i želite imati online menadžer lozinki sposoban za sinhronizaciju na više uređaja, preporučujem da pratite naš vodič o Bitwardenu:

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*Upozorenje: Menadžer lozinki je odličan za čuvanje lozinki, ali **nikada ne bi trebalo da čuvate svoju Bitcoin Wallet's Mnemonic frazu u njemu!** Zapamtite, Mnemonic fraza treba da bude isključivo sačuvana u fizičkom formatu, kao što je papir ili metal.*


---

## Uvod u KeePass


KeePass je besplatan i open-source menadžer lozinki, savršen za one koji žele besplatno i sigurno rešenje za lokalno upravljanje. To je softver koji se instalira na vašem računaru i, bez dodatka dodataka, ne komunicira sa Internetom. Ovo je radikalno drugačiji pristup od onog koji koristi Bitwarden, koji smo pokrili u prethodnom vodiču. Bitwarden, za razliku od KeePass-a, omogućava sinhronizaciju na više uređaja i stoga zahteva čuvanje vaših lozinki na online serveru.


Podrazumevano, KeePass ne podržava korišćenje ekstenzija za pregledače kao što je Bitwarden; stoga ćete morati ručno da kopirate i nalepite svoje lozinke iz softvera. Iako ovo može delovati kao ograničenje, kopiranje i lepljenje lozinki umesto korišćenja automatskog popunjavanja je dobra praksa za vašu onlajn bezbednost.


KeePass je dizajniran da bude lagan i jednostavan za korišćenje, dok se pridržava visokih sigurnosnih standarda. Softver šifrira vašu bazu podataka lokalno za optimalnu zaštitu vaših akreditiva. KeePass je takođe jedini menadžer lozinki koji je validiran od strane ANSSI (francuske agencije za sajber bezbednost).


Jedna od glavnih prednosti KeePass-a je njegova fleksibilnost. Može se koristiti na mnogo različitih načina, kao što je na USB memoriji bez potrebe za instalacijom na računar. Štaviše, zahvaljujući svom [plugin okruženju](https://keepass.info/plugins.html), KeePass se može prilagoditi kako bi zadovoljio specifičnije potrebe.

![KEEPASS](assets/notext/01.webp)

## Kako preuzeti KeePass?


Proces instalacije za KeePass varira u zavisnosti od operativnog sistema koji koristite. Za korisnike Windows ili Linux sistema, instalacija je relativno jednostavna. Međutim, ako koristite macOS, potreban je dodatni korak zbog razvoja KeePass-a na .NET platformi, koja nije direktno podržana od strane macOS-a. Stoga, biće potrebno da konfigurišete kompatibilno okruženje kako biste omogućili pokretanje KeePass-a na Apple uređajima.


Za korisnike Debian/Ubuntu, otvorite terminal i unesite sledeće komande:


```bash
sudo apt-get update

sudo apt-get install keepass2

```

For Fedora:

```

sudo dnf install keepass

```

For Arch Linux:

```

sudo pacman -S keepass

```

If you are on a Windows computer, go to the [official KeePass download page](https://keepass.info/download.html), and download the latest version of the installer:
![KEEPASS](assets/notext/02.webp)
Click on the downloaded file to run it, then follow the instructions of the setup wizard to complete the installation (see next section).

For macOS users, the installation is a bit more complex. If you wish to use the original version of KeePass as on Windows, follow the instructions below. Otherwise, you can opt for [KeePassXC](https://keepassxc.org/), an alternative version compatible with macOS, which offers a slightly different interface.

To use KeePass, you will need a runtime environment for .NET applications. I recommend installing Mono for this. Go to the [official Mono page](https://www.mono-project.com/download/stable/#download-mac) in the "*macOS*" section, and click on the link to download the installation package (`.pkg`).
![KEEPASS](assets/notext/03.webp)
Open the downloaded `.pkg` file and follow the instructions to install Mono on your Mac.
![KEEPASS](assets/notext/04.webp)
Next, go to the official KeePass website and download the latest portable version in `.zip` format.
![KEEPASS](assets/notext/05.webp)
After downloading the `.zip` file, double-click to extract it. You will get a folder containing several files, including `KeePass.exe`. Open a terminal, navigate to the KeePass folder (replace `xx` with the version number):

```

cd ~/Downloads/KeePass-2.xx

```

And finally, run KeePass with Mono:

```

mono KeePass.exe

```