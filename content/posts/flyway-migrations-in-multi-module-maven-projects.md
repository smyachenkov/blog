---
title: "Flyway Migrations in Multi-Module Maven Projects"
date: 2020-01-24T00:00:00+03:00
draft: false
tags: [programming, java, maven, flyway]
---

## What is Flyway

[Flyway](https://flywaydb.org/) is a database migration management tool, which allows you to deliver and validate changes of the database. It's a powerful tool with a lot of useful features, but my favorite use-case is an ability to use Flyway migrations as part of an application. You can execute migrations when application starts, having your DB updated and application deployed in one seamless process. Also, it stimulates you to store migrations code very close to code of your application - in the same project. 

## Common migrations for multiple applications

If you use the Maven build tool you probably have tried or seen multi-module projects. Such a structure can be useful when you want to keep similar projects, common libraries, and resources together in a single repository. This approach can help in a development process in situations when you update one common component and then you have to make new updates for every other repository which uses those components. If you use multi-module projects all those changes can be done in one single pull request.

Sometimes you need to store Flyway migrations as a common resource that can be accessed by any of the modules in your application. For example, if all your applications need to use the same version of the database and you need to ensure that the deployment of any of those apps will migrate the database to the target version.

The most reliable way to do it is to move all those migrations to the new module, package it as jar and include it to all required submodules.

Let's say we have a project with 2 modules and we want to share a set of migrations between them:
```
V1__init.sql
V2__account_add_field.sql
```

One approach is to put them in a directory and use the filesystem path, but this way those files have to be present every time you run the jar. This adds a layer of complexity to build and distribution, and running a single jar is a lot easier without knowing that there are have to be some other files nearby. 

To do that, we need to create a new module, package it as jar and include it in required projects.
Now those files can be found using classpath. 

## How to implement

For example, let's implement this approach using Spring Boot

Let's say we have two modules - `first` and `second`, which require common migrations, and module `commonmigrations` which contains said migrations.

First, we need to create parent pom:
```xml
<project>
    <groupId>com.smyachenkov</groupId>
    <artifactId>multimodule-flyway-demo</artifactId>
    <packaging>pom</packaging>
    <version>1.0</version>
    <modules>
        <module>commonmigrations</module>
        <module>first</module>
        <module>second</module>
    </modules>
</project>

```

pom.xml of `commonmigrations` module:
```xml
<project>
    <artifactId>commonmigrations</artifactId>
    <packaging>jar</packaging>
    <parent>
        <artifactId>multimodule-flyway-demo</artifactId>
        <groupId>com.smyachenkov</groupId>
        <version>1.0</version>
    </parent>
</project>
```

Also, in this module in the `src/main/resources/migrations` directory, we will store our migrations files.


In pom.xml of `first` and `second` modules we need to include `commonmigrations` dependency:
```xml
<project>
    <artifactId>first</artifactId>
    <parent>
        <artifactId>multimodule-flyway-demo</artifactId>
        <groupId>com.smyachenkov</groupId>
        <version>1.0</version>
    </parent>
    <dependencies>
        <dependency>
            <groupId>com.smyachenkov</groupId>
            <artifactId>commonmigrations</artifactId>
            <version>1.0</version>
        </dependency>
    </dependencies>
</project>
```

For both modules, we need to specify migrations location which will be resolved in the application. Here we only need to specify directory name in resources. 
```yml
flyway:
	enabled: true
	locations: classpath:migrations
```

That's all, now common migrations are available for both applications and you can store them in a single place or even in a single repository.

## Links
You can find full sample project with the code from this post here: https://github.com/smyachenkov/multimodule-flyway-demo

