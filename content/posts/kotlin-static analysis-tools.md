---
title: "Kotlin Static Analysis Tools"
date: 2019-06-16T00:00:00+03:00
draft: false
tags: [programming, kotlin]
---

[Kotlin](https://kotlinlang.org/) did an amazing job saving and including into its scope most of all valuable Java libraries, frameworks, and tools. But there is one type of a tool that can't be easily imported and reused — [static code analyzers](https://wikipedia.org/wiki/Static_program_analysis). Java developers implemented a lot of tools for code analysis, if you worked with Java you might be familiar with some of the following projects: [PMD](https://pmd.github.io/), [checkstyle](http://checkstyle.sourceforge.net/), [findbugs](http://findbugs.sourceforge.net/), [spotbugs](https://spotbugs.github.io/), etc. Sadly, those projeсts cannot be reused for different languages with different syntax and rules, such as Kotlin.  

## Why do we need static analyzers

JetBrains Team suggests to use built-in inspections and rules in IntelliJ IDEA, but relying only on an IDE is not enough. It might be sufficient for very small projects with a single contributor, but it's definitely not enough for huge projects that require teamwork and multiple contributors. Your team members are not perfect and can forget to fix inspection or leave it intentionally because they don't want to spend time on it. For those reasons we need tools that can be triggered on a build and fail pipelines, protecting your project codebase from bugged and unreadable code. 

![DevOps Cycle](/images/3_kotlin_static_analysis_tools/devops_cycle.png)

In the CI/CD cycle, static analyzers are located in the TEST stage and check, if new builds have errors, vulnerabilities, or if the number of code smells or potential bugs exceeds some threshold.

In this post, I will take a look at popular tools for code analysis and implement custom rules for them.

Let's see what Kotlin infrastructure has to offer.

## ktlint

[ktlint](https://ktlint.github.io/) is a very powerful Kotlin static analyzer. It can be run as a command line tool, as a Gradle task, or as a maven plugin.
It's a simple and reliable tool, and I won't stop here for a long time, because ktlint documentation contains all the code samples required for successful ktlint integration.

The subject I want to focus on more is the creation of custom rules and rulesets.

All the code analyzers use the same pattern — visitor for all the elements of an [abstract syntax tree](https://wikipedia.org/wiki/Abstract_syntax_tree). And every rule makes a stop at every element of this tree: import directives, functions, constructors, method calls, arguments lists — every language element. 

``` Kotlin
class CustomRule: Rule("custom-rule") {
    override fun visit(node: ASTNode,
                       autoCorrect: Boolean,
                       emit: (offset: Int,
                              errorMessage: String,
                              canBeAutoCorrected: Boolean
                       ) -> Unit
    ) {
        if (node.elementType == KtNodeTypes.FUN) {
            emit(node.startOffset, "Wrong function", false)
        }
    }
}
```

This rule will trigger on every function in the project. 

Let's do a more realistic case and trigger rules if a function name is longer than 20 symbols.

``` Kotlin
private const val MAX_LENGTH = 20

class FunctionNameLength : Rule("function-name-length") {
    override fun visit(node: ASTNode,
                       autoCorrect: Boolean,
                       emit: (offset: Int,
                              errorMessage: String,
                              canBeAutoCorrected: Boolean
                       ) -> Unit
    ) {
        if (node.elementType == KtNodeTypes.FUN) {
            node.children()
                    .first { it.elementType == KtTokens.IDENTIFIER }
                    .takeIf { it.textLength > MAX_LENGTH }
                    ?.let {
                        emit(
                                it.startOffset,
                                "Function name ${it.text} is longer than allowed $MAX_LENGTH symbols",
                                false
                        )
                    }
        }
    }
}
```

And that's almost all the code you have to write!

To complete the project, you need to implement your `RuleSetProvider` class, where you specify all the rules, that your ruleset contains:

``` Kotlin
class CustomRuleSetProvider : RuleSetProvider {
    override fun get() = RuleSet(
            "custom-ruleset",
            FunctionNameLength()
    )
}
```

Also, you need to create a service file *com.pinterest.ktlint.core.RuleSetProvider* in project's META_INF directory /resources/META-INF/services/. The content of this file should be the full name of your RuleSetProvider class, for example, com.mycustomruleset.CustomRuleSetProvider.

You can build this project using Gradle with a couple of dependencies: 

``` Groovy
apply plugin: "kotlin"

repositories {
    jcenter()
}

dependencies {
    compileOnly "com.github.shyiko.ktlint:ktlint-core:$ktlintVersion"
    testCompile "com.github.shyiko.ktlint:ktlint-core:$ktlintVersion"
    testCompile "com.github.shyiko.ktlint:ktlint-test:$ktlintVersion"
}
```

The whole project structure should look like this:

```
src/
  main/
    resources/
      META-INF/
        services/
          com.pinterest.ktlint.core.RuleSetProvider
    kotlin/
      ktlintrules/
        CustomRuleSetProvider.kt
        FunctionNameLength.kt
build.gradle
```
Here you can find the working example of a custom ktlint rule implementation: https://github.com/smyachenkov/kt-ruleset/tree/master/ktlint-rules.

## detekt

[detekt](https://github.com/arturbosch/detekt) is very similar to ktlint. It can be used as a build stage or as the [ruleset for SonarQube](https://github.com/arturbosch/sonar-kotlin).

There is a little difference between ktlint and detekt approaches. ktlint is focused on a minimalistic default configuration — you just can run the ktlint command without any arguments. The rationale of such an approach is to not spend your valuable time on tools configuration and focus more on the code of your project. On the other side, detekt makes it a lot easier to configure long and complex rulesets, rule inclusion, properties, weights, thresholds, etc. All this configuration can be set in [YAML config file](https://arturbosch.github.io/detekt/configurations.html).

The main difference between the implementation of ktlint and detekt rules is that ktlint makes you manually check every element of an AST, while detekt provides you a big number of visit methods, that visit only specific language elements, such as constructor, import directives, named functions, lambdas, etc.

``` Kotlin
class CustomRule(config: Config = Config.empty) : Rule(config) {

    override val issue = Issue(
            javaClass.simpleName,
            Severity.CodeSmell,
            "Code smell",
            Debt.FIVE_MINS
    )

    override fun visitCallExpression(expression: KtCallExpression) {
        report(CodeSmell(
                issue,
                Entity.from(expression),
                "It's a code smell!"))
    }

    override fun visitLambdaExpression(lambdaExpression: KtLambdaExpression) {
        report(CodeSmell(
                issue,
                Entity.from(lambdaExpression),
                "It's a code smell!"
        ))
    }

    override fun visitClass(klass: KtClass) {
        ...
    }

    override fun visitAnnotation(annotation: KtAnnotation) {
        ...
    }

    ...

}
```

Otherwise, both projects are pretty similar, and it won't cost you much to implement the same rule for both ktlint and detekt. 

Let's implement our FunctionNameLength rule.

``` Kotlin
private const val MAX_LENGTH = 20

class FunctionNameLength(config: Config = Config.empty) : Rule(config) {

    override val issue = Issue(
            javaClass.simpleName,
            Severity.CodeSmell,
            "Code smell",
            Debt.FIVE_MINS
    )

    override fun visitNamedFunction(function: KtNamedFunction) {
        function.name?.let {
            if (it.length > MAX_LENGTH) {
                report(
                    CodeSmell(
                        issue,
                        Entity.from(function),
                        "Function name ${function.name} is longer than allowed $MAX_LENGTH"
                    )
                )
            }
        }
    }
}

```

The custom detekt ruleset project looks a lot like ktlint. It has almost the same structure:

```
src/
  main/
    resources/
      META-INF/
        services/
          io.gitlab.arturbosch.detekt.api.RuleSetProvider
    kotlin/
      detektrules/
        CustomRuleSetProvider.kt
        FunctionNameLength.kt
build.gradle
```

The differences are in the name of the service file — it should be named *io.gitlab.arturbosch.detekt.api.RuleSetProvider*, and in a slightly different RuleSetProvider implementation:
``` Kotlin
class CustomRuleSetProvider : RuleSetProvider {

    override val ruleSetId: String = "custom-ruleset"

    override fun instance(config: Config) = RuleSet(
            ruleSetId,
            listOf(
                    NoBigDecimalDoubleConstructor(config),
                    NoEmptyLineInMethodBody(config),
                    FunctionNameLength(config)
            )
    )
}
```

To build the project, you will need the following dependencies:

``` Groovy
apply plugin: "kotlin"

repositories {
    jcenter()
}

dependencies {
    compileOnly "com.github.shyiko.ktlint:ktlint-core:$ktlintVersion"
    testCompile "com.github.shyiko.ktlint:ktlint-core:$ktlintVersion"
    testCompile "com.github.shyiko.ktlint:ktlint-test:$ktlintVersion"
}
```

Here you can find an example of the custom detekt rule implementation: https://github.com/smyachenkov/kt-ruleset/tree/master/detekt-rules.


## IntelliJ IDEA

[IntelliJ IDEA](https://www.jetbrains.com/idea/), flagship JetBrains product, it has so much awesome and useful features, that you can discover new ways to code better again and again even if you are already doing it for years. 

In this part, I will show you ways to use IDEA inspections as a part of a project build or CI stage.

### Inspections as a part of the build

If you ever used IDEA, you are familiar with its inspections suggesting improvements in the text editor. It's a big list of known and popular bugs, code smells, style suggestions and best practices for many languages. Right now there are more than 100 Kotlin inspections [bundled in](https://github.com/JetBrains/kotlin/tree/master/idea/src/org/jetbrains/kotlin/idea/inspections) Kotlin plugin for IntelliJ IDEA. Sometimes you wonder — why am I skipping all that pile of knowledge when it can be included in my build or pipeline and prevent so many problems? Well, there are a couple of ways to it

First, IDEA comes with a built-in [command line inspection tool](https://www.jetbrains.com/help/idea/command-line-code-inspector.html). It requires installed IDEA instance, so if you want to go this way — my suggestion is to build a Docker image with installed IntelliJ IDEA in your pipeline and run your project inside this image.

Second, there exist [inspection-plugin](https://github.com/JetBrains/inspection-plugin/), that allows you to run IDEA inspections as a part of Gradle build. Right now this project is still in beta version and frozen, so it's not the best solution for a reliable pipeline, but I hope its development will continue.

### Custom inspections

If you ever tried to create custom inspection for Java in IntelliJ IDEA  you might be familiar with the [structural search](https://www.jetbrains.com/help/idea/structural-search-and-replace.html). It allows you to search elements of code and [create custom inspections](https://www.jetbrains.com/help/idea/creating-custom-inspections.html). It's a pretty easy and quick way to implement new rules.

Unfortunately, the structural search is currently not available for Kotlin language — https://youtrack.jetbrains.com/issue/KT-10176.

![Sad Keanu](/images/3_kotlin_static_analysis_tools/sad_keanu.jpg)

But if you really do want a new inspection, it won't stop you, because it can be implemented via the [IDEA inspection plugin](https://www.jetbrains.org/intellij/sdk/docs/tutorials/code_inspections.html). If you ever have written IDEA plugins, this should be familiar to this type of project, if you didn't do that — it's not that hard, and JetBrains documentation provides good examples. 

There is a couple of Kotlin-specific things you have to keep in mind:  

1. Use `AbstractKotlinInspection` as a parent class of your inspection instead of `AbstractBaseJavaLocalInspectionTool` 

2. Add Kotlin dependency to plugin.xml `<depends>org.jetbrains.kotlin</depends>`

AbstractKotlinInspection implementations share a similar approach with detekt rules: you have a lot of functions, that visit only specific language elements.

``` Kotlin
class CustomInspection : AbstractKotlinInspection() {
    override fun buildVisitor(
        holder: ProblemsHolder,
        isOnTheFly: Boolean
    ): PsiElementVisitor {
        return object: KtVisitorVoid() {

            override fun visitLambdaExpression(lambdaExpression: KtLambdaExpression) {
                holder.registerProblem(lambdaExpression as PsiElement, "Lambda expression problem")
            }

            override fun visitNamedFunction(function: KtNamedFunction) {
                holder.registerProblem(function, "Named function problem")
            }
        }
    }
}
```

Now let's implement our FunctionNameLength rule.

``` Kotlin
private const val MAX_LENGTH = 20

class FunctionNameLengthInspection : AbstractKotlinInspection() {
    override fun buildVisitor(
        holder: ProblemsHolder,
        isOnTheFly: Boolean
    ): PsiElementVisitor {
        return object: KtVisitorVoid() {
            override fun visitNamedFunction(function: KtNamedFunction) {
                function.name?.let {
                    if (it.length > MAX_LENGTH) {
                        holder.registerProblem(
                                function,
                                "Function name ${function.name} is longer than allowed $MAX_LENGTH"
                        )
                    }
                }
            }
        }
    }
}
```

As for any IntelliJ plugin, you need to provide the plugin.xml file in META-INF directory:
```xml
<idea-plugin>
    <id>com.myinspectionplugin.kt-custom-inspection-plugin</id>
    <name>idea-rulesets</name>
    <vendor>Vendor Name</vendor>
    <description>Custom Kotlin ruleset for IDEA inspections</description>
    <depends>org.jetbrains.kotlin</depends>
    <extensions defaultExtensionNs="com.intellij">
        <localInspection language="kotlin"
                         displayName="No empty line in method body is allowed"
                         groupPath="Java"
                         groupBundle="messages.InspectionsBundle"
                         groupKey="group.names.probable.bugs"
                         enabledByDefault="true"
                         level="WARNING"
                         implementationClass="com.myinspectionplugin.FunctionNameLengthInspection"/>
    </extensions>
    <actions>
    </actions>
</idea-plugin>
```

You will need the following dependencies to build this project:
``` Groovy
plugins {
    id 'java'
    id 'org.jetbrains.intellij' version '0.4.9'
    id 'org.jetbrains.kotlin.jvm'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk8"
}

intellij {
    version '2019.1'
    plugins = ['Kotlin']
}
```

Here you can find a full working example of the IDEA inspection plugin for Kotlin code: https://github.com/smyachenkov/kt-ruleset/tree/master/idea-inspections-plugin.


## Conclusion

If you want to see all the inspection from this post in action, [here](https://github.com/smyachenkov/kt-ruleset/tree/master/demo) you can find the sample project, that uses custom ktlint and detekt ruleset.

Static code analysis is an important part of a project builds or pipelines and you don't have to lose it because you switched from Java to Kotlin. There are various configurable and extendable tools to it, such as the ktlint or detekt project. Besides those tools, JetBrains IDE's are very powerful providers of programming language code styles. Right now, adding a new rule or including all IDE's inspections into your pipeline is possible, but can be tricky and it's easier to do it with another tool. Given the growing Kotlin popularity in the last years, we should expect static analyzers for Kotlin to continue to improve and become even better.


## Links 

Repository with projects from this post — https://github.com/smyachenkov/kt-ruleset

ktlint — https://ktlint.github.io/

detekt — https://arturbosch.github.io/detekt/index.html

JetBrains inspection plugin — https://github.com/JetBrains/inspection-plugin

IntelliJ IDEA code inspection plugin implementation tutorial — https://www.jetbrains.org/intellij/sdk/docs/tutorials/code_inspections.html  

IntelliJ IDEA command line code inspector — https://www.jetbrains.com/help/idea/command-line-code-inspector.html