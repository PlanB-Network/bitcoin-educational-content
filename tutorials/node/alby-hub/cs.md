---
name: Alby Hub
description: Jak snadno spustíte vlastní uzel Lightning?
---
![cover](assets/cover.webp)

Alby Hub je nejnovější software od společnosti Alby, která stojí za populárním webovým rozšířením Lightning. Alby Hub je snadno použitelné rozhraní pro správu uzlů Lightning.

V tomto tutoriálu se podíváme na různé způsoby, jak používat Alby Hub ke správě vlastního uzlu Lightning a jak jej propojit s mobilní aplikací Alby Go. To vám umožní trávit saty na cestách a zároveň být při správě svého uzlu autonomní.

![ALBY HUB](assets/fr/01.webp)

## Co je Alby Hub?

V roce 2024 společnost Alby zaznamenala strategický posun. Po léta nabízela řadu nástrojů spojených s Bitcoinem a Lightning Network, včetně ikonického rozšíření Alby, které umožňuje provozovat Lightning peněženku, ať už depozitní nebo jinou. V roce 2025 však plánují ukončit službu sdílené úschovné peněženky a zaměřit se výhradně na řešení pro vlastní úschovu. Novým stěžejním nástrojem v ekosystému Alby má být Alby Hub. Tento software umožňuje uživatelům snadno spravovat vlastní uzel Lightning a zároveň si ponechat vlastnictví svých klíčů (self-custody).

Alby Hub je vysoce přizpůsobivý nástroj. Dokáže uspokojit potřeby začátečníků i pokročilých uživatelů. Začátečníci jej využijí ke snadnému samostatnému ovládání skutečného uzlu Lightning, aniž by se museli zabývat základní složitostí. Zkušenější uživatelé mohou Alby Hub využít jako kompletní rozhraní pro pokročilou správu stávajícího uzlu Lightning.

V závislosti na vašich potřebách je Alby Hub k dispozici ve 4 konfiguracích:


- Alby Hub Cloud :**

Tato první možnost je ideální pro začátečníky, je to možnost Alby cloud. Umožňuje nasadit uzel Lightning přímo na server spravovaný společností Alby, který je přístupný přes rozhraní Alby Hub. Přestože server spravuje společnost Alby, zachováváte si nad svými prostředky svrchovanost, protože vaše klíče jsou šifrovány pomocí hesla, které znáte pouze vy. Vaše klíče však musí zůstat dešifrované v paměti RAM, aby uzel mohl fungovat, což je teoreticky vystavuje riziku, pokud někdo fyzicky získá přístup k serveru. Pro začátečníky je to zajímavý kompromis, ale je důležité si uvědomit rizika.

Hlavní výhodou této možnosti je, že máte uzel Lightning v provozu 24 hodin denně, 7 dní v týdnu, aniž byste museli sami spravovat hosting. Zálohování uzlu Lightning je navíc zjednodušené a automatizované ve srovnání s možnostmi s vlastním hostingem, kde musíte zálohování kanálů spravovat sami.

Společnost Alby nabízí tuto službu za 21 000 satelitů měsíčně (sazba za prosinec 2024, může se změnit, [zkontrolujte jejich ceny](https://albyhub.com/#pricing)). Poplatek je automaticky odečítán z vašeho uzlu prostřednictvím faktury Lightning vystavené společností Alby. To se provádí prostřednictvím připojení NWC, které konfiguruje váš uzel tak, aby automaticky platil faktury společnosti Alby související s vaším předplatným.


- Alby Hub s existujícím uzlem :**

Pokud již máte uzel umístěný například na platformě Umbrel nebo Start9, lze Alby Hub použít jako rozhraní pro pokročilou správu stejně jako ThunderHub nebo RTL.


- Místní centrum Alby Hub :**

Rozbočovač Alby Hub a uzel je možné nainstalovat také přímo do počítače, ačkoli tato možnost je méně praktická, protože počítač musí zůstat neustále aktivní, aby bylo možné k uzlu Lightning přistupovat na dálku. Tato alternativa však může být vhodná pro vaše specifické potřeby.


- Alby Hub na osobním serveru :**

Pokročilí uživatelé mohou Alby Hub nasadit na osobní server pomocí jednoduchého příkazu. Touto možností se tento návod nezabývá, ale můžete najít specializovaný návod [na GitHubu Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Tento návod se zaměřuje především na rozhraní, které bude stejné bez ohledu na zvolenou možnost. Podíváme se také na to, jak nasadit Alby Hub s placenou cloudovou variantou a poté s variantou node-in-box (Umbrel nebo Start9).

![ALBY HUB](assets/fr/02.webp)

Pro místní instalaci do počítače [stáhněte a nainstalujte software podle svého operačního systému](https://github.com/getAlby/hub/releases) a poté postupujte podle stejných pokynů v rozhraní.

![ALBY HUB](assets/fr/03.webp)

## Vytvoření účtu Alby

Prvním krokem je vytvoření účtu Alby. Ten sice není pro používání Alby Hub nezbytný, ale umožňuje plně využívat dostupné možnosti, včetně možnosti získání adresy Lightning.

Přejděte na [oficiální webové stránky Alby](https://getalby.com/) a klikněte na tlačítko "*Vytvořit účet*".

![ALBY HUB](assets/fr/04.webp)

Zadejte přezdívku a e-mailovou adresu a klikněte na "*Přihlásit se*". Tato e-mailová adresa bude později sloužit k přihlášení k vašemu účtu.

![ALBY HUB](assets/fr/05.webp)

Zadejte ověřovací kód, který jste obdrželi e-mailem.

![ALBY HUB](assets/fr/06.webp)

Po přihlášení k online účtu klikněte na tlačítko "*Pokračovat*".

![ALBY HUB](assets/fr/07.webp)

Znovu klikněte na tlačítko "*Pokračovat*".

![ALBY HUB](assets/fr/08.webp)

## Možnost hostování v cloudu

Poté si budete muset vybrat mezi možností vlastního hostování, kdy hostujete uzel Lightning na vlastním hardwaru, a placenou možností s využitím cloudu společnosti Alby. Začnu vysvětlením, jak postupovat u možnosti Cloud (upozorňuji, že se jedná o placenou možnost, podrobnosti viz předchozí část).

Klikněte na "*Upgrade*".

![ALBY HUB](assets/fr/09.webp)

Potvrďte kliknutím na "*Předplatit nyní*".

![ALBY HUB](assets/fr/10.webp)

Klikněte na "*Spustit Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Počkejte několik okamžiků, než se uzel vytvoří.

![ALBY HUB](assets/fr/12.webp)

A to je vše, váš Alby Hub je nyní nakonfigurován. V další části vám ukážu, jak nainstalovat Alby Hub na existující uzel. Pokud to nepotřebujete, můžete přejít k další části a uzel nakonfigurovat.

![ALBY HUB](assets/fr/13.webp)

## Možnost vlastního hostingu

Pokud dáváte přednost použití Alby Hub jako rozhraní pro stávající uzel Lightning, máte několik možností: nainstalovat jej na server, lokálně do počítače nebo prostřednictvím uzlu v krabici (Umbrel nebo Start9). Použití Alby Hub v těchto konfiguracích je bezplatné. Zaměříme se na možnost node-in-box, protože se domnívám, že serverová varianta bez fyzického přístupu představuje podobná rizika jako cloudová verze a místní instalace na počítači je často nevhodná.

Chcete-li tuto funkci nastavit v systému Umbrel (kroky pro Start9 jsou totožné), musíte mít nejprve nakonfigurovaný uzel LND.

Přihlaste se do rozhraní Umbrel a přejděte do obchodu s aplikacemi.

![ALBY HUB](assets/fr/14.webp)

Vyhledejte aplikaci "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Nainstalujte jej do uzlu.

![ALBY HUB](assets/fr/16.webp)

Rozhraní Alby Hub je nyní připraveno. Zbytek návodu můžete sledovat, jako byste používali cloudové rozhraní, ale bez možností placené verze. Navíc na rozdíl od cloudové verze jsou vaše klíče uloženy lokálně ve vašem uzlu, nikoli na serverech Alby.

![ALBY HUB](assets/fr/17.webp)

## Spuštění Alby Hub

Klikněte na tlačítko "*Začít*".

![ALBY HUB](assets/fr/18.webp)

Alby Hub vás poté vyzve ke zvolení hesla. Toto heslo je velmi důležité, protože bude použito k zašifrování vaší peněženky. V placené cloudové verzi jsou vaše klíče uloženy na serveru Alby, zašifrovány tímto heslem, které znáte pouze vy, a poté dešifrovány a uloženy pouze v paměti RAM, aby bylo možné v případě potřeby podepisovat transakce.

Proto je nutné zvolit silné heslo. Kdokoli s tímto heslem může potenciálně získat přístup k vašemu uzlu. Ujistěte se, že jste si také vytvořili jednu nebo více fyzických záloh tohoto hesla na kus papíru nebo ještě lépe na kus kovu pro větší bezpečnost. **Pokud toto heslo ztratíte, bude nemožné obnovit přístup k vašim bitcoinům**, protože Alby nemá možnost ho obnovit. Ztráta tohoto hesla znamená ztrátu vašich bitcoinů.

Po pečlivém výběru a uložení hesla klikněte na "*Vytvořit heslo*".

![ALBY HUB](assets/fr/19.webp)

Nyní máte přístup k uzlu Lightning.

![ALBY HUB](assets/fr/20.webp)

Nejdříve je třeba uložit frázi pro obnovení, ze které jsou odvozeny klíče. Tato fráze vám umožní obnovit přístup k vaší onchain peněžence a s posledním stavem vašich kanálů i k vašim sats na Lightningu. Chcete-li tak učinit, klikněte na "*Nastavení*".

![ALBY HUB](assets/fr/21.webp)

Poté přejděte na kartu "*Zálohování*". Pro přístup k ní zadejte své heslo.

![ALBY HUB](assets/fr/22.webp)

Poté získáte přístup ke své frázi pro obnovu o 12 slovech. Vytvořte si jednu nebo více fyzických záloh této fráze na papíře nebo kovu a uložte je na bezpečném místě.

![ALBY HUB](assets/fr/23.webp)

Po uložení fráze zaškrtněte políčko pro potvrzení jejího uložení a klikněte na tlačítko "*Pokračovat*".

![ALBY HUB](assets/fr/24.webp)

## Jak mohu obnovit přístup ke svým bitcoinům?

Před odesláním finančních prostředků do uzlu je důležité pochopit, jak je v případě problému získat zpět a jaké informace jsou k tomu potřeba. Postup se liší podle povahy prostředků, které mají být obnoveny, a podle režimu hostování vašeho uzlu.

Pro uživatele placeného cloudu vyžaduje úplné obnovení bitcoinů tři základní prvky:


- Vaše fráze pro zotavení;
- Vaše heslo (heslo používané pro váš uzel) ;
- Přístup k účtu Alby, abyste získali aktuální stav svých kanálů Lightning.

Absence kterékoli z těchto tří informací by znemožnila získat vaše bitcoiny zpět v plné výši.

V případě hostitelů vlastního uzlu je proces obnovení stejný jako u jakéhokoli uzlu Lightning. Budete potřebovat :


- Vaše fráze pro zotavení;
- Nejnovější stav vašich kanálů Lightning. Pro zabezpečení těchto informací nabízí společnost Umbrel [možnost](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) jejich šifrování a dynamické a anonymní ukládání prostřednictvím sítě Tor.

## Zakupte si svůj první kanál Lightning

Nyní můžete postupovat podle pokynů společnosti Alby Hub. Kliknutím na tlačítko otevřete první kanál pro příchozí hotovost.

![ALBY HUB](assets/fr/25.webp)

Vyberte možnost "*Otevřít kanál*". Pokud nemáte v úmyslu stát se směrovacím uzlem a výslovně ho nepotřebujete, doporučuji zvolit soukromé kanály.

![ALBY HUB](assets/fr/26.webp)

Alby Hub vám vygeneruje fakturu k úhradě. Tato platba pokrývá transakční poplatky potřebné k otevření vašeho kanálu a také poplatky za služby poskytovatele služeb LSP (*Lightning Service Provider*), který otevře kanál k vašemu uzlu a umožní vám okamžitě přijímat platby.

![ALBY HUB](assets/fr/27.webp)

Po zaplacení faktury a potvrzení transakce je vytvořen první kanál Lightning.

![ALBY HUB](assets/fr/28.webp)

Na kartě "*Node*" vidíte, že nyní máte příchozí hotovost, což vám umožňuje přijímat platby prostřednictvím služby Lightning.

![ALBY HUB](assets/fr/29.webp)

Chcete-li přijmout platbu, klikněte na kartu "*Peněženka*" a poté na "*Přijmout*".

![ALBY HUB](assets/fr/30.webp)

Zadejte částku, případně přidejte popis a klikněte na tlačítko "*Vytvořit fakturu*".

![ALBY HUB](assets/fr/31.webp)

Obdržel jsem první platbu ve výši 120 000 sats.

![ALBY HUB](assets/fr/32.webp)

Po návratu na kartu "*Peněženka*" můžete zkontrolovat zůstatek v peněžence. Všimněte si, že při první platbě si Alby Hub automaticky odloží 354 sátů. Pro každý kanál Lightning, který následně otevřete, Alby Hub automaticky vyhradí rezervu odpovídající 1 % kapacity kanálu. Tato rezerva je bezpečnostní opatření, které vašemu uzlu umožňuje získat zpět prostředky kanálu v případě pokusu o podvod ze strany vašeho partnera. Proto, přestože jsem odeslal 120 000 sátů, je na mém zůstatku uvedeno pouze 119 646 sátů.

![ALBY HUB](assets/fr/33.webp)

## Ukládání bitcoinů onchain

Pokud chcete mít k dispozici odchozí hotovost k provádění plateb, můžete si také sami otevřít kanál. K tomu budete potřebovat onchain bitcoiny ve své peněžence.

Na kartě "*Node*" klikněte na "*Deposit*".

![ALBY HUB](assets/fr/34.webp)

Odeslat bitcoiny na zobrazenou adresu. Tato adresa je odvozena z vaší dříve uložené obnovovací fráze.

![ALBY HUB](assets/fr/35.webp)

Odeslal jsem 72 000 satelitů. Nyní jsou vidět v "*Savings Balance*", což zahrnuje všechny prostředky, které vlastním na řetězci, a ne na Lightningu.

![ALBY HUB](assets/fr/36.webp)

## Otevření kanálu Lightning

Nyní, když máte prostředky v řetězci, můžete otevřít nový kanál Lightning. Doporučujeme otevřít několik kanálů s dostatečnými částkami, abyste mohli vždy provádět platby bez omezení. Většina poskytovatelů služeb LSP (*Lightning Service Providers*) vyžaduje minimálně 150 000 sátů, aby si u vás mohli otevřít kanál.

Na kartě "*Node*" klikněte na "*Otevřít kanál*".

![ALBY HUB](assets/fr/37.webp)

Vyberte velikost kanálu. Doporučuji, abyste neotevírali příliš malé kanály, neboť je třeba mít na paměti, že se jedná o uzel Lightning a stroj, na kterém jsou vaše klíče umístěny, nenabízí stejnou úroveň zabezpečení jako hardwarová peněženka. Buďte tedy opatrní s částkami, které se rozhodnete blokovat.

![ALBY HUB](assets/fr/38.webp)

V nabídce "*Rozšířené možnosti*" můžete zvolit, kterým LSP se má kanál otevřít, nebo ručně zadat jiný uzel Lightning.

![ALBY HUB](assets/fr/39.webp)

Poté klikněte na "*Otevřít kanál*".

![ALBY HUB](assets/fr/40.webp)

Počkejte, až bude váš kanál potvrzen v řetězci.

![ALBY HUB](assets/fr/41.webp)

Váš nový kanál se nyní zobrazí na kartě "*Uzel*".

![ALBY HUB](assets/fr/42.webp)

## Připojení aplikace pro výpočet výdajů

Nyní, když máte funkční uzel Lightning, můžete jej používat ke každodennímu přijímání a utrácení satelitů. Webové rozhraní Alby Hub je sice praktické pro správu uzlu, ale není ideální pro provádění rychlých transakcí na cestách. K tomu budeme používat aplikaci Lightning wallet nainstalovanou v chytrém telefonu.

V tomto návodu doporučuji zvolit aplikaci Alby Go, která se velmi snadno používá, ale můžete použít i jiné kompatibilní aplikace, například Zeus.

![ALBY HUB](assets/fr/43.webp)

Chcete-li nainstalovat aplikaci Alby Go, přejděte do obchodu s aplikacemi ve svém zařízení:


- [Pro Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Pro Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Uživatelé systému Android si mohou aplikaci nainstalovat také prostřednictvím souboru `.apk` [dostupného na Albyho GitHubu](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Po spuštění aplikace klikněte na "*Připojit peněženku*".

![ALBY HUB](assets/fr/46.webp)

V centru Alby klikněte na kartě "*Připojení*" na možnost "*Přidat připojení*".

![ALBY HUB](assets/fr/47.webp)

Pojmenujte toto připojení, abyste ho mohli snadno identifikovat ve svém rozbočovači, a vyberte oprávnění, která chcete aplikaci udělit. V mém případě jsem zvolil možnost "*Plný přístup*", abych měl plný přístup k prostředkům svého uzlu Lightning z chytrého telefonu, ale můžete také omezit přístup maximálním rozpočtem, vybrat povolené funkce nebo nastavit datum vypršení platnosti těchto oprávnění. Po konfiguraci klikněte na tlačítko "*Další*".

![ALBY HUB](assets/fr/48.webp)

Rozbočovač Alby Hub poté vygeneruje tajný kód pro navázání spojení.

![ALBY HUB](assets/fr/49.webp)

Vraťte se do aplikace Alby Go, naskenujte QR kód nebo vložte tajenku.

![ALBY HUB](assets/fr/50.webp)

Klikněte na "Finish*".

![ALBY HUB](assets/fr/51.webp)

Nyní máte vzdálený přístup ke svému uzlu Lightning ze svého chytrého telefonu, takže můžete snadno vydávat a přijímat satelity každý den na cestách.

![ALBY HUB](assets/fr/52.webp)

V případě potřeby můžete oprávnění pro toto připojení spravovat přímo v Alby Hubu kliknutím na něj.

![ALBY HUB](assets/fr/53.webp)

Chcete-li přijímat satelity, klikněte na "*Přijmout*".

![ALBY HUB](assets/fr/54.webp)

Kliknutím na "*Faktura*" upravte částku a popis faktury.

![ALBY HUB](assets/fr/55.webp)

Nabijte fakturu na příjem satelitů.

![ALBY HUB](assets/fr/56.webp)

Chcete-li odeslat saty, klikněte na "*Odeslat*".

![ALBY HUB](assets/fr/57.webp)

Naskenujte fakturu, kterou chcete zaplatit.

![ALBY HUB](assets/fr/58.webp)

Poté klikněte na "*Pay*".

![ALBY HUB](assets/fr/59.webp)

Vaše transakce je potvrzena.

![ALBY HUB](assets/fr/60.webp)

Kliknutím na malou šipku získáte přístup k historii transakcí.

![ALBY HUB](assets/fr/61.webp)

Tyto transakce jsou také viditelné ve vašem centru Alby Hub.

![ALBY HUB](assets/fr/62.webp)

## Přizpůsobení adresy Lightning

Alby nabízí možnost bleskové adresy. Ta vám umožní přijímat platby na uzel, aniž byste museli pokaždé ručně generovat fakturu. Ve výchozím nastavení vám Alby přiřadí adresu Lightning, ale můžete si ji přizpůsobit. Přihlaste se do svého online účtu Alby, klikněte na své jméno v pravém horním rohu a poté vyberte možnost "*Nastavení*".

![ALBY HUB](assets/fr/63.webp)

Přejděte do nabídky "*Lightning Address*".

![ALBY HUB](assets/fr/64.webp)

Upravte svou adresu a potvrďte ji kliknutím na "*Aktualizovat bleskovou adresu*".

![ALBY HUB](assets/fr/65.webp)

Vezměte prosím na vědomí, že po změně adresy vám již nepatří. Proto se ujistěte, že na ni již nikdy nebudete posílat saty.

A to je vše, nyní víte, jak používat Lightning s vlastním uzlem pomocí nástroje Alby Hub. Pokud se vám tento návod zdál užitečný, budu vám velmi vděčný, když mi pod něj dáte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Moc vám děkuji!

Chcete-li podrobně pochopit všechny mechanismy blesku, které jsme v tomto tutoriálu použili, doporučuji vám, abyste si prohlédli naše bezplatné školení na toto téma :

https://planb.network/courses/lnp201