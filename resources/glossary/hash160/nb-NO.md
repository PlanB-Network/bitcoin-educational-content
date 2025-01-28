---
term: HASH160

---
Kryptografisk funksjon som brukes i Bitcoin, særlig for å generere Legacy- og SegWit v0-mottakeradresser. Den kombinerer to hashfunksjoner som kjøres suksessivt på inndataene: først SHA256, deretter RIPEMD160. Resultatet av denne funksjonen er derfor 160 bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$$\text{HASH160}(x)