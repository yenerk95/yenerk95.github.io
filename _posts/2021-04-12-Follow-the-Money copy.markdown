---
layout: post
title:  "Follow the Money"
date:   2021-04-12 01:26:21 +0200
categories: jekyll update
---
The goal of this project was to cluster the given company descriptions and the industry labels classify them by matching them with the target technologies and The Global Industry Classification Standard.

For these tasks I used Sentence-BERT: https://arxiv.org/pdf/1908.10084.pdf

Sentence-BERT finetunes a pre-trained BERT network using Siamese and triplet network structures and adds a pooling operation to the output of BERT to derive a fixed-sized sentence embedding vector. The produced embedding vector is more appropriate for sentence similarity comparisons within a vector space

I got the BERT encodings for each sentence in the corpus and then did a semantic search using the cosine similarity to match to a query (either a word or another short sentence).

Below you can see the company description embeddings.

<iframe src="/assets/graphdesc.html" sandbox="allow-same-origin allow-scripts" width="100%" height="500" scrolling="no" seamless="seamless" frameborder="0"> </iframe>
Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

<iframe src="/assets/graphind.html"
sandbox="allow-same-origin allow-scripts"
width="80%"
height="500"
scrolling="no"
seamless="seamless"
frameborder="0">
</iframe>

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
