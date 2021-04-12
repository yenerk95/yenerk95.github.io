---
layout: post
title:  "Follow the Money"
date:   2021-04-12 01:26:21 +0200
categories: jekyll update
---
The goal of this project was to cluster the given company descriptions and the industry labels and classify them by matching them with the target technologies and The Global Industry Classification Standard.

For these tasks I used [pretrained sentence transformers](https://www.sbert.net/index.html) based on [Sentence-BERT](https://arxiv.org/pdf/1908.10084.pdf)

Sentence-BERT finetunes a pre-trained BERT network using Siamese and triplet network structures and adds a pooling operation to the output of BERT to derive a fixed-sized sentence embedding vector. The produced embedding vector is more appropriate for sentence similarity comparisons within a vector space

I got the BERT encodings for each sentence in the corpus and then did a semantic search using the cosine similarity to match to a query (either a word or another short sentence).

Documents with similar topics are clustered together such that we can find the topics within these clusters. To visualize the simiilarities I first needed to lower the dimensionality of the embeddings. I used [UMAP](https://umap-learn.readthedocs.io/en/latest/index.html) for dimensionality reduction as it keeps a significant portion of the high-dimensional local structure in lower dimensionality. After having reduced the dimensionality of the embeddings, I  clustered them  with [HDBSCAN](https://hdbscan.readthedocs.io/en/latest/index.html).

Below you can see the visualizations of the embeddings of the given data.

### Acquisitions, Company descriptions embedding:

{% include /graphdesc.html %}

### Acquisitions, Industry labels embedding:

{% include /graphind.html %}

### Companies, Company descriptions embedding:

{% include /graphcompanydesc.html %}

### Companies, Industry labels embedding:

{% include /graphcompanyind.html %}


