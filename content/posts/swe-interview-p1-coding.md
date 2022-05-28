---
title: "Software Engineer Interview: Coding"
date: 2022-05-28T16:00:00+03:00
draft: false
tags: [interview, coding]
---


The coding section is almost always present in an SWE interview process. Sometimes even multiple times, for example, for the screening and as one of the technical sections on the onsite interview.

Usually, it's a 30-60 minutes live session.

You and the interviewer enter an online editor([CoderPad](https://coderpad.io/), [HackerRank](https://www.hackerrank.com/)), or you share your screen.
The interviewer gives you a description of the problem and maybe an empty code template or function that you need to complete.

The next step is on you — you ask clarifying questions, make sure that you understood the problem correctly, describe your approach, write the code, and analyze how it will work.

How it can be different from your typical everyday coding experience:
- You will solve an abstract, simplified problem
- There is no need to use IDE and code navigation
- No external libraries
- Syntax highlighting and code auto-completion are absent
- Code style and naming don’t matter much. Just make sure you and your interviewer understand what you wrote.


# Coding Problems

![Are you hired son](/images/11-swe-interview-coding/are-you-hired.png#center)

[LeetCode](https://leetcode.com/) is an industrial standard for coding interview task training. 

It offers thousands of tasks. Most likely, you will not solve them all, but there is no actual need to do it.
Focus on tasks that you will see in the interviews. That means you don’t need to solve math puzzles, problems that require knowledge of very specific algorithms or obscure data structures.

Stick to a list of popular tasks, and it will cover 95% of your interviews.

Here is the list of popular algorithms and data structures:

- Arrays and Strings
- Linked List
- Hash Table
- Sorting
- Binary Search
- Backtracking
- Sliding window
- Two pointers
- Priority Queue
- Recursion
- Tree
- Stack
- Greedy approach
- BFS, DFS
- A-star and Dijkstra
- Union-Find/Disjoint Set

I recommend starting with the famous “Blind 75” list  — [https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU) and its later revision, “Blind 50” — [https://www.techinterviewhandbook.org/best-practice-questions/](https://www.techinterviewhandbook.org/best-practice-questions/).

After that, you can dive deeper into areas you want to improve with LeetCode lists:  [https://leetcode.com/explore/learn](https://leetcode.com/explore/learn).

One of the most frequent questions is how many LeetCode problems are enough to be 100% prepared. There is no universal answer, and it depends on your experience. I’ve seen engineers who cleared Google L5 interview with 30 solved problems and people who solved 900+ and didn’t manage to pass the screenings.

I can share my own experience. 

After I solved 200 problems, I started to feel confident in coding sections and cleared 80% of them.
After I solved 300 problems, I didn’t fail any coding interviews I attended. 
I continued to solve LeetCode to keep myself in shape and got to 400 solved problems, but I never saw significant improvement after 300.

# Timing

![Cat time](/images/11-swe-interview-coding/cat-time.png#center)

In regular life, I encourage developers to not rush with the coding, but during the interview, timing can be an important aspect.

Not all the length of your call will be dedicated to the coding.

That’s how good timing for 45 minutes call should be:

1. (5 minutes) Introduction. Say hi to each other. Check if your mic works, your connection is stable, and ask your questions about this interview.
2. (5 minutes) Read the task and talk about how do you plan to solve it. After you both will agree on implementation — start the coding part.
3. (30 minutes) Coding.
4. (5 minutes) Your time for questions about the company, position, team, product, etc.

As you can see, you can get only **30-35 minutes of coding time**.

Aim for 30-35 minutes for the leetcode-medium question during your preparation. Put on a timer when you approach a new task or repeat the old one. You will be ready when you can solve 80% of medium questions in 35 minute period.

# Communication

Take your time to make sure that you understand the problem. Ask clarifying questions. Jumping straight into coding when you see the question most likely will not be the most productive way.

Multiple times, I wanted to begin working on a problem that I thought I already knew. But after a couple of questions about the data used for this problem and algorithm limitations, this task became a lot easier, and I managed to solve it faster.

Take your time to describe your approach, and verify that this solution will work for this task.

The most important skill in this part is the ability to listen to hints. When the interviewer suggests taking a deeper look at some part of your code — don't take it as an offense. It’s quite the opposite. The interviewer wants to give you a hint and improve your solution.

The ability to hear the interviewer, reflect on your solution, and accept critique is valued way higher than writing a perfect code.

# Complexity Analysis

![](/images/11-swe-interview-coding/big-o-cats.jpg#center)

You should be able to tell how much space and time your algorithm will require. There is no need to get the exact amount of bytes and seconds. Instead, [Big-O notation](https://wikipedia.org/wiki/Big_O_notation) is used.

95% of the time, there is no need to dive deep and create complex formulas with coefficients.

Aim for N^2, N, N * log(N), log(N) values.

# Follow-up Questions

After you have completed the coding task successfully — there is a chance that you will have follow-up questions.

Typical follow-ups can be:

- How would you optimize this code further?
- How would you test this code?
- How this code will work in a multi-threading environment?
- How this code will work on different machines?

Usually, follow-ups will not require you to write new code.

There is an approach for the coding interview when the interviewer starts with a small task that the candidate can finish in 5-10 minutes.
After you make a working solution, the interviewer will add new conditions and limitations to the problem, and the task will become more complex. In this case, you will build a base and expand your solution based on follow-ups.

If you encounter this type of interview, expect 2-3 follow-ups and manage your time using this knowledge — expect each follow-up to take about 10 minutes to analyze and solve.

# Company-Specific Requirements

While it’s a pretty standardized interview nowadays, different companies still do it in their way.

For example, **Meta** puts a very strong accent on speed — in a screening interview you need to solve two medium/hard questions, and only the coded solutions count. On the other side, in **Google** interviews sometimes you don’t even need to finish the code if you found the perfect algorithm and described all its details and caveats.

I have had interviews with companies, that required candidates to write unit tests for the code. In that case, I added extra 5 minutes to the interview schedule to not forget about this requirement.

Compilable code requirement is also a thing that different companies have different opinions on. Most of the time, if your code should be compilable — prepare to either write some tests or to have test data already present.

# Questions

**Should I do a brute-force solution first?**

I’ve seen this suggestion many times. “Even if you know the problem or see a good solution immediately, start with brute force. It will show your progress”.

I don’t recommend doing it, simply because it takes a lot of time - at least 3-5 minutes for a small piece of code. What I suggest, is to mention the simple solution, but ignore the coding part. It can help build up the way to efficient implementation, give you some time to concentrate and think about the problem, but will not waste a lot of precious time.

**Should I mention to the interviewer that I know this problem?**

Very often, different companies give the same problem. Something like [2-Sum](https://leetcode.com/problems/two-sum/) or [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) can be found in both FAANG+ and small startups.

Interviewers and candidates both know that problems are repeated. Chances are, that your honest word will not be enough for the interviewer, and they will still ask you to implement the solution.

Plus, there is still a window for mistakes: during the interview you have limited time, you need to explain your thoughts to a person who you see for the first time, and you can simply be nervous. It can affect your performance and you can find yourself in a less perfect condition than you thought you will be.

The only case where you should mention repeated tasks is when you think it was given to you by mistake. 
Once, I had two coding interviews in the same company, and the interviewer gave me the same task for a second session. I mentioned it, and they agreed that it won't be fair and replaced the problem.

**I work with Java. Should I switch to a less verbose language to minimize the amount of code in the interview?**  

Interview problems usually don't take a lot of space, even in verbose languages like Java, so don't worry about the amount of code.  Use the language that you are most comfortable with.

**Can I use IDE with code completion and syntax highlighting?**

Most of the time, you will write your code in a single file on a single screen, where you won’t need the complex code navigation features. Also, you will not need to use external libraries.

Train to write code without syntax highlights and auto-completion, and you will not have any troubles in any online editor that your interviewer company is using.
