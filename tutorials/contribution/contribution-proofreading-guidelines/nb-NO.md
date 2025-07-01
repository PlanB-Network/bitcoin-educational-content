---
name: Retningslinjer for korrekturlesing
description: Hvilke faktorer er det viktig å huske på når man korrekturleser på Plan ₿ Network?
---
![github](assets/cover.webp)


Velkommen til denne veiledningen om retningslinjene du bør følge når du korrekturleser innhold på Plan ₿ Network. Vi er glade for at du deler vårt mål om å oversette Bitcoin-materiell til så mange språk som mulig, for å hjelpe folk med å få kunnskap om hvordan det fungerer og hvordan det kan brukes i hverdagen.


Først og fremst kan du bidra til Plan ₿ Network [public repository](https://github.com/PlanB-Network/Bitcoin-educational-content) ved å skrive veiledninger, korrekturlese eksisterende innhold eller til og med foreslå å legge til et nytt språk på plattformen. Hvis du vil vite mer, kan du først bli med i [Telegram Group](https://t.me/PlanBNetwork_ContentBuilder) og skrive en kort presentasjon om deg og språkene du kan snakke.


Denne veiledningen er dedikert til bidragsytere som ønsker å korrekturlese innhold. De fleste av dem vet ikke så mye om [Github] (https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) eller [Markdown-språket] (https://www.markdownguide.org/basic-syntax/) som vi bruker på depotet, så det er viktig å dele litt innsikt i hva de må være oppmerksomme på når de utfører denne oppgaven.


Jeg har laget den etter å ha samlet de vanligste problemene som korrekturlesere støter på når de utfører oppgavene sine. Kom gjerne med flere forslag, da det kan hjelpe andre med å forbedre seg.


Før du går nærmere inn på detaljene, bør du først lese denne veiledningen om de praktiske handlingene du kan gjøre på Github, ved å forke Plan ₿ Network-depotet, legge inn endringer og sende PR-er:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6

## Hva er korrekturlesing?


Korrekturlesing er den siste gjennomgangen av en skriftlig tekst for å identifisere og rette opp feil i grammatikk, rettskriving, tegnsetting og formatering. Det sikrer at teksten er klar, sammenhengende og fri for feil før den publiseres eller sendes inn.


Når du gjennomfører denne typen oppgaver, er det viktig å følge betydningen på originalspråket (EN eller FR), men sørg for at teksten på det endelige språket er så flytende som mulig for en morsmålstalende.


## De første trinnene før korrekturlesing på Plan ₿ Network


Før du starter en ny korrekturlesingsoppgave, må du kunngjøre den i [Telegramgruppen] (https://t.me/PlanBNetwork_ContentBuilder) eller informere Plan ₿ Network-koordinatoren din, som vil åpne en dedikert [issue] (https://github.com/orgs/PlanB-Network/projects/3). Når du mottar lenken til saken, skriver du bare en kommentar om at du starter med korrekturlesingen av det aktuelle innholdet.

Dette systemet gjør det mulig for koordinatoren å holde oversikt over fremdriften i repoen, og det gjør det mulig å "kreve" innholdet av korrekturleseren, slik at man unngår at noen andre gjør dobbeltarbeid.

På selve problemet finner du lenker som tar deg direkte til innholdet du skal sjekke. Du kan klikke direkte på dem, eller enda bedre, du kan gå tilbake til din egen forked repo og jobbe direkte derfra.


Først og fremst må du ALLTID huske å synkronisere repoen din på "dev"-grenen. På denne måten vil innholdet alltid være oppdatert før du starter noen form for oppgave, og du vil ikke skape noen konflikter mellom gammelt og nytt materiale. Sørg for å klikke på "Synkroniser Fork" og "Oppdater gren".



![REVIEW](assets/en/1.webp)



Når du har synkronisert, kan du gå direkte til innholdet du er interessert i, og legge til en ny gren, som vist i denne [opplæringen] (https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Ellers kan du åpne en ny gren hvor du skal jobbe, ved å klikke på "Branches", som vist nedenfor.



![REVIEW](assets/en/2.webp)



På denne nye siden finner du alle filialene du allerede har åpnet, under tittelen "Dine filialer". Denne delen er veldig nyttig fordi den gjør det enkelt å finne stedet der du har endret noe innhold. Hvis du vil åpne en ny filial, kan du klikke på "Ny filial" øverst til høyre på siden.


![REVIEW](assets/en/3.webp)



Deretter får du opp et popup-vindu der du må skrive inn navnet på den nye filialen. I tilfellet nedenfor valgte jeg å kalle den "BTC101-FR". På denne måten vil jeg alltid huske at denne spesifikke grenen skal brukes til korrekturlesing av kurset BTC101 på fransk, og **jeg vil ikke bruke den til noen andre oppgaver**.


Jeg foreslår at du gjør det samme: Sørg for å åpne en ny gren hver gang du trenger å starte en ny oppgave.



![REVIEW](assets/en/4.webp)



Når du har opprettet denne nye grenen, må du klikke på den fra "Dine grener" på forrige side og begynne å jobbe med *.md*-filen som er relatert til det spesifikke innholdet (i mitt tilfelle vil jeg klikke på mappen "kurs", og undermappen BTC101, for å søke etter fr.md). Alle commits som er relatert til den spesifikke filen, må committes (lagres) i den samme grenen.


## Originalspråk eller oversettelse?


Når du korrekturleser innhold, er det viktig at du alltid sjekker den engelske (eller franske) originalversjonen. Vær oppmerksom på at vi oversetter ved hjelp av AI-verktøy, så det er ikke sikkert at gjengivelsen på målspråket er flytende eller forståelig for den endelige leseren.


Du må derfor gjerne gjøre justeringer i teksten og endre setninger hvis det er nødvendig. Målet vårt er å gjøre teksten så flytende som mulig, men alltid i tråd med den opprinnelige betydningen. Hvis du er i tvil om hvordan du skal behandle et bestemt ord, kan du spørre oversettelseskoordinatoren.


LLM-verktøy kan oversette noen ord relatert til Bitcoin bokstavelig, som Lightning Network, som for eksempel ville blitt "Rete Fulmine" på italiensk.


Det gjelder spesielt når det er snakk om svært tekniske ord. I slike tilfeller er det tilrådelig å beholde det opprinnelige engelske ordet på målspråket for å gjøre det tydeligere, med mindre språkreglene dine pålegger deg å oversette hvert eneste ord. I så fall bør du alltid undersøke om noen andre i Bitcoin-fellesskapet ditt allerede har oversatt det aktuelle ordet, og om det nå er mye brukt.



- En løsning kan være å sjekke på [BitcoinWiki] (https://en.Bitcoin.it/wiki/Main_Page) på målspråket ditt for å se om ordet ble oversatt eller ikke. Hvis det ikke er det, beholder du ordet på engelsk.



- Mitt råd er uansett å sette inn EN-ordet likevel, og deretter den tilsvarende betydningen på målspråket innenfor runde parenteser, etter skjemaet EN (LANG), eller omvendt. Eks. Address (indirizzo) eller indirizzo (Address).



- En annen god løsning er å beholde det opprinnelige ordet/uttrykket, og deretter opprette en hyperkobling som omdirigerer til [glossary](https://planb.network/en/resources/glossary) på planb.network. For å gjøre dette må du sette inn ordet/uttrykket i hakeparenteser, og lenken i runde parenteser, slik du kan se i eksempelet nedenfor:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


I det endelige resultatet (bildet nedenfor) vil du ikke se hele lenken, og ordet vil bli klikkbart.


![REVIEW](assets/en/5.webp)



Vær oppmerksom på at lenken til ordlisten du henter fra nettstedet, inneholder språkkoden etter ordet "network" (eksempel: ``https://planb.network/en/resources/glossary/UTXO``-> her kan du lese språkkoden "en"). I dette tilfellet fjerner du språkkoden fra lenken, som du så i boksen ovenfor. På denne måten vil systemet automatisk ta leseren til det språket han eller hun har valgt.


Innholdet på repoen er fullt av hyperkoblinger som disse ovenfor. Nå som du vet hva de betyr, må du passe på at du ikke sletter lenker som er lagt inn av forfatteren.


En annen ting relatert til ordgjengivelse er følgende. Hvis du finner "Plan ₿ Network" i teksten, skal du la det stå i sin opprinnelige form. Ikke oversett ordet "plan" eller ordet "nettverk". Dessuten skal du IKKE bruke artikkelen "The" når du introduserer Plan ₿ Network, og **betrakt det som en merkevare**.


Det samme gjelder "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", som også bør beholdes i sin opprinnelige form.


En siste kommentar til dette avsnittet: Som vi sa ovenfor, bruker vi AI-verktøy til å oversette innhold, og deretter ber vi om "menneskelig" inngripen for å sikre at alt er flytende og godt korrekturlest.


Hvis du korrekturleser ved hjelp av AI for størstedelen av teksten, vil vi helt sikkert legge merke til det, ettersom vi er kjent med de typiske setningsstrukturene som AI genererer. Hvis vi oppdager at du utelukkende har brukt AI til korrekturlesing, uten å gjøre vesentlige endringer, kan den endelige belønningen i Sats bli halvert!


## Strukturen til overskriftene


I markdown-språket begynner alle overskrifter (og avsnittstitler) med Hash-tegnet ``#``. Antallet Hash-tegn tilsvarer overskriftsnivået. En overskrift på nivå tre har for eksempel tre nummertegn før teksten (f.eks. `### Min overskrift`).


I kurs introduseres de viktigste delene med ett enkelt Hash-tegn, mens underdelene kan ha fra to til fire Hash-tegn. I opplæringsvideoer bruker vi normalt bare overskrifter med to Hash-tegn.



![REVIEW](assets/en/6.webp)


Pass på at du **ALDRI** sletter Hash-tegn før en tittel, ellers får du problemer med strukturen i teksten.


Samtidig må du **ikke** endre chapterID-delen som du kan se i bildet ovenfor, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` eller videoreferansene som ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::```.


Når vi setter inn ``#`` foran en tittel, blir den automatisk fet i forhåndsvisningen av emnet, så unngå å gjøre titlene fete når du retter dem.


I EN-versjonen av kurs har dessuten titler som har én eller to ``#``, alle ordene som begynner med store bokstaver, mens titler som begynner med tre eller fire, vanligvis ikke følger denne regelen. Hvis det er mulig, bør du sørge for at titlene på målspråket ditt følger denne strukturen.


## Den første delen av kursene


I begynnelsen av ethvert innhold finner du følgende statiske ord med små bokstaver: "navn", "beskrivelse", "mål". De brukes av nettstedet til å dekode selve innholdet, og er **alltid på EN**. Derfor må du IKKE oversette dem, ellers vil innholdet skape synkroniseringsproblemer. Sørg for å bare korrekturlese delen etter kolon, som oversettes automatisk av AI.



![REVIEW](assets/en/7.webp)



I den samme innledende delen beholder du formatet som det er. Ikke legg til noe i begynnelsen av teksten. Unngå f.eks. å legge til "tt" før bindestrekene, som i bildet nedenfor!



![REVIEW](assets/en/8.webp)


## Anbefalinger om format


Her finner du noen eksempler på formatproblemer du bør være oppmerksom på når du korrekturleser innhold på målspråket ditt.



- Vær oppmerksom på merkelig tegnsetting som "*" eller "**", som kan representere en dårlig gjengivelse av fet skrift-symbolet. På bildet nedenfor kan du se at stjernene bare er til høyre for ordet, noe som ser rart ut.


![REVIEW](assets/en/9.webp)



Sjekk alltid den engelske originalteksten for å se om det er meningen at en fet tekst skal være der. I dette tilfellet er det nok å legge til to stjerner i begynnelsen av ordet, slik at det vises riktig på nettstedet. I markdown-språket må du faktisk sette inn to stjerner ``**`` både før og etter ordet/setningen for å gjengi fet skrift (se eksempelet nedenfor).



![REVIEW](assets/en/10.webp)




- De samme problemene kan oppstå med symboler som $ og ````.

Sørg for å sjekke den opprinnelige språkfilen (ofte EN eller FR) for å se hvor disse symbolene skal være. Du kan alltid be koordinatoren om hjelp med dette.



- Hvis du finner sitater, bør du undersøke på nettet for å finne den riktige oversettelsen på ditt språk. Anførselstegn settes vanligvis inn etter symbolet ``>``.



![REVIEW](assets/en/11.webp)


## Korrekturlesing av quiz


Visste du at du også kan korrekturlese quizspørsmålene i hvert emne? Hvis du for eksempel vil korrekturlese quizene for BTC101 i IT, kan du åpne en egen gren og følge denne stien: "kurs" -> "BTC101" -> "quiz" Der finner du alle mappene som er dedikert til hvert spørsmål, sammen med den relaterte språkfilen i _yml_-format.


Igjen, sørg for at du er i en egen filial som du åpner spesielt for dette formålet, og informer alltid koordinatoren.


Når du har gjennomgått spørsmålet, må du sørge for å endre statusen "gjennomgått" fra "false" til "true", som vist i bildet nedenfor.


![REVIEW](assets/en/12.webp)


## Annen beste praksis


Hvis du trenger å søke etter bestemte ord i teksten, kan du klikke på ``CTRL+F``, og finn-erstat-delen vises. Denne delen er veldig nyttig når du trenger å hoppe til en bestemt del av teksten, eller du trenger å erstatte bestemte ord / setninger i batch, uten å bla gjennom hele innholdet.



![REVIEW](assets/en/13.webp)



Når du bruker "erstatt alt"-funksjonen, er det viktig å dobbeltsjekke resultatet for å sikre at lenker ikke også er endret. Hvis du for eksempel vil endre ordet "Bitcoin" til "Bitkoin" (noe som kan være nødvendig på enkelte språk), kan du bruke "erstatt alle"-funksjonen til å oppdatere alle forekomster i teksten. Vær imidlertid oppmerksom på at dette verktøyet også vil endre alle lenker som inneholder ordet, noe som potensielt kan føre til omdirigeringsproblemer.


I eksempelet nedenfor har korrekturleseren brukt funksjonen ovenfor til å erstatte "Satoshi" med "Satoshi(Sats)", og har også endret lenken til en veiledning som inneholder selve ordet. Som en konsekvens ble lenken ugyldig.


![REVIEW](assets/en/14.webp)


Hvis forfatteren legger inn en lenke som henviser til et Plan ₿ Network-kurs med veiledning, vil nettstedet automatisk opprette et "kort" som viser det relaterte miniatyrbildet. Sørg derfor alltid for at du har et mellomrom mellom teksten og selve lenken, ellers kan du se følgende feil på nettstedet.


![REVIEW](assets/en/15.webp)




En annen god fremgangsmåte du kan bruke når du er ferdig med korrekturlesingen og sender PR-en, er å gå tilbake til den opprinnelige saken som ble åpnet av koordinatoren, og kommentere den med "Korrekturlesing utført". Sørg for at du også legger inn lenken til PR-en din der.


## Konklusjon


For å oppsummere kan det å være klar over de vanligste korrekturleserfeilene virkelig hjelpe deg med å forbedre ferdighetene dine når du sjekker innhold. Det er lett å overse ting som kontekst eller konsistens, så det å oppdage disse feilene kan utgjøre en stor forskjell. Husk alltid at det kan være nybegynnere som leser disse kursene og veiledningene, så det er vårt ansvar å sørge for at de forstår innholdet fullt ut.


Takk for at du har lest denne veiledningen, og god fornøyelse med korrekturlesingen!