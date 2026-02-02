---
term: Opakované použití adresy

definition: Nedoporučovaná praxe, která spočívá v opakovaném použití stejné Bitcoin adresy k přijetí plateb, což poškozuje soukromí tím, že umožňuje sledovat prostředky.
---
Opakované použití adresy označuje praxi, kdy se stejná přijímací adresa používá k blokování více UTXO, někdy v rámci několika různých transakcí. Bitcoiny jsou obvykle blokovány pomocí páru kryptografických klíčů, který odpovídá jedinečné adrese. Protože je blockchain veřejný, je snadné zjistit, které adresy jsou spojeny s kolika bitcoiny. V případě opakovaného použití stejné adresy pro více plateb je rozumné si představit, že všechny související UTXO patří stejnému subjektu. Opakované použití adresy proto představuje problém pro soukromí uživatele. Umožňuje deterministické vazby mezi vícenásobnými transakcemi a UTXO a také udržování sledování prostředků v řetězci. Tento problém zmínil již Satoshi Nakamoto ve své Bílé knize:

> *Jako dodatečný firewall by měl být pro každou transakci použit nový pár klíčů, aby se zabránilo jejich propojení se společným vlastníkem.*

Nakamoto, S. (2008). "*Bitcoin: A Peer-to-Peer Electronic Cash System*". https://bitcoin.org/bitcoin.pdf.

Pro zachování minimálního soukromí se důrazně doporučuje používat každou přijímací adresu pouze jednou. Pro každou novou platbu je vhodné vygenerovat novou adresu. Pro změnové výstupy by měla být rovněž použita nová adresa. Díky deterministickým a hierarchickým peněženkám je naštěstí velmi snadné používat více adres. Všechny páry klíčů spojené s peněženkou lze snadno přegenerovat ze seedu. To je také důvod, proč software peněženky po kliknutí na tlačítko "Přijmout" vždy vygeneruje novou, jinou adresu.
