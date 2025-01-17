---
term: BIP44

---
Uma proposta de melhoria que introduz uma estrutura de derivação hierárquica normalizada para as carteiras HD. A BIP44 baseia-se nos princípios estabelecidos pela BIP32 para a derivação de chaves e na BIP43 para a utilização do campo "purpose". Introduz uma estrutura de derivação de cinco níveis: `m / purpose' / coin_type' / account' / change / address_index`. Eis os pormenores de cada nível:


- `m /` indica a chave privada mestra. É única para uma carteira e não pode ter irmãos na mesma profundidade. A chave mestra é derivada diretamente da semente da carteira;
- `m / purpose' /` indica o objetivo da derivação que ajuda a identificar a norma seguida. Este campo é descrito em BIP43. Por exemplo, se a carteira seguir o padrão BIP84 (SegWit V0), o índice será então `84'`;
- `m / purpose' / coin-type' /` indica o tipo de criptomoeda. Isto permite uma diferenciação clara entre os ramos dedicados a uma moeda criptográfica e os dedicados a outra moeda criptográfica numa carteira com várias moedas. O índice dedicado à Bitcoin é `0'`;
- `m / purpose' / coin-type' / account' /` indica o número da conta. Esta profundidade permite uma fácil diferenciação e organização de uma carteira em diferentes contas. Estas contas são numeradas a partir de `0'`. Chaves estendidas (`xpub`, `xprv`...) são encontradas nesta profundidade;
- `m / purpose' / coin-type' / account' / change /` indica a cadeia. Cada conta, tal como definida na profundidade 3, tem duas cadeias na profundidade 4: uma cadeia externa e uma cadeia interna (também designada por "troco"). A cadeia externa deriva endereços destinados a serem comunicados publicamente, ou seja, os endereços que nos são oferecidos quando clicamos em "receber" no software da nossa carteira. A cadeia interna deriva endereços que não se destinam a ser trocados publicamente, ou seja, principalmente endereços de troca. A cadeia externa é identificada com o índice `0` e a cadeia interna é identificada com o índice `1`. Notará que, a partir desta profundidade, já não efectuamos uma derivação reforçada, mas uma derivação normal (não há apóstrofo). É graças a este mecanismo que somos capazes de derivar todas as chaves públicas filhas a partir do seu `xpub`;
- `m / purpose' / coin-type' / account' / change / address-index` indica simplesmente o número do endereço de receção e o seu par de chaves, de forma a diferenciá-lo dos seus irmãos na mesma profundidade e no mesmo ramo. Por exemplo, o primeiro endereço derivado tem o índice `0`, o segundo endereço tem o índice `1`, e assim por diante...

Por exemplo, se o meu endereço de receção tiver o caminho de derivação `m / 86' / 0' / 0' / 0 / 5`, podemos deduzir a seguinte informação:


- `86'` indica que estamos a seguir o padrão de derivação do BIP86 (Taproot ou SegWitV1);
- `0'` indica que se trata de um endereço Bitcoin;
- `0'` indica que estamos na primeira conta da carteira;
- o "0" indica que se trata de um endereço externo;
- `5` indica que é o sexto endereço externo desta conta.

![](../../dictionnaire/assets/18.webp)