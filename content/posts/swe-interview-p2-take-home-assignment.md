---
title: "Software Engineer Interview: Take-home Assignment"
date: 2022-06-17T00:00:00+03:00
draft: false
tags: [interview, take-home-assignment]
---

![Let's go](/images/12-swe-interview-take-home-assignment/lets_go.png#center)

Take-home assignment is the type of interview where you will demonstrate your programming skills on a somewhat close-to-real coding project.
Usually, it’s a description of a small project that you need to implement from scratch or a skeleton that you need to extend.

It is used mostly by small and medium companies, Big Tech and FAANG/MANGA+ enterprises rarely incorporate it into their processes.

In this post, I will share with you how to make the best out of good take-home assignments and how to deal with unfair ones.

# Controversy

Take-home assignment is a very controversial interview type and It gets a massive amount of negative feedback.

The main reasons are:

- **It is long**. It takes significantly more time than any other section of the process, like a coding interview([https://smyachenkov.com/posts/swe-interview-p1-coding/](https://smyachenkov.com/posts/swe-interview-p1-coding/))
- Large amount of dull **boilerplate work**. You need to care about organizing the project from scratch, framework setup, complex data model descriptions, etc.
- **Subjective and hidden evaluation criteria.**
  For example, some companies prefer everything to be implemented from scratch, and some allow you to rely on libraries. Small things, like logging style, amount of classes, and versions of libraries can make an appearance in feedback for the assignment. It can be very frustrating when you never knew that this particular aspect is important for the interview, especially when it’s left out of the requirements.

Here’s some feedback I’ve received for my take-home assignments:

- Too much code.
- Relied too much on libraries.
- Outdated version of the library (one month old, gotta go fast!).
- The worst one — no feedback at all for 2 full days of work.

# Good And Bad Assignments

I recommend taking a closer look at your assignment and estimating the amount of work. 
If it will take more than 1 day, if it will require a lot of boilerplate code, or if it tries to cover too wide areas — something like creating a system with 2 back-end applications + front-end + database — contact your recruiter and suggest making it simpler or to find an alternative.

If your assignment requires more than 1 day to complete — generally it is a bad sign. 
I highly recommend ignoring those types of take-home assignments or negotiating to lower the amount of work or replacing this assignment with a coding or design session.

**Good assignment:**

- Short — 4-8 hours
- No boilerplate for infrastructure code (frameworks setup, database setup, etc)
- Has skeleton of the project
- One application/module or 2-3 very small modules that interact with each other
- A detailed description of goals and high-level functionality. You’ll be surprised how many times I saw take-home assignments where the whole description fitted into one paragraph of text without anything else.


![Drive](/images/12-swe-interview-take-home-assignment/gran_turismo.png#center)
https://kotaku.com/japan-its-not-funny-anymore-5484581

**Bad assignments:**

- Long — 8 hours or more
- Empty project
- Multiple applications/modules/projects
- High-level description without any API contracts/samples/sketches
- Requires specific general-purpose technology. I firmly believe that any engineer can start using technology that is new to them, let’s say MongoDB, after 1 day of studying documentation. But focusing exclusively on MongoDB in take-home assignments and not allowing a candidate to make their own decision and to select technology that they are comfortable with, will lead to overtime and frustration.

The main principle here is that in real-life scenarios things like API contracts, UI sketches, data storage designs, library choices are up to discussion and challenging. Here we want to focus on the ability to create efficient, readable, extendable, and testable code.

# Dealing With Ambiguity

Before the start of the assignment ask your recruiter for a **contact of an engineer who will review it**.

Send them your questions about parts that you have doubts about. For example, if you need extra data for the demo you can ask your reviewers about providing an extended dataset or if it is OK to create this dataset yourself.

Ask about what parts of the project can be simplified to reduce the task time. For example, if it is OK to use a text file instead of a database.

Second important advice — **document your assumptions.** Many parts of an application can be implemented in various ways. Describe why you chose this implementation and what other alternative you thought about. Do it in code comments and in the Readme file if it is an important part of the project.

When you do a coding or system design interview, assumption discussion is done online and you can just talk about it. For take-home assignments, it’s more efficient to use **asynchronous communication practices**.

# Providing Clarity

![Documentation](/images/12-swe-interview-take-home-assignment/documentation.png#center)

Make sure that your reviewers can easily understand how your application works and quickly build and run it.

- Check that it **compiles** and **runs**.
- Include a single **Readme file** with instructions.
- Describe your solution and **highlight the main parts** of the infrastructure and architecture.
  For example, *It uses MongoDB for storage, Spock for unit tests, and data is processed in TweetEventHandler class*.
- List **prerequisites** and **dependencies** required for launch.
- Provide **working** **command** **to start the project**. Especially useful if your application depends on input parameters and environment variables, and if you want to be able to change some values.
- Put it into the **Docker container.**

# Review and Follow-ups

After you have submitted your solution, usually there are two ways it’s going to be evaluated: reviewers will check it and proceed to the next stage, or you will be invited to discuss your project.

It can take up to 2-3 weeks before your submission and your meeting, so it is easy to forget the details of your project. Before the review section, go through your project once more, and make sure that you remember what you have done and why.

Go through your notes and comments, and check again — how does the whole thing work, what assumptions did you make, and what are the pros and cons of your approaches.

The most popular question is **What would you have changed if you had more time?** You can start building up your vision of the ideal project from it, describe your simplifications and propose possible improvements.

Expect to hear two types of questions: **how to improve the current solution** and **how to make it work in real life**.

When talking about the improvement of the current solution expect to be asked:

- Alternative and more efficient algorithms and data structures
- Dealing with memory limits
- Concurrent execution
- Input validation

And for the real-life-scenario questions:

- What technologies you would choose for a production-ready implementation
- How would you deploy and monitor its work
- What would be the SLA of this project
- How to scale this project
- How to secure sensitive data
- How to recover from errors

And so on. This stage often switches to a more high-level discussion about system architecture.

# Conclusion

While take-home assignments receive a lot of criticism, and often it is well deserved, you can still encounter it in many companies.

The important thing to remember is that almost always it will not be the last section in your interview process. It is usually placed in the first half of the whole road and serves as a screening tool or as an opening for the system design/architecture session for mid and senior positions.

Focus on communication, suitable algorithms and data structures, pro and con analysis, identifying bottlenecks, and think about how would you apply those principles if you were developing a production-ready application.
