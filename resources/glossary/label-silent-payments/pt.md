---
term: ETIQUETA (PAGAMENTOS SILENCIOSOS)

---
No âmbito do protocolo de pagamentos silenciosos, as etiquetas são números inteiros utilizados para modificar o endereço estático inicial, a fim de criar muitos outros endereços estáticos. O uso dessas etiquetas permite a segregação dos pagamentos enviados via Silent Payments, empregando endereços estáticos diferentes para cada uso, sem aumentar excessivamente a carga operacional para a deteção desses pagamentos (scanning). O Bob utiliza um endereço estático $B$, composto por duas chaves públicas: $B_{\text{scan}}$ para o scanning e $B_{\text{spend}}$ para o spending. O hash de $b_{\text{scan}}$ e um inteiro $m$, multiplicado por escalar pelo ponto gerador $G$, é adicionado à chave pública de despesa $B_{\text{spend}}$ para criar uma espécie de nova chave pública de despesa $B_m$:

$$ B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$

Por exemplo, a primeira chave $B_1$ é obtida desta forma:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

O endereço estático publicado pelo Bob será agora composto por $B_{\text{scan}}$ e $B_m$. Por exemplo, o primeiro endereço estático com a etiqueta $1$ será:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Só começamos a partir do rótulo $1$, porque o rótulo $0$ está reservado para alterações. Alice, que deseja enviar bitcoins para o endereço estático rotulado fornecido por Bob, derivará o endereço de pagamento único $P_0$ usando o novo $B_1$ em vez de $B_{\text{spend}}$:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Na realidade, a Alice pode nem sequer saber que o Bob tem um endereço etiquetado, pois limita-se a utilizar a segunda parte do endereço estático que ele forneceu, que neste caso é o valor $B_1$ em vez de $B_{\text{spend}}$. Para procurar pagamentos, o Bob utilizará sempre o valor do seu endereço estático inicial com $B_{\text{spend}}$ desta forma:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Depois, simplesmente subtrai o valor que encontra para $P_0$ de cada saída, uma a uma. Depois, verifica se um dos resultados destas subtracções corresponde ao valor de uma das etiquetas que usa na sua carteira. Se corresponder, por exemplo, à saída #4 com a etiqueta $1$, isto significa que esta saída é um Pagamento Silencioso associado ao seu endereço estático etiquetado como $B_1$:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Isto funciona porque:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Graças a este método, o Bob pode utilizar uma multiplicidade de endereços estáticos (com $B_1$, $B_2$, $B_3$...), todos derivados do seu endereço estático de base ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), de modo a separar corretamente as utilizações.

No entanto, esta separação de endereços estáticos só é válida do ponto de vista da gestão de carteiras pessoais, mas não permite a separação de identidades. Uma vez que todos eles têm o mesmo $B_{\text{scan}}$, é muito fácil associar todos os endereços estáticos e deduzir que pertencem a uma única entidade.