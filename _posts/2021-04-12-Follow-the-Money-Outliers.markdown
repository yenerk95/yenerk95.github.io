---
layout: post
title:  "Follow the Money Outliers"
date:   2021-04-12 12:43:21 +0200
categories: jekyll update
---
The aim of this project was to cluster the given company descriptions and  industry labels and classify them by matching them with target technologies and The Global Industry Classification Standard.

After completing the classification process, we wanted to further examine the outliers by clustering them to see if there are more clusters of interesting technologies that we have missed.

Below you can see the visualizations.
## Acquisitions Outliers
### Company descriptions embeddings:

{% include /graphoutlierdesc.html %}

### Topic Creation
#### Class-based variant of TF-IDF (c-TF-IDF)
[BERTopic](https://github.com/MaartenGr/BERTopic) methodology is used. Treated all documents in a single category (a cluster) as a single document and then applied TF-IDF.
Took the top 10 most important words in each cluster. Took the top 50 clusters.
{% include /tabledesc.html %}

### Industry labels embedding:

{% include /graphoutlierind.html %}

## Companies Funded Outliers
### Company descriptions embeddings:

{% include /graphoutliercompanydesc.html %}

### Topic Creation
#### Class-based variant of TF-IDF (c-TF-IDF)
[BERTopic](https://github.com/MaartenGr/BERTopic) methodology is used. Treated all documents in a single category (a cluster) as a single document and then applied TF-IDF.
Took the top 10 most important words in each cluster. Took the top 50 clusters.
{% include /tablecompanydesc.html %}

### Industry labels embeddings:

{% include /graphoutliercompanyind.html %}






