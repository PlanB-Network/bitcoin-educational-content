---
name: Trezor Shamir Backup
description: Frases Mnemonic de partilha única e de partilha múltipla no Trezor
---
![cover](assets/cover.webp)



*Crédito da imagem: [Trezor.io](https://trezor.io/)*



## Novas opções de cópia de segurança no Trezor



Desde 2023, a Trezor tem vindo a oferecer um novo formato de backup chamado ***Single-share Backup***, substituindo gradualmente a abordagem clássica baseada em BIP39 encontrada na maioria das carteiras. Ao contrário das tradicionais frases Mnemonic de 12 ou 24 palavras, este novo formato é baseado numa única frase de 20 palavras derivada de um padrão desenvolvido pela SatoshiLabs: **SLIP39**. O objetivo é melhorar a robustez e a legibilidade da cópia de segurança, permitindo simultaneamente uma migração suave para um modelo de cópia de segurança distribuída.



Este modelo distribuído é designado por ***Multi-share Backup***. Baseia-se no mesmo princípio, mas em vez de gerar uma única frase Mnemonic, divide-a em vários fragmentos denominados ***shares***, cada um dos quais é uma frase Mnemonic por direito próprio. Para restaurar a carteira, um determinado número destas *partilhas* (definido por um *limiar*) deve ser reunido. Por exemplo, num esquema de 3 de 5, quaisquer 3 *acções* das 5 restaurarão a carteira. Tenha em atenção que o sistema de backup distribuído do Trezor é diferente das carteiras Multisig. Para gastar os seus bitcoins, apenas é necessário o seu Trezor Hardware Wallet. Só é necessária uma assinatura. A distribuição aplica-se apenas ao nível da frase Mnemonic, ou seja, o backup.



![Image](assets/fr/01.webp)



Este sistema resolve o problema do ponto único de falha da frase Mnemonic sem os inconvenientes associados à gestão de um BIP39 Multisig ou passphrase. O processo de recuperação já não se baseia numa única informação, mas em várias, com a vantagem adicional da tolerância à perda graças ao limiar.



Os utilizadores que criaram um portfólio com a *Cópia de segurança de partilha única* podem mudar para a *Cópia de segurança de partilha múltipla* em qualquer altura sem terem de migrar o seu portfólio. Os endereços de receção e as contas permanecerão idênticos. O sistema *Multi-share* apenas afecta a cópia de segurança, enquanto o resto da carteira permanece inalterado.



A cópia de segurança multipartilha* está disponível no Trezor Model T, Safe 3 e Safe 5. Esta funcionalidade não é suportada pelo Trezor Model One.



**Nota importante:** O sistema *Multi-share* do Trezor é criptograficamente seguro, uma vez que utiliza o esquema *Shamir's Secret Sharing* para a distribuição. Aconselhamos vivamente a não aplicar um sistema semelhante manualmente, dividindo tu próprio uma frase clássica do Mnemonic. É uma má prática que aumenta significativamente o risco de roubo e perda dos seus bitcoins, por isso não o faça. Uma frase clássica do Mnemonic é armazenada na sua totalidade.



## Partilha do segredo de Shamir no SLIP39



O mecanismo criptográfico subjacente aos backups *Multi-share* no Trezor é o *Shamir's Secret Sharing Scheme* (SSSS). O seu princípio é o seguinte: a informação secreta (neste caso, o seed da carteira) é transformada num polinómio matemático. São então calculados vários pontos deste polinómio, cada um dos quais se torna uma ação. O segredo original é reconstruído por interpolação polinomial, reunindo um número mínimo de pontos (o limiar).



Nenhuma informação secreta pode ser deduzida de um número de partilhas inferior ao limiar, garantindo uma segurança teórica perfeita da informação secreta. Por outras palavras, mesmo um atacante com poder de computação ilimitado não pode adivinhar o seed se o limiar não for atingido.



O SLIP39 usa este esquema para distribuir a carteira seed. Cada ação é uma frase de 20 palavras, construída a partir de uma lista de 1024 palavras (diferente da lista do BIP39).



## Configurar uma cópia de segurança multipartilha num Trezor



Ao criar a sua carteira no Trezor, tem três opções diferentes:




- Utilize uma frase clássica BIP39 Mnemonic de 12 ou 24 palavras;
- Utilizar uma frase Mnemonic de partilha única (SLIP39);
- Configurar várias frases Mnemonic em Multi-share (SLIP39).



Se optar por uma frase SLIP39 Mnemonic de uma só ação, poderá fazer a atualização para uma multiacção numa data posterior sem ter de reiniciar a carteira. Por outro lado, se começar com um portfólio BIP39 clássico (frase de 12 ou 24 palavras), não poderá convertê-lo diretamente para uma Partilha Múltipla. Terá de criar uma nova carteira Multi-share a partir do zero e transferir os seus fundos da carteira antiga para a nova através de uma ou mais transacções Bitcoin. Trata-se de uma operação mais complexa e dispendiosa. Se quiser fazer esta migração, recomendo que compre um novo Trezor Hardware Wallet para evitar ter de introduzir o seu seed num software de carteiras.



Neste tutorial, veremos primeiro como configurar uma ação múltipla ao criar uma carteira e, numa secção seguinte, veremos como converter uma ação única numa ação múltipla numa carteira existente.



Se precisar de ajuda com a configuração inicial do seu dispositivo, também temos um tutorial detalhado para cada modelo Trezor:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Sobre uma nova carteira



Concluiu a configuração inicial do seu Trezor e está pronto para criar o portefólio. No Trezor Suite, clique no botão "*Criar novo Wallet*".



![Image](assets/fr/02.webp)



Selecione a opção "*Multi-share Backup*" e, em seguida, clique em "*Create Wallet*".



![Image](assets/fr/03.webp)



Aceite os termos de utilização no seu Trezor e confirme a criação da carteira.



![Image](assets/fr/04.webp)



No Trezor Suite, clique em "*Continue to backup*".



![Image](assets/fr/05.webp)



Leia atentamente as instruções, confirme-as e, em seguida, clique em "*Create Wallet backup*".



![Image](assets/fr/06.webp)



Para mais informações sobre a forma correta de guardar e gerir as suas frases Mnemonic, recomendo vivamente que siga este outro tutorial, especialmente se for um principiante:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

No Trezor, selecione o número total de acções que pretende configurar. As configurações mais comuns são 2-de-3 e 3-de-5. Para este exemplo, vou criar um 2-de-3, pelo que seleccionarei 3 acções. Cada partilha representará uma frase Mnemonic de 20 palavras.



*Para os utilizadores do Safe 5, embora o ecrã diga "*Toque para continuar*", terá de deslizar para cima para confirmar



![Image](assets/fr/07.webp)



Em seguida, confirma o limiar, ou seja, o número de acções necessárias para recuperar o acesso ao Wallet e aos bitcoins que contém.



![Image](assets/fr/08.webp)



O Trezor criará as suas várias acções (frases Mnemonic) utilizando o seu gerador de números aleatórios. Certifique-se de que não está a ser observado durante esta operação. Escreva as palavras apresentadas no ecrã no suporte físico da sua escolha. É importante que as palavras sejam numeradas e que estejam numa ordem sequencial.



Recomendo que anote cada partilha num suporte separado e que faça uma gestão cuidadosa do seu armazenamento para evitar que várias estejam acessíveis no mesmo local. Por exemplo, para uma configuração 2 de 3 como a minha, uma opção seria manter uma partilha em minha casa, outra com um amigo de confiança e a última num cofre de um banco. A escolha dos locais de armazenamento dependerá da sua estratégia de segurança pessoal.



Na parte superior do ecrã, pode ver qual a partilha que está a visualizar atualmente.



é claro que nunca se deve partilhar estas palavras na Internet, como estou a fazer neste tutorial. Este exemplo Wallet será utilizado apenas no Testnet e será eliminado no final do tutorial



![Image](assets/fr/09.webp)



Para passar para as palavras seguintes, clique na parte inferior do ecrã. Pode retroceder deslizando para baixo. Quando tiver escrito todas as palavras, mantenha o dedo no ecrã para passar à ação seguinte e repita a operação.



![Image](assets/fr/10.webp)



No final de cada gravação de partilha, ser-lhe-á pedido que selecione as palavras da sua frase Mnemonic para confirmar que as escreveu corretamente.



![Image](assets/fr/11.webp)



E já está, fez uma cópia de segurança bem sucedida da sua carteira utilizando a opção Multi-share. Pode agora continuar com o resto das instruções de configuração.



### Numa carteira de acções individuais existente



Se já tem um Trezor Wallet com um backup de partilha única (uma frase SLIP39 Mnemonic, não a frase clássica BIP39) e gostaria de melhorar a disponibilidade e a segurança do seu backup Wallet, pode configurar um sistema de partilha múltipla sem ter de transferir os seus bitcoins.



Para o fazer, ligue e desbloqueie o seu Hardware Wallet. No Trezor Suite, aceda às Definições.



![Image](assets/fr/12.webp)



Aceda ao separador "*Dispositivo*".



![Image](assets/fr/13.webp)



Em seguida, clique em "*Create Multi-share Backup*" (Criar cópia de segurança multipartilha).



![Image](assets/fr/14.webp)



Leia as instruções e, em seguida, clique em "*Create Multi-share Backup*".



![Image](assets/fr/15.webp)



Em seguida, terá de introduzir a sua frase Mnemonic atual (partilha única) no ecrã do Trezor. Selecione o número de palavras (a predefinição é 20).



![Image](assets/fr/16.webp)



Em seguida, utilize o teclado no ecrã do Trezor para introduzir cada palavra da sua frase Mnemonic atual.



![Image](assets/fr/17.webp)



Pode então escolher a configuração da sua cópia de segurança multipartilha seguindo as instruções fornecidas na secção anterior.



![Image](assets/fr/18.webp)



Depois de ter criado a sua cópia de segurança multipartilha, terá de decidir o que fazer com a sua frase original Mnemonic de partilha única. Como o portefólio Bitcoin permanece o mesmo, esta frase única permitirá sempre o acesso ao mesmo. Isto dependerá da sua estratégia de segurança, mas, em geral, é aconselhável destruir esta frase para eliminar este ponto único de falha, que é precisamente o objetivo da cópia de segurança multipartilha. Se decidir destruí-la, certifique-se de que o faz de forma segura, pois **ainda dá acesso aos seus bitcoins**.



Parabéns, está agora a par da utilização de Backups Single-share e Multi-share nas carteiras de hardware Trezor. Se quiseres levar a tua segurança Wallet um passo mais além, dá uma vista de olhos a este tutorial sobre as passphrases BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Se achou este tutorial útil, agradecia que deixasse um polegar Green abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!



## Recursos adicionais





- [SLIP-0039: Partilha de segredos de Shamir para códigos Mnemonic](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Cópia de segurança multipartilha no Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipédia: Partilha de segredos de Shamir](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).