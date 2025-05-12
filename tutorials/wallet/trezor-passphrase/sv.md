---
name: passphrase BIP39 Trezor
description: Hur lägger jag till en passphrase i min Trezor-portfölj?
---
![cover](assets/cover.webp)



En passphrase BIP39 är ett valfritt lösenord som, i kombination med Mnemonic-frasen, ger ytterligare en Layer säkerhet för deterministiska och hierarkiska Bitcoin-portföljer. I denna handledning kommer vi tillsammans att upptäcka hur man ställer in en passphrase på din säkra Bitcoin Wallet på en Trezor (Safe 3, Safe 5 och Model One).



![Image](assets/fr/01.webp)



Innan du börjar denna handledning, om du inte är bekant med passphrase-konceptet, hur det fungerar och dess konsekvenser för din Bitcoin Wallet, rekommenderar jag starkt att du läser den här andra teoretiska artikeln där jag förklarar allt (detta är mycket viktigt, eftersom att använda en passphrase utan att helt förstå hur den fungerar kan sätta dina bitcoins i fara) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase på Trezor hanteras på det klassiska sättet om du har valt BIP39-standarden under konfigurationen (vilket jag rekommenderar om du inte behöver *Multi-share Backup*). Det som är speciellt med Trezor är att du antingen kan ange passphrase direkt på Hardware Wallet eller via datorns tangentbord med hjälp av Trezor Suite-programvaran. Det andra alternativet är betydligt mindre säkert, eftersom datorn har en oerhört mycket större attackyta än Hardware Wallet. Det kan dock gå snabbare att skriva en komplex passphrase på ett vanligt tangentbord än på Hardware Wallet, vilket kan uppmuntra till användning av starka lösenfraser. Så det är alltid bättre att använda en passphrase, även om den måste skrivas, än att inte använda någon alls. Det är dock viktigt att vara medveten om den ökade risken för numeriska attacker som detta innebär.



Dessa alternativ är inte tillgängliga i alla Trezor-kompatibla program för portföljhantering. För Model One kan till exempel passphrase matas in via tangentbordet på Sparrow Wallet. För modellerna Model T, Safe 3 och Safe 5 måste du antingen använda Trezor Suite eller ange passphrase direkt på Hardware Wallet, eftersom möjligheten att ange via Sparrow inaktiverades av HWI för några år sedan.



![Image](assets/fr/02.webp)



I Trezor Suite har du två olika sätt att hantera passphrase-behov. Du kan aktivera alternativet "*passphrase*" på fliken "*Device*". Om det är aktiverat kommer Trezor Suite och alla andra portföljhanteringsprogram systematiskt att be dig att ange din passphrase varje gång du startar upp. Om du föredrar en mer diskret metod för att använda en passphrase kan du behålla inställningen på "*Standard*". I så fall måste du manuellt gå till menyn i din Hardware Wallet i det övre vänstra hörnet och klicka på knappen "*+ passphrase*" varje gång du startar den.



Innan du påbörjar denna handledning bör du kontrollera att du redan har initialiserat din Trezor och genererat din Mnemonic-fras. Om du inte har gjort det och din Trezor är ny, följ den modellspecifika handledning som finns på Plan ₿ Network. När du har slutfört detta steg kan du återgå till denna handledning.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Lägga till en passphrase till ett Safe 3 eller Safe 5



När du har skapat din Wallet, sparat din Mnemonic och angett en PIN-kod kommer du till startmenyn i Trezor Suite. I det övre vänstra hörnet bör ett fönster visas där du uppmanas att aktivera passphrase BIP39.



![Image](assets/fr/03.webp)



Om detta fönster inte visas måste du manuellt aktivera alternativet "*passphrase*" i inställningsfliken "*Device*".



![Image](assets/fr/04.webp)



I detta fönster uppmanas du att ange din passphrase. Välj en stark passphrase och gör omedelbart en fysisk säkerhetskopia, på ett medium som papper eller metall. I det här exemplet har jag valt passphrase: `fH3&kL@9mP#2sD5qR!82`. Det här är ett exempel, men jag rekommenderar att du väljer en något längre passphrase. Mellan 30 och 40 tecken skulle vara idealiskt (som ett bra lösenord).



du ska naturligtvis aldrig dela med dig av din passphrase på Internet, som jag gör i den här handledningen. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.**_



För mer specifika rekommendationer om hur du väljer din passphrase uppmanar jag dig återigen att läsa denna andra artikel:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Om du vill ange din passphrase via datorns tangentbord skriver du in den i det angivna fältet och klickar sedan på "*Access passphrase Wallet*".



![Image](assets/fr/05.webp)



Din Hardware Wallet kommer då att visa din passphrase. Kontrollera att den matchar din fysiska säkerhetskopia (papper eller metall) innan du klickar på skärmen för att fortsätta.



![Image](assets/fr/06.webp)



Detta kommer att ge dig tillgång till din passphrase-skyddade portfölj.



![Image](assets/fr/07.webp)



Om du föredrar att öka säkerheten genom att endast ange ditt passphrase på din Trezor, klicka på "*Ange passphrase på Trezor*" när du uppmanas att göra det.



![Image](assets/fr/08.webp)



Ett T9-tangentbord visas på din Trezor, så att du kan skriva in din passphrase. När du är klar med din inmatning klickar du på Green-fästet för att applicera passphrase på din Wallet.



![Image](assets/fr/09.webp)



Du kommer då att ha tillgång till din passphrase säkra Wallet.



![Image](assets/fr/10.webp)



För att använda Sparrow Wallet är proceduren liknande, men för modellerna T, Safe 3 och Safe 5 måste passphrase anges på Hardware Wallet och inte via datorns tangentbord.



När Sparrow Wallet kräver åtkomst till din Trezor och passphrase ännu inte har tillämpats sedan den senaste uppstarten, måste du ange den med hjälp av T9-tangentbordet.



![Image](assets/fr/11.webp)



## Lägga till en passphrase till en Model One



På Model One är det nästan oumbärligt att använda en passphrase BIP39. Eftersom denna enhet inte innehåller något Secure Element är det relativt lätt att få ut känslig information. Den är därför inte motståndskraftig mot fysiska attacker. Men eftersom passphrase inte finns kvar på enheten efter att den har stängts av, kan användning av en stark (icke-brutabel) passphrase skydda dig mot de flesta kända fysiska attacker på denna modell.



På Model One är det inte möjligt att ange passphrase direkt på Hardware Wallet. Du måste mata in den via datorns tangentbord.



När du har skapat din Wallet, sparat din Mnemonic och ställt in en PIN-kod kommer du till Trezor Suite hemmeny. I det övre vänstra hörnet visas ett fönster som inbjuder dig att aktivera passphrase BIP39.



![Image](assets/fr/12.webp)



Om detta fönster inte visas måste du aktivera alternativet "*passphrase*" på fliken "*Device*" i inställningarna.



![Image](assets/fr/13.webp)



I detta fönster uppmanas du att ange din passphrase. Välj en stark passphrase och gör omedelbart en fysisk säkerhetskopia, på ett medium som papper eller metall. I det här exemplet har jag valt passphrase: `fH3&kL@9mP#2sD5qR!82`. Detta är bara ett exempel, men jag rekommenderar att du väljer en något längre passphrase. Mellan 30 och 40 tecken skulle vara idealiskt (som ett bra lösenord).



För mer specifika rekommendationer om hur du väljer din passphrase uppmanar jag dig återigen att läsa denna andra artikel:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Ange din passphrase i det angivna fältet och klicka sedan på knappen "*Access passphrase Wallet*".



![Image](assets/fr/14.webp)



Din Hardware Wallet kommer att visa din passphrase. Kontrollera att den matchar din fysiska säkerhetskopia (papper eller metall) och klicka sedan på högerknappen för att fortsätta.



![Image](assets/fr/15.webp)



Då kommer du till din passphrase-skyddade portfölj.



![Image](assets/fr/16.webp)



För att använda Sparrow Wallet därefter är proceduren densamma. Varje gång Sparrow behöver tillgång till din Hardware Wallet, och passphrase inte har angetts sedan enheten senast startades, måste du ange den.



![Image](assets/fr/17.webp)



Gratulerar, du har nu kommit igång med att använda passphrase BIP39 på Trezors hårdvaruplånböcker. Om du vill ta din Wallet-säkerhet ett steg längre, kolla in den här handledningen om Trezors *Multi-share* backupsystem (*Shamirs Secret Sharing Scheme*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!