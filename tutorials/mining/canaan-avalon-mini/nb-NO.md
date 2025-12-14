---
name: Canaan Avalon Mini 3
description: Konfigurere ASIC Avalon for solomining eller Miner-sammenslåing
---

![cover](assets/cover.webp)



I denne veiledningen tar vi en titt på hvordan du setter opp Canaan Avalon Mini 3, for enkel hjemmebruk av Miner.



Frem til nå har ASIC-maskiner (*Application Specific Integrated Circuit*) som er spesielt utviklet for å utføre en gitt oppgave - i dette tilfellet Hash-beregning (SHA-256) for Miner av Bitcoin - vært spesielt uegnet for hjemmebruk. Støy, varmeutvikling og behovet for å tilpasse det elektriske anlegget til den enorme kraften i disse maskinene har hindret de fleste av oss i å delta.



I dag har Canaan, en av de ledende produsentene av ASIC-maskiner, bestemt seg for å gå løs på markedet for privatpersoner som ønsker Miner hjemme, ved å tilby en rekke produkter som er relativt stillegående og svært enkle å installere (plug & play).



Disse enhetene markedsføres enten som en tilleggsvarmer, som **Avalon Nano 3S (140W)**, eller som en miniradiator med en effekt på **800W**, som **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Vær oppmerksom på at prisforskjellen i forhold til tradisjonelle ovner med tilsvarende effekt i de aller fleste tilfeller ikke gir deg mulighet til å tjene penger. Satoshiene som genereres av Minings aktivitet vil aldri kompensere for denne prisforskjellen, med mindre du har tilgang til gratis (overskudd) eller svært billig strøm.



Etter min mening bør disse enhetene sees mer som en enkel måte å Miner hjemme for de som ønsker å gjøre det av personlige grunner: *få ikke-KYC Satss / spille "lotteriet" ved å solominere / delta i Hashrate desentralisering etc..*. mens du drar nytte ** som en bonus ** fra varmen som genereres for å varme opp rommet ditt om vinteren. Men ikke som en måte å spare penger på i de fleste tilfeller i det minste (vestlige land).



## Unboxing og funksjoner



### Avalon Nano 3S



La oss først se hva som er inni Avalon Mini 3-esken.



![image](assets/fr/24.webp)



Når du åpner esken, ligger bruksanvisningen rett foran deg, men enda viktigere er det at WIFI-mottakermodulen er skjult under det runde, hvite klistremerket til venstre for bruksanvisningen. Du får bruk for den senere.



![image](assets/fr/25.webp)



Under skumblokken er enheten, og når den er tatt ut av esken, er strømforsyningen Supply-enheten.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Slå på strømmen og koble til det lokale nettverket



Når du har pakket ut Avalon Mini 3, plasserer du den i et relativt åpent område, om mulig, slik at varmen kan sirkulere skikkelig. Begynn deretter med å sette den lille WIFI-mottakermodulen inn i USB-porten på undersiden av enheten, koble til strømforsyningen Supply og sørg for at av/på-knappen står i posisjon "1".



![image](assets/fr/28.webp)



Når disse trinnene er fullført, lyser enhetens LED-display og viser "Bluetooth"-symbolet, noe som indikerer at den er klar til å kobles til ditt lokale nettverk via Avalon Family-applikasjonen.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Dette gjør du ved å gå til mobilapplikasjonsbutikken din, søke etter og laste ned **Avalon Family**-applikasjonen.



![image](assets/fr/11.webp)


Når du har installert programmet, åpner du det ved å klikke på "Hopp over" øverst i høyre hjørne, deretter på "Legg til"-knappen og til slutt på "Søk". Sørg for at du har Bluetooth aktivert på smarttelefonen din, slik at deteksjonen av enheten går greit.



![image](assets/fr/12.webp)


Når enheten har blitt oppdaget av programmet, klikker du på den og velger "Koble til". Du kommer da til et skjermbilde der du kan oppgi informasjon om WIFI-tilkoblingen din.


![image](assets/fr/13.webp)


Når Mini 3 er koblet til det lokale nettverket, vil den vise informasjon som IP Address, klokkeslett, Hashrate og strømforbruk.



Nedenfor finner du en oppsummeringstabell over Mini 3s generelle tekniske spesifikasjoner:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Koble til en Mining pool



**Denne delen er felles for Nano 3s og Mini 3-enhetene, ettersom prosessene er helt identiske**



Enten vi ønsker å "solominere" eller Miner-"pool", må vi koble oss til en Mining pool. Enheten vår er faktisk ikke noe annet enn en Hash-maker uten kjennskap til Bitcoin-nettverket. Ved å koble den til en pool får den tilgang til Bitcoin-nettverket, og kan motta blokkmaler som den kan jobbe med.



### Bruke applikasjonen til å koble til en Mining pool



I Avalon Family-applikasjonen velger du enheten som vist nedenfor. Du blir automatisk bedt om å endre maskinens administratorpassord. Klikk på "OK" hvis du ønsker å gjøre dette, eller på "Avbryt" for å beholde standardpassordet "admin".


![image](assets/fr/16.webp)


Velg deretter "Settings" og deretter "Pool Config", og angi parametrene for de tre ønskede bassengene.


Basseng nr. 2 og 3 fungerer som sikkerhetskopier hvis ett av dem skulle svikte, slik at Miner ikke fungerer til ingen nytte. Som standard vil Hashrate pekes til basseng #1



I vårt tilfelle velger vi:




- 1 - Offentlig basseng,
- 2 - CkPool,
- 3 - Havet.



![image](assets/fr/17.webp)



Hvis du vil ha mer informasjon om hvordan du kobler til en Mining pool, kan du se disse veiledningene :



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

For å oppsummere trenger vi





- bassenget Address, vanligvis **stratum+tcp://xxxxxxxx:port**.





- navnet på "arbeideren" som består av *din Bitcoin Address* og *pseudo* du velger for enheten din, de to atskilt med en *prik*, for eksempel:**bc1qxxxxxxxxxxxxxxxxxxx.MonAvalonNano3S**





- passordet, som vanligvis alltid er "**x**"



Når bassenginformasjonen er lagt inn, klikker du på "Lagre".



![image](assets/fr/18.webp)


Start enheten på nytt som anvist, og vent noen minutter til Hashrate er rettet mot det foretrukne bassenget (#1).



### Bruke nettleseren til å koble til en Mining pool



Du kan også koble deg til en Mining pool og, mer generelt, få tilgang til enhetens Interface-styringssystem via favorittleseren din.



Dette gjør du ved å skrive inn IP Address for enheten som vises på skjermen nedenfor, i vårt eksempel **192.168.144.6**, i nettleserens søkefelt



![image](assets/fr/15.webp)



Følgende side vises, der du blir bedt om å åpne Avalon Family-applikasjonen og skanne QR-koden som vises sammen med applikasjonen.



![image](assets/fr/20.webp)



Åpne applikasjonen, og klikk på de tre strekene øverst til høyre, og deretter på skann. Skann QR-koden i nettleseren, skriv deretter inn administratorpassordet for applikasjonen og klikk OK.



![image](assets/fr/21.webp)



Her er du på nettsiden som lar deg samhandle med Avalon. Det er mer et instrumentpanel for visning av maskinens beregninger enn en måte å konfigurere den på.



Men du kan fortsatt få tilgang til bassenginnstillingene på denne måten, ved å klikke på **"Pool Config"** nederst i høyre hjørne.



![image](assets/fr/22.webp)



På samme måte som med mobilapplikasjonen kan du legge inn bassengparametrene dine her.



![image](assets/fr/23.webp)



## Styr enheten din via Avalon Family-appen



Vi har nå koblet vår hjemme-Miner til vårt lokale nettverk, og rettet vår Hashrate mot Minings-bassenger. La oss nå oppdage de viktigste funksjonene til maskinen vår gjennom Avalon Family-applikasjonen.



I hovedmenyen i Avalon-familieapplikasjonen klikker du på ikonet som tilsvarer Avalon Mini 3. Du kommer da direkte til menyen for styring av driftsmoduser.



3 alternativer er tilgjengelige: "Heater"-modus, "Mining"-modus eller "Night"-modus.





- I "Heater"-modus har du to effektnivåer, "Eco" eller "Super".


"Eco"-nivået tilsvarer en varmeeffekt på 500 W for en Hashrate på ca. 25 Th/s og 40 dB for lydnivået.


"Super"-nivået tilsvarer en utgangseffekt på 650 W ved ca. 30Th/s og 45 dB. I denne modusen kan du stille inn en maksimal omgivelsestemperatur som gjør at enheten slutter å fungere.



![image](assets/fr/36.webp)




- I "Mining"-modus kjører enheten med maksimal hastighet, uten mulighet til å stille inn en måltemperatur (bortsett fra den innebygde overopphetingsgrensen, selvfølgelig). Målet er å få mest mulig ut av Miners ytelse. Her nærmer utgangseffekten seg 800 W ved rundt 37,5 Th/s og et støynivå på 50-55 dB.



![image](assets/fr/37.webp)


I "Night"-modus kjører Mini 3 med lavest mulig hastighet og minst mulig støy. 400 W, 20 Th/s og ca. 33 dB.



Også her kan du stille inn en måltemperatur over hvilken enheten går inn i inaktiv modus og stopper Miner. Hvis temperaturen synker, starter enheten på nytt og gjenopptar oppvarmingen og Miner. I denne modusen er lysdiodene i displayet slått av som standard, men du kan velge å slå dem på hvis det er nødvendig for å lyse opp rommet i mørket, som et nattlys (se bildet nedenfor).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Til slutt kan du leke med lysdiodene på Avalon via menyen "Display". Du kan velge å bla gjennom relevant driftsinformasjon, velge å vise klokkeslettet eller til og med et eget (pikselert) bilde.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Som med Avalon Nano 3S kan du i "Innstillinger"-menyen endre administratorpassordet, bassenginnstillingene, sjekke filterobstruksjon (plassert på undersiden av enheten), kontakte kundestøtte eller se enhetslogger.



![image](assets/fr/42.webp)



Igjen, filteret i bunnen av enheten kan rengjøres med en støvsuger, jo oftere jo bedre.



Vi har nå kommet til slutten av denne veiledningen, som har lært oss hvordan vi kobler Avalon Mini 3 til vårt lokale nettverk, hvordan vi peker Hashrate mot Mining-bassenger, og hvordan vi navigerer gjennom alternativer og innstillinger ved hjelp av Avalon Family-applikasjonen.



Hvis du vil vite mer, kan du ta en titt på veiledningen vår om den mindre versjonen av Avalon: Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6