---
name: Picocrypt
description: Ett verktyg med öppen källkod för att kryptera dina data
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian BURNEL publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar har gjorts i det ursprungliga innehållet.*



___



## I. Presentation



I den här handledningen tittar vi på Picocrypt, en enkel, lätt och effektiv krypteringsprogramvara för att kryptera data med en hög säkerhetsnivå.



Passar för **kryptering av filer**, du kan använda den för att skydda **data på din dator, på ett USB-minne**, men också data som lagras i molnet. Du kan till exempel kryptera data och lagra dem på **Microsoft OneDrive, Google Drive, iCloud eller Dropbox**, men för detta ändamål föredrar jag en annan programvara som kommer att presenteras i en framtida artikel.



Du kan också använda den när du behöver **dela data med en tredje part**: tack vare Picocrypt och dekrypteringsnyckeln kommer de att kunna dekryptera data på sin maskin. Så om ditt konto eller din dator utsätts för intrång är dina uppgifter skyddade.



För att följa Picocrypt-projektet finns det bara en Address:





- [Picocrypt på GitHub] (https://github.com/Picocrypt/Picocrypt)



PicoCrypt är helt **fritt och med öppen källkod** och finns tillgängligt för **Windows,** **Linux** och **macOS**. På Windows kan du installera det på din egen maskin eller använda den bärbara versionen.



## II. Picocrypt, krypteringsprogramvara med öppen källkod



Krypteringsprogrammet Picocrypt** presenterar sig som **ett alternativ** till andra välkända lösningar som **VeraCrypt** och **Cryptomator** (*utformade för att kryptera data i molnmiljöer*), eller **AxCrypt**. Förresten, på Picocrypts officiella GitHub, kan du hitta en jämförelse med några konkurrenter:



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

Källa: [Github.com] (https://github.com/Picocrypt/Picocrypt)



Picocrypt är ** mycket lätt**, väger bara ** 3 MB ** och behöver inte installeras: det är en ** bärbar applikation ** med fördelen att den inte kräver administratörsrättigheter! Det försummar dock inte säkerheten, eftersom det förlitar sig på **robusta och pålitliga algoritmer**:





- XChaCha20** krypteringsalgoritm
- Funktion för förbikoppling av nyckel **Argon2**



Utöver de fördelar som just nämnts är det som verkligen lockar **den enkla användningen**!



Den behöver bara en sak: **en kodgranskning**, men det är planerat, som du kan se i jämförelsetabellen ovan (sista raden). Men eftersom det är öppen källkod finns det inget som hindrar dig från att ta en titt på källkoden.



Även om det jämförs med BitLocker i tabellen ovan, ** enligt min mening är BitLocker och Picocrypt avsedda för olika användningsområden**: BitLocker för kryptering av en komplett volym (t.ex. Windows) och Picocrypt för kryptering av en trädstruktur eller ett lagringsutrymme av typen "Drive".



## III. Använda Picocrypt



För denna demonstration kommer en Windows 11-maskin att användas.



### A. Kryptering av data med Picocrypt



Först och främst måste du ladda ner Picocrypt.exe från den officiella GitHub ([se den här sidan](https://github.com/Picocrypt/Picocrypt/releases)).



Öppna programmet för att visa dess minimalistiska Interface på skärmen. För att kryptera data, oavsett om det är **en fil, flera filer eller en mapp**, är det bara att **dra och släppa den i Picocrypts Interface**. Detta kommer att välja de data som ska krypteras.



![Image](assets/fr/020.webp)



När det gäller datakryptering har du tillgång till flera alternativ, bland annat krypteringsnyckeln. Det kan vara **ett starkt lösenord** eller **en krypteringsnyckel i form av en nyckelfil**, eller **båda**. Om vi tar exemplet med ett lösenord kan du välja mellan att skapa ditt eget lösenord eller att generera ett lösenord med Picocrypt.



Detta lösenord måste vara starkt, eftersom det kan användas för att dekryptera data. Ange det under "**Password**" och "**Confirm Password**" och klicka sedan på "**Encrypt**" för att kryptera data! Innan dess kan du klicka på knappen "**Ändra**" bredvid "**Spara utdata som**" för att ange utdatakatalogen.



**Anmärkning**: För att använda en nyckel i filformat, klicka på "**Create**" till höger om "**Keyfiles**" för att skapa en nyckel. Välj den sedan genom att klicka på "**Edit**" och dra och släppa nyckelfilen på lämpligt område.



![Image](assets/fr/019.webp)



De två valda filerna är **krypterade och grupperade tillsammans** i filen "**Encrypted.zip.pcv**", eftersom **PCV** är det tillägg som används av Picocrypt. Denna ZIP-fil är oläslig tack vare krypteringen. För att förhindra att utvalda filer grupperas i en enda krypterad ZIP-fil måste du markera alternativet "**Recursively**", så att det finns lika många krypterade filer som det finns filer som ska krypteras.



För att komma åt våra data måste vi dekryptera dem med hjälp av Picocrypt.



![Image](assets/fr/023.webp)



Innan vi talar om dekryptering av data, här är lite information om några av de tillgängliga alternativen:





- Paranoidläge**: använd den högsta säkerhetsnivån som Picocrypt erbjuder. Verktyget kommer att använda flera kaskadkrypteringsalgoritmer (XChaCha20 och Serpent) och HMAC-SHA3 istället för BLAKE2b för dataautentisering.
- Reed-Solomon**: implementera *Reed-Solomon* felkorrigeringskoder för att underlätta felkorrigering av skadade data. Detta gör att du kan stödja en korruptionsnivå på cirka 3% av din fil.
- Dela upp i bitar** eller **dela upp i flera delar**: Om du krypterar en stor fil kan du be Picocrypt att dela upp den i flera delar. Detta kan göra filen lättare att överföra.
- Compress Files** eller **Compress files**: komprimera filer för att minska storleken på krypterade filer.
- Deleted files** eller **Fichiers supprimés**: ta bort källfiler för att bara behålla den krypterade versionen



### B. Dekryptering av data med Picocrypt



Om du behöver dekryptera data är det inte mer komplicerat än att kryptera dem. Öppna helt enkelt Picocrypt och **dra och släpp PCV-filen som ska dekrypteras**. Ange sedan lösenordet och/eller välj nyckelfilen innan du klickar på "**Decrypt**".



![Image](assets/fr/021.webp)



Den okrypterade versionen av ZIP-arkivet "Encrypted.zip" gör det nu möjligt för mig att återställa mina två filer i klartext!



![Image](assets/fr/022.webp)



## IV. Slutsatser



** Du har blivit varnad: Picocrypt är mycket lätt att använda, och det fungerar! Även om Interface är minimalistisk innehåller den några mycket användbara alternativ för att anpassa kryptering! Och eftersom den finns i en bärbar version kan du ta den med dig vart du än går, så att du kan dekryptera dina data med tillförsikt**



Se till att använda starka lösenord för att skydda data, och om du använder en nyckelfil måste du komma ihåg att säkerhetskopiera den, annars kommer du inte längre att kunna dekryptera PCV-containern som genereras av Picocrypt. Slutligen bör du veta att det också finns [en CLI-version](https://github.com/Picocrypt/CLI) (med färre funktioner) som låter dig köra Picocrypt från kommandoraden: även här öppnar Picocrypt dörren till nya möjligheter.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5