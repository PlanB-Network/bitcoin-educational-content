---
name: Electrum OP_RETURN
description: Registrace zprávy na Blockchain Bitcoin pomocí Electrum
---

![cover](assets/cover.webp)




Tento návod vám krok za krokem ukáže, jak napsat zprávu na Blockchain Bitcoin pomocí Wallet Electrum. Tato operace využívá instrukci OP_RETURN k vložení textu do transakce, která je veřejně viditelná na Blockchain. Pro úspěšný zápis postupujte podle těchto jednoduchých kroků.



---
## Předpoklady





- Počítač (Windows, macOS nebo Linux).
- Připojení k internetu.
- Několik satošů (Sats) nebo bitcoinů (BTC) v Wallet na pokrytí částky transakce a poplatků.
- Převodník textu na hexadecimální znaky (např. online stránka) nebo specializovaný nástroj, jako je [tento generátor skriptů OP_RETURN](https://resources.davidcoen.it/opreturnelectrum/).



---

## Krok 1: Stáhněte si a nainstalujte Electrum



![image](assets/fr/01.webp)



1. Navštivte oficiální webové stránky společnosti Electrum: [electrum.org](https://electrum.org/).


2. Stáhněte si verzi odpovídající vašemu operačnímu systému (Windows, macOS, Linux).


3. Nainstalujte Electrum podle pokynů instalátoru.


4. Zkontrolujte integritu staženého souboru (nepovinné, ale doporučené z bezpečnostních důvodů) porovnáním podpisu souboru nebo Hash.



→ Další podrobnosti v tutoriálu Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Krok 2: Vytvoření nebo importování souboru Wallet



1. Spusťte Electrum.


2. Pokud již máte frázi seed (frázi pro obnovení), vyberte možnost Vytvořit novou frázi Wallet nebo Obnovit existující frázi Wallet.


3. Při konfiguraci zařízení Wallet postupujte podle pokynů:




 - V případě nové verze Wallet si poznamenejte větu seed a uschovejte ji na bezpečném místě (papír, trezor apod.).
 - Pro obnovení stávajícího modelu Wallet zadejte frázi seed.


4. Nastavte heslo pro zabezpečení účtu Wallet.



→ Další podrobnosti v tutoriálu Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Krok 3: Zkontrolujte dostupné finanční prostředky



Ujistěte se, že váš Wallet obsahuje dostatek bitcoinů (BTC) nebo satošů (Sats), abyste :




- Výše transakce (například 0,00001 BTC nebo 1000 Sats).
- Transakční poplatky, které se liší podle velikosti sítě (obvykle několik tisíc Sats).



Zůstatek v Electru si můžete zkontrolovat.



![image](assets/fr/02.webp)



V případě potřeby převeďte BTC nebo Sats a nakrmte jimi Wallet. To provedete tak, že přejdete na kartu "Přijmout" a kliknete na "Vytvořit požadavek" :



![image](assets/fr/03.webp)



Zobrazí se příjem Address:



![image](assets/fr/04.webp)



→ Další podrobnosti v tutoriálu Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Krok 4: Připravte zprávu, která má být napsána



Vyberte zprávu, kterou chcete zadat (např. `Díky Satoshi`). Poznámka: Zprávy OP_RETURN jsou omezeny na 80 bajtů, tj. přibližně 80 znaků ASCII.



*Zamyslete se: to, co napíšete na Blockchain Bitcoin, je věčné a přístupné všem, takže :*




- zanechat krásný výraz naší lidskosti,*
- vyhněte se zadávání obsahu, kterého byste mohli litovat*



*Blockchain prostor a vaše bitcoiny jsou cenné, používejte je moudře a s rozmyslem*



Převeďte svou zprávu do šestnáctkové soustavy :




- Můžete použít [online nástroj](https://www.rapidtables.com/convert/number/ascii-to-hex.html), ale buďte opatrní, abyste v něm nezpracovávali citlivé údaje (i když informace určené ke zveřejnění na Blockchain Bitcoin prostřednictvím OP_RETURN v zásadě nepředstavují žádný problém s důvěrností);
- Pro větší důvěrnost proveďte převod lokálně pomocí malého programu Python :



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



Příklad: `Díky Satoshi` v ASCII dává `5468616e6b73205361746f736869` v šestnáctkové soustavě.



Připravte transakční skript. Zde je příklad očekávaného formátu:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



který se skládá z :





- Cílová destinace Address**: Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Může to být váš vlastní Address, pokud si přejete převáděné prostředky vrátit sami sobě;
- Převedená částka**: částka transakce, zde `0.00001` BTC. **Upozornění**: Vzhledem k tomu, že jednotkou používanou v systému Electrum je BTC, musí být částka uvedená ve skriptu transakce rovněž vyjádřena v BTC, a nikoli v Sats ;
- Skript OP_RETURN**: Zpráva převedená do hexadecimální podoby, které předchází script(`OP_RETURN <messsage>), 0`. Zde `5468616e6b73205361746f736869` pro zprávu v šestnáctkové soustavě.



⚠️ **Upozornění**: Je velmi důležité uvést `0` za OP_RETURN, protože tento opkód označuje skript jako neplatný, čímž se výstup trvale znehodnotí. Síťové uzly tento výstup vymažou ze své sady UTXO. Pokud zadáte jinou hodnotu než `0`, bude nenávratně ztracena: vaše bitcoiny budou považovány za spálené. Měli byste proto vždy zadat `0` u OP_RETURN, abyste zaznamenali požadovaný údaj, ale nepřiřadili k němu finanční prostředky, které by byly ztraceny.



Tip: Pomocí nástroje [OP_RETURN Generator] (https://resources.davidcoen.it/opreturnelectrum/) můžete skript generate vytvořit automaticky. I když tento nástroj navrhuje zadat částku v BTC, ponechte jednotku nakonfigurovanou v Electrum.



![image](assets/fr/05.webp)



Chcete-li změnit jednotku, kterou Electrum používá, najděte v nabídce "Preferences" a na kartě "Units" vyberte BTC / mBTC / bits nebo Sats :



![image](assets/fr/06.webp)




---

## Krok 5: Odeslání transakce



V aplikaci Electrum přejděte na kartu Odeslat.



![image](assets/fr/07.webp)



Do pole "Pay to" vložte připravený skript (například výše uvedený).



![image](assets/fr/08.webp)



Pole "Zaplatit komu" by se mělo zobrazit ve formátu Green a částka transakce by se měla objevit na řádku pod ním.



Zkontrolujte částku a její jednotku v poli Částka.



Klikněte na "Zaplatit..." a upravte poplatky za transakci podle částky, kterou jste ochotni zaplatit, a rychlosti, s jakou má být transakce zpracována společností Miner a začleněna do bloku.



![image](assets/fr/09.webp)



Klikněte na tlačítko OK a potvrďte transakci svým heslem. Zobrazí se potvrzovací okno.




---

## Krok 6: Ověření registrace



Po potvrzení transakce (může to trvat několik minut) přejděte na kartu "Historie".



![image](assets/fr/10.webp)



Klikněte na transakci pravým tlačítkem myši a vyberte možnost "Zobrazit v Průzkumníku", abyste si mohli prohlédnout podrobnosti.



Případně zkopírujte cílový soubor Address (například `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) a zobrazte jej v průzkumníku Blockchain, například [Mempool.space](https://Mempool.space/) nebo [blockstream.info](https://blockstream.info/).



V podrobnostech o transakci vyhledejte pole OP_RETURN, kde se zobrazí vaše zpráva.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Tipy a osvědčené postupy





- Vyzkoušejte malé množství: Sats 1000), abyste se vyhnuli nákladným chybám.
- Ujistěte se, že výstup obsahující OP_RETURN je roven nule, jinak budou vaše bitcoiny trvale ztraceny.
- Zkontrolujte jednotku: Zkontrolujte, zda zadaná částka odpovídá jednotce zobrazené v Electrumu (BTC, mBTC nebo Sats).
- Transakční poplatek: Pokud je síť přetížená, zvyšte poplatek za rychlejší potvrzení.
- Krátká zpráva: Záznamy OP_RETURN jsou omezeny na 80 bajtů. Podle toho si naplánujte svou zprávu.



---

## Užitečné zdroje





- Stáhnout Electrum: [electrum.org](https://electrum.org/)
- Generátor skriptů OP_RETURN: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Explorers: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)