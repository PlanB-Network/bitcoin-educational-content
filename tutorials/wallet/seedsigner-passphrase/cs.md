---
name: BIP-39 Passphrase SeedSigner
description: Jak mohu přidat passphrase do svého portfolia SeedSigner?
---

![cover](assets/cover.webp)



passphrase BIP39 je volitelné heslo, které v kombinaci s mnemotechnickou frází poskytuje další vrstvu zabezpečení pro deterministické a hierarchické peněženky Bitcoin. V tomto návodu společně zjistíme, jak nastavit passphrase na Bitcoin wallet používaném se SeedSignerem.



![Image](assets/fr/01.webp)



## Předpoklady před přidáním přístupové fráze



Pokud nejste obeznámeni s konceptem passphrase, jeho fungováním a důsledky pro váš Bitcoin wallet, před zahájením tohoto návodu vám důrazně doporučuji prostudovat tento další teoretický článek, kde vše vysvětluji (je to velmi důležité, protože používání passphrase bez plného pochopení jeho fungování může ohrozit vaše bitcoiny) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Před zahájením tohoto návodu se také ujistěte, že jste již inicializovali svůj SeedSigner a vygenerovali mnemotechnickou frázi. Pokud jste tak neučinili a váš SeedSigner je zcela nový, postupujte podle návodu na stránkách Plan ₿ Academy. Po dokončení tohoto kroku se můžete vrátit k tomuto návodu:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Jak do SeedSigneru přidám kód passphrase?



Přidáním účtu passphrase do portfolia spravovaného prostřednictvím SeedSigner se vytvoří zcela nové portfolio a vygeneruje se zcela samostatná sada klíčů. Pokud tedy již máte portfolio obsahující saty, nebudete k němu mít pomocí passphrase přístup, protože se vygeneruje zcela jiné portfolio.



Chcete-li na svůj SeedSigner použít kód passphrase, zapněte zařízení a naskenujte SeedQR jako obvykle. Poté SeedSigner zobrazí otisk vašeho aktuálního wallet, který odpovídá otisku **bez passphrase**. wallet s passphrase bude mít jiný otisk prstu.



Klikněte na tlačítko `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Poté zadejte vybraný kód passphrase do příslušného pole pomocí klávesnice na obrazovce. Nezapomeňte si vytvořit jednu nebo více fyzických záloh (papírových nebo kovových): ztráta tohoto passphrase bude mít za následek trvalou ztrátu přístupu k vašim bitcoinům. **Pro obnovení wallet je nezbytné zadat jak mnemotechnickou pomůcku, tak passphrase. ** Pokud dojde ke ztrátě jedné z nich, budou vaše bitcoiny nenávratně zablokovány.



Jakmile dokončíte zadání, potvrďte je stisknutím tlačítka `KEY3` v pravém dolním rohu SeedSigneru.



![Image](assets/fr/03.webp)



*V tomto příkladu jsem použil příkaz passphrase `pba`. Ve vašem případě se však ujistěte, že jste zvolili robustní passphrase. Chcete-li zjistit, jak definovat optimální passphrase, přečtěte si tento další článek:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Poté SeedSigner zobrazí nový otisk vašeho passphrase wallet. Vytvořte si několik kopií tohoto otisku prstu: je důležitý při používání wallet s passphrase, protože umožňuje při každém zadání passphrase zkontrolovat, zda jste neudělali žádnou chybu při zadávání a zda přistupujete ke správnému wallet.



Pokud například v mém případě při spuštění SeedSigner omylem napíšu passphrase `Pba` místo `pba`, povede tato jednoduchá změna z malých písmen na velká k vytvoření zcela jiného portfolia, než ke kterému chci přistupovat.



Tento otisk prstu nepředstavuje žádné riziko pro bezpečnost nebo důvěrnost vašeho účtu wallet. Neprozrazuje žádné veřejné ani soukromé informace o vašich klíčích. Na rozdíl od mnemotechniky a passphrase tedy můžete otisk prstu uložit na digitální médium. Doporučuji uchovávat kopii na několika místech: na papíře, ve správci hesel atd.



Po uložení otisku prstu klikněte na tlačítko `Done`.



![Image](assets/fr/04.webp)



Poté máte přístup ke všem funkcím svého portfolia stejně jako v klasickém SeedSigneru.



![Image](assets/fr/05.webp)



Nyní můžete importovat úložiště klíčů do Sparrow Wallet a normálně používat svůj wallet. Při každém restartu budete muset jak naskenovat svůj SeedQR, tak znovu zadat svůj passphrase pomocí klávesnice, jak jsme to udělali zde.



Než začnete wallet s passphrase skutečně používat, důrazně doporučuji provést test obnovy úplně prázdného zařízení. Ten vám umožní potvrdit, že vaše zálohy mnemotechnické fráze a passphrase jsou platné. Jak tuto kontrolu provést, se dozvíte v následujícím návodu:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895