---
title: "AWS Lambda And Telegram Bots: A Perfect Match"
date: 2021-03-24T00:00:00+03:00  
draft: false  
tags: [programming]
---

Sometimes I want to create simple web applications, that automates one aspect of my life, try it and check if I will
need it.  

For this purpose, I often use [telegram bots](https://core.telegram.org/bots).

# One-purpose project

If you want to test an idea, you want to do it quickly and without extra layers of complexity. The closer
implementation is to your pure, raw idea — the better. For simple projects, that are aimed to check if an idea even worth
further development, you can safely ditch out staff like authorization, monitoring, or telemetry.

If you can express your idea with a single Rest API call — this is a perfect one-purpose project.

# Suitable tasks

Unsurprisingly, the best type of projects for this implementation, are the ones that do the only thing.

Here are some examples:

* Unit converter
* Weather monitoring
* Random name generator
* Translator
* Downloader

Here are some more examples of one-purpose projects that I created for myself:

* Product expiration date reminder
* TikTok video downloader
* Kotlin project name generator
* Travis build result monitor

# Why lambdas are great match for those tasks

1. No need to create a web UI.  
   Chat client is an interface for your API, you can focus only on the logic of the app, and forget about the front-end.
2. Infrastructure simplicity.   
   No need to buy a virtual server, write deploy scripts, support infrastructure, and fix webserver configs.
3. Price.   
   It's way cheaper than a virtual machine, or it even can be free depending on your workload.
4. Similar design of all applications.  
   If you'll come up with a new idea tomorrow — you can build a new API even faster by reusing
   already existing examples.

# Echo bot example
Let's go through all the steps and create a simple template: a bot that sends your message back to you.

Source code:
```python
import os
import json
import requests

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']


def send_message(chat_id, text):
    params = {
        "text": text,
        "chat_id": chat_id,
        "parse_mode": "MarkdownV2"
    }
    requests.get(
        "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/sendMessage",
        params=params
    )


def process_event(event):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    text = message['message']['text']

    if text == "/start":
        send_message(chat_id, "Hello, I am echo bot!")
        return

    if text is None:
        return

    send_message(chat_id, text)


def lambda_handler(event, context):
    process_event(event)
    return {
        'statusCode': 200
    }
```

1. Register a new bot with [@BotFather](https://t.me/botfather) and save the new bot token.
   
2. Create a new lambda function at https://console.aws.amazon.com/lambda.  

3. Create a deployment package. AWS does not provide all the possible dependencies, so you need to package them all into a zip archive.  
    
    Let's go through the whole process for Python.

    3.1. Create `requirements.txt` file with your libraries and versions.  
    3.2. Install dependencies.  
    ```shell
    pip install --target ./package -r requirements.txt
    ```
   3.3. Create a zip archive with all the files from the package directory.
   ```shell
   cd package
   zip -r deploy.zip *
   mv deploy.zip ../
   cd ..
   ```
   3.4 Add your files to this archive.
   ```shell
   zip -ur deploy.zip *  -x '*package*'
   ```
   
   That's it, now upload `deploy.zip` to lambda function via `Upload from -> .zip file`.
   
4. In `Configuration -> Environment` variables add a variable with the key `TELEGRAM_TOKEN` and the value of a token from step 1.
   
5. On the lambda page select the `Add Trigger` menu and create a new API Gateway. It will generate an URL through which you can access your function via HTTP request.
   
6. Register URL from step 4 as webhook url for bot. It can be done via telegram Rest API call  
```curl -GET https://api.telegram.org/bot{BOT_TOKEN}}/setWebhook?url={GATEWAY_URL}```
where `BOT_TOKEN` is the token from step 1 and `GATEWAY_URL` is the URL from step 4. 
   
7. Deploy lambda function with `Deploy` button from the lambda interface and write something to your bot. 

That's it!

You can find full example here — https://github.com/smyachenkov/telegram-echo-bot-aws.