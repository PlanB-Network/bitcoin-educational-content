---
name: SAFU Ninja
description: Salve o seu seed com o método SAFU Ninja
---

![cover](assets/cover.webp)


## 1. Introdução



O método **Ninja SAFU** é uma solução **DIY (Do It Yourself)** que lhe permite criar uma cópia de segurança **sustentável, segura e discreta** da sua **frase seed** (uma frase Mnemonic de 12 ou 24 palavras definida pela norma **BIP-39**). Esta frase é essencial para restaurar um Bitcoin Wallet ou qualquer outro Wallet compatível.



Em vez de escrever as suas palavras em papel - um método simples mas vulnerável - gravá-las-á em **anilhas de aço inoxidável**, montadas numa **Bolt**. O resultado é uma cópia de segurança compacta, resistente ao fogo, à corrosão, à água e aos choques. Ao contrário do papel, que pode ser destruído pelas chamas, pela humidade ou pelo tempo, o aço inoxidável garante uma preservação a longo prazo, mesmo em condições extremas (até 1300°C ou 20 toneladas de pressão).



A abordagem Ninja SAFU oferece várias vantagens:





- **Confidencialidade**: Não está a comprar um produto identificado como sendo destinado ao backup de criptomoedas. Os componentes são padrão (anilhas, parafusos, caixa metálica), disponíveis em lojas de ferragens, o que reduz o risco de ser visado no caso de uma fuga de dados de um fornecedor especializado.





- **Acessibilidade**: Esta solução custa entre **15 e 140 EUR**, consoante as ferramentas de que já dispõe.





- **Fiabilidade**: Testado desde 2020, o método foi experimentado e testado por especialistas em segurança, como [Jameson Lopp] (https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/), que o submeteram a rigorosos testes de esforço (calor extremo, corrosão, pressão mecânica).



Este guia passo-a-passo irá mostrar-lhe como fazer o seu próprio backup Ninja SAFU, para melhor proteger os seus bitcoins contra perda ou destruição. Se quiser saber mais sobre como fazer backup e proteger uma frase seed, consulte os apêndices.




## 2. Hardware



Para criar uma cópia de segurança Ninja SAFU, são necessários os seguintes componentes, todos disponíveis em lojas de hardware ou online.



### 2.1 Materiais necessários





- **Anilhas de aço inoxidável (recomenda-se M8)**:
- **Material**: Aço inoxidável (por exemplo, 304 ou V4A para maior resistência à corrosão)
- **Tamanho**: M8 (diâmetro interior 8 mm, diâmetro exterior ~24 mm). As anilhas M6 são demasiado pequenas e difíceis de gravar.
- **Quantidade**: 12 ou 24 anilhas para uma frase seed padrão, mais anilhas opcionais (ver secção 3.4) e cerca de dez para testes ou erros.





- **Aço inoxidável Bolt e porca (M8)**:
- **Especificações**: Bolt 2,5 a 5 cm de comprimento, dependendo do número e espessura das anilhas, diâmetro 8mm. Um parafuso de orelhas facilita a abertura sem ferramentas, mas também pode ser utilizada uma simples porca.



![image](assets/fr/03.webp)





- **Conjunto de punções para letras e números (3 mm ou 6 mm)**:
- **Especificações**: os caracteres com 6 mm de altura facilitam a legibilidade e podem ser preferíveis se parte das letras estiver degradada. Escolha um conjunto robusto para utilização repetida.



![image](assets/fr/04.webp)





- **Martelo ou marreta**:
    - É preferível utilizar uma marreta para obter uma força de estampagem suficiente e precisa





- **Bigorna ou superfície resistente**:
 - Uma superfície espessa, Hard (por exemplo, bigorna de 1 kg ou pedra de calçada de 10 cm) para absorver os choques.



Se não quiser investir num conjunto de punções, pode também gravar as suas anilhas com uma caneta de gravação. Esta solução é muitas vezes mais económica, mas requer mais cuidado para obter um resultado satisfatório.



### 2.2 Ferramentas opcionais





- **Dispositivo de estampagem**: Segura a anilha e guia o punção, permitindo uma estampagem precisa e limpa, uma melhor orientação e um espaçamento uniforme das letras



![image](assets/fr/05.webp)





- **Dispositivos de selagem**: Bolsa selada ou tira de selagem



![image](assets/fr/06.webp)





- **Recipiente hermeticamente fechado**: Para armazenar o bloco de anilhas



![image](assets/fr/07.webp)


### 2.3 Segurança





- Recomenda-se o uso de **luvas** e **óculos de proteção**.
- **Chave de tubos** na qual se introduz o punção, de modo a segurar o punção com a chave de tubos e não com os dedos.



### 2.4 Quantidades e custos estimados





- **Quantidade para um backup de 24 palavras**: 24 anilhas (mínimo), 1 Bolt, 1 porca de orelhas, 1 conjunto de punções, 1 martelo/masseta, 1 bigorna/suporte.





- **Custo total**:
 - Anilhas e parafusos/porcas: ~ 15 EUR
 - Conjunto de punções: ~ 45 EUR
 - Estojo de proteção: ~ 55 EUR
 - Com todos os acessórios: ~ 140 EUR





- Ver anexo para exemplos de equipamento.




## 3. Instruções passo a passo



1. **Preparando-se:**




 - Local privado, sem câmaras (incluindo smartphones)
 - Superfície robusta e amortecedora de choques
 - Luvas e óculos de proteção
 - Limpar toda a gordura e sujidade das máquinas de lavar
 - Prática em anilhas de teste


2. **Queimar palavras Mnemonic** :




    - Gravar a palavra completa num dos lados. Não se limite às primeiras 4 letras, para o caso de a 4ª estar danificada.
    - Bater firmemente com o martelo, segurando o punção com uma chave de tubos


3. **Numerar as anilhas** :




    - No mesmo lado, gravar a palavra número de posição, essencial se as anilhas se soltarem.


4. **Informações de registo** (facultativas e recomendadas) :




    - Gravar a palavra redundante no outro lado do disco
    - Gravar um identificador Wallet numa anilha adicional
    - Grave o caminho de derivação da conta que está a utilizar numa máquina de lavar adicional. Pode encontrar esta informação nas definições do seu software de carteira. Por exemplo, para uma carteira Taproot padrão, o caminho de derivação padrão será: `m / 86' / 0' / 0' /`
    - Introduza o código PIN para desbloquear o seu Hardware Wallet, ou as palavras anti-phishing se estiver a utilizar um COLDCARD.


5. **NÃO queimar passphrase :**




 - Se utilizar um passphrase, certifique-se de que não o anota no mesmo cartão que o seu Mnemonic. O passphrase foi concebido para proteger o seu Wallet em caso de roubo do Mnemonic. Mais informações em anexo.


6. **Verificar a legibilidade** :




    - Certifique-se de que todas as palavras e números são claros e legíveis.


7. **Montar as anilhas** :




    - Enrosque as anilhas no Bolt pela ordem dos números.
    - Opcional: adicionar anilhas brancas às extremidades.
    - Aparafusar o parafuso de orelhas para fixar a bateria.
    - Apertar firmemente para aumentar a proteção contra a água, o fogo e o esforço mecânico.


8. **Cópia de segurança de teste** :




    - A partir da sua nova cópia de segurança, tente recuperar a sua carteira
- **Selagem da cópia de segurança** (opcional e recomendada):
 - Em tiras seladas ou em bolsas seladas.
 - Se utilizar uma bolsa, anote o seu número de identificação único, de modo a poder verificar se se trata da bolsa correta e não de um engodo que substitui a original.




## 4. Armazenamento



### 4.1 Escolher um local adequado



Armazene a sua cópia de segurança num **local discreto**, fora da vista e acessível para verificações periódicas. Escolha um armazenamento **à prova de fogo e à prova de água**, em casa ou num local sob o seu **controlo exclusivo**.



Evite locais onde esteja dependente de terceiros (cofre bancário, notário): perderá o acesso autónomo aos seus fundos, o que vai contra os princípios de soberania da Bitcoin.



Nunca revele que utiliza um método como o SAFU Ninja. A discrição é um Layer da segurança por si só.



### 4.2 Redundância



Se necessário, criar **várias cópias** e armazená-las em **diferentes localizações geográficas**.


Mesmo que os materiais escolhidos para o seu aparelho sejam resistentes à água e ao fogo, não conseguirá aceder-lhe se estiver enterrado sob m3 de escombros na sua casa e será muito difícil, se não impossível, recuperá-lo.




## 5. Acompanhamento e manutenção



Mesmo quando bem guardada, a sua cópia de segurança precisa de ser **verificada regularmente**:





- Fora da vista, inspecionar a reserva **uma ou duas vezes por ano**.
- Em caso de **degradação das gravações**, recriar uma nova cópia de segurança, **testá-la** e, em seguida, **destruir cuidadosamente a cópia antiga**.
- Se a cópia de segurança estiver numa bolsa selada :
 - Verificar o seu início de sessão
 - Verificar a sua integridade
 - Abra regularmente o envelope para inspecionar o estado das gravuras e, se tudo estiver bem, coloque a cópia de segurança num novo bolso




**FIQUEM SEGUROS!**


![image](assets/fr/08.webp)




## APÊNDICES



### A.1 Guardar a frase de recuperação



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### A.2 Compreender o passphrase BIP39



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

### A.3 Como funcionam as carteiras Bitcoin



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### A.4 Classificação do método SAFU Ninja



De acordo com Jameson Lopp:





- [Relatório](https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/) sobre o método SAFU Ninja





- Quadro de comparação [completo] (https://jlopp.github.io/metal-Bitcoin-storage-reviews/?ref=blog.lopp.net)





- Quadro parcial :


![image](assets/fr/09.webp)



### A.5 Exemplo de hardware





- **Anilhas** para
 - [Titan](https://pleb.style/fr-fr/products/disques-de-seed-supplementaires-titan-Wallet)
- **Anilhas + porca + estojo de proteção** (para anilhas)
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-premium-acier-steel-Wallet-backup?variant=50022696419664)
 - [TerraSteel](https://pleb.style/fr-fr/products/terrasteel-Wallet-plebstyle-acier-backup)
- Conjunto de punções
 - [PlebStyle](https://pleb.style/fr/products/schlagstempelset-a-z-0-9-3mm)
- **Base de digitação**
 - [PlebStyle](https://pleb.style/fr/products/schlagunterlage-10cm-x-10cm-x-1-5cm)
- **Dispositivo de roscar** (guia)
 - [TerraSteel](https://pleb.style/fr-fr/products/zubehor-einschlag-vorrichtung?_pos=1&_sid=2767fd66f&_ss=r)
- Dispositivo de vedação
 - [Bolsa selada] (https://pleb.style/fr/products/zubehor-5x-sicherheitstasche-tamper-evident)
 - [Tiras de vedação] (https://pleb.style/fr/products/zubehor-5x-siegel-streifen-fur-dein-seed-backup)
- **Kit completo**
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-diy-kit-premium-seed-backup-steelwallet-plebstyle?pr_prod_strat=e5_desc&pr_rec_id=aa9f36359&pr_rec_pid=8728733155664&pr_ref_pid=8730877788496&pr_seq=uniform)
 - [TerraSteel](https://pleb.style/fr-fr/products/kopie-von-terrasteel-Wallet-starter-kit)



Nota: As ligações a lojas em linha são fornecidas apenas para fins informativos.


Não existe qualquer parceria comercial entre a Plan B e os vendedores e fabricantes acima referidos.


A Plan B não pode ser responsabilizada por defeitos, variações de preço ou problemas relacionados com a qualidade ou entrega dos produtos. **DYOR**




### A.6 Créditos fotográficos



https://pleb.style/fr/


https://x.com/lopp/status/1463155802345193475


https://bitcointalk.org/index.php?topic=5389446.0


https://x.com/econoalchemist/status/1329271981712289797


https://www.waivio.com/@themarkymark/create-your-ownown-metal-seed-key-backup


https://github.com/minibolt-guide/minibolt/blob/main/bonus/Bitcoin/safu-ninja.md