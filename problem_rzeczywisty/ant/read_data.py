import pandas as pd


class Reader:
    @staticmethod
    def __edit(file_name: str):
        data = ''
        first_space = True
        with open(file_name, 'r') as file:
            for line in file:
                for char in line:
                    if char != ' ':
                        data += char
                        first_space = True
                    else:
                        if first_space:
                            data += ' '
                            first_space = False
        with open(file_name, 'w') as file:
            file.write(data)

    @staticmethod
    def read_data(file_name):
        Reader.__edit(file_name)
        data = pd.read_csv(file_name, sep=" ")
        try:
            data.drop('Unnamed: 0', axis=1, inplace=True)
        except KeyError:
            pass

        return data
