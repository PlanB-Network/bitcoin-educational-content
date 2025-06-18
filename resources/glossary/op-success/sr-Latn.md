---
term: OP_USPEH
---

`OP_SUCCESS` predstavlja niz opkodova koji su ranije bili onemogućeni i sada su rezervisani za buduću upotrebu u Tapscript-u. Njihov krajnji cilj je da olakšaju ažuriranja i proširenja jezika skripti, omogućavajući uvođenje novih funkcionalnosti putem Soft forkova. Kada se jedan od ovih opkodova susretne u skripti, to označava automatski uspeh tog dela skripte, bez obzira na prisutne podatke ili uslove. To znači da skripta nastavlja sa izvršavanjem bez greške, nezavisno od prethodnih operacija.


Dakle, kada se novi opcode doda na `OP_SUCCESS`, to nužno predstavlja dodavanje restriktivnijeg pravila od prethodnog. Ažurirani čvorovi tada mogu proveriti usklađenost sa ovim pravilom, a neažurirani čvorovi neće odbiti povezane transakcije i blokove koji ih uključuju, jer `OP_SUCCESS` validira taj deo skripta. Stoga, nema Hard Fork.


U poređenju, `OP_NOP` (*No Operation*) takođe služi kao rezervno mesto u skripti, ali nema efekta na izvršenje skripte. Kada se naiđe na `OP_NOP`, skripta jednostavno nastavlja bez promene stanja steka ili napredovanja skripte. Ključna razlika, dakle, je u njihovom uticaju na izvršenje: `OP_SUCCESS` garantuje uspešan prolaz kroz taj deo skripte, dok je `OP_NOP` neutralan i ne utiče ni na stek ni na tok skripte. Ovi opkodovi su označeni sa `OP_SUCCESSN` gde je `N` broj koji se koristi za razlikovanje `OP_SUCCESS`.