import json
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

model_path = './model'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForTokenClassification.from_pretrained(model_path)

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
#example = "My name is Wolfgang and I live in Berlin"

#ner_results = nlp(example)
#print(ner_results)

def handler(event, context):
    try:
        # loads the incoming event into a dictonary
        body = json.loads(event['body'])
        #'inputs': "My name is Sarah Jessica Parker but you can call me Jessica"
        # uses the pipeline to predict the answer
        # ner_results = question_answering_pipeline(question=body['question'], context=body['context'])
        ner_results = nlp(body['inputs'])
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            "body": json.dumps({'answer': ner_results})
        }
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }