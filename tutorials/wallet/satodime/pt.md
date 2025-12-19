---
name: Satodime
description: Saiba como utilizar o Satodime com a aplicação móvel
---
![cover](assets/cover.webp)



Este guia guia-o através da instalação, configuração e utilização da aplicação móvel Satodime. Aprenderá a tomar posse do seu cartão, a criar cofres, a adicionar fundos, a desbloquear e a recuperar as suas chaves privadas. Os anexos fornecem recursos, melhores práticas e explicações técnicas.



## Introdução



**Satodime**, desenvolvido por **[Satochip](https://satochip.io/fr/)**, é um cartão portador seguro para armazenar Bitcoin de uma forma tangível e simples. Funciona como um hardware wallet auto-custodial, onde tem controlo total sobre as suas chaves privadas sem depender de terceiros. De código aberto e com certificação EAL6+, suporta até três cofres independentes.



### Fundo do produto



O Satodime, um **carte au porteur, pertence a quem o possuir fisicamente**, sem necessidade de registo ou identificação prévia. Responde à necessidade de armazenamento seguro e portátil de bitcoins, permitindo que qualquer pessoa que possua o cartão o utilize ou transfira bitcoins, digitalizando-o através da aplicação móvel para tomar posse ou desbloquear cofres. Ao contrário de uma nota de papel, utiliza um chip seguro para selar as chaves privadas, que só são reveladas depois de abertas, tornando o cartão semelhante ao dinheiro, em que a propriedade é determinada pela posse física. Ideal para oferecer bitcoins como presentes, facilita a transferência segura de bitcoins de mão em mão, enquanto a aplicação móvel explora o NFC para uma interação acessível com o smartphone.





- Segurança**: Chaves privadas geradas e armazenadas no chip inviolável; estado visível (selado, não selado, vazio).
- Caraterísticas**: Comprar bitcoins diretamente através da aplicação (parceiro Paybis); gerir Mainnet e Testnet.
- Código aberto**: Código sob licença AGPLv3, verificável no GitHub.



### Evolução contínua



A aplicação evolui regularmente. Consulte o sítio Web da Satochip ou as lojas para obter actualizações. Por exemplo, novas blockchains ou funcionalidades de compra podem ser adicionadas. Verifique o [Satochip GitHub] (https://github.com/Toporin/Satodime-Applet) para desenvolvimentos em curso.



## 1. Pré-requisitos



Antes de começar a utilizar o **Satodime**, certifique-se de que possui os seguintes elementos:





- Smartphone compatível**: Dispositivo Android ou iOS com NFC ativado.
- Cartão Satodime**: Novo ou não inicializado.
- Ligação à Internet**: Para descarregar a aplicação.
- Conhecimentos básicos**: Compreensão das chaves privadas/públicas e dos riscos de perda (irreversíveis).
- Meio seguro**: Um local seguro para registar as chaves privadas depois de abertas (papel, metal; nunca digital).



## 2. Instalação





- Descarregar a candidatura** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Verifique o programador (Satochip) para evitar fraudes.
 - Satodime é **open-source**. Código fonte : [GitHub do Satochip](https://github.com/Toporin/Satodime-Applet).





- Instalar e iniciar a aplicação**: Ativar o NFC no telemóvel, se necessário.



![image](assets/fr/01.webp)



## 3. Configuração inicial



### 3.1 Iniciar a aplicação e efetuar a verificação



Abra a aplicação e siga o assistente. Coloque o cartão Satodime no leitor NFC do seu telemóvel (normalmente na parte de trás). Mantenha-o premido durante toda a operação para garantir uma ligação estável.





- Se o NFC não funcionar, verifique as definições do seu telemóvel.
- Um brinde confirma o sucesso: "Leitura bem sucedida".



![image](assets/fr/02.webp)



Regra geral, **todas as operações seguintes requerem uma confirmação através da leitura do cartão Satodime**



### 3.2 Tomada de posse do cartão (*Ownership*)



Para a primeira utilização, tornar-se o proprietário do cartão para o proteger:





- Clique em "*Take Ownership*" na aplicação.
- Confirmar a operação: este procedimento gera uma chave de proprietário única.
- Digitalize o mapa novamente para aplicar as alterações.
- Aviso**: Este passo é irreversível. Consulte [o artigo sobre *propriedade*] (https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Criar um ambiente seguro



O Satodime suporta até 3 cofres. Crie um para guardar bitcoin:





- Selecione um cofre vazio (por exemplo, Cofre 01).
- Selecionar a cadeia de blocos (Bitcoin).
- Clicar em "*Create & Seal*".
- Digitalizar o cartão para o generate e selar a chave privada (desconhecida até ser aberta).
- Parabéns**: O seu cofre está agora selado e pronto a receber fundos.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Adicionar fundos



Uma vez selado, carrega o cofre com bitcoins:





- Selecionar o cofre.
- Clique em "*Adicionar fundos*".
- Copiar o endereço público ou ler o código QR.
- Enviar fundos de outro wallet.
- Verificar o saldo após a confirmação na cadeia de blocos.
- Opção de compra: Clique em "*Comprar*" para comprar diretamente através do Paybis (Visa, Mastercard, etc.). Taxas aplicáveis.



![image](assets/fr/06.webp)



## 6. Desbloquear um cofre



Para aceder à chave privada e transferir os fundos para outro local, abra o cofre:





- Selecionar o cofre selado.
- Clicar em "Desbloquear".
- Confirmar o aviso: esta operação é irreversível.
- Digitalize o cartão para o desbloquear.
- O cofre está definido para "*Unsealed*"; a chave privada pode agora ser vista/exportada.
- Aviso**: Uma vez aberta, a chave privada fica acessível. Se alguém se apoderar do seu smartphone, pode aceder a esta chave e, assim, recuperar os fundos do seu cofre (irreversível).



![image](assets/fr/07.webp)



## 7. Recuperar a chave privada



Depois de abrir o selo, exportar a chave para utilização noutro wallet :





- Certifique-se de que se encontra num ambiente seguro.
- Clique em "*Mostrar chave privada*".
- Selecionar o formato: Legado, SegWit, WIF, etc.
- Copiar a chave ou digitalizar o código QR.
- Segurança**: Nunca partilhe a sua chave privada. Guarde-a offline.
- Importá-lo para um programa informático wallet compatível com a gestão de fundos (Sparrow Wallet ou Electrum, por exemplo).



![image](assets/fr/08.webp)





## 8. Repor a bagageira



A reposição do cofre elimina irreversivelmente a chave privada associada. Por outras palavras, se não tiver assegurado uma cópia da sua chave privada ou se não a tiver importado para outro wallet, a reposição do cofre causará a perda irreversível dos fundos nele contidos.



![image](assets/fr/09.webp)



A reposição da bagageira deixa a ranhura vazia e pronta para receber uma nova bagageira.



## 9. Transferir a propriedade



Para - por exemplo - oferecer bitcoins através da Satodime, é necessário :




- Assumir a propriedade do cartão,
- Criar um cofre Bitcoin,
- Transferir satss para lá,
- Transferir a propriedade do cartão: a pessoa seguinte a digitalizar o cartão torna-se o seu proprietário,
- Entregue o cartão Satodime a uma pessoa à sua escolha e convide-a a descarregar a aplicação e a digitalizar o cartão para se apropriar dele - e assim aceder aos bitcoins "armazenados" no mesmo.



![image](assets/fr/10.webp)




## APÊNDICES



### A1. Melhores práticas



Para utilizar o **Satodime** de forma segura :





- Proteger o cartão**: Tratar o cartão como dinheiro; perda = perda de fundos se não for o proprietário.
- Cópia de segurança das chaves**: Depois de retirar o selo, registar as chaves privadas num suporte físico seguro. Nunca digital.
- Verificar o estado**: Efetuar sempre a leitura para confirmar a propriedade do cartão e o estado selado/não selado dos cofres.
- Confidencialidade**: Utilizar novos endereços; evitar trocas centralizadas para transferências.
- Actualizações**: Mantenha a aplicação actualizada através das lojas.
- Recuperação**: Se o cartão for perdido mas tiver dono, os fundos estão na cadeia de blocos; utilize a chave privada se não estiver selado.



### A2. Recursos adicionais



Específico para Satodime :




- [Produto Satodime](https://satochip.io/fr/product/satodime/)
- [Guia móvel] (https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy] (https://planb.academy/) para tutoriais sobre auto-custódia, chaves privadas, etc.



**Guarde a sua frase de recuperação** :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tutorial sobre o Satochip (o primeiro produto da marca) :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Tutoriais do guardião de sementes:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Sobre a Satochip



**Ligações oficiais** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Apoio: info@satochip.io



**A Satochip** é uma empresa belga que desenvolve soluções de hardware e software para gerir e armazenar bitcoins e outras criptomoedas. O seu principal produto, o hardware Satochip wallet, é um cartão NFC equipado com um secure element com certificação EAL6+. Complementado pelo Seedkeeper, uma frase mnemónica e um gestor de segredos, e pelo Satodime, um cartão ao portador, o Satochip oferece uma gama completa adaptada às necessidades dos utilizadores. Os seus dispositivos, alimentados por software de código aberto, têm como objetivo democratizar a segurança na Bitcoin.