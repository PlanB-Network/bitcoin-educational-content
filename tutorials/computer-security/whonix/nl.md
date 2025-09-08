---
name: Whonix
description: Behoud je privacy en vertrouwelijkheid.
---

![cover](assets/cover.webp)



**Whonix** is een Linux-distributie gebaseerd op **Debian**, ontworpen om een omgeving te bieden die **veiligheid**, **anonimiteit** en **privacy** combineert. Het is eenvoudig te leren en compatibel met verschillende interfaces (virtuele machines, Qubes OS, Live modus). Het bevat standaard routering van netwerkverkeer via **Tor**, **dubbele firewall** (een firewall op de gateway en een andere op het werkstation), **volledige bescherming tegen IP/DNS lekken** en tools om je activiteiten effectief te maskeren voor netwerkwaarnemers, inclusief je ISP. **Whonix** is meer dan alleen een anoniem systeem, het is een compleet beveiligde ontwikkelomgeving.



## Waarom kiezen voor Whonix?





- Gratis**: Net als de meeste Linux-distributies is Whonix een open-source systeem met een volledig gratis licentie. Het is ontwikkeld in open source, met een actieve en transparante gemeenschap.
- Privacy, veiligheid en anonimiteit**: De belangrijkste doelstelling van Whonix is het bieden van een ultraveilige omgeving, waarin al je gegevens worden beschermd en je communicatie wordt versleuteld via het Tor-netwerk.
- Gebruiksvriendelijk**: Whonix biedt een intuïtieve, vooraf geconfigureerde grafische Interface, die zelfs geschikt is voor beginnende gebruikers. Je hoeft geen expert te zijn om te profiteren van geavanceerde bescherming.
- Ideale omgeving voor veilige ontwikkeling**: Met Whonix kun je programma's ontwikkelen, testen, controleren of uitvoeren zonder ooit je echte IP Address te onthullen of je surf- of netwerkcommunicatiegewoonten bloot te leggen.
- Wegwerpsessies en Live-modus**: Whonix kan worden gestart in Live-modus of via wegwerpmachines (bijvoorbeeld via **Qubes OS**), zodat kritieke taken kunnen worden uitgevoerd zonder persistente sporen achter te laten zodra de sessie is beëindigd.
- Relatief eenvoudige installatie**: Er worden kant-en-klare images geleverd voor een snelle installatie in virtuele machines (VirtualBox, KVM, Qubes). Het systeem is gedocumenteerd en wordt regelmatig bijgewerkt.



## Installatie en configuratie



Voordat we verder gaan met de installatie van Whonix, is het essentieel om op te merken dat deze distributie **nog niet officieel beschikbaar** is als een hoofdsysteem dat direct op de Hard schijf geïnstalleerd kan worden (in bare metal modus). Met andere woorden, je **kunt Whonix nog niet installeren als een klassiek host besturingssysteem**, zoals Ubuntu of standaard Debian.



Er zijn echter verschillende edities beschikbaar, waardoor Whonix **vluchtig** (Live modus, tijdelijke sessies) of **permanent** (via virtuele machines of integratie in Qubes OS) kan worden gebruikt.



Voor langdurig, stabiel gebruik is **virtualisatie momenteel de enige officieel aanbevolen methode**. Je kunt Whonix draaien met **VirtualBox** (Whonix-Gateway en Whonix-Workstation) of integreren in een systeem zoals **Qubes OS**. In deze tutorial richten we ons op een VirtualBox-installatie.



### Vereisten



Voordat je Whonix in virtuele modus kunt installeren, moet je ervoor zorgen dat je machine voldoet aan de minimale technische vereisten. Virtualisatie vereist bepaalde middelen die niet alle computers kunnen bieden. Het is daarom essentieel dat je processor virtualisatietechnologie (Intel VT-x of AMD-V) ondersteunt en dat deze optie is ingeschakeld in de BIOS/UEFI.



Hier zijn de aanbevolen specificaties voor een soepele en stabiele ervaring met Whonix:





- Random Access Memory (RAM)**: een minimum van **8 GB** wordt sterk aanbevolen. Hoe meer RAM je hebt, hoe meer bronnen je kunt toewijzen aan de virtuele machines (Gateway en Workstation), waardoor de prestaties verbeteren.
- Beschikbare schijfruimte**: zorg voor ten minste 30 GB vrije schijfruimte**. Dit is inclusief de ruimte die nodig is voor de twee virtuele machines, systeembestanden en eventuele gegevens of snapshots.
- Processor**: een processor met ten minste **4 fysieke cores** (8 logische threads) wordt aanbevolen, vooral als je andere services of tools parallel wilt draaien.



### Whonix downloaden



Whonix is verkrijgbaar in verschillende edities, afhankelijk van het type omgeving waarin je het wilt gebruiken. Voor de meeste gebruikers (Windows, Linux of MacOs) is de VirtualBox editie het makkelijkst op te zetten. Je kunt het image rechtstreeks downloaden van [de officiële website] (https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **is niet compatibel** met MacBooks die Apple Silicon-processors (ARM-architectuur) gebruiken.



## VirtualBox installeren



Om Whonix te draaien heb je een **hypervisor** nodig zoals VirtualBox, Qubes of KVM.



Zodra je het bestand hebt gedownload, installeer je het zoals je met elke andere software zou doen. Accepteer de standaardopties tenzij je specifieke eisen hebt. Ben je de weg kwijt? Bekijk onze handleiding voor het gebruik van VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Whonix importeren



Zodra VirtualBox is geïnstalleerd, kun je de Whonix `.ova` bestanden importeren die je eerder hebt gedownload (`Whonix-Gateway-Xfce.ova` en `Whonix-Workstation-Xfce.ova`).



Open VirtualBox en klik vervolgens op **Bestand → Apparaat importeren**.


Selecteer het bijbehorende `.ova` bestand (begin met de Gateway).



![0_03](assets/fr/03.webp)



Kies de locatie waar de bestanden van de Whonix virtuele machine worden opgeslagen.



![0_04](assets/fr/04.webp)



Accepteer de gebruiksvoorwaarden, start de import en wacht tot het proces is voltooid.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix configuratie



Voordat je Whonix start, is het belangrijk om een aantal **systeeminstellingen** aan te passen voor betere prestaties:



Selecteer de virtuele machine **Whonix-Workstation-Xfce** en klik vervolgens op **Configuratie**.



![0_06](assets/fr/07.webp)



Ga naar het tabblad **Systeem**, waar de standaard RAM-toewijzing 2048 MB is. We raden je aan om **het te verhogen naar 4096 MB (4 GB)** voor meer vloeiendheid, vooral als je van plan bent om meerdere applicaties te openen of in lange sessies te werken. De Gateway kan op 2048 MB blijven staan, tenzij je veel Tor-verbindingen parallel gebruikt.



![0_08](assets/fr/08.webp)



### Aan de slag met Whonix



Om Whonix goed en veilig te laten werken, **moet je deze opstartvolgorde** volgen:



Start eerst de **Whonix-Gateway-Xfce** machine. Deze machine is verantwoordelijk voor het routeren van al het verkeer door het **Tor** netwerk. Als de gateway niet draait, wordt er geen verkeer via Tor geleid en verlies je je anonimiteit.



![0_09](assets/fr/09.webp)



Zodra de Gateway volledig is opgestart (je ziet dat Tor verbonden is), kun je **Whonix-Workstation-Xfce** starten, die automatisch verbinding maakt via de Gateway.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Systeem bijwerken



Voer in de terminal het volgende commando in om de lijst met pakketten bij te werken:



```shell
sudo apt update
```



Voer vervolgens de volgende opdracht uit om de beschikbare updates te installeren:



```shell
sudo apt full-upgrade
```



## Ontdek Whonix



**Whonix** is een systeem ontworpen om een **veilige**, **anonieme** en **vertrouwelijke** computeromgeving te bieden, ideaal om op het internet te surfen zonder je identiteit of je gegevens in gevaar te brengen. Om dit te bereiken wordt het geleverd met een aantal handige alledaagse toepassingen die ontworpen zijn om je digitale veiligheid vanaf het begin te versterken.


### KeepassXC



**KeePassXC** is de geïntegreerde wachtwoordmanager van Whonix. Hiermee **maakt, bewaart en beheert** u uw wachtwoorden veilig, zonder dat u ze allemaal handmatig hoeft te onthouden. Wachtwoorden worden opgeslagen in een **gecodeerde database**, beschermd door een hoofdwachtwoord.



### Tor-browser



**Tor Browser** is de standaard webbrowser van Whonix. Het maakt gebruik van het **Tor** netwerk, dat je verkeer omleidt via verschillende relais over de hele wereld, waardoor het vrijwel onmogelijk is om je echte IP Address te achterhalen.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** is een lichte en snelle Bitcoin Wallet, voorgeïnstalleerd op Whonix om je **cryptocurrency transacties** anoniem te laten beheren. Het downloadt niet de hele Blockchain, maar gebruikt externe servers om de benodigde informatie te verkrijgen, waardoor het veel lichter is dan een volledige Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix is meer dan alleen een besturingssysteem: het is een echte **veilige omgeving** ontworpen om je anonimiteit, je privacy en je gevoelige activiteiten te beschermen. Dankzij de Tor-gebaseerde architectuur, intelligente partitionering tussen Gateway en Workstation en voorgeïnstalleerde tools zoals Tor Browser, KeePassXC en Electrum, biedt het een kant-en-klare oplossing voor iedereen die anoniem wil surfen**, **veilig wil werken** of **vertrouwelijke gegevens** wil verwerken**.



Om je beveiliging op je Unix-systeem te versterken, kun je onze tutorial over het auditen van je machine bekijken: controleer op beveiligingslekken in je besturingssysteem en zorg ervoor dat je gegevens niet in gevaar komen.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af