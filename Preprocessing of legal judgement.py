#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
#from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#from pdfminer.converter import TextConverter
#from pdfminer.layout import LAParams
#from pdfminer.pdfpage import PDFPage
import numpy as np
import pandas as pd
from io import StringIO
from PyPDF2 import PdfReader #For converting PDF to text


# In[2]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


# In[3]:


reader = PdfReader("sample judgement.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"


# In[4]:


lone=text


# In[5]:


f=open('xxx.txt','w')
f.write(lone)
f.close()


# In[6]:


with open('xxx.txt') as f:
    clean_cont = f.read()#Obtain different sentences in form of a list


# In[7]:


from nltk.tokenize import sent_tokenize
token_text = sent_tokenize(clean_cont)


# In[8]:


legal_doc = token_text
legal_doc


# In[9]:


temp = ""
for eachDocument in legal_doc[:]:
        #removes the paragraph lables 1. or 2. etc.
        eachDocument = re.sub(r'(\d\d\d|\d\d|\d)\.\s', ' ', eachDocument)
        #removes dot(.) i.e File No.1063
        eachDocument = re.sub(r'(?<=[a-zA-Z])\.(?=\d)', '', eachDocument)
        #removes dot(.) i.e File No.1063
        eachDocument = re.sub(r'(?<=\d|[a-zA-Z])\.(?=\s[\da-z])', ' ', eachDocument)
        #to remove the ending dot of abbr
        eachDocument = re.sub(r'(?<=\d|[a-zA-Z])\.(?=\s?[\!\"\#\$\%\&\'\(\)\*\+\,\-\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~])', ' ', eachDocument)
        #removes the other punctuations
        eachDocument = re.sub(r'(?<!\.)[\!\"\#\$\%\&\'\(\)\*\+\,\-\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]',' ', eachDocument)
        #remove \n from sentences
        eachDocument = re.sub(r'\n',' ', eachDocument)
        temp = temp+''+eachDocument


# In[10]:


documents = []
temp = temp.replace("  "," ")
documents = temp.replace(" "," ")


# In[11]:


temp


# In[12]:


documents


# In[13]:


original_length = len(documents.split())
original_length


# In[14]:


type(documents)


# In[ ]:




