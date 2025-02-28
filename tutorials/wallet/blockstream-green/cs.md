---
name: Blockstream Green - Mobile
description: Vytvoření portfolia mobilního softwaru
---
![cover](assets/cover.webp)

Softwarová peněženka je aplikace nainstalovaná v počítači, chytrém telefonu nebo jiném zařízení připojeném k internetu, která umožňuje spravovat a zabezpečit klíče k bitcoinovým peněženkám. Na rozdíl od hardwarových peněženek, které izolují soukromé klíče, proto "horké" peněženky fungují v prostředí potenciálně vystaveném kybernetickým útokům, což zvyšuje riziko pirátství a krádeže.

Softwarové peněženky by měly sloužit ke správě rozumného množství bitcoinů, zejména pro každodenní transakce. Mohou být také zajímavou možností pro lidi s omezeným majetkem v bitcoinech, kterým se investice do hardwarové peněženky může zdát nepřiměřená. Jejich neustálé vystavení působení internetu je však činí méně bezpečnými pro ukládání vašich dlouhodobých úspor nebo velkých finančních prostředků. Pro ty je lepší zvolit bezpečnější řešení, například hardwarové peněženky.

V tomto návodu bych vám rád představil jedno z nejlepších řešení mobilní softwarové peněženky: **Blockstream Green**.

![GREEN](assets/fr/01.webp)

Pokud chcete zjistit, jak používat Blockstream Green na svém počítači, přečtěte si tento další návod:

https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da
## Představujeme Blockstream Green

Blockstream Green je softwarová peněženka dostupná na mobilních zařízeních a počítačích. Tato peněženka, dříve známá jako *Green Address*, se po akvizici v roce 2016 stala projektem společnosti Blockstream.

Zelená je mimořádně snadno použitelná aplikace, která je zajímavá i pro začátečníky. Nabízí všechny základní funkce dobré bitcoinové peněženky, včetně RBF (*Replace-by-Fee*), možnosti připojení přes Tor, možnosti připojení vlastního uzlu, SPV (*Simple Payment Verification*), označování mincí a kontroly.

Blockstream Green také podporuje síť Liquid, vedlejší řetězec Bitcoinu vyvinutý společností Blockstream pro rychlé a důvěrné transakce mimo hlavní blockchain. Tento tutoriál se zaměřuje výhradně na Bitcoin, ale pozdější tutoriál se bude zabývat používáním sítě Liquid.

## Instalace a konfigurace aplikace Blockstream Green

Prvním krokem je samozřejmě stažení zelené aplikace. Přejděte do svého obchodu s aplikacemi:

- [Pro Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Pro Apple](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590).
![GREEN](assets/fr/02.webp)

Uživatelé systému Android mohou aplikaci nainstalovat také prostřednictvím souboru `.apk` [dostupného na GitHubu společnosti Blockstream](https://github.com/Blockstream/green_android/releases).

![GREEN](assets/fr/03.webp)

Spusťte aplikaci a zaškrtněte políčko "Souhlasím s podmínkami...*".

![GREEN](assets/fr/04.webp)

Při prvním otevření aplikace Green se zobrazí domovská obrazovka bez nakonfigurovaného portfolia. Pokud později vytvoříte nebo importujete portfolia, zobrazí se v tomto rozhraní. Než se pustíte do vytváření portfolia, doporučuji upravit nastavení aplikace podle svých potřeb. Klepněte na tlačítko "Nastavení aplikace".

![GREEN](assets/fr/05.webp)

Možnost "*Zvýšené soukromí*", která je k dispozici pouze v systému Android, zvyšuje soukromí tím, že vypíná snímky obrazovky a skrývá náhledy aplikací. Automaticky také uzamkne přístup k aplikacím, jakmile je telefon uzamčen, čímž ztíží odhalení vašich dat.

![GREEN](assets/fr/06.webp)

Pro ty, kteří chtějí zvýšit své soukromí, nabízí aplikace možnost zakořenit svůj provoz prostřednictvím sítě Tor, která šifruje všechna vaše připojení a ztěžuje vysledování vašich aktivit. Ačkoli tato možnost může mírně zpomalit provoz aplikace, pro ochranu vašeho soukromí ji vřele doporučujeme, zejména pokud nepoužíváte vlastní kompletní uzel.

![GREEN](assets/fr/07.webp)

Uživatelům, kteří mají vlastní kompletní uzel, nabízí Zelená peněženka možnost připojit se k němu prostřednictvím serveru Electrum, což zaručuje úplnou kontrolu nad informacemi v síti Bitcoin a distribucí transakcí.

![GREEN](assets/fr/08.webp)

Další alternativní funkcí je možnost "*SPV Verification*", která umožňuje přímo ověřit určitá data blockchainu a snížit tak potřebu důvěřovat výchozímu uzlu Blockstream, ačkoli tato metoda neposkytuje všechny záruky plnohodnotného uzlu.

![GREEN](assets/fr/09.webp)

Po úpravě těchto nastavení podle svých potřeb klikněte na tlačítko "*Uložit*" a restartujte aplikaci.

![GREEN](assets/fr/10.webp)

## Vytvoření peněženky Bitcoin na Blockstream Green

Nyní jste připraveni vytvořit peněženku Bitcoin. Klikněte na tlačítko "*Začít*".

![GREEN](assets/fr/11.webp)

Můžete si vybrat mezi vytvořením místní softwarové peněženky nebo správou chladné peněženky prostřednictvím hardwarové peněženky. V tomto návodu se zaměříme na vytvoření horké peněženky, takže budete muset vybrat možnost "*Na tomto zařízení*". V některém z příštích tutoriálů vám ukážu, jak používat druhou možnost.

Možnost "*Pouze sledování*" vám umožní importovat rozšířený veřejný klíč (`xpub`) a zobrazit transakce portfolia, aniž byste mohli utratit související prostředky, což je užitečné například pro sledování portfolia v hardwarové peněžence.

![GREEN](assets/fr/12.webp)

Poté můžete obnovit stávající peněženku Bitcoin nebo vytvořit novou. Pro účely tohoto návodu budeme vytvářet novou peněženku. Pokud však potřebujete obnovit stávající peněženku Bitcoin z její mnemotechnické fráze, například po ztrátě hardwarové peněženky, budete muset zvolit druhou možnost.

![GREEN](assets/fr/13.webp)

Poté si můžete vybrat mezi mnemotechnickou frází o 12 nebo 24 slovech. Tato fráze vám v případě problému s telefonem umožní obnovit přístup k peněžence z jakéhokoli kompatibilního softwaru. V současné době nenabízí volba 24slovné fráze větší zabezpečení než 12slovná fráze. Doporučuji proto zvolit mnemotechnickou frázi o 12 slovech.

Zelená vám pak poskytne mnemotechnickou frázi. Než budete pokračovat, ujistěte se, že vás nikdo nesleduje. Kliknutím na "*Zobrazit frázi pro obnovení*" ji zobrazíte na obrazovce.

![GREEN](assets/fr/14.webp)

**Tato mnemotechnická pomůcka vám dává plný a neomezený přístup ke všem vašim bitcoinům ** Kdokoli, kdo má tuto mnemotechnickou pomůcku, může ukrást vaše peníze, a to i bez fyzického přístupu k vašemu telefonu.

Obnovuje přístup k bitcoinům v případě ztráty, krádeže nebo rozbití telefonu. Proto je velmi důležité pečlivě zálohovat **na fyzickém médiu (ne digitálním)** a uchovávat je na bezpečném místě. Můžete si ji zapsat na kus papíru, nebo pro větší bezpečnost, pokud se jedná o velkou peněženku, doporučuji vyrýt ji na nerezový nosič, který ji ochrání před rizikem požáru, povodně nebo zřícení (u horké peněženky určené k zabezpečení malého množství bitcoinů pravděpodobně postačí jednoduchá papírová záloha).

*Tato slova samozřejmě nikdy nesmíte sdílet na internetu, jako to dělám já v tomto návodu. Toto ukázkové portfolio bude použito pouze na Testnetu a po skončení výukového programu bude smazáno.*

![GREEN](assets/fr/15.webp)

Po správném nahrání mnemotechnické fráze na fyzické médium klikněte na "*Pokračovat*". Zelená peněženka vás poté požádá o potvrzení některých slov ve vaší mnemotechnické frázi, abyste se ujistili, že jste je zaznamenali správně. Vyplňte prázdná místa chybějícími slovy.

![GREEN](assets/fr/16.webp)

Zvolte PIN kód zařízení, který se použije k odemknutí zelené peněženky. To je vaše ochrana proti neoprávněnému fyzickému přístupu. Tento kód PIN se nepodílí na odvozování kryptografických klíčů vaší peněženky. Takže i bez přístupu k tomuto kódu PIN vám vlastnictví vaší 12- nebo 24slovné mnemotechnické fráze umožní znovu získat přístup k vašim bitcoinům.

Doporučujeme zvolit co nejnáhodnější šestimístný kód PIN. Nezapomeňte si tento kód uložit, abyste ho nezapomněli, jinak budete nuceni peněženku načítat z mnemotechniky. Poté můžete přidat možnost biometrického blokování, abyste nemuseli zadávat kód PIN při každém použití. Obecně platí, že biometrické údaje jsou mnohem méně bezpečné než samotný kód PIN. Ve výchozím nastavení tedy doporučuji tuto možnost odemykání nenastavovat.

![GREEN](assets/fr/17.webp)

Zadejte PIN podruhé a potvrďte jej.

![GREEN](assets/fr/18.webp)

Počkejte, až se vytvoří vaše portfolio, a klikněte na tlačítko "*Vytvořit účet*".

![GREEN](assets/fr/19.webp)

Poté si můžete vybrat mezi standardní peněženkou s jedním podpisem, kterou budeme používat v tomto návodu, nebo peněženkou chráněnou dvoufaktorovým ověřováním (2FA).

![GREEN](assets/fr/20.webp)

Možnost 2FA na zelené kartě vytváří peněženku s více podpisy 2/2, přičemž jeden klíč je v držení společnosti Blockstream. To znamená, že k provedení transakce jsou zapotřebí oba klíče: místní klíč chráněný kódem PIN v telefonu a vzdálený klíč zabezpečený pomocí 2FA na serverech společnosti Blockstream. V případě ztráty přístupu k 2FA nebo nedostupnosti služeb společnosti Blockstream zajišťují mechanismy obnovy založené na skriptech časového zámku, že vaše finanční prostředky mohou být obnoveny samostatně. Přestože tato konfigurace výrazně snižuje riziko krádeže vašich bitcoinů, je složitější na správu a částečně závislá na společnosti Blockstream. Pro tento návod se rozhodneme pro klasickou peněženku s jedním podpisem a klíči uloženými lokálně v telefonu.

Vaše peněženka Bitcoin byla nyní vytvořena pomocí aplikace Green!

![GREEN](assets/fr/21.webp)

Než obdržíte své první bitcoiny do peněženky, **důrazně doporučuji provést test obnovy prázdné peněženky**. Zaznamenejte si některé referenční údaje, jako je vaše xpub nebo první přijímací adresa, a poté peněženku v aplikaci Green vymažte, dokud je ještě prázdná. Poté zkuste peněženku obnovit v aplikaci Zelená pomocí papírových záloh. Zkontrolujte, zda informace o souboru cookie vygenerované po obnovení odpovídají těm, které jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé. Další informace o tom, jak provést zkušební obnovu, najdete v tomto dalším návodu:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Nastavení portfolia na Blockstream Green

Pokud si chcete portfolio přizpůsobit, klikněte na tři malé tečky v pravém horním rohu.

![GREEN](assets/fr/22.webp)

Možnost "*Přejmenovat*" umožňuje přizpůsobit název portfolia, což je užitečné zejména v případě, že v jedné aplikaci spravujete několik portfolií.

![GREEN](assets/fr/23.webp)

Nabídka "*Unit*" umožňuje změnit základní jednotku peněženky. Můžete například zvolit, že se má zobrazovat v satoších, a ne v bitcoinech.

![GREEN](assets/fr/24.webp)

Nabídka "*Nastavení*" poskytuje přístup k různým možnostem vaší peněženky Bitcoin.

![GREEN](assets/fr/25.webp)

Zde například najdete svůj rozšířený veřejný klíč a jeho *deskriptor*, což je užitečné, pokud plánujete z této peněženky nastavit peněženku v režimu pouze pro sledování.

![GREEN](assets/fr/26.webp)

Můžete také změnit PIN peněženky a aktivovat biometrické připojení.

![GREEN](assets/fr/27.webp)

## Používání služby Blockstream Green

Nyní, když je vaše peněženka Bitcoin nastavena, jste připraveni přijímat první saty! Jednoduše klikněte na tlačítko "*Přijmout*".

![GREEN](assets/fr/28.webp)

Zelená barva pak zobrazí první prázdnou přijímací adresu v peněžence. Můžete buď naskenovat související QR kód, nebo adresu přímo zkopírovat a odeslat bitcoiny. Tento typ adresy neurčuje částku, kterou má plátce poslat. Můžete však vygenerovat adresu, která požaduje konkrétní částku, a to tak, že kliknete na tři malé tečky v pravém horním rohu, poté na "*Požadovaná částka*" a zadáte požadovanou částku.

Protože používáte účet Segwit v0 (BIP84), vaše adresa bude začínat `bc1q...`. V mém příkladu používám portfolio Testnet, takže předpona je trochu jiná.

![GREEN](assets/fr/29.webp)

Jakmile je transakce odvysílána v síti, objeví se ve vaší peněžence.

![GREEN](assets/fr/30.webp)

Počkejte, až obdržíte dostatek potvrzení, abyste mohli transakci považovat za definitivní.

![GREEN](assets/fr/31.webp)

S bitcoiny v peněžence můžete nyní bitcoiny také posílat. Klikněte na "*Odeslat*".

![GREEN](assets/fr/32.webp)

Na další stránce zadejte adresu příjemce. Můžete ji zadat ručně nebo naskenovat QR kód.

![GREEN](assets/fr/33.webp)

Zvolte výši platby.

![GREEN](assets/fr/34.webp)

V dolní části obrazovky můžete vybrat sazbu poplatku pro tuto transakci. Máte na výběr, zda se budete řídit doporučeními aplikace, nebo si poplatky přizpůsobíte. Čím vyšší je poplatek v porovnání s ostatními nevyřízenými transakcemi, tím rychleji bude vaše transakce zpracována. Informace o trhu s poplatky naleznete na stránce [Mempool.space](https://mempool.space/) v sekci "*Poplatky za transakce*".

![GREEN](assets/fr/35.webp)

Kliknutím na tlačítko "*Další*" přejděte na obrazovku se souhrnem transakcí. Zkontrolujte, zda jsou adresa, částka a poplatky správné.

![GREEN](assets/fr/36.webp)

Pokud vše proběhne v pořádku, posunutím zeleného tlačítka v dolní části obrazovky doprava transakci podepíšete a odešlete do sítě Bitcoin.

![GREEN](assets/fr/37.webp)

Vaše transakce se nyní objeví na panelu peněženky Bitcoin a čeká na potvrzení.

![GREEN](assets/fr/38.webp)

*Tento návod vychází z [původní verze patřící Bitstacku](https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet), kterou napsal Loïc Morel. Bitstack je francouzská bitcoinová nebanka, která nabízí možnost spořit v bitcoinech, a to buď v DCA (Dollar Cost Averaging), nebo prostřednictvím automatického systému zaokrouhlování denních výdajů.* Bitstack je francouzská bitcoinová nebanka, která nabízí možnost spořit v bitcoinech, a to buď v DCA (Dollar Cost Averaging), nebo prostřednictvím automatického systému zaokrouhlování denních výdajů