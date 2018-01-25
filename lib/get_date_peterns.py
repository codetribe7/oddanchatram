import os
from fnmatch import fnmatch
import re
#import pandas as pd


def append_date_column(dir_path):
    pattern = "*.csv"
    total_CSV_files = 0
    reming_dates = 0

    length_6 = []
    length_7 = []
    length_8 = []
    well_formated = []
    ddmm_yyyy = []
    date_year = []
    all_ext_digits = []

    for root_dir, subdir, files in os.walk(dir_path):
        for file in files:
            total_CSV_files += 1
            date_list = re.findall(r'\d+', file)  # Extrect all digits from the string.
            all_ext_digits.append(date_list)

            if len(date_list) == 1 or len(date_list) == 2 and len(date_list[0]) > 4:  # This 2 list_Digit size format is handeled(1)['5112015'], (2)['28122016', '2'].
                if len(date_list[0]) == 6:
                    #print("Original date format:", date_list)
                    date_in_str = date_list[0]
                    date = '0'+ date_in_str[0]
                    month = '0'+ date_in_str[1]
                    year = date_in_str[2:]
                    in_sequence = year, month, date
                    in_format = '-'.join(in_sequence)
                    #print("Converted date format:", in_format)
                    length_6.append(in_format)
                if len(date_list[0]) == 7:
                    #print("Original date format:", date_list)
                    date_in_str = date_list[0]
                    length_7.append(date_in_str)
                if len(date_list[0]) == 8:
                    #print("Original date format:", date_list)
                    date_in_str = date_list[0]
                    date = date_in_str[:2]
                    month = date_in_str[2:4]
                    year = date_in_str[4:]
                    in_sequence = year, month, date
                    in_format = '-'.join(in_sequence)
                    #print("Converted date format:", in_format)
                    length_8.append(in_format)
            elif len(date_list) == 2 and len(date_list[0]) == 4 and len(date_list[1]):
                #print("Original date format:", date_list)
                dd_mm = date_list[0]
                date = dd_mm[:2]
                month = dd_mm[2:]
                year = date_list[1]
                in_sequence = year, month, date
                in_format = '-'.join(in_sequence)
                #print("Converted date format:", in_format)
                ddmm_yyyy.append(in_format)
            elif len(date_list) == 2 and len(date_list[0]) == 2 or len(date_list[0]) == 1 and len(date_list[1]) == 4:
                #print("Original date format:", date_list)
                if 'march' in file:
                    date = date_list[0]
                    if len(date) == 1:
                            date = '0' + date
                    month = '03'
                    year = date_list[1]
                    in_sequence = year, month, date
                    in_format = '-'.join(in_sequence)
                    #print("Converted date format:", in_format)
                    date_year.append(in_format)
                else:
                    print("Check Your month in words is 'march' and in lowercase:", file)

            elif len(date_list) == 3:            
                #print("Original date format:", date_list)
                date = date_list[0]
                month = date_list[1]
                year = date_list[2]
                if len(date) == 1 or int(date) <= 31 and len(month) == 2 and int(month) <= 12 and len(year) == 4:
                    if len(date) == 1:
                        date = '0' + date
                    if len(month) == 1:
                        month = '0' + month
                    yy_mm_dd = year, month, date
                    join_format = '-'.join(yy_mm_dd)
                    #print("Converted date format:", in_format)
                    well_formated.append(join_format)
            else:
                reming_dates += 1
                print("Remining format files: ", file)


    print('\n')
    print("Number of total CSV files: ", total_CSV_files)
    print("Numbers of All extrexted digits from CSV:", len(all_ext_digits))
    print("\nTotal Number of 6 digit file DONE:",len(length_6))
    print("Total Number of 7 digit file:",len(length_7))
    print("Total Number of 8 digit file DONE:",len(length_8))
    print("Total Number of well_formated Date file DONE:",len(well_formated))
    print("DDMM_YYYY DONE: ", len(ddmm_yyyy))
    print("Date, Year and month in characters only DONE: ", len(date_year))
    print("6D, 7D, 8D, YY_MM_DD, Month & year Total:", len(length_6)+len(length_7)+len(length_8)+len(well_formated)+len(ddmm_yyyy)+len(date_year))
    print("Remining file: ", reming_dates)


append_date_column('/home/rajan/oddanchatram/2data')  # Enter directory path
