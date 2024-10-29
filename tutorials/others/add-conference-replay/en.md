---
name: Adding a Conference Replay
description: How to add a conference replay on PlanB Network?
---
![conference](assets/cover.webp)

PlanB's mission is to provide top-tier educational resources on Bitcoin in as many languages as possible. All content published on the site is open-source and hosted on GitHub, allowing anyone to contribute to the platform's enrichment.

Do you want to add the replay of your Bitcoin conference on the PlanB Network site and give visibility to this event, but don't know how? This tutorial is for you!

However, if you want to add a conference that will take place in the future, I advise you to read this other tutorial in which we explain how to add a new event to the site.

https://planb.network/tutorials/others/add-event


![conference](assets/01.webp)
- First, you need to have an account on GitHub. If you don't know how to create an account, we have made a detailed tutorial to guide you.

https://planb.network/tutorials/others/create-github-account


- Go to [the GitHub repository of PlanB dedicated to data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) in the `resources/conference/` section:
![conference](assets/02.webp)
- Click on the top right on the `Add file` button, then on `Create new file`:
![conference](assets/03.webp)
- If you have never contributed to the contents of PlanB Network before, you will need to create your fork of the original repository. Forking a repository means creating a copy of that repository on your own GitHub account, which allows you to work on the project without affecting the original repository. Click on the `Fork this repository` button:
![conference](assets/04.webp)
- You will then arrive at the GitHub editing page:
![conference](assets/05.webp)
- Create a folder for your conference. To do this, in the `Name your file...` box, write the name of your conference in lowercase with dashes instead of spaces. For example, if your conference is called "Paris Bitcoin Conference", you should note `paris-bitcoin-conference`. Also add the year of your conference, for example: `paris-bitcoin-conference-2024`:
![conference](assets/06.webp)
- To validate the creation of the folder, simply note a slash after your name in the same box, for example: `paris-bitcoin-conference-2024/`. Adding a slash automatically creates a folder rather than a file:
![conference](assets/07.webp)
- In this folder, you will create a first YAML file named `conference.yml`:
![conference](assets/08.webp)
Fill this file with information related to your conference using this template:
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

For example, your YAML file could look like this:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Paris, France
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![conference](assets/09.webp)

If you do not yet have a "*builder*" identifier for your organization, you can add it by following this other tutorial.

https://planb.network/tutorials/others/add-builder



- Once you have finished making changes to this file, save them by clicking on the `Commit changes...` button:
![conference](assets/10.webp)
- Add a title for your changes, as well as a short description:
![conference](assets/11.webp)
- Click on the green `Propose changes` button:
![conference](assets/12.webp)
- You will then arrive at a page summarizing all your changes:
![conference](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![conference](assets/14.webp)
- Select your fork of the PlanB Network repository:
![conference](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![conference](assets/16.webp)
- You are now on your working branch:
![conference](assets/17.webp)
- Return to the `resources/conference/` folder and select the folder of your conference that you just created in the previous commit:
![conference](assets/18.webp)
- In the folder of your conference, click on the `Add file` button, then on `Create new file`:
![conference](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![conference](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`:
![conference](assets/21.webp)
- Click on the `Commit changes...` button:
![conference](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![conference](assets/23.webp)
- Return to the `assets` folder:
![conference](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`:
![conference](assets/25.webp)
- A new page will open. Drag and drop an image that represents your conference and will be displayed on the PlanB Network site: ![conference](assets/26.webp)
- It can be a logo, a thumbnail, or even a poster:
![conference](assets/27.webp)
- Once the image is uploaded, check that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![conference](assets/28.webp)
- Be careful, your image must be named `thumbnail` and must be in `.webp` format. The full file name should therefore be: `thumbnail.webp`:
![conference](assets/29.webp)
- Return to your `assets` folder and click on the `.gitkeep` intermediary file:
![conference](assets/30.webp)
- Once on the file, click on the 3 small dots in the top right corner then on `Delete file`:
![conference](assets/31.webp)
- Verify that you are still on the same working branch, then click on the `Commit changes` button:
![conference](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`:
![conference](assets/33.webp)
- Go back to your conference folder:
![conference](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`:
![conference](assets/35.webp)
- Create a new markdown (.md) file by naming it with the indicator of your native language. This file will be used for the replays of your conference. For example, if I want to write the descriptions of the conferences in English, I will name this file en.md:
![conference](assets/36.webp)
- Fill out this markdown file using this template that you can adapt to the configuration of your conference:

```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
--- 

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```

![conference](assets/37.webp)
- At the beginning of your document, in the "front matter," fill in the `name:` field with the name of your conference and the year of the replays. In the `description:` field, write a short description of your event in the language of the file. For example, for a file named `en.md`, the description should be in English. The PlanB Network team will take care of translating your description using their model.
- First-level titles, marked by a `#`, are used to organize the conference by scenes. For example, `# Main Stage` for the main stage and `# Workshop Room` for a stage dedicated to workshops.

- Second-level titles, marked by a double `##`, are used to separate the different replay videos. If the conferences were filmed continuously over a half-day, indicate, for example, `## Friday morning`. If the conferences were filmed and broadcast individually, name the conference directly with a second-level title.

- Under each second-level title, insert a link to the corresponding replay video. The syntax should be: `![video](https://youtu.be/XXXXXXXXXXXX)`, replacing `XXXXXXXXXXXX` with the actual video link.

- If the format allows (individual conferences), you can add the names of the speakers. To do this, add the `Speaker:` field followed by the name or pseudonym of the speaker under the video link. In case of multiple speakers, separate each name with a comma, like this for example: `Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![conference](assets/38.webp)
- Add a title for your modifications, as well as a short description:
![conference](assets/39.webp)
- Click on `Commit changes`:
![conference](assets/40.webp)
- Your conference folder should now look like this:
![conference](assets/41.webp)
- If everything is to your satisfaction, return to the root of your fork:
![conference](assets/42.webp)
- You should see a message indicating that your branch has undergone modifications. Click on the `Compare & pull request` button:
![conference](assets/43.webp)
- Add a clear title and description for your PR:
![conference](assets/44.webp)
- Click on the `Create pull request` button:
![conference](assets/45.webp)
Congratulations! Your PR has been successfully created. An administrator will now review it and, if everything is in order, merge it into the main repository of PlanB Network. You should see the replays of your conference appear on the website a few days later.

Please make sure to follow the progress of your PR. It's possible that an administrator may leave a comment asking for additional information. As long as your PR is not validated, you can view it under the `Pull requests` tab on the PlanB Network's GitHub repository:
![conference](assets/46.webp)

Thank you very much for your valuable contribution! :)
