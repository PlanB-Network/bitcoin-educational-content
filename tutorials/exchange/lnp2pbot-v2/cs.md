---
name: LNP2PBot
description: Kompletní průvodce LNP2PBot a P2P obchodování s bitcoiny
---
![cover](assets/cover.webp)

## Úvod

Pro zachování důvěrnosti a finanční nezávislosti uživatelů jsou zásadní výměnné burzy P2P (peer-to-peer) bez nutnosti KYC. Umožňují přímé transakce mezi jednotlivci bez nutnosti ověřování totožnosti, což je zásadní pro ty, kteří si cení soukromí. Chcete-li teoretickým konceptům porozumět hlouběji, podívejte se na kurz BTC204:

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Nákup a prodej bitcoinů peer-to-peer (P2P) je jedním z nejprivátnějších způsobů získávání bitcoinů nebo nakládání s nimi. LNP2PBot je open source bot pro Telegram, který usnadňuje P2P výměny v síti Lightning a umožňuje rychlé, levné transakce bez KYC.

### Proč používat Lnp2pbot?


- KYC není vyžadováno
- Rychlé transakce v síti Lightning Network
- Nízké náklady
- Jednoduché rozhraní přes Telegram, populární aplikaci pro zasílání zpráv dostupnou odkudkoli na světě
- Integrovaný systém reputace
- Automatická úschova pro bezpečné obchodování
- Podpora více měn
- Aktivní a rostoucí komunita

### Předpoklady

Chcete-li používat Lnp2pbot, budete potřebovat :

1. Peněženka Lightning Network (doporučujeme Breez, Phoenix nebo Blixt)

2. Nainstalovaná aplikace Telegram (https://telegram.org/)

3. Účet Telegram s definovaným uživatelským jménem

## Instalace a konfigurace

### 1. Konfigurace peněženky Lightning

Začněte instalací kompatibilní peněženky Lightning. Zde jsou naše podrobná doporučení:

**Doporučená portfolia**


- [Breez](https://breez.technology):
  - Vynikající pro začátečníky
  - Intuitivní a moderní rozhraní
  - Bez svěřenectví (zachováte si kontrolu nad svými prostředky)
  - Perfektně kompatibilní s Lnp2pbot
  - K dispozici pro iOS a Android

Níže naleznete odkaz na výukový program pro tuto peněženku:

https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co) :
  - Jednoduché a spolehlivé
  - Automatická konfigurace kanálů
  - Nativní podpora faktur BOLT11
  - Vynikající pro každodenní transakce
  - K dispozici pro iOS a Android

Níže naleznete odkaz na výukový program pro tuto peněženku:

https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io) :
  - Techničtější, ale velmi kompletní
  - Rozšířené možnosti konfigurace
  - Ideální pro zkušené uživatele
  - Otevřený zdroj
  - K dispozici pro Android

Níže naleznete odkaz na výukový program pro tuto peněženku:

https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Důležité poznámky k ostatním portfoliím**

⚠️ **Důležité**: Před prodejem satelitů se ujistěte, že vaše portfolio podporuje faktury "hold", které bot používá jako systém úschovy.


- **Peněženka Satoshi**: Funguje dobře pro příjem sats, ale může mít zpoždění při aktualizaci zůstatku, pokud je prodej zrušen.
- **Muun**: Nedoporučuje se, protože platby mohou selhat kvůli limitům poplatků za směrování botů (maximálně 0,2 %).
- **Aqua**: V případě zrušení prodeje může dojít k dlouhému zpoždění (až 48 hodin) aktualizace zůstatku.

💡 **Tip**: Pro optimální zážitek si vyberte doporučená portfolia (Breez, Phoenix nebo Blixt).

⚠️ **Důležité**: Nezapomeňte si fráze pro obnovení uložit na bezpečné místo.

### 2. Začínáme s Lnp2pbotem

1. Kliknutím na tento odkaz získáte přístup k botovi: [@lnp2pBot](https://t.me/lnp2pbot)

2. Telegram se otevře automaticky

3. Klikněte na "Start" nebo odešlete příkaz "/start"

4. Bot vás požádá o vytvoření uživatelského jména, pokud ještě žádné nemáte

5. Bot vás provede počáteční konfigurací

### 3. Připojte se ke komunitě


- Připojte se k hlavnímu kanálu: [@p2plightning](https://t.me/p2plightning)
- Podpora: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)

## Nákup a prodej bitcoinů

Na Lnp2pbot jsou dva hlavní způsoby výměny bitcoinů:

1. Procházet stávající nabídky na trhu a reagovat na ně

2. Vytvořte si vlastní nabídku na koupi nebo prodej

V této příručce se podrobně podíváme na to, jak :


- Koupit bitcoiny ze stávající nabídky
- Prodej bitcoinů vytvořením vlastní nabídky

### Jak koupit Bitcoiny

**1. Vyhledání a výběr nabídky**

![Sélection d'une offre de vente](assets/fr/01.webp)

Prohlédněte si nabídky v [@p2plightning](https://t.me/p2plightning) a klikněte na tlačítko "Koupit satoshis" pod inzerátem, který vás zajímá.

**2. Ověřte nabídku a částku**

![Validation de l'offre](assets/fr/02.webp)

1. Návrat do chatu s botem

2. Potvrzení výběru nabídky

3. Zadejte částku ve fiat měně, kterou chcete koupit

4. Bot vás požádá o vystavení faktury Lightning na částku v satoších

**3. Kontaktujte prodávajícího**

![Mise en relation](assets/fr/03.webp)

Po odeslání faktury vás bot spojí s prodejcem.

**4. Komunikace s prodávajícím**

![Chat privé](assets/fr/04.webp)

Kliknutím na přezdívku prodávajícího otevřete soukromý chatovací kanál, kde si můžete vyměnit údaje o platbě fiat.

**5. Potvrzení o platbě**

![Confirmation du paiement](assets/fr/05.webp)

Po provedení platby fiat použijte v chatu bota příkaz `/fiatsent`. Po dokončení transakce budete moci prodejce ohodnotit a transakce bude uzavřena.

### Jak prodávat Bitcoiny

**1. Vytvoření prodejní nabídky**

![Création d'une offre de vente](assets/fr/06.webp)

Chcete-li vytvořit prodejní nabídku, jednoduše použijte příkaz :

`/prodej`

Bot vás pak povede krok za krokem:

1. Zvolte si měnu

2. Uveďte množství satošů, které chcete prodat

3. Za tuto cenu máte dvě možnosti:


   - Nastavení pevné ceny za množství satošů
   - Použijte tržní cenu s možností uplatnění přirážky (kladné nebo záporné)

💡 **Tip**: Prémie vám umožní upravit cenu ve vztahu k tržní ceně. Například přirážka -1 % znamená, že prodáváte za cenu o 1 % nižší, než je tržní cena.

**2. Potvrzení o vytvoření objednávky**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Po vytvoření objednávky se zobrazí potvrzení s možností zrušit objednávku pomocí příkazu `/cancel`.

**3. Řízení prodeje**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- Když kupující na vaši nabídku zareaguje, obdržíte oznámení s QR kódem a fakturou k zaplacení.
- Zkontrolujte profil a pověst kupujícího.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Kliknutím na přezdívku kupujícího otevřete soukromý diskusní kanál.
- Sdělte kupujícímu údaje o platbě fiat.
- Vyčkejte na potvrzení platby fiat od kupujícího.
- Zkontrolujte, zda byla na váš účet přijata platba.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Potvrďte transakci pomocí `/release` a dokončete objednávku. Budete mít možnost ohodnotit kupujícího.

## Správné postupy a bezpečnost

### Bezpečnostní tipy


- Začněte s malým množstvím
- Vždy kontrolujte pověst uživatelů
- Používejte pouze navrhované způsoby platby
- Veškerá komunikace probíhá v chatu botů
- Nikdy nesdílejte citlivé informace

### Systém reputace


- Každý uživatel má skóre reputace
- Úspěšné transakce zvyšují vaše skóre
- Vyberte si uživatele s dobrou pověstí
- Nahlásit moderátorům jakékoli podezřelé chování

### Řešení sporů

1. Když se vyskytnou problémy, zachovejte klid a profesionální přístup

2. K otevření tiketu použijte příkaz `/dispute`

3. Poskytněte všechny potřebné důkazy

4. Počkejte na moderátora

## Srovnání s jinými řešeními

Lnp2pbot má několik výhod a nevýhod oproti jiným P2P výměnným řešením, jako jsou Peach, Bisq, HodlHodl a Robosat:

### Výhody Lnp2pbot


- **KYC není vyžadováno**: Na rozdíl od některých platforem Lnp2pbot nevyžaduje ověření totožnosti, čímž zachovává důvěrnost uživatelů.
- **Rychlé transakce**: Díky síti Lightning jsou transakce téměř okamžité.
- **Nízké poplatky**: Transakční náklady jsou nižší než u tradičních burz.
- **Mobilní dostupnost**: LNP2PBot je dostupný přes Telegram, což usnadňuje jeho používání na mobilních zařízeních.
- **Snadné použití**: Intuitivní rozhraní Lnp2pbot usnadňuje používání i méně zkušeným uživatelům.

### Nevýhody Lnp2pbot


- **Závislost na Telegramu**: Používání Lnp2pbot vyžaduje účet Telegram, což nemusí být vhodné pro všechny uživatele.
- **Menší likvidita**: V porovnání se zavedenými platformami, jako je Bisq, může být likvidita omezenější.

Oproti tomu řešení, jako je Bisq, nabízejí vyšší likviditu a rozhraní pro stolní počítače, ale mohou zahrnovat vyšší poplatky a delší dobu transakce. HodlHodl a Robosat mezitím také nabízejí obchodování bez KYC, ale s odlišnou strukturou poplatků a rozhraním.

## Užitečné zdroje


- Oficiální webové stránky: https://lnp2pbot.com/
- Dokumentace: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Podpora: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)