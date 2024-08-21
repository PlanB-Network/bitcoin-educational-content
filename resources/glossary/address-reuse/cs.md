---
term: OPĚTOVNÉ POUŽITÍ ADRESY
---

Opětovné použití adresy odkazuje na praxi používání téže přijímací adresy pro blokování několika UTXO, někdy v rámci několika různých transakcí. Bitcoiny jsou typicky uzamčeny pomocí kryptografického páru klíčů, který odpovídá unikátní adrese. Jelikož je blockchain veřejný, je snadné vidět, které adresy jsou spojeny s kolika bitcoiny. V případě opětovného použití téže adresy pro více plateb je rozumné předpokládat, že všechna přidružená UTXO patří téže entitě. Proto opětovné použití adresy představuje problém pro soukromí uživatele. Umožňuje deterministické spojení mezi několika transakcemi a UTXO, stejně jako podporuje sledování fondů v blockchainu. Satoshi Nakamoto již tento problém zmínil ve své bílé knize:

> "*Jako dodatečný firewall by mohl být pro každou transakci použit nový pár klíčů, aby nebyly spojeny s jedním společným vlastníkem.*" - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Konzultováno na https://bitcoin.org/bitcoin.pdf.

Pro minimální zachování soukromí se důrazně doporučuje používat každou přijímací adresu pouze jednou. Pro každou novou platbu je vhodné generovat novou adresu. Pro výstupy změny by měla být také použita nová adresa. Naštěstí díky deterministickým a hierarchickým peněženkám se používání množství adres stalo velmi snadným. Všechny páry klíčů spojené s peněženkou lze snadno regenerovat ze seedu. To je také důvod, proč software peněženky vždy generuje novou, odlišnou adresu, když kliknete na tlačítko „Přijmout“.

> ► *V angličtině se tomu říká "Address Reuse".*