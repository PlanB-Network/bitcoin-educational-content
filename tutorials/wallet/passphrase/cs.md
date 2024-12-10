---
name: BIP39 Heslo
description: Porozumění tomu, jak heslo funguje
---
![cover](assets/cover.webp)

## Co je BIP39 heslo?

HD peněženky jsou typicky generovány z mnemonické fráze skládající se z 12 nebo 24 slov. Tato fráze je velmi důležitá, protože umožňuje obnovu všech klíčů peněženky v případě, že její fyzické médium (jako je například hardwarová peněženka) je ztraceno. Nicméně, tvoří jediný bod selhání, protože pokud je kompromitována, útočník by mohl ukrást všechny bitcoiny.

![PASSPHRASE BIP39](assets/notext/01.webp)

Zde přichází na řadu heslo. Jedná se o volitelné heslo, které si můžete svobodně zvolit, a které je přidáno k mnemonické frázi v procesu odvození klíčů, aby se zvýšila bezpečnost peněženky.

![PASSPHRASE BIP39](assets/notext/02.webp)

Buďte opatrní, abyste heslo nepletli s PIN kódem vaší hardwarové peněženky nebo s heslem používaným k odemčení přístupu k vaší peněžence na počítači. Na rozdíl od všech těchto prvků, heslo hraje roli v odvození klíčů vaší peněženky. **To znamená, že bez něj nikdy nebudete schopni obnovit své bitcoiny.**

Heslo pracuje v tandemu s mnemonickou frází, mění semeno, ze kterého jsou klíče generovány. Takže i když někdo získá vaši 12 nebo 24-slovnou frázi, bez hesla nemůže přistupovat k vašim prostředkům. **Použití hesla v podstatě vytváří novou peněženku s odlišnými klíči. Modifikace (i mírná) hesla vygeneruje jinou peněženku.**

## Proč byste měli používat heslo?

Heslo je libovolné a může být jakoukoliv kombinací znaků zvolenou uživatelem. Použití hesla tak nabízí několik výhod. Především snižuje všechna rizika spojená s kompromitací mnemonické fráze tím, že vyžaduje druhý faktor pro přístup k prostředkům (vloupání, přístup do vašeho domova atd.).

Dále může být strategicky použito k vytvoření návnadové peněženky, aby se vyrovnalo s fyzickými omezeními krádeže vašich prostředků, jako je proslulý "*útok klíčem za 5 dolarů*". V tomto scénáři je nápad mít peněženku bez hesla obsahující pouze malé množství bitcoinů, dostatečné k uspokojení potenciálního agresora, zatímco máte skrytou peněženku. Tato poslední používá stejnou mnemonickou frázi, ale je zabezpečena dodatečným heslem.

Nakonec, použití hesla je zajímavé, když si přejete kontrolovat náhodnost generování semene HD peněženky.

## Jak vybrat dobré heslo?
Aby bylo heslo účinné, musí být dostatečně dlouhé a náhodné. Stejně jako u silného hesla, doporučuji vybrat heslo, které je co nejdelší a nejvíce náhodné, s různorodostí písmen, čísel a symbolů, aby jakýkoliv útok hrubou silou byl nemožný.

Je také důležité toto heslo správně uložit, stejně jako mnemonickou frázi. **Ztráta znamená ztrátu přístupu k vašim bitcoinům**. Důrazně se radí proti pouhému zapamatování si ho ve vaší hlavě, protože to nerozumně zvyšuje riziko ztráty. Ideální je zapsat ho na fyzické médium (papír nebo kov) odděleně od mnemonické fráze. Tato záloha musí být samozřejmě uložena na jiném místě, než kde je uložena vaše mnemonická fráze, aby nebyly obě kompromitovány současně.

## Tutoriály

Pro nastavení hesla na zařízení Ledger (Stax, Flex, nebo Nano) můžete konzultovat tento tutoriál:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49