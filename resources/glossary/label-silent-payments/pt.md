---
termo: LABEL (PAGAMENTOS SILENCIOSOS)
---

Dentro do protocolo de Pagamentos Silenciosos, rótulos são inteiros usados para modificar o endereço estático inicial a fim de criar muitos outros endereços estáticos. O uso desses rótulos permite a segregação de pagamentos enviados via Pagamentos Silenciosos, empregando diferentes endereços estáticos para cada uso, sem aumentar excessivamente o ônus operacional para detectar esses pagamentos (varredura). Bob usa um endereço estático $B$, composto por duas chaves públicas: $B_{\text{scan}}$ para varredura e $B_{\text{spend}}$ para gastar. O hash de $b_{\text{scan}}$ e um inteiro $m$, multiplicado escalarmente pelo ponto gerador $G$, é adicionado à chave pública de gasto $B_{\text{spend}}$ para criar uma espécie de nova chave pública de gasto $B_m$:

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Por exemplo, a primeira chave $B_1$ é obtida desta maneira:

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

O endereço estático publicado por Bob agora será composto por $B_{\text{scan}}$ e $B_m$. Por exemplo, o primeiro endereço estático com o rótulo $1$ será:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Começamos apenas do rótulo $1$, porque o rótulo $0$ é reservado para troco. Alice, que deseja enviar bitcoins para o endereço estático rotulado fornecido por Bob, derivará o endereço de pagamento único $P_0$ usando o novo $B_1$ em vez de $B_{\text{spend}}$:

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Na realidade, Alice pode nem mesmo saber que Bob tem um endereço rotulado, pois ela simplesmente usa a segunda parte do endereço estático que ele forneceu, que neste caso é o valor $B_1$ em vez de $B_{\text{spend}}$. Para varrer os pagamentos, Bob sempre usará o valor de seu endereço estático inicial com $B_{\text{spend}}$ desta maneira:

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
Então, ele simplesmente subtrai o valor que encontra para $P_0$ de cada saída, uma por uma. Ele então verifica se um dos resultados dessas subtrações corresponde ao valor de um dos rótulos que ele usa em sua carteira. Se corresponder, por exemplo, para a saída #4 com o rótulo $1$, isso significa que esta saída é um Pagamento Silencioso associado ao seu endereço estático rotulado $B_1$:
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Isso funciona porque:
$$  B_1 = B_{\text{gasto}} + \text{hash}(b_{\text{varredura}} \text{ ‖ } 1) \cdot G  $$
Graças a este método, Bob pode usar uma multiplicidade de endereços estáticos (com $B_1$, $B_2$, $B_3$...), todos derivados do seu endereço estático base ($B = B_{\text{varredura}} \text{ ‖ } B_{\text{gasto}}$), a fim de separar adequadamente os usos.

No entanto, esta separação de endereços estáticos é válida apenas do ponto de vista da gestão de carteira pessoal, mas não permite a separação de identidades. Uma vez que todos têm o mesmo $B_{\text{varredura}}$, é muito fácil associar todos os endereços estáticos juntos e deduzir que pertencem a uma única entidade.