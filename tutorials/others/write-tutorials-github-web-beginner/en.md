---
name: Contribution - GitHub Web tutorial (beginner)
description: Complete guide to Plan ₿ Network tutorials with GitHub Web
---
![cover](assets/cover.webp)

Before following this tutorial on adding a new tutorial, you need to have completed a few preliminary steps. If you haven't already done so, please take a look at this introductory tutorial first, then come back here :

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
You already have :


- Choose a theme for your tutorial;
- Contacted the Plan ₿ Network team via [Telegram group](https://t.me/PlanBNetwork_ContentBuilder) or paolo@planb.network ;
- Choose your contribution tools.

In this tutorial, we'll look at how to add your tutorial to Plan ₿ Network using the web version of GitHub. If you've already mastered Git, this very detailed tutorial may not be necessary for you. Instead, I recommend you check out one of these other 2 tutorials, where I detail the guidelines to follow and the steps for making changes from a local :


- Experienced users** :

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

- Intermediate (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957
## Prerequisites

Prerequisites before starting the tutorial :


- Have a [GitHub account](https://github.com/signup);
- Have a fork of the [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- Have [a teacher profile on Plan ₿ Network](https://planb.network/professors) (only if you offer a full tutorial).

If you need help getting these prerequisites, my other tutorials will help:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Once everything is in place and you have your fork of the Plan ₿ Network repository, you can start adding the tutorial.

## 1 - Create a new branch

Open your browser and navigate to your fork page in the Plan ₿ Network repository. This is the fork you established on GitHub. The URL of your fork should look like this: `https://github.com/[your-username]/bitcoin-educational-content` :

![GITHUB](assets/fr/01.webp)

Make sure you're on the main `dev` branch, then click on the "*Sync fork*" button. If your fork is not up to date, GitHub will ask you to update your branch. Proceed with this update:

![GITHUB](assets/fr/02.webp)

Click on the `dev` branch, then name your working branch so that its title clearly reflects its purpose, using dashes to separate words. For example, if our aim is to write a tutorial on using Green Wallet, the branch could be called: `tuto-green-wallet-loic`. After entering a suitable name, click on "*Create branch*" to confirm the creation of your new branch based on `dev` :

![GITHUB](assets/fr/03.webp)

You should now be on your new branch of work:

![GITHUB](assets/fr/04.webp)

This means that any changes you make will be saved only on that specific branch.

For each new article you plan to publish, create a new branch from `dev`.

A branch in Git represents a parallel version of the project, allowing you to work on modifications without affecting the main branch, until your work is ready to be integrated.

## 2 - Add tutorial files

Now that the working branch has been created, it's time to integrate your new tutorial.

Within your branch files, you'll need to find the appropriate subfolder for the placement of your tutorial. The organization of the folders reflects the different sections of the Plan ₿ Network website. In our example, since we're adding a tutorial on Green Wallet, head to the following path: `bitcoin-educational-content\tutorials\wallet` which corresponds to the `WALLET` section of the website:

![GITHUB](assets/fr/05.webp)

In the `wallet` folder, create a new directory specifically dedicated to your tutorial. The name of this folder should clearly indicate the software covered in the tutorial, using hyphens to connect words. For my example, the folder will be named `green-wallet`. Click on "*Add File*" then on "*Create new file*" :

![GITHUB](assets/fr/06.webp)

Enter the folder name followed by a slash `/` to confirm its creation as a folder.

![GITHUB](assets/fr/07.webp)

In this new subfolder dedicated to your tutorial, you need to add several items:


- Create an `assets` folder to hold all the illustrations needed for your tutorial;
- Within this `assets` folder, create a subfolder named according to the tutorial's original language code. For example, if the tutorial is written in English, this subfolder should be named `en`. Place all the tutorial's visuals (diagrams, images, screenshots, etc.) in this folder.
- A `tutorial.yml` file must be created to record the details of your tutorial;
- A markdown file must be created to write the actual content of your tutorial. This file must be named according to the code of the language in which it is written. For example, for a tutorial written in French, the file should be called `fr.md`.

To summarize, here is the file hierarchy (we'll continue creating them in the next section):

```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```

## 3 - Fill in the YAML file

Let's start with the YAML file. In the box for creating a new file, enter `tutorial.yml` :

![GITHUB](assets/fr/08.webp)

Fill in the `tutorial.yml` file by copying the following template:

```
id:
project_id:
tags:
-
-
-
category:
level:
credits:
professor:
# Proofreading metadata
original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributors_id:
-
reward:
```

Here are the required fields:


- id**: A UUID (_Universally Unique Identifier_) to uniquely identify the tutorial. You can generate it with [an online tool](https://www.uuidgenerator.net/version4). The only constraint is that this UUID must be random, so as not to conflict with another UUID on the platform;
- project_id** : The UUID of the company or organization behind the tool presented in the tutorial [from the list of projects](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). For example, if you're doing a tutorial on the Green Wallet software, you can find this `project_id` in the following file: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. This information is added in the YAML file of your tutorial because Plan ₿ Network maintains a database of all companies and organizations operating on Bitcoin or related projects. By adding the `project_id` of the linked entity to your tutorial, you create a link between the two elements;
- tags**: 2 or 3 relevant keywords related to the tutorial content, chosen exclusively [from the Plan ₿ Network tag list](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- category** : The subcategory corresponding to the tutorial content, according to the Plan ₿ Network structure (e.g. for wallets: `desktop`, `hardware`, `mobile`, `backup`) ;
- level** : Tutorial difficulty level, from :
    - beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- professor**: Your `contributor_id` (BIP39 words) as displayed on [your teacher profile](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- original_language** : The original language of the tutorial (e.g. `fr`, `en`, etc.) ;
- proofreading**: Information about the proofreading process. Fill in the first part, because proofreading your own tutorial counts as a first validation:
    - language**: Proofreading language code (e.g. `fr`, `en`, etc.).
    - last_contribution_date**: Today's date.
    - urgency** : Leave blank.
    - contributors_id** : Your GitHub ID.
    - reward** : Leave blank.

For more details on your teacher ID, please refer to the corresponding tutorial :

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Here is an example of a `tutorial.yml` file completed for a tutorial on the Blockstream Green wallet:

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
```

Once you have finished modifying your `tutorial.yml` file, save your document by clicking on the "*Commit changes...*" button:

![GITHUB](assets/fr/09.webp)

Add a title and description, and make sure the commit is made to the branch you created at the start of this tutorial. Then confirm by clicking on "*Commit changes*".

![GITHUB](assets/fr/10.webp)

## 4 - Creating subfolders for images

Click on "*Add File*" again and then on "*Create new file*" :

![GITHUB](assets/fr/11.webp)

Enter `assets` followed by a slash `/` to create the folder:

![GITHUB](assets/fr/12.webp)

Repeat this step in the `/assets` folder to create the language subfolder, for example `fr` if your tutorial is in French:

![GITHUB](assets/fr/13.webp)

In this folder, create a dummy file to force GitHub to keep your folder (which would otherwise be empty). Name this file `.gitkeep`. Then click on "*Commit changes...*".

![GITHUB](assets/fr/14.webp)

Check again that you are on the correct branch, then click on "*Commit changes*".

![GITHUB](assets/fr/15.webp)

## 5 - Creating the Markdown file

Now we're going to create the file that will host your tutorial, named according to your language code, for example `fr.md` if we're writing in French. Go to your tutorial folder :

![GITHUB](assets/fr/16.webp)

Click on "Add file*", then on "Create new file*".

![GITHUB](assets/fr/17.webp)

Name the file using your language code. In my case, as the tutorial is written in French, I name my file `fr.md`. The extension `.md` indicates that the file is in Markdown format.

![GITHUB](assets/fr/18.webp)

We start by filling in the `Properties` section at the top of the document. Manually add and fill in the following block of code (the `name:` and `description:` keys must be kept in English, but their values must be written in the language used for your tutorial):

```
---
name: [Titre]
description: [Description]
---
```

![GITHUB](assets/fr/19.webp)

Fill in the name of your tutorial and a short description:

![GITHUB](assets/fr/20.webp)

Then add the path to the cover image at the beginning of your tutorial. To do this, note :

```
![cover-green](assets/cover.webp)
```

This syntax will come in handy whenever you need to add an image to your tutorial. The exclamation mark indicates an image, whose alternative text (alt) is specified between the square brackets. The path to the image is indicated between the brackets:

![GITHUB](assets/fr/21.webp)

Click on the "*Commit changes...*" button to save this file.

![GITHUB](assets/fr/22.webp)

Check that you're on the right branch, then confirm the commit.

![GITHUB](assets/fr/23.webp)

Your tutorial folder should now look like this, according to your language code:

![GITHUB](assets/fr/24.webp)

## 6 - Add logo and cover

Within the `assets` folder, you need to add a file named `logo.webp`, which will serve as the thumbnail for your article. This image must be in `.webp` format, and must be square in size to match the user interface.

You're free to choose the software logo used in the tutorial, or any other relevant image, as long as it's royalty-free. In addition, add an image entitled `cover.webp` in the same place. This will be displayed at the top of your tutorial. Make sure that this image, like the logo, respects the rights of use and is appropriate to the context of your tutorial.

To add images to the `/assets` folder, you can drag and drop them from your local files. Make sure you're in the `/assets` folder and on the right branch, then click on "*Commit changes*".

![GITHUB](assets/fr/26.webp)

You should now see the images appear in the folder.

![GITHUB](assets/fr/27.webp)

## 7 - Writing the tutorial

Continue writing your tutorial by noting your content in the Markdown file with the language code (in my example, in French, it's the `fr.md` file). Go to the file and click on the pencil icon :

![GITHUB](assets/fr/28.webp)

Start writing your tutorial. When adding a subtitle, use the appropriate Markdown formatting by prefixing the text with `##` :

![GITHUB](assets/fr/29.webp)

Alternate between "*Edit*" and "*Preview*" views to better visualize the rendering.

![GITHUB](assets/fr/30.webp)

To save your work, click on "*Commit Changes...*", make sure you're on the right branch, then confirm by clicking on "*Commit Changes*" again.

![GITHUB](assets/fr/31.webp)

## 8 - Add visuals

The language subfolder in the `/assets` folder (in my example: `/assets/en`) is used to store the diagrams and visuals that will accompany your tutorial. As far as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software presented will contain text, but if you add schematics or additional indications on the software screenshots, do so without text or, if essential, use English.

To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted as two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.

Your images must be in `.webp` format only. If necessary, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).

![GITHUB](assets/fr/32.webp)

Now that you've added your images to the subfolder, you can delete the dummy file `.gitkeep`. Open this file, click on the three small dots in the top right-hand corner, then on "*Delete file*".

![GITHUB](assets/fr/33.webp)

Save your changes by clicking on "*Commit changes...*".

![GITHUB](assets/fr/34.webp)

To insert a diagram from your subfolder into your editorial document, use the following Markdown command, taking care to specify the appropriate alternative text and the correct image path for your language:

```
![green](assets/fr/01.webp)
```

The exclamation mark at the beginning indicates an image. The alternative text, which helps with accessibility and referencing, is placed between the square brackets. Finally, the path to the image is indicated between brackets.

![GITHUB](assets/fr/35.webp)

If you wish to create your own schematics, be sure to follow the Plan ₿ Network graphic guidelines to ensure visual consistency:


- Font**: Use [Rubik](https://fonts.google.com/specimen/Rubik);
- Colours** :
 - Orange: #FF5C00
 - Black : #000000
 - White: #FFFFFF

**It is imperative that all visuals integrated into your tutorials are free of copyright or respect the source file license**. Therefore, all diagrams published on Plan ₿ Network are made available under a CC-BY-SA license, in the same way as the text.

**-> Tip:** When sharing files in public, such as images, it's important to remove superfluous metadata. This can contain sensitive information, such as location data, creation dates and author details. To protect your privacy, it's a good idea to remove this metadata. To simplify this operation, you can use specialized tools such as [Exif Cleaner](https://exifcleaner.com/), which enables you to clean up a document's metadata with a simple drag-and-drop.

## 9 - Propose the tutorial

Once you've finished writing your tutorial in the language of your choice, the next step is to submit a **Pull Request**. The administrator will then add the missing translations to your tutorial, using our automated translation method with human proofreading.

To proceed with the Pull Request, after saving all your changes, click on the "*Contribute*" button, then on "*Open pull request*" :

![GITHUB](assets/fr/36.webp)

A Pull Request is a request made to integrate changes from your branch into the main branch of the Plan ₿ Network repository, which allows review and discussion of changes before they are merged.

Before continuing, check carefully at the bottom of the interface that these changes are what you expected:

![GITHUB](assets/fr/37.webp)

Make sure, at the top of the interface, that your working branch is merged onto the `dev` branch of the Plan ₿ Network repository (which is the main branch).

Enter a title that briefly summarizes the changes you wish to merge with the source repository. Add a brief comment describing these changes (if you have an issue number associated with the creation of your tutorial, remember to note `Closes #{issue number}` as a comment), then click on the green "*Create pull request*" button to confirm the merge request:

![GITHUB](assets/fr/38.webp)

Your PR will then be visible in the "*Pull Request*" tab of the main Plan ₿ Network repository. All you have to do now is wait until an administrator contacts you to confirm that your contribution has been merged, or to request any further modifications.

![GITHUB](assets/fr/39.webp)

After merging your PR with the main branch, we recommend deleting your working branch (in my example: `tuto-green-wallet`) to maintain a clean history of your fork. GitHub will automatically offer you this option on your PR page:

![GITHUB](assets/fr/40.webp)

If you wish to make changes to your contribution after you have already submitted your PR, the steps to follow depend on the current status of your PR:


- If your PR is still open and has not yet been merged, make the changes on the same workbranch. The commit changes will be added to your still open PR;
- In the event that your PR has already been merged with the main branch, you'll need to redo the process from the beginning by creating a new branch, then submitting a new PR. Make sure your fork is synchronized with the Plan ₿ Network source repository on the `dev` branch before proceeding.

If you're having technical difficulties submitting your tutorial, please don't hesitate to ask for help on [our dedicated Telegram group for contributions](https://t.me/PlanBNetwork_ContentBuilder). Thank you very much!