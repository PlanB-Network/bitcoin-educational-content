---
term: CAMINHO DE DERIVAÇÃO

---
No contexto das carteiras Determinísticas Hierárquicas (HD), um caminho de derivação refere-se à sequência de índices utilizados para derivar chaves-filhas a partir de uma chave-mestra. Descrito na BIP32, este caminho identifica a estrutura em árvore para derivar chaves-filhas. Um caminho de derivação é representado por uma série de índices separados por barras, e sempre começa com a chave mestra (denotada como `m/`). Por exemplo, um caminho típico pode ser `m/84'/0'/0'/0'/0/0`. Cada nível de derivação está associado a uma profundidade específica:


- `m /` indica a chave privada mestra. É única para uma carteira e não pode ter irmãos na mesma profundidade. A chave mestra é derivada diretamente da semente;
- `m / purpose' /` indica o objetivo da derivação que ajuda a identificar a norma seguida. Este campo é descrito em BIP43. Por exemplo, se a carteira segue o padrão BIP84 (SegWit V0), o índice será então `84'`;
- `m / purpose' / coin-type' /` indica o tipo de criptomoeda. Isto permite uma diferenciação clara entre os ramos dedicados a uma criptomoeda e os dedicados a outra numa carteira com várias moedas. O índice dedicado à Bitcoin é `0'`;
- `m / purpose' / coin-type' / account' /` indica o número da conta. Esta profundidade facilita a diferenciação e a organização de uma carteira em diferentes contas. Estas contas são numeradas a partir de `0'`. Chaves estendidas (`xpub`, `xprv`...) são encontradas neste nível de profundidade;
- `m / purpose' / coin-type' / account' / change /` indica o percurso. Cada conta, tal como definida na profundidade 3, tem dois caminhos na profundidade 4: uma cadeia externa e uma cadeia interna (também designada por "troco"). A cadeia externa deriva endereços destinados a serem partilhados publicamente, ou seja, os endereços que nos são oferecidos quando clicamos em "receber" no software da nossa carteira. A cadeia interna obtém endereços que não se destinam a ser trocados publicamente, principalmente endereços de troco. A cadeia externa é identificada com o índice `0` e a cadeia interna é identificada com o índice `1`. Notará que, a partir desta profundidade, já não efectuamos uma derivação reforçada, mas uma derivação normal (não há apóstrofo). É graças a este mecanismo que somos capazes de derivar todas as chaves públicas filhas a partir do seu `xpub`;
- `m / purpose' / coin-type' / account' / change / address-index` indica simplesmente o número do endereço de receção e o seu par de chaves, de forma a diferenciá-lo dos seus irmãos na mesma profundidade e no mesmo ramo. Por exemplo, o primeiro endereço derivado tem o índice `0`, o segundo endereço tem o índice `1`, e assim por diante...

Por exemplo, se o meu endereço de receção tiver o caminho de derivação `m / 86' / 0' / 0' / 0 / 5`, podemos deduzir a seguinte informação:


- `86'` indica que estamos a seguir o padrão de derivação do BIP86 (Taproot / SegWit V1);
- `0'` indica que se trata de um endereço Bitcoin;
- `0'` indica que estamos na primeira conta da carteira;
- o "0" indica que se trata de um endereço externo;
- `5` indica que é o sexto endereço externo desta conta.

![](../../dictionnaire/assets/18.webp)