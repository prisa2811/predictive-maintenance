import pandas as pd

def load_data(file_path):
    column_names = ['unit_number', 'time_in_cycles'] + \
                   [f'op_setting_{i}' for i in range(1, 4)] + \
                   [f'sensor_measurement_{i}' for i in range(1, 22)]
    data = pd.read_csv(file_path, sep=' ', header=None, names=column_names)
    return data

def save_preprocessed_data(data, file_path):
    data.to_csv(file_path, index=False)

if __name__ == "__main__":
    datasets = ['FD001', 'FD002', 'FD003', 'FD004']
    for dataset in datasets:
        train_data = load_data(f'data/{dataset}_train.txt')
        test_data = load_data(f'data/{dataset}_test.txt')
        save_preprocessed_data(train_data, f'data/{dataset}_train_preprocessed.csv')
        save_preprocessed_data(test_data, f'data/{dataset}_test_preprocessed.csv')