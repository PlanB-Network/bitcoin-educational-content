---
name: Alias Vault
description: Kraftig verktøy for å administrere passord, tofaktorautentisering og aliaser (med innebygd e-postserver) - også selvbetjent!
---

![cover](assets/cover.webp)



Personvern og sikkerhet på nettet er et tema som alle, uansett virksomhet, bør følge nøye med på.



Disse problemstillingene er dessuten en del av en verden i stadig endring: Stadig flere utviklere engasjerer seg i temaet, med implementeringer av etablerte løsninger og nye produkter.



Dette er tilfellet med **Leendert de Borst** og hans `Alias Vault`, et revolusjonerende verktøy (det første i sitt slag) som lar deg administrere og lagre passord, bruke passordoppføringer til å autentisere deg til webtjenester, administrere tofaktorautentisering, men viktigst av alt generate ekte _aliaser_, alt i en enkelt Interface.



**Men Alias Vault stopper ikke der**.



## Viktige funksjoner



Alias Vault fungerer i skyen på utviklerens servere eller selvhostet i sin egen infrastruktur, et alternativ som Docker-filer og image er tilgjengelig for å installere med en scipt. I tillegg til web Interface er utvidelser tilgjengelig for alle populære nettlesere, samt mobilapper for iOS og Android; sistnevnte kan også lastes ned fra F-Droid, utenom den offisielle Google Store.



I en Interface Alias Vault er:




- Gratis og åpen kildekode**
- Password Manager**, for å lagre alle komplekse passord. Ved hjelp av nettleserutvidelsen fullfører passordbehandleren pålogginger til nettsteder
- 2FA**, for å støtte tofaktorautentisering
- Alias-manager med innebygd e-postserver**: Alias Vault oppretter ikke aliaser som videresender e-post til en brukers postkasse, men oppretter faktiske alter-egoer med fornavn, etternavn, kjønn, brukernavn, passord og bursdag (hvis denne informasjonen er påkrevd).



En omfattende og grundig dokumentasjon er en del av pakken, som vil hjelpe nykommere med å oppdage dette kraftige verktøyet.



## Ingen personopplysninger!



Det starter som alltid fra nettstedet [aliasvault.net](aliasvault.net). Som nevnt kan Alias Vault brukes på egen server, eller fra utviklerens sky for å bli kjent med den før man går over til den selv-hostede løsningen.



Nettstedet har virkelig iøynefallende og godt vedlikeholdt grafikk, men de gode tingene kommer hvis du begynner å få tak i det: **opprett kontoen din**.



![img](assets/en/01.webp)



Til din enorme overraskelse vil du oppdage at Alias Vault ikke ber om personlig informasjon: alt du trenger for å opprette kontoen er et kallenavn, et ord som er kjent for deg, så lenge det er tilgjengelig. Godta vilkårene for bruk, velg ordet og fortsett.



![img](assets/en/02.webp)



Angi **`hovedpassordet`** nå, som er den viktigste informasjonen i hele det nye systemet ditt. Med dette ene passordet vil du faktisk være den eneste som kan få tilgang til/gjenfinne kontoen, ettersom det vil holde `hvelvet` kryptert på serveren som skal være vert for informasjonen din.



![img](assets/en/03.webp)



Fakta: Du har opprettet din egen passordbehandler og aliasbehandler, men uten å oppgi din egen fungerende, private e-post Address.



![img](assets/en/04.webp)



Alias Vault ønsker deg velkommen til et trygt, nytt, personlig, men også tomt rom. Og nå begynner vi å fylle det litt.



Hvis du allerede har en passordbehandler, kan du importere filen fra den du bruker, for å evaluere forskjellene med andre leverandører, eller kanskje eliminere aliasbehandleren slik at du kan administrere alt i ett og samme program.



![img](assets/en/05.webp)



Alias Vault er ekstremt enkelt: Du har én hovedside, som er `Home`, med to menyer:




- `Credentials`: som lar deg opprette og administrere identiteter og aliaser
- `Email`: en innboks der du kan sjekke innkommende meldinger for aliaser du har generert.



![img](assets/en/06.webp)



Det er opprettelsen av et første alias vi er interessert i å gjøre, så gå til øverst til høyre på siden og klikk på _+Nytt alias_.



![img](assets/en/07.webp)



I utgangspunktet ser menyen minimal ut, i tråd med filosofien til Alias Vault. For å oppdage funksjonene i denne funksjonen, klikk på _Create via advanced mode_.



![img](assets/en/08.webp)



Den øverste delen av det første skjermbildet kan du bruke til å importere passordopplysninger som du allerede bruker for tjenester du har abonnement på, eller som du bruker ofte på nettet.



Hvis du har aktivert tofaktorautentisering på noen (eller alle) av de ovennevnte tjenestene, kan du med Alias Vault også administrere denne ekstra Layer-sikkerheten ved å importere den "hemmelige nøkkelen". Alias Vault oppretter den `TOTP` som kreves for tilgang.



![img](assets/en/09.webp)



**Forsiktig**: I plassen som er reservert for e-postadressen Address, foreslår Alias Vault sitt eget domene som standard; for å bruke riktig Address som du tidligere har opprettet kontoer med, må du klikke på _Enter custom domain_, slik at du kan angi riktig domene etter `@`.



![img](assets/en/14.webp)



Den nederste delen av dette skjermbildet er det morsomste. Klikk på _Generate Random Alias_, så oppretter Alias Vault separate identiteter for deg for ulike behov, hver med sin egen postkasse, passord på et svært robust nivå, supplert med andre detaljer som kjønn, fødselsdato og et passende kallenavn.



![img](assets/en/10.webp)



Fra en tilhørende meny kan du endre innstillingene som påvirker genereringen av passord, for eksempel ved å velge bare små bokstaver og eliminere tegn som kan være tvetydige.



![img](assets/en/11.webp)



Du kan bruke alias-e-posten som foreslås av Alias Vault, eller endre domener ved å klikke på den tilhørende rullegardinmenyen.



![img](assets/en/12.webp)



Før du bruker denne e-posten til en påloggingstjeneste, kan du teste funksjonaliteten ved å sende en melding fra en egen Address til den nyopprettede postkassen.



![img](assets/en/13.webp)



**⚠️ ADVARSEL**: Mottak av e-post er mulig takket være Alias Vaults innebygde server, men dette lar deg bare motta e-post og ikke svare, eller bruke e-postboksen med de "konvensjonelle" funksjonene til en `alias`-tjeneste. Det skiller seg dermed sterkt fra Simple Login, Addy og andre plattformer som utelukkende er dedikert til denne typen tjenester. For eksempel på Simple Login kan du se den dedikerte opplæringen:



https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

For å slette et alias du har opprettet som en test, trenger du bare å logge deg inn på `Home`, deretter `Credentials` og klikke på identiteten du vil slette. Kommandoen _Delete_ vises i øvre høyre hjørne, og du kan gå videre.



![img](assets/en/16.webp)



## Nettleserutvidelse



Avhengig av hva du har behov for, kan du ty til nettleserutvidelsen, som finnes i de mest brukte nettleserne.



![img](assets/en/15.webp)



Den installeres slik du allerede har gjort med alle de andre utvidelsene, så jeg skal ikke gå nærmere inn på den detaljen.



Nettleserutvidelsen skal gjøre det enklere å logge på nettbaserte tjenester, eller å opprette nye alias etter behov: Hvis tjenesten er lagret blant Alias Vault-postene dine, gjør den automatiske utfyllingen det som trengs.



![img](assets/en/17.webp)



Den eneste forsiktighetsregelen er å kontrollere at Alias Vault er aktivt. Programmet har faktisk en standardinnstilling som gjør at det settes på pause etter en periode med inaktivitet. Dette er en svært nyttig funksjon **når du for eksempel må gå bort fra datamaskinen for å forhindre at noen andre får tilgang til kontoene dine**. En strømlinjeformet prosedyre gjør at du kan logge inn igjen ved å skrive inn "hovedpassordet", hvis den forrige økten fortsatt ligger i hurtigbufferen. Tiden for utlogging er en av parameterne du kan tilpasse, og du kan forkorte eller forlenge den i henhold til dine preferanser.



## Mobilapp



Som alle apper av denne typen med respekt for seg selv har Alias Vault en versjon for mobile enheter, både i Android- og iOS-miljøer. For Android kan du laste ned appen fra [F-Droid] (https://f-droid.org/packages/net.aliasvault.app/).



I skrivende stund (slutten av august 2025) anser mobilappen "automatisk utfylling" som en eksperimentell funksjon, og den fungerer bare på noen få nettsteder. Inntil den er fullt implementert, må du kopiere/lim inn data for å bruke Alias Vault på mobilen.



Når du har lastet ned appen fra butikken, logger du inn ved å oppgi brukeren og "hovedpassordet" som er opprettet i webappen.



![img](assets/en/18.webp)



Når du åpner "hvelvet" ditt, blir du spurt om du vil aktivere biometrisk kontrollert tilgang, en ekstra Layer-sikkerhet for å forhindre at andre får tilgang til passordene dine hvis de tilfeldigvis holder telefonen din.



![img](assets/en/19.webp)



Hvis du bestemmer deg for å konfigurere biometrisk kontroll, kan du fortsette. Hvis du hopper over trinnet og ombestemmer deg, kan du også konfigurere det senere fra _Settings_-menyen.



Når du er ferdig med å logge inn, vil du finne dataene du allerede har opprettet, synkronisert på nytt.



![img](assets/en/20.webp)



Mobilappen kan dirigeres til lenken til "hvelvet" som ligger på en egen server.



![img](assets/en/22.webp)



Og det er nettopp den selvbetjente versjonen vi skal se nærmere på i neste avsnitt.



## Selvhosting: full kontroll over dataene dine



Alias Vault er riktignok ikke den første passordbehandleren som lar deg distribuere tjenesten på infrastrukturen din. Det finnes andre, men noen har enten begrensninger eller er delvis lukket kildekode.



Muligheten er unik: **Slutt å være avhengig av eksterne tjenesteleverandører eller skyer, men bruk din egen lokale server til å beskytte og administrere passord, aliaser og ekstremt sensitiv informasjon knyttet til det hele**. Med Alias Vault kan du også få e-posttjenesten til å peke til din egen e-postserver for ekstra konfidensialitet.



Det er på tide å gå til [documentation] (https://docs.aliasvault.net/installation/) for å finne ut hvordan du går frem for å hoste Alias Vault selv.



![img](assets/en/23.webp)



Alias Vault kjører på Docker Compose, så det kreves minimal erfaring med Linux og Docker. Du kan begynne med den grunnleggende installasjonen og deretter fullføre med mer avanserte løsninger.



Serveren din må kjøre på en 64-biters maskin, med en Linux-distribusjon, 1 GB RAM og minst 16 GB lagringsplass. Versjonen av Docker (CE) må være minst 20.10 eller høyere, mens Docker Compose krever en versjon fra 2.0 og oppover.



Jeg bestemte meg for å prøve Alias Vault med en tynn klient, der DietPi er installert som en distribusjon, en Debian Bookworm-base, optimalisert til det vesentlige og som allerede kjører `Docker` og `Docker Compose`.



For å få litt orden, må du først opprette en katalog i hjemmet ditt, åpne `terminal` og lime inn kommandoen for å kjøre installasjonsskriptet.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Når installasjonen er fullført, finner du legitimasjonen din for tilgang:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Kontroller innholdet i katalogen etter installasjonen.



![img](assets/en/29.webp)



Bruk kommandoen for å starte Alias Vault:



``` Start alias-hvelv


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Betraktninger om kryptering og sikkerhet



![img](assets/en/32.webp)



I henhold til det Lanedirt sier på nettstedet, i dokumentasjonen og på Github, med Alias Vault ** all informasjon (komponenter) du plasserer på Alias Vault, forblir tett bundet til enheten, kryptert og utilgjengelig for alle som ikke kjenner "hovedpassordet" **.



Hovedpassordet er dermed det grunnleggende elementet i hele "hvelvet". Etter at det er lagt inn, behandles det med `Argon2id`-algoritmen, en Hard-minnefunksjon for nøkkelavledning, for å forhindre at hemmeligheten forlater enheten.



Alt forblir skjult, selv fra skyen eller hostingtjenestens leder. Faktisk kan du ikke få tilgang til brukerdetaljer fra administrasjonspanelet, du kan bare vite om de har opprettet aliaser, mottatt e-post og lite annet.



Alt lagret innhold krypteres og dekrypteres ved hjelp av kryptografiske nøkler avledet fra "hovedpassordet". **Kun krypterte data lagres på serveren, ingenting vises i klartekst**. Hvis en bruker glemmer eller mister hovedpassordet sitt, vil kontoen som er knyttet til det, gå tapt for alltid, siden serveren ikke har tilgang til innholdet i klartekst.



For den selvhostede versjonen finnes det et skript for å tilbakestille "hovedpassordet", men dette forhindrer ikke tap av data.



![img](assets/en/33.webp)



Siden Alias Vault er i _Beta_-stadiet, kan du få problemer med å få tilgang hvis du endrer/oppdaterer hovedpassordet. Jeg foreslår at du velger et robust og komplekst passord fra begynnelsen av, slik at du kan eksperimentere med tjenesten og til slutt bestemme deg for om du vil bruke den. Hvis du har problemer med å få tilgang til skyen etter at du har oppdatert passordet, kan du kontakte Alias Vault-support.



For å få en fullstendig forståelse av arkitekturen og sikkerheten i Alias Vault, anbefaler jeg på det sterkeste at du leser [denne siden] (https://docs.aliasvault.net/architecture/), som inneholder detaljer om kryptografien som ligger til grunn for driften.



## Veikart


Utviklerne har som mål at Alias Vault skal være modent og stabilt innen utgangen av 2025, slik at det er mulig å definere de fremtidige bruksegenskapene.



Alias Vault er og vil alltid forbli åpen kildekode og gratis, men sannsynligvis ikke ubegrenset som i beta. Noen betalte funksjoner er i ferd med å bli implementert, slik de allerede har blitt annonsert.



Det finnes team-/familieplaner og støtte for maskinvarenøkler, sistnevnte for autentisering med FIDO2 eller WebAuth.



## Hvem trenger Alias Vault



**Et verktøy som dette er ideelt for alle som setter personvern på nettet først**.



Identiteten din er etter all sannsynlighet kjernen i virksomheten du driver på nettet, og den må beskyttes på alle måter for å holde **denne** informasjonen unna tjenester, selskaper og meglere som er villige til å gjøre hva som helst for å få tak i nettatferden din.



Alias Vault gir deg full kontroll over legitimasjonen din, noe som reduserer eller eliminerer behovet for å stole på tredjeparter for å beskytte og kryptere de mest sensitive dataene dine.



Alias Vaults arkitektur og kryptografiske fasiliteter er ideelle for suverene enkeltpersoner, små og mellomstore bedrifter, utviklingsteam og alle entusiaster av **åpen kildekode**-applikasjoner. Hvis du faller inn i noen av disse kategoriene: ha det gøy med å oppdage Alias Vault.