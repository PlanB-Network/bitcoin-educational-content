---
term: BIP22

---
BIP proposto em 2012 por Luke Dashjr que introduz um método JSON-RPC padronizado para interfaces de mineração externas, chamado "getblocktemplate". Com o aumento da dificuldade de mineração, desenvolveu-se o uso de software externo especializado para produzir prova de trabalho. Este BIP propõe um padrão comum de comunicação para o modelo de bloco entre nós completos e software especializado em mineração. Este método envolve o envio de toda a estrutura do bloco, em vez de apenas o cabeçalho, para permitir que o mineiro o personalize.