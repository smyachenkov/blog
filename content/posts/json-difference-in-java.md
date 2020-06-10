---
title: "How To Compare JSON Documents In Java"
date: 2020-06-10T00:00:00+03:00
draft: false
tags: [programming, java]
description: "Calculating difference between JSON objects."
---

Sometimes we want to know the difference between 2 or more JSON documents. We may want to do it to display the history of edits of the document to review, validate, and have a chance to roll back these changes.

For example, if we have two documents describing the movie Titanic:

```json
{
 	"name": "Titanic",
  	"length": 195,
  	"genres": ["romance"],
  	"cast": {
  		"Jack": "James Cameron" 
  	}
}
```
and
```json
{
 	"name": "Titanic",
  	"genres": ["romance", "drama"],
	"cast": {
  		"Jack": "Leonardo DiCaprio",
  		"Rose": "Kate Winslet"
  	}
}
```

How can we find the difference between those two? 

# JSON Patch 

[JSON Patch](https://tools.ietf.org/html/rfc6902) is a format for the description of changes in the JSON document. The patch of the Titanic document will look like this:
```json
[
    {
        "op": "replace",
        "path": "/cast/Jack",
        "value": "Leonardo DiCaprio"
    },
    {
        "op": "add",
        "path": "/cast/Rose",
        "value": "Kate Winslet"
    },
    {
        "op": "add",
        "path": "/genres/1",
        "value": "drama"
    }
]
```

Here we can see all the changes: `length` is updated, value for `Jack` in object `cast` is changed, there is a new field `Rose` in `cast` object, and there is a new entry in `genres` array.

There are [libraries for JSON Patch](http://jsonpatch.com/) for many languages, with [zjsonpatch](https://github.com/flipkart-incubator/zjsonpatch) being the most popular solution for Java. Those libraries calculate the differences between two objects.

# Compare Manually

If you don't want to use JSON Patch libraries the comparison of two documents is quite easy to implement yourself.

First of all, we want to deserialize JSON to Java object. For that purpose, we can use [Jackson](https://github.com/FasterXML/jackson) or [GSON](https://github.com/google/gson). A JSON object can be represented as a map with the string key and the value that is either an object or a primitive.

To compare those maps we will execute the following algorithm.

First, we collect the keys from both maps.
```java
List<Difference> differences = new ArrayList<>();
Set<String> keys = new HashSet<>();
keys.addAll(from.keySet());
keys.addAll(to.keySet());
```

Iterate through the collected keys. If the key is absent in the first object, but present in second - create the new ADDED entry. If the key is present in the first object, but is absent in second - create REMOVED entry. If the key exists in both objects  - collect the differences between values for this key in both objects.

```java
keys.forEach(key -> {
  // key is removed
  if (!to.containsKey(key) && from.containsKey(key)) {
    differences.add(
      new Difference(from.get(key), path + key, Operation.REMOVED)
    );
  // new key is added
  } else if (to.containsKey(key) && !from.containsKey(key)) {
    differences.add(
      new Difference(to.get(key), path + key, Operation.ADDED)
    );
  // existing key is modified
  } else {
    differences.addAll(
      compare(from.get(key), to.get(key), path + key + "/")
    );
  }
});
```

To collect the differences between two keys we are going to implement `compare` method for a deep comparison of the values. 

```java 
List<Difference> compare(Object from, Object to, String path)
```
The value of the key can be primitive value, array, or an object, so we need to handle all those situations.
Let's create functions to check if both object belong to the same category.

```java
Set<Class<?>> JSON_PRIMITIVES = Set.of(
  Integer.class, Long.class,
  Double.class, String.class
);

boolean oneIsPrimitive(Class<?> from, Class<?> to) {
  return JSON_PRIMITIVES.contains(to) || JSON_PRIMITIVES.contains(from);
}

boolean bothAreObjects(Object from, Object to) {
  return from instanceof Map && to instanceof Map;
}

boolean bothAreArrays(Class<?> from, Class<?> to) {
  return from == ArrayList.class && to == ArrayList.class;
}
```

And now we are ready to implement `compare`.
```java
private List<Difference> compare(Object from, Object to, String path) {
  var differences = new ArrayList<Difference>();
  var fromClass = from.getClass();
  var toClass = to.getClass();
```
We are going to check if one of the entries is primitive, and that they are not equals. If that is true, we add to our differences 2 new operations: deletion of an old value and addition of a new.
```java
if (oneIsPrimitive(fromClass, toClass)) {
  if (!from.equals(to)) {
    differences.add(new Difference(from, path, Operation.REMOVED));
    differences.add(new Difference(to, path, Operation.ADDED));
  }
}
```
If both entries are objects, then we compare them recursively.
```java
else if (bothAreObjects(from, to)) {
  differences.addAll(
    diff((Map<String, Object>) from, 
         (Map<String, Object>) to,
         path)
  );
}
```
And if both the entries are arrays we recursively compare first `min(fromArray.size(), toArray.size())` elements and then add all extra elements from toArray or remove, if toArray has fewer elements than `fromArray`.
```java
else if (bothAreArrays(fromClass, toClass)) {
  var fromArray = (ArrayList<Object>) from;
  var toArray = (ArrayList<Object>) to;
  var arrayDiffs = new ArrayList<Difference>();
  for (int i = 0; i < Math.min(fromArray.size(), toArray.size()); i++) {
    arrayDiffs.addAll(
      compare(fromArray.get(i), toArray.get(i), path + i + "/")
    );
  }
  // add new to fromArray
  if (toArray.size() > fromArray.size()) {
    for (int i = fromArray.size(); i < toArray.size(); i++) {
      arrayDiffs.add(
        new Difference(toArray.get(i), path + i, Operation.ADDED)
      );
    }
  }
  // remove extra from fromArray
  if (toArray.size() < fromArray.size()) {
    for (int i = toArray.size(); i < fromArray.size(); i++) {
      arrayDiffs.add(
        new Difference(fromArray.get(i), path + i, Operation.REMOVED)
      );
    }
  }
  differences.addAll(arrayDiffs);
}
```
If we do not hit any of those conditions, that means we have a replacement of an old entry with a new, so we just add two more operations. 
``` java
else {
  differences.add(new Difference(from, path, Operation.REMOVED));
  differences.add(new Difference(to, path, Operation.ADDED));
}
```

And that's it! You can use this method to implement a comparison of multiple JSON objects.

Full code from this post is available at https://github.com/smyachenkov/json-diff.