---
name: Keet
description: Peer-to-peer chat
---
![cover](assets/cover.webp)



Keet is een instant messaging-applicatie die is ontworpen om zonder servers te werken. De applicatie, die in 2022 werd gelanceerd door Holepunch (een bedrijf dat wordt gefinancierd door Tether en Bitfinex), is volledig gebaseerd op een peer-to-peer netwerk en heeft een radicaal gedecentraliseerde aanpak: berichten, gesprekken en bestanden worden direct uitgewisseld tussen gebruikers, zonder tussenpersonen.



Keet versleutelt alle communicatie end-to-end en vraagt niet om persoonlijke gegevens. De registratie is anoniem en er is geen telefoonnummer of e-mailadres vereist. Naast het uitwisselen van tekstberichten biedt Keet videogesprekken van zeer hoge kwaliteit en onbeperkt bestanden delen. De applicatie kan daarom op een hybride manier worden gebruikt, voor zowel persoonlijk als professioneel gebruik.



![Image](assets/fr/01.webp)



Op dit moment (april 2025) is Keet niet volledig open-source. Een deel van de broncode is beschikbaar op [Holepunch's GitHub repository](https://github.com/holepunchto), met name de cryptografische en netwerkcomponenten, maar de client Interface is dat nog niet. Holepunch heeft echter zijn intentie aangekondigd om uiteindelijk de hele applicatie open-source te maken. Afhankelijk van wanneer je deze tutorial ontdekt, kan dit al gebeurd zijn.




| Application          | E2EE 1:1       | E2EE groups    | Anonymous registration | Open-source client license | Open-source server license | Decentralized server | Year of creation  |
| -------------------- | -------------- | -------------- | ---------------------- | -------------------------- | -------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                      | ❌                          | ❌                          | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optional) | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Telegram             | 🟡 (optional) | ❌              | 🟡                     | ✅                          | ❌                          | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                      | ❌                          | ❌                          | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                      | ✅                          | ✅                          | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                      | ✅                          | ❌                          | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                      | ✅                          | ✅                          | 🟡 (federated)      | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                      | ✅                          | N/A                        | 🟡 (via email)      | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                      | ✅                          | ✅                          | 🟡 (federated)      | 2014              |
| Session              | ✅              | ✅              | ✅                      | ✅                          | ✅                          | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                      | ✅                          | ✅                          | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                      | ✅                          | ❌                          | 🟡(no directory)     | 2019              |
| Keet                 | ✅              | ✅              | ✅                      | ❌                          | N/A                        | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                      | ✅                          | N/A                        | ✅                    | 2013              |

*E2EE = End-to-endencryptie*



## Keet installeren



Keet is beschikbaar op alle platforms. Je kunt de applicatie rechtstreeks downloaden in de app store van je telefoon:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



Op Android is het ook mogelijk om [te installeren via APK] (https://github.com/holepunchto/keet-mobile-releases/releases).



In deze tutorial concentreren we ons op de mobiele versie, maar [er zijn ook computerversies beschikbaar](https://keet.io/) (MacOS, Linux en Windows). Het is ook mogelijk om je account op meerdere apparaten te synchroniseren.



## Maak een account aan op Keet



Bij de eerste start kun je de presentatieschermen negeren.



![Image](assets/fr/02.webp)



Klik op de knop "*Ik ben een nieuwe gebruiker*".



![Image](assets/fr/03.webp)



Accepteer de gebruiksvoorwaarden en klik vervolgens op "*Snel instellen*".



![Image](assets/fr/04.webp)



Kies een naam of bijnaam en klik dan op "*Setup voltooien*".



![Image](assets/fr/05.webp)



Je profiel is nu aangemaakt. Klik opnieuw op "*Setup voltooien*" om af te ronden.



![Image](assets/fr/06.webp)



Je kunt je profiel op elk moment aanpassen via het tabblad "*Profiel*".



## Je Keet-account opslaan



Het eerste wat je moet doen met je nieuwe Keet account is je herstelzin opslaan. Dit is een reeks van 24 woorden waarmee je de toegang tot je account kunt herstellen in geval van verlies of verandering van apparaat. Deze zin geeft volledige toegang tot je account aan iedereen die hem kent, dus het is belangrijk om een betrouwbare back-up te maken en hem nooit vrij te geven.



Klik hiervoor op het tabblad "*Profiel*" rechtsonder in de Interface.



![Image](assets/fr/07.webp)



Ga dan naar het menu "*Instellingen*".



![Image](assets/fr/08.webp)



Selecteer "*Privacy en beveiliging*".



![Image](assets/fr/09.webp)



Klik vervolgens op "*Recovery phrase*".



![Image](assets/fr/10.webp)



Druk op de knop "*Zin weergeven*" om je herstelzin weer te geven. Kopieer het zorgvuldig en bewaar het op een veilige plaats.



![Image](assets/fr/11.webp)



## Berichten versturen met Keet



Om op Keet te communiceren, moet je "*Rooms*" aanmaken. Om dit te doen, klik je op het potloodpictogram rechtsboven in de Interface.



![Image](assets/fr/12.webp)



Selecteer "*Nieuwe groepschat*".



![Image](assets/fr/13.webp)



Kies een naam en beschrijving voor je "*Room*" en klik dan op "*Groepschat maken*".



![Image](assets/fr/14.webp)



Uw "*Room*" is nu aangemaakt. Klik op het "*+*" pictogram rechtsboven om deelnemers uit te nodigen.



![Image](assets/fr/15.webp)



Definieer de rechten die je aan nieuwe leden verleent via de uitnodigingslink, evenals de geldigheidsduur van de link. Klik vervolgens op "*generate uitnodigen*".



![Image](assets/fr/16.webp)



Keet zal generate een link geven om lid te worden van je "*Room*". Je kunt de link kopiëren en delen, of de QR-code laten scannen door de mensen die je wilt uitnodigen.



![Image](assets/fr/17.webp)



U kunt nu berichten en multimediabestanden gaan uitwisselen. Om een gesprek te starten, klikt u op het telefoonpictogram in de rechterbovenhoek.



![Image](assets/fr/18.webp)



Vanuit deze groep kun je ook privéberichten sturen naar een specifiek lid. Klik op de profielfoto van de groep en selecteer vervolgens het gewenste lid in het gedeelte "*Leden*".



![Image](assets/fr/19.webp)



Klik op de knop "*Stuur DM-verzoek*" en voer je bericht in.



![Image](assets/fr/20.webp)



Zodra het DM-verzoek is geaccepteerd, vind je dit contact op de startpagina, waar je privé met hem kunt praten.



![Image](assets/fr/21.webp)



## Synchroniseer je account op meerdere apparaten



Nu je weet hoe je Keet moet gebruiken en een account hebt, kun je Keet ook synchroniseren op een ander apparaat, zoals een computer. Om dit te doen, open je de applicatie op je mobiel, klik je op "*Profiel*" en ga je naar "*Instellingen*".



![Image](assets/fr/22.webp)



Ga dan naar het menu "*Mijn apparaten*".



![Image](assets/fr/23.webp)



Klik op "*Apparaat toevoegen*". Keet zal generate een link geven om een nieuw apparaat te synchroniseren. Kopieer deze link.



![Image](assets/fr/24.webp)



Installeer Keet op je tweede apparaat. Selecteer op het beginscherm de optie "*Ik ben een huidige gebruiker*".



![Image](assets/fr/25.webp)



Klik vervolgens op "*Link device*".



![Image](assets/fr/26.webp)



Plak de link van je eerste apparaat en klik op "*Start synchronisatie*".



![Image](assets/fr/27.webp)



Klik op het eerste apparaat op "*Confirm link devices*" om de verbinding te autoriseren.



![Image](assets/fr/28.webp)



Voltooi het proces op het tweede apparaat door op "*Link devices*" te klikken.



![Image](assets/fr/29.webp)



Je hebt nu toegang tot al je "*Room*" en gesprekken vanaf dit nieuwe apparaat.



![Image](assets/fr/30.webp)



Gefeliciteerd, je bent nu op de hoogte van het gebruik van Keet messaging, een geweldig alternatief voor WathsApp! Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duimpje achterlaat. Voel je vrij om deze tutorial te delen op je sociale netwerken. Hartelijk dank!



Ik raad ook deze andere tutorial aan, waarin ik je kennis laat maken met Proton Mail, een veel privacy-vriendelijker alternatief voor Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2