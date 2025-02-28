---
name: Ubuntu
description: Guia completo para instalar e utilizar o Ubuntu como alternativa ao Windows
---
![cover](assets/cover.webp)

## Introdução

Um sistema operativo (SO) é o software principal que gere todos os recursos do seu computador. A escolha de um sistema operativo alternativo como o Ubuntu pode oferecer muitas vantagens em termos de segurança, custo e privacidade.

### Porquê o Ubuntu?


- Segurança melhorada** : As distribuições Linux são conhecidas pela sua segurança e robustez
- Custo zero**: O Ubuntu e a maioria das distribuições Linux são gratuitas
- Grande comunidade**: Uma comunidade de utilizadores prontos a ajudar através de fóruns e tutoriais
- Respeito pela privacidade**: Sistema de fonte aberta para maior transparência
- Simplicidade**: Interface amigável e facilidade de utilização
- Ecossistema rico** : Catálogo alargado de software de fonte aberta
- Suporte regular**: Actualizações seguras da Canonical

## Instalação e configuração

### 1. Pré-requisitos

**Equipamento necessário


- Uma chave USB de pelo menos 12 GB
- Um computador com pelo menos 25 GB disponíveis

### 2. Descarregar


- Aceder a [ubuntu.com/download] (https://ubuntu.com/download)
- Escolha a versão estável (LTS recomendada)
- Transferir imagem ISO

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3. Criar uma chave USB de arranque

É possível utilizar várias ferramentas, como o Balena Etcher :


- Transferir e instalar [Balena Etcher] (https://etcher.balena.io/)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)


- Abra o Balena Etcher e, em seguida, selecione a imagem ISO do Ubuntu
- Selecionar a chave USB como suporte de destino
- Clique em Flash e aguarde que o processo termine

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Instalar e proteger o Ubuntu

**4.1 Arrancar a partir de um dispositivo de memória USB** (em francês)


- Desligar o computador
- Ligar a chave USB (que contém o Ubuntu)
- Ligue o seu computador. Em PCs recentes, o sistema deve reconhecer automaticamente a chave de arranque USB. Se não for esse o caso, reinicie mantendo premida a tecla de acesso à BIOS/UEFI (normalmente F2, F12 ou Delete, dependendo da marca)
 - No menu BIOS/UEFI, selecione a sua chave USB como dispositivo de arranque
 - Guardar e reiniciar

**4.2 Iniciar a instalação** (em francês)

**Ecrã de arranque

Quando arrancar a partir da chave USB, verá este ecrã, que lhe permite iniciar o Ubuntu.

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**Escolha da língua

Escolha a sua língua preferida para a instalação e o sistema.

![Sélection de la langue](assets/fr/07.webp)

**Opções de acessibilidade

Configurar as opções de acessibilidade, se necessário (leitor de ecrã, alto contraste, etc.).

![Options d'accessibilité](assets/fr/08.webp)

**Configuração do teclado

Selecione a disposição do seu teclado. Está disponível um campo de teste para verificar se as teclas correspondem à sua configuração.

![Configuration du clavier](assets/fr/09.webp)

**Ligação de rede

Ligue-se à sua rede Wi-Fi ou com fios para descarregar actualizações durante a instalação.

![Configuration réseau](assets/fr/10.webp)

**Tipo de instalação

Escolha entre "Experimentar o Ubuntu" (para testar sem instalar) ou "Instalar o Ubuntu".

![Choix du type d'installation](assets/fr/11.webp)

**Método de instalação

Selecionar a instalação interactiva.

![Mode d'installation](assets/fr/12.webp)

**Seleção da aplicação

Escolha entre a instalação predefinida ou uma seleção alargada de aplicações.

![Sélection des applications](assets/fr/13.webp)

**Aplicações de terceiros

Decida se quer ou não instalar controladores adicionais e software proprietário.

![Installation applications tierces](assets/fr/14.webp)

**Tipo de particionamento

Existem duas opções principais:


- "Apagar o disco e instalar o Ubuntu": utiliza todo o disco para o Ubuntu
- "Instalação manual: crie um arranque duplo com o Windows ou personalize as suas partições

![Choix du partitionnement](assets/fr/15.webp)

**Criação de conta de utilizador

Defina o seu nome de utilizador e palavra-passe para a sua conta Ubuntu.

![Création du compte](assets/fr/16.webp)

**Fuso horário

Selecione a sua área geográfica para definir a hora do sistema.

![Sélection du fuseau horaire](assets/fr/17.webp)

**Resumo da instalação

Verifique todas as suas escolhas antes de iniciar a instalação final. Depois de clicar em "Instalar", o processo inicia-se.

![Résumé de l'installation](assets/fr/18.webp)

**4.3 Atualizar o Ubuntu após a instalação** (em francês)

A atualização do sistema é um passo importante após uma nova instalação. Existem duas opções:

**Opção 1: Através da interface gráfica do utilizador


- Procurar "Software e actualizações" no menu de aplicações
- A aplicação verificará automaticamente se existem actualizações disponíveis
- Siga as instruções no ecrã para instalar as actualizações

**Opção 2: via terminal


- Abrir o Terminal (Ctrl + Alt + T)
- Digite o seguinte comando para verificar as actualizações disponíveis:

```bash
sudo apt update
```


- Introduza a sua palavra-passe quando lhe for pedido
- Para instalar actualizações, digite :

```bash
sudo apt upgrade
```


- Confirme a instalação digitando "Y" e depois Enter

### 5. Descobrir as tarefas básicas

**5.1 Navegar na Internet

Por predefinição, é frequente encontrar o Firefox na barra de lançamento.

Inicie o Firefox e comece a navegar.

Outros browsers (Chrome, Brave, etc.) podem ser instalados através do Gestor de Software ou através de pacotes .deb.

**5.2 Processamento de texto

O Ubuntu vem com o pacote LibreOffice (Writer para processamento de texto).

Para o abrir: Actividades > Procurar "LibreOffice Writer" ou clicar no ícone se este aparecer na barra.

Pode criar, editar e guardar documentos numa variedade de formatos (incluindo .docx).

**5.3 Instalação de aplicações

Gestor de software (chamado "Ubuntu Software"): interface gráfica para procurar e instalar aplicações.

No Terminal, utilize o comando :

```bash
sudo apt install nom-du-paquet
```

Exemplo:

```bash
sudo apt install vlc
```

### 6. Conclusão e recursos adicionais

Agora está pronto para utilizar o Ubuntu diariamente: proteja o seu sistema, navegue, faça trabalho de escritório, instale software e mantenha o seu SO atualizado!

Para levar a segurança da sua vida digital um passo mais além, recomendamos que dê uma vista de olhos ao nosso serviço de mensagens encriptadas, que é perfeitamente adequado para proteger a sua privacidade e complementa a sua instalação Ubuntu:

https://planb.network/tutorials/others/proton-mail