---
termine: EXCLUSIVE OR
---

Una funzione fondamentale della logica Booleana. L'"Exclusive Or" o XOR ("*Or esclusivo*") prende due operandi Booleani, ciascuno vero o falso, e produce un output vero solo quando i due operandi differiscono. In altre parole, l'output dell'operazione `XOR` è vero se esattamente uno (ma non entrambi) degli operandi è vero. Per esempio, l'operazione `XOR` tra `1` e `0` risulterà in `1`. Notiamo: $1 \oplus 0 = 1$. Analogamente, l'operazione `XOR` può essere eseguita su sequenze più lunghe di bit. Per esempio, $10110 \oplus 01110 = 11000$. Ogni bit della sequenza è confrontato con il suo corrispondente, e l'operazione `XOR` viene applicata. Ecco la tabella di verità per l'operazione `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

L'operazione `XOR` è utilizzata in molte aree dell'informatica, specialmente nella crittografia, per i suoi interessanti attributi come:
* La sua commutatività: l'ordine degli operandi non influisce sul risultato. Per due variabili date $D$ e $E$: $D \oplus E = E \oplus D$;
* La sua associatività: il raggruppamento degli operandi non influisce sul risultato. Per tre variabili date $A$, $B$ e $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Ha un elemento neutro `0`: un operando eseguito con lo XOR con 0 sarà sempre uguale all'operando. Per una variabile data $A$: $A \oplus 0 = A$;
* Ogni elemento è il proprio inverso. Per una variabile data $A$: $A \oplus A = 0$.

Nel contesto di Bitcoin, l'operazione `XOR` è ovviamente utilizzata in molti punti. Per esempio, `XOR` è massicciamente usato nella funzione `SHA256`, che è ampiamente utilizzata nel protocollo Bitcoin. Alcuni protocolli come il *SeedXOR* di Coldcard utilizzano anche questa primitiva per altre applicazioni. Si trova anche in BIP47 per criptare il codice di pagamento riutilizzabile durante la sua trasmissione.
Nel campo più ampio della crittografia, `XOR` può essere utilizzato così com'è come algoritmo di crittografia simmetrica. Questo algoritmo è chiamato "One-Time Pad" o "Cifrario di Vernam", dal nome del suo inventore. Sebbene sia impraticabile a causa della lunghezza della chiave, questo algoritmo è uno dei soli algoritmi di crittografia riconosciuti come incondizionatamente sicuri.