---
termo: BECH32 E BECH32M
---

`Bech32` e `Bech32m` são dois formatos de codificação de endereços para receber bitcoins. Eles são baseados em uma base 32 ligeiramente modificada. Incorporam um checksum baseado em um algoritmo de correção de erros chamado BCH (*Bose-Chaudhuri-Hocquenghem*). Comparados aos endereços Legacy, codificados em `Base58check`, os endereços `Bech32` e `Bech32m` possuem um checksum mais eficiente, permitindo a detecção e potencial correção automática de erros de digitação. Seu formato também oferece melhor legibilidade, com apenas caracteres minúsculos. Aqui está a matriz de adição para este formato a partir da base 10:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;
Bech32 e Bech32m são formatos de codificação usados para representar endereços SegWit. Bech32 é um formato de codificação de endereço introduzido pelo BIP173 em 2017. Utiliza um conjunto específico de caracteres, composto por números e letras minúsculas, para minimizar erros de digitação e facilitar a leitura. Endereços Bech32 geralmente começam com `bc1` para indicar que são nativos do SegWit. Este formato é usado apenas em endereços SegWit V0, com os scripts P2WPKH (Pay to Witness Public Key Hash) e P2WSH (Pay to Witness Script Hash). No entanto, existe uma pequena falha inesperada específica ao formato Bech32. Sempre que o último caractere do endereço é um `p`, adicionar ou remover qualquer número de caracteres `q` imediatamente antes dele não invalida o checksum. Isso não afeta os usos existentes de endereços SegWit V0 (BIP173) devido à sua restrição a dois comprimentos definidos. No entanto, isso poderia afetar usos futuros da codificação Bech32. O formato Bech32m é simplesmente um formato Bech32 com esse erro corrigido. Foi introduzido com o BIP350 em 2020. Endereços Bech32m também começam com `bc1`, mas são especificamente projetados para serem compatíveis com SegWit V1 (Taproot) e versões posteriores, com o script P2TR (Pay to TapRoot).