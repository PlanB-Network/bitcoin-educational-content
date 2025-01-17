---
term: (TICHÉ PLATBY)

---
V protokolu Silent Payments jsou štítky celá čísla, která se používají k úpravě počáteční statické adresy za účelem vytvoření mnoha dalších statických adres. Použití těchto štítků umožňuje oddělit platby zasílané prostřednictvím tichých plateb tím, že se pro každé použití použijí jiné statické adresy, aniž by se nadměrně zvýšila provozní zátěž při zjišťování těchto plateb (skenování). Bob používá statickou adresu $B$ složenou ze dvou veřejných klíčů: $B_{\text{scan}}$ pro skenování a $B_{\text{spend}}$ pro utrácení. K veřejnému klíči $B_{\text{skenování}}$ a celému číslu $m$, skalárně vynásobenému generátorovým bodem $G$, se přidá hash $B_{\text{výdaje}}$ a vytvoří se tak jakýsi nový veřejný klíč $B_m$:

$$ B_m = B_{\text{výdaj}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$

Například první klíč $B_1$ získáme tímto způsobem:

$$ B_1 = B_{\text{výdaj}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Statická adresa zveřejněná Bobem se nyní bude skládat z $B_{\text{scan}}$ a $B_m$. Například první statická adresa s označením $1$ bude:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Začínáme pouze od štítku $1$, protože štítek $0$ je vyhrazen pro změnu. Alice, která chce poslat bitcoiny na označenou statickou adresu poskytnutou Bobem, odvodí jedinečnou platební adresu $P_0$ pomocí nové $B_1$ místo $B_{\text{spend}}$:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Ve skutečnosti Alice ani nemusí vědět, že Bob má označenou adresu, protože jednoduše použije druhou část statické adresy, kterou jí poskytl, což je v tomto případě hodnota $B_1$, nikoli $B_{\text{spend}}$. Při vyhledávání plateb bude Bob tímto způsobem vždy používat hodnotu své původní statické adresy s $B_{\text{výdaj}}$:

$$ P_0 = B_{\text{výdaj}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Poté jednoduše odečte zjištěnou hodnotu $P_0$ od každého výstupu po jedné. Poté zkontroluje, zda jeden z výsledků těchto odečtů odpovídá hodnotě jednoho ze štítků, které používá na své peněžence. Pokud se shoduje například pro výstup č. 4 se štítkem $1$, znamená to, že tento výstup je Tichá platba spojená s jeho statickou adresou označenou $B_1$:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

To funguje, protože:

$$ B_1 = B_{\text{výdaj}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Díky této metodě může Bob používat množství statických adres (s $B_1$, $B_2$, $B_3$...), které jsou odvozeny od jeho základní statické adresy ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), aby bylo možné správně oddělit použití.

Toto oddělení statických adres však platí pouze z hlediska správy osobních peněženek, ale neumožňuje oddělení identit. Protože všechny mají stejnou $B_{\text{scan}}$, je velmi snadné spojit všechny statické adresy dohromady a odvodit, že patří jedné entitě.