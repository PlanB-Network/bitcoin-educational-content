---
term: HASHCASH

---
O HashCash é um sistema de prova de trabalho concebido por Adam Back em 1997 para combater o spam e os ataques DoS. Baseia-se no princípio de que um remetente deve executar uma tarefa computacional (especificamente, encontrar uma colisão parcial numa função hash criptográfica) para provar o seu trabalho. Esta tarefa é dispendiosa em termos de tempo e energia para o remetente, mas a verificação do resultado pelo destinatário é rápida e simples. Este protocolo revelou-se particularmente adequado para combater o spam nas comunicações por correio eletrónico, uma vez que é minimamente oneroso para os utilizadores legítimos e constitui um obstáculo significativo para os autores de spam. Com efeito, o envio de uma única mensagem de correio eletrónico requer alguns segundos de computação, mas a replicação desta operação milhões de vezes torna-se extremamente dispendiosa em termos de energia e de tempo, o que muitas vezes anula o interesse económico das campanhas de spam, sejam elas para fins de marketing ou maliciosas. Além disso, permite a preservação do anonimato do remetente.

O HashCash foi rapidamente adotado pelos cypherpunks que procuravam desenvolver um sistema de moeda eletrónica anónima sem intermediários. De facto, a inovação de Adam Back introduziu pela primeira vez o conceito de escassez no mundo digital. O conceito de prova de trabalho encontra-se depois em vários sistemas de moeda eletrónica anteriores à Bitcoin, incluindo:


- b-money de Wei Dai publicado em 1998;
- R-POW, de Hal Finney, publicado em 2004;
- BitGold por Nick Szabo publicado em 2005.

O princípio do HashCash também se encontra no protocolo Bitcoin, onde é utilizado como um mecanismo de proteção contra ataques Sybil.