---
term: LABEL (SILENT PAYMENTS)
---

V rámci protokolu Silent Payments jsou štítky (labels) celá čísla používaná k modifikaci původní statické adresy za účelem vytvoření mnoha dalších statických adres. Použití těchto štítků umožňuje segregaci plateb odeslaných prostřednictvím Silent Payments tím, že pro každé použití se využívají různé statické adresy, aniž by to nadměrně zvyšovalo operační zátěž při detekci těchto plateb (skenování). Bob používá statickou adresu $B$, která se skládá ze dvou veřejných klíčů: $B_{\text{scan}}$ pro skenování a $B_{\text{spend}}$ pro utrácení. Hash $b_{\text{scan}}$ a celého čísla $m$, skalárně násobený generátorovým bodem $G$, je přidán k veřejnému klíči pro utrácení $B_{\text{spend}}$, aby se vytvořil jakýsi nový veřejný klíč pro utrácení $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Například první klíč $B_1$ je získán tímto způsobem:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Statická adresa publikovaná Bobem bude nyní složena z $B_{\text{scan}}$ a $B_m$. Například první statická adresa se štítkem $1$ bude:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Začínáme pouze od štítku $1$, protože štítek $0$ je rezervován pro změnu. Alice, která si přeje poslat bitcoiny na označenou statickou adresu poskytnutou Bobem, odvodí unikátní platební adresu $P_0$ použitím nového $B_1$ místo $B_{\text{spend}}$:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Ve skutečnosti Alice nemusí ani vědět, že Bob má označenou adresu, protože jednoduše použije druhou část statické adresy, kterou jí poskytl, což v tomto případě je hodnota $B_1$ namísto $B_{\text{spend}}$. Pro skenování plateb Bob vždy použije hodnotu své původní statické adresy s $B_{\text{spend}}$ tímto způsobem:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Poté jednoduše odečte hodnotu, kterou najde pro $P_0$, od každého výstupu postupně. Poté zkontroluje, zda jedna z výsledků těchto odečtů odpovídá hodnotě jednoho ze štítků, které používá ve své peněžence. Pokud to odpovídá, například pro výstup č. 4 se štítkem $1$, to znamená, že tento výstup je Silent Payment spojený s jeho statickou adresou označenou $B_1$:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

To funguje, protože:
$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$
Díky této metodě může Bob používat množství statických adres (s $B_1$, $B_2$, $B_3$...), všechny odvozené od jeho základní statické adresy ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), aby správně oddělil použití.

Avšak toto oddělení statických adres je platné pouze z pohledu správy osobní peněženky, ale neumožňuje oddělení identit. Jelikož všechny mají stejný $B_{\text{scan}}$, je velmi snadné všechny statické adresy spojit dohromady a usoudit, že patří jedné entitě.