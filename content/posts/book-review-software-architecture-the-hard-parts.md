---
title: "Book review. Software Architecture: The Hard Parts: Modern Trade-Off Analyses for Distributed Architectures"
date: 2023-01-15T00:00:00+08:00  
draft: false  
tags: [book]
---

**Software Architecture: The Hard Parts: Modern Trade-Off Analyses for Distributed Architectures is written by** Pramod Sadalage, Mark Richards, Neal Ford, and Zhamak Dehghani and published on 23 September 2021 by O'Reilly Media.

![cover](/images/13-book-review-software-architecture-the-hard-parts/cover.jpg#center)

# What is inside

**Software Architecture: The Hard Parts: Modern Trade-Off Analyses for Distributed Architectures** is a book about making a weighted decision during the design, redesign, or refactoring of the software system. 

It is focused mostly on modern web-enterprise architectures and the popular dilemma of making a choice between monolithic and microservice architectures.

It dives deep into the analysis of the pros and cons of a common architectural decision and provides tradeoff analysis templates for many decomposition and integration patterns.

A large part of the book is dedicated to **Sysops Saga** — every chapter contains part of a continuous story about the architecture group analyzing existing systems, validating tradeoffs, and applying refactoring patterns. It can be useful if you like narrative or don't have relevant examples in your experience.

For some parts, it uses the [architectural fitness function](https://www.thoughtworks.com/en-sg/radar/techniques/architectural-fitness-function) idea from the [**Building Evolutionary Architectures**](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/). If you found Evolutionary Architecture helpful - you can check **The Hard Parts** as a follow-up.

# What is Good

It contains useful terms and concepts in one place, making it a great resource for a glossary with examples.

It provides both perspectives on coupling and decoupling without bias towards either and an extensive list of tradeoffs for both. It follows a practical approach, for example - not advocating for puristic domain data division when it would result in extra communication overhead and unnecessary complexity.

Introduction of composition and decomposition drivers: tradeoffs that pull together and apart parts of the system into modules/apps/services. They are a very practical and visual way of demonstrating architectural direction.

The real-life appliance of static analysis metrics for architecture decisions. Usually, things like cyclomatic complexity and code distance stay just a warning in the SonarQube report that needs to be fixed for the sake of a clean report. Here authors demonstrate how to apply this data for module decomposition or integration.

It dives deep into Saga pattern implementation details and describes different types of sagas design, and when all of them can be useful.

Finally, It's modern, and all technologies are still very relevant.

# What Can Be Better

The most important thing I found this book lacks, is working with performance metrics and estimations. It makes a lot of assumptions about making a more efficient and reliable version of a system, but without backing this information by real or estimated data. What would work great here is Business and performance metrics showing how the system was improved, and what modules work better or cost less.

Continuing this, a good follow-up would mention plans for rollback strategies and risk mitigation.

All the storage usage and refactoring patterns don't consider basic data scale properties, like the total amount of the stored data, distribution, and hot/cold storage size. It’s weird to talk about data replication and decomposition and ignore that it can be a very different type of problem depending on the scale.

The book is very focused on enterprise-web services. If you are looking for universal tips, that can be applied to gamedev, embedded, or mobile development, this book will be less useful.

Finally, I would love to see more real-life examples and ideally — retrospectives. The authors use *Sysops SAGA* narrative as a continuous story that uses acquired knowledge and evolves. It helps to add to ground abstract design schemas to reality if the reader doesn't have a similar experience, but sometimes it feels a little forced and artificial.

# Who Will Find It Useful
- Developers who work with large distributed and multi-module systems
- Developers who work with projects with a long history, large codebase, and complex architecture.
- Developers/Architects/Analysts starting large-scale refactoring of the live system and looking for design patterns, refactoring practices, and tradeoff analysis templates.
