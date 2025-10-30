---
name: Braiins Mini Miner
description: Fazer Mining facilmente a partir de casa.
---
![cover](assets/cover.webp)



## Introdução



O Mini Miner braiins BMM 100 é um produto criado pela Mining pool Braiins. Este dispositivo tem um design atrativo e é extremamente silencioso. Produz 1,1 Th/s de potência de computação e consome cerca de 40 watts. Ao contrário de outros dispositivos, não é de código aberto, mas é muito fácil de instalar, bastando apenas alguns cliques! O Mini Miner BMM 100 é a primeira versão lançada. Agora está em produção a versão 2, chamada BMM 101, que difere da primeira por ter um ecrã maior e a presença de Wi-Fi, mas os procedimentos de instalação são os mesmos.



Também pode encontrar informações muito mais importantes consultando o guia completo diretamente no [sítio do fabricante] (https://braiins.com/hardware/mini-Miner-bmm-100).



## Visão geral do BMM 100



o dispositivo assemelha-se a um paralelepípedo com um ecrã na frente



![image](assets/en/01.webp)



uma ventoinha na parte superior



![image](assets/en/02.webp)



enquanto na parte de trás temos: o orifício para a alimentação, espaço para um cartão SD (que pode ser necessário para quaisquer actualizações), um pequeno botão que diz `IP REPORT` que lhe permite saber o IP Address do mini Miner, que Address é necessário para aceder ao painel de instrumentos do dispositivo. Uma vez premido o botão, o IP Address é apresentado durante cerca de 5 segundos, depois desaparece e volta a aparecer o ecrã de configuração. No entanto, se precisar de alterar algumas definições, basta premir novamente o botão em questão e o IP Address reaparecerá no ecrã. Continuando com a lista, encontramos uma porta Ethernet e um acesso para efetuar uma reinicialização do dispositivo, para a qual será necessário agarrar num pino e mantê-lo premido durante 10 segundos, de modo a reiniciar todas as definições do mini Miner. Por fim, encontramos dois indicadores luminosos, um Green e outro vermelho, que nos indicam o estado do Miner.



![image](assets/en/03.webp)



## Ligar o Mini Miner



É necessário ligar o dispositivo à Internet através da ethernet, mas, com a nova versão (BMM 101), isso já não é necessário. Voltando a este mini Miner, uma vez localizada a localização, será necessário ligá-lo primeiro à linha de Internet e depois à alimentação: o dispositivo ligar-se-á automaticamente e mostrará o seu IP Address no ecrã.



## Configuração



Temos de abrir um browser e introduzir o IP Address que nos mostra o mini Miner na barra de pesquisa. Recordo que, para encontrar o dispositivo na rede, terá de ser local, pelo que terá de ter o computador que está a utilizar ligado à mesma rede que o mini Miner. Assim que introduzirmos o IP Address, carregamos no enter e aparece no ecrã a página de início de sessão no sistema operativo do mini Miner, que é o Braiins OS.



![image](assets/en/06.webp)



Para iniciar a sessão, terá de introduzir `root` como nome de utilizador, podendo deixar a palavra-passe em branco. Clique em login e o seu mini painel de controlo do Miner aparecerá.



![image](assets/en/07.webp)



## Definições gerais



Vamos para Sistema



![image](assets/en/24.webp)



nas definições, encontramos algumas definições gerais, como o tema (claro ou escuro), o idioma, o fuso horário e a alteração da palavra-passe.



![image](assets/en/25.webp)



Se formos a "Mini Miner Screen", temos as definições do nosso mini Miner, como a apresentação do ecrã. Podemos escolher se queremos mostrar a hora, ou o preço do Bitcoin, ou o ecrã com a informação do estado da máquina, como o produto Hash, a temperatura, os watts consumidos, etc. Aqui cabe ao utilizador escolher o que pretende ver no ecrã; podemos também alterar o brilho do ecrã, definir o modo noturno e apresentar a hora no formato de 12 ou 24 horas.



![image](assets/en/26.webp)



Depois de efetuar as alterações, clique em "Guardar alterações" e verá as alterações no ecrã do seu dispositivo



![image](assets/en/27.webp)



## Ligação ao Mining pool



Agora ainda não estamos operacionais, porque temos de nos ligar a uma piscina para iniciar o Mining, pelo que temos de ir a "Configuration" (Configuração)



![image](assets/en/08.webp)



e a primeira entrada é apenas `Pools`.



![image](assets/en/09.webp)



Aqui teremos de decidir qual a piscina a utilizar. Neste tutorial, vou mostrar-vos duas opções. A primeira é ligar-nos à Mining pool Braiins, que também é utilizada por mineiros profissionais, como pode ver neste tutorial:



https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

A segunda opção é ligar-nos a um Mining pool que mina a solo, como o Public Pool, seguindo este guia para o fazer:



https://planb.academy/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Piscina Braiins



Para nos ligarmos a esta pool, temos de criar uma conta. Esta pool também efectua pagamentos em Lightning Network, pelo que poderemos receber alguns Sats por dia. Para isso, temos de criar um raio de Address para receber as recompensas. Se não sabe como criar uma conta no braiins pool ou como configurar o seu relâmpago Address, pode seguir este guia:



https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Uma vez feito isso, estamos no painel de controlo do pool Braiins. O que temos de fazer é dizer à pool que queremos ligar-nos a um dos nossos mineiros, por isso, no lado esquerdo do ecrã, encontrará uma série de entradas. Temos de ir a "trabalhadores"



![image](assets/en/04.webp)



e temos de clicar no botão roxo à direita que diz "Ligar trabalhadores"



![image](assets/en/05.webp)



Aqui aparece a janela com a informação de que necessitamos para ligar o nosso mini Miner à piscina. Aqui a única alteração que podemos fazer é escolher Stratum V2. Para saber o que é Stratum v2 veja esta entrada no [glossário](https://planb.academy/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Agora precisamos de copiar esta cadeia que começa com stratumv2. Por isso, clicamos no pequeno símbolo "copy" (copiar) e, em seguida, vamos para o painel de controlo do nosso mini Miner que deixámos em configuration and pools (configuração e pools). Clicamos em "add new pool



![image](assets/en/11.webp)



e cole a cadeia de caracteres que copiámos no espaço abaixo do URL do agrupamento.



![image](assets/en/12.webp)



Agora temos de adicionar o nome de utilizador e a palavra-passe. Voltemos ao painel de controlo da piscina. Por baixo, temos também um userID e uma palavra-passe. O userID e o nosso nome de utilizador, o que demos quando criámos a conta, mais o nome do Miner que queremos colocar. Pode decidir se quer ou não dar um nome ao dispositivo que está a ligar à pool, é opcional, mas é aconselhável colocá-lo, por isso, se ligar vários dispositivos, será mais fácil identificá-los de imediato. Se não quiser colocar nada, pode deixar `workerName`.



![image](assets/en/13.webp)



Em seguida, vamos ao nosso mini Miner e introduzimos o nome de utilizador. Aqui introduzimos, no meu caso, "finalstepbitcoin", que é o meu ID de utilizador, ponto miniminer. Este é o nome que decidi dar ao dispositivo. Se não quiser dar um nome, basta escrever userid dot workername. No meu caso, seria finalstepbitcoin.workername. Depois de introduzires o nome de utilizador, podes escolher uma palavra-passe e escrevê-la no campo em branco. Também podes colocar anithing123, que é a que também aparece no ecrã da piscina, mas ele quer simplesmente indicar que podes colocar a password que quiseres.



Depois de ter introduzido todos os dados, tem de premir o botão de guardar à direita (o que tem a forma de uma disquete) e, desta forma, configurou os dados da piscina no mini Miner.



![image](assets/en/14.webp)



Agora, tem de voltar ao painel de controlo da piscina e clicar em "Ligado! Voltar atrás"



![image](assets/en/15.webp)



Ligámos o nosso mini Miner ao pool de braiins! Já o podem ver na lista de trabalhadores. Se não aparecer, basta fazer um refresh e esperar alguns momentos. Quando aparecer, verifique se tem o estado "OK" com uma marca de verificação Green.



![image](assets/en/17.webp)



se voltarem ao painel de controlo, devem começar a ver movimento no gráfico e a ver o Hashrate do nosso dispositivo. Isto significa que a piscina está a receber o nosso trabalho e, por conseguinte, estamos, para todos os efeitos, a minar.



![image](assets/en/16.webp)



### Piscina pública



Através deste pool é possível tentar a sorte e minerar sozinho, apoiando-se num pool. Neste caso, não receberemos recompensa, mas receberemos a recompensa total se conseguirmos minerar um bloco. Vamos então ligar-nos à piscina pública, uma piscina apenas para Mining que é completamente open source. Abrimos uma nova janela no navegador e vamos para [web.public-pool.io] (https://web.public-pool.io/#/).



![image](assets/en/18.webp)



aparece uma página com todas as informações de que necessitamos. Em seguida, copiamos para lá o estrato Address



![image](assets/en/19.webp)



depois voltamos ao painel de controlo do nosso mini Miner, vamos à configuração e aos pools, clicamos em adicionar novo pool (o mesmo processo que vimos acima) e colamos o 'stratum Address sob o url do pool.



![image](assets/en/20.webp)



Voltemos agora à página do pool e vejamos que, como nome de utilizador, temos de introduzir um Bitcoin Address, que será aquele em que receberemos a recompensa no caso de minarmos um bloco, depois um ponto e, em seguida, o nome do nosso dispositivo, como fizemos anteriormente com o Braiins Pool, enquanto a palavra-passe pode ser escolhida por nós próprios.



![image](assets/en/21.webp)



Voltamos ao mini Miner e, em nome de utilizador, colamos um Address Bitcoin seguido de ponto e o nome, vou colocar `miniminer`. Na palavra-passe, em vez disso, vou colocar test, pode introduzir o que quiser.



![image](assets/en/22.webp)



Agora, guardamos as definições e desactivamos a piscina Braiins.



![image](assets/en/23.webp)



Ótimo! Agora somos Mining na piscina pública!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)