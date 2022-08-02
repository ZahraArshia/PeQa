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
- We have trained a baseline model based on transformers to check the dataset. you can also check it out on [Google Colab](https://colab.research.google.com/drive/1ErYuA6Rh582AS-BVKBbqw3gzUbZgAWN7?usp=sharing).
- [PeQa paper]() soon!
- [PeQa Blog Post]()

## Getting Started

## Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](./issues).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

I would like to acknowledge both [MUT DeepLearning Lab]() and [MUT NLP lab]() for their financial support.

## License

This project is [MIT](./MIT.md) licensed.
