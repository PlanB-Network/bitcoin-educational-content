---
name: Raspberry Pi Zero
description: Como construir um computador mínimo, isolado e de baixo custo usando um Raspberry Pi Zero e um kit de acessórios.
---
![cover](assets/cover.webp)



Se já está nas páginas do Plan ₿ Network há algum tempo, já aprendeu que uma das configurações de segurança mais defendidas, quase obrigatória, **é a gestão de fundos através do armazenamento offline das suas chaves privadas**.



Se ainda não o descobriu, ao longo deste tutorial encontrará ligações para recursos de código aberto com os quais poderá aprender mais sobre ele.



Para gerir chaves privadas offline, é necessário, portanto, um dispositivo permanentemente desconectado da rede, seja uma [carteira de hardware](https://planb.network/resources/glossary/hardware-wallet) ou um computador com airgap, dedicado a essa função específica.



Como fazê-lo se, por exemplo, não tiver a possibilidade de adquirir hardware que execute apenas esta tarefa, mas não quiser abdicar deste passo de segurança?



## A solução


E se eu lhe dissesse que pode criar um dispositivo offline sob a forma de um computador airgap que tem o tamanho e o peso de uma pen USB e custa 35 euros? Não acreditarias?



Continuar a ler.



Digo-vos mais: leiam até ao fim. A solução proposta é barata, mas não é exatamente a mais fácil. Primeiro, fica-se com a ideia geral, depois decide-se investir algum tempo numa pesquisa pessoal e escolher, com a maior tranquilidade possível, se e como se deve proceder.



## Requisitos


**1** Um [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): o PI Zero (sem qualquer sufixo) é a base para construir um computador com desempenho mínimo, mas acima de tudo carece de placas de Wi-Fi e Bluetooth, requisitos indispensáveis para o objetivo deste exercício.





- Custo**: cerca de 15,00 à data da redação deste tutorial (agosto de 2025).
- Continuidade da produção**: A Raspberry garante a produção até janeiro de 2030.



O PI Zero sem Wi-Fi e Bluetooth, infelizmente, tornou-se praticamente indisponível. Poderá encontrar mais facilmente as alternativas PI Zero W e PI Zero 2W. Neste caso, pode desativar as funções de ligação alterando o ficheiro de configuração. Depois de instalar o sistema operativo, terá de adicionar estes itens ao ficheiro de configuração:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



uma secção deste guia mostra-lhe como e onde o fazer. No entanto, se quiser ter a certeza, pode encontrar vários tutoriais na Web para remover o chip Wi-Fi com um pequeno cortador, do tipo adequado para trabalhar em placas electrónicas.



**2** Um _starter kit_ para Raspberry PI Zero: como é prática no mundo Raspberry, bare bones, sem caixa externa. Além disso, os recursos limitados de uma placa tão pequena condicionam as possibilidades de ligação com o mundo exterior.



Quando decidi avançar, encontrei [este kit](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) cheio de acessórios, para tirar o máximo partido de todo o potencial da PI Zero. De facto, o kit contém uma fonte de alimentação USB A -> micro USB Supply, um pequeno hub USB, um adaptador mini-HDMI -> HDMI, um dissipador de calor em cobre e uma caixa exterior em alumínio. O kit inclui também os parafusos e a chave allen necessários para colocar o PI Zero na nova caixa.





- Custo**: 19.99 euros.



**3** Este tutorial não exige que gaste grandes orçamentos com o computador airgap. No entanto, deve saber que vai precisar de um teclado e rato USB (estritamente com fios, evite o Bluetooth) e de um monitor. Dependendo da entrada do seu monitor, pode precisar de um adaptador de mini-HDMI, a única saída disponível no PI Zero. Por último, veja o Hard para o facto de que todos nós temos um teclado e um rato sem fios algures em casa - está na altura de os tirar do Dust.



## Orçamento suplementar



**4** Pode adquirir a fonte de alimentação original Supply na Raspberry, que custa cerca de 15,00 euros.



**5** Pessoalmente, optei por utilizar o power Supply fornecido no _starter kit_, combinando-o, no entanto, com um cabo USBA → miniUSB dito "sem dados", que custa 3,70 euros.



**6** Um cartão micro SD, com um mínimo de 32 GB de memória de massa; se for de qualidade industrial, é melhor.



**7** É necessário um sistema, um adaptador USB para micro SD, como o que se vê na imagem. O sistema operativo e a memória do seu PI Zero funcionarão, de facto, nesse suporte.



![img](assets/it/06.webp)



## Instalação do sistema operativo


Antes de fechar o seu PI Zero na caixa, recomendo que instale o sistema operativo. Assim, poderá verificar logo de início o LED que indica o funcionamento.



Para escolher e gravar o sistema operativo, optei pela forma mais fácil: usar a ferramenta `PI Imager` do Raspberry.



![img](assets/it/01.webp)



Vá então ao [Github da Raspberry](https://github.com/raspberrypi/rpi-imager/releases) para baixar a versão mais recente do Imager, escolhendo a que for mais adequada para o seu sistema operacional (v. 1.9.6 no momento da redação). Você notará que, ao lado de cada recurso, também há o hash do arquivo correspondente. Isso será útil para a verificação.



![img](assets/it/02.webp)



Recomendo que verifique o sistema operativo que vai utilizar no seu computador airgap, para sua tranquilidade pessoal. Isto dar-lhe-á a certeza de que está a trabalhar com uma versão legítima (não maliciosa) do Imager e, consequentemente, do Raspi OS.



Efectue a verificação imediatamente após a transferência, com a máquina que utiliza normalmente ligada à Internet



Em seguida, abra o terminal Linux e prepare o download, criando um diretório `raspios` útil para trabalhar com ele.



![img](assets/it/19.webp)



Descarregue o Imager para a sua distribuição Linux com `wget`.



![img](assets/it/20.webp)



Por fim, execute o comando file `sha256sum` e compare o Hash com o fornecido pelo Raspberry em seu Github.



![img](assets/it/21.webp)



Ou, se tiver o Windows, abra o Power Shell e digite o seguinte comando:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Obterá o Hash que deve corresponder ao publicado no Raspberry Github.



Depois de verificar a transferência, pode instalar o Imager no seu computador diário e abri-lo. O Imager é a ferramenta necessária para gravar o sistema operativo no micro SD, que será o "disco de sistema" do PI Zero.



O processo é extremamente simples: primeiro, escolha o dispositivo Raspberry que vai utilizar (por isso, preste atenção ao **seu modelo** de Raspi Zero), depois a versão do SO e, por fim, o ponto de montagem do cartão micro SD para o qual vai fazer o flash do SO.



### Primeiro passo



![img](assets/it/03.webp)



### Segunda etapa



![img](assets/it/07.webp)



**Atenção**: escolha o `PI OS 32-bit`, o único que funciona com o PI Zero.



### Terceira etapa



![img](assets/it/08.webp)



(Tenha o cuidado de deixar a opção _Exclude System Drive_ selecionada para evitar que lhe seja pedido para instalar o sistema operativo do Raspi no seu computador)



Quando tudo estiver configurado, o gerador de imagens perguntar-lhe-á se pretende utilizar definições personalizadas. Escolha o que pretende ou clique em _No_ para continuar com as opções predefinidas.



![img](assets/it/09.webp)



Confirmar que pretende apagar o conteúdo do micro SD



![img](assets/it/10.webp)



O gerador de imagens começa a passar o sistema operativo para o micro SD, uma barra de deslocação informa-o do progresso.



![img](assets/it/11.webp)



No final, há uma verificação automática, pelo que aconselho a não a interromper.



![img](assets/it/12.webp)



Por fim, aparece uma mensagem no ecrã e, se tudo tiver corrido bem, a mensagem é semelhante à que se lê na imagem.



![img](assets/it/13.webp)



Agora você pode realmente remover o micro SD do leitor e colocá-lo no slot do PI Zero. Ligue o pequeno Raspberry e observe o LED: esperamos que esteja verde e pisque, indicando o carregamento normal do sistema operacional, e depois permaneça aceso continuamente. Se tiver outras indicações, por exemplo se o LED piscar em frequência regular ou for vermelho, consulte as FAQ ou [as páginas do fórum de suporte](https://forums.raspberrypi.com/).



## Primeira configuração


O primeiro arranque do Raspi OS é um pouco mais lento do que o habitual, porque tem de efetuar uma série de tarefas de instalação. Mas se tudo tiver corrido bem, encontrará um ecrã de boas-vindas.



![img](assets/it/14.webp)



Clique em _Next_ para definir a região geográfica, especialmente para carregar o teclado correto. Preste especial atenção a este último.



![img](assets/it/15.webp)



Clique em _Next_ e ser-lhe-á pedido que crie o seu utilizador, anote as suas credenciais e guarde-as bem.



![img](assets/it/16.webp)



O assistente pede-lhe para escolher um navegador Web predefinido, entre o Chromium e o Firefox; pode também perguntar-lhe sobre as definições de rede Wi-Fi se estiver a trabalhar com um PI Zero W ou 2W. Vá em frente e clique em _Skip_.



A dada altura, ser-lhe-á pedido que actualize o software de bordo e o sistema operativo. Escolha _Skip_: para efeitos deste exercício, estamos de facto a construir uma máquina offline, que deve permanecer offline a partir deste momento.



Finalmente, ele pode pedir para habilitar o `ssh`, mas recuse este passo também, já que é um IP Zero airgap.



![img](assets/it/17.webp)



Não há muito mais para configurar. Quando terminar, reinicie o Raspberry para que as alterações tenham efeito.



![img](assets/it/18.webp)



## Um novo espaço aéreo para computadores


Depois de reiniciar, o seu novo computador airgap está pronto. O PI Zero mostra-lhe o novo ambiente de trabalho, com o qual pode trabalhar através da GUI ou da linha de comandos.



![img](assets/it/22.webp)



### Primeiros passos para o PI Zero W ou 2W


Se estiver a trabalhar com um Raspberry PI Zero série W ou 2W, a sua placa tem chips para Wi-Fi e Bluetooth integrados. Durante a primeira instalação, saltou a configuração da ligação, pelo que o PI Zero não está ligado à Internet. Agora pode desativar os dois chips permanentemente através do software.



De facto, o Raspi OS fornece um ficheiro `config.txt` que pode ser editado a seu gosto. O `config` está localizado na partição `boot`, no diretório `firmware`, e pode ser editado e guardado com privilégios `root`.



Abra o terminal a partir do ícone no canto superior esquerdo e ele se torna `root`.(1)



![img](assets/it/23.webp)



(1) Se o Raspi OS não lhe pediu para criar a password `root` durante os passos anteriores, recomendo que o faça agora, com o comando `passwd`. Ter o utilizador `root` a mover-se independentemente do seu utilizador pessoal pode revelar-se muito conveniente em situações de recuperação.



Com o terminal, verifique o arquivo `config.txt` e esteja preparado para editá-lo com o editor `nano`.



![img](assets/it/24.webp)



A edição deve ser feita na parte inferior de todo o `config`, após as palavras `[All]`. É neste ponto que serão adicionados os comandos `dtoverlay` mostrados no início do tutorial.



![img](assets/it/25.webp)



Guardar, fechar e reiniciar. No passo seguinte, iremos à exploração do pequeno Raspberry.



## O que esperar deste dispositivo?


De acordo com as [especificações técnicas](https://www.raspberrypi.com/products/raspberry-pi-zero/) no site da Raspberry, o PI Zero possui um processador BCM2835 de um núcleo e 512 MB de RAM, portanto não parece ser muito potente.



Como o terminal é mais leve, usaremos a linha de comando para explorar as configurações do sistema.



Quando ligar a alimentação, verá um breve ecrã com as cores do arco-íris, seguido de uma mensagem de boas-vindas da Raspberry e, no canto inferior esquerdo, mensagens do kernel relacionadas com o arranque.



Quando o ambiente de trabalho do PI OS aparecer, abra o terminal e escreva:



```bash
uname -a
```


Este comando mostra-lhe a versão do kernel atualmente em uso no ecrã, para além de outras informações.



![img](assets/it/26.webp)



Também pode ver informações sobre a CPU e o hardware escrevendo:



```bash
lscpu
```



![img](assets/it/27.webp)



E veja também `proc/mem/info`.



![img](assets/it/28.webp)



Para descobrir a versão de Debian e o nome de código do lançamento:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Utilização


Embora o desempenho pareça limitado (no papel e em comparação com a potência das máquinas actuais), o PI Zero tem um bom desempenho, especialmente como terminal.





- Primeiro pode ir aos menus principais e inspirar-se no painel _Adicionar/Remover software_, onde encontrará uma série de utilitários para programar e praticar. Lembre-se que também é possível fazer isso a partir do terminal, mas sempre com privilégios de `root`.



![img](assets/it/33.webp)





- Pode "adotar" este dispositivo offline para armazenar uma variedade de documentos confidenciais, que permanecerão acessíveis quando necessário, sem nunca serem expostos à Internet.
- Pode utilizar esta configuração para generate as suas chaves GPG de forma segura.
- Você poderia até mesmo usar este novo "brinquedinho" como um dispositivo de assinatura airgap, [seguindo os conselhos de Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Entre as carteiras que eu conheço, a única que oferece uma versão de 32 bits é a Electrum. Pois bem: o IP Zero, tal como o preparámos neste tutorial, permitir-lhe-ia manter as chaves privadas offline, a configuração do Wallet airgap que abordámos neste tutorial:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Conclusões


A configuração tem, provavelmente, um grande ponto fraco: o micro SD é um suporte que pode dar problemas. É vulnerável a uma utilização intensiva; talvez já tenha experiência com isto, por o ter utilizado no seu telemóvel. Depois de instalar todo o software que vai querer usar no Zero airgap IP, faça uma boa cópia de segurança do precioso micro SD, usando a ferramenta Raspi OS que tem disponível.



![img](assets/it/34.webp)



À medida que as suas necessidades aumentam, e com elas as suas possibilidades orçamentais, pode explorar outros Raspberry ou soluções semelhantes. Falando de memória, por exemplo, o PI 5 oferece a possibilidade de montar uma unidade M2 NVME, que é certamente mais robusta do que o microSD.



Não se esqueça de tomar notas e documentar cada passo da instalação do software utilitário que está prestes a utilizar offline. **Mais cedo ou mais tarde, será lançado um Raspi OS atualizado**, do qual quererá definitivamente tirar partido. Nessa altura, terá de apagar tudo e fazer tudo de novo (talvez com um novo micro SD 😂).



O exercício que acabámos de fazer, partindo do princípio que é também a sua primeira experiência, vai ficar na memória durante muito tempo. Nem sempre é possível dedicar hardware a operações `embedded` offline, sem descurar a atenção a uma máquina airgapped para ligar e verificar de vez em quando.



Mas conseguiu fazê-lo, parabéns! E vai poder sugerir esta solução a todos aqueles que precisam de manter os seus orçamentos baixos.