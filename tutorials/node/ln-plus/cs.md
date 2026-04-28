---
name: Lightning Network+
description: Získejte bezplatnou příchozí likviditu s kooperativním otevřením uzlu Lightning
---

![cover](assets/cover.webp)



## Úvod



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) je komunitní platforma určená k usnadnění spolupráce mezi provozovateli uzlů Lightning Network. Jejím hlavním cílem je zlepšit propojení, likviditu a decentralizaci sítě Lightning bez potřeby centralizovaných zprostředkovatelů.



Tento tutoriál se zaměří na službu **"Swaps "**, která je dnes nejpoužívanější a nejstrukturovanější funkcí systému LN+. Představeny budou také další služby, které platforma nabízí.



## Přehled LN+



### Co je Lightning Network Plus?



Lightning Network Plus (LN+) je komunitní platforma pro provozovatele bleskových uzlů, kteří chtějí spolupracovat přímo a dobrovolně. Jejím cílem je usnadnit vytváření užitečných, vyvážených a udržitelných kanálů Lightning a zároveň se vyhnout potřebě centralizovaných řešení nebo vnucených uzlů.



LN+ je založen na základním principu: vzájemné spolupráci založené na transparentnosti, reciprocitě a dobré pověsti.



### Přehled služeb LN+



LN+ nabízí několik služeb určených ke zlepšení topologie a likvidity sítě Lightning, včetně :





- Swapy**: vzájemné otevření kanálů mezi operátory (hlavní služba).
- Kruhy**: kruhové otvory v kanálech mezi několika účastníky.
- Swapy založené na důvěře**: varianty, které se více spoléhají na důvěru a historii účastníků.
- Sociální funkce**: profily, komentáře a systém reputace.



Ve zbývající části tohoto návodu se zaměříme výhradně na službu **Swaps**, která je základem současného používání systému LN+.



## Služba LN+ "Swaps"



### Definice výměny LN+



**Výměna** LN+ je dobrovolná dohoda mezi dvěma provozovateli uzlů Lightning o vzájemném otevření kanálů Lightning s rovnocennou (nebo předem dohodnutou) kapacitou. Na rozdíl od běžného jednostranného otevření kanálu je výměna založena na **výslovné reciprocitě**.



V praxi :





- Otevřete kanál do uzlu svého partnera.
- Váš partner otevře kanál do vašeho uzlu.
- Obě strany vážou podobné množství bitcoinů on-chain.



### K čemu slouží swapy pro operátory uzlů?



Služba Swaps řeší několik klíčových problémů, se kterými se provozovatelé bleskových systémů setkávají:





- Vylepšená konektivita**: vytváření užitečných obousměrných kanálů ihned po jejich otevření.
- Lepší řízení likvidity**: každá strana má příchozí i odchozí kapacitu.
- Snížení rizika zbytečných kanálů**: partner je podporován v tom, aby kanál zůstal otevřený.
- Větší decentralizace**: přímá spojení mezi operátory bez vnucených uzlů.



### Pro které profily uzlů jsou swapy užitečné?



Swapy jsou užitečné zejména pro :





- Nové uzly, které chtějí rychle zlepšit svou směrovatelnost.
- Zprostředkovatelské subjekty, které chtějí zvýšit hustotu svého kanálu.
- Uzly orientované na směrování, které chtějí optimalizovat svou topologii.



## Připojení uzlu Lightning ke LN+



### Technické požadavky



Než začnete, budete potřebovat :





- Funkční uzel Lightning (LND, Core Lightning nebo Eclair).
- Přístup k rozhraní pro správu uzlu.
- Dostatečná kapacita on-chain pro otevření kanálů.



Přejděte na webové stránky [Lightning Network](https://lightningnetwork.plus/) Plus a klikněte na tlačítko `Přihlášení` v pravém horním rohu rozhraní.



![capture](assets/fr/03.webp)



### Ověřování pomocí podpisu zprávy



Chcete-li se ověřit, musíte poskytnutou zprávu podepsat pomocí soukromého klíče uzlu Lightning. Pomocí ThunderHub je tato operace velmi jednoduchá.



Začněte zkopírováním zprávy zobrazené programem LN+.



![capture](assets/fr/04.webp)



V aplikaci ThunderHub přejděte na kartu `Nástroje` a v části `Zprávy` klikněte na tlačítko `Podepsat`.



![capture](assets/fr/05.webp)



Vložte ověřovací zprávu poskytnutou společností LN+ a klikněte na tlačítko `Podepsat`.



![capture](assets/fr/06.webp)



ThunderHub pak tuto zprávu podepíše pomocí soukromého klíče vašeho uzlu. Zkopírujte vygenerovaný podpis.



![capture](assets/fr/07.webp)



Vložte tento podpis do příslušného pole na webu LN+ a klikněte na tlačítko `Přihlásit se`.



![capture](assets/fr/08.webp)



Nyní jste připojeni ke LN+ pomocí uzlu Lightning. Tento proces umožňuje společnosti LN+ ověřit, že jste právoplatným vlastníkem uzlu, o který žádáte na její platformě.



![capture](assets/fr/09.webp)



Pokud chcete, můžete si profil LN+ přizpůsobit, například přidáním krátkého životopisu.



## Účast na stávajícím swapu



### Přístup ke swapovým nabídkám



Chcete-li se zúčastnit prvního otevření kanálu, přejděte do nabídky `Swaps` v horní části rozhraní. Zde naleznete všechny aktuálně dostupné swapy v závislosti na vlastnostech vašeho uzlu.



![capture](assets/fr/10.webp)



### Podmínky způsobilosti



Chcete-li se připojit k existující nabídce swapu, stačí vybrat příslušný inzerát a zaregistrovat se. Služba LN+ však umožňuje tvůrci swapu definovat určité **podmínky způsobilosti**, jako např:





- minimální počet již otevřených kanálů ;
- minimální celková kapacita uzlu ;
- některé typy připojení jsou akceptovány.



### Nedávné uzly



V důsledku toho je možné, že zejména v počátečních fázích používání bude pro váš uzel k dispozici **málo nabídek** nebo žádné. To je běžná situace u nových nebo dosud nepřipojených uzlů.



V mém případě i přes existenci několika otevřených kanálů žádná z nabídek nesplňovala požadovaná kritéria.



## Vytvořte si vlastní nabídku výměny



### Kdy byste měli vytvořit vlastní výměnu?



Pokud není k dispozici žádná existující nabídka, je často nejlepším řešením vytvoření vlastní výměny. Umožňuje vám také zachovat si kontrolu nad parametry swapu.



### Výměna konfigurace



Klikněte na **Start Liquidity Swap** a poté nakonfigurujte parametry nabídky:





- vyberte celkový počet účastníků (3, 4 nebo 5);
- udávají kapacitu kanálů, které mají být otevřeny;
- definovat dobu závazku, během níž se účastníci zavazují, že nezavřou své kanály;
- upřesnit veškerá omezení platná pro účastníky (minimální počet kanálů, minimální celková kapacita, typ přijímaného připojení).



![capture](assets/fr/11.webp)



### Zveřejnění a očekávání účastníků



Po zadání všech parametrů klikněte na **Start Liquidity Swap** a nabídku zveřejněte. Nyní stačí počkat, až se přihlásí další operátoři.



![capture](assets/fr/12.webp)



## Dokončení výměny



### Efektivní otevření kanálu



Po obsazení všech výměnných pozic může každý účastník na svém rozhraní LN+ zjistit, ke kterému uzlu má otevřít kanál Lightning.



![capture](assets/fr/13.webp)



Na své straně otevřete kanál pomocí ID uzlu poskytnutého společností LN+ a respektujte uvedenou částku. Tuto operaci lze provést prostřednictvím ThunderHub, jiného správce uzlu Lightning nebo přímo prostřednictvím základního rozhraní vašeho uzlu.



![capture](assets/fr/14.webp)



Po otevření se kanál zobrazí v části čekajících kanálů.



![capture](assets/fr/15.webp)



### Potvrzení v LN+



Poté se vraťte do aplikace LN+ a potvrďte zahájení otevírání kanálu kliknutím na tlačítko `Otevření kanálu zahájeno`.



![capture](assets/fr/16.webp)



### Konec výměny



Jakmile všichni účastníci otevřou kanály, ke kterým se zavázali, je výměna považována za dokončenou.



## Dobrá pověst a správné komunikační postupy



### Systém pověsti LN+



LN+ obsahuje systém reputace založený na názorech, které účastníci zanechávají na konci výměn. Tyto názory jsou veřejné a přímo ovlivňují možnost provozovatele připojit se k budoucím swapům nebo je vytvořit.



![capture](assets/fr/17.webp)



### Doporučené osvědčené postupy



V zájmu zachování dobré pověsti a zajištění hladkého průběhu výměn se doporučuje :





- dodržovat lhůty pro otevření kanálu ;
- rychle komunikovat v případě problému nebo zpoždění;
- využít sekci komentářů k výměně názorů s ostatními účastníky;
- neuzavřít kanál před koncem doby závazku.




![capture](assets/fr/18.webp)



### Proč je pověst pro LN+ klíčová



LN+ je založen na modelu dobrovolné spolupráce bez silných technických omezení. Hlavním podnětem pro zajištění spolehlivosti a důvěryhodnosti účastníků je proto pověst.



## Další služby LN+



Kromě swapů nabízí LN+ i další služby určené ke zlepšení propojení a koordinace mezi provozovateli bleskových uzlů. Kroužky** umožňují několika účastníkům vytvořit smyčku otevření kanálů, čímž se posiluje redundance směrovacích cest a hustota grafu Lightning. Swapy založené na důvěře** jsou založeny na podobných principech jako klasické swapy, ale nabízejí větší flexibilitu účastníkům, kteří již mají na platformě zavedenou pověst.



LN+ také integruje sociální funkce, jako jsou veřejné profily uzlů, výměna komentářů a systém reputace. Tyto nástroje nejsou samy o sobě technickými službami, ale hrají ústřední roli v hladkém chodu platformy a usnadňují komunikaci, koordinaci a důvěru mezi operátory.



## Závěr



Služba Swaps společnosti LN+ je účinným nástrojem pro zlepšení konektivity, likvidity a decentralizace v síti Lightning. Podporou vzájemného, koordinovaného otevírání kanálů umožňuje společnost LN+ provozovatelům uzlů posílit jejich topologii a zároveň podporuje odpovědnou, decentralizovanou spolupráci.