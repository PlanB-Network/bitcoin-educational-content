---
name: Lipa
description: Nastavení a používání mobilní peněženky Lipa lightning
---
![cover](assets/cover.webp)

Peněženka Bitcoin Lightning je mobilní aplikace, která umožňuje okamžité a levné transakce v síti Bitcoin Lightning. Na rozdíl od transakcí v hlavním blockchainu (on-chain) jsou platby Lightning téměř okamžité a vyžadují minimální poplatky, takže jsou vhodné zejména pro drobné každodenní platby.

Peněženky Lightning, stejně jako všechny mobilní peněženky, jsou považovány za "horké" peněženky, protože jsou připojeny k internetu. Jsou tedy primárně určeny ke správě malých částek peněz pro každodenní výdaje. Pro větší částky je vhodnější používat bezpečnější řešení ukládání, jako jsou hardwarové peněženky.

Pokud se chcete dozvědět více o síti Lightning a pochopit, jak technicky funguje, doporučuji vám absolvovat tento kurz:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
V tomto návodu se podíváme na **Lipa**, jednoduchou a efektivní peněženku Lightning vyvinutou ve Švýcarsku.

## Představujeme společnost Lipa

Lipa je blesková peněženka, která se vyznačuje jednoduchým používáním a nenáročným rozhraním. Vyvinul ji švýcarský tým a klade důraz na důvěrnost a snadné používání pro začátečníky.

Mezi hlavní funkce patří:


- Intuitivní uživatelské rozhraní
- Autonomní správa kanálu Lightning
- Podpora protokolu LNURL
- Možnost nákupu bitcoinů přímo v aplikaci

## Instalace a konfigurace systému Lipa

Prvním krokem je stažení aplikace Lipa. Zatím je k dispozici pouze pro iOS :


- [Pro Apple](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

Verze pro Android je v současné době ve vývoji a bude brzy k dispozici.

![Installation de Lipa](assets/fr/01.webp)

Po spuštění aplikace se dostanete na domovskou obrazovku, která nabízí dvě možnosti:


- Vytvoření nového portfolia
- Obnovení stávajícího portfolia ze zálohy

Po výběru možnosti vás aplikace vyzve k povolení oznámení. Tento krok je důležitý, protože oznámení jsou nezbytná pro :


- Přijímání upozornění na přijaté platby, i když je aplikace zavřená
- Buďte informováni o krocích spojených s nákupem bitcoinů prostřednictvím jejich integrovaného řešení

Aplikace pak představuje své hlavní funkce prostřednictvím řady úvodních obrazovek:


- Bezproblémové přijímání plateb**: Uživatelé mohou přijímat platby v bitcoinech, i když je aplikace zavřená, což zaručuje spolehlivost a pohodlí.
- Bleskové adresy, na které se nevztahuje opatrovnictví**: Lipa nyní podporuje neúřední adresy Lightning, čímž zvyšuje soukromí a bezpečnost a dává uživatelům plnou kontrolu nad jejich bitcoiny.
- Kontrola analytických dat** : Vzhledem k tomu, že transparentnost a důvěrnost jsou prvořadé, mohou si uživatelé prohlédnout typy shromážděných dat a zvolit své preference sdílení.
- Odeslat prostřednictvím telefonního čísla**: Jednoduše vyberte kontakt, zadejte částku a pošlete bitcoiny přímo na jeho telefonní číslo.

Aplikace také těží z neustálého zlepšování stability, bezpečnosti a spolehlivosti, aby byla zaručena optimální uživatelská zkušenost.

## Navigace v aplikaci

Rozhraní aplikace Lipa je uspořádáno do 4 hlavních karet, které jsou přístupné přes navigační panel ve spodní části obrazovky:

![Navigation principale](assets/fr/02.webp)


- Domov**: Zobrazuje aktuální zůstatek a historii transakcí
- Skener**: Umožňuje skenovat QR kódy a provádět platby
- Mapa**: Zobrazí interaktivní mapu podniků, které přijímají bitcoiny ve vašem okolí
- Nastavení**: Přístup k nastavení aplikace, zálohování a předvolbám

Další nabídku lze otevřít stažením domovské obrazovky dolů:

![Menu supplémentaire](assets/fr/03.webp)

Toto gesto odhalí další funkce, jako je :


- Nákup bitcoinů
- On-chain Bitcoin vklad
- Vytváření faktur Lightning pro příjem bitcoinů
- Blesková platba faktury

## Uložení portfolia

Chcete-li zálohovat peněženku, přejděte na kartu "Nastavení" a vyberte možnost "Fráze pro obnovení". Lipa používá frázi pro obnovení, kterou je nutné pečlivě zapsat na fyzické médium (papír, kov). Tato fráze je jediným způsobem, jak obnovit své finanční prostředky v případě ztráty nebo krádeže telefonu. Pro ověření zálohy vás aplikace požádá o potvrzení 3 náhodných slov z vaší fráze.

![Backup](assets/fr/04.webp)

Další informace o tom, jak správně zálohovat a spravovat fázi obnovení, doporučuji sledovat v tomto dalším návodu, zejména pokud jste začátečníci:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Přijímání bitcoinů

Chcete-li získat bitcoiny, máte dvě možnosti. Chcete-li se k těmto možnostem dostat, vraťte se na domovskou obrazovku a stáhněte obrazovku dolů. Poté můžete buď :


- Chcete-li přijímat bitcoiny v řetězci, vyberte možnost "Transfer BTC". Pak jednoduše naskenujte QR kód pomocí své druhé peněženky a dokončete transakci.
- Pro příjem prostřednictvím sítě Lightning vyberte možnost "Request" a zadejte částku, kterou chcete obdržet.

V obou případech budete muset zaplatit poplatek ve výši 0,4 % z částky nebo přibližně 2 500 sátů, pokud je třeba v aplikaci otevřít nový platební kanál (což bude nevyhnutelně případ první platby).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Odeslat bitcoiny

Chcete-li poslat bitcoiny, přejděte na domovskou obrazovku, stáhněte obrazovku dolů a vyberte možnost "Zaplatit". Poté jednoduše buď :


- zadejte bleskovou adresu LNURL
- naskenovat bleskový QR kód a provést platbu.

Můžete také přejít na druhou kartu ve spodní části obrazovky a naskenovat QR kód přímo.

![Envoi de bitcoins](assets/fr/07.webp)

## Koupit bitcoiny

Lipa nabízí možnost nákupu bitcoinů přímo v aplikaci za poplatek 1,5 %. Chcete-li provést nákup, přejděte na domovskou obrazovku a tahem dolů zobrazte nabídku. Poté vyberte možnost "Koupit BTC". Procesem nákupu vás provedou tři úvodní obrazovky.

![Menu d'achat](assets/fr/08.webp)

Poté jednoduše zadejte bankovní údaje účtu, který budete používat k nákupu. Zvolte měnu a zadejte svou e-mailovou adresu.

Po načítací obrazovce najdete referenční číslo, které je třeba zahrnout do převodu, který se chystáte provést, a bankovní údaje pro výměnu.

![Sélection du montant](assets/fr/09.webp)

K převodu požadované částky stačí použít vaši banku, nastavit převod uvedením dříve načteného RIB a při transakci uvést referenci, aby Lipa mohla tento bankovní pohyb přiřadit k vaší peněžence Lipa.

![Confirmation d'achat](assets/fr/10.webp)

## Výhody a nevýhody

### Výhody


- Intuitivní rozhraní
- Správné poplatky za služby
- Bez opatrovnictví
- Integrované řešení nákupu bitcoinů
- Integrace BTCmap
- Podpora NFC

### Nevýhody


- Není možné posílat bitcoiny na řetězci
- Mírně delší než průměrná platba

Lipa je vynikající volbou pro začátky s Lightning Network, zejména pro uživatele, kteří hledají jednoduché řešení pro každodenní platby. Díky snadnému používání a nenáročnému rozhraní je ideální peněženkou pro začátečníky a zároveň nabízí základní funkce pro každodenní používání Lightning.

## Zdroje


- [oficiální webové stránky Lipa](https://lipa.swiss/)
- [Podpora Lipa](https://getlipa.atlassian.net/servicedesk/customer/portal/1)