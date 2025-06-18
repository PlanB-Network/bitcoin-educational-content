---
term: LIBSECP256K1
---

Biblioteca C de alto desempenho e alta segurança para assinaturas digitais e outras primitivas criptográficas na curva elíptica `secp256k1`. Uma vez que esta curva nunca foi amplamente utilizada fora do Bitcoin (ao contrário da frequentemente preferida curva `secp256r1`), esta biblioteca pretende ser a referência mais abrangente para o seu uso. O desenvolvimento da libsecp256k1 foi primariamente orientado para as necessidades do Bitcoin, e as caraterísticas destinadas a outras aplicações podem ser menos testadas ou verificadas. O uso apropriado desta biblioteca requer atenção cuidadosa, para garantir que ela seja adequada para os propósitos específicos de outras aplicações que não o Bitcoin.


A biblioteca libsecp256k1 oferece uma variedade de funcionalidades, incluindo:




- Assinatura e verificação ECDSA-secp256k1 e geração de chaves criptográficas ;
- Operações aditivas e multiplicativas em chaves secretas e públicas ;
- Serialização e análise de chaves secretas, chaves públicas e assinaturas ;
- Assinatura e geração de chaves públicas em tempo constante com acesso constante à memória;
- E uma série de outros primitivos criptográficos.