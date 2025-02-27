---
name: Nakamochi
description: Snadné spuštění uzlu - Jak nastavit a používat uzel Nakamochi Bitcoin a Lightning.
---
Provozování vlastního uzlu Bitcoin a Lightning už nemusí být složitý úkol omezený na technické experty. Zřizování a správa uzlů tradičně vyžadovaly hluboké znalosti kryptografie, sítí a vývoje softwaru. Nakamochi to mění tím, že uzly zpřístupňuje všem bez ohledu na technické zázemí.

Díky službě Nakamochi si může každý zřídit a provozovat uzel z domova, což mu umožní plné soukromí a finanční nezávislost. Provozování plnohodnotného uzlu nejen zabezpečuje vlastní transakce, ale také přispívá k síle sítě Bitcoin. Decentralizovaná a odolná síť Bitcoin spoléhá na široké rozložení uzlů, které zajišťuje její bezpečnost a nezávislost.

### Obsah


- Co je Nakamochi a jak funguje?
- Nastavení Nakamochi
- O síti Lightning Network
- Otevírání kanálů a provádění transakcí v síti Lightning Network

## Co je Nakamochi a jak funguje?

Nakamochi je plnohodnotný uzel určený pouze pro Bitcoin, který podporuje sítě Bitcoin i Lightning. Obsahuje integrovanou peněženku Bitcoin a Lightning, což uživatelům umožňuje provozovat bezpečný, samostatný uzel Bitcoin a zároveň využívat rychlost a nízké transakční náklady sítě Lightning.

Váš uzel Nakamochi je spravován prostřednictvím mobilní aplikace [BitBanana (Android)](https://bitbanana.app) a [Zeus (iOS)](https://bitbanana.app), která vám umožní pohodlně jej ovládat odkudkoli. Tyto aplikace fungují jako dálkové ovládání vašeho uzlu a umožňují vám snadno platit přímo Bitcoinem nebo Lightningem, spravovat transakce, otevírat nebo zavírat kanály, kontrolovat zůstatky a sledovat výkon vašeho uzlu.

## Nastavení aplikace Nakamochi trvá pouhých 5 minut

### Krok 1: Zapojte se a začněte

1. Připojte zařízení Nakamochi k napájení a Wi-Fi.

2. Klikněte na **"Nastavit novou peněženku "** a bezpečně uložte svou 24slovnou frázi pro obnovení.

3. K připojení k zařízení Nakamochi použijte aplikaci pro správu uzlů (Zeus nebo BitBanana):

4. Otevřete aplikaci a naskenujte QR kód zobrazený na zařízení Nakamochi.

5. Pro zvýšení bezpečnosti nastavte v zařízení kód PIN.

![image](assets/en/01.webp)

_Connect to power and write down your 24-word seed phrase_ (Připojte se k napájení a zapište si svou 24slovnou frázi)

![image](assets/en/02.webp)

_Počkejte, až Blockchain dožene_

![image](assets/en/03.webp)

_Nastavení nové peněženky na kartě Lightning_

![image](assets/en/04.webp)

_Skenování QR kódu pomocí aplikace pro správu uzlů_

![image](asset/en/05.webp)

_Pro větší bezpečnost nastavte kód PIN_

**Poznámka:** _Povolte uzlu Nakamochi synchronizaci s blockchainem. Tento proces může trvat nějakou dobu v závislosti na vašem internetovém připojení._

## O síti Lightning Network

Blesková síť bitcoinů přináší revoluci v transakcích bitcoinů, protože je zrychluje, zlevňuje a zefektivňuje. Je ideální pro každodenní použití, protože umožňuje téměř okamžité platby s minimálními poplatky, což je ideální pro mikrotransakce, jako je nákup kávy nebo vyřizování častých drobných nákupů.

Díky tomu, že Lightning funguje mimo řetězec, je navržen tak, aby umožňoval škálování a podporoval tisíce transakcí za sekundu, aniž by přetěžoval hlavní blockchain Bitcoinu. To z něj činí klíčového hráče při vývoji Bitcoinu v praktický globální platební systém.

Další výhodou je ochrana soukromí, protože transakce na platformě Lightning probíhají prostřednictvím soukromých platebních kanálů a nezaznamenávají se přímo v blockchainu. To zajišťuje diskrétnější způsob transakcí při zachování robustního zabezpečení Bitcoinu.

#### Vysvětlení platebních kanálů

Síť Lightning Network funguje prostřednictvím platebních kanálů, což jsou spojení mezi dvěma stranami umožňující více transakcí bez přímé interakce s blockchainem. Když je kanál otevřen, zůstatek mezi oběma stranami se při každé transakci aktualizuje v tomto řešení Lightning druhé vrstvy, což zajišťuje rychlé a levné platby. V řetězci se zaznamenává pouze otevření a uzavření kanálu, což snižuje přetížení blockchainu Bitcoinu. tato konstrukce zajišťuje škálovatelnost a soukromí, protože jednotlivé transakce zůstávají ve veřejné účetní knize nezaznamenány.

**Příklad:** Alice a Bob otevřou kanál tím, že do něj vloží Bitcoin. Alice pošle Bitcoiny Bobovi a jejich zůstatky mimo řetězec se okamžitě aktualizují bez záznamu v řetězci. Pokud pak Alice zaplatí Charliemu a Alice nemá přímý kanál k Charliemu, může být platba směrována přes Bobův kanál, aby se dostala k Charliemu. Směrování přes zprostředkující uzly zajišťuje platby i bez přímého spojení, což činí síť vysoce efektivní.

## Otevírání kanálů a provádění transakcí v síti Lightning Network

Jakmile je vaše zařízení Nakamochi nastaveno a připojeno k aplikaci pro správu uzlů, můžete začít používat síť Lightning Network otevíráním kanálů a prováděním transakcí.

### Otevření kanálů v systému Zeus (iOS):

1. Přejděte na kartu **"Kanály "** (spodní nabídka).

2. Kliknutím na **"+"** otevřete nový kanál.

3. Naskenujte nebo zadejte pubkey uzlu, ke kterému se chcete připojit.

4. Zadejte uzamčenou částku (vyberte si ji společně s partnerem nebo použijte minimální pevnou částku pro známé uzly).

5. Klikněte na **"Otevřít kanál "**.

![image](asset/en/06.webp)

_ZEUS Screenshot_

Další informace: [Kanály | Dokumentace Zeus](https://docs.zeusln.app/)

### Otevření kanálů na BitBanana (Android):

1. Otevřete nabídku hamburgeru (vlevo).

2. Přejděte na **"Kanály "**.

3. Kliknutím na **"+"** přidáte/otevřete nový kanál.

4. Naskenujte nebo vložte pubkey.

5. Zadejte uzamčenou částku (vyberte si ji společně s partnerem nebo použijte minimální pevnou částku pro známé uzly).

![image](asset/en/07.webp)

_Bitbanana Snímek obrazovky_

Další informace: [BitBanana](https://bitbanana.com)

Jakmile je váš kanál otevřen, lze přes něj směrovat platby ostatním účastníkům sítě. Zůstatky se upravují mimo řetězec, což zajišťuje, že transakce probíhají téměř okamžitě a jsou zatíženy minimálními poplatky.

Pokud již kanál nepotřebujete, můžete jej zavřít. Tato akce vypořádá konečný zůstatek mezi vámi a vaším partnerem a zaznamená jej v řetězci. V ideálním případě obě strany souhlasí a jsou online, aby došlo ke "kooperativnímu uzavření" (rychlejší a méně poplatků oproti "vynucenému uzavření" s nereagujícím/nepřipojeným peerem).

Obecně doporučujeme ponechat kanály otevřené, aby se snížily náklady a zvýšila spolehlivost a efektivita sítě. Ponecháním otevřených kanálů minimalizujete poplatky za transakce v řetězci, vyhnete se výpadkům při opětovném připojování kanálů a udržíte stabilní směrovací kapacitu pro bezproblémové zpracování plateb. Tento přístup podporuje robustní a odolnou síť a zároveň zvyšuje celkový uživatelský komfort a snižuje provozní režii.

### Užitečné odkazy


- [O Nakamochi](https://nakamochi.io/)
- [Přihlásit se k odběru novinek Nakamochi](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)