---
termo: BIP44
---

Uma proposta de melhoria que introduz uma estrutura de derivação hierárquica padrão para carteiras HD. O BIP44 se baseia nos princípios estabelecidos pelo BIP32 para derivação de chaves e no BIP43 para o uso do campo “purpose” (finalidade). Ele introduz uma estrutura de derivação de cinco níveis: `m / purpose' / coin_type' / account' / change / address_index`. Aqui estão os detalhes de cada profundidade:
* `m /` indica a chave privada mestre. É única para uma carteira e não pode ter irmãos na mesma profundidade. A chave mestre é derivada diretamente da semente da carteira;
* `m / purpose' /` indica o propósito da derivação, o que ajuda a identificar o padrão seguido. Este campo é descrito no BIP43. Por exemplo, se a carteira segue o padrão BIP84 (SegWit V0), o índice seria então `84'`;
* `m / purpose' / coin-type' /` indica o tipo de criptomoeda. Isso permite uma clara diferenciação entre ramos dedicados a uma criptomoeda e aqueles dedicados a outra criptomoeda em uma carteira multi-moedas. O índice dedicado ao Bitcoin é `0'`;
* `m / purpose' / coin-type' / account' /` indica o número da conta. Esta profundidade permite uma fácil diferenciação e organização de uma carteira em diferentes contas. Estas contas são numeradas a partir de `0'`. Chaves estendidas (`xpub`, `xprv`...) são encontradas nesta profundidade;
* `m / purpose' / coin-type' / account' / change /` indica a cadeia. Cada conta, conforme definido na profundidade 3, tem duas cadeias na profundidade 4: uma cadeia externa e uma cadeia interna (também chamada de “change”). A cadeia externa deriva endereços destinados a serem comunicados publicamente, ou seja, os endereços oferecidos a nós quando clicamos em “receber” no nosso software de carteira. A cadeia interna deriva endereços não destinados a serem trocados publicamente, ou seja, principalmente endereços de troco. A cadeia externa é identificada com o índice `0` e a cadeia interna é identificada com o índice `1`. Você notará que a partir desta profundidade, não realizamos mais uma derivação endurecida, mas uma derivação normal (não há apóstrofo). É graças a este mecanismo que somos capazes de derivar todas as chaves públicas filhas a partir de seu `xpub`;
* `m / purpose' / coin-type' / account' / change / address-index` simplesmente indica o número do endereço de recebimento e seu par de chaves, a fim de diferenciá-lo de seus irmãos na mesma profundidade no mesmo ramo. Por exemplo, o primeiro endereço derivado tem o índice `0`, o segundo endereço tem o índice `1`, e assim por diante...
Por exemplo, se meu endereço de recebimento tem o caminho de derivação `m / 86' / 0' / 0' / 0 / 5`, podemos deduzir as seguintes informações:
* `86'` indica que estamos seguindo o padrão de derivação do BIP86 (Taproot ou SegWitV1);
* `0'` indica que é um endereço Bitcoin;
* `0'` indica que estamos na primeira conta da carteira;
* `0` indica que é um endereço externo;
* `5` indica que é o sexto endereço externo desta conta.

![](../../dictionnaire/assets/18.png)