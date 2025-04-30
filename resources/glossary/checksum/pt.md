---
term: CHECKSUM
---

A soma de controlo é um valor calculado a partir de um conjunto de dados, utilizado para verificar a integridade e a validade desses dados durante a transmissão ou o armazenamento. Os algoritmos de soma de controlo são concebidos para detetar erros acidentais ou alterações não intencionais dos dados, tais como erros de transmissão ou corrupção de ficheiros. Existem diferentes tipos de algoritmos de soma de controlo, tais como verificações de paridade, somas de controlo modulares, funções criptográficas Hash ou códigos BCH (*Bose, Ray-Chaudhuri e Hocquenghem*).


No Bitcoin, as somas de controlo são utilizadas a nível da aplicação para garantir a integridade dos endereços de receção. Uma soma de controlo é calculada a partir da carga útil do Address de um utilizador, sendo depois adicionada a esse Address para detetar eventuais erros na sua entrada. Uma soma de controlo está também presente nas frases de recuperação (mnemónicas).


> ► *É geralmente aceite utilizar o termo inglês "checksum" diretamente em francês.*