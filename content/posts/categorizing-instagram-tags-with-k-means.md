---
title: "Categorizing Instagram Tags with K-Means"
date: 2019-03-24T00:00:00+03:00
draft: false
tags: [machine learning, categorization, k-means, instagram]
---
Over the last couple of years Instagram, Facebook and many other social media got rid of chronological order in the post feed. It was a bit frustrating at first, but this decision promotes one part of social media that I like the most: your content can be seen, discovered and rated not only by your friends, but by many other new people. In order to make your content discoverable you can use such features as hashtags, geolocations, tagging other people, etc.

In this post we will talk about choice of hashtags for your post which will make it more discoverable and will show it to as many other people who are interested in similar posts as it's possible. To solve this problem I will try to separate a set of Instagram hashtags from different users by it's categories, so we can always have a good set of hashtags on our hands. Idealy we will end up with a set of categories where each one of them will be specific enough to fit to your particular post, for example about minimalistic architecture photography in Morocco or skydiving in New Zealand.

## Perfect tag

Lets have a quick introduction to Instagram hashtag selection problem. You have to balance two things.   

First, your tags must not be too popular, because they can be easily lost in millions of other posts. For example, such hashtags as [<u>#travel</u>](https://www.instagram.com/explore/tags/travel/) with 380M  posts at this moment or [<u>#photooftheday</u>](https://www.instagram.com/explore/tags/photooftheday/) with 644M posts right now are simply too popular and it's very hard to compete for top place in those categories.  

Second, your tags must be popular enough in their category, there must be some people who update its category with new posts daily. Let's say, our lowest boundary will be 100k posts and highest will be 10m. Those numbers are purely emperic and I got it from my friends who are active Instagram users. This data may be not perfect, it's good enough for first iteration of this task.

After all that numeric criteria your tag must be related to your post and your post category, simply because users want to discover related content.

So, which tags should we consider good enough for our task?

Our perfect tag must:   
• Be specific enough  
• Have between 100k and 10m posts  
• Belong to some group(s)  

## Our Goals

We are going to implement categorization system, that will take tags like <u>#building</u>, <u>#skyscaper</u>, <u>#architecturelovers</u> and <u>#architectureporn</u> and put them in some category that we later will call **Architecture**. Or put tags like <u>#pizza</u>, <u>#pasta</u> and <u>#italy</u> in another category that can be called **Italian Food**.

To acomplish this we want to collect a big number of Instagram posts, extract tags from all of them, and divide those tags into some categories. You may ask: where are we going to find a list of those categories? Here's the beauty of machine learning algorithms: we don't know right now and it's fine! But, using some techniques and algorithms we can separate a huge number of tags into small groups.  

This task is called __Unsupervised Learning__.

In machine learning there are two huge areas: [supervised learning](https://wikipedia.org/wiki/Supervised_learning) and [unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning). The main goal of supervised machine learning is do determine if new data belong to one of already known groups, while unsupervised learning separates data into new categories, unknown before.

We will be using one of the most popular unsupervised machine learning algorithms —  [**k-means**](https://wikipedia.org/wiki/K-means_clustering).

## Dataset

Our dataset consist of sets of hashtags, one set for every instagram post. Single post may contain from 0 to 30 hashtags.

Here's distribution of tags in my dataset:

![Tag distribution](/images/1_categorizing-instagram-tags-with-k-means/tag_count_distribution.png)

From this data we can already make some quick assumption. Most popular numbers of hashtags is 1 or 30. It means that there are two categories of users: first pust one most meaningfull tag and move on to next post without spending lot's of time on choosing popular tags, and other milks hashtag machine with every possible opportunity :)

Posts without any tags are excluded from this dataset because they dont provide anything for our task.

We don't need any other information from posts except list of tags — we dont care about author, location or number of likes. Our input data will look like list of arrays of tags, where each line represents one single post:

```
. . .
{artofvisual,instamoment,spain,photo,andalucia,instalike,igersspain}
{artofvisual,photos,nature,andalucia,instamoment,pic,spain,seville}
{picture,exposure,instalike,photoftheday,igers,spain,picoftheday}
{instamoment,picoftheday,photoftheday,picture,exploreeverything,igers}
{christmas,photoftheday,picoftheday,moment,pic,igers}
{ramennoodles,ramen,vegan,veganfood,whatveganseat,berlin,japanese,weekend}
{summer,frozenyogurt,oreo,mango,blueberry}
{photography,see,love,pic,mountains,view,picture,mood,dream,day,nature,pictureoftheday}
{autumn,tofu,instadaily,whatveganseat,lunch,vegan,pumpkin}
{hamburger,manhattan,fries,vegan,downtown,vacation,nyc}
{naturewalk,zipline,archery,sunset,cycling,hiking,kenya}
{sunsetlover,sunset,lovephotography,mobilephotography,sunsetsky,mobileclick,visionofpictures}
{flowers,shadow,simplicity,spring,minimalism,home,nature,sunny,weekend,tulips,morning,still,mood}
. . .
```
## Measuring tf-idf for tags

We are going to place our posts into some multi-dimensional space, where each dimension represents one hashtag. It will be very sparse space, because each post contains maximum of 30 tags, which means there will be 30 non-zero coordinate values, while all other coordinates, couple of thousands of them, will be zeros.

From here lets do all the job on a small sample dataset of 6 posts about Italian food and architecture:
```
0: {italy,food}
1: {food,italy}
2: {food}
3: {italy,architecture}
4: {architecture,italy}
5: {architecture, }
```

As you can see, this dataset has 3 unique hashtags: <u>#italy</u>, <u>#food</u>, and <u>#architecture</u>. It means we are going to deal with 3-dimensional space.

![Empty tag dimension](/images/1_categorizing-instagram-tags-with-k-means/plot_1_empty.png)


Now we need to put our posts into this 3-d-tag space. We will calculate dimension values for every post using [**td-idf**](https://wikipedia.org/wiki/Tf–idf) metric. This metric shows how important is a word in some document, in our case it measures impact of single tag for post. It means that tags with very or very high frequency will be assigned lower rank. 

```
vectorizer = TfidfVectorizer()
posts_coordinates = vectorizer.fit_transform(posts)	
print(posts_coordinates)
```

|              	| 0    	| 1    	| 2   	| 3    	| 4    	| 5   	|
|--------------	|------	|------	|-----	|------	|------	|-----	|
| architecture 	| 0    	| 0    	| 0   	| 0.75 	| 0.75 	| 1.0 	|
| food         	| 0.75 	| 0.75 	| 1.0 	| 0    	| 0    	| 0   	|
| italy        	| 0.65 	| 0.65 	| 0   	| 0.65 	| 0.65 	| 0   	|


![Posts in 3d space](/images/1_categorizing-instagram-tags-with-k-means/plot_2_tags.png)

Posts 0 and 1 contains exeactly the same set of tags, so they have exactly the same coordinates and they are placed on the same position in our tag space. Same goes for the posts 3 and 4, order of tags doesn't matter to us.

This will be our data for following clustering with k-means.

## Applying K-Means 

[K-Means](https://wikipedia.org/wiki/K-means_clustering) is one of the most popular clustering algorithms and it is pretty simple. The only decision you have to make is a number of clusters you want your data to be divided into — _k_ number. The goal of this algorithm is to determine coordinates of _k_ points, which will be centers of mass for a cluster. Those points are also called _centroids_.

This algorithm has 3 steps:	

1. Initialize _k_ cenrtoids with random coordinates
2. Divide all training examples into _k_ groups by choosing the nearest centroid
3. Assign new centroid coordinates by calculating the center of mass for groups from step 2

Steps 2 and 3 are repeated until algorithm is converged or reaches some optimal state. Results may depend a lot on randomly chosen initial centroid values, so calculcations can be run multiple times to get rid of random impact.

Let's see how it works on the example.
 
1. In this image gray squares are training examples and colored circles are initial centroids. All centroids are initialized with random coordinates, training examples are not clustered.  
![K-Means step 1](/images/1_categorizing-instagram-tags-with-k-means/K_Means_Example_Step_1.svg)  
<sup><sup><sup><sup>By I, Weston.pace, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=2463053<sup><sup><sup><sup>
2. Here all training examples are assigned to the closest centroid and marked with its color  
![K-Means step 2](/images/1_categorizing-instagram-tags-with-k-means/K_Means_Example_Step_2.svg)  
<sup><sup><sup><sup>By I, Weston.pace, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=2463076<sup><sup><sup><sup>
3. Now we need to calculate new centroinds for groups created in step 2. This achieved by calculating centers of masses for every training example belonging to a group  
![K-Means step 3](/images/1_categorizing-instagram-tags-with-k-means/K_Means_Example_Step_3.svg)  
<sup><sup><sup><sup>By I, Weston.pace, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=2463081<sup><sup><sup><sup>
4. Clusterisation by distance from newly created centroid is repeated and if we see that there no more iterations required we can stop the algorithm and call this clusterisation final  
![K-Means step 4](/images/1_categorizing-instagram-tags-with-k-means/K_Means_Example_Step_4.svg)  
<sup><sup><sup><sup>By I, Weston.pace, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=2463085<sup><sup><sup><sup>

Now we are going to apply k-means clusterisation to our dataset with posts about Italy. By looking at it we can tell that there are 2 groups: food and architecture. So our _k_-parameter, the number of clusters in which we are going to divide our group, will be 2.

```
KMEANS_CLUSTERS = 2
...
model = KMeans(
    n_clusters=KMEANS_CLUSTERS,
    init='k-means++',
    max_iter=5,
    n_init=1,
    verbose=True
)
groups = model.fit_predict(data)
```

`groups` is an array with a size of initial `data` array 6. And it contains groups ids for entries in `data` in the same order:
```
post 0: 0
post 1: 0
post 2: 0
post 3: 1
post 4: 1
post 5: 1
```

Our dataset was successfully divided into two groups: 0 —  "food" and 1 —  "architecture".

## Extracting Tags For Categories

Lets see where centroids are located.

```
centroids = model.cluster_centers_
```

`centroids` is 2x3 matrix where each row is a coordinates of centroid in 3-dimensional space. Lets add them to our plot.

|   	| architecture 	| food 	| italy 	|
|---	|--------------	|------	|-------	|
| 0 	| 0            	| 0.84 	| 0.43  	|
| 1 	| 0.84         	| 0    	| 0.43  	|

![K-Means centroids](/images/1_categorizing-instagram-tags-with-k-means/plot_3_kmeans.png)

Our categories are located in the same 3-dimendional space as posts from the training example. It means that each category has some a numeric value that represents it's relations to tags - coordinates. If we take absolute values of coordinates and sort them in ascending order - from highest to lowest - we can find tags with most impact on this particular category: it will be tags with lowest value, most closest to a category.

For example, most meaningfull tag for our first centroid(right on the picture) is an <u>#architecture</u>, and for second centroid(left on the picture) its a <u>#food</u>.

Imagine if we have much more tags, let's say 10.000. We will not be interested in all 10.000 relations for eache category, we want only most meaningful tags. So we will limit top tags for each category by some number and show only them. This number will depend on how much clusters we chose.

Let's get back to our example. We are going to limit the number of tags in each category by 2 and pick 2 most meaningful tags.

```
TAGS_IN_CATEGORY = 2
...
ordered_centroids = model.cluster_centers_.argsort()[:, ::-1]	
tags = vectorizer.get_feature_names()

for idx, centroids in enumerate(ordered_centroids):
    print("Centroid %s:" % idx)
    for centroid_tag in centroids[:TAGS_IN_CATEGORY]:
        print("#%s" % tags[centroid_tag])
```

This code separeates our tags into two categories:
```
Centroid 0:
#architecture
#italy
Centroid 1:
#food
#italy
```

Here tags in category are ordered from the most relevant to least. If we take some tags from the top of every category we'll get tags, that can represent this category in shorter way than listing all members. Let's call them _leading tags_. For example, if we choose 1 leading tag from our categories it will be <u>#architecture</u> and <u>#food</u>. 

Let's try this approach on a bigger example. Imagine we have a classifier that produces tag categories with 20 tags and one of the categories looks like that:
```
#boat
#water
#sailing
#ocean
#lake
#ship
#river
#boatlife
#boats
#port
#island
#sail
#yacht
#vacation
#reflection
#sailboat
#fishing
#bateau
#relax
#boating
```

This group clearly unites tags related to boats and sailing. We can give it human-readable name by choosing it's leading tags. Let's say we want to have 3 leading tags, it will be <u>#boat</u>, <u>#water</u> and <u>#sailing</u>. In the next step we will concatenate this tags in a single name so it will look like **boat_water_sailing**.

While working on a large dataset we will end up with a huge list of categories with names like this one, or for example something like **animal_animals_cat**, **goodmorning_coffee_morning** or **sushi_japanesefood_food**.
This human-readable name can help us quickly understand what this group is about and implement groups catalogue, search or group suggestions.

## Result

In this post we've found the way to group instagram tags from a set of instagram posts into a thematic categories.

You can find working demo here: https://github.com/smyachenkov/k-means_tags_demo

I left behind some of the topics, for example choosing k-means parameters like number of categories and number of tags in a single category. I will cover this topics in the next posts.

In conclusion I would like to say that exploring new content can be very fun and some categories have huge amount of awesome content. You can use this knowledge to find new ways to find new people, place your content into right category or to be inspired by something new. 

Keep expressing yourself!