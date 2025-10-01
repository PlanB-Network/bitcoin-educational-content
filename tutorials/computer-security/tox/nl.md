---
name: Tox
description: Open gesprekken zonder tussenpersonen op het gedecentraliseerde Tox-protocol
---
![cover](assets/cover.webp)



End-to-end-encryptie is een dienst die wordt aangeboden door veel berichtenapps zoals WhatsApp en Telegram. Encryptie betekent hier dat voordat het bericht wordt verzonden door de verzender, het wordt beveiligd door een cryptografisch slot waarvan alleen de ontvanger de sleutel heeft. Vandaag gaan we op ontdekkingstocht naar een volledig gedecentraliseerde, end-to-end versleutelde berichtentoepassing, gebaseerd op principes die vergelijkbaar zijn met Blockchain, om veilige, end-to-end versleutelde communicatie aan te bieden zonder tussenpersonen: Tox Chat.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-endencryptie*



## Wat is Tox?



Tox is een gratis (open source), gedecentraliseerd communicatieprotocol dat gebruik maakt van *Networking and Cryptography Library* (NaCl) technologie plus combinaties van versleutelingsalgoritmen om de veiligheid en vertrouwelijkheid van de gebruikers te garanderen. Met Tox kun je veilig, gedecentraliseerd en zonder tussenpersonen Exchange tekstberichten versturen, audio- en videogesprekken voeren, bestanden delen en je scherm delen met vrienden.



De technologie die het Tox protocol gebruikt is vergelijkbaar met peer-to-peer netwerken zoals blockchains, wat de decentralisatie van de infrastructuur van het protocol bevordert. In tegenstelling tot sociale netwerken en end-to-end versleutelde berichtenapplicaties, is de Tox Chat-applicatie gebouwd op een gedecentraliseerd protocol dat geen centrale server heeft. Alle gebruikers communiceren in een intermediairvrij, censuurbestendig peer-to-peer netwerk. Om te communiceren wordt elke gebruiker geïdentificeerd door een unieke ID (ToxID) die is afgeleid van zijn of haar publieke sleutel, die is opgeslagen in een gedistribueerde Hash tabel.



## Word lid van Tox



U kunt het Tox protocol gebruiken via een instant messaging client die u kunt downloaden van de [Tox Chat site](https://tox.chat).



![download](assets/fr/01.webp)



Afhankelijk van je besturingssysteem kun je een Tox-client downloaden en installeren die overeenkomt met:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), een Tox-client geschreven in Kotlin die alleen beschikbaar is op Android



![aTox](assets/fr/02.webp)





- qTox: Een Tox-client van [open source](https://github.com/TokTok/qTox) gebaseerd op het Qt Framework (C++) beschikbaar op Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) is een Tox client geschreven in C en draait op systemen met commandoregelinterfaces.



![Toxic](assets/fr/04.webp)



In deze tutorial gebruiken we qTox clients op Windows en aTox om te communiceren.



## Aan de slag met qTox



Installeer na het downloaden je Tox-client en maak je profiel aan.



![qTox-acount](assets/fr/05.webp)



Gefeliciteerd, u bent zojuist lid geworden van het Tox-protocol. In de qTox-software kun je je profielinformatie vinden door op je gebruikersnaam te klikken.



![profil](assets/fr/06.webp)



Je vindt er met name je Tox ID, die je kunt opslaan als QR-code en kunt delen met mensen die contact met je willen opnemen.



Exporteer je Tox-profielbestand zodat je een back-up hebt van je profiel en contactgegevens die je kunt gebruiken om te herstellen. Klik op de knop **Exporteren** en kies vervolgens het pad naar je back-upbestand.



![export](assets/fr/07.webp)



In het menu **Meer** kunt u vrienden toevoegen, contacten importeren en de vriendschapsverzoeken die u ontvangt beheren.



![friends](assets/fr/08.webp)



Je kunt me bijvoorbeeld bereiken via deze Tox ID: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Zodra het vriendschapsverzoek is verzonden, moet de ontvanger je verzoek accepteren of afwijzen voordat je contact met hem of haar kunt opnemen.



![request](assets/fr/09.webp)



Je Tox client bevat alle opties die instant messaging applicaties bieden:





- Videogesprekken





- Spraakoproepen





- Bestanden delen





- emoji's



![chat](assets/fr/10.webp)



### Peer-to-peer groepen



Uw Tox clients stellen u ook in staat om met een groep mensen te communiceren op een volledig gedecentraliseerde manier: dit worden conferenties genoemd. Maak in het menu **Groepen** een nieuwe conferentie aan of raadpleeg de lijst met uitnodigingen voor conferenties die je hebt ontvangen.



![conferences](assets/fr/11.webp)



Zodra de conferentie is aangemaakt, kun je je vrienden uitnodigen om deel te nemen aan de conferentie op je Tox client. Klik in je vriendenlijst met de rechtermuisknop op de gebruikersnaam van de vriend die je wilt uitnodigen. Klik op de optie **Uitnodigen voor conferentie** en selecteer vervolgens de naam van de conferentie die je hebt aangemaakt. Je kunt ook een vriend uitnodigen door impliciet een conferentie aan te maken met de optie **Een nieuwe conferentie aanmaken**.



⚠️ Tox clients zijn nog in ontwikkeling, dus u kunt fouten tegenkomen wanneer u met de software werkt. Conferencing en videobellen zijn nog niet beschikbaar op de Tox Android client (aTox).



![invite](assets/fr/12.webp)



### Bestandsoverdrachten



In het menu **Bestandsoverdrachten** vindt u een overzicht van de bestanden die u hebt verzonden en ontvangen van uw contactpersonen.



![files](assets/fr/13.webp)



U kunt ook uw configuraties voor het delen van bestanden aanpassen voor elke discussie die u hebt. Klik met de rechtermuisknop op de gebruikersnaam van uw ontvanger en selecteer "Meer details weergeven".



![details](assets/fr/14.webp)



Vanuit de Interface details kunt u de autorisaties beheren die u aan uw ontvanger geeft voor:





- Automatisch accepteren van uitnodigingen voor conferenties.





- Automatische bestandsacceptatie.





- Backuppaden voor je discussiebestanden.



![permissions](assets/fr/15.webp)



### Meer parameters



In het menu **Instellingen** kun je de instellingen van je Tox client aanpassen.





- In de sectie **Algemeen** wijzigt u de basistaal van uw Tox client, definieert u de back-uppaden en de maximale bestandsgrootte die automatisch wordt geaccepteerd.



![general](assets/fr/16.webp)





- In het gedeelte **Interface gebruiker** kunt u de lettertypen en groottes van uw berichten aanpassen. U kunt ook het thema van uw Tox client wijzigen.



![ui](assets/fr/17.webp)





- Op het tabblad **Privacy** kun je efemere berichten definiëren door het vinkje bij "Chatgeschiedenis bewaren" uit te zetten. Je kunt ook je Nospam-code wijzigen als je merkt dat je wordt gespamd door vriendverzoeken door te klikken op de knop "generate willekeurige NoSpam-code".



![privacy](assets/fr/18.webp)



### Wat garandeert vertrouwelijkheid op Tox?



Het Tox protocol gebruikt de Distributed Hash Table om een netwerk van gedecentraliseerde knooppunten te creëren. Elke Tox client maakt deel uit van het DHT netwerk en slaat informatie op over andere nodes. In het geval van Tox slaat de DHT IP-adressen op als waarden die geassocieerd zijn met de openbare sleutels van Tox (Tox ID). Dit maakt het gemakkelijk om naar een Tox-clientapparaat te zoeken zonder een centrale server te hoeven raadplegen.



Stel je voor dat je naar onze gebruiker `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` schrijft, die we **gebruiker B** zullen noemen. Je Tox client zal deze identifier opzoeken in de Hash Gedistribueerde tabel en het bijbehorende IP Address ophalen. Zodra het IP Address is gevonden, zal jouw Tox client een direct, versleuteld communicatiekanaal creëren met de machine van **gebruiker B**, of andere knooppunten gebruiken als relais om **gebruiker B** te bereiken. Versleutelingsalgoritmen zorgen ervoor dat, ongeacht het communicatiekanaal, alleen **User B** de inhoud van uw bericht kan lezen.



Als je het leuk vond om Tox te ontdekken en je hebt kunnen begrijpen hoe het nuttig is om je privacy te versterken, geef deze handleiding dan gerust een duimpje omhoog. We raden ook onze tutorial over Simple Login aan, een tool waarmee je anoniem e-mails kunt ontvangen en versturen.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41