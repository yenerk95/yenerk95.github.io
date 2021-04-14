---
layout: post
title:  "Follow the Money Outliers"
date:   2021-04-12 12:43:21 +0200
categories: jekyll update
---
The aim of this project was to cluster the given company descriptions an industry labels and classify them by matching them with target technologies and The Global Industry Classification Standard.

After completing the classification process, we wanted to further examine the outliers by clustering them to see if there are more clusters of interesting technologies that we have missed.

To create cluster summaries, class-based variant of TF-IDF (c-TF-IDF) [BERTopic](https://github.com/MaartenGr/BERTopic) methodology is used. Treated all documents in a single category (a cluster) as a single document and then applied TF-IDF.
Took the top 10 most important words in each cluster. 

Below you can see the visualizations and tables.
## Acquisitions Outliers
### Company descriptions embeddings:

{% include /graphoutlierdesc_updated.html %}

### Cluster Summaries

{% include /tabledesc_updated.html %}

### Industry labels embeddings:

{% include /graphoutlierind_updated.html %}

### Cluster Summaries

{% include /tableind_updated.html %}

## Companies Funded Outliers
### Company descriptions embeddings:

{% include /graphoutliercompanydesc_updated.html %}

### Cluster Summaries

{% include /tablecompanydesc_updated.html %}

### Industry labels embeddings:

{% include /graphoutliercompanyind_updated.html %}

### Cluster Summaries

{% include /tablecompanyind_updated.html %}






