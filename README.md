# BERT Named Entity Recognition API
Created BERT Named Entity Relation(NER) API deployed on AWS ECR

## Hugging Face model

Following Hugging face model was used : [dslim/bert-base-NER](https://huggingface.co/dslim/bert-base-NER) :rocket:

### Model description

bert-base-NER is a fine-tuned BERT model that is ready to use for Named Entity Recognition and achieves state-of-the-art performance for the NER task. It has been trained to recognize four types of entities: location (LOC), organizations (ORG), person (PER) and Miscellaneous (MISC).

Specifically, this model is a bert-base-cased model that was fine-tuned on the English version of the standard CoNLL-2003 Named Entity Recognition dataset. 

### How to use

You can use this model with Transformers pipeline for NER.
```
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Wolfgang and I live in Berlin"

ner_results = nlp(example)
print(ner_results)
```
This model was fine-tuned on English version of the standard CoNLL-2003 Named Entity Recognition dataset.

The training dataset distinguishes between the beginning and continuation of an entity so that if there are back-to-back entities of the same type, the model can output where the second entity begins. As in the dataset, each token will be classified as one of the following classes:

![image](https://user-images.githubusercontent.com/13203059/162643182-61327085-2a6a-40b6-af33-79c8086df1af.png)

![image](https://user-images.githubusercontent.com/13203059/162643218-c682ae47-b518-4788-8d16-9b65e290b787.png)


# AWS deployed ECR - Lambda function

The API is deployed and REST POST call was 200 OK

![image](https://user-images.githubusercontent.com/13203059/162643293-465b6283-b129-4d9d-8250-1e8e3242c6a5.png)

# Streamlit integration 

Following steps can be done to integrate the REST API response to get the UI on streamlit 

https://blog.jcharistech.com/2019/11/28/summarizer-and-named-entity-checker-app-with-streamlit-and-spacy/

## Screenshot

![image](https://user-images.githubusercontent.com/13203059/162646505-95d264a7-9c31-40dc-832f-948978766d39.png)


# References

https://github.com/philschmid/serverless-bert-huggingface-aws-lambda-docker
