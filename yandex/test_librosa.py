
import os
import random
import librosa
import librosa.display
import numpy as np
from tqdm import tqdm
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


# def split_train_test(X_arr, Y_arr, split_value):
#     assert (len(X_arr) == len(Y_arr))
#     split_idx = int(len(X_arr) * split_value)
#     return X_arr[:split_idx], Y_arr[:split_idx], X_arr[split_idx:], Y_arr[split_idx:]


# def main():

#     # parse train data
#     dirpath = r"H:\Projects\HackerRank\yandex\train"
#     tsv_file = open(os.path.join(dirpath, "targets.tsv"))
#     train_lines = tsv_file.readlines()
#     print("train file count: ", len(train_lines))

#     N = 20
#     train_seq_length = 10
#     train_val_split = 0.95

#     # count how much memory to reserve
#     audio_spectrs = list()
#     sexes = np.zeros(N)
#     train_data_length = 0
#     for i in tqdm(range(0, N)):
#         file_name, sex = train_lines[i].split()
#         y, sr = librosa.load(os.path.join(dirpath, file_name + ".wav"))
#         yt, index = librosa.effects.trim(y, top_db=20)
#         spectr = librosa.feature.melspectrogram(y=yt, sr=sr)
#         # librosa.display.waveplot(yt, sr=sr)
#         # plt.tight_layout()
#         # plt.show()

#         audio_spectrs.append(spectr)
#         sexes[i] = int(sex)

#         if spectr.shape[1] > train_seq_length:
#             for i in range(0, (spectr.shape[1] // train_seq_length) - 1):
#                 train_data_length += 1
#             train_data_length += 1

#     # reserve memory
#     X_train = np.zeros((train_data_length, 128 * train_seq_length))
#     Y_train = np.zeros((train_data_length))

#     # fill X and Y train
#     train_data_idx = 0
#     for i in tqdm(range(0, N)):

#         spectr = audio_spectrs[i]
#         sex = sexes[i]

#         if spectr.shape[1] > train_seq_length:
#             for i in range(0, (spectr.shape[1] // train_seq_length) - 1):
#                 X_train[train_data_idx] = spectr[:, i *
#                                                  train_seq_length:(i+1)*train_seq_length].flatten()
#                 Y_train[train_data_idx] = sex
#                 train_data_idx += 1
#             X_train[train_data_idx] = spectr[:,
#                                              -1 * train_seq_length:].flatten()
#             Y_train[train_data_idx] = sex
#             train_data_idx += 1

#     # shuffle
#     print("shuffling data...")
#     train_data = list(zip(X_train, Y_train))
#     random.shuffle(train_data)
#     X_train, Y_train = zip(*train_data)
#     X_train, Y_train, X_test, Y_test = split_train_test(
#         X_train, Y_train, train_val_split)

#     # train
#     print("Training classifier...")
#     cls = LogisticRegression(max_iter=1000).fit(X_train, Y_train)

#     # test
#     print("Started classifier evaluation...")
#     preds = cls.predict(X_train)
#     eval_train = (preds == Y_train)
#     precision = len(eval_train == True) / len(preds)
#     print("Train precision: ", precision)

#     preds = cls.predict(X_test)
#     eval_test = (preds == Y_test)
#     precision = len(eval_test == True) / len(preds)
#     print("Test precision: ", precision)


# if __name__ == "__main__":
#     main()


def main():
    f = open("targets.tsv")
    lines = f.readlines()
    for line in lines:
        print(line[:-1])
    f.close()


if __name__ == "__main__":
    main()
