---
term: BIP0330
---

Predlog poznat kao "*Erlay*", koji ima za cilj optimizaciju propagacije nepotvrđenih transakcija u Bitcoin mreži. Trenutno se transakcije emituju svim čvorovima jednog nod-a, što rezultira redundancijom i prekomernom upotrebom propusnog opsega. BIP330 predlaže da se ovo emitovanje ograniči na 8 čvorova po defaultu, a zatim koristi mehanizam za usklađivanje kako bi se efikasno delile nedostajuće transakcije. Erlay smanjuje potrošnju propusnog opsega za oko 40%. Takođe izbegava linearno povećanje potrošnje propusnog opsega sa brojem čvorova povezanih na nod.