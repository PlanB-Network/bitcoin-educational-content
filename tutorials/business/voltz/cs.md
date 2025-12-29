---
name: Voltz
description: Univerzální blesk wallet pro vaši firmu.
---

![cover](assets/cover.webp)



S nápadem na vytvoření platformy Voltz přišla skupina bitcoinerů, kteří chtěli poskytovat vlastní bitcoinovou službu wallet. Výsledkem byla kompletní infrastruktura pro přijímání bitcoinů v maloobchodě. V tomto tutoriálu vás provedeme platformou Voltz a možnostmi integrace bitcoinů, které platforma nabízí.



## Začínáme s Voltzem



Kromě toho, že je Voltz správcovskou službou Lightning wallet, která umožňuje denně odesílat, přijímat a platit, je to kompletní platforma, která poskytuje četná rozšíření pro integraci bitcoinu jako prodejního místa nebo tržiště ve vašem podnikání.



Přejděte na platformu [Voltz] (https://www.voltz.com/en) a vytvořte si účet kliknutím na tlačítko "Try now".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Je důležité nastavit silné alfanumerické heslo, abyste zvýšili své šance proti útokům hrubou silou, a zkontrolovat, zda jste skutečně na oficiálních webových stránkách Voltz, kde vyplníte své přihlašovací údaje, abyste se chránili před phishingem.



Rozhraní Voltz je velmi podobné rozhraní platformy LnBits.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz je ve skutečnosti postaven na serveru LnBits; podívejte se na náš návod, jak připojit vlastní servery LnBits a vytvořit na nich vlastní řešení.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Platforma umožňuje efektivně spravovat více portfolií. Ve výchozím nastavení, když se zaregistrujete, máte automaticky portfolio Lightning. Můžete však přidat další portfolia.



![wallets](assets/fr/03.webp)



### Přenositelnost



Voltz se neomezuje pouze na webové rozhraní: v sekci **Mobilní přístup** můžete připojit aktivní Voltz wallet k aplikacím, jako je Zeus nebo Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

K tomu je třeba nainstalovat a aktivovat rozšíření **LndHub** na platformě.



![lndhub](assets/fr/04.webp)



Vyberte své aktivní portfolio Voltz a v závislosti na právech, která chcete udělit, naskenujte příslušný QR kód.




- Kód QR faktury umožňuje pouze číst historii portfolia a generate nových faktur.
- Správce QR kódu umožňuje zobrazit historii, faktury generate a také zaplatit faktury Lightning.



![qrs](assets/fr/05.webp)



V tomto návodu připojíme náš Voltz wallet k aplikaci Blue Wallet.



![connect](assets/fr/06.webp)



Po propojení našeho portfolia budou všechny provedené akce synchronizovány mezi společnostmi Blue Wallet a Voltz. Například když v systému Blue Wallet vystavíte fakturu generate, budete mít historii i v systému Voltz.



![sync](assets/fr/07.webp)



V části **Konfigurace portfolia** najdete minimální parametry, jako je přizpůsobení názvu portfolia a měna, ve které chcete přijímat platby.



![config](assets/fr/08.webp)



### Rozšíření



Jednou ze zvláštností platformy Voltz je její modularita, která umožňuje aktivovat potřebná rozšíření. Seznam rozšíření naleznete v nabídce **Rozšíření**.



![extensions](assets/fr/09.webp)



Mezi tato rozšíření patří TPoS, terminál pro prodejní místa, který můžete používat k evidenci zásob a vybírání plateb od zákazníků.



![tpos](assets/fr/10.webp)



Na terminálu prodejního místa můžete :




- Získejte webovou stránku, kterou můžete sdílet se svými zákazníky a partnery;
- Správa zásob produktů;
- Generování faktur Lightning;
- Platby v hotovosti prostřednictvím karet Bolt.



Rozšíření je k dispozici ve verzi zdarma a v placené verzi pro pokročilejší funkce. Chcete-li vytvořit pokladní terminál, klikněte na tlačítko **Otevřít** pod logem rozšíření a poté na **Nový pokladní terminál**.



![new_tpos](assets/fr/11.webp)



Definujte název svého prodejního místa a poté připojte Voltz wallet k terminálu pro výběr plateb. Spropitné můžete aktivovat zaškrtnutím políčka **Aktivovat spropitné**. Aktivujte také možnost tisku faktur, pokud chcete zákazníkům vystavovat účtenky (tato funkce je stále ve vývoji, takže může docházet k poruchám).



Terminál pro prodejní místa zahrnuje také konfiguraci daní, pokud chcete na své produkty přímo aplikovat daň platnou ve vaší zemi.



![tpos](assets/fr/12.webp)



Po vytvoření pokladního terminálu můžete přidat předkonfigurované produkty a služby, které vám a vašim zákazníkům zajistí bezproblémové placení a účtování.



![product](assets/fr/13.webp)



Vytvořte své produkty definováním jejich názvu, přidáním obrázku a nastavením prodejní ceny.  Pro snadnější sledování můžete své produkty zařadit do kategorií. Daně můžete uplatnit přímo na konkrétní produkt. Pokud produkt nemá uplatněnou žádnou daň, automaticky se uplatní daň nakonfigurovaná ve fázi vytvoření prodejního terminálu.



![products](assets/fr/14.webp)



Seznam produktů můžete automaticky importovat z formátu JSON kliknutím na tlačítko **Import/Export**.



![exports](assets/fr/15.webp)



K pokladní zóně se dostanete přes odkaz kliknutím na ikonu **Nová karta**, nebo můžete sdílet pokladní platformu prostřednictvím QR kódu se svými zákazníky kliknutím na ikonu **QR kód**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Vaši zákazníci si mohou prohlédnout váš katalog a provést platbu z tohoto rozhraní.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



Ve skupině dostupných rozšíření najdete také nástroje, jako jsou rozšíření **Invoice** a **Payment Link**, které umožňují vystavovat faktury generate s konkrétními produkty a vybírat izolované platby bez nutnosti procházet terminálem POS.



## Sledujte své platby



V nabídce **Platby** vám Voltz nabízí přehled plateb do různých portfolií.


Své platby můžete sledovat pomocí :




- Stav.
- Označení: například **TPOS** pro platby v místě prodeje a **lnhub** prostřednictvím mobilního připojení v peněženkách Zeus a Blue Wallet.
- Portfolio sbírky.
- Celkové příchozí a odchozí platby.
- Dobře vymezené období.



![payments](assets/fr/22.webp)



## Další možnosti



Voltz je také infrastruktura, na které můžete postavit vlastní řešení. V části **Rozšíření** najdete průvodce vývojem vlastních rozšíření v rámci ekosystému Voltz a LnBits.



![build](assets/fr/23.webp)



V případě, že chcete vyvíjet řešení mimo ekosystém, ale přesto používat jeho infrastrukturu, najdete v části **URL uzlu** klíče API a informace o dokumentaci s příkladem, co můžete s těmito daty dělat.



Můžete vytvářet faktury Lightning ze svých aplikací pomocí Voltz wallet, platit faktury Lightning, dekódovat a ověřovat faktury.



![keys](assets/fr/24.webp)



Nyní již Voltzovi dobře rozumíte. Pokud se vám tento návod líbil, jsme si jisti, že se v našem kurzu dozvíte více o nejlepších metodách a nástrojích pro integraci bitcoinu do vašeho podnikání: Bitcoin pro firmy.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a