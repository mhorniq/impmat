f#%%

from scipy.io import loadmat
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def import_file(path, file_name, signal_source=None, n_max=0, sub_lane=0):

    if signal_source is not None:
        os.chdir(path)  # changing working directory
        dataset_file = loadmat(file_name)  # using loadmat to import matfile and save it in var
        extract_signal = dataset_file[signal_source]  # picking signal from its source
        signal_raw = np.array(extract_signal)  # converting to numpy array
        signal_original = signal_raw[sub_lane, :]  # choosing the sequence from source (signal stored as line)
        # signal_original = signal_raw[:, sub_lane]  # choosing the sequence from source (signal stored as column)

        if n_max == 0:
            n_max = signal_original.shape[0]

        if n_max > signal_original.shape[0]:
            print('NOTE: n_max = ', n_max,'> length of the signal ( signal length =', signal_original.shape[0], ')')
            n_max = signal_original.shape[0]
            print('n_max set to ', n_max)

        # reduce n_max to make load less amount of values faster
        # add or remove slicing to apply script on the whole values
        signal_original = signal_original[0:n_max]  # slicing

        print('Importing: ', file_name)  # verbose process

        return signal_original  # numpy darray as output

    else:
        os.chdir(path)  # changing working directory
        dataset_file = loadmat(file_name)  # using loadmat to import matfile and save it in var

        data = {}
        i = 0
        for item in dataset_file:
            data[i] = dataset_file[item]
            print('data[%s]' % i, item, dataset_file[item])
            i += 1

        main_df = pd.DataFrame()

        main_data = np.transpose(data[3])
        # print(main_data)
        # print(main_data.shape)

        for i in range(main_data.shape[0]):
            # print(i)
            main_df[i] = main_data[i]
            # print(main_df)

        # ADD OUTPUT AS PANDAS DATAFRAME, NUMPY MULTIDIM ARRAY, DICTIONARY AND RAW DICTIONARY HERE
        return main_df, main_data, data, dataset_file

# path = 'D:\\OneDrive\\Documents\\!study\\THM\\M.Sc. BMT Sem. 1\\Laborpraktikum\\Evozierte Potenzialen\\LAEP\\Testdata\\'
# file1 = 'EEGChirps.mat'
# file2 = 'EEGKlicks.mat'


# file1_df, file1_data, file1_raw_data, file1_dataset = import_file(path, file1)

#%%
# type(file1_df)
# file1_df.plot()
# plt.show()
