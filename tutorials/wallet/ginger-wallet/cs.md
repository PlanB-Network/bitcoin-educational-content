---
name: Ginger Wallet
description: Software Bitcoin wallet s otevřeným zdrojovým kódem, fork z Wasabi Wallet, integrace Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet je otevřený zdrojový kód, který není součástí portfolia Bitcoin a je zaměřen na důvěrnost a soukromí. Vznikl jako fork z Wasabi Wallet (po verzi 2.0.7.2 - licence MIT).



Ginger Wallet zachovává technickou architekturu Wasabi a přidává několik specifických funkcí. Podle dokumentace [Ginger Wallet](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) klade Wasabi důraz na **autonomii a ovládání**, zatímco Ginger se zaměřuje na **snadné používání, bezpečnost a zjednodušené prostředí**, což jej činí přístupným i pro ty, kteří jsou s technickými aspekty méně obeznámeni.



Ginger Wallet je software wallet pouze pro počítače (bez mobilní aplikace).



## Co je Coinjoin?



**coinjoin** je speciální struktura transakce Bitcoin, která spojuje několik účastníků v jedné společné transakci. Tento mechanismus mísí vstupy různých uživatelů do společné transakce, což velmi ztěžuje - ne-li často znemožňuje, pokud je provedeno správně - dohledání finančních prostředků. V důsledku toho je pro vnějšího pozorovatele téměř nemožné s jistotou určit původ a určení zúčastněných bitcoinů, na rozdíl od běžných transakcí Bitcoin.



Pro vás jako uživatele pomáhá coinjoin zachovat důvěrnost. Pokud například obdržíte dar ve výši 10 000 sats na adresu Bitcoin, odesílatel může tyto prostředky vysledovat a v některých případech odvodit, že držíte větší množství bitcoinů, nebo sledovat vaše aktivity. Tím, že po tomto daru ve výši 10 000 sats provedete coinjoin, tuto sledovatelnost přerušíte: odesílatel již nebude moci z této platby o vás odvodit žádné informace.



Chaumian coinjoin nabízí vysokou úroveň zabezpečení, protože finanční prostředky zůstávají po celou dobu pod výhradní kontrolou uživatele. Ani provozovatelé koordinačních serverů nemohou bitcoiny účastníků za žádných okolností odklonit. Uživatelé ani koordinátoři si nemusí navzájem důvěřovat: každý si ponechává kontrolu nad svými soukromými klíči a zůstává výhradně oprávněn ověřovat transakce. Žádná třetí strana si tedy nemůže během coinjoinu přivlastnit vaše bitcoiny ani vytvořit přímé spojení mezi vašimi vstupy a výstupy.



Chcete-li se o coinjoinu dozvědět více, podívejte se na kurz Plan ₿ Academy BTC 204 :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Instalace Ginger Wallet



Chcete-li nainstalovat zázvor Wallet, navštivte webovou stránku [Ginger Wallet](https://gingerwallet.io).



Stisknutím tlačítka **Stáhnout** stáhnete správnou verzi pro svůj počítač (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Další možností je přejít na stránku projektu [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) a stáhnout si ji.



![screen](assets/fr/04.webp)



Poté spusťte instalační program.



![screen](assets/fr/05.webp)




## Nastavení parametrů



### Předběžné konfigurace



Otevřete aplikaci Ginger Wallet a vyberte preferovaný jazyk.



![screen](assets/fr/06.webp)



Ginger vás hned na začátku upozorní na náklady spojené s procesem spojování mincí.



![screen](assets/fr/07.webp)



Poté stiskněte tlačítko **Start** a poté tlačítko **Nový** a vytvořte nové portfolio.



![screen](assets/fr/08.webp)



Poté uložte a potvrďte seedphrase.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Pro větší bezpečnost je možné ke kameře Ginger Wallet přidat kameru passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Po přidání tohoto kódu passphrase bude vyžadován při každém pokusu o přístup k vašemu portfoliu.



![screen](assets/fr/12.webp)



Ginger při vytváření portfolia automaticky aktivuje výchozí funkci **Coinjoin**. Jste o tom informováni a můžete si pak toto nastavení upravit podle svých potřeb.



![screen](assets/fr/13.webp)




### Obecná nastavení



Po vytvoření prvního portfolia budete přesměrováni do rozhraní Ginger Wallet.



![screen](assets/fr/14.webp)



Pokud chcete zůstatky v peněženkách skrýt, aktivujte **diskrétní režim**.



![screen](assets/fr/15.webp)



V aplikaci Ginger Wallet můžete vytvořit více portfolií. Stačí kliknout na **Přidat portfolio**.



![screen](assets/fr/16.webp)



Ginger podporuje používání hardwarových portfolií prostřednictvím standardního rozhraní Bitcoin Core, ačkoli přímá integrace z hardwarového portfolia nebo do něj zatím není k dispozici.



Mezi kompatibilní hardwarová portfolia patří (mimo jiné) :




- Blockstream Jade
- Karta Coldcard MK4
- Karta Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- atd.



Nyní klikněte na možnost **Nastavení**.



![screen](assets/fr/17.webp)



Tato nastavení jsou obecná nastavení aplikace a konfigurace, které zde provedete, budou platit pro všechna portfolia.



V části **Nastavení** máte k dispozici karty :





- Obecné**



![screen](assets/fr/18.webp)





- Vzhled



Na této kartě můžete mimo jiné změnit jazyk, měnu a jednotku zobrazení poplatků (BTC/Satoshi).



![screen](assets/fr/19.webp)





- Bitcoin**



Na této kartě můžete povolit spuštění modulu Bitcoin Knots při spuštění aplikace, vybrat síť (Main/RegTest) a poskytovatele poplatků (Mempool Space/Blockstream info/Full Node) atd.



![screen](assets/fr/20.webp)





- Bezpečnostní prvky**



Na kartě Zabezpečení můžete povolit dvoufaktorové ověřování, aktivovat nebo deaktivovat Tor a dokonce jej zakázat po zavření aplikace Ginger.



![screen](assets/fr/21.webp)



**NB** :




- Pro dvoufaktorové ověřování se ujistěte, že vaše ověřovací aplikace podporuje protokol SHA256 a 8místné kódy. Ginger Wallet vyžaduje 8místný kód 2FA pro zvýšení zabezpečení. Díky tomuto delšímu formátu je mnohem obtížnější kód uhodnout nebo prolomit, což nabízí větší ochranu proti neoprávněnému přístupu.
- Ve výchozím nastavení prochází veškerý provoz sítě Ginger přes Tor, takže není třeba provádět ruční konfiguraci. Pokud je v systému Tor již aktivní, Ginger mu automaticky přidělí prioritu.



Jakmile však Tor v nastavení deaktivujete, vaše soukromí zůstane obecně zachováno, s výjimkou dvou situací:




- během spojení Coinjoin by koordinátor mohl propojit vaše vstupy a výstupy s vaší IP adresou;
- při vysílání transakce by mohl zlomyslný uzel, ke kterému se připojíte, spojit vaši transakci s vaší IP adresou.



Nezapomeňte pokaždé stisknout tlačítko **Done** (v pravém dolním rohu), abyste uložili nastavení. Aby se některá nastavení projevila, je třeba přístroj Ginger Wallet restartovat.



Kromě toho můžete v horní části portfolií vyhledávat a přistupovat k jakémukoli parametru atd...



![screen](assets/fr/22.webp)




### Konfigurace portfolia



V aplikaci lze vytvořit několik portfolií, takže každé portfolio lze nakonfigurovat podle svých potřeb. To provedete kliknutím na **tři tečky** před názvem portfolia a poté na **Nastavení portfolia**.



![screen](assets/fr/23.webp)



Jak vidíte, kromě parametru wallet uvidíte své UTXO (seznam vlastněných tokenů), statistiky a informace o wallet (například rozšířený veřejný klíč).



Chcete-li se vrátit ke konfiguraci našeho portfolia, klikněte na parametry portfolia a dostanete se na následující karty:




- Obecné** (kde můžete změnit název portfolia) ;



![screen](assets/fr/24.webp)





- Coinjoin** (kde můžete upravit nastavení coinjoinu pro tento wallet) ;



![screen](assets/fr/25.webp)





- Nástroje** (kde můžete zkontrolovat své portfolio seedphrase, znovu jej synchronizovat nebo odstranit).



![screen](assets/fr/26.webp)




## Přijímání bitcoinů



![video](https://youtu.be/cqv35wBDWMQ)



Přijímání bitcoinů v wallet na Ginger Wallet:




- stiskněte tlačítko **Přijmout** ;



![screen](assets/fr/27.webp)





- Zadejte název zdroje, ke kterému chcete adresu přiřadit. Toto označení slouží k evidenci plateb. Nemá to žádné důsledky pro on-chain; jde pouze o informace o dohledatelnosti uložené lokálně ve vaší aplikaci;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klikněte na malou šipku vlevo od tlačítka **Generovat** a zvolte formát adresy (**SegWit** /**Taproot**) , poté klikněte na tlačítko **Generovat**, abyste generate adresu a QR kód.



![screen](assets/fr/29.webp)



Tuto adresu nebo QR kód použije odesílatel k zaslání bitcoinů.



![screen](assets/fr/30.webp)




## Odeslat bitcoiny




![video](https://youtu.be/2nf5aAimfhg)



Za tímto účelem :




- Stiskněte tlačítko **Odeslat**;
- zadejte adresu příjemce, částku k odeslání a štítek;
- zkontrolujte přehled transakcí a potvrďte odeslání.



![screen](assets/fr/31.webp)




## Utrácet bitcoiny



Je snadné nakupovat a prodávat Bitcoin se zázvorem Wallet. V několika málo krocích můžete utratit své bitcoiny.



### Koupit bitcoiny



![video](https://youtu.be/lEqTBzm5MEA)



Uživatelé služby Ginger Wallet mohou nakupovat bitcoiny.





- Stiskněte tlačítko **Koupit**. Toto tlačítko zůstane viditelné, i když je wallet prázdná.



![screen](assets/fr/32.webp)





- Před nákupem bitcoinu si vyberte svou zemi nebo dokonce stát (v některých oblastech, například v Kanadě). Když poprvé kliknete na funkci **Koupit**, budete muset zadat také svůj region.



![screen](assets/fr/33.webp)



Stisknutím tlačítka **Pokračovat** projdete nákupním procesem.





- Do vyhrazeného pole pak zadejte částku bitcoinů, kterou chcete zakoupit. Můžete si také vybrat měnu transakce.



![screen](assets/fr/34.webp)



Každá měna má minimální a maximální limit nákupu. Například v USD je maximální limit 30 000 USD.



Pokud jste již provedli nákup, můžete si prohlédnout historii transakcí kliknutím na tlačítko **Předchozí objednávky**. Zobrazí se seznam minulých transakcí a jejich stav.





- Vyberte si nabídku, která vám vyhovuje.



V tomto okamžiku se zobrazí seznam všech dostupných nabídek. U každé nabídky máte :




 - název dodavatele (1) ;
 - počet bitcoinů odpovídající dříve zadané částce, způsob platby a nákupní poplatek (2) ;
 - tlačítko **Accept** (3).



![screen](assets/fr/35.webp)



Poplatky uvedené v nabídce nepředstavují dodatečné náklady. Jsou již zahrnuty v celkové částce nabídky.



V pravém horním rohu obrazovky, označeném **Všechny**, můžete nabídky filtrovat podle způsobu platby. Vybraný způsob platby bude nastaven jako výchozí, ale můžete jej kdykoli změnit.



![screen](assets/fr/36.webp)



Pokud najdete vhodnou nabídku, klikněte na tlačítko **Přijmout** a pokračujte v nákupu. Poté budete přesměrováni na stránku prodávajícího, kde můžete transakci dokončit.



### Prodej bitcoinů



Uživatelé zázvoru Wallet mohou prodávat Bitcoin. Tlačítko **Prodat** je viditelné pouze v případě, že jsou v portfoliu k dispozici finanční prostředky.





- Klikněte na možnost **Prodat**.



![screen](assets/fr/37.webp)





- Stejně jako u možnosti **Koupit** musíte při prvním použití funkce Prodej před zahájením prodeje bitcoinů vybrat svou zemi.





- Dále musíte zadat částku bitcoinů, kterou chcete prodat. Tuto částku můžete zadat v BTC nebo ve fiat měně, například v americkém dolaru (USD).





- Jakmile to uděláte, zobrazí se seznam dostupných nabídek. Vyberte si prodejní nabídku, která vám vyhovuje, a pokračujte kliknutím na tlačítko **Přijmout**.





- Nyní je třeba transakci dokončit:
 - Po přijetí nabídky budete přesměrováni na stránku dodavatele;
 - Postupujte podle pokynů na stránce dodavatele ;
 - V určitém okamžiku obdržíte adresu příjemce a přesnou částku k odeslání;
 - Poté se vraťte do aplikace Ginger Wallet a pokračujte v procesu;
 - Po návratu do aplikace Ginger Wallet se zobrazí dialogové okno, ve kterém můžete pokračovat kliknutím na tlačítko **Odeslat**.



Otevře se obrazovka **Odeslat** s předvyplněnou adresou příjemce a částkou. Můžete také použít tlačítko **Odeslat** na domovské obrazovce. Přestože můžete transakci odeslat ručně, doporučujeme ji pro optimalizaci procesu dokončit prostřednictvím dialogového okna.



## Vytvoření mincovního spojení v aplikaci Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Chraňte důvěrnost svých bitcoinů pomocí služby **Coinjoin** integrované přímo do aplikace Ginger Wallet. wallet používá **WabiSabi**, chaumský protokol coinjoin navržený tak, aby usnadňoval přístupnější a efektivnější coinjoiny.



Záleží jen na vás, jakou strategii spojování mincí (automatickou nebo ruční) si zvolíte.



Ginger Coinjoin je připraven k použití ihned po stažení (není třeba provádět žádné další kroky). Ginger Coinjoin automaticky běží na pozadí, aby chránil vaše soukromí při každé transakci. V praxi se přehrávač Coinjoin zobrazí vždy, když máte zůstatek, který lze anonymizovat.



Pokud jde o ruční spuštění funkce coinjoin, je to operace na jedno kliknutí. Spusťte kolo a počkejte na sestavení a potvrzení transakce coinjoin. V rozhraní se zobrazí skóre anonymizace.



Lze provést několik kombinací, dokud není dosaženo požadované úrovně anonymity. Z mixu můžete také vyloučit určité části.



Ve výchozím nastavení používá Ginger vlastního koordinátora se všemi přednastavenými parametry a garantovanými poplatky. Za spojení tokenů v hodnotě vyšší než 0,03 BTC je kromě poplatku mining účtován také 0,3% poplatek koordinátorovi. Vstupy v hodnotě 0,03 BTC nebo nižší, stejně jako remixy, jsou od poplatků koordinátora osvobozeny, a to i po jedné transakci. Platba provedená prostředky Coinjoin tedy umožňuje odesílateli i příjemci remixovat své mince, aniž by jim vznikly poplatky koordinátora.



Ginger dává přednost coinjoinům s více účastníky před menšími a rychlejšími koly. Větší coinjoiny nabízejí větší anonymitu, nižší náklady a větší efektivitu blokového prostoru.




## Bezpečnost a osvědčené postupy



Snaha o decentralizaci a zachování soukromí vyžadují přijetí několika osvědčených postupů:




- Přístroj seedphrase vždy uchovávejte na bezpečném místě mimo síť;
- Pokud počítač ztratíte nebo máte podezření na neoprávněný přístup, okamžitě vytvořte nový účet wallet. Převeďte své prostředky do tohoto nového portfolia a staré vymažte;
- Pro každý příjem použijte jinou adresu, abyste se vyhnuli opakovanému používání adres;
- Aplikace portfolia stahujte vždy výhradně z oficiálního účtu GitHub nebo z oficiálních webových stránek.



Nyní jste se seznámili s používáním aplikace Ginger Wallet k odesílání, přijímání a utrácení bitcoinů.



Pokud pro vás byl tento návod užitečný, zanechte mi prosím níže zelený palec. Neváhejte sdílet tento článek prostřednictvím svých sociálních sítí. Moc vám děkuji!



Doporučuji vám také podívat se na tento návod, jak používat počítačovou aplikaci Liana k odesílání a přijímání bitcoinů a jak realizovat automatizovaný plán pozůstalosti.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04