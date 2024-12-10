---
name: Contribution - Tutorials
description: How to propose a new tutorial on PlanB Network?
---
![cover](assets/cover.webp)

The mission of PlanB is to provide top-tier educational resources on Bitcoin, in as many languages as possible. All content published on the site is open-source and hosted on GitHub, which offers the opportunity for anyone to participate in enriching the platform. Contributions can take various forms: correcting and proofreading existing texts, translating into other languages, updating information, or creating new tutorials not yet available on our site.

In this tutorial, I will explain how to modify the "Tutorials" section of the PlanB Network. If you wish to add a new tutorial or improve an existing one, this article is for you! We will look in detail at how to contribute to the PlanB Network via GitHub, while using Obsidian, a writing tool.

## Prerequisites

To contribute to the PlanB Network, you have 3 options depending on your experience level with GitHub:
1. **Experienced users**: Continue with your usual methods and consult this tutorial to familiarize yourself with the structure of the PlanB repository, specific requirements, and the workflow.
2. **Beginners ready to learn**: I recommend setting up your own work environment. Follow this tutorial as well as our other articles listed below to guide you step by step.
3. **Beginners for minor contributions**: For tasks that require less modification, such as proofreading or corrections, use GitHub's web interface directly without setting up a complete local environment.

**Software required to follow my tutorial:**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- A code editor ([VSC](https://code.visualstudio.com/) or [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/1.webp)
**Prerequisites before starting the tutorial:**
- Have a [GitHub account](https://github.com/signup).
- Have a fork of the [PlanB Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content).
- Have [a professor profile on PlanB Network](https://planb.network/professors) (only if you are proposing a complete tutorial).

**If you need help obtaining these prerequisites, my other tutorials will guide you:**
**[Understanding Git and GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Creating a GitHub account](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Setting up your work environment](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
**[Creating a professor profile](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**
## What type of content to write on PlanB Network?
We are primarily looking for tutorials on tools related to Bitcoin or its ecosystem. These contents can be organized around six main categories:
- Wallet;
- Node;
- Mining;
- Merchant;
- Exchange;
- Privacy.
![tutorial](assets/2.webp)
Beyond these topics specifically related to Bitcoin, PlanB is also looking for contributions on themes that highlight individual sovereignty, such as:
- Open source tools;
- Computing;
- Cryptography;
- Energy;
- Mathematics;
- Economics;
- DIYs;
- LifeHacking...

For example, we currently have tutorials on Tails, Nostr, or GrapheneOS. These tools are not directly related to Bitcoin, but they are systems that can interest us in a process of sovereignty in the digital world. These contents can be integrated into a sub-category of the "Others" section.

You have the choice between designing a tutorial from scratch or taking a tutorial previously published on your website (provided you own the copyright) to also share it on PlanB Network, adding a link to the original article.

Whatever your choice, keep in mind that all content published on PlanB Network is under the free license [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). This license allows anyone to copy and, potentially, to modify your content, provided that the original source is duly credited.

## How to propose a tutorial on PlanB Network?

Once everything is in place, and your local environment is well set up with your own fork of PlanB Network, you can start adding the tutorial.

### Create a new branch

- Open your browser and head to the page of your fork of the PlanB repository. This is the fork you have established on GitHub. The URL of your fork should look like: `https://github.com/[your-username]/bitcoin-educational-content`:
![tutorial](assets/3.webp)
- Make sure you are on the main branch `dev` then click on the `Sync fork` button. If your fork is not up to date, GitHub will offer to update your branch. Proceed with this update. If, on the contrary, your branch is already up to date, GitHub will inform you:
![tutorial](assets/4.webp)
- Open the GitHub Desktop software and make sure your fork is correctly selected in the top left corner of the window:
![tutorial](assets/5.webp)
- Click on the `Fetch origin` button. If your local repository is already up to date, GitHub Desktop will not suggest any further action. Otherwise, the `Pull origin` option will appear. Click on this button to update your local repository: ![tutorial](assets/6.webp)
- Ensure that you are on the main branch `dev`:
![tutorial](assets/7.webp)
- Click on this branch, then click on the `New Branch` button:
![tutorial](assets/8.webp)
- Make sure the new branch is based on the source repository, namely `PlanB-Network/bitcoin-educational-content`.
- Name your branch in a way that the title is clear about its purpose, using dashes to separate each word. For example, let's say our goal is to write a tutorial on using Sparrow Wallet software. In this case, the working branch dedicated to writing this tutorial could be named: `tuto-sparrow-wallet-loic`. Once the appropriate name is entered, click on `Create branch` to confirm the creation of the branch:
![tutorial](assets/9.webp)
- Now click on the `Publish branch` button to save your new working branch on your online fork on GitHub:
![tutorial](assets/10.webp)
Now, on GitHub Desktop, you should be on your new branch. This means that all changes made locally on your computer will be recorded exclusively on this specific branch. Also, as long as this branch remains selected on GitHub Desktop, the files locally visible on your machine correspond to those of this branch (`tuto-sparrow-wallet-loic`), and not to those of the main branch (`dev`).
![tutorial](assets/11.webp)
For each new article you wish to publish, you will need to create a new branch from `dev`. A branch in Git is a parallel version of the project, which allows you to make changes without affecting the main branch, until the work is ready to be merged.

### Adding the tutorial

Now that the working branch is created, it's time to integrate your new tutorial.
- Open your file manager and navigate to the `bitcoin-educational-content` folder, which represents the local clone of your repository. You should normally find it under `Documents\GitHub\bitcoin-educational-content`. Within this directory, it will be necessary to locate the appropriate sub-folder for placing your tutorial. The organization of the folders reflects the different sections of the PlanB Network website. In our example, since we wish to add a tutorial on Sparrow Wallet, it is appropriate to go to the following path: `bitcoin-educational-content\tutorials\wallet` which corresponds to the `WALLET` section on the website: ![tutorial](assets/12.webp)
- Within the `wallet` folder, you need to create a new directory specifically dedicated to your tutorial. The name of this folder must evoke the software covered in the tutorial, ensuring to connect words with dashes. For my example, the folder will be titled `sparrow-wallet`:
![tutorial](assets/13.webp)
- In this new sub-folder dedicated to your tutorial, several elements need to be added:
	- Create an `assets` folder, intended to receive all the illustrations necessary for your tutorial;
    - Within this `assets` folder, you need to create 8 sub-folders named `fr`, `de`, `en`, `it`, `es`, `ja`, `vi`, and `pt`, in order to classify the visuals according to the corresponding languages. You must also add a `notext` sub-folder for visuals that do not need translation, such as screenshots for example;
	- A `tutorial.yml` file must be created to record the details related to your tutorial;
	- A markdown format file is to be created to write the actual content of your tutorial. This file must be titled according to the language code of the writing. For example, for a tutorial written in French, the file should be called `fr.md`.
![tutorial](assets/14.webp)
- To summarize, here is the hierarchy of files to create:
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (to be modified with the right category)
        └── sparrow-wallet/ (to be modified with the name of the tutorial)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (to be modified according to the appropriate language code)
```

- To start, open your `tutorial.yml` file using your code editor.
- Fill in each field with the information specified below:
- **builder**: Enter the name of the company that produces the software you are creating a tutorial for;
- **tags**: Determine a series of keywords closely related to the topic of your article, to facilitate its search and indexing;
- **category**: Select an appropriate sub-category among those available on the PlanB site, based on the content of your tutorial. For example, for a tutorial in the `WALLET` section, the available options are `Desktop`, `Hardware`, and `Mobile`;
- **level**: Indicate the difficulty level of your tutorial by choosing one of the following four categories:
    - Beginner (`beginner`),
    - Intermediate (`intermediary`),
    - Advanced (`advanced`),
    - Expert (`expert`).
- **professor**: Provide your contributor ID as it appears on your professor profile. For more details, refer to [the corresponding tutorial](https://planb.network/fr/tutorials/others/create-teacher-profile);
- **link** (optional): In case you wish to credit a source website for the tutorial you are developing, such as your own personal site, this is where you can add the concerned link.
![tutorial](assets/15.webp)
- Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![tutorial](assets/16.webp)
- You can now close your code editor.
- In the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You have the freedom to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same location. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
![tutorial](assets/17.webp)
- Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree to the folder of your tutorial and to the searched file:
![tutorial](assets/18.webp)
- Click on the file to open it:
![tutorial](assets/19.webp)
- We will start by filling out the `Properties` section at the top of the document. If this section is missing from your file (if the document is completely blank), you can reproduce it by copying it from another existing tutorial: ![tutorial](assets/20.webp)
- You can also add it manually in this way using your code editor:
```markdown
---
name: [Title]
description: [Description]
---
```
![tutorial](assets/21.webp)
- Fill in the name of your tutorial and a short description of it:
![tutorial](assets/22.webp)
- Then add your cover image at the beginning of your tutorial. To do this, type:
```markdown
![cover-sparrow](assets/cover.webp)
```
- This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![tutorial](assets/23.webp)
- Continue writing your tutorial by writing your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![tutorial](assets/24.webp)

### How to add diagrams to the tutorial?

The language subfolders in the `assets` folder are intended to organize the diagrams and visuals that will accompany your tutorial. If your images include text, make sure to translate them for each concerned language to make your content accessible to an international audience. For diagrams without text to translate or screenshots, place them directly in the `notext` subfolder.
![tutorial](assets/25.webp)
To name your images, simply put numbers in the order of appearance in the tutorial. For example, name your first image `1.webp`, your second `2.webp`, and so on.

If the same diagram is translated into multiple languages, keep the same file name for the different translations in the language subfolders, such as `en/1.webp`, `fr/1.webp`, `pt/1.webp`, etc.

You have the option to use different image formats such as `jpeg`, `png`, or `webp`. It is recommended to opt for the `webp` format so that the images are less heavy.
![tutorial](assets/26.webp)
To insert a diagram into your document, use the following command in Markdown, making sure to specify the appropriate alternative text and the correct path of the image:
```markdown
![sparrow](assets/notext/1.webp)
```
The exclamation point at the beginning indicates that it's an image. The alternative text, which aids in accessibility and SEO, is placed between the brackets. Finally, the path to the image is indicated between the parentheses: ![tutorial](assets/27.webp)
If you wish to create your own diagrams, make sure to adhere to the graphic charter of PlanB Network to ensure visual consistency:
- **Font**: Use [Rubik](https://fonts.google.com/specimen/Rubik);
- **Colors**:
	- Orange: #FF5C00
	- Black: #000000
	- White: #FFFFFF

**It is imperative that all visuals integrated into your tutorials are royalty-free or comply with the source file's license**. Also, all diagrams published on PlanB Network are made available under the CC-BY-SA license, in the same way as the text.

**-> Tip:** When sharing files publicly, such as images, it's important to remove any superfluous metadata. This can contain sensitive information, like location data, creation dates, or details about the author. To protect your privacy, it's advisable to remove this metadata. To simplify this operation, you can use specialized tools like [Exif Cleaner](https://exifcleaner.com/), which offers the ability to clean a document's metadata with a simple drag-and-drop.

### How to save and push the tutorial?

Once you have finished writing your tutorial in the language of your choice, the next step is to submit a **Pull Request**. The administrator will then add the missing translations of your tutorial, thanks to our automated translation method.

- To proceed with the Pull Request, open the GitHub Desktop software.
- The software should automatically detect the changes you have made locally compared to the original repository. Before continuing, carefully check on the left side of the interface that these changes correspond exactly to what you expected: ![tutorial](assets/28.webp)
- Add a title for your commit, then click on the blue `Commit to [your branch]` button to validate these changes: ![tutorial](assets/29.webp)
A commit is a save of the changes made to the branch, accompanied by a descriptive message, allowing to follow the evolution of a project over time. It's thus a sort of intermediate checkpoint.

- Then click on the `Push origin` button. This will send your commit to your fork: ![tutorial](assets/30.webp)
- If you haven't finished your tutorial, you can come back to it later and make new commits.
- If you have finished your edits for this branch, now click on the `Preview Pull Request` button: ![tutorial](assets/31.webp)
- You can check one last time that your modifications are correct, then click on the `Create pull request` button:
![tutorial](assets/32.webp)
A Pull Request is a request made to integrate the changes from your branch to the main branch of the PlanB Network repository, which allows for the review and discussion of the changes before their merger.

- You will be automatically redirected in your browser to GitHub on the preparation page of your Pull Request:
![tutorial](assets/33.webp)
- Provide a title that briefly summarizes the modifications you wish to merge with the source repository.
- Add a brief comment describing these changes.
- Click on the green `Create pull request` button to confirm the merge request:
![tutorial](assets/34.webp)
Your PR will then be visible in the `Pull Request` tab of the main repository of PlanB Network. All you have to do now is wait until an administrator contacts you to confirm the merger of your contribution or to request any additional modifications.
![tutorial](assets/35.webp)
After the merger of your PR with the main branch, it is recommended to delete your working branch (`tuto-sparrow-wallet`) to maintain a clean history on your fork. GitHub will automatically offer you this option on the page of your PR:
![tutorial](assets/36.webp)
On the GitHub Desktop software, you can switch back to the main branch of your fork (`dev`).
![tutorial](assets/7.webp)
If you wish to make modifications to your contribution after having already submitted your PR, the procedure to follow depends on the current state of your PR:
- If your PR is still open and has not yet been merged, perform the modifications locally while staying on the same branch. Once the modifications are finalized, use the `Push origin` button to add a new commit to your still-open PR;
- In the case where your PR has already been merged with the main branch, you will need to redo the process from the beginning by creating a new branch, then submitting a new PR. Ensure that your local repository is synchronized with the source repository of PlanB Network before proceeding.
