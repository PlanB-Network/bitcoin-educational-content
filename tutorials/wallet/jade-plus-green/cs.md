---
name: Jade Plus - zelená
description: Snadná konfigurace systému Jade Plus s technologií Green
---
![cover](assets/cover.webp)

Jade Plus je hardwarová peněženka určená pouze pro bitcoiny, kterou navrhla společnost Blockstream. Je to nástupce klasické peněženky Jade s vylepšeným softwarem, více možnostmi a přepracovanou ergonomií pro intuitivnější používání. Tato nová verze se může pochlubit nádherným 1,9palcovým LCD displejem s širším barevným gamutem než její předchůdce. Optimalizována byla také tlačítka a navigace v nabídkách.

Jade Plus lze používat několika způsoby: přes kabelové připojení USB-C, v režimu "*Air-Gap*" s kartou micro SD (nutný adaptér), přes Bluetooth nebo dokonce výměnou QR kódů díky integrované kameře. Tato hardwarová peněženka je napájena z baterie.

V základní černé verzi je k dispozici od 149,99 USD, cena se může zvýšit až o 20 USD za verze "*Genesis Grey*" nebo "*Lunar Silver*". Jade Plus je tedy zajímavou volbou s pokročilými funkcemi srovnatelnými s funkcemi špičkových hardwarových peněženek, jako jsou Coldcard Q nebo Passport V2, ale za poměrně nízkou cenu, blízkou modelům střední třídy.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Jade Plus je kompatibilní s většinou softwaru pro správu portfolia. Zde je přehled kompatibility v době psaní článku (leden 2025):

| Stolní počítače | Mobilní zařízení | USB | Bluetooth | QR | JadeLink | Software pro správu

| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |

| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 | 🔴

| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

| Vrabec | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 |

| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 |

| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |

| Keeper | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |

V tomto návodu nastavíme a budeme používat zařízení Jade Plus s mobilní aplikací Green Wallet společnosti Blockstream prostřednictvím připojení Bluetooth. Toto nastavení je ideální pro začátečníky. Pokud hledáte pokročilejší přístup, doporučuji podívat se na tento návod, kde používáme Jade Plus s peněženkou Sparrow Wallet v režimu QR kódů:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Bezpečnostní model Jade Plus

Jade Plus používá bezpečnostní model založený na "virtuálním bezpečném prvku", který je zhmotněn "slepým orákulem". Konkrétně tento mechanismus kombinuje PIN zvolený uživatelem, tajemství umístěné v systému Jade a tajemství držené orákulem (serverem spravovaným společností Blockstream) a vytváří klíč AES-256 distribuovaný mezi dvěma entitami. Během iniciace se výměnou ECDH zabezpečí komunikace s orákulem a zašifruje se fráze pro obnovení v hardwarové peněžence. V praxi to znamená, že když chcete získat přístup k seedu pro podepisování transakcí, potřebujete přístup k :


- K samotnému zařízení Jade Plus;
- Kód PIN pro odemknutí zařízení ;
- A k tajemství věštírny.

Hlavní výhodou tohoto přístupu je absence jediného bodu selhání na úrovni hardwaru, protože pokud útočník někdy získá přístup k vašemu Jade, extrakce klíčů vyžaduje současné ohrožení Jade a orákula. Tento model také znamená, že Jade Plus je zcela open-source, čímž se vyhýbá omezením spojeným s používáním skutečně fyzicky zabezpečených prvků, jaké se používají například u Ledgeru.

Nevýhodou tohoto systému je, že použití systému Jade Plus závisí na věštírně, kterou spravuje společnost Blockstream. Pokud se toto orákulum stane nedostupným, není již možné používat hardwarovou peněženku přímo s PIN kódem. To však neznamená, že vaše bitcoiny jsou ztraceny, protože je stále můžete získat zpět pomocí obnovovací fráze, kterou můžete zadat v systému Jade Plus v režimu "*stateless*". Chcete-li tuto závislost obejít, můžete si také nakonfigurovat a spravovat vlastní oracle server.

## Rozbalení modelu Jade Plus

Po obdržení produktu Jade Plus zkontrolujte, zda jsou krabice a pečeť v dobrém stavu, abyste se ujistili, že váš balíček nebyl otevřen.

![JADE-PLUS-GREEN](assets/fr/02.webp)

V krabici najdete :


- Le Jade Plus;
- Kabel USB-C;
- Karty pro záznam mnemotechnické fráze jako slova nebo jako "*CompactSeedQR*";
- Některé pokyny k použití ;
- Šňůra;
- Některé nálepky.

![JADE-PLUS-GREEN](assets/fr/03.webp)

Zařízení má 4 navigační tlačítka:


- Tlačítko vpravo dole zapne nefrit;
- Velké tlačítko na přední straně přístroje slouží k výběru položky;
- Dvě malá tlačítka v horní části umožňují navigaci doleva a doprava;
- Položku můžete vybrat také současným kliknutím na dvě tlačítka v horní části zařízení.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Nastavení nové peněženky Bitcoin

Klikněte na tlačítko Start.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Klikněte na "*Nastavení Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Zvolte možnost "Zahájit nastavení". Volba "*Pokročilé nastavení*" dělá totéž, ale s přístupem k pokročilým nastavením.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Poté klikněte na "*Vytvořit novou peněženku*" a vygenerujte nový seed.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Kliknutím na tlačítko "*Pokračovat*" zobrazíte novou frázi pro obnovení.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Jade Plus zobrazí vaši 12slovnou mnemotechnickou frázi. **Tato mnemotechnická fráze vám dává plný, neomezený přístup ke všem vašim bitcoinům. Kdokoli, kdo tuto frázi zná, může vaše prostředky ukrást, a to i bez fyzického přístupu k vašemu Jade Plus. Dvanáctislovná fráze obnoví přístup k vašim bitcoinům v případě ztráty, krádeže nebo rozbití vašeho Jade. Je proto velmi důležité ji pečlivě uložit a uchovávat na bezpečném místě.

Můžete jej napsat na karton dodávaný v krabici, nebo pro větší bezpečnost doporučuji vyrýt jej na podstavec z nerezové oceli, který jej ochrání před požárem, povodní nebo zřícením.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Pro více informací o správném způsobu ukládání a správy mnemotechnických frází vřele doporučuji sledovat tento další návod, zejména pokud jste začátečníci:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Samozřejmě nesmíte tato slova nikdy sdílet na internetu, jak to dělám v tomto návodu. Toto ukázkové portfolio bude použito pouze na Testnetu a po skončení výukového kurzu bude smazáno

Kliknutím na šipku v pravé části obrazovky zobrazíte následující slova.

![JADE-PLUS-GREEN](assets/fr/11.webp)

Po uložení fráze vás aplikace Jade Plus vyzve k jejímu potvrzení. Pomocí tlačítek v horní části zařízení vyberte správné slovo podle pořadí a kliknutím na prostřední tlačítko přejděte na další slovo.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Připojení služby Jade Plus k zelené peněžence

V tomto návodu budeme ke správě peněženky umístěné v zařízení Jade Plus používat aplikaci Green Wallet. Tato metoda je vhodná zejména pro začátečníky. Pokud chcete spravovat peněženku s bitcoiny podrobněji, můžete použít také aplikaci Sparrow Wallet, které se budeme věnovat v samostatném tutoriálu:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Pokyny k instalaci a nastavení aplikace Blockstream Green naleznete v první části tohoto dalšího návodu:

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

V aplikaci Blockstream Green klikněte na tlačítko "*Konfigurace nového portfolia*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Vyberte možnost "*Na hardwarové peněžence*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Aktivujte Bluetooth ve smartphonu a klikněte na tlačítko "*Připojit Jade*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Autorizujte zelenou aplikaci pro přístup k připojení Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

Aplikace hledá váš Jade Plus.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Na obrazovce Jade Plus klikněte na nabídku "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

V zelené aplikaci vyberte své zařízení.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Potvrďte párovací kód na zařízení Jade Plus.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green vám nabízí test, který zajistí, že váš Nefrit je pravý. Klikněte na tlačítko a proveďte jej.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Potvrďte na Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Zelená barva potvrzuje, že zařízení je pravé.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Nastavení kódu PIN

Klikněte na tlačítko "*Pokračovat*" a zvolte PIN kód Jade.

![JADE-PLUS-GREEN](assets/fr/24.webp)

Kód PIN odemkne zařízení Jade. Je tedy ochranou proti neoprávněnému fyzickému přístupu. Tento PIN kód se nepodílí na odvození kryptografických klíčů vaší peněženky. Takže i bez přístupu k tomuto kódu PIN vám vlastnictví vaší 12slovné mnemotechnické fráze umožní znovu získat přístup k vašim bitcoinům. Doporučujeme zvolit co nejnáhodnější kód PIN. A nezapomeňte si tento kód uložit na jiné místo, než kde máte uložen svůj Nefrit (např. do správce hesel).

Zvolte šestimístný kód PIN na zařízení Jade a pomocí pravého a levého tlačítka procházejte číslicemi a prostředním tlačítkem potvrďte zadání číslice.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Potvrďte PIN podruhé.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Vaše bitcoinová peněženka byla vytvořena.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Vytvoření účtu Bitcoin

Nyní si musíte vytvořit účet v rámci svého portfolia. Klikněte na tlačítko "*Vytvořit účet*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Chcete-li vytvořit klasické portfolio s jedním signálem, vyberte možnost "*Standardní*".

![JADE-PLUS-GREEN](assets/fr/29.webp)

Další informace o možnosti "*2FA*" naleznete v tomto dalším návodu:

https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Váš účet byl vytvořen.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Pokud si chcete zelené portfolio přizpůsobit, klikněte na tři malé tečky vpravo nahoře.

![JADE-PLUS-GREEN](assets/fr/31.webp)

Možnost "*Přejmenovat*" umožňuje přizpůsobit název portfolia, což je užitečné zejména v případě, že v jedné aplikaci spravujete několik portfolií. Nabídka "*Jednotka*" umožňuje změnit základní jednotku vašeho portfolia. Můžete si například zvolit, že se má zobrazovat v satoších, a ne v bitcoinech. A konečně nabídka "*Parametry*" vám umožní přístup k dalším možnostem. Zde například najdete svůj rozšířený veřejný klíč a jeho deskriptor, což je užitečné, pokud plánujete nastavit peněženku pouze pro hodinky z vašeho Jade.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Chcete-li se po vypnutí zařízení Jade znovu připojit, stiskněte tlačítko zapnutí/vypnutí na spodní straně zařízení. V zelené aplikaci vyberte zařízení na domovské stránce:

![JADE-PLUS-GREEN](assets/fr/33.webp)

Poté zadejte kód PIN na zařízení Jade a budete opět připojeni.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Váš Jade je odemčen prostřednictvím "virtuálního bezpečného prvku" Blockstream (viz první část tohoto návodu). To vyžaduje připojení Bluetooth s aplikací Green. Pokud během odemykání narazíte na potíže s připojením Bluetooth, zkuste obě zařízení rozpojit a znovu spojit. Pokud problém přetrvává, můžete přesto odemknout svůj Jade výběrem možnosti "*QR Scan*" a podle pokynů dostupných [na webových stránkách Blockstream](https://jadefw.blockstream.com/pinqr/index.html).

Než obdržíte své první bitcoiny do peněženky, **důrazně doporučuji provést test obnovy prázdné peněženky**. Zaznamenejte si některé referenční informace, jako je vaše xpub nebo první přijímací adresa, a poté vymažte peněženku v aplikaci Green a v Jade Plus, dokud je ještě prázdná (`Možnosti -> Zařízení -> Obnovení továrního nastavení`). Poté zkuste peněženku obnovit pomocí papírových záloh mnemotechnické fráze. Zkontrolujte, zda se informace o souboru cookie vygenerované po obnovení shodují s těmi, které jste si původně zapsali. Pokud ano, můžete si být jisti, že vaše papírové zálohy jsou spolehlivé. Další informace o tom, jak provést zkušební obnovu, najdete v tomto dalším návodu :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Přijímání bitcoinů

Nyní, když je vaše peněženka Bitcoin nastavena, jste připraveni přijímat první saty! Jednoduše klikněte na tlačítko "*Přijmout*" v zelené aplikaci.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Zelená barva zobrazuje adresu recepce, ale před jejím použitím je nutné ji zkontrolovat na Nefritovém displeji a ověřit, že skutečně patří do našeho portfolia. To provedete kliknutím na tlačítko "*Ověřit na zařízení*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Zkontrolujte, zda je adresa na Nefritovém poli stejná jako na Zeleném poli, a poté kliknutím na tlačítko potvrďte.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Nyní můžete s plátcem sdílet adresu a získat bitcoiny do své peněženky. Jakmile bude transakce v síti odvysílána, objeví se ve vaší peněžence. Počkejte, až obdržíte dostatek potvrzení, abyste mohli transakci považovat za definitivní.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Odeslat bitcoiny

S bitcoiny v peněžence můžete nyní bitcoiny také posílat. Klikněte na "*Odeslat*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Na další stránce zadejte adresu příjemce. Můžete ji zadat ručně nebo naskenovat QR kód.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Zvolte výši platby.

![JADE-PLUS-GREEN](assets/fr/41.webp)

V dolní části obrazovky můžete vybrat sazbu poplatku pro tuto transakci. Máte na výběr, zda se budete řídit doporučeními aplikace, nebo si poplatky přizpůsobíte. Čím vyšší je poplatek v porovnání s ostatními nevyřízenými transakcemi, tím rychleji bude vaše transakce zpracována. Informace o trhu s poplatky naleznete na stránce [Mempool.space](https://mempool.space/) v sekci "*Poplatky za transakce*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Kliknutím na tlačítko "*Další*" přejděte na obrazovku se souhrnem transakcí. Zkontrolujte, zda jsou adresa, částka a poplatky správné.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Pokud vše proběhne v pořádku, posunutím zeleného tlačítka v dolní části obrazovky doprava transakci podepíšete a odešlete do sítě Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

Nyní budete vyzváni k potvrzení transakce na účtu Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Zkontrolujte, zda je adresa příjemce správná. Klikněte na zaškrtávací políčko a potvrďte.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Zkontrolujte, zda je částka poplatku správná, a poté ji potvrďte.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Vaše transakce byla podepsána a odvysílána ze Zelené.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Gratulujeme, nyní víte, jak nastavit a používat zařízení Jade Plus s mobilní aplikací Blockstream Green prostřednictvím připojení Bluetooth. Pokud pro vás byl tento návod užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji za sdílení!

Chcete-li se posunout o krok dál, doporučuji tento návod na Jade Plus, kde jej konfigurujeme pomocí softwaru Sparrow Wallet v režimu QR. Dozvíte se také, jak používat pokročilá nastavení hardwarové peněženky:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262



