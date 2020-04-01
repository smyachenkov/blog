---
title: "Cognitive Biases In Software Development"
date: 2020-03-18T00:00:00+03:00
draft: false
tags: [programming, psychology]
description: "Common mistakes in programming and system design."
---

A couple of years ago, I started my first job as a programmer. On the first day, I entered the office, sat in my new chair, turned on the computer, checked out a project from the version control system and opened it in IDE. The first-ever piece of the code I saw looked like that:

```js

// TODO it works, but it's ugly, rewrite
function init() {
	// some code
}

```
As you may already have guessed, this code remained untouched for a couple of years, until the project became obsolete and was archived and longer used. But the thing that bothered me then and still bothers me sometimes is why the person who coded working solution felt not comfortable with it, despite it being the completely normal and working solution. Why on a code review, or when exploring new projects, frameworks, and libraries we sometimes think — it is implemented weirdly, they should've done it some other way.

In this post, I will try to answer the question: why do we feel weird about technical solutions? 

# Thinking in patterns

![Cat dog](/images/5_cognitive_biases_development/cat_dog.jpg#center)

Humans like patterns. And I am not even talking only about programming or system design right now. Patterns are everywhere in the life of any person. Patterns save us a lot of time by providing a working solution for a familiar task. You don't recreate the process of brushing your teeth and taking a shower in the morning, as well as you don't put many thoughts into writing simple [CRUD](https://wikipedia.org/wiki/Create,_read,_update_and_delete) application.

Patterns of thinking are the main principle of many puzzles and riddles, such as [Bat and ball price](https://wikipedia.org/wiki/Cognitive_reflection_test#Test_questions_and_answers) or [Monty Hall Problem](https://wikipedia.org/wiki/Monty_Hall_problem).

Patterns help our brains to do less work and to solve problems quicker. Of course, when you need to do many similar things every day, your brain creates a "cache" of those situations with many predefined actions to do. But there are cases when your subconscious consistently matches an incorrect answer to real-world situations. 

Such situations are called [cognitive biases](https://wikipedia.org/wiki/Cognitive_bias). And, as in any other professional area, software development is full of specific behavioral patterns. I think we all can remember some stories from our professional experience where we've seen this behavior in other people and in ourselves.

# Dirty hack or a clever solution?

![workaround](/images/5_cognitive_biases_development/workaround.jpg#center)

Sometimes we can think about the code: this is not straightforward, it feels like a hack rather than a good solution. But very often, this code can work just all right with the only drawback — being "ugly". We strive to see simple and elegant solutions. But almost all of the software is built with workarounds and duct-taped together.

The very famous example is the calculation of inverse square root — the value of 1/√x. The desired solution would look like a direct calculation of this value:

```C
float inverseSquareRoot(float number) {
	return 1.0f/sqrtf(number);
}
```
Pretty straightforward. 

And here's another solution from [Quake III Arena source code](https://wikipedia.org/wiki/Fast_inverse_square_root). This code is famous for it's "indirectness" and low readability, but it solves the initial problem and does it faster than a direct solution:

```C
float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       // evil floating point bit level hacking
	i  = 0x5f3759df - ( i >> 1 );               // what the fuck? 
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
//	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

	return y;
}
```

The desire to see a straightforward solution that covers all the cases of the problem is often referred to as a **perfect solution fallacy** or [Nirvana Fallacy](https://wikipedia.org/wiki/Nirvana_fallacy). The perfect solution should be simple, readable, and working out of the box. But often you have to add multiple checks, optimizations, resources, preparation of data or even do the whole thing in an unintuitive or confusing way. All these small additions can distract from the main focus of the application, thus creating the impression that there are many ugly “wrappings” around the essential part.

There are multiple ways of dealing with imperfection. We can ignore them, we can try to find other solutions that satisfy our perfectionism, or we can modify existing solutions to be more in line with ours. The question is: at what cost? This may vary depending on the context and scale of the refactoring. A simple component, like a single function, can be modified harmlessly. But the cost of the refactoring of a complex system can be very high. When you are refactoring some of the parts, the whole system must remain fully functional. Such tasks can cost a lot of time and resources and should be approached with an awareness that it may brake a lot of things.

# I Should Rewrite It

![documentation](/images/5_cognitive_biases_development/documentation.jpg#center)

We know that good code should be reusable, readable and should follow coding conventions. With modern IDEs, linters, and static analyzers, it has become a common practice to use a set of tools that keep a codebase in good shape. But on the scale of the system design, they may only help a little. Because to quote famous [Joel Spolsky](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) post — **It’s harder to read code than to write it**.

When your project grows, it can reach a point where you forget the exact details of implementation. You have to restore these details by searching them in the documentation, and by reading the code and trying to understand not only what it does, but why it does that. This process often leads to emotional discussions about the state of this project and the skills of a person who wrote this code, even if that person is the one who reads this code right now. This can result in the desire to throw the whole thing away and start from scratch.

![camel](/images/5_cognitive_biases_development/camel.jpg#center)

A complex system can not be easily extended without affecting its other parts. Most of us saw some good old-fashioned spaghetti code, that covered a lot of conditions and was very hard to read. Fixing bugs or adding new features in such code can result in a [Hydra Code](https://blog.codinghorror.com/new-programming-jargon/) — the situation when fixing one of the problems results in breaking other functions or new bugs. And leaving the system in this state will surely not make further development easy. 

Take a look at the [test-driven development in Oracle Database](https://news.ycombinator.com/item?id=18442941) story. Sure, high test coverage and TDD practices can help to manage code quality, but if your project will fall apart when you remove long and complex tests and pipelines – this project is not an easy one to maintain and understand.

# Instagram effect

![Insta vs Reality](/images/5_cognitive_biases_development/insta_vs_reality.jpg#center) 
<div style="text-align: center; font-size:0.7em;">https://www.instagram.com/geraldinewest_/</div>

Software solutions can be complex not only in the complexity of the source code of applications. Modern systems use many different frameworks, libraries, and languages united in large complexes by a convoluted architecture. In a single system, there can exist libraries you are not familiar with, algorithms you never heard of and patterns in languages, you have not seen before.

It is easy to think: “Wow, the guys who did it are really smart!”.

![Your company](/images/5_cognitive_biases_development/your_company.png#center)

I like the analogy with Instagram here. Instagram is full of great pictures, where people enjoy life chilling on the beach with a colorful cocktail in hand, spend the whole day eating pretty food or traveling to new destinations. But many times, those pictures are very distant from the real way it happened because they were staged to show only the bright side.

The same approach applies to the code. When you look at complicated systems and clever solutions - most likely it took a lot of time and resources to implement it, but all you can see is the smooth result. It is easy to fall into this fallacy because complex solutions always require a lot of work, testing, and iterations. 

There is a pretty interesting way to use fear of trying to understand the unknown. Say you came to a new job or a team and you want to make an impression of yourself. Start using obscure and complex solutions right away! There is a good chance your new teammates will think you know much more than they do. Surprisingly, it works very well, and I saw it many times in different companies. Needless to say, the true state of things becomes clear after some time.


# Default choice

It's hard to make a choice. Especially if there are a lot of different options. But if one of those options is presented as the default one — it is highly likely it will be picked. It works in a lot of real-life scenarios, such as contracts signing or selecting meals in a restaurant. This behavior is often referred to as [the default effect](https://wikipedia.org/wiki/Default_effect). And it works really well in software engineering. 

The default option can be used as a safe pick, meaning it saves time for search of new solutions, reading reviews and selecting the one you think is more suitable. You could experience it when you've selected version of software that was suggested in a readme, chose some library that was bundled with a framework, used default config(hello, [MongoDB!](https://www.theregister.co.uk/2017/01/11/mongodb_ransomware_followup/)), or when you've read some article or documentation that suggested one of the approaches without comparing it to others or explaining why this approach was chosen.

Recently, I stumbled upon an interesting example of the drawbacks of the default effect. There was a library that used [semantic versioning](https://semver.org/) and the last released and published version had number `0.11.1`. But then, by some mistake, developers have published the new version with the number `1.11.1`.

![Versioning](/images/5_cognitive_biases_development/versioning.png)

This version quickly became the default choice for lots of users who compared only the versions instead of release dates, which is often the only thing you watch when selecting the version of the library. And even after they released the new version `0.12.0`, version `1.11.1` is still picked and used because it is the first position in most of the lists and suggestions.


# We Have This At Home

![Our vs their](/images/5_cognitive_biases_development/our_their.png#center)

Many times we need to choose something: library, framework, or database from many existing options. And many times, you could have seen in-house solutions or maybe even you have implemented such projects yourself.

The tendency to prefer in-house projects to projects from the "outside" is a popular bias in programming and referred to as [Not Invented Here](https://wikipedia.org/wiki/Not_invented_here).

The drawbacks of creating things from scratch are pretty obvious. It requires a lot of time and human resources to carefully test the software product, to write documentation and guides, to extend it with the new functionality, and to fix bugs.   

![git](/images/5_cognitive_biases_development/git.png#center)

And of course, it works the opposite way too. [Invented Here](https://wikipedia.org/wiki/Invented_here) syndrome makes you feel uncomfortable about the in-house solutions. In today's software development ecosystem, there are tools for 99% of the problems you will encounter. Reinventing the wheel is a waste of time, but if your product really does something new or drastically improves existing processes — maybe it's a good decision to move it from your company's repository and show it to the world.

There can exist the third option — don't choose anything and stay where you are. The [Comfort zone](https://wikipedia.org/wiki/Comfort_zone) is a neat place with a friendly environment. It is easy to become so comfortable with the tools and architecture you use, that changing the set of tools will result in a lot of frustration. The preference for the current state of affairs is called [Status Quo Bias](https://wikipedia.org/wiki/Status_quo_bias).

Doing your own thing can be very fun. It can be a chance to try new technology or to take a much-needed break from the project you've spent every day for the last couple of months. Creating a completely new thing instead of fixing bugs in old applications almost always seems more interesting. Even if the new creation will be very simple, will require a lot of attention and constant fixes in comparison with just taking a working product from the open-source or some provider. 

# Golden Hammer 

![kafka](/images/5_cognitive_biases_development/kafka.jpg#center)

If all you have is a hammer, everything looks like a nail. This saying describes the [Law of the instrument](https://wikipedia.org/wiki/Law_of_the_instrument) or the Golden Hammer bias. 

I’ve seen many times applications written confusingly, just because the author of the application did not know the more suitable tools for the job. For example, a very small application for validation of a text file, that was written in Java and required the whole Java environment to run it and needed to recompile the whole application for any small change. But the author of the application loved Java so much that he did not even consider using some scripting language for essentially a small script. 

This can also happen during the design of a system and the selection of its components. Developers who worked only with Oracle Database will choose it for data storage and may even irrationally hate NoSQL solutions like MongoDB even if it is more suitable for this particular task. 

The search for facts in defense of only the favorite solution can result in a selection of arguments that only support your version or in a [Confirmation bias](https://wikipedia.org/wiki/Confirmation_bias).

And sometimes you want to do it with those tools, because you already have invested a lot of time and money into one thing and now you want to justify it. This situation referred to as [Post-Purchase Rationalization](https://wikipedia.org/wiki/Choice-supportive_bias).

Avoiding problems of the Golden Hammer bias can be achieved by improving your knowledge, learning new languages and tools, their advantages and flaws to choose the correct tool for a job.

# Bikeshedding

![bikeshedding](/images/5_cognitive_biases_development/bikeshedding.png#center)

Most of the programmers do their job in teams. And it’s a common practice to review each other’s decisions, such as code, design, or architecture. It can be hard to review complex projects, but it can be very easy to pick one small thing from it and start a long discussion, nitpicking all the small details about it.

This behavior pattern is called [Law of triviality](https://wikipedia.org/wiki/Law_of_triviality) or **bikeshedding**. The understanding of complex systems takes time and effort, but the small things are way easier to notice, so they become the first target of the criticism. One of the most common examples 
is the arguments about the naming of variables or functions in code. Most of the time, those decisions affect the product very little but can become a topic for a long discussion. 

One of the possible solutions is to put a hard stop on small conflicts after they took more time than needed. For example, this limit can be 30 minutes in a meeting or 5 messages in a code review system. After that, if this thing is not crucial, pick one of the decisions and move on. May be debating for 3 days on the color of the button in your internal system does not worth the effort. 

# Conclusion

There is a lot more to cognitive biases. It is a very interesting and diverse subject. The more software development grows — the more it becomes dependant not only on the algorithms, data, and hardware but also on soft skills, teamwork, and communication.  

And people are not perfect. We often behave in irrational patterns. But if you can detect and understand those patterns, it can help you to make a balanced and honest decision.

# Links

List of cognitive biases — https://wikipedia.org/wiki/List_of_cognitive_biases

Programming jargon — https://blog.codinghorror.com/new-programming-jargon/

Dirty hacks in video game development — https://www.gamasutra.com/view/feature/132500/dirty_coding_tricks.php
