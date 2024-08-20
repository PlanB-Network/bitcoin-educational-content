---
term: BIP22
---

BIP proposto em 2012 por Luke Dashjr que introduz um método JSON-RPC padronizado para interfaces de mineração externas, chamado "getblocktemplate". Com o aumento na dificuldade de mineração, o uso de software externo especializado para produzir prova de trabalho se desenvolveu. Este BIP propõe um padrão de comunicação comum para o template de bloco entre nós completos e software especializado em mineração. Este método envolve enviar a estrutura inteira do bloco, em vez de apenas o cabeçalho, para permitir que o minerador o personalize.