# -*- coding: utf-8 -*-
"""TextSummarizationNoteBook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WHISFhwsQedgfRf4LZaeROnpymqOmmB6
"""

!pip install transformers
!pip install sentencepiece

from transformers import pipeline, PegasusTokenizer, PegasusForConditionalGeneration

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

from google.colab import files
uploaded = files.upload()
content = uploaded

ARTICLE = content
ARTICLE = str(content)

print(summarizer(ARTICLE, max_length=1300, min_length=30, do_sample=False)) # BERT

# PEGASUS
ARTICLE_TO_SUMMARIZE = (
ARTICLE
)
inputs = tokenizer(ARTICLE_TO_SUMMARIZE, return_tensors="pt")

# Generate Summary
summary_ids = model.generate(inputs["input_ids"])
tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]