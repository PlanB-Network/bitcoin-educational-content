---
name: Adding Educational Tools
description: How to add new educational materials on PlanB Network?
---
![event](assets/cover.webp)

PlanB's mission is to provide leading educational resources on Bitcoin, in as many languages as possible. All content published on the site is open-source and hosted on GitHub, which allows anyone to participate in enriching the platform.

Beyond tutorials and training, PlanB Network also offers a vast library of varied educational content on Bitcoin, accessible to everyone, [in the "BET" (_Bitcoin Educational Toolkit_) section](https://planb.network/resources/bet). This database includes educational posters, memes, humorous propaganda posters, technical diagrams, logos, and other tools for users. The goal of this initiative is to support individuals and communities teaching Bitcoin around the world by providing them with the necessary visual resources.

Do you want to participate in enriching this database, but don't know how? This tutorial is for you!

*It is imperative that all content integrated into the site is free of rights or respects the source file's license. Also, all visuals published on PlanB Network are made available under the [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) license.*
![event](assets/01.webp)
- First, you need to have an account on GitHub. If you don't know how to create an account, we have made a detailed tutorial to guide you.

https://planb.network/tutorials/others/create-github-account


- Go to [the GitHub repository of PlanB dedicated to data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) in the `resources/bet/` section:
![event](assets/02.webp)
- Click on the top right on the `Add file` button, then on `Create new file`:
![event](assets/03.webp)
- If you have never contributed to the contents of PlanB Network before, you will need to create your fork of the original repository. Forking a repository means creating a copy of that repository on your own GitHub account, which allows you to work on the project without affecting the original repository. Click on the `Fork this repository` button:
![event](assets/04.webp)
- You will then arrive at the GitHub editing page:
![event](assets/05.webp)
- Create a folder for your content. To do this, in the `Name your file...` box, write the name of your content in lowercase with dashes instead of spaces. In my example, let's say I want to add a PDF visual of the 2048-word BIP39 list. So, I will call my folder `bip39-wordlist`: ![event](assets/06.webp)
- To confirm the creation of the folder, simply add a slash after the name in the same box, for example: `bip39-wordlist/`. Adding a slash automatically creates a folder rather than a file:
![event](assets/07.webp)
- In this folder, you will create a first YAML file named `bet.yml`:
![event](assets/08.webp)
- Fill this file with information related to your content using this template:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```

Here are the details to fill in for each field:

- **`builder`**: Indicate your organization's identifier on PlanB Network. If you do not yet have a "builder" identifier for your company, you can create one by following this tutorial.

https://planb.network/tutorials/others/add-builder

 If you do not have one, you can simply use your name, your pseudonym, or the name of your company without having created a builder profile.

- **`type`**: Select the nature of your content among the following two options:
	- `Educational Content` for educational contents.
	- `Visual Content` for other types of diverse contents.

- **`links`**: Provide links to your contents. You have two options:
	- If you choose to host your content directly on PlanB's GitHub, you will need to add the links to this file during the following steps.
	- If your contents are hosted elsewhere, like on your personal website, indicate the corresponding links here:
	    - `download`: A link to download your content.
	    - `view`: A link to view your content (can be the same as the download link). If your content is available in multiple languages, add a link for each language.

- **`tags`**: Add two tags associated with your content. Examples:
	- bitcoin
	- technology
	- economy
	- education
	- meme...

- **`contributors`**: Mention your contributor identifier if you have one.

For example, your YAML file could look like this:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```yaml
name: 
description: |
  
```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model. 
For example, here is what your file might look like:

```yaml
name: BIP39 WORDLIST
description: |
  Complete and numbered list of the 2048 English words from the BIP39 dictionary used to encode mnemonic phrases. The document can be printed on a single page.
```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Keep only the last part of the URL from `/resources` onwards:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Add to the base of the URL the following information to have the correct link:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

What we are doing here is anticipating the future link to your file, once your proposal has been merged into the source repository of the PlanB Network.
- Go back to your `bet.yml` file and click on the pencil icon: ![event](assets/47.webp)
- Add your link there:
![event](assets/48.webp)
- Once your changes are complete, click on the `Commit changes...` button:
![event](assets/49.webp)
- Add a title for your changes, as well as a short description:
![event](assets/50.webp)
- Click on the green `Commit changes` button:
![event](assets/51.webp)

---

- If everything looks good to you, return to the root of your fork:
![event](assets/52.webp)
- You should see a message indicating that your branch has been modified. Click on the `Compare & pull request` button:
![event](assets/53.webp)
- Add a clear title and a description for your PR:
![event](assets/54.webp)
- Click on the `Create pull request` button:
![event](assets/55.webp)
Congratulations! Your PR has been successfully created. An administrator will now review it and, if everything is in order, merge it into the main repository of PlanB Network. You should see your BET appear on the website a few days later.

Be sure to follow the progress of your PR. An administrator may leave a comment asking for additional information. As long as your PR is not validated, you can consult it in the Pull requests tab on the PlanB Network GitHub repository:
![event](assets/56.webp)
Thank you very much for your valuable contribution! :)
