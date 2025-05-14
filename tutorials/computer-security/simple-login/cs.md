---
name: Jednoduché přihlášení
description: Identita chráněná přezdívkami
---
![cover](assets/cover.webp)

## Přihlášení = e-mail = ztráta soukromí


V digitálním světě se stalo běžnou praxí mít účet na každé platformě, ke které chcete přistupovat.

Každá z těchto služeb vyžaduje přihlášení, obvykle spojené s dvojicí _uživatelské jméno_ a _heslo_. Uživatelské jméno je často osobní e-mail uživatele.


Při používání osobního e-mailu Address pro každé přihlášení si lze snadno představit první důsledek: ztrátu důvěrnosti, která se stává závažnou, pokud je Address složen z _name.surname@serviceemail.com_.


Vývojáři nástrojů s otevřeným zdrojovým kódem vytvořili řadu sad aplikací, které vznikly právě proto, aby uživatelé získali zpět trochu soukromí: stále se budou přihlašovat, ale místo nástroje, který odhaluje jejich soukromou identitu, budou používat přezdívku.


Nejjednodušší z těch, které jsem osobně vyzkoušel a stále je testuji, je [Simple Login](https://simplelogin.io/).


## Alias


E-mailový alias jednoduše nahradí část _jméno.příjmení_ vašeho e-mailu Address smyšleným jménem. Pro uživatele se nic nemění; služba aliasu přeposílá e-maily z a na obvyklé jméno Address jako obvykle. Každý může nadále používat svou schránku jako vždy, ale místo skutečného jména se zobrazí neznámý uživatel. Tato služba musí být efektivní a služba Simple Login se zatím osvědčila.


Při první návštěvě webu Simple Login si musíte vytvořit účet (také zde!) a použít "oficiální" e-mail Address. Zde musíte zadat e-mail, heslo a vyřešit captcha.


![image](assets/it/02.webp)


Jednoduché přihlášení odešle ověřovací zprávu na uvedený e-mail Address. Místo kliknutí na ověřovací tlačítko doporučujeme odkaz zkopírovat a vložit do lišty Address.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Okamžitě se otevře ovládací panel jednoduchého přihlášení se stručným návodem k navigaci.


![image](assets/it/05.webp)


Je třeba poznamenat, že jednoduché přihlášení automaticky aktivuje odběr newsletteru, který lze deaktivovat příslušným příkazem.


![image](assets/it/06.webp)


## Nastavení


Můžete se hned podívat do _Nastavení_ a zjistit funkce služby. Jednoduché přihlášení začíná s aktivními všemi možnostmi, včetně těch _Premium_, které zůstávají použitelné po dobu 10 dnů. Po skončení zkušební doby budete mít možnost vytvořit si s tímto profilem 10 aliasů a můžete přímo propojit svůj e-mail Proton, protože Simple Login získal švýcarský poskytovatel e-mailu.


![image](assets/it/07.webp)


Můžete si nastavit řadu parametrů nebo zkontrolovat, zda váš e-mail již nebyl ohrožen z hlediska ochrany osobních údajů.


![image](assets/it/08.webp)


Nakonec můžete zálohu svého profilu exportovat nebo importovat z jiného poskytovatele.


![image](assets/it/09.webp)


### Pracovní e-mail


Ti, kteří používají e-mail s osobní doménou jako pracovní e-mail, si mohou nastavit svou soukromou doménu.


![image](assets/it/10.webp)


Na hlavním panelu je možné výběrem možnosti _Mailboxes_ přidat další e-mailové adresy a používat také odpovídajícím způsobem vytvořené aliasy. V tomto návodu jsem se například rozhodl vytvořit profil s poštovní schránkou _gmail.com_ a následně k ní přiřadit _proton.me_ Address. V tomto případě jsem se rozhodl vytvořit profil s poštovní schránkou _gmail.com_.


![image](assets/it/11.webp)


Při přidávání nového Address, zejména pokud patří k poskytovateli Proton, se v naváděcím postupu zobrazí možnost vstupu do režimu _sudo_, superuživatele. Jednoduché přihlášení vyzve k zadání hesla této schránky, k prokázání legitimity Ownership.


⚠️ **Osobně vám to nedoporučuji**. ⚠️


![image](assets/it/12.webp)


**Je lepší vstoupit do e-mailové schránky -> zkopírovat odkaz pro ověření a vložit jej do řádku URL -> a získat ověření bez prozrazení hesla.**


![image](assets/it/13.webp)


Ze dvou zadaných adres se jedna stává výchozí a druhá je sekundární, ale lze je snadno přepínat a nastavení je snadno identifikovatelné na ovládacím panelu.


![image](assets/it/14.webp)


Po přidání druhého e-mailu Address (nepovinné) se podíváme, co můžeme udělat s jednoduchým přihlášením.


## Vytváření aliasů


Na panelu je první možnost nabídky označena _Alias_, kde je můžete vytvořit. Máte možnost náhodně zvolit aliasy generate kliknutím na tlačítko Random Alias, což je tlačítko Green zobrazené na další fotografii. Tato funkce vytvoří jedinečný a zajímavý e-mail Address.


![image](assets/it/24.webp)


Pokud však chcete služby odlišit tím, že jim dáte různé názvy, musíte zvolit možnost _Nový vlastní alias_. Tímto způsobem můžete aliasu dát název služby, ke které chcete mít přístup (sociální média, poskytovatelé služeb, online události, náhodně potkaní cizinci atd.). O zbytek se postará funkce Jednoduché přihlášení.

Pro zábavu (ale popravdě řečeno ne úplně) jsem se rozhodl vytvořit alias pro banku a nazval jsem ho `BANK`. I když je pravda, že moje banka o mně ví všechno, přijde mi zábavné komunikovat s ní pomocí e-mailu Address, který je pro ně nesrozumitelný. Jednoduché přihlášení skutečně generuje náhodné jméno, které je od toho, které jsme si zvolili, odděleno znakem `.`


Zde se může stát novým e-mailem Address:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- a tak dále


Můžete si vybrat více než jednu doménu: veřejné domény jsou k dispozici v rámci bezplatného plánu, zatímco další, označené jako soukromé (včetně _@simplelogin.com_), rozšiřují výběr pro uživatele, kteří se rozhodnou předplatit si placený plán.


![image](assets/it/15.webp)


Po výběru náhodné přípony a domény můžete nastavit, zda má tato nová (a podivná) doména Address sloužit jako alias pouze pro jednu z osobních e-mailových schránek, nebo pro všechny. Alias se stane připraveným a aktivním po kliknutí na tlačítko _Create_ (Vytvořit)


![image](assets/it/16.webp)


Byl vytvořen nový e-mail Address, který je nyní viditelný a připravený k odeslání (do banky!) pouhým zkopírováním.


![image](assets/it/18.webp)


V tuto chvíli se můžete zaměřit na vytvoření aliasu pro každou službu nebo platformu, ke které chcete mít přístup a kde je e-mail vyžadován jako základní parametr pro vytvoření účtu.


![image](assets/it/19.webp)


Pro milovníky ochrany soukromí je zde také možnost generate e-mail Address založený na protokolu UUID (nikoli na identifikovatelných jménech), který vytváří jedinečný 128bitový identifikátor, který není kontrolován centralizovanými stranami. Tuto funkci, která je užitečná pro citlivé účty, najdete v nabídce _Random Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Jak vidíte, jedná se o e-mail Address, který vyžaduje správnou správu.


Pokud si to rozmyslíte a nechcete již alias používat, stačí kliknout na příkaz _Další_ u každého jednotlivého aliasu a zvolit možnost _Smazat_.


![image](assets/it/23.webp)


## Správa přezdívek


Vytváření aliasů je jednoduché, stejně jako jejich správa, která vyžaduje jen trochu péče a disciplíny. Veškerý provoz bude ve skutečnosti stále probíhat přes e-mailovou schránku, kterou jsme na začátku definovali jako oficiální. Oznámení a důležitá sdělení z platforem budou i nadále přicházet na Gmail, Proton nebo jakéhokoli poskytovatele e-mailu.


Výsledkem však je, že jsme zachovali hlavní Address, který od okamžiku vytvoření aliasu můžeme svobodně rozhodnout, komu ho prozradíme a komu ne.


Pseudonym funguje jak pro příjem, tak pro odesílání: jiný uživatel skutečně obdrží odpověď z adresy alias.preoccupy789@8shield.net, pokud je to pseudonym zvolený pro daného příjemce.


## Klady


Používání přezdívek je celkově účinný způsob ochrany identity a soukromí. E-mailové adresy jsou často shromažďovány zprostředkovateli dat a webovými stránkami za účelem sledování zvyků a chování uživatelů. Ačkoli vás alias neudělá zcela nevystopovatelnými, jeho důsledné používání je pozitivním krokem k ochraně vašich informací. V naší "globální digitální vesnici", kde jsou hackerské útoky, prodej dat a narušení bezpečnosti až příliš časté, je navíc velmi pravděpodobné, že e-mail, který používáte k registraci na různých webových stránkách, již byl napaden nebo se stal terčem útoku.


Jedinečný pseudonym, který se používá při každém přihlášení, nám **umožňuje okamžitě zjistit, která platforma odesílá spam (nebo něco horšího) do naší schránky, protože e-mail je identifikován podle přezdívky, která je s ním spojena**. Netušíte, kolik spamu a phishingu přichází z tzv. spolehlivých kanálů, protože jsou institucionální, dokud nezačnete používat alias pro banky, jeden pro poštovní služby nebo specifický pro některé povinné vládní služby. Jakmile identifikujete odesílatele spamu (nebo ještě hůře), dozvíte se, že daná stránka byla napadena, a přijmete veškerá opatření k ochraně všech údajů poskytnutých (myslete na kreditní karty!) této konkrétní webové stránce, která si narušení může uvědomit až o několik týdnů později.


Pokud jde o jednoduché přihlášení, tento nástroj má následující funkce:



- mobilní aplikace (také od F-Droid) a rozšíření prohlížeče, které umožňuje spravovat aliasy v jakékoli situaci;
- dvoufaktorové ověřování pro každý nový pseudonym, což zvyšuje míru nezávislosti na samotné službě;
- Podpora PGP (pro uživatele s příplatkem _Premium);
- jednoduché vytváření všech typů aliasů (vlastní, náhodné a UUID);
- mezi bezplatnými plány v tomto odvětví možnost používat aliasy s více "oficiálními" e-mailovými schránkami. Ostatní konkurenti se omezují pouze na jednu.


## Nevýhody


- 10 aliasů nemusí stačit, pokud plánujete používat Simple Login ve velké míře. V takovém případě se hodí placený tarif, který je cenově poměrně dostupný a který zvýší počet možných dostupných aliasů.
- Není možné vytvořit alias s konkrétním názvem a doménou. Náhodná přípona přidaná za námi vybrané jméno generuje Address, který lze označit přinejlepším za bizarní. Tradiční sociální sítě obvykle odmítají poskytovat účty vytvořené s tímto typem e-mailových adres. Nostr to napravuje!
- Pokud někomu pošlete zprávu pomocí přezdívky, snadno skončí ve složce spamu příjemce. Jako první krok je vhodné použít pseudonym pro příjem, stejně jako v případě vytvoření účtu, přihlášení se do poštovní konference apod.