---
term: BIP111

---
Tehakse ettepanek lisada teenuse bit nimega `NODE_BLOOM`, et võimaldada sõlmedel selgesõnaliselt teatada oma Bloomi filtrite toetusest, nagu on kirjeldatud BIP37-s. NODE_BLOOM`i lisamine võimaldab sõlmeoperaatoritel keelata selle teenuse kasutamine, et vähendada DoS-i ohtu. Bitcoin Core'is on BIP37 valik vaikimisi välja lülitatud. Selle lubamiseks tuleb konfiguratsioonifaili sisestada parameeter `peerbloomfilters=1`.