# The Sovereign University Content Repo

Welcome to the Sovereign University Content Repo! There's a chance that if you are here, it is to contribute to this larger-than-us project, which aims at consolidating the first multilingual and open-source e-learning platform focused on Bitcoin. (If you're just lost on GitHub, visit our [website](https://planb.network/) to learn more about Bitcoin).

Assuming you're here to contribute, I will detail the inner workings of the content management and how you can assist us -- either by producing new content or translating/reviewing content in your language.

Thank you for your time, involvement, and effort in this project. Here we believe in a [value-for-value model](https://dergigi.com/2021/12/30/the-freedom-of-value/) and we'll do our best to reciprocate for your contribution based on your Proof-of-Work. Moreover, by participating in creating valuable Bitcoin resources for your local community, tips from them could also come your way.

## Repo Structure and Content Management

This repo is organized around three main directories, which are:

- `courses`: comprising all the courses about Bitcoin, Lightning, Cryptography, Mining, and so on.
- `resources`: consisting of various types of resources about Bitcoin, such as books, company info, or podcasts.
- `tutorials`: consisting of how-to articles, categorized into themes like exchange, merchant, node, privacy, and so on.
- `quizz`: comprising all the questions that accompagnies the chapter of each courses.
  
Each individual content piece, which is a markdown file, is defined by its location in this tree structure and by its language in the name. For instance, the Italian tutorial about Nerd-Miner would have the following path: `sovereign-university-data/tutorials/mining/nerd-miner/it.md`.

The different images referred to in the content are saved in the `assets` folder, which is at the same level as the corresponding content.

## How to Become a PlanB Network Content Builder?

### Become a Translator/Reviewer

To scale the translation process, we are testing a combined AI x Human approach. We believe that with the use of Large Language Models (LLMs), like the infamous ChatGPT, we can translate a vast number of resources in a relatively short amount of time. We therefore created a [simple program](https://github.com/Asi0Flammeus/LLM-Translator) that leverages the ChatGPT API to translate technical contents and can add support for an additional language with ease.

While this kind of automated translation is more effective and efficient than traditional methods, such as Google Translate or DeepL, it is far from perfect -- that's when the human factor comes in. Indeed, once new content is produced (pushed into the `main` branch), it is automatically translated into the supported languages. Then, those translations MUST be reviewed by a fluent language speaker to ensure high-quality content in all languages. Most of the time, these reviews will correct wrongly translated expressions or grammatical sentence structures.
Once content is reviewed, it will be reviewed by other peers before being merged into the dedicated branch for the corresponding language, which will periodically be merged into the main branch.

Now that you understand the high-level procedure of the translation, you want to review a content you have to complete its associated issue via a PR from your local branch to the corresponding language branch (e.g. `italian-translation-and-review`).

**If you are not familiar with Git, don't worry, we have made a [step-by-step tutorial](https://notes.decouvrebitcoin.com/s/K9ijdGj9X) with comprehensive explanations.** 
Moreover, we are working on a [local interface](https://github.com/pythcoiner/planb_contributor_client) to ease the workflow by hiding all Github mechanics to contributors. 

### Sat Reward 

We consider that any review should be rewarding in sat, so we have derived a equation to compute the corresponding reward to any review contribution:
$$R(W)=B+U\cdot D_C \cdot D_L \cdot W$$

with $R$ the reward, $B$ the base fee (currently 2,500 sats), $U$ the review urgency, $D_C$ the difficulty content, $D_L$ the language difficulty (see below for factor values) and $W$ the number of words in the content.

| Urgency    | Factor |
|------------|--------|
| Non-Urgent | 1      |
| Urgent     | 10     |

| Content Difficulty | Factor |
|--------------------|--------|
| Easy               | 1      |
| Intermediate       | 2      |
| Hard               | 4      |

| Language   | Language Code | Difficulty Factor | Branch Name                            |
|------------|---------------|-------------------|----------------------------------------|
| English    | EN            | 1.0               | `english-translation-and-review`       |
| German     | DE            | 1.0               | `german-translation-and-review`        |
| French     | FR            | 1.0               | `french-translation-and-review`        |
| Italian    | IT            | 1.5               | `italian-translation-and-review`       |
| Portuguese | PT            | 1.0               | `portuguese-translation-and-review`    |
| Spanish    | ES            | 1.5               | `spanish-translation-and-review`       |
| Danish     | DA            | 2.0               | `danish-translation-and-review`        |
| Finish     | FI            | 2.0               | `finnish-translation-and-review`        |
| Dutch      | NL            | 1.5               |           Not yet created              |
| Greek      | EL            | 2.5               |           Not yet created              |
| Hindi      | HI            | 3.0               |           Not yet created              |
| Polish     | PL            | 2.0               |           Not yet created              |
| Swahili    | SW            | 2.5               | `swahili-translation-and-review`       |
| Afrikaans  | AF            | 2.5               | `afrikaans-translation-and-review`     |
| Turkish    | TR            | 3.0               |           Not yet created              |
| Bengali    | BN            | 4.0               |           Not yet created              |
| Russian    | RU            | 2.0               |           Not yet created              |
| Japanese   | JA            | 3.0               | `japanese-translation-and-review`      |
| Arabic     | AR            | 3.0               | `arabic-translation-and-review`        |
| Chinese    | ZH            | 2.5               |           Not yet created              |
| Korean     | KO            | 3.0               |           Not yet created              |
| Thai       | TH            | 3.5               |  `thai-translation-and-review`         |



The reward is sent via Lightning once its review is merged into the `dev` branch. 

### Become a Content Producer

For now, DecouvreBitcoin is in charge of adding new pieces of content. But soon, we will open that process to outside contributions. Nevertheless, if you want to add some content, you should directly contact us via [mail](mailto:asi0@decouvrebitcoin.com) or do it via a PR.


## Join the Network

As part of the PlanB initiative, we believe in mutual support and knowledge-sharing among Bitcoin communities worldwide. To achieve cohesion, we aim to create a network of "Bitcoin Nodes" that share the same values and collectively promote a bottom-up approach to Bitcoin adoption.

To bootstrap this network, we'll utilize the exceptional work of the [BTCmap](https://btcmap.org/) team and the coordination efforts from various Bitcoin communities over the past year, including [einundzwanzig](https://einundzwanzig.space/), [2140](https://2140meetups.com/), [DecouvreBitcoin](https://decouvrebitcoin.com/ambassadeurs/), [satoshispritz](https://satoshispritz.it/), and others. While the progress made thus far is exemplary, we propose advancing to the next step by organizing a global effort more efficiently. If you'd like your community to join this new initiative, please [email us](mailto:rogzy@decouvrebitcoin.com).

For your application, please provide detailed information about your community so we can best assist you. Consider including:

- Your community's name
- Your BTCmap link
- Your community size
- Past educational efforts
- Your needs (e.g., grants, educational content, visibility)
- Your community's 2024 objectives

Please note that our review process will be thorough, so provide all essential details to assist us. Thank you for your cooperation! 

Stack sats and keep building!


