---
name: Satodime
description: Finn ut hvordan du bruker Satodime med mobilapplikasjonen
---
![cover](assets/cover.webp)



Denne veiledningen tar deg gjennom installasjon, konfigurasjon og bruk av Satodimes mobilapplikasjon. Du lærer hvordan du tar kortet ditt i besittelse, oppretter safer, legger til penger, opphever forseglingen og gjenoppretter de private nøklene dine. Vedleggene inneholder ressurser, beste praksis og tekniske forklaringer.



## Innledning



**Satodime**, utviklet av **[Satochip](https://satochip.io/fr/)**, er et sikkert bærerkort for lagring av Bitcoin på en håndgripelig og enkel måte. Det fungerer som en selvforvaltende Hardware Wallet, der du har full kontroll over de private nøklene dine uten å være avhengig av en tredjepart. Det er åpen kildekode og EAL6+-sertifisert, og støtter opptil tre uavhengige safer.



### Produktbakgrunn



Satodime, et **carte au porteur, tilhører den som fysisk besitter det**, uten behov for forhåndsregistrering eller identifikasjon. Det oppfyller behovet for sikker, bærbar Bitcoin-lagring, slik at alle som har kortet, kan bruke det eller overføre bitcoins ved å skanne det via mobilappen for å ta det i besittelse eller låse opp safer. I motsetning til en papirseddel bruker kortet en sikker chip for å Seal de private nøklene, som først avsløres etter at forseglingen er åpnet, noe som gjør at kortet ligner på kontanter der Ownership bestemmes av fysisk besittelse. Kortet er ideelt for å gi bort bitcoins som gaver, og muliggjør sikker overføring av bitcoins fra hånd til hånd, samtidig som mobilapplikasjonen utnytter NFC for tilgjengelig interaksjon med smarttelefonen.





- Sikkerhet**: Private nøkler generert og lagret i den sabotasjesikre brikken; synlig status (forseglet, uforseglet, tom).
- Funksjoner**: Kjøp bitcoins direkte via appen (Paybis-partner); administrer Mainnet og Testnet.
- Åpen kildekode**: Kode under AGPLv3-lisens, verifiserbar på GitHub.



### Kontinuerlig utvikling



Programmet utvikles regelmessig. Sjekk Satochips nettsted eller butikker for oppdateringer. For eksempel kan nye blokkjeder eller kjøpsfunksjoner bli lagt til. Sjekk [Satochip GitHub] (https://github.com/Toporin/Satodime-Applet) for løpende utvikling.



## 1. Forutsetninger



Før du begynner å bruke **Satodime**, må du sørge for at du har følgende utstyr:





- Kompatibel smarttelefon**: Android- eller iOS-enhet med NFC-aktivering.
- Satodime**-kort: Nytt eller uinitialisert.
- Internett-tilkobling**: For å laste ned appen.
- Grunnleggende kunnskap**: Forståelse av private/offentlige nøkler og risikoen for tap (irreversible).
- Sikkert medium**: Et sikkert sted å oppbevare private nøkler når de er åpnet (papir, metall; aldri digitalt).



## 2. Installasjon





- Last ned søknaden** :
 - [App Store] (https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store] (https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Sjekk utvikleren (Satochip) for å unngå svindel.
 - Satodime er **åpen kildekode**. Kildekode : [Satochips GitHub] (https://github.com/Toporin/Satodime-Applet).





- Installer og start applikasjonen**: Aktiver NFC på telefonen om nødvendig.



![image](assets/fr/01.webp)



## 3. Opprinnelig konfigurasjon



### 3.1 Start programmet og skann



Åpne appen og følg veiviseren. Plasser Satodime-kortet på telefonens NFC-leser (vanligvis på baksiden). Hold det nede under hele operasjonen for å sikre en stabil tilkobling.





- Hvis NFC ikke fungerer, må du sjekke telefonens innstillinger.
- En skål bekrefter suksessen: "Vellykket lesning".



![image](assets/fr/02.webp)



Som en generell regel vil **alle følgende operasjoner kreve bekreftelse ved å skanne Satodime-kortet**



### 3.2 Overtakelse av kortet (*Ownership*)



Ved første gangs bruk må du bli eier av kortet for å sikre det:





- Klikk på "*Take Ownership*" i appen.
- Bekreft operasjonen: Dette genererer en unik eiernøkkel.
- Skann kartet på nytt for å bruke endringene.
- Advarsel**: Dette trinnet er irreversibelt. Vennligst se [artikkelen *Ownership*] (https://satochip.io/satodime-Ownership-explained/).



![image](assets/fr/03.webp)




## 4. Skap en trygg



Satodime støtter opptil 3 safer. Opprett en for å lagre Bitcoin :





- Velg en tom safe (f.eks. Safe 01).
- Velg Blockchain (Bitcoin).
- Klikk på "*Opprett og Seal*".
- Skann kortet til generate og Seal den private nøkkelen (ukjent inntil den er åpnet).
- Gratulerer**: Safen din er nå forseglet og klar til å motta penger.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Legg til midler



Når safen er forseglet, fyller du den med bitcoins:





- Velg safen.
- Klikk på "*Legg til midler*".
- Kopier den offentlige Address eller skann QR-koden.
- Send midler fra en annen Wallet.
- Kontroller saldoen etter bekreftelse på Blockchain.
- Mulighet for kjøp: Klikk på "*Kjøp*" for å kjøpe direkte via Paybis (Visa, Mastercard osv.). Gjeldende avgifter.



![image](assets/fr/06.webp)



## 6. Åpne en safe



For å få tilgang til den private nøkkelen og overføre pengene til et annet sted, åpner du safen:





- Velg den forseglede safen.
- Klikk på "Fjern forseglingen".
- Bekreft advarselen: Denne operasjonen er irreversibel.
- Skann kortet for å åpne forseglingen.
- Safen er satt til "*Unsealed*"; den private nøkkelen kan nå vises/eksporteres.
- Advarsel**: Når forseglingen er åpnet, er den private nøkkelen tilgjengelig. Hvis noen tar smarttelefonen din, kan de få tilgang til denne nøkkelen og dermed få tilbake pengene i safen din (irreversibelt).



![image](assets/fr/07.webp)



## 7. Gjenopprett privat nøkkel



Etter at du har åpnet forseglingen, eksporterer du nøkkelen for bruk i en annen Wallet :





- Sørg for at du er i trygge omgivelser.
- Klikk på "*Vis privat nøkkel*".
- Velg format: Legacy, SegWit, WIF osv.
- Kopier nøkkelen eller skann QR-koden.
- Sikkerhet**: Del aldri den private nøkkelen din. Lagre den offline.
- Importer den til et Wallet-program som er kompatibelt med fondsforvaltning (f.eks. Sparrow wallet eller Electrum).



![image](assets/fr/08.webp)





## 8. Tilbakestill bagasjerommet



Hvis du tilbakestiller safen, slettes den tilhørende private nøkkelen irreversibelt. Med andre ord, hvis du ikke har sikret deg en kopi av den private nøkkelen eller importert den til en annen Wallet, vil en tilbakestilling av safen føre til et irreversibelt tap av midlene i den.



![image](assets/fr/09.webp)



Når du tilbakestiller bagasjerommet, blir sporet tomt og klart for en ny bagasjerom.



## 9. Overføring Ownership



For å - for eksempel - tilby bitcoins gjennom Satodime, må du :




- Ta Ownership av kortet,
- Opprett en Bitcoin safe,
- Overfør Satss dit,
- Overfør kort Ownership: Den neste personen som skanner kortet, blir eier av det,
- Gi Satodime-kortet til den personen du ønsker, og inviter vedkommende til å laste ned applikasjonen og deretter skanne kortet for å ta Ownership av det - og dermed få tilgang til bitcoinsene som er "lagret" på det.



![image](assets/fr/10.webp)




## VEDLEGG



### A1. Beste praksis



For å bruke **Satodime** sikkert :





- Sikre kortet**: Behandle det som kontanter; tap = tapte midler hvis det ikke er eieren.
- Sikkerhetskopiering av nøkler**: Etter at forseglingen er fjernet, skal private nøkler lagres på et sikkert fysisk medium. Aldri digitalt.
- Sjekk status**: Skann alltid for å bekrefte kort Ownership og status for forseglet/uforseglet safe.
- Konfidensialitet**: Bruk nye adresser; unngå sentraliserte sentraler for overføringer.
- Oppdateringer**: Hold appen oppdatert via butikkene.
- Gjenoppretting**: Hvis kortet er tapt, men eies, er midlene på Blockchain. Bruk den private nøkkelen hvis den ikke er forseglet.



### A2. Ytterligere ressurser



Spesifikt for Satodime :




- [Satodime-produkt](https://satochip.io/fr/product/satodime/)
- [Mobilguide] (https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Network] (https://planb.network/) for veiledninger om selvoppbevaring, private nøkler osv.



**Gjenopprettingsfrasen din** :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tutorial om Satochip (merkets første produkt) :**



https://planb.network/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Seedkeeper-opplæringer:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Om Satochip



**Offisielle lenker** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub] (https://github.com/Toporin/Satodime-Applet)
- Støtte: info@satochip.io



**Satochip** er et belgisk selskap som utvikler maskinvare- og programvareløsninger for håndtering og lagring av bitcoins og andre kryptovalutaer. Selskapets flaggskip, Satochip Hardware Wallet, er et NFC-kort utstyrt med en EAL6+-sertifisert secure element. Sammen med Seedkeeper, en Mnemonic-frase- og hemmelighetshåndterer, og Satodime, et ihendehaverkort, tilbyr Satochip et omfattende utvalg som er skreddersydd for brukernes behov. Enhetene, som drives av programvare med åpen kildekode, har som mål å demokratisere sikkerheten på Bitcoin.