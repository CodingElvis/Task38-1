#SE Bootcamp T38 - Intro to NLP - Semantic Similarity - Task 1 similarity of words

#we run the first code snippets

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""Similarity output:
Cat-monkey 0.59         simple 0.68
Banana - monkey 0.40    simple 0.73
Banana - cat 0.22       simple 0.68
"""

"""Similarity output:
Cat - monkey 0.59    simple 0.67
Lion - Monkey 0.49   simple 0.79
Lion - Cat 0.38      simple 0.72
"""

"""
Comment: The results of the cat-banana-monkey similarity analysis suggest that:
1. cat and monkey are the most similar - perhgaps because both share the characteristic of being creatures
2. banana and moonkey have an intermediate similarity, the association between creature and its food exists but is weaker
3. banana and cat have the lowest similarity, with no obvious link between them.

We can develop this example further by replacing banana with lion (results shown above)
Here cat-monkey is most similar, lion-monkey next.  Lion - cat is third and comes in around the intermediate level seen with monkey-banana.
It seems surprising here that lion-cat comes in lowest, when lion and cats are most closely genetically related.  A liop is a member of the cat family.
Here, it looks like a factor like "suitability as pets" drives the similarity results more strongly than a biological classification of animal family trees.
"""

""""
Comments on rerunning the "example" file with the simple language model.

1. We get a warning with the results, that the simple model does not take any account of word vectors.
2. We get much lower similarity numbers in general, as shown in the following table
3. The simpler language model still delivers a roughly similar ORDER eg comparing recipes with recipes still generates more similarity than comparing recipes with complaints

                                Full model  Basic model
Complaints average similarity   0.86            0.62
Recipes average similarity      0.89            0.69
Cross average similarity        0.67            0.46
(figures of 1.0 for self-comparison removed from averages calculation)
"""

#we run the other code extracts

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = [
"where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"
]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)