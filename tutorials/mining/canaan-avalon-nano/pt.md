---
name: Canaan Avalon Nano 3S
description: Configurando seu ASIC Avalon para solomining ou pooling Miner
---

![cover](assets/cover.webp)



Neste tutorial, vamos ver como configurar o Canaan Avalon Nano 3S, para uma utilização doméstica fácil do Miner.



Até agora, as máquinas ASIC (*Application Specific Integrated Circuit*) especificamente concebidas para realizar uma determinada tarefa - neste caso, o cálculo Hash (SHA-256) para Miner de Bitcoin - eram particularmente inadequadas para uso doméstico. O incómodo do ruído, o calor gerado e a necessidade de adaptar a instalação eléctrica para suportar a enorme potência destes dispositivos impediam a maioria de nós de participar.



Atualmente, a Canaan, um dos principais fabricantes de máquinas ASIC, decidiu abordar o mercado dos particulares que pretendem ter Miner em casa, propondo uma gama de produtos relativamente silenciosos e muito fáceis de instalar (plug & play).



Estes dispositivos são comercializados como um aquecedor auxiliar, no caso do **Avalon Nano 3S (140W)**, ou como um mini radiador com uma potência de **800W**, no caso do **Avalon Mini 3**.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Note-se que a diferença de preço em relação aos aquecedores tradicionais de potência equivalente não lhe permite, na grande maioria dos casos, obter um lucro financeiro. Os satoshis gerados pela atividade do Mining nunca compensarão esta diferença de preço, a menos que tenha acesso a eletricidade gratuita (excedente) ou muito barata.



Na minha opinião, estes dispositivos devem ser vistos mais como uma forma simples de Miner em casa para aqueles que o desejam fazer por razões pessoais: *obter Satss sem KYC / jogar na "lotaria" solominando / participar na descentralização do Hashrate, etc.*, enquanto beneficia **como bónus** do calor gerado para aquecer o seu quarto no inverno. Mas não como uma forma de poupar dinheiro, pelo menos na maioria dos casos (países ocidentais).



## Desembalagem e caraterísticas



Primeiro, vamos ver o que está dentro da caixa do Avalon Nano 3S.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Depois de abrir a caixa, encontrará uma manga de cartão que contém um recetor WIFI que, como veremos mais tarde, terá de ligar à porta USB do dispositivo para permitir a ligação à sua rede local. Inclui também o manual de instruções e um pino metálico para repor as definições de fábrica do dispositivo, se necessário.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Depois de tirar tudo da caixa, eis o que temos à mão: o aparelho propriamente dito, claro, o manual de instruções, o recetor WIFI, a ponta metálica acima mencionada e o Supply de alimentação do aparelho. O cartão de crédito fornecido não é digno de menção, na nossa opinião.



![image](assets/fr/05.webp)



Segue-se um quadro que resume as especificações técnicas gerais do Nano 3S :



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Ligar e estabelecer ligação à rede local



Depois de desembalado, coloque o Avalon Nano 3 S, se possível, numa área relativamente aberta para permitir a circulação do calor. Em seguida, comece por inserir o pequeno módulo recetor WIFI, como mostrado abaixo:



![image](assets/fr/06.webp)


Em seguida, ligue a ficha USB-C do Supply à porta USB-C do dispositivo para o alimentar.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



O dispositivo arrancará e o logótipo do Avalon Nano aparecerá no ecrã, seguido de um logótipo de "telemóvel" com as palavras "Please Configure the Network With Avalon Family App".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Para tal, vá à sua loja de aplicações móveis, procure e transfira a aplicação **Avalon Family**.



![image](assets/fr/11.webp)


Uma vez instalado, abra-o clicando em "Saltar" no canto superior direito, depois no botão "Adicionar" e, por fim, em "Procurar". Certifique-se de que tem o Bluetooth ativado no seu smartphone, para que a deteção do dispositivo decorra sem problemas.



![image](assets/fr/12.webp)


Assim que o dispositivo for detectado pela aplicação, clique no mesmo e selecione "Ligar". Em seguida, é apresentado um ecrã onde pode introduzir os dados da sua ligação WIFI.


![image](assets/fr/13.webp)


Quando o dispositivo estiver ligado à sua rede local, o ecrã terá o seguinte aspeto:



![image](assets/fr/14.webp)



Mostra um Hashrate "fictício", uma vez que ainda não foi configurada nenhuma pool, e a hora, data, energia e IP do dispositivo Address - muito útil se quiser aceder ao Interface do dispositivo através de um PC e de um browser (mais sobre isto adiante).



![image](assets/fr/15.webp)




## Ligação a um Mining pool



**Esta parte é comum ao Nano 3s e ao Mini 3, uma vez que os processos são rigorosamente idênticos**.



Quer queiramos "solominar" ou "reunir" Miner, vamos ter de nos ligar a um Mining pool. De facto, o nosso dispositivo não é mais do que um fabricante de Hash sem qualquer conhecimento da rede Bitcoin. Ligá-lo a uma pool dá-lhe acesso à rede Bitcoin e permite-lhe receber modelos de blocos para trabalhar.



### Utilizar a aplicação para ligar a um Mining pool



Na aplicação Avalon Family, selecione o dispositivo como indicado abaixo. Ser-lhe-á então pedido automaticamente que altere a palavra-passe de administrador da máquina. Clique em "OK" se o desejar fazer, ou em cancelar para manter a palavra-passe de acesso predefinida "admin".


![image](assets/fr/16.webp)


Em seguida, selecione "Definições", depois "Configuração da piscina" e introduza os parâmetros para as 3 piscinas solicitadas.


Os pools #2 e #3 actuarão como backups no caso de um deles falhar, para que o seu Miner não funcione em vão. Por defeito, o Hashrate será apontado para a piscina #1



No nosso caso, escolhemos:




- 1 - Piscina pública,
- 2 - CkPool,
- 3 - Oceano.



![image](assets/fr/17.webp)



Para obter mais informações sobre como ligar a um Mining pool, consulte estes tutoriais:



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.network/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Em suma, precisamos de





- o pool Address, normalmente **stratum+tcp://xxxxxxxx:port**.





- o nome do "trabalhador" composto pelo *seu Bitcoin Address* e o *pseudo* que escolher para o seu dispositivo, sendo os 2 separados por um *ponto*, por exemplo:**bc1qxxxxxxxxxxxxxxxxx.MonAvalonNano3S**





- a palavra-passe, que normalmente é sempre "**x**"



Uma vez introduzidas as informações do agrupamento, clique em "Guardar".



![image](assets/fr/18.webp)


Reinicie o dispositivo conforme as instruções e aguarde alguns minutos até que o Hashrate esteja apontado para a sua piscina preferida (#1).



### Utilizar o browser para ligar a um Mining pool



Pode também ligar-se a um Mining pool e, de uma forma mais geral, aceder ao sistema de gestão Interface do seu dispositivo através do seu browser favorito.



Para tal, escreva na barra de pesquisa do browser o IP Address do dispositivo apresentado no ecrã abaixo, no nosso exemplo **192.168.144.6**



![image](assets/fr/15.webp)



Aparecerá a seguinte página, pedindo-lhe para abrir a aplicação Avalon Family e digitalizar o código QR apresentado com a aplicação.



![image](assets/fr/20.webp)



Abra a aplicação e clique nos 3 traços no canto superior direito e depois em digitalizar. Digitalize o código QR do navegador, introduza a palavra-passe de administrador da aplicação e clique em OK.



![image](assets/fr/21.webp)



Aqui está a página web que lhe permite interagir com o seu Avalon. É mais um painel de controle para exibir as métricas da máquina do que um meio de configurá-la.



Mas as definições da piscina continuam a poder ser acedidas desta forma, clicando em **"Configuração da piscina "** no canto inferior direito.



![image](assets/fr/22.webp)



Da mesma forma que na aplicação móvel, pode introduzir aqui os parâmetros da sua piscina.



![image](assets/fr/23.webp)



## Controle o seu dispositivo através da aplicação Avalon Family



Já ligámos o nosso Miner à nossa rede local e apontámos o nosso Hashrate para as poças de minério. Agora vamos descobrir as caraterísticas essenciais da nossa máquina através da aplicação Avalon Family.



Na aplicação da família Avalon, clique no ícone correspondente ao Avalon Nano 3S.


são-lhe apresentados 3 menus: "Modo de trabalho", "Controlo da luz" e "Definições". Primeiro, clique em "Modo de trabalho". Ser-lhe-ão então propostos 3 modos de alimentação para a sua máquina.



**Baixo**: permite-lhe obter cerca de 3 Th/s de Hashrate para 70W de consumo de energia


**Médio**: proporciona-lhe cerca de 4,5 Th/s de Hashrate para 100W de consumo de energia


**High**: permite-lhe obter cerca de 6 Th/s de Hashrate com um consumo máximo de 140W



![image](assets/fr/31.webp)


Vamos dar um passo atrás e explorar o menu "Controlo da luz". Este é um menu puramente cosmético. Há uma série de opções disponíveis para variar a cor, a intensidade, o calor, desligar os LED do dispositivo à noite, etc... É fácil descobrir por si próprio.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Por fim, o último menu disponível é o menu "Definições" que já vimos para nos ligarmos às nossas piscinas Mining. Aqui pode gerir as suas piscinas, alterar a palavra-passe de administrador do dispositivo e observar várias métricas, como a data de expiração da garantia, a limpeza do filtro ou a forma de contactar o apoio em caso de avaria.



![image](assets/fr/35.webp)


Para efeitos de manutenção e para manter o filtro o mais limpo possível, recomendamos a utilização de um aspirador e a aspiração regular das entradas e saídas de ar para evitar entupimentos.



Chegámos ao fim deste tutorial, que nos ensinou a ligar o nosso Avalon Nano 3 S à nossa rede local, a apontar o nosso Hashrate para as piscinas Mining e a navegar pelas opções e definições usando a aplicação Avalon Family.



Para saber mais, consulte o nosso tutorial sobre a versão superior do Avalon: o Mini 3.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7