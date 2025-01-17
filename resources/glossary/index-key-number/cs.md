---
term: (ČÍSLO KLÍČE)

---
V kontextu peněženky HD se jedná o pořadové číslo přidělené podřízenému klíči vygenerovanému z nadřazeného klíče. Tento index se používá v kombinaci s rodičovským klíčem a kódem rodičovského řetězce k deterministickému odvození jedinečných podřízených klíčů. Umožňuje strukturovanou organizaci a reprodukovatelné generování více sourozeneckých párů podřízených klíčů ze stejného rodičovského klíče. Je to 32bitové celé číslo používané v odvozovací funkci `HMAC-SHA512`. Toto číslo tedy rozlišuje sourozenecké podřízené klíče v rámci peněženky HD.