---
term: CAMINHO DE DERIVAÇÃO
---

No contexto de carteiras Hierárquicas Determinísticas (HD), um caminho de derivação refere-se à sequência de índices usados para derivar chaves filhas a partir de uma chave mestre. Descrito no BIP32, esse caminho identifica a estrutura de árvore para derivar chaves filhas. Um caminho de derivação é representado por uma série de índices separados por barras, e sempre começa com a chave mestre (denotada como `m/`). Por exemplo, um caminho típico pode ser `m/84'/0'/0'/0/0`. Cada nível de derivação está associado a uma profundidade específica:
* `m /` indica a chave privada mestre. É única para uma carteira e não pode ter irmãos na mesma profundidade. A chave mestre é derivada diretamente da semente;
* `m / purpose' /` indica o propósito da derivação, que ajuda a identificar o padrão seguido. Este campo é descrito no BIP43. Por exemplo, se a carteira adere ao padrão BIP84 (SegWit V0), o índice seria então `84'`;
* `m / purpose' / coin-type' /` indica o tipo de criptomoeda. Isso permite uma clara diferenciação entre ramos dedicados a uma criptomoeda e aqueles dedicados a outra em uma carteira multi-moedas. O índice dedicado ao Bitcoin é `0'`;
* `m / purpose' / coin-type' / account' /` indica o número da conta. Esta profundidade facilita a diferenciação e organização de uma carteira em diferentes contas. Estas contas são numeradas a partir de `0'`. Chaves estendidas (`xpub`, `xprv`...) são encontradas neste nível de profundidade;
* `m / purpose' / coin-type' / account' / change /` indica o caminho. Cada conta, conforme definido na profundidade 3, tem dois caminhos na profundidade 4: uma cadeia externa e uma cadeia interna (também chamada de "troco"). A cadeia externa deriva endereços destinados a ser compartilhados publicamente, ou seja, os endereços que nos são oferecidos quando clicamos em "receber" em nosso software de carteira. A cadeia interna deriva endereços não destinados a serem trocados publicamente, principalmente endereços de troco. A cadeia externa é identificada com o índice `0` e a cadeia interna é identificada com o índice `1`. Você notará que a partir desta profundidade, não realizamos mais uma derivação endurecida, mas uma derivação normal (não há apóstrofo). É graças a este mecanismo que somos capazes de derivar todas as chaves públicas filhas a partir de seu `xpub`;

* `m / purpose' / coin-type' / account' / change / address-index` simplesmente indica o número do endereço de recebimento e seu par de chaves, a fim de diferenciá-lo de seus irmãos na mesma profundidade no mesmo ramo. Por exemplo, o primeiro endereço derivado tem o índice `0`, o segundo endereço tem o índice `1`, e assim por diante...

Por exemplo, se meu endereço de recebimento tem o caminho de derivação `m / 86' / 0' / 0' / 0 / 5`, podemos deduzir as seguintes informações:
* `86'` indica que estamos seguindo o padrão de derivação do BIP86 (Taproot / SegWit V1);
* `0'` indica que é um endereço Bitcoin;
* `0'` indica que estamos na primeira conta da carteira;
* `0` indica que é um endereço externo;
* `5` indica que é o sexto endereço externo desta conta.

![](../../dictionnaire/assets/18.png)