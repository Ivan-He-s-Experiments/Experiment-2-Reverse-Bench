# Experiment-2-Reverse-Bench

## Benchmark Introduction

### Purpose:

Evaluate's a models ability toe use context and ability to reason.

### Goal:

Reverse the input.

E.g. Input: Hello World. Output: .dlroW olleH

### Format:

Text Generation (English)

## Results


## Normal Models
| Model                  | Accuracy  | Precision | BLEU   | Rouge-1 (r/p/f)          | Rouge-2 (r/p/f)          | Rouge-l (r/p/f)          |
|------------------------|-----------|-----------|--------|--------------------------|--------------------------|--------------------------|
| Llama 3.3 70B Instruct | 4.08%     | 5.51%     | 30.33  | 3.09% / 17.18% / 5.00%   | 0.14% / 0.93% / 0.24%    | 3.03% / 16.87% / 4.91%   |
| Llama 3.1 405B Instruct| 3.40%     | 4.38%     | 25.12  | 3.69% / 15.78% / 5.71%   | 0.33% / 0.15% / 0.54%    | 3.58% / 15.44% / 5.54%   |
| Llama 3.3 70B Instruct | 4.08%     | 5.51%     | 30.33  | 3.09% / 17.18% / 5.00%   | 0.14% / 0.93% / 0.24%    | 3.03% / 16.87% / 4.91%   |
| Llama 3.1 Tulu 3 405   | 2.23%     | 4.51%     | 9.95   | 24.81% / 50.23% / 30.74% | 14.31% / 27.38% / 17.60% | 24.22% / 49.23% / 30.01% |
| Deepseek V3            | 4.05%     | 4.99%     | 15.42  | 24.25% / 34.45% / 26.84% | 12.07% / 16.02% / 13.12% | 23.29% / 33.09% / 25.76% |
| Llama 4.1 Maverick     | 2.87%     | 5.82%     | 24.06  | 0.61% / 0.57% / 0.59%    | 0.00% / 0.00% / 0.00%    | 0.56% / 0.51% / 0.53%    |
| Gemini 2.0 Flash       | **9.19%** | **9.61%** | **47.15** | **61.36% / 64.47% / 61.16%** | **51.19% / 54.35% / 51.46%** | **61.13% / 64.33% / 61.00%** |




## Reasoning Models

Not Available Yet (I hit rate limit while testing ;-;)

# So What?

The Results proove that the models we have are currently not as close to AGI, since humans, given enough time, can do it in their most fluent language.

However, the current best opensourced models failed at this task.

# Next Steps

Try other close sourced models (I don't have money right now tho .___. ) and also Reasoning Models.
