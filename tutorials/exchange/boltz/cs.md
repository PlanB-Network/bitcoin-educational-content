---
name: Boltz
description: Přepínání mezi různými vrstvami Bitcoin při zachování kontroly.
---


![cover](assets/cover.webp)



Od svého nasazení v roce 2009 se elektronický peněžní systém peer-to-peer Bitcoin exponenciálně rozrostl a dal život řešením, která dnes umožňují, aby se stal systémem, který můžeme okamžitě používat při našich každodenních činnostech, zejména prostřednictvím Lightning Network.



Mezi vrstvami protokolu Bitcoin však přetrvával zásadní problém: interoperabilita tekutin. Aby bylo možné plně využít potenciál protokolu Bitcoin, bylo nutné najít řešení, které by umožnilo transakce mezi jednotlivými vrstvami protokolu. Tato potřeba dala v roce 2019 vzniknout mostu Boltz, který propojuje několik vrstev protokolu Bitcoin.



## Co je Boltz?



[Boltz](https://boltz.Exchange) je platforma, která není určena pro všechny, kdo chtějí provádět transakce mezi různými vrstvami protokolu Bitcoin:




- on chain**: V hlavním řetězci Bitcoin, kde jsou transakce potvrzovány v průměru každých 10 minut, jsou transakční poplatky často vysoké, což nemusí nutně vyhovovat potřebám uživatelů;
- Lightning Network**: Překrytí Bitcoin pro okamžité platby za nízké poplatky, což umožňuje používat Bitcoin pro denní platby;
- Liquid Network**: překryvný nástroj pro Bitcoin vytvořený společností Blockstream, který umožňuje rychlé použití Confidential Transactions a použití dalších finančních nástrojů založených na Bitcoin;
- RootStock**: Řešení pro vývoj chytrých smluv založených na protokolu Bitcoin.



![layers](assets/fr/01.webp)



Interoperabilita mezi těmito různými vrstvami je velmi důležitá, protože poskytuje uživatelům flexibilitu, kterou potřebují k plnému využití všech výhod, které ekosystém Bitcoin nabízí.



Boltz používá atomické výměny. Tato technologie umožňuje výměnu bitcoinů mezi dvěma vrstvami (např. BTC onchain v Exchange za BTC v Lightningu) přímo mezi dvěma stranami, bez nutnosti důvěry a bez prostředníka. Tyto výměny se nazývají "atomické", protože mohou přinést pouze dva výsledky:




- Buď je transakce Exchange úspěšná a oba účastníci si fakticky vyměnili své BTC ;
- Buď Exchange selže, a oba účastníci odejdou se svými původními BTC.



Tímto způsobem si zachováváte trvalou vlastní péči o své bitcoiny a Exchange není založen na důvěře v protistranu: buď Exchange uspěje, nebo selže, ale žádná ze stran nemůže ukrást prostředky té druhé.



Atomický Exchange pracuje s inteligentními smlouvami [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). V tomto typu Contract je částka "uzamčena" v obousměrném kanálu a je zavedeno časové omezení, takže pokud transakce není dokončena do určité doby, zůstatek se vrátí vkladateli. Tento mechanismus používá platforma Boltz.



## Vaše první výměny se společností Boltz



Boltz je webová platforma, která není depozitářem a nevyžaduje od vás žádné osobní údaje. Boltz má minimalistický, plynulý Interface, který vám umožní začít obchodovat za méně než minutu.



![boltz](assets/fr/02.webp)



Po vstupu na platformu můžete vytvářet atomické výměny mezi různými vrstvami ekosystému Bitcoin.



![home](assets/fr/03.webp)



Uvidíte minimální a maximální počet satošů (nejmenší jednotka Bitcoin), se kterými můžete obchodovat prostřednictvím služby Boltz, včetně síťových poplatků a procenta, které si společnost Boltz účtuje, ve výši 0,1 % až 0,5 %.



![fees](assets/fr/04.webp)



Poté vyberte Layer, ze kterého chcete vytvořit atomový Exchange, a vyberte Layer, na který chcete bitcoiny přijmout.



![couches](assets/fr/05.webp)



V tomto tutoriálu se zaměříme na atomovou Exchange z hlavní Layer na Lightning Network.



Základní jednotku můžete nakonfigurovat pro své ústředny výběrem z možností :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Jakmile dokončíte základní konfigurace, vložte částku svého atomového účtu Exchange a poté vytvořte bleskový účet Invoice pro odpovídající částku nebo jednoduše vložte svůj LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Pro jistotu zkontrolujte parametry svého atomového Exchange, abyste mohli exportovat záložní klíče spojené s vaším Exchange.



Na ikoně **Nastavení** stáhněte záložní klíč a soubor vhodně uložte.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Tento soubor obsahuje 12 klíčových slov portfolia přidruženého k vašim atomovým burzám.



Poté klikněte na tlačítko **Vytvořit atomovou Exchange** a pokračujte v platbě uvedené částky.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Po provedení a potvrzení platby obdržíte automaticky odpovídající částku na účet Lightning Wallet.



V nabídce **Vrácení peněz** najděte historii atomového kódu Exchange a určete kód Exchange, u kterého si přejete vrátit peníze. Můžete také importovat historii výměn, které jste provedli na jiném zařízení, například pomocí souboru záložního klíče spojeného s těmito výměnami.



![refund](assets/fr/11.webp)



V nabídce **Historie** si můžete stáhnout podrobnější historii výměn spojených s vaším záchranným klíčem kliknutím na tlačítko **Zálohovat**.



![backup](assets/fr/12.webp)



⚠️ Ani tento soubor neprozrazujte, protože obsahuje všechny informace spojené s vašimi transakcemi a záložní klíč, který je s těmito transakcemi spojen.



Boltz nabízí vysokou úroveň důvěrnosti díky přístupu přes odkaz `.onion` v síti Tor. Atomové výměny můžete provádět zcela anonymně výběrem nabídky **Onion** po aktivaci procházení přes Tor v prohlížeči.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Nyní již znáte Boltz, jedinečnou platformu Exchange, která umožňuje interoperabilitu mezi různými vrstvami ekosystému Bitcoin.