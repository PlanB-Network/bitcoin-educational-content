---
term: SCRIPTSIG
---

Element transakcji Bitcoin znajdujący się w danych wejściowych. `scriptSig` dostarcza niezbędnych danych, aby spełnić warunki określone przez `scriptPubKey` poprzedniej transakcji, z której wydawane są środki. Odgrywa on zatem rolę uzupełniającą do `scriptPubKey`. Zazwyczaj `scriptSig` zawiera podpis cyfrowy i klucz publiczny. Podpis jest generowany przez właściciela bitcoinów przy użyciu jego klucza prywatnego i dowodzi, że ma on autoryzację do wydania UTXO. W tym przypadku `scriptSig` pokazuje, że posiadacz danych wejściowych posiada klucz prywatny odpowiadający kluczowi publicznemu powiązanemu z Address określonym w `scriptPubKey` poprzedniej transakcji wychodzącej.


Gdy transakcja jest weryfikowana, dane z `scriptSig` są wykonywane w odpowiednim `scriptPubKey`. Jeśli wynik jest prawidłowy, oznacza to, że warunki wydania środków zostały spełnione. Jeśli wszystkie wejścia transakcji dostarczają `scriptSig`, który weryfikuje ich `scriptPubKey`, transakcja jest ważna i może zostać dodana do bloku do wykonania.


Na przykład, oto klasyczny `scriptSig` P2PKH:


```text
<signature> <public key>
```


Odpowiednim `scriptPubKey` będzie:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


![](../../dictionnaire/assets/35.webp)


> `scriptSig` jest również czasami nazywany "skryptem odblokowującym" w języku angielskim