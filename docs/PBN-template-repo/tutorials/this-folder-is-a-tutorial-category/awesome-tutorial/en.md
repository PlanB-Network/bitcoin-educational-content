---
name: Awesome tutorial

description: How to use an awesome tool
---

![cover](assets/cover.webp)

**Note**: the cover image should always have a horizontal rectangular shape, like the `cover.webp` above.

Info: the planb.academy platform will display chapter titles on the right side of each tutorial (on desktop): to create a chapter title, you only need to create a H2 title (using two ##), as you can see for the title below.

## Chapter Title 1 - Images

Such chapter titles on the right side can be clicked by the user to jump to the specific chapter. Here below you can see how they appear on the platform (if you use Github web, make sure to click on the `Preview` mode)

![image](assets/en/01.webp)

Here, you can see the chapter legend displayed right after the tutorial cover image

**Attention**: all the images in tutorials must have a horizontal shape, with a size of 1280 x 720; you can insert images with higher resolution, but pay attention to the ratio of the image

## Chapter Title 2 - Special Text

To write bold text, follow the two examples below (adding `**` or `_` before and after the word): the "Info" and "Note" words will appear in bold

**Info**: I strongly advise you fully read this markdown file, as it contains precious examples about how the markdown language is rendered within the Plan ₿ Academy platform. While some of the rules are the same of markdown syntax, others aren't.

**Note**: _This sentence appears in italic on the platform_

## Chapter Title 3 - Quotations

If you write a paragraph and then press `Enter`, the two paragraphs will remain attached on the platform, like if you only put a space, instead of a new line, even if see a new line on your text editor. To avoid that, you **have to insert an empty line** between the two paragraphs, meaning you need to press the `Enter` button twice to start a new text paragraph.

Let's see an example (below) regarding how to quote other texts, and insert the name of people who spoke such things, together with other details.

**Example**: below, a famous statement from Satoshi Nakamoto is shown; it was posted on the Bitcointalk forum on July 30, 2010:

> If you don't believe me or don't get it, I don't have time to try to convince you, sorry.

As you can see, no need to use the `"` quote sign, as they will be automatically rendered by the platform when using the symbol `>`. Just provide a brief introduction to the mentioned author, along with any relevant context you deem necessary.

### Information about explaining words

Whenever you mention a word specifically used in the Bitcoin space, you may decide to further explain it to be clearer. Well, this is something we encourage, but we kindly ask you not to write such description yourself. If possible, mention the word from the Plan ₿ Academy [Glossary](https://planb.academy/en/resources/glossary). For example, let's say you are going to explain the `Ark` term:

**Example:** ..if you don't know what Ark is, please take a look at the [following definition](https://planb.academy/resources/glossary/ark) from the Plan ₿ Academy Glossary.

**Note** be sure to remove the `/en` path (or any other language selected) from the link you copy: https://planb.academy/en/resources/glossary/ark → becomes → https://planb.academy/resources/glossary/ark

## Chapter Title 4 - Image path

Some text before an image. Please note how the image paths are written, the image 01 is an image containing no text, or English text only. You should only put English or no-text images inside an English markdown file.

![image](assets/en/02.webp)

Other text after an image.

### A special way to mention other tutorials

If you want to mention a Plan ₿ Academy tutorial, paste the link as you see below (remember to add empty lines above and below, as if it were a paragraph):

https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Insert a new line after the link, then you can go on writing your text..

## Chapter Title 5 - Lists

Please look at this example list:
- this is the first element;
- that's the second one;

Now an ordered list:
1. First element;
2. Second element;

Please, never use list with this `*` sign - it will create conflicts with the script taking care of fixing missing bold symbols `**` after the auto translation. Instead, always use the dash `-` for unordered lists.
