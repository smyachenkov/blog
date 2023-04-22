import sys
import json
import os
import shutil
import re

# path to ChatExport_2023-04-09 dir with photos, videos, texts
export_dir_path = sys.argv[1]
export_log_path = sys.argv[1] + "/result.json"

with open(export_log_path, "r", encoding="utf-8") as input_file:
    contents = input_file.read()
    data = json.loads(contents)

    # largest current post
    max_current_post = 0
    current_posts = os.listdir("content/posts/this-is-singapore")
    current_posts.remove("_index.md")
    post_ids = [int(os.path.splitext(file)[0]) for file in current_posts]
    if len(post_ids) > 0:
        max_current_post = max(post_ids)

    for message in data["messages"]:

        if message["type"] == "service":
            continue

        # ignore old posts since they can be manually edited
        post_id = message["id"]
        if post_id <= max_current_post:
            print("Skipping post {}".format(post_id))

        out_file = f"content/posts/this-is-singapore/{post_id}.md"
        if os.path.exists(out_file):
            print("File exists, skipping post {}".format(post_id))
            continue

        message_text = message["text"]
        hashtags = []

        post_text = ""
        if type(message_text) == list:
            for part in message_text:
                if type(part) == str:
                    post_text += part
                elif type(part) == dict:
                    if part["type"] == "bold":
                        has_newline = part["text"].endswith('\n')
                        t = part["text"].replace('\n', '').replace('\r', '')
                        post_text += "**" + t + "**"
                        if has_newline:
                            post_text += "\n\n"
                    elif part["type"] == "italic":
                        has_newline = part["text"].endswith('\n')
                        t = part["text"].replace('\n', '').replace('\r', '')
                        post_text += "*" + t + "*"
                        if has_newline:
                            post_text += "\n\n"
                    elif part["type"] == "link":
                        post_text += part["text"]
                    elif part["type"] == "text_link":
                        post_text += "[" + part["text"] + "](" + part["href"] + ")"
                    elif part["type"] == "hashtag":
                        hashtags.append(part["text"])

        if "photo" in message:
            # copy file
            photo_file = "./" + export_dir_path + "/" + message["photo"]
            print("copying photo {}".format(photo_file))
            shutil.copy(photo_file, "./static/images/this-is-singapore/photos/")

            # example ![avatar](/images/about/avatar.jpg#center)
            post_text += "\n"
            post_text += "![img](/images/this-is-singapore/" + message["photo"] + "#center)"

        if "media_type" in message and message["media_type"] == "video_file":
            # ignore video files
            print("skipping video file {}".format(message["file"]))

        is_empty = len(post_text.split('\n', 1)[0]) == 0

        date = message["date"]

        # title - first sentence
        title = post_text[:post_text.find("\n")]
        title = re.sub(r"[^a-zA-Zа-яА-Я\s]", "", title)
        if len(title.strip()) == 0:
            title = "empty_title"

        with open(out_file, "w", encoding="utf-8") as o:
            # header
            o.write("---\n")
            o.write("title: " + title + "\n")
            o.write("date: " + date + "\n")
            if is_empty:
                o.write("draft: true\n")
            else:
                o.write("draft: false\n")
            o.write("tags: [this-is-singapore]\n")
            o.write("hideFromMain: true\n")
            o.write("---\n")

            # content
            o.write(post_text)

            o.write("\n")
