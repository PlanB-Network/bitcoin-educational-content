---
term: PAGOS SILENCIOSOS

---
Método para utilizar direcciones Bitcoin estáticas para recibir pagos sin reutilización de direcciones, sin interacción y sin un vínculo visible en la cadena entre los diferentes pagos y la dirección estática. Esta técnica elimina la necesidad de generar nuevas direcciones receptoras no utilizadas para cada transacción, evitando así las interacciones habituales en Bitcoin en las que el receptor debe proporcionar una nueva dirección al pagador.

Con los pagos silenciosos, el pagador utiliza las claves públicas del destinatario (clave pública de gasto y clave pública de escaneado) y la suma de sus propias claves privadas como entrada para generar una nueva dirección para cada pago. Sólo el receptor, con sus claves privadas, puede calcular la clave privada correspondiente a esta dirección de pago. ECDH (*Elliptic-Curve Diffie-Hellman*), un algoritmo de intercambio de claves criptográficas, se utiliza para establecer un secreto compartido que luego se utiliza para derivar la dirección de recepción y la clave privada (sólo en el lado del destinatario). Para identificar los pagos silenciosos que les están destinados, los receptores deben escanear la cadena de bloques y examinar cada transacción que coincida con los criterios del protocolo. A diferencia de BIP47, que utiliza una transacción de notificación para establecer el canal de pago, Silent Payments elimina este paso, ahorrando una transacción. Sin embargo, el compromiso es que el receptor debe escanear todas las transacciones potenciales para determinar, aplicando ECDH, si van dirigidas a él.

Por ejemplo, la dirección estática $B$ de Bob representa la concatenación de su clave pública de exploración y su clave pública de gasto:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Estas claves se derivan simplemente de la siguiente ruta:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Esta dirección estática es publicada por Bob. Alice la recupera para hacer un pago silencioso a Bob. Ella calcula la dirección de pago de Bob $P_0$ de esta manera:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{text{scan}} \text{ ‖ } 0) \cdot G $$

Dónde:

$$ \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A) $$

Con:


- $B_{text{scan}}$: clave pública de escaneo de Bob (dirección estática);
- $B_{\text{spend}}$: la clave pública de gasto de Bob (dirección estática);
- $A$: La suma de las claves públicas en entrada (tweak);
- $a$: La clave privada del tweak, es decir, la suma de todos los pares de claves utilizados en el `scriptPubKey` de los UTXOs consumidos como inputs en la transacción de Alice;
- $\text{outpoint}_L$: El UTXO más pequeño (lexicográficamente) utilizado como entrada en la transacción de Alice;
- $\text{ ‖ }$: Concatenación (la operación de unir operandos de extremo a extremo);
- $G$: El punto generador de la curva elíptica `secp256k1`;
- $\text{hash}$: La función hash SHA256 etiquetada con `BIP0352/SharedSecret`;
- $P_0$: La primera clave pública / dirección única para el pago a Bob;
- $0$: Un número entero utilizado para generar múltiples direcciones de pago únicas.

Bob escanea la blockchain para encontrar así su Pago Silencioso:

$$ P_0 = B_{{texto{gasto}} + \text{hash}(\text{inputHash} \cdot b_{text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Con:


- $b_{\text{scan}}: La clave privada de escaneo de Bob.

Si encuentra $P_0$ como dirección que contiene un Pago Silencioso dirigido a él, calcula $p_0$, la clave privada que le permite gastar los fondos enviados por Alice a $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Con:


- $b_{\text{spend}}: la clave privada de gasto de Bob;
- $n$: el orden de la curva elíptica `secp256k1`.

Además de esta versión básica, las etiquetas también pueden utilizarse para generar varias direcciones estáticas diferentes a partir de la misma dirección estática básica, con el objetivo de separar usos múltiples sin multiplicar injustificadamente el trabajo necesario durante el escaneado.