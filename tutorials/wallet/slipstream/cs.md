---
name: Slipstream
description: Odeslání podepsané transakce přímo těžaři pomocí nástroje Slipstream, bez jejího vysílání do sítě Bitcoin
---

![cover](assets/cover.webp)

Když podepíšete transakci, je za normálních okolností automaticky rozeslána všem uzlům Bitcoinu v síti. Poté čeká na vytěžení.

Dokud však není v bloku, může ji útočník, který získal váš soukromý klíč, nahradit a prostředky ukrást. To je typicky případ, kdy používáte hardwarovou peněženku ColdCard.

Nástroj Slipstream od těžařské společnosti MARA umožňuje obejít vysílání transakce do sítě: je odeslána přímo (a pouze) jednomu těžaři, což ji uchová v soukromí a zabrání jejímu vystavení v síti. Vytěžení transakce bude pravděpodobně trvat déle, ale bude chráněna před útokem nahrazením.

Níže nabízíme návod, který uživatelům peněženky [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) i uživatelům peněženky [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) umožňuje používat nástroj Slipstream těžaře MARA prostřednictvím stránky [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Upozornění**: tento nástroj je určen pouze pro určité profily, především pro peněženky Liana, miniscriptové peněženky a některé typy multisigu. Wizardsardine **výslovně nedoporučuje** jeho použití u peněženek, jejichž prostředky jsou již vystaveny kritickému riziku krádeže, například u těch, jejichž obnovovací fráze byla vygenerována na zařízení ColdCard postiženém zranitelností generátoru náhodných čísel. V takové situaci jde v závodě s útočníkem o vteřiny a transakce odeslaná jedinému těžaři se potvrzuje mnohem déle než transakce běžně rozeslaná do sítě. Pokud se vás to týká, přečtěte si nejprve náš samostatný návod:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Pro uživatele peněženky Liana

Lianu spravuje Wizardsardine, provozovatel stránky [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), takže cesta je přímá: jednoduše exportujete podepsaný soubor PSBT místo toho, abyste transakci rozeslali do sítě.

*Podmínka: mít prostředky na své peněžence Liana.*

### Krok 1: Vytvořte transakci v Lianě

Jako obvykle sestavte transakci zadáním cílové adresy, popisu a částky (zde maximum dostupné v peněžence).

Nastavení sazby poplatků:

- vyberte mince, které chcete utratit, kliknutím na malé pole vlevo dole, pod "Coins selection";
- poté zadejte sazbu poplatků. Nezapomeňte nastavit poplatky mnohem vyšší, než je doporučovaná sazba, jak je popsáno na této stránce: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Nakonec klikněte na "Next".

![Sestavení transakce v Lianě](assets/fr/01.webp)

### Krok 2: Zkontrolujte podrobnosti transakce

Než kliknete na "Sign", zkontrolujte podrobnosti své transakce, zejména:

- odesílanou částku;
- počet satoshi vyhrazených na transakční poplatky;
- ale především adresu, na kterou prostředky posíláte (nezapomeňte zkontrolovat prvních 5/6 znaků, posledních 5/6 znaků a 5/6 znaků uprostřed adresy, abyste se vyhnuli útokům typu "address poisoning").

![Kontrola podrobností transakce](assets/fr/02.webp)

### Krok 3: Vyberte podepisující peněženky

Dále vyberte softwarové a/nebo hardwarové peněženky, kterými potřebujete transakci podepsat. Malá připomínka: v případě multisigové peněženky 2 z 2 potřebujete 2 podpisy ze 2.

### Krok 4: Exportujte soubor PSBT své transakce

Bitcoinová transakce je nyní podepsána příslušnými klíči. Neklikejte na "Broadcast", jinak bude sdílena s celou sítí a v případě, že používáte hardwarovou peněženku ColdCard, bude vaše transakce veřejně vystavena a vaše prostředky budou ohroženy.

Nyní můžete kliknout na "Export" a uložit soubor PSBT lokálně do svého počítače.

![Export souboru PSBT z Liany](assets/fr/03.webp)

### Krok 5: Odešlete transakci těžaři přes outofband.wizardsardine.com

Nyní k posledním krokům. Chcete-li transakci odeslat těžaři, stačí vzít soubor PSBT a přetáhnout jej do vyznačené oblasti.

![Přetažení souboru PSBT na outofband.wizardsardine.com](assets/fr/04.webp)

Transakce se poté zobrazí tak, jak je vidět níže.

![Transakce ve frontě](assets/fr/05.webp)

### Krok 6: Odešlete transakci přes Slipstream

Nakonec stačí kliknout na "Send", aby byla transakce odeslána společnosti MARA přes Slipstream.

![Odeslání transakce přes Slipstream](assets/fr/06.webp)

Během několika sekund se stav transakce změní ze "Sending" na "Accepted":

![Transakce přijatá Slipstreamem](assets/fr/07.webp)

Zbývá už jen zkopírovat identifikátor transakce (TXID) a vložit jej do [mempool.space](https://mempool.space/), abyste mohli sledovat její vytěžení:

![Vyhledání TXID na mempool.space](assets/fr/08.webp)

Vezměte prosím na vědomí: transakce se bude zobrazovat jako "Transaction not found", dokud těžař MARA nevytěží blok a nezahrne do něj vaši transakci. To může trvat několik desítek minut, ba i hodin, protože MARA drží jen zhruba 4,5 % hashrate sítě Bitcoin. K 4. srpnu 2026 to odpovídá přibližně jednomu vytěženému bloku každé 3 hodiny a 45 minut.

## Pro uživatele jiných peněženek

Pokud nepoužíváte [Lianu](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), ale přesto chcete tento nástroj využít, zde je návod využívající multisigovou peněženku 2 z 2. Použijeme k tomu softwarovou peněženku [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Podmínka: mít prostředky na své peněžence Sparrow.*

### Krok 1: Vytvořte transakci

V [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) vytvořte transakci na své multisigové peněžence. Nezapomeňte nastavit poplatky mnohem vyšší, než je doporučovaná sazba, jak je popsáno na této stránce: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Po vytvoření klikněte na "Create Transaction".

![Vytvoření transakce ve Sparrow](assets/fr/09.webp)

### Krok 2: Dokončete transakci

Abyste transakci dokončili, musíte ji nyní podepsat. Klikněte za tímto účelem na "Finalize Transaction for Signing".

![Dokončení transakce pro podpis](assets/fr/10.webp)

### Krok 3: Podepište transakci svými jednotlivými klíči

Nyní přichází čas transakci podepsat. Stačí ji podepsat softwarovou nebo hardwarovou peněženkou (či peněženkami), které používáte.

![Podepsání transakce klíči multisigu](assets/fr/11.webp)

### Krok 4: Stáhněte podepsanou transakci a nerozesílejte ji do sítě

Bitcoinová transakce je nyní podepsána oběma klíči našeho multisigu 2 z 2. Neklikejte na "Broadcast Transaction", jinak bude sdílena s celou sítí a v případě, že používáte hardwarovou peněženku ColdCard, bude vaše transakce veřejně vystavena a vaše prostředky budou ohroženy.

![Podepsaná transakce, připravená, ale nerozeslaná](assets/fr/12.webp)

### Krok 5: Zobrazte skript podepsané transakce nebo stáhněte soubor PSBT

Chcete-li zobrazit podepsanou bitcoinovou transakci, klikněte nyní na "View Final Transaction". Poté můžete zkopírovat skript podepsané bitcoinové transakce:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Zobrazení skriptu podepsané transakce](assets/fr/13.webp)

Pokud si chcete soubor transakce stáhnout, můžete buď:

- kliknout na "File" a poté na "Save transaction…";
- nebo kliknout na tlačítko síťového připojení vpravo dole (žluté tlačítko) a poté kliknout na "Save Final Transaction".

Transakce se pak uloží lokálně do vašeho počítače.

![Lokální uložení finální transakce](assets/fr/14.webp)

### Krok 6: Odešlete transakci těžaři přes outofband.wizardsardine.com

Nyní k posledním krokům. Chcete-li transakci odeslat těžaři, stačí:

- přejít na [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- vložit skript podepsané transakce zkopírovaný v předchozím kroku a poté kliknout níže na "ADD TO QUEUE";

![Vložení skriptu transakce do nástroje](assets/fr/15.webp)

- nebo vzít soubor a přetáhnout jej do vyznačené oblasti.

![Přetažení souboru transakce na nástroj](assets/fr/16.webp)

Transakce se poté zobrazí tak, jak je vidět níže.

![Transakce ve frontě](assets/fr/17.webp)

Pokud vás zpráva upozorní, že celková vstupní částka satoshi ve vaší transakci není známa (a že v důsledku toho nelze vypočítat počet satoshi na poplatky), stačí celkovou vstupní částku satoshi zadat ručně. Najdete ji tak, že ve Sparrow kliknete na zobrazení své transakce, doprostřed diagramu:

![Celková vstupní částka zobrazená ve Sparrow](assets/fr/18.webp)

Poté tuto částku (v našem příkladu 15 904 satů) zadejte do nástroje [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Ruční zadání celkové vstupní částky](assets/fr/19.webp)

Nakonec zkontrolujte, že je sazba poplatků správná.

### Krok 7: Odešlete transakci přes Slipstream

Nakonec stačí kliknout na "Send", aby byla transakce odeslána společnosti MARA přes Slipstream.

![Odeslání transakce přes Slipstream](assets/fr/20.webp)

Během několika sekund se stav transakce změní ze "Sending" na "Accepted":

![Transakce přijatá Slipstreamem](assets/fr/21.webp)

Zbývá už jen zkopírovat identifikátor transakce (TXID) a vložit jej do [mempool.space](https://mempool.space/), abyste mohli sledovat její vytěžení:

![Vyhledání TXID na mempool.space](assets/fr/22.webp)

Vezměte prosím na vědomí: transakce se bude zobrazovat jako "Transaction not found", dokud těžař MARA nevytěží blok a nezahrne do něj vaši transakci. To může trvat několik desítek minut, ba i hodin, protože MARA drží jen zhruba 4,5 % hashrate sítě Bitcoin. K 4. srpnu 2026 to odpovídá přibližně jednomu vytěženému bloku každé 3 hodiny a 45 minut.
