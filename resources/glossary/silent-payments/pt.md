---
term: PAGAMENTOS SILENCIOSOS

---
Método para utilizar endereços Bitcoin estáticos para receber pagamentos sem reutilização de endereços, sem interação e sem uma ligação visível na cadeia entre os diferentes pagamentos e o endereço estático. Esta técnica elimina a necessidade de gerar novos endereços de receção não utilizados para cada transação, evitando assim as interações habituais na Bitcoin em que o destinatário tem de fornecer um novo endereço ao pagador.

Com os pagamentos silenciosos, o pagador utiliza as chaves públicas do destinatário (chave pública de despesa e chave pública de digitalização) e a soma das suas próprias chaves privadas como entrada para gerar um novo endereço para cada pagamento. Apenas o destinatário, com as suas chaves privadas, pode calcular a chave privada correspondente a este endereço de pagamento. O ECDH (*Elliptic-Curve Diffie-Hellman*), um algoritmo de troca de chaves criptográficas, é utilizado para estabelecer um segredo partilhado que é depois utilizado para derivar o endereço de receção e a chave privada (apenas do lado do destinatário). Para identificar os pagamentos silenciosos que lhes são destinados, os destinatários devem analisar a cadeia de blocos e examinar cada transação que corresponda aos critérios do protocolo. Ao contrário do BIP47, que utiliza uma transação de notificação para estabelecer o canal de pagamento, os Silent Payments eliminam este passo, poupando uma transação. No entanto, o compromisso é que o destinatário deve examinar todas as transações potenciais para determinar, aplicando o ECDH, se elas são endereçadas a ele.

Por exemplo, o endereço estático de Bob $B$ representa a concatenação da sua chave pública de scan e da sua chave pública de spend:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{gastos}} $$

Estas chaves são simplesmente derivadas do seguinte caminho:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Este endereço estático é publicado pelo Bob. Alice recupera-o para efetuar um pagamento silencioso ao Bob. Ela calcula o endereço de pagamento do Bob $P_0$ desta forma:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Onde:

$$ \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A) $$

Com:


- $B_{\text{scan}}$: a chave pública de scan do Bob (endereço estático);
- $B_{\text{spend}}$: a chave pública de despesa do Bob (endereço estático);
- $A$: A soma das chaves públicas na entrada (tweak);
- $a$: A chave privada do tweak, ou seja, a soma de todos os pares de chaves utilizados no `scriptPubKey` dos UTXOs consumidos como inputs na transação da Alice;
- $\text{outpoint}_L$: O UTXO mais pequeno (lexicograficamente) utilizado como entrada na transação da Alice;
- $\text{ ‖ }$: Concatenação (a operação de juntar operandos de ponta a ponta);
- $G$: O ponto gerador da curva elíptica `secp256k1`;
- $\text{hash}$: A função de hash SHA256 marcada com `BIP0352/SharedSecret`;
- $P_0$: A primeira chave pública / endereço único para pagamento ao Bob;
- $0$: Um número inteiro utilizado para gerar vários endereços de pagamento únicos.

O Bob analisa a cadeia de blocos para encontrar o seu pagamento silencioso desta forma:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Com:


- $b_{\text{scan}}$: A chave de digitalização privada do Bob.

Se encontrar um endereço $P_0$ que contenha um pagamento silencioso dirigido a ele, calcula $p_0$, a chave privada que lhe permite gastar os fundos enviados pela Alice para $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Com:


- $b_{\text{spend}}$: a chave privada de despesa do Bob;
- $n$: a ordem da curva elíptica `secp256k1`.

Para além desta versão de base, as etiquetas podem também ser utilizadas para gerar vários endereços estáticos diferentes a partir do mesmo endereço estático de base, com o objetivo de separar as múltiplas utilizações sem multiplicar excessivamente o trabalho necessário durante a digitalização.