# ref http://blog.csdn.net/a819825294/article/details/51172466
# ref https://www.zhihu.com/question/47744216?from=profile_question_card
# ref http://www.cnblogs.com/happylion/p/4169945.html
import math

def inner_product(w, x):
    product = 0
    for i in range(0, len(w)):
        product += w[i] * x[i];
    return product

def train(feature, label, lr, steps):
    num = len(feature)
    dim = len(feature[0]) + 1
    for i in range(0, num):
        feature[i].append(1)
    w = [0 for i in range(0, dim)]
    for s in range(0, steps):  #iteration
        loss = 0
        gradient = [0 for i in range(0, dim)]
        for i in range(0, num):
            product = inner_product(w, feature[i])
            loss += label[i] * product - math.log(1 + math.exp(product))
            for j in range(0, dim):
                gradient[j] += feature[i][j] * (label[i] - 1 / (1 + math.exp(-product)))
        loss = -loss / num
        print 'interation ' + str(s) + ', loss = ' + str(loss)
        for j in range(0, dim):
            gradient[j] = -gradient[j] / num
            # update
            w[j] = w[j] - gradient[j] * lr
    return w

def predict(model, feature):
    dim = len(feature[0]) + 1
    feature.append(1)
    product = inner_product(model, feature)
    p1 = math.exp(product) / (1 + math.exp(product))
    p0 = 1 - p1
    return [p1, p0]

if __name__ == "__main__":