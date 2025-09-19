---
name: "Bitcoin Core (macOS & Windows)"
description: Installera Bitcoin Core på Mac eller Windows
---

![cover](assets/cover.webp)

Att installera Bitcoin Core på din vanliga dator kan göras, men det är inte idealiskt. Om du inte har något emot att lämna din dator på 24/7, kommer det här att fungera bra. Om du behöver stänga av datorn blir det irriterande att vänta på att programvaran ska synkroniseras varje gång du slår på den igen.


Dessa instruktioner är för Mac- eller Windows-användare. Linux-användare behöver troligen inte min hjälp, men instruktionerna för Linux är mycket lika Mac.


## Börja rent


Helst vill du använda en ren dator, en utan skadlig kod. Även om du använder en Hardware Wallet kan skadlig kod lura dig på dina mynt.


Du kan antingen rensa en gammal dator och använda den som en dedikerad Bitcoin-dator eller köpa en dedikerad dator/laptop.


## Hard-enheten


Bitcoin Core kommer att ta upp cirka 400 gigabyte data på din hårddisk och kommer att fortsätta växa. Du kan använda din interna enhet, men du kan också ansluta en extern Hard-enhet. Jag ska förklara båda alternativen. Helst bör du använda en solid state-enhet. Om du har en gammal dator har den förmodligen inte en av dessa internt. Köp bara en extern SSD på 1 eller 2 terabyte och använd den. Den vanliga enheten kommer förmodligen att fungera, men du kan få problem och det kommer att bli mycket långsammare.


![image](assets/fr/01.webp)


## Ladda ner Bitcoin Core


Gå till Bitcoin.org (se till att du inte går till Bitcoin.com, som är en shitcoin-webbplats som ägs av Roger Ver, som lurar människor att köpa Bitcoin Cash istället för Bitcoin)


Väl där är det konstigt nog inte uppenbart var man får tag på programvaran. Gå till resursmenyn och klicka på "Bitcoin Core", som visas nedan:


![image](assets/fr/02.webp)


Du kommer då till nedladdningssidan:


![image](assets/fr/03.webp)


Klicka på den orangefärgade knappen Download Bitcoin Core:


![image](assets/fr/04.webp)


Det finns flera alternativ att välja mellan, beroende på vilken dator du har. De två första är relevanta för den här guiden; välj Windows eller Mac i den vänstra fältet. När du klickar på filen börjar den laddas ner, troligen till din katalog för nedladdningar.


## Verifiera nedladdningen (del 1)


Du behöver filen som innehåller hasharna för de olika utgåvorna. Den här filen fanns tidigare på nedladdningssidan på Bitcoin.org, men har nu flyttats till bitcoincore.org/en/download:


![image](assets/fr/05.webp)


Du behöver filen SHA256 binära hashes. Den här filen innehåller SHA256-hasharna för de olika nedladdningspaketen för Bitcoin Core.


Därefter måste vi Hash Bitcoin Core-nedladdningen och jämföra den med vad filen säger att Hash ska vara. Då vet vi att nedladdningen är identisk med vad som förväntas, enligt bitcoincore.org.


Navigera till katalogen Downloads igen och kör det här kommandot (ersätt X med det exakta namnet på nedladdningsfilen för Full node Bitcoin):


```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```


Du kommer att få en Hash-utdata. Notera den och jämför den med den Hash som finns i SHA256SUMS-filen.


Om utdata är identiska har du verifierat att ingen bit av data har manipulerats... nästan. Vi måste fortfarande vara säkra på att SHA256SUMS-filen inte är skadlig.


För att gå vidare till nästa steg måste vi ha gpg installerat på vår dator.


För att göra det, se min SHA256/gpg-guide, och bläddra ungefär halvvägs till avsnittet "Ladda ner gpg" och leta efter underrubriken för ditt operativsystem. Kom sedan tillbaka hit.


## Hämta den offentliga nyckeln


Tillbaka på nedladdningssidan, hämta SHA256 Hash-signaturfilen


![image](assets/fr/06.webp)


Klicka på den och spara filen på hårddisken, helst i katalogen Downloads.


Den här filen innehåller signaturer av olika personer, av SHA256SUMS-filen.


Vi vill ha huvudutvecklarens publika nyckel, Wladimir J. van der Laan, på vår dators nyckelring. Hans publika nyckel-ID är:

1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964


Kopiera den texten till följande kommando:


```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```


Av intresse kan du när som helst se vilka nycklar som finns i datorns nyckelring med det här kommandot:


```bash
gpg --list-keys
```


## Verifiera nedladdningen (del 2)


Vi har den offentliga nyckeln, så vi kan nu verifiera SHA256SUMS-filen som innehåller hasharna för Bitcoin Core-nedladdningen och signaturen för dessa hashar.


Öppna Terminal eller CMD igen och se till att du befinner dig i katalogen Downloads. Därifrån kör du det här kommandot:


```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```


Den första listade filen är den exakta stavningen av signaturfilen. Den andra listade filen bör vara den exakta stavningen av textfilen som innehåller hasharna. Båda filerna ska finnas i samma katalog och du måste befinna dig i filernas katalog, annars måste du skriva ut den fullständiga sökvägen för varje fil.


Detta är vad du bör få ut


![image](assets/fr/07.webp)


Det är säkert att ignorera varningsmeddelandet - det påminner dig bara om att du inte har träffat Wladimir vid en nyckeldel och personligen frågat honom vad hans offentliga nyckel var och sedan sagt till din dator att lita på den här nyckeln helt.


Om du fick det här meddelandet vet du nu att filen SHA256SUMS.asc inte har manipulerats efter att Wladimir signerade den.


## Installera Bitcoin-kärna


Du ska inte behöva detaljerade instruktioner om hur du installerar programmet.


![image](assets/fr/08.webp)


## Körning Bitcoin Kärnan


På en Mac kan du få en varning (Apple är fortfarande emot Bitcoin)


![image](assets/fr/09.webp)


Klicka på OK och öppna sedan dina Systeminställningar


![image](assets/fr/10.webp)


Klicka på ikonen för säkerhet och sekretess:


![image](assets/fr/11.webp)


Klicka sedan på "öppna ändå":


![image](assets/fr/12.webp)


Felet kommer att visas igen, men den här gången har du en OPEN-knapp tillgänglig. Klicka på den.


![image](assets/fr/13.webp)


Bitcoin Core bör laddas och du kommer att presenteras med några alternativ:


![image](assets/fr/14.webp)


Här kan du välja att använda standardsökvägen för var Blockchain kommer att laddas ner till, eller så kan du välja din externa enhet. Jag rekommenderar att du inte ändrar standardsökvägen om du ska använda den interna enheten, det gör det lättare att ställa in när du installerar annan programvara för att kommunicera med Bitcoin Core.


Du kan välja att köra en beskuren nod, det sparar utrymme, men begränsar vad du kan göra med din nod. Hur som helst kommer du att ladda ner hela Blockchain och verifiera den ändå, så om du har utrymme, behåll det du laddade ner och beskär inte om du kan undvika det.


När du har bekräftat kommer Blockchain att börja laddas ner. Det kommer att ta många dagar.


![image](assets/fr/15.webp)


Du kan stänga av datorn och komma tillbaka för att ladda ner om du vill, det kommer inte att göra någon skada.
