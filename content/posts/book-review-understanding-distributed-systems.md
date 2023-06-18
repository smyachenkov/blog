---
title: "Understanding Distributed Systems — Book Review"
date: 2023-06-18T00:00:00+08:00  
draft: false  
tags: [book]
---

**Understanding Distributed Systems: What every developer should know about large distributed applications, Second Edition** is written by Roberto Vitillo and published on 23 February 2022 by Roberto Vitillo.

![cover](/images/16-book-review-understanding-distributed-systems/cover.png#center)


# Structure

Broad coverage of approaches and technologies of distributed systems. It leans more towards a practical side with a noticeable focus on troubleshooting, error handling, and resilience with a focus on web technologies.

There are five main parts: 

- Communication
- Coordination
- Scalability
- Resiliency
- Maintainability

The *Communication* chapter overviews the modern network web stack, TCP, TLS, HTTP, and DNS. It’s a good place to quickly refresh knowledge about the “what happens when you enter a URL in the browser” question.

*Coordination* is slightly more theoretical and does an overview of the fundamental bricks of distributed systems theory, such as Logical Clocks, Leader election and Consensus protocols, CRDT, Replication, and CAP theorem. The second part of this chapter is more practical. It focuses on databases and transactions: ACID guarantees, isolation levels in RDBMS, transactions, and alternatives – such as SAGA and async communication patterns.

*Scalability* goes on the journey of making a simple application available for more and more users and checks scaling techniques, load balancing, CDN, caching, API gateways, and messaging.

*Resiliency* is focused on handling scenarios off the happy path, such as identifying SPOF, handling retries and timeouts, maintaining the working state of the system with load leveling, rate limiting, and identifying constant work patterns.

The *Maintainability* chapter covers the development process, testing practices, metrics, monitoring, SLI/SLA/SLO, and CI/CD processes.

# What to expect

Overall, it’s a simple and very easy-reading book. In the beginning, the author deliberately states that the goal of this book is a broad overview without deep dives.

All chapters are relatively small, taking 3-5 minutes of the reader’s time and explicitly stopping before going into more details on the topic. This structure helps to keep the material accessible, and you can quickly go through the whole book and get a grasp on the main concepts.

To compensate the lack of details and keep book at small size, every part contains links to blogs and articles about mentioned terms and techniques, which can be suitable for further reading.

The author used https://excalidraw.com/ for diagrams, which is an awesome tool for small sketches and diagrams, but in my opinion, the default font is the least readable in any online tool I’ve seen lately.
![excalidraw1](/images/16-book-review-understanding-distributed-systems/excalidraw1.png#center) 

You might find this book helpful if you are an engineer starting to work with backend and distributed systems, or if you are preparing for interviews and want to refresh your knowledge without going deeper into one topic.