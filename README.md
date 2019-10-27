# askfm-qa-crawler

![img](./docs/image/header.png)

[![license](https://img.shields.io/github/license/tubone24/askfm-qa-clawler.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

> Crawl Ask.fm QA lists and create corpus for ML.

This is a selenium tasks to crawl Ask.fm because of correcting QA list for Machine Learning.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Background

Among machine learning, there was a task to create a bot that responds to natural language using LSTM (a kind of RNN).

At that time, a large amount of conversation corpus is required, but since I did not get a good conversation corpus, I decided to make a conversation corpus by crawling the Ask.fm question answer list with Selenium (Google Chrome) Did.

I'm using Selenium for Python because my favorite programming language is Python.

## Install

### Precondition

- Python 3.6+
- Google Chrome
- [Google Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
  - Check your Chrome version and install suitable driver version.

### PIP

Install dependencies.

```
pip install -r requirements.txt
```

## Usage

### Create faces list (Account list)

Before create conversation corpus, create `face list` because of crawling QA.

First args, number of loop count.

```
python src/get_faces.py 100
```

After run script, get face list into `data/face_list.txt`

### Create conversation corpus

```
python src/main.py
```

After run script, get conversation corpus into `data/askfm_data/foobar.txt`

## Contributing

See [the contributing file](CONTRIBUTING.md)!

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[MIT © tubone.](LICENSE)
