---
name: Breez - POS
description: Breez gjør det enkelt å samle inn bitcoin-betalinger for bedriften din.
---

![cover](assets/cover.webp)



Siden covid-19-pandemien har kontaktløse digitale betalinger blitt utbredt, selv i de minste butikkene. I løpet av denne perioden har mange bedrifter oppdaget det praktiske med bitcoin cash-løsninger, som gjør det mulig å motta betalinger fra hele verden. Disse løsningene er imidlertid noen ganger vanskelige å bruke eller uegnet for små bedrifter. I denne veiledningen tar vi en titt på betalingsterminalen Breez, en løsning som skiller seg ut ved at den er enkel å bruke, samtidig som den gir deg full kontroll over forvaltningen av bitcoinsene dine.



## Installer Breez POS



Breez POS er en selvforvaringstjeneste som leveres av Breez wallet. Formålet med denne tjenesten er å gjøre det mulig for kjøpmenn å samle inn betalinger via Bitcoin, samtidig som de forblir i et enkelt grensesnitt, veldig likt de ulike Lightning-lommebøkene. Breez POS er tilgjengelig på nedlastingsplattformene [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) og [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS).



![download](assets/fr/01.webp)



![setup](assets/fr/12.webp)



⚠️ Det er viktig å merke seg at disse programmene fortsatt er under utvikling, og at det kan være noen feil i bruken av funksjonene. Vi anbefaler moderat bruk.



Med denne applikasjonen gir Breez deg full kontroll over nettverkskonfigurasjoner og gebyrinnstillinger, samtidig som du garanterer din suverenitet i å administrere bitcoinsene dine.



Du kan utforske de ulike Breez wallet-alternativene ved å følge veiledningen nedenfor. Dette trinnet vil hjelpe deg med å forstå økosystemet på salgsstedet bedre og ta i bruk beste praksis for å effektivt sikre bitcoins knyttet til din seed.



https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Bruk av Breez POS



I denne veiledningen fokuserer vi på "*Point-of-Sale*"-delen for å hjelpe deg med å forstå hvordan du integrerer den som betalingsmiddel i virksomheten din.



Salgsstedet er en integrert del av Breez-porteføljen og er først og fremst avhengig av Lightning Network for å samle inn betalinger.



I menyen "*Point of Sale*" har du et direkte grensesnitt for innkreving av betalinger. Det er delt inn i to deler:



### Avtalegiro



Den første delen er direkte debiteringstastaturet. Dette grensesnittet er praktisk for å kreve inn hele beløpet når du kjenner kundens totale kjøp, eller når du ikke trenger en fast produktkatalog i virksomheten din (f.eks. frilanstjenester).



![keyboard](assets/fr/02.webp)



For å bruke Breez POS for første gang må du betale et beløp på over 2500 satoshier (rundt 3 euro etter dagens kurs). Dette beløpet, som kun betales ved første utbetaling, representerer kostnaden for å opprette en betalingskanal slik at du kan kommunisere med andre Lightning Network-noder og sende og motta satoshier.



![channel_fee](assets/fr/03.webp)


### Produktkatalog



Den andre delen er produktkatalogen. Dette grensesnittet er ideelt når du har en produktkatalog med forhåndsdefinerte priser. Her kan du forhåndskonfigurere produktene dine og deretter bruke dem til generate-fakturaer for å forbedre sporbarheten til kontantkvitteringene dine.



![items](assets/fr/04.webp)



Du kan konfigurere hver enkelt vare manuelt fra dette grensesnittet ved å klikke på "**Plus**"-knappen og deretter definere navn, pris og en identifikator for denne varen.



![add_items](assets/fr/05.webp)



Deretter kan du legge den til og definere antallet for å kreve inn den tilknyttede betalingen.



Når katalogen din er ganske stor, kan det bli komplisert å legge til produktene ett og ett. For dette formålet kan du i delen **Innstillinger > Innstillinger for salgssted** i menyen "Vareliste" automatisk importere og eksportere varelisten din fra CSV-filer.



![import](assets/fr/07.webp)



I den samme delen kan du definere gyldighetsperioden for lynfakturaene dine. Fra nå av har kundene `N` sekunder på seg til å betale for alle fakturaene dine, hvis ikke må du generere en ny lynfaktura.



![invoice_time](assets/fr/08.webp)



Som administrator kan du styrke sikkerheten til bitcoinsene dine ved å legge til et passord som kreves for alle utgående betalinger fra din wallet. Denne funksjonen er spesielt nyttig når du ikke er den eneste som administrerer uttaket ditt.



![manager](assets/fr/09.webp)



I menyen **Transaksjoner** finner du en liste over alle betalinger du har samlet inn. Du kan også filtrere resultatene over en bestemt periode ved å klikke på knappen **Kalender**.



![transactions](assets/fr/10.webp)



Du kan også se en daglig oversikt over salget og det totale innsamlede beløpet ved å klikke på knappen **Dokument**.



![summary](assets/fr/11.webp)



Du har nå en fullstendig forståelse av Breez-applikasjonen for sømløs integrering av Bitcoin i virksomheten din. Hvis du synes denne veiledningen var nyttig, anbefaler vi vår veiledning om be-BOP, en e-handelsplattform som lar deg ta imot betalinger i bitcoins og tjene penger på virksomheten din.



https://planb.academy/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa