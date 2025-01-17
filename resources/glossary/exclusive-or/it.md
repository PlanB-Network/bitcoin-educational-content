---
term: ESCLUSIVO O

---
Funzione fondamentale della logica booleana. L'operazione "Or esclusivo" o XOR ("*Or esclusivo*") prende due operandi booleani, ciascuno dei quali è vero o falso, e produce un'uscita vera solo quando i due operandi differiscono. In altre parole, l'uscita dell'operazione `XOR` è vera se esattamente uno (ma non entrambi) degli operandi è vero. Ad esempio, l'operazione `XOR` tra `1` e `0` darà come risultato `1`. Notiamo: $1 ´oplus 0 = 1$. Analogamente, l'operazione `XOR` può essere eseguita su sequenze di bit più lunghe. Ad esempio, $10110 \oplus 01110 = 11000$. Ogni bit della sequenza viene confrontato con la sua controparte e viene applicata l'operazione `XOR`. Ecco la tabella di verità per l'operazione `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

L'operazione `XOR` è utilizzata in molte aree dell'informatica, in particolare nella crittografia, per le sue interessanti caratteristiche, quali:


- La commutatività: l'ordine degli operandi non influisce sul risultato. Per due variabili date $D$ ed $E$: $D \oplus E = E \oplus D$;
- La sua associatività: il raggruppamento degli operandi non influisce sul risultato. Per tre variabili date $A$, $B$ e $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Ha un elemento neutro, `0`: un operando che ha come base 0 sarà sempre uguale all'operando. Per una variabile data $A$: $A ´oplus 0 = A$;
- Ogni elemento è il suo inverso. Per una variabile data $A$: $A ´oplus A = 0$.

Nel contesto di Bitcoin, l'operazione `XOR` è ovviamente utilizzata in molti punti. Ad esempio, l'operazione `XOR` è utilizzata in modo massiccio nella funzione `SHA256`, ampiamente utilizzata nel protocollo Bitcoin. Alcuni protocolli come *SeedXOR* di Coldcard utilizzano questa primitiva anche per altre applicazioni. Si trova anche in BIP47 per criptare il codice di pagamento riutilizzabile durante la sua trasmissione.

Nel campo più ampio della crittografia, il `XOR' può essere utilizzato come algoritmo di crittografia simmetrica. Questo algoritmo è chiamato "One-Time Pad" o "Cifrario di Vernam", dal nome del suo inventore. Sebbene poco pratico a causa della lunghezza della chiave, questo algoritmo è uno dei pochi algoritmi di crittografia riconosciuti come incondizionatamente sicuri.