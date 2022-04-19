import numpy as np


def normalize(dataset, n_dataset, n, m):
    for j in range(m):
        sq = np.sqrt(sum(dataset[:, j] ** 2))
        n_dataset[:, j] = [dataset[i, j] / sq for i in range(n)]
    return n_dataset


def get_worst_best(signs, dataset, m):
    worst = []
    best = []
    for i in range(m):
        fir, sec = (max(dataset[:, i]), min(dataset[:, i])) if signs[i] == 1 else (min(dataset[:, i]), max(dataset[:, i]))
        worst.append(sec)
        best.append(fir)
    return worst, best


def get_worst_best_distanse(dataset, worst, best, n):
    worst_dist = (dataset - worst) ** 2
    best_dist = (dataset - best) ** 2
    worst_dist = np.array([sum(worst_dist[i, :]) ** 0.5 for i in range(n)])
    best_dist = np.array([sum(best_dist[i, :]) ** 0.5 for i in range(n)])
    return worst_dist, best_dist


def __topsis__(dataset, weights, name, signs):
    dataset = np.array(dataset, dtype=float)
    n, m = len(dataset), len(dataset[0])
    n_dataset = np.empty((n, m), np.float64)
    n_dataset = normalize(dataset, n_dataset, n, m) * weights
    (worst, best) = get_worst_best(signs, n_dataset, m)
    (worst_dist, best_dist) = get_worst_best_distanse(n_dataset, worst, best, n)
    return worst_dist / (best_dist + worst_dist)


def prepare_info(res_dataset, name):
    max_ind = np.argmax(res_dataset)
    min_ind = np.argmin(res_dataset)
    max_info = f'\nПродукт {name[max_ind]} лучше всего. Его счет = {res_dataset[max_ind]:.4f}'
    min_info = f'Продукт {name[min_ind]} хуже всех(. Его счет = {res_dataset[min_ind]:.4f}\n'
    res = [f'{name[i]} = {x:.4f}' for i, x in enumerate(res_dataset)]
    res.append(max_info)
    res.append(min_info)
    res = '\n'.join(res)
    print('\nTOPSIS\n')
    print(res)


def topsis(dataset, weights, name, signs):
    res_dataset = __topsis__(dataset, weights, name, signs)
    prepare_info(res_dataset, name)
    return res_dataset
