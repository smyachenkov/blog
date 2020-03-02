---
title: "Cognitive Biases In Software Development"
date: 2020-02-10T00:00:00+03:00
draft: false
tags: [programming, psychology]
---


A couple years ago, I started my first job as a programmer. At the first day I entered the office, sat in my new chair, turned on computer, checked out project from version control system and opened it in IDE. The first ever piece of the code I saw looked like that:

```js

// TODO it works, but it's ugly, rewrite
function init() {
	// some coded
}

```
As you may already have guessed, this code remained untocuched for couple of years, until the project became obsolete and was archived and longer used. But the thing that bothered me than and still bothers me sometimes is why the person who coded working solution felt not comfortable with it, despite it being completely normal and absolutely working solution. Why on a code review, or when exploring new projects, frameworks and libraries we sometimes think - it is implemented weirdly, they should've done it some other way.

In this post I will try answer the question: why do feel weird about technical solutions? 

## Thinking in patterns

Humans like patterns. And I am not even talking only about programming or system design. Patterns are everywhere in a life of any person. Patterns save us a lot of time by providing a working solution for a familiar task. You don't recreate the process of brushing your teeth and taking a shower in the mourning, as well as you don't put much thoughts in writing simple [CRUD](https://wikipedia.org/wiki/Create,_read,_update_and_delete) application.

Patterns of thinking are the main principle of many puzzles and riddles, such as [Bat and ball price](https://wikipedia.org/wiki/Cognitive_reflection_test#Test_questions_and_answers) or [Monty Hall Problem](https://wikipedia.org/wiki/Monty_Hall_problem).

Patterns help our brains to do less work and to solve problems quicker. Of course, when you need to do many similar things every day, your brain creates a "cache" of those situations with a number of predefined actions to do. But there are cases, when your subconsious consistently matches an incorrect answer to real world situation. 

// todo or some other pattern meme
![Cat dog](/images/5_cognitive_biases_development/cat_dog.jpg)

Such situations are called [cognitive biases](https://wikipedia.org/wiki/Cognitive_bias). And, as any other professional area, software development is full of biases we experience and sometimes don't even notice. 

<!--
dont have to waste time on processing whole situation - мыслетопливо

https://danlark.org/2020/01/31/i-wrote-go-code-for-3-weeks-and-you-wont-believe-what-happened-next/

Humans like patterns, when they see something familiar, what they did themselves, they feel it, they know exactly how it is working.

Go is full of patterns, like the very simple one:

1
2
3
if err != nil {
  return nil, err
}
Human eye is very catchy on such kind of things. So, this is one more argument for better readability. To make people use patterns in C++ is barely possible and is not a priority for the standard.
-->


## Dirty hack or a clever solution?
When we write or read code we often think - this is not optimal and not paradigmical, it feels like a hack rather than a good solution. But lots of a times such a code can work just all right and provide all desired functionality, with the only drawback - being "ugly" or not being a direct. 

There are many examples of such "hacks" in video game development industry, especially in it's early years. For example, in first versions of [Wing Commader](https://wikipedia.org/wiki/Wing_Commander_(video_game)#Development) developers fixed an exception during the exit by covering it with another message that said "Thank you for playing Wing Commander."  

Does it solve the problem? Of course! Is it a hack rather than a solution? Sure!

In many cases such shortcuts in problem solving are saving a lot of time and resources, and the line between beeing "dirty" and being "optimal" becomes blurred and it's hard to say what would be more efficient in this particular case. Another famous example is [Fast inverse square root](https://wikipedia.org/wiki/Fast_inverse_square_root) used in Quake 3 engine:
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

This code is pretty famous for it's comments and being hardly readable, especially if you don't know the initial task - to calculate value of 1⁄√number. It gave the precise enough value with a high calculation speed at cost of lowering readability and maintenance potential, which are pretty good conditions for a tasks where you will not reuse or modify this code in other components of your system.

We still can call this solution a "hack", because of it's nature - not being a direct and precise solution, but this kind of hacking intentionally saves lot's of time by implementing only "good enough for the purpose" part of the solution.

Another example from video game development is mirrors. Mirrors in games can be tricky to implement, especially if you are writing your own engine.

screenshot.jpg

And many times the mirror problem was solved by not calculating how light woud be displayed on a mirror surface, but by just rendering the same area and items, and placing the player model with an inversed cordinates or additionally rendering the view from mirror perspective and placing this texture to a mirror.

Such a solution saves a lot of time and resources by not requiring you to write the code for rendering reflections. It does not solves the problems directly - by rendering the "correct reflections", but it can produce 100% accurate representation and be absolutely correct from viewrs perspective. 

So, why do we feel weird about non-direct solutions, which solves the problem to a some degreee with a bit of "hackiness"?

Such a contradiction is often referred as a **perfect solution fallacy** or **nirvana fallacy**. The perfect soultion for a problem should be easy, simple, readable and working out of the box. But lot's of the times you have to add multiple checks, optimizations, resources, preparation of data or even do the whole thing in an unintuitive or confusing way, which can distract from the main focus of the application thus creating an impression that there is a lot of ugly "wrappings" around the essential part.  

There are multiple ways deaing with imperfection - we can ignore them, we can try to find another solutuions which satisfies our perfectionism, or we can modify existing solutions to be more in line with ours. The question - at what cost? This may vary depending on context and it may vary greatly. While simple component like approximate Fast inverse square root function produces accurate enough result to rely on, some other decisions may affect your system in a suprising ways.

[League of Legends](https://leagueoflegends.com/) is one of the most popular competitive videogames with a long history. In this game there are many small units aka minions, who fight along side with the other players. 

![League of Legends Minion](/images/5_cognitive_biases_development/minions.png)

And for a long time many in-game objects like [projectiles](https://www.youtube.com/watch?v=sxKujLWJ4xo), [spells](https://www.youtube.com/watch?v=QBLP83gfq10&feature=youtu.be&t=12m1s), structures are coded as a minions. To the current days this architecture causes a lot of small bugs in different interactions between players and game, which is only becoming more and more complex. 

But the cost of the refactoring of a extremely complex system is very high and when as a engineer or as an architect you are starint to refactor some of the parts, the whole system must remain fully functional. Such tasks can cost a lot of time and resources and should be approached with an awareness that it may brake a lot of things. 

Satisfaction of a nirvana fallacy can be both helpfull and worthless investment, highly depending on the complexity and scale of a system, number of corner-cases it is solving and amount of resources for it's solution.   

<!-- 
// more examples  
https://github.com/apache/maven-checkstyle-plugin/blob/eae07f99f01584bfd3da90a8c5eb32364e8ee82b/src/main/java/org/apache/maven/plugins/checkstyle/exec/DefaultCheckstyleExecutor.java#L839
-->

## Hard To Read

We all know that good code should be reusable, readable, should follow coding conventions and be easy to read. And with all modern IDE, linters and static analyzers it has become a common practice to use a set of tools to keep a codebase in a good condition. All this measures definetely help to remove arguments about size of a indent or brackets placement from code review process, but on the scale of a problem solution they may only help a little. Because, to quote famous [Joel Spolsky](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) post - **It’s harder to read code than to write it**.

When your project reaches a certain point where your forget the exact details of implementation you have to restore the details by searching it in documentation and by reading the code and trying to understand not only what it does, but why it does that. This process often leads to emotional discussions about the state of this project and skills of a person who wrote this code, even if that person is the one who reads this code right now. This can result in desire to throw the whole thing away and start from scratch. And refactoring by rewriting huge parts can be very expensive process. 

Obviously, there are cases when complex system can not be easiy extended without affecting it's other parts. Most of us saw some good old-fashioned spaghetti code, that covered a lot of conditions and contained massive amount of logic, but was very hard to read.

![Spaghetti](/images/5_cognitive_biases_development/spaghetti.jpg)

Fixing bugs or adding new features in such code can result in a [Hydra Code](https://blog.codinghorror.com/new-programming-jargon/) - the situation when fixing one of the problems results in breaking another functions or new bugs. And leaving the system in this state will surely not make further development easy. 

Take a look at the story about [test-driven development in Oracle Database](https://news.ycombinator.com/item?id=18442637). Sure, good test coverage and TDD practices can help to manage code quality, but if your project will fall apart if you remove extremely long and complex tests and pipelines then this project is definetely not an easy one to read and understand.

## Instagram effect

![Insta vs Reality](/images/5_cognitive_biases_development/insta_vs_reality.jpg)  
https://www.instagram.com/geraldinewest_/

Software solutions can be complex not only in the complexity of the source code of applications. Modern systems tend to use many different frameworks, libraries, and languages united in large complexes by a convoluted architecture. While the code of applications can be in a good shape and written by all rules, there can exist libraries you are not familiar with, algorithms you never heard of and patterns in languages you have not seen before.

The first subconsious reaction for many people is to ignore unknown pieces of puzzle. The motive is easy to understand - our brain tries to save the resources dividing the components into 2 categories: once you known and completely new. And if there are only few new components, for example one unknown library or new algorithm, it is easier to understand it in comparison with a system with a multiple unknown to user components.

I like the analogy with an Instagram here. Instagram is full of great pictures where peoply enjoy the life chilling on beach with a colorful cocktail in hand or spend whole days eating pretty food, traveling to new destinations and so on. But many times those pictures are very distant from the real way it happened and staged.

![Your company](/images/5_cognitive_biases_development/your_company.png)

Same approach can be applied to the code. When you look at complicated and clever solutions most likely it took a lot of time and resources to implement it, but all you see - a smooth and clean result. It is easy to think "Wow, they are really smart!". It is easy to fall into this fallacy, but complex solutions always require a lot of work, testing and iterations. 

There is a pretty interesing way to use fear of trying to understand the unknown things. Say you are coming to a new job or a team and you want to make an impression of yourself. Start using obscure and complex solutions right away! There is a good chance your new teammates will think you know much more than they do. Surprisingly, it works extremely well and I saw it many times in different companies. Needless to say, true state of the things becomes very clear after some time.

<!---
http://gamedevwithoutacause.com/?p=1329
Appeal to authority

For many programmers, the toughest barrier preventing them from reading code may be saying to themselves: “The person who wrote this just might be smarter than I am.”

https://medium.com/@mrlauriegray/the-way-to-read-other-peoples-code-without-ending-up-crying-dd71fee6d005 

compare with instagram

https://dev.to/dangolant/other-peoples-code-and-the-intentional-fallacy-5djd

code myopia, that tunnel vision that sets in after you've been plugging away at something for so long that you've lost track of the overall goal

https://en.wikipedia.org/wiki/Illusory_truth_effect 
-->


## First-come

https://en.wikipedia.org/wiki/Default_effect

Anchoring
Первое попавшееся решение принмиается чаще всего. Привычка и желание не думать каждый раз полный цикл: версионирование, копипаст из ридми, дефолтный конфиг. - todo найти как это называется.


## How To Choose Between

If we successfully avoided traps of choosing first available solutions we will end up with a dillema: which one of si,ilar altertives to pick?

Choosing one thing from multiple is hard. 

You can use techniques like that https://en.wikipedia.org/wiki/Ishikawa_diagram to rationalize your decision.

https://en.wikipedia.org/wiki/Law_of_the_instrument - to NIH
https://en.wikipedia.org/wiki/Pro-innovation_bias

NIH/IH
IH - opposite of NIH,
Also see: IKEA Effect, Halo effect, Post-purchase rationalization

## Teamwork: Bikeshedding, Camel 


Bikeshedding
law of triviality
Споры о минорных функциях - байкшеддинг, например котлин и экстеншены.

Camel - a horse designed by a committee


## Links

Dirty hacks in video game development — https://www.gamasutra.com/view/feature/132500/dirty_coding_tricks.php   




Frontend

https://github.com/denysdovhan/wtfjs
http://browserhacks.com/
google closure compiler

https://github.com/cristaloleg/sabotage


https://artur-martsinkovskyi.github.io/2018/logical-fallacies-in-programming/	


https://blog.codinghorror.com/new-programming-jargon/
Refuctoring
Hydra Code
Protoduction

https://en.wikipedia.org/wiki/Omission_bias

https://en.wikipedia.org/wiki/Outcome_bias 

https://en.wikipedia.org/wiki/Status_quo_bias

