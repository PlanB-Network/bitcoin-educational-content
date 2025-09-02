---
name: Picocriptografia
description: Uma ferramenta de código aberto para encriptar os seus dados
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian BURNEL publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Foram efectuadas alterações ao conteúdo original.*



___



## I. Apresentação



Neste tutorial, vamos dar uma vista de olhos ao Picocrypt, um software de encriptação simples, leve e eficaz para encriptar dados com um elevado nível de segurança.



Adequado para **encriptar ficheiros**, pode utilizá-lo para proteger **dados no seu computador, numa pen USB**, mas também dados armazenados na Nuvem. Por exemplo, pode encriptar dados e armazená-los no **Microsoft OneDrive, Google Drive, iCloud ou Dropbox**, embora para este efeito prefira outro software que será apresentado num artigo futuro.



Também pode utilizá-lo quando precisar de **partilhar dados com terceiros**: graças ao Picocrypt e à chave de desencriptação, eles poderão desencriptar os dados no seu computador. Assim, se a sua conta ou computador for comprometido, os seus dados estão protegidos.



Para acompanhar o projeto Picocrypt, existe apenas um Address:





- [Picocrypt no GitHub](https://github.com/Picocrypt/Picocrypt)



Totalmente **gratuito e de código aberto**, o PicoCrypt está disponível para **Windows,** **Linux** e **macOS**. No Windows, pode instalá-lo na sua própria máquina ou utilizar a versão portátil.



## II. Picocrypt, software de cifragem de fonte aberta



O software de encriptação Picocrypt** apresenta-se como **uma alternativa** a outras soluções bem conhecidas, como o **VeraCrypt** e o **Cryptomator** (*desenvolvidos para encriptar dados em ambientes Cloud*), ou o **AxCrypt**. A propósito, no GitHub oficial do Picocrypt, pode encontrar uma comparação com alguns concorrentes:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Fonte: [Github.com](https://github.com/Picocrypt/Picocrypt)



O Picocrypt é **muito leve**, pesando apenas **3 MB**, e não precisa de ser instalado: é uma **aplicação portátil** com a vantagem de não necessitar de direitos de administrador! No entanto, não descura a segurança, uma vez que se baseia em **algoritmos robustos e fiáveis**:





- Algoritmo de encriptação XChaCha20**
- Função de desvio de chave **Argon2**



Para além das vantagens que acabámos de mencionar, o que realmente atrai é a **facilidade de utilização**!



Só precisa de uma coisa: **uma auditoria ao código**, mas isso está planeado, como se pode ver na tabela de comparação acima (última linha). Mas como é open source, nada o impede de dar uma vista de olhos ao seu código fonte.



Apesar de ser comparado com o BitLocker na tabela acima, **na minha opinião o BitLocker e o Picocrypt destinam-se a utilizações diferentes**: O BitLocker para encriptar um volume completo (o do Windows, por exemplo) e o Picocrypt para encriptar uma estrutura em árvore ou um espaço de armazenamento do tipo "Drive".



## III. Utilização do Picocrypt



Para esta demonstração, será utilizada uma máquina com Windows 11.



### A. Encriptação de dados com Picocrypt



Em primeiro lugar, é necessário descarregar o Picocrypt.exe a partir do GitHub oficial ([ver esta página](https://github.com/Picocrypt/Picocrypt/releases)).



Abra a aplicação para visualizar o seu Interface minimalista no ecrã. Para encriptar dados, quer se trate de **um ficheiro, vários ficheiros ou uma pasta**, basta **arrastar e largar no Interface** do Picocrypt. Isto selecionará os dados a encriptar.



![Image](assets/fr/020.webp)



Em seguida, para a encriptação de dados, tem acesso a várias opções, incluindo a chave de encriptação. Pode ser **uma palavra-passe forte** ou **uma chave de encriptação sob a forma de um ficheiro de chaves**, ou **ambas**. Se tomarmos o exemplo de uma palavra-passe, pode escolher entre criar a sua própria palavra-passe ou gerar uma palavra-passe com o Picocrypt.



Esta palavra-passe deve ser forte, pois pode ser utilizada para desencriptar os dados. Introduza-a em "**Password**" e "**Confirm Password**", depois clique em "**Encrypt**" para encriptar os dados! Antes disso, pode clicar no botão "**Alterar**" junto a "**Guardar saída como**" para especificar o diretório de saída.



**Nota**: para utilizar uma chave em formato de ficheiro, clique em "**Criar**" à direita de "**Arquivos de chaves**" para criar uma chave. Em seguida, selecione-a clicando em "**Editar**" e arrastando e largando o ficheiro chave na área apropriada.



![Image](assets/fr/019.webp)



Os dois ficheiros selecionados são **encriptados e agrupados** no ficheiro "**Encriptado.zip.pcv**", uma vez que **PCV** é a extensão utilizada pelo Picocrypt. Este ficheiro ZIP é ilegível graças à encriptação. Para evitar que os ficheiros selecionados sejam agrupados num único ficheiro ZIP encriptado, é necessário marcar a opção "**Recursivamente**", de modo a que haja tantos ficheiros encriptados quantos os ficheiros a encriptar.



Para aceder aos nossos dados, temos de os desencriptar utilizando o Picocrypt.



![Image](assets/fr/023.webp)



Antes de falarmos sobre a desencriptação de dados, eis algumas informações sobre algumas das opções disponíveis:





- Modo paranoico**: utiliza o nível de segurança mais elevado oferecido pelo Picocrypt. A ferramenta utilizará vários algoritmos de encriptação em cascata (XChaCha20 e Serpent) e HMAC-SHA3 em vez de BLAKE2b para autenticação de dados.
- Reed-Solomon**: implementa códigos de correção de erros *Reed-Solomon* para facilitar a correção de erros em dados corrompidos. Isto permite-lhe suportar um nível de corrupção de cerca de 3% do seu ficheiro.
- Dividir em pedaços** ou **dividir em várias partes**: se estiver a encriptar um ficheiro grande, pode pedir ao Picocrypt para o dividir em várias partes. Isto pode tornar o ficheiro mais fácil de transferir.
- Comprimir ficheiros** ou **Comprimir ficheiros**: comprimir ficheiros para reduzir o tamanho dos ficheiros encriptados.
- Ficheiros eliminados** ou **Fichiers supprimés**: eliminar ficheiros de origem para manter apenas a versão encriptada



### B. Desencriptar dados com Picocrypt



Se precisar de desencriptar os dados, não é mais complicado do que encriptá-los. Basta abrir o Picocrypt e **arrastar e largar o ficheiro PCV a desencriptar**. Em seguida, introduza a palavra-passe e/ou selecione o ficheiro-chave antes de clicar em "**Desencriptar**".



![Image](assets/fr/021.webp)



A versão não encriptada do arquivo ZIP "Encrypted.zip" permite-me agora recuperar os meus dois ficheiros em texto simples!



![Image](assets/fr/022.webp)



## IV. Conclusão



**Foi avisado: O Picocrypt é muito fácil de utilizar e funciona! Embora o Interface seja minimalista, incorpora algumas opções muito úteis para personalizar a encriptação! E como está disponível numa versão portátil, pode levá-lo consigo para onde quer que vá, para que possa desencriptar os seus dados com confiança**



Certifique-se de que utiliza palavras-passe fortes para proteger os dados e, se utilizar um ficheiro de chaves, não se esqueça de fazer uma cópia de segurança, caso contrário deixará de poder desencriptar o contentor PCV gerado pelo Picocrypt. Finalmente, deve saber que existe também [uma versão CLI](https://github.com/Picocrypt/CLI) (com menos funcionalidades) que permite executar o Picocrypt a partir da linha de comandos: mais uma vez, o Picocrypt abre a porta a novas possibilidades.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5