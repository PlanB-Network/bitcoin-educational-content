# Installera Bitcoin Core på Mac eller Windows

Det är möjligt att installera Bitcoin Core på din vanliga dator, men det är inte idealiskt. Om du inte har något emot att ha din dator påslagen 24/7 kommer det att fungera bra. Om du behöver stänga av datorn kan det vara irriterande att vänta på att programvaran ska synkroniseras varje gång du startar om den.

Dessa instruktioner är avsedda för användare av Mac eller Windows. Linux-användare kommer förmodligen inte att behöva min hjälp, men instruktionerna för Linux är mycket liknande de för Mac.

## Börja med en ren dator

Idealt sett vill du använda en ren dator utan skadlig programvara. Även om du använder en hårdvaruplånbok kan skadlig programvara lura dig och få dig att förlora dina bitcoins.

Du kan antingen rengöra en gammal dator och använda den som en dedikerad Bitcoin-dator, eller köpa en dedikerad dator/laptop.

## Hårddisken

Bitcoin Core kommer att ta upp cirka 400 gigabyte data på din hårddisk och kommer att fortsätta växa. Du kan använda din interna hårddisk, men du kan också ansluta en extern hårddisk. Jag kommer att förklara båda alternativen. Idealt sett bör du använda en solid state-enhet (SSD). Om du har en gammal dator har den förmodligen inte en inbyggd SSD. Köp helt enkelt en extern SSD med 1 eller 2 terabyte och använd den. En vanlig hårddisk kommer förmodligen att fungera, men du kan stöta på problem och det kommer att vara mycket långsammare.

![image](assets/1.png)

## Ladda ner Bitcoin Core

Gå till bitcoin.org (se till att inte gå till bitcoin.com, som är en shitcoin-webbplats ägd av Roger Ver, som lurar människor att köpa Bitcoin Cash istället för Bitcoin).

När du är där är det konstigt nog inte uppenbart var du kan få programvaran. Gå till resursmenyn och klicka på "Bitcoin Core", som visas nedan:

![image](assets/2.png)

Detta tar dig till nedladdningssidan:

![image](assets/3.png)

Klicka på den orangea knappen "Ladda ner Bitcoin Core":

![image](assets/4.png)

Det finns flera alternativ att välja mellan, beroende på din dator. De två första är relevanta för den här guiden; välj Windows eller Mac i vänstermenyn. Nedladdningen börjar efter att du har klickat på den, förmodligen i din nedladdningsmapp.

## Kontrollera nedladdningen (del 1)

Du behöver filen som innehåller hashvärden för olika versioner. Denna fil fanns tidigare på nedladdningssidan på bitcoin.org, men den har nu flyttats till bitcoincore.org/en/download:

![image](assets/5.png)
Du behöver SHA256-binärhashfilen. Denna fil innehåller SHA256-hasharna för olika nedladdningspaket för Bitcoin Core.
Därefter måste vi hasha nedladdningen av Bitcoin Core och jämföra den med vad filen säger att hashen ska vara. På så sätt kommer vi att veta att nedladdningen är identisk med vad som förväntas enligt bitcoincore.org.

Gå tillbaka till nedladdningsmappen och kör följande kommando (ersätt XXXXXXXXXXXX med det exakta namnet på Bitcoin Core fullständiga nodnedladdningsfilen):

```
FÖR MAC —–> shasum -a 256 XXXXXXXXXXXX
FÖR WINDOWS —–> certutil -hashfile XXXXXXXXXXX SHA256
```

Du kommer att få en hashresultat. Skriv ner detta och jämför det med hashen som finns i filen SHA256SUMS.
Om utgångarna är identiska har du verifierat att ingen data har ändrats... nästan. Vi måste fortfarande se till att SHA256SUMS-filen inte är skadlig.
För att gå vidare till nästa steg måste vi ha gpg installerat på vår dator.

För detta, se min SHA256/gpg-guide och bläddra till avsnittet "Ladda ner gpg" och leta sedan upp undertiteln för ditt operativsystem. Kom sedan tillbaka hit.

## Hämta den offentliga nyckeln

Återvänd till nedladdningssidan och hämta SHA256-hashsignaturfilen.

![image](assets/6.png)

Klicka på den och spara filen på disken, helst i nedladdningsmappen.

Denna fil innehåller signaturer från olika personer för SHA256SUMS-filen.

Vi vill ha huvudutvecklaren Wladimir J. van der Laans offentliga nyckel i vår nyckelring på datorn. Hans offentliga nyckel-ID är:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Kopiera denna text till följande kommando:

```
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Av nyfikenhet kan du när som helst se vilka nycklar som finns i datorns nyckelring med följande kommando:

```
gpg --list-keys
```

## Verifiera nedladdningen (del 2)

Vi har den offentliga nyckeln, nu kan vi verifiera SHA256SUMS-filen som innehåller hasharna för Bitcoin Core-nedladdningen, samt signeringen av dessa hashar.

Öppna Terminalen eller CMD igen och se till att du är i nedladdningsmappen. Kör sedan följande kommando:

```
gpg –verify SHA256SUMS.asc SHA256SUMS
```

Den första listade filen är den exakta stavningen av signaturfilen. Den andra listade filen bör vara den exakta stavningen av textfilen som innehåller hashvärdena. Båda filerna måste vara i samma katalog och du måste vara i filernas katalog, annars måste du ange den fullständiga sökvägen för varje fil.
Här är utdata du bör få:

![image](assets/7.png)

Det är säkert att ignorera varningsmeddelandet - det påminner bara om att du inte träffade Wladimir vid en viktig punkt och personligen frågade honom vilken hans publika nyckel var, och sedan sa till din dator att lita helt på den här nyckeln.

Om du har fått detta meddelande vet du nu att filen SHA256SUMS.asc inte har ändrats efter att Wladimir har signerat den.

## Installera Bitcoin Core

Du bör inte behöva detaljerade instruktioner om hur du installerar programmet.

![image](assets/8.png)

## Köra Bitcoin Core

På en Mac kan du få en varning (Apple är alltid anti-Bitcoin)

![image](assets/9.png)

Klicka på OK och öppna sedan dina Systeminställningar

![image](assets/10.png)

Klicka på ikonen för Säkerhet och integritet:

![image](assets/11.png)

Klicka sedan på "öppna ändå":

![image](assets/12.png)

Felet kommer att visas igen, men den här gången kommer du att ha en ÖPPNA-knapp tillgänglig. Klicka på den.

![image](assets/13.png)

Bitcoin Core bör laddas och du kommer att presenteras med några alternativ:

![image](assets/14.png)

Här kan du välja att använda standardvägen för nedladdning av blockkedjan, eller så kan du välja din externa hårddisk. Jag rekommenderar att du inte ändrar standardvägen om du använder interna hårddisken, det gör det enklare att konfigurera när du installerar annan programvara för att kommunicera med Bitcoin Core.
Du kan välja att köra en beskuren nod, det sparar utrymme men begränsar vad du kan göra med din nod. Hur som helst kommer du att ladda ner hela blockkedjan och verifiera den, så om du har utrymme, behåll det du har laddat ner och beskär det inte om du kan undvika det.

När du bekräftar kommer nedladdningen av blockkedjan att börja. Detta kommer att ta flera dagar.

![image](assets/15.png)

Du kan stänga av datorn och komma tillbaka för att fortsätta nedladdningen om du vill, det kommer inte att orsaka någon skada.
