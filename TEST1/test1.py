import torch
import torchvision
print(torch.cuda.is_available())
#a = torch.Tensor(5 ,3)
#a = a.cuda()
#print(a)


def f():
    yield 1
    yield 2
    yield 3
    yield 4

f1 = f()

print([next(f1) for i in range(4)])

def fibonacci():
    a = [1, 1]
    while True:
        a.append(sum(a))
    # add next element for list
        yield a.pop(0)
    # acquire the first element
for x in fibonacci():
    print(x)
    if x > 50:
        break
#only print the number is less than 50
