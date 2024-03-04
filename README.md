
---

# Finetuning FinBERT for Stock Market News Sentiment Analysis

This repository contains the code and resources used to finetune the FinBERT model for sentiment analysis of stock market news articles. The objective is to classify the sentiment of financial news headlines and content into three categories: positive, negative, and neutral.

## Dataset

The dataset used for finetuning the FinBERT model is sourced from Kaggle and is preprocessed for sentiment analysis. The preprocessed dataset is available in the repository as `FineTuned_dataset.csv`.

## Finetuning Process

The FinBERT model is finetuned using the preprocessed dataset mentioned above. The finetuning process involves training the model on GPU instances for approximately 5 hours, achieving an accuracy of 81-82%. The notebook used for the finetuning process is `finbert-fine-tuning.ipynb`.

## Kaggle Live Finetuning Process

Additionally, a Kaggle notebook is available for the finetuning process, which was executed on CPU instances. Despite the hardware limitations, the finetuning process on Kaggle achieved a respectable accuracy of 79%. You can access the live finetuning process [here](https://www.kaggle.com/code/meruvulikith/finbert-fine-tuning).

## Hosted Application

The finetuned model is deployed as an application for easy access and usage. You can interact with the sentiment analysis model through the hosted app. The link to the hosted application will be provided [here](https://www.kaggle.com/code/meruvulikith/finbert-fine-tuning).

## Finetuned Model

If you prefer to download and use the finetuned model, it is available on the Hugging Face model hub. You can access the model card [here](https://huggingface.co/likith123/SSAF-FinBert).

## About FinBERT

FinBERT is a specialized language model developed for financial sentiment analysis. It is based on the BERT architecture and is pretrained on a large corpus of financial text. FinBERT is capable of understanding and analyzing financial language, making it suitable for sentiment analysis tasks in the domain of stock markets and finance.

---
