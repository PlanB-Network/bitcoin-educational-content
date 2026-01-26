---
name: White Noise
description: En privat, desentralisert meldingsapplikasjon basert på Nostr- og MLS-protokollene
---

![cover](assets/cover.webp)




## Innledning



"Midt i vanskelighetene ligger det muligheter". Dette sitatet fra Albert Einstein minner oss om at problemer ikke er endelige, men at de bærer i seg kimen til nye, innovative løsninger.



Motivasjonen bak lanseringen av løsningen vi presenterer i denne veiledningen, illustrerer dette perfekt. Det er **White Noise**, født av nødvendighet.



Som grunnleggeren Max Hillebrand uttrykker det, ifølge *Bitcoin Magazine*: "Vi lanserte dette prosjektet fordi det manglet alternativer." Han forklarer at "eksisterende krypteringsapplikasjoner er ineffektive i stor skala: Å legge til 100 personer i en gruppesamtale bremser krypteringen betraktelig. Desentraliserte plattformer tilbyr i mellomtiden ikke private meldinger. Nostrs åpne relénettverk gjør det mulig for alle å spre ideer, men beskyttelsen av direktemeldinger er fortsatt dramatisk utilstrekkelig. Vi innså at vi måtte slå sammen disse systemene for å beskytte friheten."



## Hva er White Noise?



White Noise er et meldingsprogram med åpen kildekode som er utviklet av et ideelt team. Programmet fremmer sikkerhet, personvern og desentralisering. I motsetning til konvensjonelle applikasjoner krever den verken telefonnummer eller e-postadresse.


White Noise kjennetegnes av integreringen av to grunnleggende protokoller - Nostr og MLS - som utgjør det tekniske grunnlaget.



Nostr (Notes and Other Stuff Transmitted by Relays) er en desentralisert protokoll med åpen kildekode som er utviklet for å motstå sensur.  Protokollen bruker reléer, nøkkelpar og klienter.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Med White Noise kan du til og med velge dine egne reléinnstillinger for å maksimere personvernet.



MLS (Messaging Layer Security) er derimot en sikkerhetsprotokoll som muliggjør ende-til-ende-kryptering av meldinger. Det vil si at meldingene bare er tilgjengelige ved endepunktene, det vil si avsenderen og mottakeren av meldingen. Det betyr at reléer som er involvert i ruting av meldinger, ikke har tilgang til innholdet.



Her er en rask sammenligning mellom White Noise og en rekke av de mest kjente meldingsapplikasjonene.





| Sammenligningspunkter       | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| E2EE-kryptering / 1:1       | ✅ Ja         | Valgfritt  | ✅ Ja             | ✅ Ja    | ✅ Ja     | ✅ Ja              | ✅ Ja   |
| Gruppe-E2EE-kryptering      | ✅ Ja         | ❌ Nei      | ✅ Ja             | ✅ Ja    | ✅ Ja     | Valgfritt         | ✅ Ja   |
| Anonymisering av identitet  | ✅ Ja         | Valgfritt  | ❌ Nei            | ✅ Ja    | ❌ Nei    | ❌ Nei             | ❌ Nei  |
| Åpen kildekode-server       | ✅ Ja         | ❌ Nei      | ❌ Nei            | ✅ Ja    | ❌ Nei    | ❌ Nei             | ✅ Ja   |
| Åpen kildekode-klient       | ✅ Ja         | ✅ Ja        | ❌ Nei            | ✅ Ja    | ❌ Nei    | ❌ Nei             | ✅ Ja   |
| Desentralisert server       | ✅ Ja         | ❌ Nei      | ❌ Nei            | ✅ Ja    | ❌ Nei    | ❌ Nei             | ❌ Nei  |
| Opprettelsesår              | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |

## Kom i gang med White Noise



### White Noise-installasjon



Gå til [White Noise-nettstedet](https://www.whitenoise.chat/), og klikk deretter på **Last ned**.



![screen](assets/fr/03.webp)



White Noise er for øyeblikket bare tilgjengelig på mobile enheter.


I det nye grensesnittet som vises, trykker du på :





- knappen **Zapstore** eller **Android APK** hvis du vil laste den ned på Android ;
- på **iOS TestFlight**-knappen hvis du bruker en iPhone.



![screen](assets/fr/04.webp)



I denne veiledningen skal vi utføre en Android-nedlasting.


Hvis du velger å laste ned via **Zapstore**, vil du bli omdirigert til den. Når du er på Zapstore, skriver du inn **White Noise** i søkefeltet. Fortsett deretter nedlastingen ved å klikke på **Install**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Hvis du velger å laste ned APK-filen, blir du omdirigert til White Noise GitHub-depotet for å velge riktig versjon for smarttelefonen din.



APK-filene som er tilgjengelige er :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), egnet for nyere telefoner med 64-biters prosessorer;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) passer for eldre telefoner med 32-biters prosessorer.



Du har også **.sha256**-filer, som bare er sjekksummer for å bekrefte integriteten til nedlastingen.



![screen](assets/fr/07.webp)



Når nedlastingen er fullført, installerer og åpner du programmet.



![screen](assets/fr/08.webp)



### Første oppsett av brukerkonto



For din første tilkobling til White Noise trykker du på **Register**-knappen.



![screen](assets/fr/09.webp)



Deretter konfigurerer du profilen din ved å velge et profilbilde, et navn og legge til en kort beskrivelse av deg selv. Du trenger ikke å fylle inn din virkelige identitet (navn og bilde).


Merk at White Noise automatisk velger et navn (pseudonym) for deg, som du kan beholde eller endre. Trykk til slutt på **Slutt**-knappen.



![screen](assets/fr/10.webp)



Du vil bli omdirigert til White Noises **hjemmeskjerm**, der samtalene dine vil bli listet opp. Kontoen din er nå satt opp og klar til bruk. Du kan dele profilen din eller søke etter venner for å starte en chat.



![screen](assets/fr/11.webp)




### Oppdage White Noise-grensesnitt



På hovedgrensesnittet, øverst på skjermen, ser du :



Øverst i venstre hjørne er profilikonet et miniatyrbilde av profilbildet ditt, eller den første bokstaven i profilnavnet ditt. Klikk på det for å få tilgang til kontoinnstillingene dine.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



Øverst i høyre hjørne finner du ikonet for å starte en ny samtale.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Innstillinger for brukerkonto



Trykk på profilikonet øverst i venstre hjørne for å få tilgang til innstillingene.



![screen](assets/fr/16.webp)



Øverst i **Innstillinger**-grensesnittet finner du bildet og profilnavnet ditt, etterfulgt av den offentlige nøkkelen din, som du kan dele ved hjelp av QR-koden ved siden av.



![screen](assets/fr/17.webp)



Rett nedenfor finner du knappen **Bytt konto**, som lar deg koble til en annen profil i programmet.



![screen](assets/fr/18.webp)



Deretter har du en første seksjon med fire (4) undermenyer, for eksempel :





- Endre profil**



I denne undermenyen kan du endre profilnavnet, Nostr-adressen (NIP-05)... Ikke glem å klikke på **Lagre** for å lagre endringene.



![screen](assets/fr/19.webp)





- Profilnøkler**



Her har du tilgang til dine offentlige og private (hemmelige) nøkler. Som White Noise minner om, skal den private nøkkelen ikke under noen omstendigheter avsløres.



![screen](assets/fr/20.webp)





- Nettrelé



I denne undermenyen kan du legge til eller fjerne **generelle reléer** (reléer som er definert for bruk i alle Nostr-applikasjonene dine), **inbox-reléer** og **nøkkelpakkereléer**.



Dette gjør du ved å trykke på **søppel**-ikonet foran et stafett for å slette det, eller ved å trykke på **+**-ikonet (pluss) for å legge til et nytt stafett.



![screen](assets/fr/21.webp)





- Frakobling**



Klikk på denne undermenyen for å koble kontoen din fra applikasjonen. Men sørg for at du har lagret de private nøklene dine offline, ellers vil du ikke kunne logge inn igjen senere.



![screen](assets/fr/22.webp)




En annen del inneholder undermenyer:





- Programinnstillinger



Her kan du definere utseendet (tema og visningsspråk) til applikasjonen, og du kan til og med slette data hvis du mener at de har blitt kompromittert, eller hvis du selv føler deg utsatt for risiko.



![screen](assets/fr/23.webp)





- Gi en gave til White Noise



Du kan støtte teamet bak White Noise (en ideell organisasjon) med donasjoner via deres Lightning-adresse eller deres Bitcoin-adresse for stille betaling.



![screen](assets/fr/24.webp)



Til slutt, helt nederst, finner du **utviklerinnstillingene**.



![screen](assets/fr/25.webp)




## Start en samtale



La oss nå ta en titt på hvordan du starter en samtale. I skrivende stund tilbyr White Noise tre kommunikasjonsalternativer. I tur og orden skal vi se nærmere på **Private samtaler** (**Chat 1:1**), dvs. mellom bare deg og én annen person, **Gruppesamtaler** og **Sending av multimediefiler**.




### Kat 1:1



For å legge til en ny korrespondent klikker du på ikonet for å starte en ny samtale fra hovedgrensesnittet.


Skann deretter QR-koden til den offentlige nøkkelen (1) eller lim inn den offentlige nøkkelen (2) til den nye korrespondenten din i søkefeltet for å finne ham eller henne.



![screen](assets/fr/26.webp)



Trykk deretter på knappen **Start samtale** for å starte en samtale med korrespondenten din. Du kan også **Følge** korrespondenten din eller invitere ham/henne til en gruppesamtale ved å trykke på knappen **Legg til i gruppe**.



![screen](assets/fr/27.webp)



Den første meldingen du sender til en ny korrespondent, er en slags invitasjonsforespørsel. Denne forespørselen må aksepteres av korrespondenten din før du kan kommunisere med ham/henne. Hvis vedkommende nekter, er det ikke mulig å føre noen samtale.



![screen](assets/fr/28.webp)



Så lenge de ikke aksepterer invitasjonen din, vil de heller ikke kunne lese innholdet i den første meldingen din.



Når han har akseptert invitasjonen din, kan han svare deg, og dere kan kommunisere sømløst og sikkert.



![screen](assets/fr/29.webp)



I en diskusjon har du dessuten flere funksjoner.



Du kan trykke lenge på en bestemt melding for å vise alternativer som f.eks:




- reagere på meldingen med en emoji (1) ;
- lag et **direkte sitat** for å svare på meldingen ved å trykke på **Reply** (2) ;
- kopier meldingen ved å trykke på **Kopier** (3).



![screen](assets/fr/30.webp)





- slett en melding med **Slett**-knappen bare hvis den kommer fra deg.



![screen](assets/fr/31.webp)



Du kan søke i en samtale.



Klikk på korrespondentens avatar øverst på skjermen for å få tilgang til "samtaleinformasjon", og trykk på knappen **Søk i samtale**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



I søkefeltet som vises, skriver du inn ordet du vil søke etter, og starter søket. Du vil da se søkeordene dine uthevet i **fet skrift**.



![screen](assets/fr/34.webp)




### Gruppesamtaler



Samtalegrupper kan opprettes på White Noise.



Dette gjør du ved å trykke på ikonet i oppstartsgrensesnittet for nye samtaler og deretter klikke på **Ny gruppesamtale**. Skriv deretter inn den offentlige nøkkelen til det første medlemmet du ønsker å legge til i gruppen, i søkefeltet.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Hvis dette alternativet ikke fungerer, kan du i grensesnittet **Start en ny samtale** skrive inn den offentlige nøkkelen til det første medlemmet du ønsker å legge til i gruppen, i søkefeltet. Du kan også skanne QR-koden som er knyttet til hans eller hennes offentlige nøkkel.



I stedet for å trykke på knappen **Start samtale**, klikker du denne gangen på knappen **Legg til i gruppe**.



![screen](assets/fr/37.webp)



Trykk på **Ny gruppesamtale** i popup-menyen som vises.



![screen](assets/fr/38.webp)



Trykk deretter på **Fortsett** (du trenger ikke å oppgi den offentlige nøkkelen på nytt).



![screen](assets/fr/39.webp)



Som oppretter av gruppen er du automatisk administrator. Fyll inn gruppedetaljene, for eksempel **gruppenavn og beskrivelse**, og klikk deretter på knappen **Opprett gruppe**.



![screen](assets/fr/40.webp)



Brukeren du legger til som første medlem, og alle andre du legger til senere, mottar et varsel der du inviterer dem til å bli med i gruppen. De må akseptere ved å klikke på **Accept** for å bli med i gruppen.



![screen](assets/fr/41.webp)



Det er også mulig å legge til et nytt medlem som du allerede chatter med, i en eksisterende gruppe. Dette gjør du ved å klikke på avataren til vedkommende øverst på skjermen for å få tilgang til "samtaleinformasjonen" og trykke på knappen **Legg til i gruppen**.



![screen](assets/fr/42.webp)



I det nye grensesnittet som vises, **krysser du av** for gruppen du ønsker å legge den til i, og trykker på **Legg til i gruppe**. Nå er det bare å vente på at den godtar å bli med i gruppen.



![screen](assets/fr/43.webp)



Merk at bare en gruppeadministrator kan endre gruppeinformasjon og legge til eller utvise medlemmer. Nøkkelrotasjon forhindrer også at utestengte medlemmer kan dekryptere fremtidige meldinger.



Hvis du vil fjerne et medlem, trykker du på gruppeikonet øverst i hovedgruppegrensesnittet for å få tilgang til grensesnittet for gruppeinformasjon.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Klikk deretter på medlemmets navn og **Fjern fra gruppen**. Fra dette grensesnittet kan du også sende en melding, følge ham eller legge ham til i en annen gruppe.



![screen](assets/fr/46.webp)



### Sende multimediefiler



For øyeblikket er det bare bilder som kan deles mellom brukere på White Noise. Enten du er i en privat samtale eller en gruppechat, må du :





- trykk på **pluss (+)**-symbolet på venstre side av inntastingsfeltet for tekstmeldinger.



![screen](assets/fr/47.webp)





- klikk deretter på boksen merket **Bilder** nederst for å få tilgang til galleriet ditt.



![screen](assets/fr/48.webp)





- velg bildet/bildene du vil sende.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Viktige punkter å huske på



White Noise tilbyr et godt konfidensialitetsnivå og overlegen sikkerhet. På den annen side er det et svært nytt program, ikke særlig utbredt og fortsatt i sin spede begynnelse. Derfor er det fortsatt for tidlig å trekke noen aktive konklusjoner. Det er mulig å støte på noen få funksjonsfeil under bruk.



For øyeblikket mangler den visse funksjoner (ingen lyd- eller videosamtaler, ingen sending av lyd- eller videomultimediefiler) sammenlignet med populære meldingsapplikasjoner.



White Noise er likevel et interessant alternativ for samtaler der konfidensialitet er viktig (f.eks. med familie, nære venner eller aktivister i en felles sak), selv om det krever litt innsats å installere (via alternative applikasjonsbutikker eller APK-filer) og lære seg (å mestre litt av konseptet med nøkkelpar, klienter og reléer med Nostr-protokollen).



Nå vet du hvordan du bruker White Noise til å kommunisere trygt med venner og familie. Gi oss en tommel opp hvis du synes denne veiledningen var nyttig.



Vi anbefaler vår veiledning om Tox Chat, et program som lar deg chatte uten mellomledd over den desentraliserte Tox-protokollen.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3