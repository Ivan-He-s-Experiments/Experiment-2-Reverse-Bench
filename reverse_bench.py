import requests
import random
import json
import itertools
import pickle

# Import and download necessary NLTK data for tokenization.
import nltk
from nltk.translate.bleu_score import sentence_bleu

nltk.download('punkt')

# Import the ROUGE metric implementation.
from rouge import Rouge

rouge = Rouge()
import os
import openai

model_name = "Meta-Llama-3.1-405B-Instruct"
def getResponse(message):
    client = openai.OpenAI(
        api_key="APIKEY",
        base_url="https://api.sambanova.ai/v1",
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "system",
                   "content": "You are a helpful assistant that echoes the user's input, but backwards, do not simply rearrange the words, reverse the user's input down to the character (e.g. reverse Hello World to dlroW olleH). Surround the backwards version of the user's input with <back> </back> tags."},
                  {"role": "user", "content": f"{message}"}],
    )

    return response.choices[0].message.content


# Define helper functions for character-level accuracy and precision.
def char_accuracy(true_output, model_output):
    # Compare matching characters in corresponding positions.
    matches = sum(1 for c1, c2 in zip(true_output, model_output) if c1 == c2)
    # Account for any extra characters in either string.
    total = max(len(true_output), len(model_output))
    return matches / total if total > 0 else 1.0


def char_precision(true_output, model_output):
    # Here, precision is defined as matching characters divided by the length of the model's output.
    matches = sum(1 for c1, c2 in zip(true_output, model_output) if c1 == c2)
    return matches / len(model_output) if len(model_output) > 0 else 0.0


from datasets import load_dataset

# Use name="sample-10BT" to use the 10BT sample.
fw = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2024-10", split="train", streaming=True)

# Get 10 samples.
samples = list(itertools.islice(fw, 10))
word_threshold = 200
acc = []
pres = []
bleu = []
rouges = []
for x in samples:
    nextt = x["text"].split(" ")
    for n in range(len(nextt) // word_threshold):
        inp = nextt[word_threshold * n:word_threshold * (n + 1)]
        inp = " ".join(inp)

        # Ground truth: reverse the input (character by character)
        true_output = inp[::-1].replace("\n", "")
        print("True output:", true_output)
        # print(inp)

        # Get the model output.
        model_output = getResponse(inp)
        if "</think>" in model_output:
            think_end = model_output.find("</think>")
            # print(think_end)
            # print(model_output)
            model_output = model_output[think_end:-1]
            # print(model_output)
        tag1 = model_output.find("<back>")
        tag2 = model_output.find("</back>")
        model_output = model_output[tag1 + 6:tag2 - 5]
        print("Model output:", model_output)
        # print(model_output[::-1])

        # Tokenize both outputs for BLEU calculation.
        reference_tokens = nltk.word_tokenize(true_output)
        candidate_tokens = nltk.word_tokenize(model_output)

        # Compute BLEU score (using the single reference).
        bleu_score = sentence_bleu([reference_tokens], candidate_tokens)
        print("BLEU score:", bleu_score)

        # Compute ROUGE scores.
        rouge_scores = rouge.get_scores(model_output, true_output)
        print("ROUGE scores:", rouge_scores)
        accuracy_metric = char_accuracy(true_output, model_output)
        precision_metric = char_precision(true_output, model_output)
        print("Character Accuracy:", accuracy_metric)
        print("Character Precision:", precision_metric)
        print("-" * 80)
        acc.append(accuracy_metric)
        pres.append(precision_metric)
        bleu.append(bleu_score)
        rouges.append(rouge_scores)

with open(f'accuracy-{model_name}.pkl', 'wb') as file:
    pickle.dump(acc, file)
with open(f'precision-{model_name}.pkl', 'wb') as file:
    pickle.dump(pres, file)
with open(f'bleu-{model_name}.pkl', 'wb') as file:
    pickle.dump(bleu, file)
with open(f'rouge-{model_name}.pkl', 'wb') as file:
    pickle.dump(rouges, file)