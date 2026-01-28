---
name: Heritage
description: Portfolio Bitcoin s integrovaným mechanismem dědičnosti prostřednictvím skriptů Taproot
---

![cover](assets/cover.webp)



Předání bitcoinů v případě úmrtí nebo nezpůsobilosti představuje pro každého držitele kryptoaktiv velkou výzvu. Bez vhodného dědického plánu se tato aktiva stávají pro vaše blízké nedobytnými.



Společnost Heritage nabízí elegantní odpověď implementací mechanismu přepínání mrtvého muže přímo v blockchainu Bitcoin. Tento open-source wallet umožňuje konfigurovat podmínky nástupnictví po on-chain: pokud vlastník neprovede po definovanou dobu žádné další transakce, mohou předem určené alternativní klíče uvolnit finanční prostředky.



## Co je to dědictví?



Dědictví je portfolio Bitcoin nativně integrující mechanismus dědičnosti prostřednictvím skriptů Taproot. Tento open-source software vyvinutý pod licencí MIT Jérémie Rodonem zaručuje transparentnost a trvanlivost.



Heritage používá skripty Taproot zakódované v adresách Bitcoin. Každý UTXO v sobě integruje dva typy výdajových podmínek:





- Primární cesta** : Majitel může kdykoli utratit své bitcoiny pomocí svého primárního klíče
- Alternativní cesty**: Pro každého určeného dědice skript spojí jeho veřejný klíč s časovým zámkem



Každá transakce vlastníka automaticky odkládá datum aktivace dědických doložek. V případě delší nečinnosti (úmrtí, neschopnost) se podmínky automaticky aktivují.



## Památková péče (volitelně)



Společnost Heritage nabízí dvě možnosti použití:



**Vyrobte si to sami (zdarma)**: Pouze aplikace s otevřeným zdrojovým kódem. Vše spravujete samostatně pomocí vlastního uzlu. Tato možnost nabízí vestavěný přístup k zálohování, vestavěnou dědičnost a výhradní kontrolu nad vašimi bitcoiny. Musíte si však vytvořit vlastní upozornění (kalendář, upomínky), abyste nezapomněli obnovit své časové bloky, a neexistují žádná automatická oznámení pro vaše dědice.



**Využití služby (0,05 % ročně)** : Služba btc-heritage.com přidává funkce pro zjednodušení správy:




- Automatické připomenutí před vypršením lhůt
- Automatická oznámení dědicům, která je provedou procesem obnovy
- Prioritní podpora
- Zjednodušená správa deskriptorů



Poplatek: 0,05 % ze spravované částky ročně, minimálně 0,5 mBTC/rok. První rok zdarma.



Služba je i nadále neveřejná: vaše soukromé klíče nikdy neopustí vaše zařízení. Dědictví nemá přístup k vašim finančním prostředkům.



## Heritage CLI



Pokročilým uživatelům, kteří dávají přednost terminálu, nabízí společnost Heritage nástroj příkazového řádku (CLI) pro granulární ovládání a provoz stroje se vzduchovým uzávěrem.



![Page Heritage CLI](assets/fr/03.webp)



Úplná dokumentace ke CLI je k dispozici na adrese [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Zde najdete pokyny pro stažení, připojení ke službě, vytváření peněženek (s klíči Ledger nebo místními klíči), správu dědiců a transakcí.



Tento návod se zaměřuje na aplikaci Desktop, která je pro většinu uživatelů přístupnější.



## Heritage Desktop



Heritage Desktop je grafická aplikace s intuitivním rozhraním, které uživatele provede každým krokem procesu konfigurace.



### Stáhnout



Přejděte na stránku [btc-heritage.com](https://btc-heritage.com) a klikněte na "Download application".



![Page d'accueil Heritage](assets/fr/01.webp)



Vyberte verzi odpovídající vašemu operačnímu systému (Linux 64bits nebo Windows 64bits). Binární soubory nejsou digitálně podepsány, což může vyvolat bezpečnostní varování.



![Page de téléchargement](assets/fr/02.webp)



### Instalace v systému Linux



V systému Linux je aplikace distribuována ve formátu AppImage. Před jejím spuštěním je třeba nainstalovat závislost `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Poté vytvořte spustitelný soubor a spusťte jej:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### První spuštění



Při prvním spuštění vám průvodce nástupem nabídne tři možnosti:



![Onboarding initial](assets/fr/05.webp)





- Nastavení dědictví Wallet**: Vytvořit nový plán dědictví wallet
- Zdědění bitcoinů**: Získejte zpět bitcoiny jako dědic
- Prozkoumejte sami**: Prozkoumejte funkce bez pomoci



Výběrem možnosti "Nastavení dědictví Wallet" vytvoříte svůj první model wallet.



### Připojení k síti Bitcoin



Zvolte způsob připojení k síti Bitcoin:



![Choix connexion](assets/fr/06.webp)





- Používání služby Heritage Service**: Spravovaná infrastruktura, jednodušší pro dědice
- Používám vlastní uzel**: Připojení k vlastnímu uzlu Bitcoin Core nebo Electrum



V tomto tutoriálu použijeme vlastní uzel.



### Správa soukromých klíčů



Vyberte způsob správy soukromých klíčů:



![Gestion des clés](assets/fr/07.webp)





- S hardwarovým zařízením Ledger** : Maximální bezpečnost s hardwarovým zařízením wallet (doporučeno)
- Místní úložiště s heslem**: Místně uložené klíče s ochranou heslem
- Obnovení stávajícího zařízení wallet** : Obnovení ze stávajícího seed



### Konfigurace uzlu



Pokud používáte vlastní uzel, aplikace vás provede jeho konfigurací. Ujistěte se, že váš uzel Bitcoin nebo Electrum je :




- Nainstalováno a spuštěno
- Synchronizováno se sítí Bitcoin
- Nakonfigurováno na přijímání připojení RPC (pro Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Jakmile je váš uzel připraven, klikněte na "Můj uzel Bitcoin je spuštěn".



### Stavový panel



Kliknutím na "Status" v pravém horním rohu a poté na "Open Configuration" získáte přístup k parametrům připojení.



![Panneau Status](assets/fr/09.webp)



Nastavte adresu URL serveru Electrum (např. `umbrel.local:50001`, pokud používáte Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Vytvoření wallet



Po navázání spojení klikněte na kartě WALLETS na tlačítko "Create Wallet".



![Créer wallet](assets/fr/11.webp)



Vyskakovací okno vysvětluje rozdělenou architekturu služby Heritage :



![Architecture split](assets/fr/12.webp)



1. **Poskytovatel klíčů (offline)**: Spravuje vaše soukromé klíče a podepisuje transakce. Může to být software Ledger nebo wallet.


2. **Online Wallet**: Zpracovává synchronizaci se sítí Bitcoin, vytváření adres a vysílání transakcí.



Vyplňte formulář pro vytvoření :



![Formulaire création wallet](assets/fr/13.webp)





- Název Wallet**: Jedinečný název pro identifikaci vašeho wallet
- Klíčový poskytovatel**: Pro tento výukový program vyberte místní úložiště klíčů
- Nové/obnovené**: Výběrem možnosti "New" (Nový) vytvoříte nový generate
- Počet slov**: 24 slov pro maximální bezpečnost



Zadejte silné heslo a vyberte možnosti pro Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Místní uzel**: Používá vlastní uzel Electrum nebo Bitcoin Core
- Památková péče**: Používá službu Heritage (doporučeno pro oznamovací funkce)



Vytvoření dokončíte kliknutím na tlačítko "Create Wallet".



### Interface z wallet



Nyní je vytvořena vaše karta wallet. V rozhraní se zobrazí :



![Interface wallet](assets/fr/15.webp)





- Bilance
- Tlačítka SEND a RECEIVE
- Historie transakcí
- Historie konfigurace dědictví
- Adresy wallet



### Vytvoření dědiců



Přejděte na kartu "DĚDICOVÉ" a vytvořte dědice.



![Page Heirs](assets/fr/16.webp)



Vyskakovací okno s informacemi vysvětluje:




- Dědicové jsou veřejné klíče Bitcoin spojené s jednotlivci
- Každý dědic má svou vlastní mnemotechnickou frázi
- První dědic by měl být "záložní" pro vás (pro případ ztráty vašeho hlavního wallet)



#### Vytvoření záložního dědice



Klikněte na "Create Heir" a pojmenujte jej "Backup".



![Création héritier Backup](assets/fr/17.webp)



Vyskakovací okno vysvětluje, proč je věta o 12 slovech bez passphrase pro dědice bezpečná:


1. **Žádný okamžitý přístup**: Klíče dědiců nemají přístup k prostředkům, dokud nevyprší časový zámek


2. **Detekce kompromitace**: Pokud někdo získá přístup k frázi, můžete aktualizovat konfiguraci dědictví


3. **Dlouhodobá dostupnost**: passphrase by mohl být po mnoha letech zapomenut



Konfigurace dědice :



![Configuration héritier](assets/fr/18.webp)





- Klíčový poskytovatel** : Místní úložiště klíčů
- Novinka**: Vytvoření nového seed
- Počet slov**: 12 slov



Dokončení tvorby :



![Finalisation héritier](assets/fr/19.webp)





- Typ dědice**: Rozšířený veřejný klíč
- Export do služby**: Volitelné, umožňuje automatické oznámení dědicům



Nyní je vytvořen dědic Zálohování:



![Héritier créé](assets/fr/20.webp)



#### Uložení mnemotechnické fráze dědice



Klikněte na položku Backup heir a poté na položku "Show Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**DŮLEŽITÉ: Zapište si těchto 12 slov a uschovejte je na bezpečném místě. Je to klíč k získání finančních prostředků.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Odstranění seed z aplikace



Po zapsání fráze přejděte k parametrům dědice (ikona ozubeného kolečka):



![Paramètres héritier](assets/fr/23.webp)



K odstranění soukromého klíče z aplikace použijte příkaz "Strip Heir Seed". Potvrďte, že jste frázi uložili.



![Strip Heir Seed](assets/fr/24.webp)



Jedná se o bezpečnostní opatření: v aplikaci zůstává pouze veřejný klíč, který stačí ke konfiguraci dědičnosti.



#### Vytvoření druhého dědice



Zopakujte tento postup a vytvořte druhého dědice (např. "Satoshi"). Nyní budete mít dva dědice:



![Deux héritiers](assets/fr/25.webp)





- Záloha**: Váš osobní nouzový klíč
- Satoshi**: Určený dědic



### Konfigurace dědictví



Vraťte se do zařízení wallet a klikněte na ikonu Nastavení:



![Paramètres wallet](assets/fr/26.webp)



V části "Heritage Configuration" klikněte na tlačítko "Create":



![Heritage Configuration](assets/fr/27.webp)



Nastavte časové limity pro každého dědice:



![Configuration délais](assets/fr/28.webp)





- Záloha**: datum splatnosti: 2026-06-18
- Satoshi**: datum splatnosti: 2027-03-20



**Důležité**: Každý dědic musí mít delší zpoždění než ten předchozí. První dědic (záložní) bude mít k prostředkům přístup jako první.



Konfigurace také :



![Configuration finale](assets/fr/29.webp)





- Referenční datum**: Počáteční datum pro výpočet dodacích lhůt
- Minimální zpoždění splatnosti**: Minimální prodleva po transakci (doporučeno 10 dní)



Kliknutím na tlačítko "Vytvořit" ověřte konfiguraci.



Konfigurace Heritage je nyní aktivní:



![Configuration active](assets/fr/30.webp)



Zobrazuje oba dědice s jejich příslušnými lhůtami a daty platnosti.



### Ukládání deskriptorů



**Důležité**: Uložte si deskriptory wallet. Bez nich, a to i s mnemotechnickou frází, je obnova fondu nemožná.



Klikněte na položku "Záložní deskriptory" :



![Bouton Backup](assets/fr/31.webp)



Uložte soubor JSON obsahující deskriptory Bitcoin:



![Backup descripteurs](assets/fr/32.webp)



Tento soubor by měl být předán vašim dědicům spolu s příslušnými mnemotechnickými frázemi.



### Přijímání bitcoinů



Kliknutím na "RECEIVE" zadejte adresu příjmu generate:



![Recevoir bitcoins](assets/fr/33.webp)



Gratulujeme! Váš Heritage Wallet je připraven přijímat bitcoiny. Každá vygenerovaná adresa automaticky zahrnuje vaše podmínky Heritage.



Po přijetí transakce se aktualizuje váš zůstatek:



![Solde mis à jour](assets/fr/34.webp)



V historii se zobrazí transakce a související konfigurace dědictví.



---

## Vymáhání dědicem



Po uplynutí stanovené doby si dědic může prostředky vyzvednout.



### Předpoklady



Dědic potřebuje :


1. Jeho mnemotechnická fráze o 12 slovech


2. Původní záložní soubor deskriptoru wallet (JSON)



### Vytvoření dědice Wallet



Na kartě "DĚDICTVÍ" se zobrazí vyskakovací okno, které vám tyto předpoklady připomene:



![Page Heir Wallets](assets/fr/35.webp)



**Upozornění**: Bez záložního souboru deskriptoru je přístup k fondům NEMOŽNÝ, a to i se správnou mnemotechnickou frází.



Klikněte na "Vytvořit dědice Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Vyplňte prosím formulář:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Jméno dědice Wallet**: Jméno pro identifikaci tohoto dědice wallet
- Klíčový poskytovatel** : Místní úložiště klíčů
- Obnovení**: Tuto možnost vyberte, chcete-li zadat existující frázi



Zadejte 12 slov mnemotechnické fráze dědice a nakonfigurujte službu Heritage Provider:



![Entrée mnemonic](assets/fr/38.webp)





- Poskytovatel kulturního dědictví**: "Místní" pro použití vlastního uzlu se záložním souborem



Načtěte záložní soubor JSON a klikněte na "Create Heir Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Dědic Wallet



Je vytvořen dědic Wallet. Pokud časový zámek ještě nevypršel, není zpočátku dědictví k dispozici:



![Pas d'héritage disponible](assets/fr/40.webp)



Po uplynutí prodlevy a synchronizaci prostředků se sítí Bitcoin se objeví v seznamu dědictví:



![Héritage disponible](assets/fr/41.webp)



V rozhraní se zobrazí :




- Typ klíče a otisk prstu
- Dědičné fondy celkem
- Aktuální částka, kterou lze utratit (0 sedí, pokud časový zámek ještě nevypršel)
- Data splatnosti a vypršení platnosti



Po dosažení data splatnosti převedete bitcoiny tlačítkem "Spend" na osobní účet wallet.



---

## Osvědčené postupy



### Ukládání deskriptorů



Deskriptory wallet jsou nezbytné pro rekonstrukci adres dědictví. **Bez deskriptorů nebudete schopni najít své fondy ani s pomocí mnemotechnické fráze.



### Zabezpečení klíčů





- Pokud je to možné, použijte pro hlavní klíč model Ledger
- Nikdy neukládejte věty dědiců na stejné místo jako své vlastní
- Šíření informací ve více médiích a na různých místech



### Dokumentace pro vaše blízké



Napište jasné pokyny vysvětlující jednotlivé kroky procesu obnovy. Vaši dědicové nemusí být v kritickém okamžiku obeznámeni se systémem Bitcoin.



## Alternativy



Existují i další řešení pro správu přenosu vašich bitcoinů, včetně Liana a Bitcoin Keeper. Níže najdete naše návody:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Závěr



Aplikace Heritage umožňuje suverénně plánovat nástupnictví po Bitcoin prostřednictvím aplikace Desktop. Realizace vyžaduje promyšlené zvážení vhodných časových rámců a zajištění tajemství. Nezapomeňte na předání dědicům:




- Jejich mnemotechnická fráze o 12 slovech
- Záložní soubor deskriptoru
- Pokyny pro obnovu



## Zdroje





- [oficiální webové stránky dědictví](https://btc-heritage.com)
- [Dokumentace CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)