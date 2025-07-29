---
name: passphrase BIP39
description: Förstå hur en passphrase fungerar
---
![cover](assets/cover.webp)


## Vad är en BIP39 passphrase?


HD-plånböcker genereras vanligtvis från en Mnemonic-fras som består av 12 eller 24 ord. Denna fras är mycket viktig eftersom den gör det möjligt att återställa alla nycklar i en Wallet om dess fysiska medium (som t.ex. en Hardware Wallet) skulle gå förlorat. Den utgör dock en enda felkälla eftersom en angripare kan stjäla alla bitcoins om den komprometteras.


![PASSPHRASE BIP39](assets/notext/01.webp)


Det är här passphrase kommer in i bilden. Det är ett valfritt lösenord som du fritt kan välja och som läggs till Mnemonic-frasen i nyckelhärledningsprocessen för att förbättra Wallet:s säkerhet.


![PASSPHRASE BIP39](assets/notext/02.webp)


Var noga med att inte förväxla passphrase med din Hardware Wallet:s PIN-kod eller det lösenord som används för att låsa upp åtkomsten till din Wallet på datorn. Till skillnad från alla dessa Elements spelar passphrase en roll i härledningen av din Wallet:s nycklar. **Detta innebär att utan den kommer du aldrig att kunna återfå dina bitcoins


passphrase fungerar tillsammans med Mnemonic-frasen och ändrar seed från vilken nycklarna genereras. Även om någon får tag på din 12- eller 24-ordsfras kan de alltså inte komma åt dina pengar utan passphrase. **Genom att använda en passphrase skapas i princip en ny Wallet med olika nycklar. Om du ändrar (även lite) passphrase kommer generate att bli en annan Wallet.**


## Varför ska du använda en passphrase?


passphrase är godtycklig och kan vara vilken kombination av tecken som helst som användaren väljer. Att använda en passphrase har därför flera fördelar. För det första minskar den alla risker som är förknippade med att Mnemonic-frasen äventyras genom att det krävs en andra faktor för att få tillgång till pengarna (inbrott, tillgång till ditt hem etc.).


Därefter kan den användas strategiskt för att skapa en lockande Wallet, för att hantera fysiska begränsningar för att stjäla dina medel som den ökända "*$5 wrench attack*". I det här scenariot är tanken att ha en Wallet utan en passphrase som bara innehåller en liten mängd bitcoins, tillräckligt för att tillfredsställa en potentiell angripare, samtidigt som man har en dold Wallet. Denna senare använder samma Mnemonic-fras men är säkrad med ytterligare en passphrase.


Slutligen är det intressant att använda en passphrase när man vill styra slumpmässigheten i HD Wallet:s seed-generering.


## Hur väljer man en bra passphrase?

För att passphrase ska vara effektivt måste det vara tillräckligt långt och slumpmässigt. Precis som med ett starkt lösenord rekommenderar jag att du väljer en passphrase som är så lång och slumpmässig som möjligt, med en mängd olika bokstäver, siffror och symboler för att omöjliggöra en brute force-attack.


Det är också viktigt att spara denna passphrase på rätt sätt, på samma sätt som Mnemonic frasen. ** Att förlora den innebär att du förlorar tillgången till dina bitcoins**. Jag avråder starkt från att memorera den enbart i ditt huvud, eftersom detta orimligt ökar risken för förlust. Det ideala är att skriva ner den på ett fysiskt medium (papper eller metall) separat från Mnemonic-frasen. Denna säkerhetskopia måste självklart lagras på en annan plats än där din Mnemonic-fras förvaras för att förhindra att båda komprometteras samtidigt.


## Handledning


För att konfigurera en passphrase på en Ledger-enhet (Stax, Flex eller Nano) kan du läsa denna handledning:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

På ett COLDCARD:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

På en Jade Plus:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

On a Passport (batch-2):


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

På en Trezor-enhet (Safe 3, Safe 5 eller Model One):


https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42