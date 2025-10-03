---
name: Manjaro
description: Gjør kraften i Arch Linux mer tilgjengelig
---
![cover](assets/cover.webp)



Arch Linux er et populært operativsystem på mange områder, takket være sin robusthet og stabilitet. Det kan imidlertid være vanskelig å sette seg inn i for nybegynnere. Det er nettopp for å løse dette problemet at **Manjaro** ble skapt: for å tilby kraften i Arch Linux, men med en enklere og mer tilgjengelig opplevelse, basert på en intuitiv og lettlært Interface.



## Kom i gang med Manjaro



En av Manjaros største fordeler er det **enkle og effektive oppdateringssystemet**. Du trenger ikke å administrere dem manuelt: Manjaro tar seg av dem for deg! Et ikon i varslingsområdet (plasseringen varierer avhengig av utgave) varsler deg når en oppdatering er tilgjengelig. Alt du trenger å gjøre er å følge instruksjonene, og prosessen er rask og uanstrengt.



Manjaro tilbyr også en **stor katalog med applikasjoner**. Siden Manjaro er basert på Arch Linux, har den direkte tilgang til Arch Linux' offisielle repositorier, som er rike på programvare, inkludert proprietære applikasjoner. Manjaro forsinker noen Arch Linux-oppdateringer litt for ytterligere testing; dette forbedrer stabiliteten på bekostning av en liten forsinkelse i nye utgivelser. Og hvis dette valget ikke er nok for deg, kan du også få tilgang til **AUR (*Arch User Repository*)**, et stort bibliotek som administreres av fellesskapet. Hvis et program ikke finnes i de offisielle repositoriene, er sjansen stor for at det er tilgjengelig i AUR.



En annen fordel med Manjaro er at det er **mye mindre ressurskrevende** enn systemer som Windows eller macOS. Det bruker mindre RAM og datakraft, noe som gjør det til et ideelt valg for eldre eller mindre kraftige datamaskiner: Maskinen din blir smidigere og raskere, og får en ny ungdom.



På toppen av det hele er Manjaro **helt gratis**. I motsetning til Windows eller macOS trenger du ikke å betale noe for å installere det og få mest mulig ut av det. Til slutt tilbyr det **forbedret sikkerhet** takket være regelmessige, raske oppdateringer, noe som begrenser eksponeringen for sårbarheter. Det aktive fellesskapet sørger også for at eventuelle problemer raskt blir rettet og effektive løsninger foreslått.



## Oppdag Manjaro OS



Før du begynner å installere Manjaro, er det viktig å vite at denne distribusjonen er tilgjengelig i flere utgaver. Hver av disse utgavene tilbyr et unikt skrivebordsmiljø som påvirker både arbeidsflyten din og forbruket av systemressurser. Det finnes tre offisielle hovedutgaver av Manjaro.



![0_01](assets/fr/01.webp)





- **KDE Plasma**-utgaven er den mest tilpasningsdyktige. Hvis du er ute etter et system som både er visuelt elegant og har høy ytelse, er KDE Plasma et utmerket valg. Dette stabile skrivebordsmiljøet er ideelt for brukere som ønsker full kontroll og en skreddersydd opplevelse.





- For maskiner med mer begrensede ressurser er **Xfce**-utgaven den ideelle løsningen. Interface er lett og intuitiv, noe som garanterer problemfri drift selv på eldre datamaskiner. I tillegg minner layouten om Windows, noe som gjør overgangen til Linux enklere for nye brukere.





- Endelig tilbyr **GNOME**-utgaven en helt annen tilnærming. Den strømlinjeformede designen legger vekt på produktivitet og organisering gjennom virtuelle arbeidsområder. Denne aktivitetsfokuserte arbeidsflyten er spesielt tiltalende for brukere som allerede er kjent med Linux, og som er ute etter et minimalistisk og svært effektivt miljø.



### Andre Manjaro-utgaver



![0_02](assets/fr/02.webp)



I tillegg til de offisielle utgavene tilbyr Manjaro-fellesskapet også andre versjoner. Disse alternative utgavene er utviklet for å dekke spesifikke behov og tilbyr en rekke ulike skrivebordsmiljøer.



**Cinnamon**-utgaven er et utmerket valg for deg som nettopp har begynt og er på utkikk etter en velkjent Interface. Den er designet for å være enkel å bruke, samtidig som den beholder de klassiske konvensjonene fra tradisjonelle kontormiljøer.



For mer avanserte brukere finnes det utgaver som **i3 Window Manager** eller **Sway**. De er mye lettere og raskere, men krever likevel at man behersker kommandolinjen godt for å kunne konfigureres og utnyttes fullt ut. Disse miljøene er ideelle for dem som ønsker total kontroll over systemet sitt, og som setter effektivitet over alt annet.



## Tekniske krav



For at Manjaro skal fungere optimalt, må datamaskinen din oppfylle noen minimumskrav. Vi anbefaler at du har minst :





- En 64-biters (x86_64) **prosessor**
- 4 GB RAM anbefales **(minimum 2 GB)** (se nedenfor)
- 30 GB diskplass (mer hvis du oppretter en egen `/home`-partisjon)



## Installasjon av Manjaro



For å laste ned, gå til [det offisielle Manjaro-nettsiden] (https://manjaro.org/) og velg den utgaven som passer best til dine behov. Når du har lastet ned filen, må du opprette en oppstartbar USB-nøkkel med Manjaro ISO-bildet.



Gå deretter til [Rufus]-programvarens nettsted (https://rufus.ie/fr/) og last den ned. Kjør programmet, koble til USB-nøkkelen, velg Manjaro ISO-bildet og start flashingen. Vent til prosessen er ferdig før du fjerner nøkkelen. Deretter kan du starte datamaskinen på nytt.



![0_03](assets/fr/03.webp)



For å installere Manjaro på datamaskinen din, må du først slå den helt av. Plugg deretter inn USB-nøkkelen, slå maskinen på igjen og åpne oppstartsmenyen eller UEFI/BIOS-fastvaren ved å trykke på **F2, F10, F12, Escape** eller **Delete** (avhengig av produsent).



Velg deretter USB-nøkkelen som oppstartsenhet for å starte OS-installasjonsprosessen.



### Oppstartsskjerm



Første gang du starter Manjaro fra USB-nøkkelen, kommer du direkte til installasjonsmenyen. Før du starter installasjonen, kan du endre tastaturoppsettet eller systemspråket.



Velg deretter alternativet **Start med drivere med åpen kildekode** for å starte Manjaro-installasjonen. Disse driverne med åpen kildekode er kompatible med det meste av maskinvaren og vil være tilstrekkelige i de fleste tilfeller. Hvis du for eksempel har et NVIDIA-grafikkort eller trenger høyere grafikkytelse, kan du velge **Boot med proprietære drivere**, som bruker proprietære drivere.



![0_04](assets/fr/04.webp)



Systemet vil starte i **standard live-modus**. Dette gir deg mulighet til å teste Manjaros funksjonalitet for å se om det passer til dine behov før du installerer det permanent. Når du er klar, klikker du på **Installer Manjaro Linux**.



Velg ønsket språk for installasjonen, og klikk deretter på **Neste**.



![0_06](assets/fr/06.webp)



Deretter velger du hvor du befinner deg for å stille inn riktig tidssone. På dette stadiet kan du også endre språk og datoformat.



![0_07](assets/fr/07.webp)



Velg tastaturoppsett. Et testfelt er tilgjengelig for å kontrollere at tastene som skrives inn, tilsvarer de forventede tegnene.



![0_08](assets/fr/08.webp)



### Diskpartisjonering


Du har to alternativer for partisjonering av disken.





- Det første, og enkleste, er å slette hele disken og installere Manjaro på den.
- Den andre tillater **manuell partisjonering**.



![0_09](assets/fr/09.webp)



For å få en ren installasjon anbefaler vi at du oppretter minst tre partisjoner:





- En første partisjon på **516 MB** (primær) for **boot**.
- En ekstra **2 GB** (logisk) partisjon for **swap**.
- En tredje partisjon for dine **personlige data**.



Hvis du ønsker å installere et annet system parallelt, må du dele opp denne siste partisjonen og bare allokere én del til Manjaro (minst **15 GB** for å garantere at systemet fungerer som det skal).


### Opprette en brukerkonto



Opprett en brukerkonto på systemet ved å fylle ut den nødvendige informasjonen. Til slutt angir du passordet til administratoren (**root**). Denne administratoren er en **superbruker** med fulle rettigheter på systemet og mulighet til å utføre avanserte kommandoer.



![0_10](assets/fr/10.webp)



### Velg riktig kontorpakke



Manjaro lar deg velge mellom **FreeOffice** og **LibreOffice**.





- **LibreOffice** er mer komplett, med et bredere utvalg av programvare og avanserte funksjoner.
- **FreeOffice** er derimot lettere og inneholder bare det aller viktigste: **TextMaker**, **PlanMaker** og **Presentations**.



![0_11](assets/fr/11.webp)



### Sammendrag av konfigurasjonen



Et oppsummeringsskjermbilde viser alle parameterne du har stilt inn. Du kan gå tilbake for å gjøre endringer hvis det er nødvendig, uten at det påvirker andre innstillinger du allerede har gjort.



Klikk deretter på **Install**, og bekreft for å starte selve installasjonen.



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



### Slutt på installasjonen



På slutten av prosessen merker du av i boksen **Start på nytt nå**, og klikker deretter på **Utført**. Systemet starter på nytt, og **Manjaro er klar til bruk**.



![0_13](assets/fr/14.webp)



## Første skritt med Manjaro



Installasjonen av Manjaro er bare det første steget. For å få mest mulig ut av systemet ditt, er det noen nyttige ting du bør vite.



### Oppdater systemet



Manjaro forenkler oppdateringer i stor grad. Slik oppdaterer du pakkene dine :



```shell
sudo pacman -Syu
```



Denne kommandoen laster ned og installerer de nyeste tilgjengelige versjonene. Vi anbefaler at du kjører den regelmessig for å holde systemet **sikkert og stabilt**.



### Konfigurere et utviklingsmiljø



For å utvikle webapplikasjoner på Manjaro kan du installere de viktigste verktøyene med én enkelt kommando:



```shell
sudo pacman -S nodejs npm git yarn
```



Denne kommandoen installerer Node.js og npm for å kjøre og administrere JavaScript- og TypeScript-prosjektene dine, Git for versjonshåndtering og Yarn som en alternativ pakkebehandler.



### Installere en Bitcoin Wallet



For å administrere bitcoins på Manjaro kan du installere **Electrum**, en lett og sikker Wallet :



```shell
sudo pacman -S electrum  # Install Electrum
```



Electrum lar deg **motta og sende bitcoins** på en enkel måte, samtidig som det tilbyr avanserte funksjoner som flere Wallet-administrasjoner og passphrase-beskyttelse. For en komplett guide til hvordan du bruker Electrum, sjekk ut vår dedikerte veiledning som forklarer hvordan du oppretter en Wallet, sikrer midlene dine og gjennomfører transaksjoner.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

## Sikring av Manjaro-systemet ditt



Sikkerhet er et avgjørende aspekt ved enhver Linux-installasjon. Det er viktig for deg å beskytte konfidensialiteten og integriteten til dataene dine.



### Konfigurasjon av brannmur



Manjaro inkluderer UFW (*Uncomplicated Firewall*), et program for å administrere nettverksfilterbrannmurer, men du må aktivere det manuelt:



```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```



![verbose](assets/fr/15.webp)



### Administrere brukerrettigheter



1. **Opprett en ikke-privilegert bruker**



```shell
sudo useradd -m username
sudo passwd username
```



2. **Sudoers-filkonfigurasjon**



```shell
sudo EDITOR=nano visudo
```



Nå er du klar til å bruke Manjaro Linux på maskinen din. Takket være den **enkle installasjonen**, **enkle oppdateringene** og **fleksibiliteten** får du et kraftig system med høy ytelse, egnet for utvikling, daglig bruk og administrasjon av bitcoins med verktøy som Electrum.



Manjaro kombinerer **stabilitet, hastighet og sikkerhet**, samtidig som det er **helt gratis**, noe som gjør det til et ideelt valg for både nybegynnere og avanserte brukere. Ta deg tid til å utforske de ulike funksjonene og tilpasse miljøet etter dine behov. Hvis du vil ha mer kunnskap og lære mer om Arch Linux-systemet, kan vi anbefale veiledningen vår på det sterkeste.



https://planb.network/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973