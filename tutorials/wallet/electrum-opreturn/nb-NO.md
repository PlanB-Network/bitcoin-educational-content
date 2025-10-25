---
name: Electrum OP_RETURN
description: Registrer en melding på Blockchain Bitcoin med Electrum
---

![cover](assets/cover.webp)




Denne trinnvise veiledningen viser deg hvordan du skriver en melding på Blockchain Bitcoin ved hjelp av Wallet Electrum. Denne operasjonen bruker OP_RETURN-instruksjonen til å sette inn tekst i en transaksjon som er offentlig synlig på Blockchain. Følg disse enkle trinnene for å få en vellykket registrering.



---
## Forutsetninger





- En datamaskin (Windows, macOS eller Linux).
- Internett-tilkobling.
- Noen satoshier (Sats) eller bitcoins (BTC) i Wallet for å dekke transaksjonsbeløpet og gebyrene.
- En tekst-til-hex-omformer (f.eks. et nettsted på nettet) eller et dedikert verktøy som [denne OP_RETURN-skriptgeneratoren] (https://resources.davidcoen.it/opreturnelectrum/).



---

## Trinn 1: Last ned og installer Electrum



![image](assets/fr/01.webp)



1. Besøk Electrums offisielle nettsted: [electrum.org](https://electrum.org/).


2. Last ned den versjonen som passer til operativsystemet ditt (Windows, macOS, Linux).


3. Installer Electrum i henhold til installatørens instruksjoner.


4. Kontroller integriteten til den nedlastede filen (valgfritt, men anbefales av sikkerhetshensyn) ved å sammenligne filens signatur eller Hash.



→ Mer informasjon om Electrum-veiledningen :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Trinn 2: Opprett eller importer en Wallet



1. Start Electrum.


2. Velg Opprett en ny Wallet eller Gjenopprett en eksisterende Wallet hvis du allerede har en seed-frase (gjenopprettingsfrase).


3. Følg instruksjonene for å konfigurere Wallet :




 - For en ny Wallet må du notere ned seed-setningen og oppbevare den på et trygt sted (papir, safe osv.).
 - For en eksisterende Wallet skriver du inn seed-frasen din for å gjenopprette den.


4. Angi et passord for å sikre Wallet.



→ Mer informasjon om Electrum-veiledningen :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Trinn 3: Sjekk tilgjengelige midler



Sørg for at Wallet inneholder nok bitcoins (BTC) eller satoshier (Sats) til å :




- Transaksjonsbeløp (for eksempel 0,00001 BTC eller 1000 Sats).
- Transaksjonsgebyrer, som varierer avhengig av størrelsen på nettverket (vanligvis noen få tusen Sats).



Se saldoen i Electrum for å sjekke midlene dine.



![image](assets/fr/02.webp)



Overfør BTC eller Sats for å mate Wallet om nødvendig. Dette gjør du ved å gå til "Mottak"-fanen og klikke på "Opprett forespørsel":



![image](assets/fr/03.webp)



Dette vil vise et mottak Address:



![image](assets/fr/04.webp)



→ Mer informasjon om Electrum-veiledningen :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Trinn 4: Forbered meldingen som skal skrives inn



Velg meldingen du ønsker å legge inn (f.eks. `Takk Satoshi`). Merk: OP_RETURN-meldinger er begrenset til 80 byte, dvs. ca. 80 ASCII-tegn.



*Ta deg tid til å tenke: Det du skriver på Blockchain Bitcoin er evig og tilgjengelig for alle, så :*




- etterlater et vakkert uttrykk for vår menneskelighet
- unngå å legge inn innhold du kanskje vil angre på



*Blockchain-plassen og bitcoinsene dine er dyrebare, bruk dem klokt og med hensikt*



Konverter meldingen din til heksadesimal :




- Du kan bruke et [online-verktøy] (https://www.rapidtables.com/convert/number/ascii-to-hex.html), men vær forsiktig med å behandle sensitive data der (selv om informasjon som skal publiseres på Blockchain Bitcoin via en OP_RETURN, i prinsippet ikke byr på noen konfidensialitetsproblemer);
- For større konfidensialitet kan du utføre konverteringen lokalt ved hjelp av en liten Python :



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



Eksempel: `Takk Satoshi` i ASCII gir `5468616e6b7320536361746f736869` i heksadesimal.



Forbered transaksjonsskriptet. Her er et eksempel på det forventede formatet:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



som består av :





- **Destinasjon Address**: En gyldig Bitcoin Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Dette kan være din egen Address, hvis du ønsker å returnere de overførte midlene til deg selv;
- **Overført beløp**: transaksjonsbeløpet, her `0,00001` BTC. **Vær oppmerksom på**: siden enheten som brukes i Electrum er BTC, må beløpet som er angitt i transaksjonsskriptet også uttrykkes i BTC, og ikke i Sats ;
- Skript **OP_RETURN**: Meldingen konvertert til heksadesimal innledes med script(`OP_RETURN <messsage>), 0`. Her, `5468616e6b73205361746f736869` for meldingen i heksadesimal.



⚠️ **Forsiktighetsregler**: Det er svært viktig å angi `0` etter OP_RETURN, da denne opkoden markerer skriptet som ugyldig, noe som gjør utdataene permanent ubrukelige. Nettverksnoder vil slette denne utdataen fra UTXO-settet sitt. Hvis du skriver inn en annen verdi enn `0`, vil den være ugjenkallelig tapt: bitcoinsene dine vil bli ansett som brent. Du bør derfor alltid angi `0` med en OP_RETURN for å registrere de ønskede dataene, men uten å knytte midler til dem, som vil gå tapt.



Tips: Bruk verktøyet [OP_RETURN Generator] (https://resources.davidcoen.it/opreturnelectrum/) for å generate skriptet automatisk. Selv om dette verktøyet foreslår å angi beløpet i BTC, må du beholde enheten konfigurert i Electrum.



![image](assets/fr/05.webp)



For å endre enheten som brukes av Electrum, finn "Preferences" i menylinjen, og velg deretter BTC / mBTC / bits eller Sats i fanen "Units" :



![image](assets/fr/06.webp)




---

## Trinn 5: Send transaksjonen



I Electrum går du til Send-fanen.



![image](assets/fr/07.webp)



Lim inn det forberedte skriptet (for eksempel det ovenfor) i "Betal til"-feltet.



![image](assets/fr/08.webp)



Feltet "Betal til" skal vises i Green, og transaksjonsbeløpet skal vises på linjen under.



Kontroller beløpet og enheten i Beløp-feltet.



Klikk på "Betal ..." og juster transaksjonsgebyrene i henhold til beløpet du er villig til å betale, og hvor raskt du vil at transaksjonen skal behandles av en Miner og integreres i en blokk.



![image](assets/fr/09.webp)



Klikk på OK, og bekreft transaksjonen med passordet ditt. Et bekreftelsesvindu vises.




---

## Trinn 6: Bekreft registreringen



Når transaksjonen er bekreftet (dette kan ta noen minutter), går du til "Historikk"-fanen.



![image](assets/fr/10.webp)



Høyreklikk på transaksjonen og velg "Vis i utforskeren" for å se detaljene.



Alternativt kan du kopiere destinasjonen Address (for eksempel `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) og vise den i en Blockchain-utforsker, for eksempel [Mempool.space](https://Mempool.space/) eller [blockstream.info](https://blockstream.info/).



Se etter OP_RETURN-feltet i transaksjonsdetaljene for å se meldingen din.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Tips og beste praksis





- Test med et lite beløp: Begynn med en liten transaksjon (f.eks. Sats 1000) for å unngå kostbare feil.
- Sørg for at utdataene som inneholder OP_RETURN er lik null, ellers vil bitcoinsene dine gå tapt permanent.
- Kontroller enheten: Kontroller at beløpet som er angitt, samsvarer med enheten som vises i Electrum (BTC, mBTC eller Sats).
- Transaksjonsgebyr: Hvis nettverket er overbelastet, kan du øke avgiften for raskere bekreftelse.
- Kort melding: OP_RETURN-oppføringer er begrenset til 80 byte. Planlegg meldingen din deretter.



---

## Nyttige ressurser





- Last ned Electrum: [electrum.org] (https://electrum.org/)
- OP_RETURN skriptgenerator: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Explorers: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)