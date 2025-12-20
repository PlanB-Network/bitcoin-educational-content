---
name: Jade - Electrum
description: Så här använder du din Jade eller Jade Plus med Electrum (skrivbord)
---

![cover](assets/cover.webp)



_Den här guiden är hämtad från en [Bitcoin Workshops-lektion](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Handledningen är gjord med Jade Classic, men operationerna är också giltiga för dem som har Jade Plus.



När Jade har initialiserats kan du börja använda den och välja en wallet-display för att göra det.



Jade är en enhet som kan användas med flera wallet, eller kompletterande appar som Blockstream specificerar dem på sin webbplats.



I den här guiden beskrivs hur du använder Electrum Wallet via USB-kabelanslutning.



## Överföring av offentlig nyckel



Ta och slå på din initialiserade Jade. Så snart du slår på den ser den ut så här:




![img](assets/en/32.webp)



Om du väljer _Unlock Jade_ kommer du till en meny där du måste välja hur du ansluter din enhet till Companion-appen.



Med Electrum kan du bara ansluta Jade via USB, så välj den här metoden.



Starta Electrum, som kommer att öppna förslagsvis som ett standardalternativ för att öppna den senast använda wallet.



Om det här är första gången du ansluter Jade till Electrum väljer du _Create New Wallet_ och sedan _Finish_.



![img](assets/en/34.webp)



Namn wallet.



![img](assets/en/35.webp)



Välj standard Wallet.



![img](assets/en/36.webp)



När du väljer keystore är det viktigt att du väljer _Use a hardware device_.



![img](assets/en/37.webp)



Electrum börjar skanna efter maskinvaruenheten.



![img](assets/en/38.webp)



Genom att ansluta USB till datorn (redan ansluten på USB C-sidan till Jade) visas wallet-hårdvaran i låsläge. Jade låser upp genom att sätta in den sexsiffriga PIN-koden som ställdes in under installationen.




![img](assets/en/39.webp)



Olåst hårdvaruenhet, Electrum upptäcker Jade. Fortsätt genom att klicka på _Nästa_.



![img](assets/en/40.webp)



Vid denna punkt ber Electrum dig att ställa in policyskriptet: välj _Native Segwit_.



![img](assets/en/41.webp)



Fasen med överföring av publik nyckel från wallet från Jade till displayen Electrum börjar.



När exporten av den offentliga nyckeln har slutförts är processen klar.



Watch-only är klar och Electrum meddelar att den är klar med följande skärm.



![img](assets/en/42.webp)



wallet skapas faktiskt och du kan börja utforska den: du kan se _adresserna_, _plånboksinformationen_ och - viktigast av allt - du kan se i det nedre högra hörnet indikationen på att det är Blockstreams enhet. Den gröna pricken bredvid Blockstream-logotypen visar att enheten är påslagen och korrekt ansluten till det lokala nätverket.



![img](assets/en/43.webp)



## Mottagande och utbetalning av transaktioner



Från menyn _Receive_ i Electrum, generate en `scriptPubKey` (adress) för att ta emot pengar. Börja alltid med en liten summa och gör ett mottagnings- och utgiftstest.



![img](assets/en/44.webp)



När du har tagit emot satss kan du kontrollera deras ankomst i menyn _History_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



När transaktionen är bekräftad kan du spendera denna UTXO och avsluta testet.



Kostnaden innebär att Jade används för att signera.



Gå till _Send_-menyn i Electrum, klistra in en scriptPubKey och kontrollera den väl.



![img](assets/en/47.webp)



När du är klar trycker du på _Pay_.



Transaktionsfönstret öppnas, där det är viktigt att ställa in rätt transaktionsavgifter. När du är klar med alla inställningar klickar du på _Preview_ i nedre högra hörnet.



![img](assets/en/48.webp)



I transaktionsfönstret visas några viktiga detaljer, först och främst status: "Osignerad".



I det här skedet kan du också se kommandot _Sign_, som du måste klicka på för att fästa signaturen med Jade.



![img](assets/en/49.webp)



Nu börjar en kommunikationsfas mellan displayen wallet och hårdvaruenheten, där Electrum varnar dig för att följa instruktionerna på hårdvaruenheten, som är påslagen och redo att signeras.



![img](assets/en/50.webp)



**Först är det dock bäst att du verifierar vad du skriver under: alla parametrar för den transaktion som du just har satt upp visas också på Jade** och du kan verifiera dem alla.



![img](assets/en/51.webp)



För att fortsätta, se till att du alltid placerar markören på pilen `→` som leder till nästa steg och aldrig på `X` om du inte vill avsluta operationen utan att slutföra den.



Verifieringsdelen avslutas med att avgiften visas. Vid denna tidpunkt är bekräftelsen likvärdig med att sätta din signatur.



![img](assets/en/52.webp)



Under en kort stund bearbetar Jade operationen och när den är klar återgår den till hemmenyn.



![img](assets/en/53.webp)



På Electrum kan du se status för transaktionen, som har ändrats från "Osignerad" till "Signerad" och nu är det möjligt för dig att sprida den genom att klicka på _Broadcast_.



![img](assets/en/54.webp)



wallet, sålunda testad, kan användas för att ta emot UTXO avsedd för säker förvaring.



![img](assets/en/55.webp)



Den här guiden är ett exempel på hur du använder din Jade, ansluten via USB, till en wallet watch-only. Electrum är ett klassiskt exempel, men du kanske föredrar annan wallet-programvara. Jade exporterar den offentliga nyckeln till många andra plånböcker: hitta liknande funktioner som du läser om i den här handledningen, för att vägleda dig och hitta hur du använder den i din favorit companio-app.