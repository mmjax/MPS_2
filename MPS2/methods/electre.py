import numpy as np


def normalize(dataset):
    n = dataset.shape[0]
    m = dataset.shape[1]
    n_dataset = np.zeros((n, m))
    for j in range(m):
        _max = max(dataset[:, j])
        n_dataset[:, j] = [dataset[i, j] / _max for i in range(n)]
    return n_dataset


def concordance_matrix(dataset, weigths):
    concordance = np.zeros((dataset.shape[0], dataset.shape[0]))
    for i in range(0, concordance.shape[0]):
        for j in range(0, concordance.shape[1]):
            concordance[i, j] = sum(weigths[k] for k in range(0, dataset.shape[1]) if (dataset[i, k] >= dataset[j, k]))
    return concordance


def discordance_matrix(dataset):
    n = dataset.shape[0]
    discordance = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            discordance[i, j] = round(max(dataset[j, :] - dataset[i, :]), 2)
    return discordance


def dominance_matrix(concordance, discordance, c_lim, d_lim):
    dominance = np.zeros((concordance.shape[0], concordance.shape[0]))
    for i in range(0, dominance.shape[0]):
        for j in range(0, dominance.shape[1]):
            if (concordance[i, j] >= c_lim and discordance[i, j] <= d_lim and
                    i != j):
                dominance[i, j] = 1
    return dominance


def lim_concordance_list(concordance):
    return [round(min(x), 4) for x in concordance]


def lim_discordance_list(discordance):
    return [round(max(x), 4) for x in discordance]


def prepare_text_info(dominance, name):
    dominated = [(f'{name[i]}', elem) for i, elem in enumerate(dominance)]
    dominated = sorted(dominated, key=lambda k: sum(k[1]), reverse=True)
    info = '\nМЕТОД ELECTRE\n'
    for ind, el in enumerate(dominated):
        info += f'№{ind + 1}: {el[0]}\n'
    return info


def electre(dataset, name, weigths, c_lim=0.45, d_lim=0.5):
    dataset = np.array(dataset)
    dataset = normalize(dataset)
    concordance = concordance_matrix(dataset, weigths)
    discordance = discordance_matrix(dataset)
    dominance = dominance_matrix(concordance, discordance, c_lim, d_lim)
    print(prepare_text_info(dominance, name))
    return concordance, discordance, dominance

