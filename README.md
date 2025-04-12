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
| Model                         | Accuracy | Precision | BLEU   | Rouge-1 (r) | Rouge-1 (p) | Rouge-1 (f) | Rouge-2 (r) | Rouge-2 (p) | Rouge-2 (f) | Rouge-l (r) | Rouge-l (p) | Rouge-l (f) |
|-------------------------------|----------|-----------|--------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Llama 3.3 70B Instruct        | 4.07%    | 5.51%     | 30.33% | 3.08%       | 17.17%      | 5%          | 0.13%       | 0.93%       | 0.23%       | 3.03%       | 16.86%      | 4.90%       |
| Llama 3.1 405B Instruct       | 3.40%    | 4.38%     | 25.12% | 3.69%       | 15.78%      | 5.71%       | 0.33%       | 0.15%       | 0.54%       | 3.58%       | 15.44%      | 5.54%       |
| Llama 3.1 Tulu 3 405          | 2.25%    | 4.51%     | 9.94%  | 24.7%       | 50.3%       | 30.7%       | 14.29%      | 27.42%      | 17.59%      | 24.19%      | 49.29%      | 30%         |
| DeepSeek-R1-Distill-Llama 70B | 2.24%    | 6.4%      | 17.58% | 1.81%       | 12.98%      | 2.94%       | 0.09%       | 0.97%       | 0.17%       | 1.78%       | 12.68%      | 2.89%       |
| Llama 4.1 Maverick            | 0.028%   | 0.058%    | 0.24%  | 0.006%      | 0.006%      | 0.006%      | 0%          | 0%          | 0%          | 0.006%      | 0.006%      | 0.006%      |


## Reasoning Models

Not Available Yet (I hit rate limit while testing ;-;)

# So What?

The Results proove that the models we have are currently not as close to AGI, since humans, given enough time, can do it in their most fluent language.

However, the current best opensourced models failed at this task.

# Next Steps

Try other close sourced models (I don't have money right now tho .___. ) and also Reasoning Models.
