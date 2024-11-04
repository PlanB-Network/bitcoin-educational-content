---
name: GitHub Desktop
description: How to set up your local work environment?
---
![github](assets/cover.webp)

PlanB's mission is to provide top-tier educational resources on Bitcoin in as many languages as possible. All content published on the site is open-source and hosted on GitHub, which allows anyone to participate in enriching the platform. Contributions can take various forms: correcting and proofreading existing texts, translating into other languages, updating information, or creating new tutorials not yet available on our site.

If you wish to contribute to the PlanB Network, you will need to use GitHub to propose changes. To do this, you have two options:
- **Contribute directly via GitHub's web interface**: This is the simplest method. If you are a beginner or if you plan to make only a few minor contributions, this option is probably the best for you;
- **Contribute locally using Git**: This method is more suitable if you plan to make regular or significant contributions to the PlanB Network. Although setting up your local Git environment on your computer may seem complex at first, this approach is more efficient in the long run. It allows for more flexible management of changes. If you are new to this, don't worry, **we explain the entire process of setting up your environment in this tutorial** (promise, you won't need to type any command lines ^^).

If you have no idea what GitHub is, or if you want to learn more about the technical terms related to Git and GitHub, I recommend you read our introductory article to familiarize yourself with these concepts.

https://planb.network/tutorials/others/basics-of-github



- To start, you will obviously need a GitHub account. If you already have one, you can log in, otherwise, you can use our tutorial to create a new one.

https://planb.network/tutorials/others/create-github-account



## Step 1: Install GitHub Desktop

- Go to https://desktop.github.com/ to download the GitHub Desktop software. This software allows you to interact easily with GitHub, without having to use a terminal:
![github-desktop](assets/1.webp)
- When you first launch the software, you will be asked to connect your GitHub account. To do this, click on `Sign in to GitHub.com`:
![github-desktop](assets/2.webp)
- An authentication page will open in your browser. Enter your email address and password chosen when creating your account, then click on the `Sign in` button:
![github-desktop](assets/3.webp)
- Click on `Authorize desktop` to confirm the connection between your account and the software:
![github-desktop](assets/4.webp)
- You will be automatically redirected to the GitHub Desktop software. Click on `Finish`: ![github-desktop](assets/5.webp)
- If you have just created your GitHub account, you will be redirected to a page indicating that you have not yet created any repositories. At this point, set aside the GitHub Desktop software; we will return to it later: ![github-desktop](assets/6.webp)

## Step 2: Install Obsidian

Let's move on to installing the writing software. Here, you have several options. You will need software that supports editing Markdown files, as PlanB Network uses this format for text files in its repository.

There are a multitude of software specialized in editing Markdown files, such as Typora, designed specifically for writing. Although it is not ideal, it is also possible to choose a code editor, like Visual Studio Code (VSC) or Sublime Text. However, as a writer, I prefer to use the Obsidian software. Let's see together how to install and get started with it.

- Go to https://obsidian.md/download and download the software: ![github-desktop](assets/7.webp)
- Install Obsidian, launch the software, choose your language, and then click on `Quick Start`: ![github-desktop](assets/8.webp)
- You will arrive at the Obsidian software. For now, you have no files open: ![github-desktop](assets/9.webp)

## Step 3: Fork the PlanB Network repository

- Go to the PlanB Network data repository at the following address: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- From this page, click on the `Fork` button at the top right of the window: ![github-desktop](assets/11.webp)
- In the creation menu, you can leave the default settings. Make sure the `Copy the dev branch only` box is checked, then click on the `Create fork` button: ![github-desktop](assets/12.webp)
- You will then arrive at your own fork of the PlanB Network repository: ![github-desktop](assets/13.webp)
This fork constitutes a separate repository from the original, although it currently contains the same data. You will now work on this new repository.

We have, in a way, made a copy of the PlanB Network source repository. Your fork (the copy) and the original repository will now evolve independently of each other. On the original repository, other contributors may add new data, while you, on your fork, will proceed with your own modifications.
To maintain consistency between these two repositories, it will be necessary to synchronize them periodically so that they retrieve the same information. To send your changes to the source repository, you will use what is called a **Pull Request**. And to integrate changes from the source repository into your fork, you will use the **Sync fork** command available on the GitHub web interface.
![github-desktop](assets/14.webp)

## Step 4: Clone the fork

- Return to the GitHub Desktop software. By now, your fork should appear in the `Your repositories` section. If you don't see it immediately, use the double arrow button to refresh the list. When your fork appears, click on it to select it:
![github-desktop](assets/15.webp)
- Then click on the blue button: `Clone [username]/bitcoin-educational-content`:
![github-desktop](assets/16.webp)
- Keep the default path. To confirm, click on the blue `Clone` button:
![github-desktop](assets/17.webp)
- Wait while GitHub Desktop clones your fork locally:
![github-desktop](assets/18.webp)
- After cloning the repository, the software offers you two options. You must select the first one: `To contribute to the parent project`. This choice will allow you to present your future work as a contribution to the parent project (`PlanB-Network/bitcoin-educational-content`), and not exclusively as a modification of your personal fork (`[username]/bitcoin-educational-content`). Once the option is chosen, click on `Continue`:
![github-desktop](assets/19.webp)
- Your GitHub Desktop is now correctly configured. Now, you can leave the software open in the background to follow the modifications we will make.
![github-desktop](assets/20.webp)
What we have achieved at this stage is the creation of a local copy of your repository, which is hosted on GitHub. As a reminder, this repository is a fork of the source repository of PlanB Network. You will be able to make modifications to this local copy, such as adding tutorials, translations, or corrections. Once these modifications are made, you will use the **Push origin** command to send your local modifications to your fork hosted on GitHub.

You can also retrieve modifications from the fork, for example, during a synchronization with the PlanB Network repository. For this, you will use the **Fetch origin** command to download the modifications to your local copy (your clone), and then the **Pull origin** command to merge them with your work. This allows you to stay up to date with the latest developments of the project while contributing effectively.

![github-desktop](assets/21.webp)
## Step 5: Create a new Obsidian vault

- Open the Obsidian software and click on the small vault icon at the bottom left of the window:
![github-desktop](assets/22.webp)
- Click on the `Open` button to open an existing folder as a vault: ![github-desktop](assets/23.webp)
- Your file explorer will open. You need to locate and select the folder titled `GitHub`, which should be in your `Documents` directory among your files. This path corresponds to the one you established during step 4. After choosing the folder, confirm its selection. The creation of your vault on Obsidian will then launch on a new page of the software:

![github-desktop](assets/24.webp)
-> **Attention**, it is important not to choose the `bitcoin-educational-content` folder when creating a new vault in Obsidian. Instead, select the parent folder, `GitHub`. If you select the `bitcoin-educational-content` folder, the configuration folder `.obsidian`, containing your local Obsidian settings, will automatically be integrated into the repository. We want to avoid this, as it is not necessary to transfer your Obsidian configurations to the PlanB Network repository. An alternative is to add the `.obsidian` folder to the `.gitignore` file, but this method would also modify the `.gitignore` file of the source repository, which is not desirable.

- On the left side of the window, you can see the file tree with your different GitHub repositories that have been cloned locally.
- By clicking on the arrows next to the folder names, you can expand them to access the subfolders of the repositories and their documents:
![github-desktop](assets/25.webp)
- Don't forget to set Obsidian to dark mode: "Light attracts bugs" ;)

## Step 6: Install a Code Editor

Most of your modifications will be on files in Markdown format (`.md`). To edit these documents, you can use Obsidian, the software we discussed earlier. However, PlanB Network uses other file formats, and you will need to modify some of them.

For example, when creating a new tutorial, you will need to create a YAML (`.yml`) file to enter the tags for your tutorial, its title, and your teacher ID. Obsidian does not offer the possibility to modify this type of files, so you will need a code editor.

For this, several options are available to you. Although the standard notepad of your computer can be used for these modifications, this solution is not ideal for neat work. I recommend choosing software specifically designed for this purpose, such as [VS Code](https://code.visualstudio.com/download) or [Sublime Text](https://www.sublimetext.com/download). Sublime Text, being particularly lightweight, will be more than sufficient for our needs.
- Install one of these software programs, and keep it aside for your future modifications. ![github-desktop](assets/26.webp)
Congratulations! Your work environment is now set up to contribute to PlanB Network. You can now explore our other specific tutorials for each type of contribution (translation, proofreading, writing.

https://planb.network/tutorials/others

..).
