---
term: BECH32 E BECH32M

---
`Bech32` e `Bech32m` são dois formatos de codificação de endereços para receber bitcoins. São baseados numa base 32 ligeiramente modificada. Eles incorporam um checksum baseado num algoritmo de correção de erros chamado BCH (*Bose-Chaudhuri-Hocquenghem*). Em comparação com os endereços Legacy, codificados em `Base58check`, os endereços `Bech32` e `Bech32m` têm um checksum mais eficiente, permitindo a deteção e potencialmente a correção automática de erros de digitação. O seu formato também oferece melhor legibilidade, com apenas caracteres minúsculos. Aqui está a matriz de adição para este formato a partir da base 10:

&nbsp;

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | q | p | z | r | y | 9 | x | 8 |

| 8 | g | f | 2 | t | v | d | w | 0 |

| 16 | s | 3 | j | n | 5 | 4 | k | h |

| 24 | c | e | 6 | m | u | a | 7 | l |

&nbsp;

Bech32 e Bech32m são formatos de codificação utilizados para representar endereços SegWit. O Bech32 é um formato de codificação de endereços introduzido pelo BIP173 em 2017. Utiliza um conjunto específico de caracteres, composto por números e letras minúsculas, para minimizar os erros de digitação e facilitar a leitura. Os endereços Bech32 geralmente começam com `bc1` para indicar que são nativos do SegWit. Este formato é usado apenas em endereços SegWit V0, com os scripts P2WPKH (Pay to Witness Public Key Hash) e P2WSH (Pay to Witness Script Hash). No entanto, existe uma pequena e inesperada falha específica do formato Bech32. Sempre que o último caractere do endereço é um `p`, adicionar ou remover qualquer número de caracteres `q` imediatamente anteriores a ele não invalida a soma de verificação. Isto não afecta as utilizações existentes dos endereços SegWit V0 (BIP173) devido à sua restrição a dois comprimentos definidos. No entanto, isto pode afetar futuras utilizações da codificação Bech32. O formato Bech32m é simplesmente um formato Bech32 com este erro corrigido. Foi introduzido com o BIP350 em 2020. Os endereços Bech32m também começam com `bc1`, mas foram especificamente concebidos para serem compatíveis com o SegWit V1 (Taproot) e versões posteriores, com o script P2TR (Pay to TapRoot).