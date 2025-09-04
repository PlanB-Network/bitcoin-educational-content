---
name: Whonix
description: Bevar personvernet og konfidensialiteten din.
---

![cover](assets/cover.webp)



**Whonix** er en Linux-distribusjon basert på **Debian**, designet for å tilby et miljø som kombinerer **sikkerhet**, **anonymitet** og **privatliv**. Den er enkel å lære og kompatibel med ulike grensesnitt (virtuelle maskiner, Qubes OS, Live-modus), og inkluderer som standard ruting av nettverkstrafikk via **Tor**, **dobbel brannmur** (en brannmur på gatewayen og en annen på arbeidsstasjonen), **full beskyttelse mot IP/DNS-lekkasjer** og verktøy for å effektivt skjule aktiviteten din for nettverksobservatører, inkludert Internett-leverandøren din. Whonix** er mer enn bare et anonymt system, det er et komplett og sikkert utviklingsmiljø.



## Hvorfor velge Whonix?





- Gratis**: I likhet med de fleste Linux-distribusjoner er Whonix et system med åpen kildekode som lisensieres helt gratis. Det er utviklet i åpen kildekode, med et aktivt og åpent fellesskap.
- Personvern, sikkerhet og anonymitet**: Whonix' hovedmål er å tilby et ultrasikkert miljø, der alle dataene dine er beskyttet og kommunikasjonen din kryptert via Tor-nettverket.
- Enkel å bruke**: Whonix tilbyr en intuitiv, forhåndskonfigurert grafisk Interface, som passer selv for nybegynnere. Du trenger ikke å være ekspert for å dra nytte av avansert beskyttelse.
- Ideelt miljø for sikker utvikling**: Med Whonix kan du utvikle, teste, revidere eller kjøre programmer uten å avsløre din virkelige IP Address eller eksponere dine surfe- eller nettverkskommunikasjonsvaner.
- Engangsøkter og Live-modus**: Whonix kan startes i Live-modus eller via engangsmaskiner (f.eks. via **Qubes OS**), noe som gjør det mulig å utføre kritiske oppgaver uten å etterlate vedvarende spor når økten er avsluttet.
- Relativt enkel installasjon**: Det følger med ferdige avbildninger for rask installasjon i virtuelle maskiner (VirtualBox, KVM, Qubes). Systemet er dokumentert og oppdateres jevnlig.



## Installasjon og konfigurasjon



Før vi går videre til installasjonen av Whonix, er det viktig å merke seg at denne distribusjonen ennå ikke er **offisielt tilgjengelig** som et hovedsystem som kan installeres direkte på Hard-disken (i bare metal-modus). Med andre ord kan du **ikke installere Whonix som et klassisk vertsoperativsystem**, som Ubuntu eller standard Debian.



Det finnes imidlertid flere utgaver, slik at Whonix kan brukes **flyktig** (Live-modus, midlertidige økter) eller **permanent** (via virtuelle maskiner eller integrering i Qubes OS).



For langsiktig, stabil bruk er **virtualisering for øyeblikket den eneste offisielt anbefalte metoden**. Du kan kjøre Whonix ved hjelp av **VirtualBox** (Whonix-Gateway og Whonix-Workstation) eller integrere det i et system som **Qubes OS**. I denne veiledningen fokuserer vi på en VirtualBox-installasjon.



### Forutsetninger



Før du kan installere Whonix i virtuell modus, må du sørge for at maskinen din oppfyller de tekniske minimumskravene. Virtualisering krever visse ressurser som ikke alle datamaskiner kan tilby. Det er derfor viktig at prosessoren din støtter virtualiseringsteknologi (Intel VT-x eller AMD-V), og at dette alternativet er aktivert i BIOS/UEFI.



Her er de anbefalte spesifikasjonene for en jevn og stabil opplevelse med Whonix:





- Random Access Memory (RAM)**: minimum **8 GB** anbefales på det sterkeste. Jo mer RAM du har, desto flere ressurser kan du allokere til de virtuelle maskinene (Gateway og Workstation), noe som forbedrer ytelsen.
- Tilgjengelig diskplass**: Sørg for minst 30 GB ledig diskplass**. Dette inkluderer plassen som kreves for de to virtuelle maskinene, systemfiler og eventuelle data eller øyeblikksbilder.
- Prosessor**: En prosessor med minst **4 fysiske kjerner** (8 logiske tråder) anbefales, spesielt hvis du ønsker å kjøre andre tjenester eller verktøy parallelt.



### Last ned Whonix



Whonix er tilgjengelig i flere utgaver, avhengig av hva slags miljø du ønsker å bruke det i. For de fleste brukere (Windows, Linux eller MacOs) er VirtualBox-utgaven den enkleste å sette opp. Du kan laste ned avbildningen direkte fra [det offisielle nettstedet] (https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **er ikke kompatibel** med MacBooks som bruker Apple Silicon-prosessorer (ARM-arkitektur).



## Installere VirtualBox



For å kjøre Whonix trenger du en **hypervisor** som VirtualBox, Qubes eller KVM.



Når du har lastet ned filen, installerer du den på samme måte som all annen programvare. Godta standardalternativene med mindre du har spesifikke krav. Har du gått deg vill? Ta en titt på vår guide til bruk av VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Importerer Whonix



Når VirtualBox er installert, kan du importere Whonix `.ova`-filene du lastet ned tidligere (`Whonix-Gateway-Xfce.ova` og `Whonix-Workstation-Xfce.ova`).



Åpne VirtualBox, og klikk deretter på **File → Import appliance**.


Velg den tilsvarende `.ova`-filen (start med Gateway).



![0_03](assets/fr/03.webp)



Velg stedet der filene til den virtuelle Whonix-maskinen skal lagres.



![0_04](assets/fr/04.webp)



Godta vilkårene for bruk, start deretter importen og vent til prosessen er ferdig.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix-konfigurasjon



Før du starter Whonix, er det viktig å justere noen **systeminnstillinger** for å sikre bedre ytelse:



Velg den virtuelle maskinen **Whonix-Workstation-Xfce**, og klikk deretter på **Configuration**.



![0_06](assets/fr/07.webp)



Gå til fanen **System**, der standard RAM-allokering er 2048 MB. Vi anbefaler at du **øker den til 4096 MB (4 GB)** for å få bedre flyt, spesielt hvis du har tenkt å åpne flere programmer eller jobbe i lange økter. Gateway kan forbli på 2048 MB, med mindre du bruker mange Tor-tilkoblinger parallelt.



![0_08](assets/fr/08.webp)



### Kom i gang med Whonix



For at Whonix skal fungere korrekt og sikkert, **må du følge denne oppstartssekvensen**:



Først starter du maskinen **Whonix-Gateway-Xfce**. Denne maskinen er ansvarlig for å dirigere all trafikk gjennom **Tor**-nettverket. Hvis gatewayen ikke kjører, vil ingen trafikk bli rutet via Tor, og du vil miste anonymiteten.



![0_09](assets/fr/09.webp)



Når gatewayen er ferdig lansert (du vil se at Tor er tilkoblet), kan du starte **Whonix-Workstation-Xfce**, som automatisk kobler seg til via gatewayen.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Oppdatering av systemet



Gå inn i terminalen, og skriv inn følgende kommando for å oppdatere listen over pakker:



```shell
sudo apt update
```



Kjør deretter følgende kommando for å installere de tilgjengelige oppdateringene:



```shell
sudo apt full-upgrade
```



## Oppdag Whonix



**Whonix** er et system som er utviklet for å gi deg et **sikkert**, **anonymt** og **fortrolig** datamiljø, ideelt for å surfe på Internett uten å kompromittere din identitet eller dine data. For å oppnå dette leveres det med en rekke nyttige hverdagsapplikasjoner som er utviklet for å styrke din digitale sikkerhet helt fra starten av.


### KeepassXC



**KeePassXC** er Whonix' integrerte passordbehandling. Den lar deg **opprette, lagre og administrere** passordene dine på en sikker måte, uten at du trenger å huske dem manuelt. Passordene lagres i en **kryptert database**, beskyttet av et hovedpassord.



### Tor-nettleser



**Tor Browser** er Whonix' standard nettleser. Den er avhengig av **Tor**-nettverket, som omdirigerer trafikken din gjennom flere releer rundt om i verden, noe som gjør det praktisk talt umulig å identifisere din virkelige IP Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** er en lett og rask Bitcoin Wallet, forhåndsinstallert på Whonix for å la deg administrere **kryptovaluta-transaksjoner** anonymt. Den laster ikke ned hele Blockchain, men bruker eksterne servere for å innhente nødvendig informasjon, noe som gjør den mye lettere enn en full Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix er mer enn bare et operativsystem: Det er et ekte **sikkert miljø** som er utviklet for å beskytte din anonymitet, ditt personvern og dine sensitive aktiviteter. Takket være den Tor-baserte arkitekturen, intelligent partisjonering mellom Gateway og Workstation og forhåndsinstallerte verktøy som Tor Browser, KeePassXC og Electrum, tilbyr Whonix en nøkkelferdig løsning for alle som ønsker å **surfe anonymt**, **jobbe sikkert** eller **håndtere konfidensielle data**.



For å styrke sikkerheten på Unix-systemet ditt kan du ta en titt på veiledningen vår om revisjon av maskinen din: Sjekk om det finnes sikkerhetshull i operativsystemet ditt, og sørg for at dataene dine ikke er kompromittert.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af