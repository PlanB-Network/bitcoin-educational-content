---
name: Jade - Electrum
description: Jak používat Jade nebo Jade Plus s Electrum (stolní počítač)
---

![cover](assets/cover.webp)



_Tento návod je převzat z lekce [Bitcoin Workshops](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Výukový program je vytvořen v programu Jade Classic, ale operace jsou platné i pro uživatele programu Jade Plus.



Po inicializaci programu Jade jej můžete začít používat a vybrat si k tomu displej wallet.



Jade je zařízení, které lze používat s několika aplikacemi wallet nebo doprovodnými aplikacemi, jak je Blockstream uvádí na svých stránkách.



V tomto návodu se seznámíte s postupem používání Electrum Wallet prostřednictvím připojení kabelem USB.



## Přenos veřejného klíče



Vezměte a zapněte inicializované zařízení Jade. Jakmile jej zapnete, bude vypadat takto:




![img](assets/en/32.webp)



Pokud vyberete možnost _Unlock Jade_, zobrazí se nabídka, ve které je třeba vybrat způsob připojení zařízení k doprovodné aplikaci.



S Electrum můžete Jade připojit pouze přes USB, proto zvolte tuto metodu.



Spusťte program Electrum, který otevře nabídku jako výchozí možnost otevření posledního použitého programu wallet.



Pokud připojujete Jade ke službě Electrum poprvé, vyberte možnost _Create New Wallet_ a poté možnost _Finish_.



![img](assets/en/34.webp)



Název wallet.



![img](assets/en/35.webp)



Vyberte možnost Standard Wallet.



![img](assets/en/36.webp)



Při výběru úložiště klíčů je nutné vybrat možnost _Použít hardwarové zařízení_.



![img](assets/en/37.webp)



Electrum zahájí vyhledávání hardwarového zařízení.



![img](assets/en/38.webp)



Po připojení USB k počítači (již připojeného na straně USB C k Jade) se vám hardware wallet zobrazí v režimu uzamčení. Jade se odemkne vložením šestimístného kódu PIN nastaveného během nastavení.




![img](assets/en/39.webp)



Odemčené hardwarové zařízení, Electrum detekuje Jade. Pokračujte kliknutím na tlačítko _Další_.



![img](assets/en/40.webp)



V tomto okamžiku vás Electrum vyzve k nastavení skriptu zásad: vyberte _Nativní Segwit_.



![img](assets/en/41.webp)



Začíná fáze přenosu veřejného klíče z wallet z Jade na displej Electrum.



Po dokončení exportu veřejného klíče je proces ukončen.



Hlídání je připraveno a Electrum upozorňuje na dokončení následující obrazovkou.



![img](assets/en/42.webp)



wallet je skutečně vytvořen a vy jej můžete začít zkoumat: vidíte _adresy_, _informace o peněžence_ a - což je nejdůležitější - v pravém dolním rohu vidíte údaj, že se jedná o zařízení Blockstream. Zelená tečka vedle loga Blockstream znamená, že zařízení je zapnuté a správně připojené k místní síti.



![img](assets/en/43.webp)



## Přijímání a utrácení transakcí



V nabídce _Přijmout_ v modulu Electrum, generate zadejte `scriptPubKey` (adresu) pro příjem prostředků. Vždy začněte s malou částkou a proveďte test příjem+výdej.



![img](assets/en/44.webp)



Po obdržení satss můžete zkontrolovat jejich příchod v nabídce _Historie_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Jakmile je transakce potvrzena, můžete utratit tuto částku UTXO a dokončit test.



Výdaje jsou spojeny s používáním podpisu Jade.



Přejděte do nabídky _Odeslat_ programu Electrum, vložte skriptPubKey a dobře jej zkontrolujte.



![img](assets/en/47.webp)



Po dokončení stiskněte tlačítko _Pay_.



Otevře se okno transakce, ve kterém je důležité nastavit správné transakční poplatky. Po dokončení všech nastavení klikněte na _Preview_ v pravém dolním rohu.



![img](assets/en/48.webp)



Okno transakce zobrazuje některé důležité údaje, především stav: `Nepodepsáno`.



V této fázi se také zobrazí příkaz _Podepsat_, na který je třeba kliknout, abyste připojili podpis pomocí Jade.



![img](assets/en/49.webp)



Nyní začíná fáze komunikace mezi displejem wallet a hardwarovým zařízením, ve které vás Electrum upozorní, abyste se řídili pokyny na hardwarovém zařízení, které je zapnuté a připravené k podpisu.



![img](assets/en/50.webp)



**Nejdříve si však raději ověřte, co podepisujete: všechny parametry právě nastavené transakce se objeví také na Jade** a můžete si je všechny ověřit.



![img](assets/en/51.webp)



Chcete-li pokračovat, vždy umístěte kurzor na šipku `→`, která vede k dalším krokům, a nikdy na `X`, pokud nechcete operaci ukončit bez dokončení.



Ověřovací část končí zobrazením poplatku. V tomto okamžiku se potvrzení rovná vložení podpisu.



![img](assets/en/52.webp)



Jade na krátkou chvíli zpracuje operaci, po dokončení se vrátí do domovské nabídky.



![img](assets/en/53.webp)



Na obrazovce Electrum vidíte stav transakce, který se změnil z `Nepodepsané` na `Podepsané`, a nyní ji můžete propagovat kliknutím na tlačítko _Vysílání_.



![img](assets/en/54.webp)



Takto testovaný wallet může být použit pro příjem UTXO určeného k bezpečnému skladování.



![img](assets/en/55.webp)



Tento návod je příkladem použití hodinek Jade připojených přes USB k hodinkám wallet. Klasickým příkladem je Electrum, ale možná dáváte přednost jinému softwaru wallet. Jade exportuje veřejný klíč do mnoha dalších peněženek: najděte si podobné funkce, o kterých se dočtete v tomto návodu, abyste se jimi mohli řídit a zjistit, jak je využít vaše oblíbená aplikace companio.