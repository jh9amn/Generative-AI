IMDB Dataset ---> Feature Engineering ---> Simple RNN 
---> (.h5) streamlit Web App ---> Deployement


Simple RNN -> 1) Embeding Layer 
              2) Simple RNN


[RNN Architecture](https://share.google/fVp2pX4wgqwckexzx)


## Word Embedding(Feature Representation)

#### DataSet

Text              o/p
x11 x12 x13 x14    0
x21 x22 x23 x24    1
- - - - - -- -     - 
- - - -- - - -     -


*** 1) One-Hot Emcoding ***

|v| = 10000

man ->  [0]
        [0]
        [0]
        --
        --      sparse matirx => Overfitting
        [1]
        [0]
        [0]


boy ->  [0]
        [0]
        [1]
        --
        --
        [0]
        [0]
        [0]


FOR OVERCOME THIS DISADVANTAGE WE ARE USING

2) Word Embedding (word2vec)

![Alt text](image/Screenshot 2025-11-18 113859.png)
