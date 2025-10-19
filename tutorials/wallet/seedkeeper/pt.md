---
name: Guardião das sementes
description: Como é que faço uma cópia de segurança do meu Wallet Bitcoin com o cartão inteligente Seedkeeper?
---

![cover](assets/cover.webp)



O Seedkeeper é um smartcard desenvolvido pela Satochip, uma empresa belga especializada em soluções de hardware para gestão e proteção de segredos digitais. Reconhecida pela sua gama de smartcards para o ecossistema Bitcoin, a Satochip concebeu o Seedkeeper como uma alternativa aos métodos tradicionais de armazenamento de frases Mnemonic.



Em termos concretos, o Seedkeeper assume a forma de um cartão inteligente multifuncional, certificado pela EAL6, com um processador seguro e uma memória inviolável (ou seja, um "secure element*"). Como o seu nome sugere, a sua função é armazenar frases e palavras-passe Bitcoin Mnemonic de forma encriptada e protegida. Com o Seedkeeper, pode generate, importar, organizar e guardar os seus segredos diretamente no componente seguro do cartão.



Na minha opinião, o Seedkeeper tem duas utilizações principais, que iremos explorar em dois tutoriais separados:




- Armazenamento de frases Bitcoin** Mnemonic: em vez de escrever as suas 12 ou 24 palavras em papel, pode importá-las para o smartcard e protegê-las com um código PIN.
- Gestão de palavras-passe**: pode criar 10 palavras-passe fortes através da aplicação Seedkeeper e armazená-las diretamente no smartcard, o que lhe permite ter um gestor de palavras-passe offline prático e fácil de utilizar.



Tecnicamente, o Seedkeeper tem uma capacidade de 8192 bytes, o que lhe permite armazenar um mínimo de 50 segredos distintos (o número exato dependerá do seu tamanho e dos metadados associados a cada um). O Seedkeeper pode ser acedido quer [através de um leitor de cartões inteligentes ligado](https://satochip.io/accessories/) a um computador, quer através da aplicação móvel com ligação NFC. Todo o sistema funciona em modo offline, sem ligação à Internet, garantindo uma superfície de ataque limitada.



![Image](assets/fr/001.webp)



Uma funcionalidade particularmente interessante é a capacidade de duplicar o conteúdo de um Seedkeeper para outro, de modo a criar uma cópia de segurança. Neste tutorial, mostraremos como fazer isso.



O Seedkeeper também é muito interessante quando combinado com um Hardware Wallet sem estado, como o SeedSigner ou o Specter DIY. Neste caso, não há necessidade de usar o computador ou o cliente móvel do Satochip. O Seedkeeper mantém o seed no seu secure element e pode ser utilizado diretamente com o dispositivo de assinatura, eliminando a necessidade de um código QR em papel. Não vou desenvolver este caso de utilização específico neste tutorial, uma vez que é objeto de outro tutorial dedicado:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Qual o caso de utilização do Seedkeeper?



Neste tutorial, apenas tratarei de casos de utilização relacionados com o Bitcoin, uma vez que é disso que trata este tutorial. Não abordaremos a funcionalidade de gestão de palavras-passe, que será objeto de outro tutorial.



Em comparação com uma simples cópia de segurança em papel da frase Mnemonic, a utilização de um Seedkeeper tem várias vantagens:





- Resistente a roubo:** O seed no seu Wallet não é acessível em texto claro. Para o extrair, é necessário conhecer o PIN do Seedkeeper. Um ladrão que se apodere do dispositivo não conseguirá fazer nada com ele sem este código.





- Repartir o risco por dois factores:** é possível dividir a segurança entre um fator digital e um fator físico. Por exemplo, se armazenar o PIN do Seedkeeper no seu gestor de palavras-passe, precisará de ter acesso a este gestor e à posse física do cartão inteligente para obter o seed (uma probabilidade de ataque significativamente reduzida).





- Gestão centralizada:** O Seedkeeper facilita a gestão de várias sementes de diferentes carteiras.





- Cópias de segurança fáceis:** basta duplicar as cópias de segurança encriptadas para outros SeedKeepers.



No entanto, há uma série de desvantagens em comparação com uma simples cópia de segurança em papel do seu seed:





- O preço:** embora modesto (cerca de 25 euros), continua a ser superior ao de uma folha de papel.





- Dependência de um dispositivo informático de uso geral:** A entrada e gestão do seed requer um computador ou smartphone, o que significa que o seu Mnemonic passa por uma máquina com uma superfície de ataque muito mais ampla do que um Hardware Wallet. Isto pode representar um risco se a estação de trabalho for comprometida. É por isso que eu não recomendo usar o Seedkeeper para armazenar o seed de um Hardware Wallet (exceto para uso sem estado sem um computador, como com o SeedSigner). O papel do Hardware Wallet é precisamente armazenar o seed num ambiente minimalista e altamente seguro. Ao introduzir manualmente o seu seed no seu computador habitual, este deixa de estar confinado ao Hardware Wallet: acaba também numa máquina de uso geral, exposta a múltiplos vectores de ataque. Por isso, é melhor usar o Seedkeeper para um Hot Wallet do que para um Cold (exceto SeedSigner / Hardware Wallet sem estado).





- O risco de perda associado ao PIN:** a inacessibilidade direta do seed, ao contrário de uma cópia de segurança em papel, oferece efetivamente uma proteção contra o roubo físico. Mas, como sempre, a segurança é um ato de equilíbrio entre o risco de roubo e o risco de perda. Se a sua cópia de segurança exigir um PIN, a perda deste código impossibilitará a recuperação da sua frase Mnemonic e, por conseguinte, o acesso aos seus bitcoins.



Tendo em conta estas vantagens e desvantagens, considero que as melhores utilizações para o Seedkeeper (para além da sua função de gestor de palavras-passe) são, por um lado, armazenar sementes das suas **carteiras de software**, uma vez que já residem no seu telefone ou computador, ou das suas carteiras de hardware sem ecrã, como o Satochip, e, por outro lado, utilizá-lo em combinação com um Hardware Wallet sem estado, como o SeedSigner, onde realmente se destaca.



Outro caso de utilização particularmente interessante para o Seedkeeper é a possibilidade de efetuar uma cópia de segurança segura e fiável dos *Descritores* das suas carteiras.



## 2. Como posso obter um guardião de sementes?



Existem duas formas principais de obter o seu Seedkeeper. Pode [comprá-lo diretamente na loja oficial da Satochip](https://satochip.io/product/seedkeeper/) ou num revendedor autorizado. Mas como [o applet do Seedkeeper é open-source](https://github.com/Toporin/Seedkeeper-Applet), também tem a opção de o instalar você mesmo em [um smart card em branco](https://satochip.io/product/blank-javacard-for-diy-project/).



Se pretender utilizar a funcionalidade de cópia de segurança do Seedkeeper, terá obviamente de adquirir dois cartões inteligentes.



## 3. Instalar o cliente Seedkeeper



Neste tutorial, vamos fazer uma cópia de segurança da nossa carteira seed no nosso Seedkeeper. O primeiro passo é instalar o software no seu computador ou smartphone. Num PC, é necessário [descarregar a versão mais recente do Satochip-Utils] (https://github.com/Toporin/Satochip-Utils/releases). No telemóvel, a aplicação Seedkeeper está disponível na [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper), bem como na [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Inicialização do guardião da semente



Inicie a aplicação e clique no botão "*Click & Scan*".



![Image](assets/fr/003.webp)



Ser-lhe-á pedido um código PIN para o seu Seedkeeper. Como se trata de um cartão novo, ainda não foi definido um PIN. Introduza um código qualquer para saltar esta etapa e clique em "*Próximo*".



![Image](assets/fr/004.webp)



Em seguida, coloque o cartão na parte de trás do seu smartphone. A aplicação detectará que o Seedkeeper ainda não foi inicializado e pedir-lhe-á que defina o código PIN do seu cartão inteligente, com um comprimento entre 4 e 16 caracteres. Para uma segurança óptima, escolha uma palavra-passe forte, o mais longa possível, aleatória e composta por uma grande variedade de caracteres. Este código PIN é a única barreira contra o acesso físico à sua frase de recuperação.



**Lembre-se também de guardar este PIN agora**, por exemplo, num gestor de senhas ou num suporte físico separado. Neste último caso, nunca guarde o suporte que contém o PIN no mesmo local que o seu Seedkeeper, caso contrário esta segurança tornar-se-á inútil. É importante ter uma cópia de segurança fiável: sem o PIN, não será possível recuperar os segredos armazenados no Seedkeeper.



![Image](assets/fr/005.webp)



Confirme o seu código PIN uma segunda vez.



![Image](assets/fr/006.webp)



O Seedkeeper está agora inicializado. Pode desbloqueá-lo introduzindo o código PIN que acabou de definir.



![Image](assets/fr/007.webp)



Será agora encaminhado para a página de gestão do seu cartão inteligente.



![Image](assets/fr/008.webp)



## 5. Registar um seed no Seedkeeper



Quando o Guardião das Sementes estiver desbloqueado, clica no botão "*+*".



![Image](assets/fr/009.webp)



Selecionar "Importar segredo*". A opção "*generate secret*" permite-lhe criar uma nova frase Mnemonic diretamente a partir da aplicação.



![Image](assets/fr/010.webp)



No nosso caso, queremos guardar o seed na nossa carteira. Clique em "*Mnemonic*".



![Image](assets/fr/011.webp)



Atribua um "*Rótulo*" a este segredo para que possa ser facilmente identificado se guardar várias informações no seu guardião de sementes.



![Image](assets/fr/012.webp)



Em seguida, introduza a sua frase de recuperação no campo previsto para o efeito. Se desejar, pode também adicionar um passphrase BIP39 ou os seus *Descritores*. Em seguida, clique em "Importar*".



![Image](assets/fr/013.webp)



*O Mnemonic apresentado nesta imagem é fictício e não pertence a ninguém. É apenas um exemplo. Nunca revele o seu próprio Mnemonic a ninguém, ou os seus bitcoins serão roubados



Coloque o Seedkeeper na parte de trás do seu smartphone.



![Image](assets/fr/014.webp)



O seu seed foi registado.



![Image](assets/fr/015.webp)



## 6. Aceder ao seu seed no Seedkeeper



Se quiser verificar a sua frase Mnemonic, pegue no seu Seedkeeper e clique no botão "*Click & Scan*".



![Image](assets/fr/016.webp)



Introduza o seu código PIN e prima "*Próximo*".



![Image](assets/fr/017.webp)



Coloque o Seedkeeper na parte de trás do seu smartphone.



![Image](assets/fr/018.webp)



Isto leva-o a uma lista de todos os seus segredos registados. Neste exemplo, quero mostrar o seed no meu portefólio "*BLOCKSTREAM App*", por isso clico nele.



![Image](assets/fr/019.webp)



Prima o botão "*Revelar*".



![Image](assets/fr/020.webp)



Faça novamente a leitura do seu Seedkeeper.



![Image](assets/fr/021.webp)



A frase Mnemonic previamente gravada é agora apresentada no ecrã.



![Image](assets/fr/022.webp)



## 7. Cópia de segurança do Seedkeeper



Vamos agora fazer uma cópia de segurança do meu Seedkeeper num segundo Seedkeeper para termos duas cópias. Esta redundância pode ser parte de uma estratégia para proteger os seus bitcoins: por exemplo, armazenar a sua frase em dois locais separados para limitar os riscos físicos, ou confiar uma cópia a um familiar de confiança como parte de um plano de herança.



Para isso, leve consigo o seu segundo guardião de sementes (lembre-se de identificar um dos dois com uma marca para evitar qualquer confusão). Comece por inicializá-lo, como descrito na etapa 4 deste tutorial. Escolha uma senha forte mais uma vez. Dependendo da sua estratégia, pode optar por uma palavra-passe diferente ou manter a mesma.



![Image](assets/fr/023.webp)



Abra a aplicação, clique em "*Click & Scan*", introduza a palavra-passe do seu Seedkeeper n.º 1 (fonte) e, em seguida, digitalize-o.



![Image](assets/fr/024.webp)



Isto leva-o para a página inicial com uma lista dos seus segredos. Clica nos três pequenos pontos no canto superior direito do Interface.



![Image](assets/fr/025.webp)



Selecione "*Fazer uma cópia de segurança*" e, em seguida, prima "*Iniciar*".



![Image](assets/fr/026.webp)



Introduza o código PIN do seu cartão de segurança (Seedkeeper n.º 2).



![Image](assets/fr/027.webp)



Em seguida, digitalizar o cartão.



![Image](assets/fr/028.webp)



Faça o mesmo com o cartão principal (Seedkeeper n.º 1) e, em seguida, clique em "*Fazer uma cópia de segurança*".



![Image](assets/fr/029.webp)



O Seedkeeper n.º 2 contém agora todos os segredos guardados no Seedkeeper n.º 1.



![Image](assets/fr/030.webp)



Pode digitalizar o seu Seedkeeper n.º 2 para verificar se os segredos foram copiados.



![Image](assets/fr/031.webp)



É tudo o que há para fazer! Agora já sabe como usar o Seedkeeper para armazenar a frase Mnemonic de um Bitcoin Wallet. Num futuro tutorial, veremos como usar o Seedkeeper para armazenar as suas palavras-passe. Convido-o também a descobrir a sua utilização combinada com o SeedSigner :



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.network/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

Neste tutorial, mencionámos várias vezes os ***Descriptores*** da sua carteira Bitcoin. Não sabe o que são? Nesse caso, recomendo que faça o nosso curso de formação gratuito CYP 201, que aprofunda todos os mecanismos de funcionamento das carteiras HD!



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f