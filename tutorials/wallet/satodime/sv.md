---
name: Satodime
description: Ta reda på hur du använder Satodime med mobilapplikationen
---
![cover](assets/cover.webp)



Den här guiden tar dig igenom installation, konfiguration och användning av Satodimes mobilapplikation. Du lär dig hur du tar ditt kort i besittning, skapar kassaskåp, lägger till pengar, öppnar och återställer dina privata nycklar. I bilagorna finns resurser, bästa praxis och tekniska förklaringar.



## Inledning



**Satodime**, utvecklat av **[Satochip](https://satochip.io/fr/)**, är ett säkert innehavarkort för att lagra Bitcoin på ett konkret och enkelt sätt. Det fungerar som en självförvarande wallet-hårdvara, där du har full kontroll över dina privata nycklar utan att vara beroende av en tredje part. Open-source och EAL6+-certifierad, den stöder upp till tre oberoende kassaskåp.



### Produktens bakgrund



Satodime, ett **carte au porteur, tillhör den som fysiskt innehar det**, utan behov av föregående registrering eller identifiering. Det tillgodoser behovet av säker, portabel bitcoinlagring, vilket gör att alla som har kortet kan använda det eller överföra bitcoins genom att skanna det via mobilappen för att ta över eller öppna kassaskåp. Till skillnad från en papperssedel används ett säkert chip för att försegla de privata nycklarna, som avslöjas först efter att de öppnats, vilket gör att kortet liknar kontanter där ägandet bestäms av fysisk besittning. Det är idealiskt för att ge bitcoins som gåvor och underlättar säker överföring av bitcoins från hand till hand, medan mobilapplikationen utnyttjar NFC för tillgänglig smartphone-interaktion.





- Säkerhet**: Privata nycklar genereras och lagras i det manipuleringssäkra chippet; synlig status (förseglad, oförseglad, tom).
- Funktioner**: Köp bitcoins direkt via appen (Paybis-partner); hantera Mainnet och Testnet.
- Öppen källkod**: Kod under AGPLv3-licens, verifierbar på GitHub.



### Kontinuerlig utveckling



Applikationen utvecklas regelbundet. Kontrollera Satochips webbplats eller butiker för uppdateringar. Till exempel kan nya blockkedjor eller köpfunktioner läggas till. Kontrollera [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) för pågående utveckling.



## 1. Förkunskapskrav



Innan du börjar använda **Satodime** ska du se till att du har följande saker:





- Kompatibel smartphone**: Android- eller iOS-enhet med NFC-aktivering.
- Satodime**-kort: Nytt eller oinitialiserat.
- Internetanslutning**: För att ladda ner appen.
- Grundläggande kunskaper**: Förståelse för privata/offentliga nycklar och riskerna med förlust (irreversibel).
- Säkert medium**: En säker plats för att registrera privata nycklar när de har öppnats (papper, metall; aldrig digitalt).



## 2. Installation





- Ladda ner ansökan** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Kontrollera utvecklaren (Satochip) för att undvika bedrägeri.
 - Satodime är **öppen källkod**. Källkod : [Satochips GitHub](https://github.com/Toporin/Satodime-Applet).





- Installera och starta applikationen**: Aktivera NFC på din telefon om det behövs.



![image](assets/fr/01.webp)



## 3. Inledande konfiguration



### 3.1 Starta programmet och skanna



Öppna appen och följ guiden. Placera Satodime-kortet på telefonens NFC-läsare (vanligtvis på baksidan). Håll den nedtryckt under hela operationen för att säkerställa en stabil anslutning.





- Om NFC inte fungerar ska du kontrollera telefonens inställningar.
- En skål bekräftar framgången: "Framgångsrik läsning".



![image](assets/fr/02.webp)



Som en allmän regel gäller att **alla följande operationer kräver bekräftelse genom skanning av Satodime-kortet**



### 3.2 Att ta kortet i besittning (*Ownership*)



Vid första användningen måste du bli ägare till kortet för att säkra det:





- Klicka på "*Take Ownership*" i appen.
- Bekräfta åtgärden: detta genererar en unik ägarnyckel.
- Skanna kartan igen för att tillämpa ändringarna.
- Varning**: Detta steg är irreversibelt. Se [artikeln om *äganderätt*](https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Skapa ett säkert



Satodime stöder upp till 3 kassaskåp. Skapa ett för att lagra bitcoin:





- Välj ett tomt kassaskåp (t.ex. Kassaskåp 01).
- Välj blockkedja (Bitcoin).
- Klicka på "*Create & Seal*".
- Skanna kortet till generate och försegla den privata nyckeln (okänd tills den öppnas).
- Gratulerar**: Ditt kassaskåp är nu förseglat och redo att ta emot pengar.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Lägg till medel



När kassaskåpet är förseglat laddar du det med bitcoins:





- Välj kassaskåp.
- Klicka på "*Lägg till medel*".
- Kopiera den offentliga adressen eller skanna QR-koden.
- Skicka pengar från en annan wallet.
- Kontrollera saldot efter bekräftelse på blockkedjan.
- Alternativ för köp: Klicka på "*Purchase*" för att köpa direkt via Paybis (Visa, Mastercard etc.). Tillämpliga avgifter.



![image](assets/fr/06.webp)



## 6. Öppna ett kassaskåp



För att komma åt den privata nyckeln och överföra pengarna någon annanstans, öppna kassaskåpet:





- Välj det förseglade kassaskåpet.
- Klicka på "Öppna förseglingen".
- Bekräfta varningen: denna operation är irreversibel.
- Skanna kortet för att öppna det.
- Kassaskåpet är inställt på "*Unsealed*"; den privata nyckeln kan nu visas/exporteras.
- Varning**: När förseglingen har öppnats är den privata nyckeln tillgänglig. Om någon tar din smartphone i besittning kan de komma åt nyckeln och på så sätt återfå pengarna i ditt kassaskåp (irreversibelt).



![image](assets/fr/07.webp)



## 7. Återställ privat nyckel



Efter att ha öppnat förseglingen, exportera nyckeln för användning i en annan wallet :





- Se till att du befinner dig i en säker miljö.
- Klicka på "*Visa privat nyckel*".
- Välj format: Legacy, SegWit, WIF, etc.
- Kopiera nyckeln eller skanna QR-koden.
- Säkerhet**: Dela aldrig din privata nyckel. Förvara den offline.
- Importera den till ett wallet-program som är kompatibelt med fondförvaltning (t.ex. Sparrow Wallet eller Electrum).



![image](assets/fr/08.webp)





## 8. Återställ bagageutrymmet



Om du återställer kassaskåpet raderas den tillhörande privata nyckeln oåterkalleligen. Med andra ord, om du inte har säkrat en kopia av din privata nyckel, eller importerat den till en annan wallet, kommer återställning av kassaskåpet att orsaka en oåterkallelig förlust av pengarna i det.



![image](assets/fr/09.webp)



När du återställer stammen blir facket tomt och redo för en ny stam.



## 9. Överlåtelse av äganderätt



För att till exempel erbjuda bitcoins via Satodime måste du :




- Ta ansvar för kortet,
- Skapa ett Bitcoin kassaskåp,
- Överför satss dit,
- Överföra äganderätten till kortet: nästa person som skannar kortet blir dess ägare,
- Ge Satodime-kortet till den person du väljer och uppmana dem att ladda ner applikationen och sedan skanna kortet för att ta över ägandet av det - och därmed få tillgång till de bitcoins som "lagras" på det.



![image](assets/fr/10.webp)




## BILAGOR



### A1. Bästa praxis



För att använda **Satodime** på ett säkert sätt :





- Säkra kortet**: Behandla det som kontanter; förlust = förlorade pengar om inte ägaren.
- Säkerhetskopiering av nycklar**: När förseglingen har öppnats ska privata nycklar sparas på ett säkert fysiskt medium. Aldrig digitalt.
- Kontrollera status**: Skanna alltid för att bekräfta kortinnehav och förseglad/icke förseglad status för kassaskåp.
- Konfidentialitet**: Använd nya adresser; undvik centraliserade växlar för överföringar.
- Uppdateringar**: Håll appen uppdaterad via butikerna.
- Återvinning**: Om kortet förloras men ägs finns pengarna på blockkedjan; använd den privata nyckeln om förseglingen öppnas.



### A2. Ytterligare resurser



Specifikt för Satodime :




- [Satodime-produkt](https://satochip.io/fr/product/satodime/)
- [Mobilguide](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy](https://planb.academy/) för handledning om självförvaring, privata nycklar etc.



**Spara din återställningsfras** :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Handledning om Satochip (varumärkets första produkt) :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Handledning för fröskötare:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Om Satochip



**Officiella länkar** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Support: info@satochip.io



**Satochip** är ett belgiskt företag som utvecklar hård- och mjukvarulösningar för hantering och lagring av bitcoins och andra kryptovalutor. Dess flaggskeppsprodukt, Satochip-hårdvaran wallet, är ett NFC-kort utrustat med en EAL6+-certifierad secure element. Med Seedkeeper, en minnesfras och hemlighetshanterare, och Satodime, ett bärarkort, erbjuder Satochip ett omfattande sortiment som är skräddarsytt för användarnas behov. Dess enheter, som drivs av programvara med öppen källkod, syftar till att demokratisera säkerheten på Bitcoin.