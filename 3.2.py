import random

counter = 0
heads = 0
tails = 0
while counter != 100:
    flip = random.randint(0,1)
    if flip == 0:
        heads += 1
    if flip == 1:
        tails += 1
    counter += 1
print(f"После 100 подбрасываний мы получили {heads} орлов и {tails} решек")