---
name: LN VPN

description: Sett opp din VPN
---

![bilde](assets/cover.webp)

LN VPN er en tilpassbar VPN-tjeneste som kun aksepterer lynbetalinger. I dag skal jeg vise deg hvordan du bruker den og etterlater færre spor når du surfer på internett.

Det finnes mange kvalitetsleverandører av VPN-tjenester, og vi har gjennomført en omfattende anmeldelse i denne artikkelen (hyperlenke). LN VPN skiller seg imidlertid ut, og vi kunne ikke la være å introdusere den for deg.

De fleste VPN-tjenesteleverandører som ProtonVPN og Mullvad tilbyr muligheten til å betale med bitcoins, men krever at du oppretter en konto og kjøper en plan for en lengre eller kortere periode, noe som kanskje ikke passer for alles budsjett.

LN VPN muliggjør VPN-bruk på forespørsel for så kort som én time, takket være implementeringen av bitcoin-betalinger via lynnettet. Øyeblikkelige og anonyme lynbetalinger åpner opp en verden av muligheter for mikrobetalinger.

> 💡 Denne guiden beskriver hvordan du bruker LN VPN fra et Linux Ubuntu 22.04 LTS-system.

## Forutsetninger: Wireguard

Enkelt forklart brukes Wireguard til å opprette en sikker tunnel mellom datamaskinen din og den eksterne serveren som du vil surfe på Internett gjennom. Det er IP-adressen til denne serveren som vil vises som din for varigheten av leieavtalen du vil inngå ved å følge denne guiden.

Offisiell Wireguard installasjonsguide: https://www.wireguard.com/install/

```
Wireguard-installasjon
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Forutsetninger: Lightning Bitcoin Wallet

Hvis du ikke har en Lightning Bitcoin-lommebok ennå, ikke bekymre deg, vi har laget en veldig enkel guide for deg her. (LN-opplæringsdelen kan hjelpe deg)

## Steg 1: Inngå en leieavtale

Fra https://lnvpn.com, må du velge landet for VPN-tunnelens utgangs-IP og en varighet. Når disse parameterne er satt, klikk på Betal med lyn.

![bilde](assets/1.webp)

En lynfaktura vil bli vist, og du trenger bare å skanne den med din lynlommebok.

Når fakturaen er betalt, må du vente noen sekunder til opptil to minutter for at dine Wireguard-konfigurasjonsinnstillinger skal genereres. Hvis det tar litt lenger tid, ikke få panikk, vi har gjort denne prosedyren dusinvis av ganger, og noen ganger tar det bare litt lenger tid.

Neste skjermbilde vil dukke opp, og du trenger bare å klikke på "Last ned som fil" for å motta din konfigurasjonsfil, som vil ha et navn som ser ut som lnvpn-xx-xx.conf hvor "xx" vil tilsvare gjeldende dato.
![bilde](assets/2.webp)

## Steg 2: Aktiver tunnelen

Først må du omdøpe konfigurasjonsfilen du fikk i forrige trinn slik at den automatisk kan gjenkjennes av Wireguard.

Gå til nedlastingsmappen din, enten i et terminalvindu eller med filutforskeren, og omdøp lnvpn-xx-xx.conf-filen til wg0.conf slik:

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

Der har du det! Tunnelen er aktivert!

## Steg 3: Verifiser

Bruk en nettjeneste som whatismyip for å verifisere at din offentlige IP-adresse nå er den fra VPN-en du nettopp aktiverte.

## Steg 4: Deaktiver
Når leieavtalen din utløper, må du deaktivere tilkoblingen for å gjenopprette tilgangen til internett. Du kan deretter gjenta trinn 1 til 3 hver gang du ønsker å etablere en leieavtale med LN VPN.
Deaktiver tunnelen:

```
    $ sudo ip link delete dev wg0
```

Der har du det! Du vet nå hvordan du bruker LN VPN, en unik VPN-tjeneste!