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
| **Model**                     | **Accuracy** | **Precision** | **BLEU** | **Rouge-1 (r/p/f)**             | **Rouge-2 (r/p/f)**            | **Rouge-l (r/p/f)**             |
|-------------------------------|--------------|---------------|----------|---------------------------------|--------------------------------|---------------------------------|
| DeepSeek-R1-Distill-Llama 70B | 2.44%        | 6.41%         | 17.58    | 1.81% / 12.98% / 2.95%          | 0.10% / 0.95% / 0.18%          | 1.79% / 12.69% / 2.90%          |
| DeepSeek R1                   | 4.41%        | 4.83%         | 17.00    | 28.24% / 29.62% / 28.21%        | 16.49% / 18.72% / 17.04%       | 27.49% / 28.94% / 27.53%        |
| Gemini Pro 2.5                | **23.94%**   | **24.17%**    | **83.20**| **92.09% / 92.98% / 92.51%**    | **87.76% / 88.36% / 88.05%**   | **92.04% / 92.92% / 92.45%**    |
| Gemini Flash 2.0 Thinking     | 11.99%       | 12.73%        | 53.82    | 63.00% / 70.34% / 64.06%        | 53.83% / 60.41% / 54.74%       | 61.10% / 68.43% / 62.15%        |


# So What?

The Results proove that the models we have are currently not as close to AGI, since humans, given enough time, can do it in their most fluent language.

However, the current best opensourced models failed at this task.

# Next Steps

Try other close sourced models (I don't have money right now tho .___. ) and also Reasoning Models.
