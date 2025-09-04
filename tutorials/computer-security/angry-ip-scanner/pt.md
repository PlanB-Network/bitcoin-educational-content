---
name: Angry IP Scanner
description: Uma forma simples de analisar a sua rede
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian BURNEL publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original



___



## I. Apresentação



Como é que se analisa uma rede Windows em busca de máquinas ligadas de forma rápida e fácil? A resposta é o Angry IP Scanner. Este projeto de código aberto permite-lhe analisar uma rede facilmente, utilizando um Interface gráfico fácil de utilizar.



Esta ferramenta pode ser utilizada por indivíduos para **verificar a sua rede local**, mas também por profissionais de TI para o mesmo fim. Como prova de que **esta ferramenta é muito prática**, já foi utilizada por **alguns grupos de cibercriminosos** para analisar redes empresariais (da mesma forma que o Nmap). Um bom exemplo é o [grupo de ransomware RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Continua a ser um bom software, mas, tal como acontece com outras ferramentas orientadas para as redes e para a segurança, a sua utilização pode ser abusiva.



Aqui, vamos utilizá-lo no **Windows 11**, mas é perfeitamente possível utilizá-lo noutras versões do **Windows**, bem como no **Linux** e no **macOS**.



Menos abrangente que o Nmap, o **Angry IP** Scanner continua a ser interessante para uma análise de rede rápida e básica, mas também porque está ao alcance de todos. Ele **detectará hosts conectados à rede** e identificará **nomes de hosts** e **portas abertas**.



Se quiser ir mais longe, consulte o tutorial sobre o Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Começar a utilizar o Angry IP Scanner



### A. Descarregar e instalar o Angry IP Scanner



Pode descarregar a versão mais recente do Angry IP Scanner a partir do site oficial da aplicação ou do GitHub. Vamos usar a última opção. Clique no link abaixo e baixe a versão EXE: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Execute o executável para prosseguir com a instalação. Não há nada de especial a fazer durante a instalação.



![Image](assets/fr/013.webp)



### B. Executar uma análise inicial da rede



No primeiro lançamento, leia as instruções na janela "**Começar**" para saber mais sobre o funcionamento da ferramenta. A propósito, há vários termos a considerar:





- Alimentador**: módulo responsável pela geração de listas de endereços IP a serem verificados, a partir de um intervalo de IP aleatório ou de um ficheiro com uma lista de endereços IP.
- Fetcher**: um conjunto de módulos para obter informações sobre anfitriões na rede. Existem, por exemplo, fetchers para detetar endereços MAC, pesquisar portas, detetar nomes de anfitriões ou enviar pedidos HTTP.



![Image](assets/fr/018.webp)



Para pesquisar uma sub-rede IP, basta introduzir o **Início IP Address** e o **Fim IP Address** no campo "**Faixa IP**" (caso contrário, alterar o tipo à direita). Em seguida, clicar no botão "**Iniciar**".



![Image](assets/fr/019.webp)



Algumas dezenas de segundos depois, o resultado será visível no Interface do software. **Para cada IP Address do intervalo analisado, verá se o Angry IP Scanner detectou ou não um anfitrião.** Aparecerá também um resumo no ecrã, indicando o número de anfitriões activos (neste caso, 6) e o número de anfitriões com portas abertas.



![Image](assets/fr/020.webp)



Aqui, podemos ver a presença de um anfitrião chamado "**OPNsense.local.domain**", associado ao IP Address "**192.168.10.1**" e acessível nas **portas 80** e **443** (HTTP e HTTPS). Clicar com o botão direito do rato no anfitrião dá acesso a comandos adicionais, como ping, trace route e abertura do browser através deste IP Address.



![Image](assets/fr/012.webp)



### C. Adicionar portas de rastreio



Por predefinição, o **Angry IP Scanner** efectua o scan de 3 portas: **80** (HTTP), **443** (HTTPS) e **8080**. Pode adicionar mais portas a serem verificadas a partir das preferências da aplicação. Clique no menu "**Ferramentas**" e, em seguida, no separador "**Portas**".



Aqui, pode modificar a lista de portas através da opção "**Seleção de portas**". Pode **indicar números de portas específicos separados por uma vírgula, ou intervalos de portas**. O exemplo abaixo adiciona duas portas: **445** (SMB) e **389** (LDAP). Para examinar portas de 1 a 1000, digite "**1-1000**". Não é especificado se as verificações de portas são efectuadas em TCP, UDP ou ambos.



![Image](assets/fr/021.webp)



Se executar a verificação novamente, é provável que obtenha novas informações. No exemplo abaixo, o Angry IP Scanner diz-me que as portas 389 e 445 estão abertas nos anfitriões "**SRV-ADDS-01**" e "**SRV-ADDS-02**", graças à nova configuração das portas a serem verificadas.



![Image](assets/fr/022.webp)



**Nota**: a partir do menu "**Scanner**", pode exportar os resultados da digitalização para um ficheiro de texto.



Se pretender aprofundar a verificação, clique no menu "**Ferramentas**" e, em seguida, clique em "**Apanhadores**". Isto adiciona "capacidades" à verificação. Basta selecionar um fetcher e movê-lo para a esquerda para o ativar. Isto adicionará uma coluna extra ao resultado da verificação.



![Image](assets/fr/014.webp)



O exemplo abaixo mostra as funções "**NetBIOS info**" e "**Web detection**". A primeira fornece informações adicionais, como o MAC Address e o nome de domínio da máquina, enquanto a segunda apresenta o título da página Web (que pode dar alguma indicação do tipo de servidor ou aplicação Web).



![Image](assets/fr/011.webp)



Finalmente, a partir das preferências, pode também alterar o método utilizado para "**ping**", ou seja, para considerar se um anfitrião está ativo ou não. Uma vez que alguns anfitriões não respondem a pings, isto permite-lhe tentar outros métodos (pacote UDP, sonda de porta TCP, ARP, combinação UDP + TCP, etc.).



## III. Conclusão



Simples e eficaz: O Angry IP Scanner detecta anfitriões ligados a uma rede e permite-lhe configurar scans de portas. Em termos de opções, não é tão flexível como o Nmap e não vai tão longe, mas é um bom começo para um scan rápido.



Se pretender utilizar o **Nmap** com um Interface gráfico, pode utilizar a **aplicação Zenmap** (ver síntese abaixo).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d