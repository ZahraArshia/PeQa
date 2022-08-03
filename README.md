<h1><img src="https://i.pinimg.com/originals/40/fd/fb/40fdfb3aa832a7e80485f7c37c0b97ad.gif" width="100" height="100">PeQa (Persian Question-Answering Dataset)</h1>

> Is PeQa a knight? A samurai? A robot? No! It is a MASSIVE **Pe**rsian **Q**uestion **A**nswering dataset! :)

PeQa dataset is a huge dataset of 14 million Persian tweets from tweeter that is meticulously processed to create a rich collection of 420,000 pairs of question-answer data. Therefore, this valuable dataset can be used in many chatbot or other question-answering projects. Although over 14 million pairs of questions and answers were extracted, bout 800,000 pairs are published in .CSV cleaned format for now in this repository for researcher's use.
|  | Total | Unique Questions | Unique Answers 
| :---: | :------------: | :----------------: | :------------------: |
| **Data Count** | 436,072  |127,752  |   308,320|         

The complete 14 million data is also available for free.

Each pair of data consist of a tweet and it's relevant reply, which are considered as a question and it's answer. PeQa dataset consists of tweets and replies, rather than questions and answers, which has some consequences for the type of linguistic patterns it contains. Specifically, a question-answering dataset primarily consists of questions and related answers but in this dataset, a question can be answered by another question.

### Examples
| Question(Tweet) | Answer(Reply) |
| :------------: | :----------------: |
|    اتفاقا تازه سوپ خوردم     |       نوش جان ، چه سوپی ؟       |
|    دانشگاه‌ها هم تعطیل شدند     |         نشدند ، تکذیب شد     |
|    استعفا داده ظریف ؟     |     قبلا استعفا داده_بود وقتی اقای بشار اسد اومده بود ایران         |
|     چرا پنج تا ؟    |       پ چندتا ؟       |
|     پادکست گوش نمیدین ؟    |       تا الان این کارو نکردم       |


## Quick Links
- The raw data is too large to be shown in a repository, you can download it from [here](https://drive.google.com/file/d/1sw1q8iqjGYyHDXU6eIsVtC4PummJvqQv/view?usp=sharing).
- We have trained a baseline model based on transformers to check the dataset. you can also check it out on [Google Colab](https://colab.research.google.com/drive/1ErYuA6Rh582AS-BVKBbqw3gzUbZgAWN7?usp=sharing).
- [PeQa paper]() soon!
- [PeQa Blog Post]()

## Getting Started
### Requirements
The testbench requires [PyTorch](https://pytorch.org/) framework. There are multiple ways to install it:
- Pip:
```
!pip install torch===[version]
```
- Anaconda
```
conda install python=3.6 pytorch torchvision
```
### Encoder
**Computation Graph:**

   1) Convert word indexes to embeddings.
   2) Pack padded batch of sequences for RNN module.
   3) Forward pass through GRU.
   4) Unpack padding.
   5) Sum bidirectional GRU outputs.
   6) Return output and final hidden state.

**Inputs:**

-  ``input_seq``: batch of input sentences; shape=\ *(max_length,
   batch_size)*
-  ``input_lengths``: list of sentence lengths corresponding to each
   sentence in the batch; shape=\ *(batch_size)*
-  ``hidden``: hidden state; shape=\ *(n_layers x num_directions,
   batch_size, hidden_size)*

**Outputs:**

-  ``outputs``: output features from the last hidden layer of the GRU
   (sum of bidirectional outputs); shape=\ *(max_length, batch_size,
   hidden_size)*
-  ``hidden``: updated hidden state from GRU; shape=\ *(n_layers x
   num_directions, batch_size, hidden_size)*

### Decoder
**Computation Graph:**

1) Get embedding of current input word. 
2) Forward through unidirectional GRU. 
3) Calculate attention weights from the current GRU output from (2). 
4) Multiply attention weights to encoder outputs to get new "weighted sum" context vector. 
5) Concatenate weighted context vector and GRU output.
6) Predict next word(without softmax).
7) Return output and final hidden state.

**Inputs:**

- ``input_step``: one time step (one word) of input sequence batch; shape=\ (1, batch_size)
- ``last_hidden``: final hidden layer of GRU; shape=\ (n_layers x num_directions, batch_size, hidden_size)
- ``encoder_outputs``: encoder model’s output; shape=\ (max_length, batch_size, hidden_size)

**Outputs:**

- ``output``: softmax normalized tensor giving probabilities of each word being the correct next word in the decoded sequence; shape=\ (batch_size, voc.num_words)
- ``hidden``: final hidden state of GRU; shape=\ (n_layers x num_directions, batch_size, hidden_size)

### Run Training
Run the `Configure training/optimization` block if you want to train the model.
First we set ***training parameters***, then we ***initialize*** our optimizers, and finally we call the ``trainIters`` function to run our training iterations.


## Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/ZahraArshia/PeQa/issues).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

We would like to acknowledge both [MUT DeepLearning Lab](https://github.com/mut-deep) and [MUT NLP lab](https://github.com/mutnlp) for their financial support.

## License

This project is [MIT](./MIT.md) licensed.
