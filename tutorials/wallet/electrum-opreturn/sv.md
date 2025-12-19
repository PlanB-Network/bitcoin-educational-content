---
name: Electrum OP_RETURN
description: Registrera ett meddelande om Blockchain Bitcoin med Electrum
---

![cover](assets/cover.webp)




Denna steg-för-steg-handledning visar hur du skriver ett meddelande på Blockchain Bitcoin med hjälp av Wallet Electrum. Denna operation använder OP_RETURN-instruktionen för att infoga text i en transaktion som är allmänt synlig på Blockchain. Följ dessa enkla steg för en lyckad registrering.



---
## Förkunskapskrav





- En dator (Windows, macOS eller Linux).
- Internetanslutning.
- Några satoshis (Sats) eller bitcoins (BTC) i din Wallet för att täcka transaktionsbeloppet och avgifterna.
- En text-till-hex-omvandlare (t.ex. en webbplats på nätet) eller ett särskilt verktyg som [denna OP_RETURN-skriptgenerator] (https://resources.davidcoen.it/opreturnelectrum/).



---

## Steg 1: Ladda ner och installera Electrum



![image](assets/fr/01.webp)



1. Besök Electrums officiella webbplats: [electrum.org](https://electrum.org/).


2. Ladda ner den version som motsvarar ditt operativsystem (Windows, macOS, Linux).


3. Installera Electrum enligt installatörens anvisningar.


4. Kontrollera integriteten för den nedladdade filen (valfritt, men rekommenderas av säkerhetsskäl) genom att jämföra filens signatur eller Hash.



→ Mer information om Electrum-handledningen :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Steg 2: Skapa eller importera en Wallet



1. Starta Electrum.


2. Välj Skapa en ny Wallet eller Återställ en befintlig Wallet om du redan har en seed-fras (återställningsfras).


3. Följ instruktionerna för att konfigurera din Wallet :




 - För en ny Wallet, anteckna din seed mening och förvara den på en säker plats (papper, kassaskåp, etc.).
 - För en befintlig Wallet anger du din seed-fras för att återställa den.


4. Ange ett lösenord för att skydda din Wallet.



→ Mer information om Electrum-handledningen :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Steg 3: Kontrollera tillgängliga medel



Se till att din Wallet innehåller tillräckligt med bitcoins (BTC) eller satoshis (Sats) för att :




- Transaktionsbelopp (t.ex. 0,00001 BTC eller 1000 Sats).
- Transaktionsavgifter, som varierar beroende på nätverkets storlek (i allmänhet några tusen Sats).



Konsultera balansen i Electrum för att kontrollera dina medel.



![image](assets/fr/02.webp)



Om det behövs, överför BTC eller Sats för att mata din Wallet. För att göra detta, gå till fliken "Mottagning" och klicka på "Skapa begäran" :



![image](assets/fr/03.webp)



Detta kommer att visa en mottagning Address:



![image](assets/fr/04.webp)



→ Mer information om Electrum-handledningen :



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Steg 4: Förbered det meddelande som ska skrivas in



Välj det meddelande som du vill skriva (t.ex. "Tack Satoshi"). Obs: OP_RETURN-meddelanden är begränsade till 80 byte, dvs. cirka 80 ASCII-tecken.



*Ta en stund att tänka: det du skriver på Blockchain Bitcoin är evigt och tillgängligt för alla, så :*




- lämna ett vackert uttryck för vår mänsklighet
- undvik att skriva innehåll som du kan ångra



*Blockchain-utrymme och dina bitcoins är värdefulla, använd dem klokt och med avsikt*



Konvertera ditt meddelande till hexadecimal :




- Du kan använda ett [onlineverktyg] (https://www.rapidtables.com/convert/number/ascii-to-hex.html), men var försiktig så att du inte behandlar känsliga uppgifter där (även om information som är avsedd att publiceras på Blockchain Bitcoin via en OP_RETURN i princip inte medför några sekretessproblem);
- För större konfidentialitet kan du utföra konverteringen lokalt med hjälp av en liten Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Exempel: `Tack Satoshi` i ASCII ger `5468616e6b73205361746f736869` i hexadecimal.



Förbered transaktionsskriptet. Här är ett exempel på det förväntade formatet:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



som består av :





- **Destination Address**: En giltig Bitcoin Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Detta kan vara din egen Address, om du vill återföra de överförda medlen till dig själv;
- **Överfört belopp**: beloppet för transaktionen, här `0.00001` BTC. **Observera**: eftersom enheten som används i Electrum är BTC, måste beloppet som anges i transaktionsskriptet också uttryckas i BTC, och inte i Sats ;
- Skript **OP_RETURN**: Meddelandet omvandlat till hexadecimal föregås av script(`OP_RETURN <messsage>), 0`. Här, `5468616e6b73205361746f736869` för meddelandet i hexadecimal.



⚠️ **Försiktighet**: Det är mycket viktigt att ange `0` efter OP_RETURN, eftersom denna opcode markerar skriptet som ogiltigt, vilket gör att utdata permanent inte kan användas. Nätverksnoder kommer att ta bort denna utdata från sin UTXO-uppsättning. Om du anger ett annat värde än `0` kommer det att vara oåterkalleligt förlorat: dina bitcoins kommer att betraktas som brända. Du bör därför alltid ange `0` med en OP_RETURN för att registrera önskad data, men utan att associera medel med den, vilket skulle gå förlorat.



Tips: Använd verktyget [OP_RETURN Generator] (https://resources.davidcoen.it/opreturnelectrum/) för att generate skriptet automatiskt. Även om det här verktyget föreslår att du anger beloppet i BTC, behåll enheten konfigurerad i Electrum.



![image](assets/fr/05.webp)



För att ändra den enhet som används av Electrum, hitta "Inställningar" i menyraden och välj sedan BTC / mBTC / bits eller Sats på fliken "Enheter":



![image](assets/fr/06.webp)




---

## Steg 5: Skicka transaktionen



I Electrum går du till fliken Skicka.



![image](assets/fr/07.webp)



I fältet "Pay to" klistrar du in det förberedda skriptet (t.ex. det ovan).



![image](assets/fr/08.webp)



Fältet "Pay to" ska visas i Green och transaktionsbeloppet ska visas på raden under.



Kontrollera beloppet och dess enhet i fältet Amount (Belopp).



Klicka på "Pay..." och justera dina transaktionsavgifter enligt det belopp du är villig att betala och den hastighet med vilken du vill att din transaktion ska behandlas av en Miner och integreras i ett block.



![image](assets/fr/09.webp)



Klicka på OK och bekräfta transaktionen med ditt lösenord. Ett bekräftelsefönster visas.




---

## Steg 6: Verifiera registreringen



När transaktionen har bekräftats (det kan ta några minuter) går du till fliken "Historik".



![image](assets/fr/10.webp)



Högerklicka på transaktionen och välj "Visa i Explorer" för att se detaljerna.



Alternativt kan du kopiera destinationen Address (till exempel `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) och visa den på en Blockchain-utforskare som [Mempool.space](https://Mempool.space/) eller [blockstream.info](https://blockstream.info/).



Titta efter OP_RETURN-fältet i transaktionsinformationen för att se ditt meddelande.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Tips och bästa praxis





- Testa med ett litet belopp: Börja med en liten transaktion (t.ex. Sats 1000) för att undvika kostsamma fel.
- Se till att utdata som innehåller OP_RETURN är lika med noll, annars kommer dina bitcoins att gå förlorade permanent.
- Kontrollera enheten: Kontrollera att det belopp som anges motsvarar den enhet som visas i Electrum (BTC, mBTC eller Sats).
- Transaktionsavgift: Om nätverket är överbelastat kan du höja avgiften för snabbare bekräftelse.
- Kort meddelande: OP_RETURN-poster är begränsade till 80 byte. Planera ditt meddelande i enlighet med detta.



---

## Användbara resurser





- Ladda ner Electrum: [electrum.org](https://electrum.org/)
- OP_RETURN skriptgenerator: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Utforskare: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)