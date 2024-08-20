---
termo: PAGAMENTOS SILENCIOSOS
---

Método para usar endereços Bitcoin estáticos para receber pagamentos sem reutilização de endereço, sem interação e sem um link visível na cadeia entre os diferentes pagamentos e o endereço estático. Esta técnica elimina a necessidade de gerar novos endereços de recebimento não utilizados para cada transação, evitando assim as interações usuais no Bitcoin onde o destinatário deve fornecer um novo endereço ao pagador.

Com Pagamentos Silenciosos, o pagador usa as chaves públicas do destinatário (chave pública de gasto e chave pública de escaneamento) e a soma de suas próprias chaves privadas como entrada para gerar um endereço novo para cada pagamento. Apenas o destinatário, com suas chaves privadas, pode calcular a chave privada correspondente a este endereço de pagamento. ECDH (*Elliptic-Curve Diffie-Hellman*), um algoritmo de troca de chaves criptográficas, é usado para estabelecer um segredo compartilhado que é então usado para derivar o endereço de recebimento e a chave privada (apenas do lado do destinatário). Para identificar os Pagamentos Silenciosos destinados a eles, os destinatários devem escanear a blockchain e examinar cada transação que corresponda aos critérios do protocolo. Diferente do BIP47, que usa uma transação de notificação para estabelecer o canal de pagamento, os Pagamentos Silenciosos eliminam este passo, economizando uma transação. No entanto, o compromisso é que o destinatário deve escanear todas as transações potenciais para determinar, aplicando ECDH, se são endereçadas a eles.

Por exemplo, o endereço estático de Bob $B$ representa a concatenação de sua chave pública de escaneamento e sua chave pública de gasto:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Estas chaves são simplesmente derivadas do seguinte caminho:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Este endereço estático é publicado por Bob. Alice o recupera para fazer um Pagamento Silencioso a Bob. Ela calcula o endereço de pagamento de Bob $P_0$ desta maneira:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Onde:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

Com:
* $B_{\text{scan}}$: Chave pública de escaneamento de Bob (endereço estático);
* $B_{\text{spend}}$: Chave pública de gasto de Bob (endereço estático);
* $A$: A soma das chaves públicas em entrada (ajuste);
* $a$: A chave privada do ajuste, isto é, a soma de todos os pares de chaves usados no `scriptPubKey` dos UTXOs consumidos como entradas na transação de Alice;
* $\text{outpoint}_L$: O UTXO mais pequeno (lexicograficamente) usado como entrada na transação de Alice;
* $\text{ ‖ }$: Concatenação (a operação de juntar operandos de ponta a ponta);
* $G$: O ponto gerador da curva elíptica `secp256k1`;
* $\text{hash}$: A função de hash SHA256 marcada com `BIP0352/SharedSecret`;
* $P_0$: A primeira chave pública / endereço único para pagamento a Bob;
* $0$: Um inteiro usado para gerar múltiplos endereços de pagamento únicos.

Bob escaneia a blockchain para encontrar seu Pagamento Silencioso desta maneira:
$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Com:
* $b_{\text{scan}}$: chave privada de escaneamento do Bob.

Se ele encontrar $P_0$ como um endereço contendo um Pagamento Silencioso endereçado a ele, ele calcula $p_0$, a chave privada que permite a ele gastar os fundos enviados pela Alice para $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Com:
* $b_{\text{spend}}$: chave privada de gasto do Bob;
* $n$: a ordem da curva elíptica `secp256k1`.

Além desta versão básica, etiquetas também podem ser usadas para gerar vários endereços estáticos diferentes a partir do mesmo endereço estático básico, com o objetivo de separar múltiplos usos sem multiplicar de maneira irrazoável o trabalho requerido durante a varredura.