---
name: Picocrypt
description: Een open-sourcetool om je gegevens te versleutelen
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian BURNEL gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er zijn wijzigingen aangebracht in de oorspronkelijke inhoud.*



___



## I. Presentatie



In deze tutorial bekijken we Picocrypt, een eenvoudige, lichte en effectieve encryptiesoftware voor het versleutelen van gegevens met een hoog beveiligingsniveau.



Geschikt voor **het versleutelen van bestanden**, kun je het gebruiken om **data op je computer, op een USB-stick**, maar ook data opgeslagen in de Cloud** te beschermen. Je kunt bijvoorbeeld gegevens versleutelen en opslaan op **Microsoft OneDrive, Google Drive, iCloud of Dropbox**, hoewel ik voor dit doel de voorkeur geef aan een ander stuk software dat in een toekomstig artikel zal worden gepresenteerd.



Je kunt het ook gebruiken als je gegevens moet **delen met een derde partij**: dankzij Picocrypt en de decoderingssleutel kunnen zij de gegevens op hun machine ontsleutelen. Dus als je account of computer in gevaar komt, zijn je gegevens beschermd.



Om het Picocrypt project te volgen, is er maar één Address:





- [Picocrypt op GitHub](https://github.com/Picocrypt/Picocrypt)



PicoCrypt is volledig **gratis en open source** en is beschikbaar voor **Windows**, **Linux** en **macOS**. Onder Windows kun je het op je eigen machine installeren of de portable versie gebruiken.



## II. Picocrypt, open-source versleutelingssoftware



Picocrypt** encryptiesoftware presenteert zichzelf als **een alternatief** voor andere bekende oplossingen zoals **VeraCrypt** en **Cryptomator** (*ontworpen om gegevens te versleutelen op Cloud-omgevingen*), of **AxCrypt**. Trouwens, op de officiële GitHub van Picocrypt kun je een vergelijking vinden met enkele concurrenten:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Bron: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt is **zeer licht**, met een gewicht van slechts **3 MB**, en hoeft niet geïnstalleerd te worden: het is een **draagbare applicatie** met het voordeel dat er geen beheerdersrechten nodig zijn! Het verwaarloost echter de beveiliging niet, omdat het vertrouwt op **robuuste en betrouwbare algoritmen**:





- XChaCha20** versleutelingsalgoritme
- Functie voor toetsomleiding **Argon2**



Naast de voordelen die net zijn genoemd, is wat je echt aanspreekt **het gebruiksgemak**!



Het heeft maar één ding nodig: **een code-audit**, maar dat is gepland, zoals je kunt zien in de vergelijkingstabel hierboven (laatste regel). Maar omdat het open source is, houdt niets je tegen om de broncode te bekijken.



Ook al wordt het vergeleken met BitLocker in de bovenstaande tabel, **naar mijn mening zijn BitLocker en Picocrypt bedoeld voor verschillende doeleinden**: BitLocker voor het versleutelen van een compleet volume (dat van Windows, bijvoorbeeld) en Picocrypt voor het versleutelen van een boomstructuur of "Drive"-achtige opslagruimte.



## III. Picocrypt gebruiken



Voor deze demonstratie wordt een Windows 11-machine gebruikt.



### A. Gegevens versleutelen met Picocrypt



Allereerst moet je Picocrypt.exe downloaden van de officiële GitHub ([zie deze pagina](https://github.com/Picocrypt/Picocrypt/releases)).



Open de toepassing en de minimalistische Interface verschijnt op het scherm. Om gegevens te versleutelen, of het nu **een bestand, meerdere bestanden of een map** is, hoef je het alleen maar **sleep en zet het neer in Picocrypt's Interface**. Dit selecteert de gegevens die versleuteld moeten worden.



![Image](assets/fr/020.webp)



Vervolgens heb je voor gegevensversleuteling toegang tot verschillende opties, waaronder de versleutelingscode. Het kan **een sterk wachtwoord** zijn of **een encryptiesleutel in de vorm van een sleutelbestand**, of **beide**. Als we het voorbeeld van een wachtwoord nemen, heb je de keuze tussen het maken van je eigen wachtwoord, of het genereren van een wachtwoord met Picocrypt.



Dit wachtwoord moet sterk zijn, omdat het kan worden gebruikt om de gegevens te ontsleutelen. Voer het in onder "**Password**" en "**Confirm Password**" en klik dan op "**Encrypt**" om de gegevens te versleutelen! Daarvoor kun je klikken op de knop "**Wijzig**" naast "**Uitvoer opslaan als**" om de uitvoermap op te geven.



**Noot**: om een sleutel in bestandsformaat te gebruiken, klik je op "**Create**" rechts van "**Keyfiles**" om een sleutel te maken. Selecteer deze vervolgens door op "**Edit**" te klikken en het sleutelbestand naar het juiste gebied te slepen.



![Image](assets/fr/019.webp)



De twee geselecteerde bestanden zijn **versleuteld en gegroepeerd** in het bestand "**Encrypted.zip.pcv**", aangezien **PCV** de extensie is die Picocrypt gebruikt. Dit ZIP-bestand is onleesbaar dankzij de versleuteling. Om te voorkomen dat geselecteerde bestanden worden gegroepeerd in een enkel versleuteld ZIP-bestand, moet je de optie "**Recursief**" aanvinken, zodat er net zoveel versleutelde bestanden zijn als er bestanden zijn die moeten worden versleuteld.



Om toegang te krijgen tot onze gegevens, moeten we deze ontsleutelen met Picocrypt.



![Image](assets/fr/023.webp)



Voordat we het hebben over het ontsleutelen van gegevens, volgt hier wat informatie over enkele van de beschikbare opties:





- Paranoïde modus**: gebruik het hoogste beveiligingsniveau dat Picocrypt biedt. De tool gebruikt verschillende cascade-encryptie-algoritmen (XChaCha20 en Serpent) en HMAC-SHA3 in plaats van BLAKE2b voor gegevensauthenticatie.
- Reed-Solomon**: implementeer *Reed-Solomon* foutcorrectiecodes om foutcorrectie op beschadigde gegevens mogelijk te maken. Hiermee kunt u een corruptieniveau van ongeveer 3% van uw bestand ondersteunen.
- Splitsen in brokken** of **verdelen in meerdere delen**: als je een groot bestand versleutelt, kun je Picocrypt vragen om het in meerdere delen te splitsen. Dit kan de overdracht van het bestand vergemakkelijken.
- Bestanden comprimeren** of **Bestanden comprimeren**: bestanden comprimeren om de grootte van versleutelde bestanden te verkleinen.
- Verwijderde bestanden** of **Verwijderde bestanden**: verwijder bronbestanden om alleen de versleutelde versie te behouden



### B. Gegevens ontsleutelen met Picocrypt



Als je de gegevens moet ontsleutelen, is dat niet ingewikkelder dan versleutelen. Open gewoon Picocrypt en **sleep het PCV-bestand dat moet worden gedecodeerd**. Voer vervolgens het wachtwoord in en/of selecteer het sleutelbestand voordat je op "**Decrypt**" klikt.



![Image](assets/fr/021.webp)



Met de niet-versleutelde versie van het "Encrypted.zip" ZIP-archief kan ik nu mijn twee bestanden in duidelijke tekst herstellen!



![Image](assets/fr/022.webp)



## IV. Conclusie



**Je bent gewaarschuwd: Picocrypt is erg makkelijk te gebruiken, en het werkt! Hoewel de Interface minimalistisch is, bevat het een aantal zeer nuttige opties om encryptie aan te passen! En omdat het beschikbaar is in een draagbare versie, kun je het overal mee naartoe nemen, zodat je je gegevens met een gerust hart kunt ontsleutelen**



Zorg ervoor dat je sterke wachtwoorden gebruikt om gegevens te beschermen, en als je een sleutelbestand gebruikt, moet je niet vergeten daar een back-up van te maken, anders kun je de PCV container die door Picocrypt is gegenereerd niet meer ontsleutelen. Tot slot moet je weten dat er ook [een CLI versie](https://github.com/Picocrypt/CLI) is (met minder mogelijkheden) waarmee je Picocrypt vanaf de commandoregel kunt uitvoeren: ook hier opent Picocrypt de deur naar nieuwe mogelijkheden.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5