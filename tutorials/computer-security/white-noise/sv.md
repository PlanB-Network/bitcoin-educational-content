---
name: White Noise
description: En privat, decentraliserad meddelandeapplikation baserad på Nostr- och MLS-protokollen
---

![cover](cover.webp)




## Inledning



"Mitt i svårigheterna ligger möjligheterna". Detta citat av Albert Einstein påminner oss om att problem inte är slutgiltiga, utan att de innehåller fröet till nya, innovativa lösningar.



Motiveringarna bakom lanseringen av den lösning vi presenterar i denna handledning illustrerar detta perfekt. Det är **White Noise**, född av nödvändighet.



Enligt grundaren Max Hillebrand, som citeras av *Bitcoin Magazine*: "Vi startade det här projektet i brist på alternativ." Han förklarar att "befintliga krypteringsapplikationer är ineffektiva i stor skala: att lägga till 100 personer i en gruppkonversation saktar ner krypteringen avsevärt. Decentraliserade plattformar erbjuder under tiden inte privata meddelanden. Nostr:s öppna relänätverk gör det möjligt för alla att sprida idéer, men skyddet av direktmeddelanden är fortfarande dramatiskt otillräckligt. Vi insåg att vi var tvungna att slå samman dessa system för att skydda friheten."



## Vad är White Noise?



White Noise är en meddelandeapplikation med öppen källkod som utvecklats av ett ideellt team. Applikationen främjar säkerhet, integritet och decentralisering. Till skillnad från konventionella applikationer kräver den varken ett telefonnummer eller en e-postadress.


White Noise kännetecknas av integrationen av två grundläggande protokoll - Nostr och MLS - som utgör dess tekniska grund.



Nostr (Notes and Other Stuff Transmitted by Relays) är ett decentraliserat protokoll med öppen källkod som är utformat för att motstå censur.  Protokollet använder reläer, nyckelpar och klienter.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Med White Noise kan du till och med välja dina egna reläinställningar för att maximera integriteten.



MLS (Messaging Layer Security) är å andra sidan ett säkerhetsprotokoll som möjliggör kryptering av meddelanden från början till slut. Med andra ord är meddelanden endast tillgängliga vid slutpunkterna, dvs. avsändaren och mottagaren av meddelandet. Detta innebär att reläer som är inblandade i routningen av meddelanden inte kan komma åt innehållet i dem.



Här är en snabb jämförelse mellan White Noise och ett antal av de mest kända meddelandeprogrammen.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## Komma igång med White Noise



### White Noise installation



Gå till [White Noise:s webbplats] (https://www.whitenoise.chat/) och klicka sedan på **Download**.



![screen](assets/fr/03.webp)



White Noise är för närvarande endast tillgängligt på mobila enheter.


I det nya gränssnittet som visas trycker du på :





- knappen **Zapstore** eller **Android APK** om du vill ladda ner den på Android ;
- på **iOS TestFlight**-knappen om du använder en iPhone.



![screen](assets/fr/04.webp)



I den här handledningen kommer vi att genomföra en Android-nedladdning.


Om du väljer att ladda ner via **Zapstore** kommer du att omdirigeras till den. När du är på Zapstore skriver du **White Noise** i sökfältet. Fortsätt sedan att ladda ner genom att klicka på **Install**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Om du väljer att ladda ner APK-filen kommer du att omdirigeras till White Noise GitHub-arkivet för att välja rätt version för din smartphone.



De tillgängliga APK-filerna är :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), lämplig för nya telefoner med 64-bitars processorer;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) lämplig för äldre telefoner med 32-bitars processorer.



Du har också **.sha256**-filer, som bara är kontrollsummor för att verifiera integriteten i nedladdningen.



![screen](assets/fr/07.webp)



När nedladdningen är klar installerar och öppnar du programmet.



![screen](assets/fr/08.webp)



### Inledande konfiguration av användarkonto



För din första anslutning till White Noise, tryck på **Register**-knappen.



![screen](assets/fr/09.webp)



Därefter konfigurerar du din profil genom att välja ett profilfoto, ett namn och lägga till en kort beskrivning av dig själv. Du behöver inte fylla i din riktiga identitet (namn och foto).


Observera att White Noise automatiskt väljer ett namn (pseudonym) åt dig, som du kan behålla eller ändra. Tryck slutligen på knappen **End**.



![screen](assets/fr/10.webp)



Du kommer att omdirigeras till White Noise:s **hemsida**, där dina konversationer kommer att listas. Ditt konto är nu konfigurerat och redo att användas. Du kan dela din profil eller söka efter vänner för att starta en chatt.



![screen](assets/fr/11.webp)




### Upptäcka White Noise-gränssnitt



I huvudgränssnittet, högst upp på skärmen, ser du :



Profilikonen i det övre vänstra hörnet är en miniatyrbild av din profilbild eller första bokstaven i ditt profilnamn. Klicka på den för att komma till dina kontoinställningar.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



I det övre högra hörnet hittar du ikonen för att starta en ny konversation.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Inställningar för användarkonto



Tryck på profilikonen i det övre vänstra hörnet för att komma till inställningarna.



![screen](assets/fr/16.webp)



Högst upp i gränssnittet **Settings** hittar du ditt foto och profilnamn, följt av din publika nyckel, som du kan dela med dig av med hjälp av QR-koden bredvid.



![screen](assets/fr/17.webp)



Strax nedanför hittar du knappen **Change account**, som låter dig ansluta till en annan profil i programmet.



![screen](assets/fr/18.webp)



Sedan har du en första sektion med fyra (4) undermenyer som t.ex:





- Ändra profil**



I den här undermenyn kan du ändra profilnamn, Nostr-adress (NIP-05) ... Glöm inte att klicka på **Save** för att spara dina ändringar.



![screen](assets/fr/19.webp)





- Profilnycklar **



Här har du tillgång till dina offentliga och privata (hemliga) nycklar. Som White Noise påminner dig om får din privata nyckel inte avslöjas under några omständigheter.



![screen](assets/fr/20.webp)





- Nätrelä



I den här undermenyn kan du lägga till eller ta bort **generella reläer** (reläer som definieras för användning i alla dina Nostr-applikationer), **inbox-reläer** och **nyckelpaketreläer**.



Tryck på ikonen **skräp** framför ett relä för att ta bort det, eller på ikonen **+** (plus) för att lägga till ett nytt.



![screen](assets/fr/21.webp)





- Frånkoppling**



Klicka på den här undermenyn för att koppla bort ditt konto från programmet. Men se till att du har sparat dina privata nycklar offline, annars kommer du inte att kunna logga in igen senare.



![screen](assets/fr/22.webp)




En andra sektion erbjuder undermenyer:





- Applikationsinställningar



Här kan du definiera applikationens utseende (tema och visningsspråk) och till och med radera data om du anser att den har äventyrats eller om du själv känner dig utsatt för risk.



![screen](assets/fr/23.webp)





- Donera till White Noise



Du kan stödja teamet bakom White Noise (en icke-vinstdrivande organisation) med donationer via deras Lightning-adress eller deras Bitcoin silent betalningsadress.



![screen](assets/fr/24.webp)



Längst ner finns slutligen **utvecklarinställningarna**.



![screen](assets/fr/25.webp)




## Starta en konversation



Låt oss nu ta en titt på hur man startar en konversation. I skrivande stund erbjuder White Noise tre kommunikationsalternativ. I tur och ordning kommer vi att utforska **Privata konversationer** (**Chat 1:1**), dvs. mellan bara dig och en annan person, **Gruppkonversationer** och **Skicka multimediafiler**.




### Kat 1:1



Om du vill lägga till en ny korrespondent klickar du på ikonen för att starta en ny konversation i huvudgränssnittet.


Skanna sedan QR-koden för den offentliga nyckeln (1) eller klistra in den offentliga nyckeln (2) för din nya korrespondent i sökfältet för att hitta honom eller henne.



![screen](assets/fr/26.webp)



Tryck sedan på knappen **Starta konversation** för att starta en konversation med din korrespondent. Du kan också **Följa** din korrespondent eller bjuda in honom/henne till en gruppkonversation genom att trycka på knappen **Lägg till i grupp**.



![screen](assets/fr/27.webp)



Ditt första meddelande till en ny korrespondent är att likna vid en inbjudan. Denna begäran måste accepteras av din korrespondent innan du kan kommunicera med honom/henne. Om de vägrar, ja, då är ingen konversation möjlig.



![screen](assets/fr/28.webp)



Och så länge de inte accepterar din inbjudan kan de inte heller läsa innehållet i ditt första meddelande.



När han har accepterat din inbjudan kan han nu svara dig och ni kan kommunicera sömlöst och säkert.



![screen](assets/fr/29.webp)



I en diskussion har du dessutom ytterligare funktioner.



Du kan trycka länge på ett visst meddelande för att visa alternativ som t.ex:




- reagera på meddelandet med en emoji (1) ;
- gör ett **direkt citat** för att svara på meddelandet genom att trycka på **Reply** (2) ;
- kopiera meddelandet genom att trycka på **Kopiera** (3).



![screen](assets/fr/30.webp)





- radera ett meddelande med **Radera**-knappen endast om det kommer från dig.



![screen](assets/fr/31.webp)



Du kan söka inom en konversation.



Klicka på korrespondentens avatar längst upp på skärmen för att komma till "konversationsinformation" och tryck på knappen **Sök i konversation**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



I sökfältet som visas skriver du det ord du vill söka efter och startar sökningen. Du kommer då att se dina sökord markerade med **fett**.



![screen](assets/fr/34.webp)




### Samtal i grupp



Samtalsgrupper kan skapas på White Noise.



Detta gör du genom att trycka på ikonen i gränssnittet för start av ny konversation och sedan klicka på **Ny gruppkonversation**. I sökfältet anger du sedan den offentliga nyckeln för den första medlemmen som du vill lägga till i din grupp.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Om det här alternativet inte fungerar kan du i gränssnittet **Starta en ny konversation** ange den offentliga nyckeln för den första medlemmen som du vill lägga till i gruppen i sökfältet. Du kan också skanna QR-koden som är kopplad till hans eller hennes publika nyckel.



Istället för att trycka på knappen **Starta konversation** klickar du den här gången på knappen **Lägg till i grupp**.



![screen](assets/fr/37.webp)



I popup-menyn som visas trycker du på **Ny gruppkonversation**.



![screen](assets/fr/38.webp)



Tryck sedan på **Fortsätt** (du behöver inte ange den publika nyckeln igen).



![screen](assets/fr/39.webp)



Som skapare av gruppen är du automatiskt dess administratör. Fyll i gruppens uppgifter, t.ex. **gruppnamn och beskrivning**, och klicka sedan på knappen **skapa grupp**.



![screen](assets/fr/40.webp)



Den användare som du lägger till som första medlem, och alla andra som du lägger till senare, får ett meddelande med en inbjudan att gå med i gruppen. De måste acceptera genom att klicka på **Accept** för att gå med i gruppen.



![screen](assets/fr/41.webp)



Det är också möjligt att lägga till en ny medlem som du redan chattar med i en befintlig grupp. Det gör du genom att klicka på avataren längst upp på skärmen för att komma till "konversationsinformationen" och trycka på knappen **Lägg till i gruppen**.



![screen](assets/fr/42.webp)



I det nya gränssnittet som visas **markerar du** den grupp du vill lägga till honom i och trycker på **Lägg till i grupp**. Allt som återstår att göra är att vänta på att den går med på att gå med i gruppen.



![screen](assets/fr/43.webp)



Observera att endast en gruppadministratör kan ändra gruppinformation och lägga till eller utesluta medlemmar. Nyckelrotation förhindrar också att medlemmar som uteslutits kan dekryptera framtida meddelanden.



Om du vill ta bort en medlem trycker du på gruppikonen längst upp i gruppens huvudgränssnitt för att komma till gränssnittet för gruppinformation.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Klicka sedan på medlemmens namn och **Avlägsna från gruppen**. Från det här gränssnittet kan du också skicka ett meddelande till honom, följa honom eller lägga till honom i en annan grupp.



![screen](assets/fr/46.webp)



### Skicka multimediafiler



För tillfället kan endast foton delas mellan användare på White Noise. Oavsett om du befinner dig i en privat konversation eller en gruppchatt måste du göra följande för att göra det :





- tryck på symbolen **plus (+)** till vänster om inmatningsfältet för textmeddelanden.



![screen](assets/fr/47.webp)





- klicka sedan på rutan med texten **Foton** längst ner för att komma till ditt galleri.



![screen](assets/fr/48.webp)





- välj det eller de foton som ska skickas.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Viktiga punkter att komma ihåg



White Noise erbjuder en god nivå av konfidentialitet och överlägsen säkerhet. Å andra sidan är det en mycket ny applikation, inte särskilt utbredd och fortfarande i sin linda. Följaktligen är det fortfarande för tidigt att dra några aktiva slutsatser. Det är möjligt att stöta på några funktionsstörningar under användning.



I dagsläget saknar den vissa funktioner (inga ljud- eller videosamtal, ingen sändning av ljud- eller videomultimediefiler) jämfört med populära meddelandeprogram.



White Noise är dock fortfarande ett intressant alternativ för konversationer där sekretess är av största vikt (t.ex. med familj, nära vänner eller aktivister för en gemensam sak), även om det kräver lite ansträngning att installera (via alternativa applikationsbutiker eller APK-filer) och lära sig (behärska lite av konceptet med nyckelpar, klienter och reläer med Nostr-protokollet).



Nu vet du hur du använder White Noise för att kommunicera säkert med dina vänner och din familj. Ge oss en tumme upp om du tycker att den här handledningen var användbar.



Vi rekommenderar vår handledning om Tox Chat, ett program som låter dig chatta utan mellanhänder över det decentraliserade Tox-protokollet.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3