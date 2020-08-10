---
title: "Code Presentation Tips"
date: 2020-08-11T00:00:00+03:00
draft: false
tags: [programming]
description: "How to make code in slides look better."
---

Sometimes, I need to show some code in my slides. It can be an internal presentation for 3-5 developers, an online meetup, or a live event. And many times, I have found myself trying to recover the lost code style configuration or to recreate a color palette from the previous presentation.

I've decided to save all the templates and share them and some tips about code in slides with you. I hope it will help you to create code slides quicker and better. 

# Know Your Tools

![Logos](/images/6_code_presentation/logos.png#center)

<div style="text-align: center; font-size:0.8em; font-style: italic;">IntelliJ IDEA, Sublime, Carbon</div>

Get familiar with the tools for code formating and syntax highlight.

#### IDE
Popular choices for many languages are [JetBrains IDEs](https://jetbrains.com/) or [VS Code](https://code.visualstudio.com/).  
There also some useful extensions for IDEs that can help you to take screenshots directly from the editor, such as [Code screenshots](https://plugins.jetbrains.com/plugin/9406-code-screenshots) or [Polacode](https://dev.to/arbaoui_mehdi/take-a-screenshot-of-vscode-using-polacode-extension-524h).  

#### General-purpose text editors
I use [Sublime Text](https://www.sublimetext.com/). It supports syntax highlight for many languages and has a lot of helpful extensions. Mine most often used commands for work with small pieces of code are `Set syntax: %language_name%` to use syntax highlight for a particular language in the current file and `Reindent Lines` to apply auto-indentation. Both commands can be accessed through the command menu by `Ctrl/Command + Shift + P` shortcut.

#### Online tools
The best online tool I've seen so far is [Carbon](https://carbon.now.sh/). It supports many languages, has many color themes, modern design, and it offers a lot of options for color theme configuration.

<br>

Those are my favorite tools to create a formatted and visually appealing piece of code, but there are other products in the market. What else do you use? Please, share your setup in comments!

# Prepare Format & Highlight Presets

![No Highlight](/images/6_code_presentation/highlight_1.png#center)
![Highlight](/images/6_code_presentation/highlight_2.png#center)

<div style="text-align: center; font-size:0.8em; font-style: italic;">Turn on the light</div>

Prepare and save the configuration for your editor.

It is possible to import and export code style configurations for IntelliJ Idea. For convenience, I store them in GitHub repository: [Idea Config](https://github.com/smyachenkov/code-slides-config/tree/master/idea). You can apply this code style configuration in `Settings → Editor → Code Style → Scheme → Import Scheme → IntelliJ IDEA code style XML` and selecting your config file. The same menu allows you to export the current scheme. Create your config, save it in a repository, and use it when you need to have your code style in IDE.

Also, I store color schemes for [Carbon](https://carbon.now.sh/). Carbon has many ready-to-use themes, but you can customize and share your configurations. You can find my configs and instructions on how to apply them here: [Carbon Config](https://github.com/smyachenkov/code-slides-config/tree/master/carbon).

# Have Dark And Light Presets

![Dark and Light](/images/6_code_presentation/color.png#center)
<div style="text-align: center; font-size:0.8em; font-style: italic;">Both will come in handy</div>

Create presets for both light and dark environments.

I like the white code on a dark background, and usually, I use this theme for personal projects. But a couple of times, I had to redo a big presentation with a lot of code just because of the requirements from event organizers. It is convenient to have presets for two themes: dark and light. This way, you can quickly rewrite all your slides and adjust your presentation.
 
# Choose Suitable Language

![Java](/images/6_code_presentation/lang_1.png#center)
![Scala](/images/6_code_presentation/lang_2.png#center)

<div style="text-align: center; font-size:0.8em; font-style: italic;">Some languages have more expressive options</div>

This problem may occur only when your presentation content is not about one particular technology. But if you are talking about a problem that can be solved and demonstrated in any programming language, then it is better to use a more suitable programming language.

For example, the Spark application can be written both in Java and Scala, but the Scala version almost always will be shorter and more expressive.  

# Keep It Short

![Long](/images/6_code_presentation/long_1.png#center)
![Short](/images/6_code_presentation/long_2.png#center)

<div style="text-align: center; font-size:0.8em; font-style: italic;">Get rid of non-essential code</div>

Long code is acceptable only when you want to demonstrate how awful the long code looks.

Respect the time and effort of your audience. Leave only the code that shows the idea. Don't include things that do not solve the problem of your slide, such as logging, error handling, imports, comments, etc. Also, don't hesitate to replace a long or uninteresting block of code with comment or pseudocode.

Remember that simplicity is achieved not when there is nothing to add, but when there is nothing to take away.

# Useful Links

Carbon code image share tool - https://carbon.now.sh/.

Codestyle templates - https://github.com/smyachenkov/code-slides-config.
