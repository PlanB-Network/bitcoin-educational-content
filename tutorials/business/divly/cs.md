---
name: Divly
description: S Divly snadno vypočtete a přiznáte daně z kryptoměn, a to v plném souladu s daňovými předpisy.
---

![cover](assets/cover.webp)



## Úvod


Tento návod vysvětluje, jak pomocí [Divly](https://divly.com/) připravit daňové hlášení Bitcoin (BTC). Příprava daňového hlášení zahrnuje shromáždění všech relevantních transakcí BTC v daném finančním roce, výpočet zdanitelných zisků nebo příjmů a export hlášení, které lze předložit místnímu daňovému úřadu.


V jurisdikcích, kde Bitcoin podléhá daňovým pravidlům, musíte vykazovat zisky nebo ztráty z prodeje BTC a příjmy získané v BTC. Použití softwaru pro daňové výkaznictví vám pomůže tyto informace uspořádat a efektivně vygenerovat daňový výkaz.


## Začínáme


Začněme tím, že:



- Vytvořte si účet Divly.
- Nastavte **zemi daňové rezidence** a **místní měnu**.
- Zkontrolujte, zda tato nastavení odpovídají jurisdikci, ve které podáváte daňové přiznání.


Divly použije tuto konfiguraci k použití příslušných daňových pravidel a převodů měn při generování sestavy.


![img](assets/en/01.webp)


## Krok 1 - Import všech transakcí Bitcoin z vašich wallet a výměn


Před výpočtem daně je nutné importovat všechny transakce Bitcoin za dané zdaňovací období.


Divly podporuje více metod importu:



- Připojení API nebo OAuth** pro výměny nebo služby, které je podporují
- Nahrávání souborů CSV** ze zařízení wallet nebo z výměnných stanic
- Ruční zadávání** všech transakcí, na které se nevztahují automatizované metody


Ujistěte se, že jste importovali **všechny přítoky a odtoky BTC** relevantní pro vykazované zdaňovací období.


![img](assets/en/02.webp)


## Krok 2 - Kontrola importovaných transakcí


**Potvrzení zůstatku na kryptografickém účtu:**


Nejlépe začněte tím, že zkontrolujete, zda se celkový počet vámi vlastněných kryptoměn shoduje s číslem zobrazeným v Divly. Divly vypočítá váš majetek tak, že sečte všechny transakce, které jste importovali.


Začněte tím, že přejdete na stránku Přehled. Zkontrolujte, zda jsou jednotlivé uvedené kryptogramy skutečně číslem, které vlastníte. Divly v Přehledu nezobrazuje vaše fiat měny, takže je v tomto cvičení ignorujte.


Pokud najdete nějaké problémy, můžete je filtrovat podle wallet. To vám pomůže pochopit, které wallet mohou být nesynchronizované.


![img](assets/en/03.webp)


Po importu:



- Přejděte do sekce **Transakce**.
- Zkontrolujte, zda se každá transakce zobrazuje se správnými daty a částkami.
- V případě potřeby vyřešte chybějící upozornění na cenu nebo nákladový základ.


**Důležité:** Než přejdete k dalšímu kroku, ujistěte se, že jste do Divly importovali **VŠECHNY** své kryptografické transakce. Včetně studených wallet! Jinak hrozí, že vaše daně nebudou správné.


![img](assets/en/04.webp)


## Krok 3 - Kategorizace příslušných vkladů a výběrů


Různé typy kryptografických transakcí mohou mít odlišné daňové dopady. Patří mezi ně činnosti, jako je darování kryptoměny, ztracený majetek, odměny mining, fork, airdrops a podobné události. Je důležité, aby všechny transakce byly přesně kategorizovány.


Ve většině případů Divly automaticky přiřadí správné štítky. Pokud jsou však dostupná data o transakcích nedostatečná, nemusí být automatická klasifikace možná. V těchto situacích je povinností uživatele přiřadit příslušný štítek ručně. Chcete-li porozumět významu a daňovému režimu jednotlivých štítků, přečtěte si související článek nápovědy.


Chcete-li označit transakce, přejděte na stránku Transakce. Vyberte jednu nebo více transakcí a z rozevírací nabídky v horní části stránky vyberte správný štítek.


![img](assets/en/05.webp)


## Krok 4 - Generování daňového hlášení


Po importu a klasifikaci transakcí:



- Přejděte do části **Daňové hlášení**.
- Vyberte příslušný **daňový rok**.
- Zkontrolujte přehled vypočtených zisků, ztrát a kategorií příjmů.


Přehled agreguje zdanitelné události na základě importovaných údajů a klasifikací.


Rozhraní daňového hlášení Divly umožňuje před exportem potvrdit, že jsou zachyceny všechny transakce.


![img](assets/en/06.webp)


## Krok 5 - Export zprávy


Po přezkoumání:



- Exportujte dokončené daňové hlášení BTC ve formátu dostupném pro vaši zemi.
- Exportovaný soubor uložte nebo vytiskněte pro předložení daňovému úřadu.


![img](assets/en/07.webp)


V závislosti na jurisdikci může být nutné dodržovat zvláštní pokyny pro předkládání nebo používat formuláře specifické pro danou zemi. v případě potřeby vám s kroky při předkládání pomohou [Divlyho průvodci pro jednotlivé země](https://divly.com/en/guides).