import os
from fnmatch import fnmatch
import pandas as pd


def date(file_name):
    file_name = file_name[:-4]
    if 'oddanchatram' in file_name:
        get_date = file_name.split('-')[-3:]
        date = get_date[0]
        month = get_date[1]
        year = get_date[2]
        get_date = year, month, date
        date_join = ('_'.join(get_date))
        return date_join

    if 'dindigul' in file_name:
        get_date = file_name.split('-')[-1:]
        string_date = get_date[0]
        date_chr, month = (0, 0)
        date = str(date_chr) + string_date[0]
        month = str(month) + string_date[1]
        year = string_date[2:]
        date_tuple = year, month, date
        join_date = '_'.join(date_tuple)
        return join_date


def readfile(full_file_path, file_name):
    df = pd.read_csv(full_file_path, error_bad_lines=False)
    date_format = date(file_name)
    df['Date'] = date_format
    df.to_csv(full_file_path, index=False)


def append_date_column(dir_path):
    pattern = "*.csv"
    for root_dir, subdir, files in os.walk(dir_path):
        for file in files:
            if fnmatch(file, pattern):
                os.path.join(root_dir, file)
                full_file_path = os.path.join(root_dir, file)
                readfile(full_file_path, file)
