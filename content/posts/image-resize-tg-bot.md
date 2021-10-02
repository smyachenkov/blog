---
title: "Telegram Image Resize Bot"
date: 2021-10-01T00:00:00+03:00
draft: false
tags: [programming, go]
---

Some time ago, I’ve had a project where I needed to have sets of images in different sizes. That was the only work with images in this project, and I did not want to bother with a complex image editor setup.

So, I’ve decided to create a simple telegram bot for quick image resize.

Telegram: [https://t.me/resizerbot](https://t.me/resizerbot).  

Github: [https://github.com/smyachenkov/resizer_bot](https://github.com/smyachenkov/resizer_bot).

# How it works

First, you need to send an image. Both files and compressed images are supported.
After that, you can send your desired dimensions, and the bot will respond with the converted image or images.

![Chat example](/images/9_image-resize-tg-bot/chat_screen.png)

# Implementation

It's written in Go.

I use the [Telebot framework](https://github.com/tucnak/telebot) for interactions with Telegram API and the [Imaging library](https://github.com/disintegration/imaging) for image conversions.  

I use [GitHub actions](https://github.com/smyachenkov/resizer_bot/tree/master/.github/workflows) to check if this project can be built and to run the tests. After that, it creates a Docker image and pushes  it to DockerHub on every commit to the `master` branch.