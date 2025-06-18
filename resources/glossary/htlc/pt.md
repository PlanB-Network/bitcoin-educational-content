---
term: HTLC
---

Significa "*Hashed Timelock Contract*". Este é um mecanismo Smart contract usado principalmente em Lightning. Também se encontra por vezes em trocas atómicas. Basicamente, o HTLC condiciona uma transferência de dinheiro à revelação de um segredo, e também inclui uma condição temporal para proteger o dinheiro do remetente no caso de uma transação falhada.


No Lightning, o HTLC permite-lhe enviar bitcoins para um nó com o qual não tem um canal direto, passando por vários canais, sem necessidade de confiança ao longo do caminho. O pagamento entre cada nó está condicionado à disponibilização de uma pré-imagem (o segredo que, depois de hash, corresponde a um valor acordado). Se o destinatário final fornecer esta pré-imagem, pode reclamar os fundos, o que permite necessariamente a cada nó intermédio reclamar os fundos em cascata.


Por exemplo, se Alice quiser enviar 1 BTC para David, mas não tiver um canal direto com ele, tem de passar por Bob e Carol, que têm canais de pagamento entre si. Eis como funciona a transação:




- David apresenta a Alice um relâmpago Invoice. Este contém o Hash $h$ de um segredo $s$ (a pré-imagem) que só David conhece. Então temos: $h = \text{Hash}(s)$ ;
- Alice cria um HTLC com Bob, que se oferece para lhe enviar 1 BTC na condição de Bob lhe fornecer um segredo $s$ (a pré-imagem) que corresponde ao Hash $h$ ;
- O Bob cria um HTLC com a Carol, que se oferece para lhe enviar 1 BTC na condição de ela fornecer o mesmo segredo $s$ ;
- A Carol cria um HTLC com o David, que oferece mais 1 BTC se ele revelar a pré-imagem $s$;
- O David revela $s$ (que só ele sabia) à Carol para receber 1 BTC. A Carol pode agora usar $s$ para obter o BTC do Bob. E o Bob, que agora sabe $s$, faz o mesmo com a Alice.


Por fim, Alice enviou 1 BTC a David através de Bob e Carol (uma ação neutra para esta última), sem que ninguém tenha de confiar uns nos outros, uma vez que tudo está protegido em cascata pelas condições dos HTLCs.


Os HTLC permitem assim as chamadas trocas "atómicas": ou a transferência é totalmente bem sucedida, ou falha, e os fundos são devolvidos. Isto garante a segurança das transacções, mesmo entre múltiplos participantes sem necessidade de confiança.