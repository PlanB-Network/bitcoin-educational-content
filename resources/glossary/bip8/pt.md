---
term: BIP8

---
Desenvolvido após os debates sobre o SegWit, que usou o BIP9 para sua ativação, o BIP8 é um método de ativação de soft fork que incorpora nativamente um mecanismo automático de UASF (*User-Activated Soft Fork*). Como o BIP9, o BIP8 utiliza a sinalização do minerador, mas adiciona o parâmetro `LOT` (*Lock-in On Time out*). Se `LOT` for definido como `true`, após a expiração do período de sinalização sem atingir o limite necessário, um UASF é automaticamente acionado, forçando a ativação do soft fork. Esta abordagem obriga os mineiros a serem cooperativos ou arriscam uma UASF imposta pelos utilizadores. Além disso, ao contrário do BIP9, o BIP8 define o período de sinalização com base na altura do bloco, eliminando potenciais manipulações através da taxa de hash por parte dos mineiros. O BIP8 também permite definir um limiar de votação variável e introduz um parâmetro para uma altura mínima de bloco para ativação, dando aos mineiros tempo para se prepararem e sinalizarem o seu acordo antecipadamente sem estarem necessariamente prontos. Quando um soft fork é ativado via BIP8 com o parâmetro `LOT=true`, este utiliza um método muito agressivo contra os mineiros que são imediatamente colocados sob a pressão de uma potencial UASF. De facto, deixa-lhes apenas duas opções:


- Seja cooperante e facilite assim o processo de ativação;
- Não cooperar, caso em que os utilizadores executam automaticamente uma UASF para impor o soft fork.