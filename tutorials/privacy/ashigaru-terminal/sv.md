---
name: Ashigaru Terminal
description: Använd Ashigaru på skrivbordet för att göra coinjoins
---

![cover](assets/cover.webp)



Ashigaru Terminal är Ashigaru-teamets anpassning av Sparrow Server, som implementerar Whirlpool coinjoin-protokollet. Denna programvara är en fortsättning på det arbete som påbörjades av Samourai Wallet, i synnerhet på Whirlpool GUI, vars grundläggande principer den antar: självförvaring och konfidentialitetsbevarande.



Denna programvara är en fork av Sparrow Server, modifierad och optimerad för full integration med Whirlpool-ekosystemet, ZeroLink coinjoin-protokollet som ursprungligen utvecklades av Samourai-teamen.



Ashigaru Terminal drivs från ett minimalistiskt TUI-gränssnitt och kan distribueras på en persondator eller på en dedikerad server. Det låter dig interagera direkt med Whirlpool för att initiera "*Tx0*", hantera "*Deposit*", "*Premix*", "*Postmix*" och "*Badbank*" konton, och utföra automatiska remixer för att förstärka sekretessen för dina delar.



Kort sagt, Ashigaru Terminal kommer att vara särskilt användbart om du vill skapa coinjoins med Whirlpool.



I den här första handledningen tar jag dig igenom installationen och användningen av Ashigaru Terminal. En andra, mer avancerad handledning kommer sedan att ägnas åt det faktiska skapandet av coinjoins.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Installera Ashigaru Terminal



För att installera Ashigaru Terminal behöver du Tor Browser, eftersom binärfilerna endast distribueras via Tor-nätverket. Om du inte redan har gjort det, [installera det på din maskin](https://www.torproject.org/download/).



### 1.1. Ladda ner Ashigaru Terminal



Från Tor Browser, gå till [release-sidan i deras Git-arkiv](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) för att ladda ner den senaste versionen av Ashigaru Terminal för ditt operativsystem.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Ladda ner följande 2 filer för ditt operativsystem:




- Den binära filen (`ashigaru_terminal_v1.0.0_amd64.deb` för Debian/Ubuntu, `.dmg` för macOS eller `.zip` för Windows) ;
- Den signerade hash-filen: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Kontrollera Ashigaru Terminal



Innan du kör programvaran på din enhet måste du kontrollera dess äkthet och integritet. Detta är ett viktigt steg, eftersom det förhindrar att du installerar en bedräglig version som kan äventyra dina bitcoins eller infektera din maskin.



Öppna en ny webbläsarflik och gå till [Keybase verifieringsverktyg](https://keybase.io/verify). Klistra in innehållet i filen `.txt` som du just har laddat ner i det angivna fältet och klicka sedan på knappen `Verify`.



![Image](assets/fr/02.webp)



För att diversifiera dina verifieringskällor kan du också jämföra meddelandet med det som finns tillgängligt på webbplatsen clearnet [ashigaru.rs](https://ashigaru.rs/download/), i avsnittet `/download`.



![Image](assets/fr/03.webp)



Om signaturen är giltig kommer Keybase att visa ett meddelande som bekräftar att filen har signerats av Ashigarus utvecklare.



![Image](assets/fr/04.webp)



Du kan också klicka på profilen `ashigarudev` som visas av Keybase och kontrollera att deras nyckelfingeravtryck matchar exakt : `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Om ett felmeddelande visas i detta skede är signaturen ogiltig. I så fall ska du **inte installera den nedladdade programvaran**. Börja om från början, eller be communityn om hjälp innan du fortsätter.



Keybase har försett dig med den autentiserade hashen för applikationen. Vi ska nu kontrollera att hashen för filen `.deb`, `.zip` eller `.dmg` som du har hämtat matchar den som validerats på Keybase. För att göra detta, gå till [HASH FILE ONLINE](https://hash-file.online/).



Klicka på knappen `BROWSE...` och välj filen `.deb`, `.zip` eller `.dmg` som hämtades i steg 1.1. Välj sedan hashfunktionen `SHA-256` och klicka på `CALCULATE HASH` för att generate hashen för din fil.



![Image](assets/fr/06.webp)



Webbplatsen kommer då att visa programvarans hash. Jämför den med den hash som du verifierade på Keybase.io. Om de två matchar perfekt har äkthets- och integritetskontrollen varit framgångsrik. Du kan då använda programvaran.



![Image](assets/fr/07.webp)



### 1.3 Lansering av Ashigaru Terminal





- Debian / Ubuntu



För att installera programvaran, kör kommandot :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Ändra ordningen enligt den nedladdade versionen.



Kontrollera sedan installationen:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Starta sedan programvaran:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Fönster**



Högerklicka på filen `.zip` som du har hämtat och kontrollerat och välj sedan `Extract All...` för att extrahera innehållet.



När extraktionen är klar dubbelklickar du på filen `Ashigaru-terminal.exe` för att starta programvaran.



![Image](assets/fr/08.webp)



## 2. Komma igång med Ashigaru Terminal



Ashigaru Terminal är ett TUI-program (*Text-based User Interface*), dvs. ett minimalistiskt gränssnitt som körs direkt i terminalen. Du interagerar med det med hjälp av menyer och kortkommandon, men utan någon riktig klassisk grafisk miljö.



![Image](assets/fr/09.webp)



Det är lätt att använda: använd tangentbordets piltangenter för att navigera genom menyerna och tryck på "Enter" för att validera en åtgärd eller bekräfta ett val.



## 3. Ansluta din nod till Ashigaru Terminal



Som standard ansluter Ashigaru Terminal till en offentlig Electrum-server. Detta innebär uppenbarligen risker när det gäller sekretess och suveränitet. Så vi kommer att konfigurera den så att den ansluter direkt till din egen Electrum Server.



För att göra detta öppnar du menyn `Preferences > Server`.



![Image](assets/fr/10.webp)



Klicka på knappen `< Edit >`.



![Image](assets/fr/11.webp)



Välj `Private Electrum Server` och klicka sedan på `<Fortsätt>`.



![Image](assets/fr/12.webp)



Ange URL och port för din server. Du kan ange en Tor-adress i `.onion`. Klicka sedan på `< Test >` för att verifiera anslutningen.



![Image](assets/fr/13.webp)



Om anslutningen lyckas visas meddelandet `Success` tillsammans med information om din server.



![Image](assets/fr/14.webp)



Om du ännu inte har en Bitcoin-nod rekommenderar jag att du går den här kursen:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*I mitt fall, för denna handledning, kommer jag att koppla bort från min Electrs-server eftersom jag arbetar på testnet. Operationen förblir dock strikt identisk på mainnet.*



## 4. Skapa en portfölj på Ashigaru Terminal



Nu när programvaran är korrekt konfigurerad kan vi lägga till en Bitcoin-portfölj.



Du har två alternativ:




- Du kan skapa en ny wallet från grunden och använda den uteslutande på Ashigaru Terminal. I så fall måste du öppna den här programvaran varje gång du vill interagera med din wallet;
- Alternativt kan du importera din befintliga Ashigaru wallet direkt från din telefon till Ashigaru Terminal. Nackdelen med den här metoden är att den minskar säkerheten i din installation något, eftersom din wallet då utsätts för två riskfyllda miljöer istället för en. Å andra sidan ger det fördelen att du kan låta Ashigaru Terminal vara igång kontinuerligt för att blanda dina mynt, samtidigt som du kan spendera dem på distans via Ashigarus mobilapp.



I den här handledningen väljer vi den andra metoden. Men om du föredrar att skapa en helt ny portfölj är proceduren densamma: den enda skillnaden är under skapandet, då du måste spara din nya minnesfras och din nya passphrase.



Observera också att Ashigaru Terminal inte tillåter dig att spendera dina bitcoins direkt. Du kan antingen synkronisera samma plånbok på Ashigaru Terminal och Ashigaru-appen (vilket jag kommer att göra i denna handledning), eller på Sparrow Wallet.



Om du ännu inte har en wallet på Ashigaru-applikationen kan du följa den dedikerade handledningen :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Gå till menyn "Plånböcker".



![Image](assets/fr/15.webp)



Välj sedan "Skapa/återställ wallet...". Med alternativet `Öppna Wallet...` kan du komma åt en portfölj som redan sparats i Ashigaru Terminal vid ett senare tillfälle.



![Image](assets/fr/16.webp)



Ge din portfölj ett namn.



![Image](assets/fr/17.webp)



Välj sedan portföljtyp `Hot Wallet`.






![Image](assets/fr/18.webp)



Det är i detta skede som förfarandet skiljer sig åt beroende på ditt ursprungliga val:




- Om du vill skapa en ny portfölj från grunden klickar du på `<Generera ny Wallet>`, definierar en passphrase BIP39 och sparar sedan noggrant din mnemoniska fras och din passphrase på ett fysiskt medium;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Om du vill använda samma wallet som din Ashigaru-applikation ska du skriva in de 12 orden i din minnesfras och din passphrase BIP39 direkt i motsvarande fält. Skriv orden med gemener, hela, i ordning, åtskilda av ett mellanslag, utan siffror eller extra tecken.



När detta steg är klart klickar du på `< Nästa >`.



*Obs*: Om du inte kan klicka på den här knappen är din minnesfras ogiltig. Kontrollera noga att inget av orden är felaktigt eller felstavat.



![Image](assets/fr/19.webp)



Du måste sedan ange ett lösenord. Detta kommer att användas för att låsa upp din Ashigaru Terminal wallet och skydda den mot obehörig fysisk åtkomst. Det är inte involverat i den kryptografiska härledningen av dina nycklar: med andra ord, även utan detta lösenord kommer vem som helst med din mnemoniska fras och passphrase att kunna återställa din wallet och komma åt dina bitcoins.



Välj ett långt, komplext och slumpmässigt lösenord. Förvara en kopia på en säker plats: helst på ett fysiskt medium eller i en säker lösenordshanterare.



Klicka på `< OK >` när du är klar.



![Image](assets/fr/20.webp)



## 5. Användning av portföljen



Du kan sedan välja vilket konto du vill komma åt. För tillfället har vi inte initierat några mixar, så vi kommer att komma åt `Deposit`-kontot.



![Image](assets/fr/21.webp)



Användningen är då identisk med Sparrow, eftersom Ashigaru Terminal är en fork av Sparrow Server. Du kommer att hitta samma menyer:



![Image](assets/fr/22.webp)





- transaktioner": låter dig se historiken över transaktioner som är kopplade till detta konto. I mitt fall visas några av dem redan, eftersom jag hade gjort några med Ashigaru-applikationen på samma wallet.



![Image](assets/fr/23.webp)





- receive`: genererar en ny, tom kvittoadress för att placera satss på insättningskontot.



![Image](assets/fr/24.webp)





- addresses`: visar en lista över alla dina adresser, oavsett om de tillhör ditt kontos interna eller externa kedja.



![Image](assets/fr/25.webp)





- `UTXOs`: listar alla dina tillgängliga UTXOs.



![Image](assets/fr/26.webp)





- `Settings`: ger tillgång till din portföljs *descriptor*. Du kan också konsultera din seed, justera *Gap Limit* eller ändra skapandedatumet för din portfölj.



![Image](assets/fr/27.webp)



Du vet nu hur du installerar och använder Ashigaru Terminal. I nästa handledning kommer vi att se hur man utför coinjoins med denna programvara och hur man hanterar medel i "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
