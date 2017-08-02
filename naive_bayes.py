def train(feature, label, lamd):
    num = len(feature)
    dim = len(feature[0])
    counter = dict()
    counter_label = dict()
    for i in range(0, num):
        if not counter.has_key(label[i]):
            counter[label[i]] = [dict() for dim_i in range(dim)]
            counter_label[label[i]] = 0
        for j in range(0, dim):
            if not counter[label[i]][j].has_key(feature[i][j]):
                counter[label[i]][j][feature[i][j]] = 0
            counter[label[i]][j][feature[i][j]] += 1
        counter_label[label[i]] += 1
    model_x = dict()
    model_y = dict()
    for v in counter_label:
        model_x[v] = [dict() for dim_i in range(dim)]
        for i in range(0, dim):
            k_num = len(counter[v][i])
            for k in counter[v][i]:
                model_x[v][i][k] = (counter[v][i][k] + lamd) / 1.0 / (counter_label[v] + k_num * lamd)
        model_y[v] = (counter_label[v] + lamd) / 1.0 / (num + len(counter_label) * lamd)
    print model_x
    print model_y
    return [model_x, model_y]

def predict(model, feature):
    model_x = model[0]
    model_y = model[1]
    class_num = len(model_y)
    dim = len(feature)
    prob = dict()
    for k in model_y:
        prob[k] = model_y[k]
        for i in range(0, dim):
            prob[k] *= model_x[k][i][feature[i]]
    return prob

if __name__ == "__main__":
    feature = [(1, 'S'), (1, 'M'), (1, 'M'), (1, 'S'), (1, 'S'), (2, 'S'), (2, 'M'), (2, 'M'), (2, 'L'), (2, 'L'), (3, 'L'), (3, 'M'), (3, 'M'), (3, 'L'), (3, 'L')]
    label = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
    model = train(feature, label, 0)
    print predict(model, (2, 'S'))