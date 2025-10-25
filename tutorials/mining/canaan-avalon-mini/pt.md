---
name: Canaan Avalon Mini 3
description: Configurando seu ASIC Avalon para solomining ou pooling Miner
---

![cover](assets/cover.webp)



Neste tutorial, vamos ver como configurar o Canaan Avalon Mini 3, para uma utilização doméstica fácil do Miner.



Até agora, as máquinas ASIC (*Application Specific Integrated Circuit*) especificamente concebidas para realizar uma determinada tarefa - neste caso, o cálculo Hash (SHA-256) para Miner de Bitcoin - eram particularmente inadequadas para uso doméstico. O incómodo do ruído, o calor gerado e a necessidade de adaptar a instalação eléctrica para suportar a enorme potência destes dispositivos impediam a maioria de nós de participar.



Atualmente, a Canaan, um dos principais fabricantes de máquinas ASIC, decidiu abordar o mercado dos particulares que pretendem ter Miner em casa, propondo uma gama de produtos relativamente silenciosos e muito fáceis de instalar (plug & play).



Estes dispositivos são comercializados como um aquecedor auxiliar, no caso do **Avalon Nano 3S (140W)**, ou como um mini radiador com uma potência de **800W**, no caso do **Avalon Mini 3**.



https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Note-se que a diferença de preço em relação aos aquecedores tradicionais de potência equivalente não lhe permite, na grande maioria dos casos, obter um lucro financeiro. Os satoshis gerados pela atividade do Mining nunca compensarão esta diferença de preço, a menos que tenha acesso a eletricidade gratuita (excedente) ou muito barata.



Na minha opinião, estes dispositivos devem ser vistos mais como uma forma simples de Miner em casa para aqueles que o desejam fazer por razões pessoais: *obter Satss sem KYC / jogar na "lotaria" solominando / participar na descentralização do Hashrate, etc.*, enquanto beneficia **como bónus** do calor gerado para aquecer o seu quarto no inverno. Mas não como uma forma de poupar dinheiro, pelo menos na maioria dos casos (países ocidentais).



## Desembalagem e caraterísticas



### Avalon Nano 3S



Primeiro, vamos ver o que está dentro da caixa do Avalon Mini 3.



![image](assets/fr/24.webp)



Quando abre a caixa, o manual de instruções está mesmo à sua frente, mas o mais importante é que o módulo recetor WIFI está escondido por baixo do autocolante branco redondo à esquerda do manual de instruções. Vai precisar dele mais tarde.



![image](assets/fr/25.webp)



Por baixo do bloco de espuma encontra-se o aparelho e, depois de retirado da caixa, a unidade de alimentação Supply.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Ligar e estabelecer ligação à rede local



Depois de desembalado, coloque o Avalon Mini 3 numa área relativamente aberta, se possível, para permitir que o calor circule adequadamente. De seguida, comece por inserir o pequeno módulo recetor WIFI na porta USB na parte inferior do dispositivo, ligue o cabo de alimentação Supply e certifique-se de que o botão de alimentação está na posição "1".



![image](assets/fr/28.webp)



Uma vez concluídos estes passos, o ecrã LED do dispositivo acende-se e mostra o símbolo "Bluetooth", indicando que está pronto para ser ligado à sua rede local através da aplicação Avalon Family.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Para tal, vá à sua loja de aplicações móveis, procure e transfira a aplicação **Avalon Family**.



![image](assets/fr/11.webp)


Uma vez instalado, abra-o clicando em "Saltar" no canto superior direito, depois no botão "Adicionar" e, por fim, em "Procurar". Certifique-se de que tem o Bluetooth ativado no seu smartphone, para que a deteção do dispositivo decorra sem problemas.



![image](assets/fr/12.webp)


Assim que o dispositivo for detectado pela aplicação, clique no mesmo e selecione "Ligar". Em seguida, é apresentado um ecrã onde pode introduzir os dados da sua ligação WIFI.


![image](assets/fr/13.webp)


Uma vez ligado à sua rede local, o seu Mini 3 apresentará informações como o IP Address, a hora, o Hashrate e a potência eléctrica.



Segue-se um quadro recapitulativo das especificações técnicas gerais do Mini 3:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Ligação a um Mining pool



**Esta parte é comum aos dispositivos Nano 3s e Mini 3, uma vez que os processos são rigorosamente idênticos.**



Quer queiramos "solominar" ou Miner "pool", teremos de nos ligar a um Mining pool. De facto, o nosso dispositivo não é mais do que um Hash-maker sem conhecimento da rede Bitcoin. Ligá-lo a uma pool dá-lhe acesso à rede Bitcoin e permite-lhe receber modelos de blocos para trabalhar.



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



Para mais pormenores sobre como ligar a um Mining pool, consulte estes tutoriais :



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



Já ligámos o nosso Miner doméstico à nossa rede local e apontámos o nosso Hashrate para as piscinas de Minings. Agora vamos descobrir as caraterísticas essenciais da nossa máquina através da aplicação Avalon Family.



No menu principal da aplicação da família Avalon, clique no ícone correspondente ao Avalon Mini 3. Será levado diretamente para o menu de gestão dos modos de funcionamento.



estão disponíveis 3 opções: modo "Aquecimento", modo "Mining" ou modo "Noite".





- No modo "Aquecedor", existem 2 níveis de potência "Eco" ou "Super".


O nível "Eco" corresponde a uma potência de aquecimento de 500 W para um Hashrate de cerca de 25 Th/s e 40 dB para o nível sonoro.


O nível "Super" corresponde a uma potência de saída de 650 W a cerca de 30Th/s e 45 dB. Este modo permite-lhe definir uma temperatura ambiente máxima acima da qual a unidade deixará de funcionar.



![image](assets/fr/36.webp)




- No modo "Mining", a unidade funciona à velocidade máxima, sem a opção de definir uma temperatura alvo (para além do limite de sobreaquecimento incorporado, claro). O objetivo é tirar o máximo partido do desempenho do Miner. Aqui, a potência de saída aproxima-se dos 800 W a cerca de 37,5 Th/s e um nível de ruído de 50-55 dB.



![image](assets/fr/37.webp)


Finalmente, no modo "Noite", o seu Mini 3 funciona à velocidade mais baixa possível e com o mínimo de ruído. 400 W, 20 Th/s e aprox. 33 dB.



Também aqui é possível definir uma temperatura-alvo acima da qual a unidade entra no modo inativo e pára o Miner. Se a temperatura baixar, a unidade reinicia-se e retoma o aquecimento e o Miner. Neste modo, os LED do ecrã estão desligados por defeito, mas pode optar por ligá-los, se necessário, para iluminar a divisão no escuro, como uma luz de presença (ver foto abaixo).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Finalmente, pode brincar com os LEDs do seu Avalon através do menu "Display". Pode optar por percorrer as informações operacionais relevantes, optar por mostrar a hora, ou até mesmo uma imagem personalizada (pixelizada).



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Tal como no Avalon Nano 3S, o menu "Settings" (Definições) permite-lhe alterar a palavra-passe do administrador, as definições da piscina, verificar a obstrução do filtro (localizado na parte inferior do dispositivo), contactar a assistência ou ver os registos do dispositivo.



![image](assets/fr/42.webp)



Mais uma vez, o filtro na parte inferior da unidade pode ser limpo com um aspirador, quanto mais regularmente, melhor.



Chegámos ao fim deste tutorial, que nos ensinou a ligar o nosso Avalon Mini 3 à nossa rede local, a apontar o nosso Hashrate para as piscinas Mining e a navegar pelas opções e definições usando a aplicação Avalon Family.



Para saber mais, consulte o nosso tutorial sobre a versão mais pequena do Avalon: o Nano 3S.



https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6