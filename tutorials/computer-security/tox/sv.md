---
name: Tox
description: Öppna upp konversationer utan mellanhänder på det decentraliserade Tox-protokollet
---
![cover](assets/cover.webp)



End-to-end-kryptering är en tjänst som erbjuds av många meddelandeappar som WhatsApp och Telegram. Kryptering här innebär att innan meddelandet skickas av avsändaren, säkras det av ett kryptografiskt lås som endast mottagaren har nyckeln till. Idag ska vi upptäcka en helt decentraliserad, end-to-end-krypterad meddelandeapplikation, baserad på principer som liknar Blockchain, för att erbjuda säker, end-to-end-krypterad kommunikation utan mellanhänder: Tox Chat.



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

*E2EE = End-to-end-kryptering*



## Vad är Tox?



Tox är ett gratis (öppen källkod), decentraliserat kommunikationsprotokoll som använder NaCl-teknik (*Networking and Cryptography Library*) och kombinationer av krypteringsalgoritmer för att garantera användarnas säkerhet och sekretess. Med Tox kan du Exchange-textmeddelanden, ringa ljud- och videosamtal, dela filer och dela din skärm med vänner på ett säkert, decentraliserat sätt och utan mellanhänder.



Den teknik som Tox-protokollet använder liknar peer-to-peer-nätverk som blockkedjor, vilket gynnar decentraliseringen av protokollets infrastruktur. Till skillnad från sociala nätverk och end-to-end-krypterade meddelandeapplikationer bygger Tox Chat-applikationen på ett decentraliserat protokoll som inte har någon central server. Alla användare kommunicerar i ett censurresistent peer-to-peer-nätverk utan mellanhänder. För att kommunicera identifieras varje användare med ett unikt ID (ToxID) som härrör från hans eller hennes offentliga nyckel, som lagras i en distribuerad Hash-tabell.



## Ansluta sig till Tox



Du kan använda Tox-protokollet via en snabbmeddelandeklient som du kan ladda ner från [Tox Chat-webbplatsen] (https://tox.chat).



![download](assets/fr/01.webp)



Beroende på ditt operativsystem kan du ladda ner och installera en Tox-klient som matchar :





- aTox: [aTox](https://github.com/evilcorpltd/aTox), en Tox-klient skriven i Kotlin som endast är tillgänglig på Android



![aTox](assets/fr/02.webp)





- qTox: En Tox-klient från [öppen källkod] (https://github.com/TokTok/qTox) baserad på Qt Framework (C++) tillgänglig på Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) är en Tox-klient skriven i C och som körs på system med kommandoradsgränssnitt.



![Toxic](assets/fr/04.webp)



I den här handledningen använder vi qTox-klienter på Windows och aTox för att kommunicera.



## Komma igång med qTox



När du har laddat ner den installerar du din Tox-klient och skapar din profil.



![qTox-acount](assets/fr/05.webp)



Grattis, du har just anslutit dig till Tox-protokollet. I qTox-programvaran kan du hitta din profilinformation genom att klicka på ditt användarnamn.



![profil](assets/fr/06.webp)



Där hittar du bland annat ditt Tox-ID, som du kan spara som en QR-kod och dela med dig av till personer som vill komma i kontakt med dig.



Exportera din Tox-profilfil så att du har en säkerhetskopia av din profil och kontaktinformation som du kan använda för att återställa. Klicka på knappen **Exportera** och välj sedan sökvägen till din backup-fil.



![export](assets/fr/07.webp)



I menyn **More** kan du lägga till vänner, importera kontakter och hantera de vänförfrågningar du får.



![friends](assets/fr/08.webp)



Du kan nå mig via detta Tox ID till exempel: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



När vänförfrågan har skickats måste mottagaren acceptera eller avvisa din förfrågan innan du kan kontakta dem.



![request](assets/fr/09.webp)



Din Tox-klient innehåller alla de alternativ som erbjuds av applikationer för snabbmeddelanden:





- Videosamtal





- Röstsamtal





- Fildelning





- emojis



![chat](assets/fr/10.webp)



### Peer-to-peer-grupper



Med dina Tox-klienter kan du också kommunicera med en grupp människor på ett helt decentraliserat sätt: dessa kallas konferenser. I menyn **Grupper** skapar du en ny konferens eller tittar i listan över inbjudningar att delta i konferenser som du har fått.



![conferences](assets/fr/11.webp)



När konferensen har skapats kan du bjuda in dina vänner att delta i konferensen på din Tox-klient. Högerklicka på användarnamnet för den vän du vill bjuda in i din lista över vänner. Klicka på alternativet **Inbjud till konferens** och välj sedan det konferensnamn som du har skapat. Du kan också bjuda in en vän genom att implicit skapa en konferens med alternativet **Skapa en ny konferens**.



⚠️ Tox-klienter är fortfarande under utveckling, så du kan stöta på fel när du interagerar med programvaran. Konferens- och videosamtalsfunktioner är ännu inte tillgängliga på Tox Android-klient (aTox).



![invite](assets/fr/12.webp)



### Överföring av filer



I menyn **File transfers** hittar du en historik över de filer du har skickat och de du har tagit emot från dina kontakter.



![files](assets/fr/13.webp)



Du kan också anpassa konfigurationerna för fildelning för varje diskussion du har. Högerklicka på din mottagares användarnamn och välj "Visa mer information".



![details](assets/fr/14.webp)



Från Interface-detaljerna kan du hantera de behörigheter som du ger din mottagare för :





- Automatisk acceptans av konferensinbjudningar.





- Automatisk filacceptans.





- Sökvägar för säkerhetskopiering av dina diskussionsfiler.



![permissions](assets/fr/15.webp)



### Fler parametrar



I menyn **Settings** kan du anpassa inställningarna för din Tox-klient.





- I avsnittet **General** kan du ändra det grundläggande språket för din Tox-klient, definiera sökvägarna för säkerhetskopiering av filer och den maximala filstorlek som ska accepteras automatiskt.



![general](assets/fr/16.webp)





- I avsnittet **Interface-användare** kan du ändra typsnitt och storlek på dina meddelanden. Du kan också ändra temat för din Tox-klient.



![ui](assets/fr/17.webp)





- På fliken **Privacy** kan du definiera kortlivade meddelanden genom att avmarkera rutan "Keep chat history". Du kan också ändra din Nospam-kod när du märker att du blir spammad av vänförfrågningar genom att klicka på knappen "generate random NoSpam code".



![privacy](assets/fr/18.webp)



### Vad garanterar sekretess på Tox?



Tox-protokollet använder Distributed Hash Table för att skapa ett nätverk av decentraliserade noder. Varje Tox-klient är en del av DHT-nätverket och lagrar information om andra noder. När det gäller Tox lagrar DHT IP-adresser som värden som är associerade med Tox publika nycklar (Tox ID). Detta gör det enkelt att söka efter en Tox Client-enhet utan att behöva fråga en central server.



Föreställ dig att du skriver till vår användare `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` som vi kallar **användare B**. Din Tox-klient kommer att hitta den här identifieraren i Hash Distributed-tabellen och hämta den associerade IP Address. När IP Address har hittats kommer din Tox-klient att skapa en direkt, krypterad kommunikationskanal med vår **användare B**s maskin, eller använda andra noder som reläer för att nå **användare B**. Krypteringsalgoritmer säkerställer att, oavsett kommunikationskanal, endast **användare B** kan läsa innehållet i ditt meddelande.



Om du har tyckt om att upptäcka Tox och har kunnat förstå hur det är användbart för att stärka din integritet, får du gärna ge den här handledningen tummen upp. Vi rekommenderar också vår handledning om Simple Login, ett verktyg som låter dig ta emot och skicka e-post anonymt.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41