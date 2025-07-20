---
name: Bacca
description: Konfigurisanje Ledger bez Ledger Live softvera
---
![cover](assets/cover.webp)


Ako koristite Ledger, verovatno ste otkrili da morate proći kroz Ledger Live softver, barem za početnu konfiguraciju uređaja, da biste proverili njegovu autentičnost i instalirali Bitcoin aplikaciju na njega. Međutim, nakon ove konfiguracije, mnogi bitkoineri preferiraju da koriste specijalizovani Bitcoin Wallet softver za upravljanje kao što su Sparrow ili Liana umesto Ledger Live. Iako Ledger proizvodi odlične hardverske novčanike koji brzo uključuju najnovije Bitcoin funkcije, njihov softver nije nužno prilagođen specifičnim potrebama bitkoinera. Naime, Ledger Live uključuje mnoge funkcije dizajnirane za altcoine, dok su opcije posvećene Bitcoin Wallet upravljanju ograničene. Ali problem sa Sparrow i Liana (za sada), je što ne omogućavaju instalaciju Bitcoin aplikacije na Ledger.


Da biste zaobišli potrebu korišćenja Ledger Live tokom početne konfiguracije vašeg Ledger, možete koristiti alat Bacca (ili "Ledger Installer"). Ovaj softver vam omogućava da instalirate i ažurirate Bitcoin aplikaciju, verifikujete autentičnost vašeg Ledger, pa čak i kasnije ažurirate firmware uređaja. Bacca je kreirao Antoine Poinsot (Darosior), Bitcoin Core developer u Chaincode Labs, suosnivač [Revault i Liana](https://wizardsardine.com/), i Pythcoiner.


U ovom vodiču pokazaću vam kako da koristite ovaj alat, tako da možete zauvek bez Ledger Live softvera, a i dalje uživate u Ledger uređajima. Radi na svim uređajima: Nano S Classic, Nano S Plus, Nano X, Flex i Stax.


---
*Imajte na umu da je ovaj alat prilično nov, a njegovi programeri navode da je još uvek **u fazi testiranja**. Preporučuju da se koristi samo za testne svrhe, a ne za uređaj namenjen za hostovanje pravog Bitcoin Wallet, iako je to moguće. U tom smislu, preporučujem da pratite preporuke programera ovog alata, koje su navedene [u README njihovog GitHub repozitorijuma](https://github.com/darosior/ledger_installer).*


---
## Preduslovi


Na vašem računaru, biće vam potrebna dva alata za korišćenje Bacca:




- Git ;
- Rust.


Ako ste ih već instalirali, možete preskočiti ovaj korak.


**Linux:**


Na Linux distribuciji, Git je obično unapred instaliran. Da biste proverili da li je Git instaliran na vašem sistemu, možete upisati sledeću komandu u terminalu :


```bash
git --version
```


Ako nemate instaliran Git na vašem sistemu, evo komande za instalaciju na Debianu:


```bash
sudo apt install git
```


Konačno, da biste instalirali vaše Rust razvojno okruženje, koristite komandu :


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Prozori:**


Da biste instalirali Git, idite na [zvaničnu veb stranicu projekta](https://git-scm.com/). Preuzmite softver i pratite uputstva za instalaciju.


![BACCA](assets/fr/01.webp)


Postupite na isti način da instalirate Rust sa [zvanične veb stranice](https://www.Rust-lang.org/tools/install).


![BACCA](assets/fr/02.webp)


**MacOS:**


Ako Git već nije instaliran na vašem sistemu, otvorite terminal i pokrenite sledeću komandu da ga instalirate:


```bash
git --version
```


Ako Git nije instaliran na vašem sistemu, otvoriće se prozor koji vam nudi instalaciju Xcode-a, koji uključuje Git. Jednostavno pratite uputstva na ekranu da biste nastavili sa instalacijom.


Da instalirate Rust, pokrenite sledeću komandu:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Instalacija Bacca


Otvorite terminal i idite do fascikle u kojoj želite da sačuvate softver, zatim pokrenite sledeću komandu:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


Idite u direktorijum softvera:


```bash
cd ledger_installer
```


Zatim koristite Cargo za kompajliranje projekta i pokretanje Bacca GUI:


```bash
cargo run -p ledger_manager_gui
```


Sada imate pristup softveru Interface.


![BACCA](assets/fr/03.webp)


## Konfigurisanje Ledger


Pre nego što počnete, ako je vaš Ledger nov, uverite se da ste postavili PIN kod i sačuvali frazu za oporavak. Za ove početne korake vam nije potreban Ledger Live. Jednostavno povežite vaš Ledger putem USB kabla da biste ga napajali. Ako niste sigurni kako da nastavite sa ova dva koraka, možete se obratiti početku tutorijala specifičnog za vaš model:


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Korišćenje Bacca


Povežite svoj Ledger sa računarom i otključajte ga koristeći PIN kod koji ste postavili. Bacca bi trebalo automatski da detektuje vaš Ledger.


![BACCA](assets/fr/04.webp)


Da biste potvrdili autentičnost vašeg Ledger, kliknite na dugme "*Proveri*". Biće potrebno da autorizujete vezu na vašem Ledger uređaju da biste nastavili.


![BACCA](assets/fr/05.webp)


Bacca će vas zatim obavestiti da li je vaš Ledger originalan. Ako nije, to ukazuje na to da je uređaj ili kompromitovan, ili da je falsifikat. U tom slučaju, odmah prestanite da ga koristite.


![BACCA](assets/fr/06.webp)


U meniju "*Aplikacije*", možete pogledati listu aplikacija koje su već instalirane na vašem Ledger.


![BACCA](assets/fr/07.webp)


Da biste instalirali aplikaciju Bitcoin, kliknite na "*Install*", zatim autorizujte instalaciju na vašem Ledger.


![BACCA](assets/fr/08.webp)


Aplikacija je dobro instalirana.


![BACCA](assets/fr/09.webp)


Ako nemate instaliranu najnoviju verziju aplikacije Bitcoin, Bacca će prikazati dugme "*Update*" umesto oznake "*Latest*". Jednostavno kliknite na ovo dugme da biste ažurirali aplikaciju.


![BACCA](assets/fr/10.webp)


Sada kada je vaš Ledger pravilno konfigurisan sa najnovijom verzijom aplikacije Bitcoin, spremni ste da uvezete i koristite vaš Wallet na softverima za upravljanje kao što su Sparrow ili Liana, bez potrebe da prolazite kroz Ledger Live!


Ako ste smatrali ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!


Preporučujem vam da pogledate ovaj vodič o GnuPG-u, koji objašnjava kako proveriti integritet i autentičnost vašeg softvera pre nego što ga instalirate. Ovo je važna praksa, posebno kada instalirate Wallet upravljački softver kao što su Liana ili Sparrow :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc