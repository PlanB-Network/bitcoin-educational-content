---
name: LN VPN

description: Uw VPN instellen
---

![image](assets/cover.webp)


LN VPN is een aanpasbare VPN-service die alleen bliksembetalingen accepteert. Vandaag laat ik je zien hoe je het kunt gebruiken om minder sporen achter te laten tijdens het surfen op internet.


Er zijn veel VPN-serviceproviders van goede kwaliteit en we hebben in dit artikel (hyperlink) een uitgebreide beoordeling uitgevoerd. LN VPN springt er echter uit, en we konden de kans niet voorbij laten gaan om het aan je voor te stellen.


De meeste VPN-serviceproviders zoals ProtonVPN en Mullvad bieden de optie om met bitcoins te betalen, maar vereisen het aanmaken van een account en het kopen van een plan voor een langere of kortere termijn, wat misschien niet in ieders budget past.


LN VPN maakt on-demand VPN-gebruik voor slechts één uur mogelijk, dankzij de implementatie van Bitcoin-betalingen via de Lightning Network. Onmiddellijke en anonieme bliksembetalingen openen een wereld van mogelijkheden voor microbetalingen.


Opmerking💡: **Deze handleiding beschrijft hoe u LN VPN kunt gebruiken vanaf een Linux Ubuntu 22.04 LTS-systeem.**


## Vereisten: Wireguard


Eenvoudig gezegd wordt Wireguard gebruikt om een veilige tunnel te creëren tussen jouw computer en de externe server waarmee je op het internet surft. Het IP Address van deze server verschijnt als het jouwe voor de duur van de lease die je Contract door het volgen van deze handleiding.


Officiële Wireguard installatiegids: https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## Vereisten: Bliksem Bitcoin Wallet


Als je nog geen Lightning Bitcoin Wallet hebt, geen zorgen, we hebben hier een heel eenvoudige gids voor je gemaakt. (de LN tutorial sectie kan je helpen)


## Stap 1: Contract een leasecontract


Op https://lnvpn.com moet je het land van het uitgangs-IP van de VPN-tunnel en een duur selecteren. Zodra deze parameters zijn ingesteld, klikt u op Betalen met bliksem.


![image](assets/1.webp)


Er verschijnt een bliksemschicht Invoice en je hoeft hem alleen maar te scannen met je bliksemschicht Wallet.


Zodra de Invoice is betaald, moet u enkele seconden tot maximaal twee minuten wachten voordat uw Wireguard-configuratie-instellingen worden gegenereerd. Als het iets langer duurt, geen paniek, we hebben deze procedure tientallen keren uitgevoerd en soms duurt het gewoon iets langer.

De volgende tekst is vertaald naar het Engels met behoud van dezelfde markdown lay-out als de originele tekst:


Het volgende scherm verschijnt en je hoeft alleen maar te klikken op "Download as File" om je configuratiebestand te ontvangen, dat een naam zal hebben die lijkt op lnvpn-xx-xx.conf waarbij "xx" overeenkomt met de huidige datum.

![image](assets/2.webp)


## Stap 2: Activeer de tunnel


Eerst moet je het config-bestand dat je in de vorige stap hebt verkregen een andere naam geven, zodat het automatisch wordt herkend door Wireguard.


Ga naar je downloadmap, in een terminalvenster of met de bestandsverkenner, en hernoem het lnvpn-xx-xx.conf bestand als volgt naar wg0.conf:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


Ziezo! De tunnel is geactiveerd!


## Stap 3: Controleer


Gebruik een online service zoals whatismyip om te controleren of je publieke IP Address nu die van de VPN is die je zojuist hebt geactiveerd.


## Stap 4: Uitschakelen


Wanneer uw leaseovereenkomst afloopt, moet u de verbinding uitschakelen om weer toegang te krijgen tot het internet. U kunt vervolgens stap 1 tot en met 3 herhalen wanneer u een lease wilt opzetten met LN VPN.


Schakel de tunnel uit:


```
$ sudo ip link delete dev wg0
```


Daar heb je het! Je weet nu hoe je LN VPN, een unieke VPN-dienst, kunt gebruiken!