import pickle
import math
model_name = "Meta-Llama-3.1-405B-Instruct"
#model_name="Llama-3.3-70B-Instruct"
with open(f"accuracy-{model_name}.pkl", "rb") as file:
    acc = pickle.load(file)
with open(f"precision-{model_name}.pkl", "rb") as file:
    prec = pickle.load(file)
with open(f"rouge-{model_name}.pkl", "rb") as file:
    rouges = pickle.load(file)
with open(f"bleu-{model_name}.pkl", "rb") as file:
    bleus = pickle.load(file)

def mean(x):
    avg=0
    for i in x:
        avg+=i
    return avg/len(x)
def add_dict(a,b):
    #print(a,b)
    keyss = list(a.keys())
    for key in keyss:

        a[key] += b[key]
    return a
def div_rouge(a,b):
    keyss = list(a.keys())
    for key in keyss:

        a[key] /= b
    return a
def mean_rouges(x):
    original = x[0][0]
    keyss = list(x[0][0].keys())
    for key in keyss:
        avg = x[0][0][key]
        for i in range(1,len(x)):
            avg=add_dict(avg,x[i][0][key])
        original[key]= div_rouge(avg,len(x))
    return original

print(mean(acc))
print(mean(prec))
print(mean(bleus))
#print(add_dict(rouges[0][0]["rouge-1"],rouges[1][0]["rouge-1"]))
print(mean_rouges(rouges))