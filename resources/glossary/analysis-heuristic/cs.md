---
term: ANALÝZA HEURISTIKA

---
Heuristická analýza řetězce bitcoinů je rodina empirických metod používaných ke sledování toku bitcoinů v blockchainu na základě charakteristik pozorovaných v transakcích. Heuristika je praktický přístup k řešení problému, často pomocí přibližných metod, ale představuje dostatečně dobré řešení k dosažení daného cíle. Tyto heuristiky přinášejí poměrně spolehlivé výsledky, nikdy však s absolutní přesností. Jinými slovy, řetězová analýza vždy zahrnuje určitou míru pravděpodobnosti vyvozených závěrů. Například lze s větší či menší jistotou odhadnout, že dvě adresy patří stejnému subjektu, ale úplná jistota je vždy nedosažitelná. Celý cíl řetězové analýzy spočívá právě v agregaci různých heuristik, aby se minimalizovalo riziko chyby. Je to svým způsobem kumulace důkazů, která nám umožňuje přiblížit se realitě. V této souvislosti se rozlišuje vnitřní a vnější heuristika.

Interní heuristika se zaměřuje na charakteristiky specifické pro jednotlivé transakce. Do své analýzy zahrnují prvky, jako je množství UTXO, použité skripty, verze nebo doba uzamčení. Například heuristika kulaté platby umožňuje identifikovat výstup transakce jako pravděpodobně platbu, pokud je její částka kulaté číslo. Tyto heuristiky často umožňují identifikovat změnu (peníze vrácené stejnému uživateli) a pokračovat tak ve sledování.

Vnější heuristika naopak analyzuje podobnosti a charakteristiky mimo samotnou transakci. Zahrnují celé transakční prostředí. Například opakované použití adresy v rámci více transakcí je externí heuristika. Jednou z nich je také CIOH.