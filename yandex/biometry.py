
"""
Biometry
https://contest.yandex.ru/contest/28413/problems/F/

В данной задаче нужно по звуковым файлам в формате wav предсказать пол человека, речь которого записана на каждом
из файлов (0 – мужчина, 1 – женщина). Для того, чтобы получить OK по этой задаче, нужно получить точность более
98 процентов на тестовом наборе данных. Тренировочный набор данных: https://yadi.sk/d/IUUTPJFOfwn_OQ.
В тренировочном наборе данных есть файл targets.tsv, в котором находятся правильные значения пола для всех записей
в тренировочном наборе данных. Тестовый набор данных: https://yadi.sk/d/K8Z-_gQbspmxkhw. В систему нужно
отправить файл аналогичный targets.tsv из тренировочного набора. То есть для каждого файла id.wav в тестовом
наборе данных в файле ответа должна быть строка вида 'id\tgender'

Примечания
Обратите внимание, что в данной задаче нужно прислать не код, а файл с результатом. Для того, чтобы из звуковых файлов
получить признаки, можно воспользоваться функцией https://librosa.org/doc/main/generated/librosa.feature.melspectrogram.html,
которая для звукового файла вычислит его спектрограмму, то есть матрицу размера число признаков
(задаётся параметром n_mels) на длину записи. Если получен WA, чтобы узнать причину, можно посмотреть отчёт по посылке
и увидеть его в выводе постпроцессора. Причиной такого вердикта может быть как неправильный формат вывода, так и
недостаточная точность.
"""

import os
import random
import pickle
import librosa
import librosa.display
import numpy as np
from tqdm import tqdm
from sklearn.linear_model import LogisticRegression


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def split_train_test(X_arr, Y_arr, split_value):
    assert (len(X_arr) == len(Y_arr))
    split_idx = int(len(X_arr) * split_value)
    return X_arr[:split_idx], Y_arr[:split_idx], X_arr[split_idx:], Y_arr[split_idx:]


def main():

    train_seq_length = 10
    silence_top_db = 20

    # # ---------- read train data ----------

    # train_dirpath = r"H:\Projects\HackerRank\yandex\train"
    # tsv_file = open(os.path.join(train_dirpath, "targets.tsv"))
    # train_lines = tsv_file.readlines()
    # N = len(train_lines)
    # print("train file count: ", N)

    # # parse train data
    # audio_spectrs = list()
    # sexes = np.zeros(N)
    # train_data_length = 0
    # for i in tqdm(range(0, N)):
    #     file_name, sex = train_lines[i].split()
    #     y, sr = librosa.load(os.path.join(train_dirpath, file_name + ".wav"))
    #     yt, index = librosa.effects.trim(y, top_db=silence_top_db)
    #     spectr = librosa.feature.melspectrogram(y=yt, sr=sr)

    #     audio_spectrs.append(spectr)
    #     sexes[i] = int(sex)

    #     if spectr.shape[1] > train_seq_length:
    #         for i in range(0, (spectr.shape[1] // train_seq_length) - 1):
    #             train_data_length += 1
    #         train_data_length += 1

    # # reserve memory
    # X_train = np.zeros((train_data_length, 128 * train_seq_length))
    # Y_train = np.zeros((train_data_length))

    # # fill X and Y train
    # train_data_idx = 0
    # for i in tqdm(range(0, N)):

    #     spectr = audio_spectrs[i]
    #     sex = sexes[i]

    #     if spectr.shape[1] > train_seq_length:
    #         for i in range(0, (spectr.shape[1] // train_seq_length) - 1):
    #             X_train[train_data_idx] = spectr[:, i *
    #                                              train_seq_length:(i+1)*train_seq_length].flatten()
    #             Y_train[train_data_idx] = sex
    #             train_data_idx += 1
    #         X_train[train_data_idx] = spectr[:,
    #                                          -1 * train_seq_length:].flatten()
    #         Y_train[train_data_idx] = sex
    #         train_data_idx += 1

    # # shuffle
    # print("shuffling training data...")
    # train_data = list(zip(X_train, Y_train))
    # random.shuffle(train_data)
    # X_train, Y_train = zip(*train_data)

    # # ---------- save dataset ------------

    # dataset = (X_train, Y_train)
    # save_obj(dataset, "dataset")
    X_train, Y_train = load_obj("dataset")

    # ------------ train -----------------
    print("Training classifier...")
    cls = LogisticRegression(max_iter=2000).fit(X_train, Y_train)

    # ---------- read test data ----------

    test_dirpath = r"H:\Projects\HackerRank\yandex\test"
    test_lines = os.listdir(test_dirpath)
    print("test file count: ", len(test_lines))
    N_test = len(test_lines)
    test_data_length = 0

    out_file = "targets.tsv"
    f = open(out_file, "w+")
    for i in tqdm(range(0, N_test)):
        X_test = list()
        file_name = test_lines[i]
        y, sr = librosa.load(os.path.join(test_dirpath, file_name))
        yt, index = librosa.effects.trim(y, top_db=silence_top_db)
        spectr = librosa.feature.melspectrogram(y=yt, sr=sr)

        if spectr.shape[1] > train_seq_length:
            for i in range(0, (spectr.shape[1] // train_seq_length) - 1):
                X_test.append(
                    spectr[:, i * train_seq_length:(i+1)*train_seq_length].flatten())
            X_test.append(spectr[:, -1 * train_seq_length:].flatten())
            Y_test = int(
                round(sum(cls.predict(np.array(X_test)))) / len(X_test))
        else:
            Y_test = 0
        f.write(str(test_lines[i][:-4]) + " " + str(Y_test) + "\n")
    f.close()


if __name__ == "__main__":
    main()
