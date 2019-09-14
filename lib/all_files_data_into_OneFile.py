import os
import pandas as pd


def write_to_csv(dir_path, file_content):
	file_name = 'all_csv_data_in_One.csv'
	create_file = dir_path+'/'+file_name

	if not os.path.exists(create_file):
		names_for_column = ['Commodity', ' Weight in Kg', ' Price in Rs', 'Date']
		add_column = pd.DataFrame(columns=names_for_column)
		add_column.to_csv(create_file, index=None)
	
	with open(create_file, 'a') as f:
		file_content.to_csv(f, index=None, header=False)


def read_csv(file_path):
	file_DataFrame = pd.read_csv(file_path, index_col=None)
	if 'Date' in file_DataFrame.columns:
		write_to_csv(dir_path, file_DataFrame)


def find_csvs(dir_path):
	for root_dir, subdir, files in os.walk(dir_path):
			for file in files:
				file_path = root_dir+'/'+file
				read_csv(file_path)


dir_path = "../data" 
find_csvs(dir_path)
