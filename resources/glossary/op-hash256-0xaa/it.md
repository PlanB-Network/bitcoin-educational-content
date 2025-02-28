---
term: OP_HASH256 (0XAA)

---
Prende l'elemento superiore dalla pila e lo sostituisce con il suo hash utilizzando due volte la funzione `SHA256`. L'input viene sottoposto a hash una volta con `SHA256`, quindi il digest viene sottoposto a hash una seconda volta con `SHA256`. Questo processo in due fasi genera un'impronta digitale a 256 bit.