import os
from fnmatch import fnmatch
import re
import pandas as pd

def write_to_csv(file_path, date_to_add):
    df = pd.read_csv(file_path, error_bad_lines=False)
    df['Date'] = date_to_add
    df.to_csv(file_path, index=False)


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
    all_numbers = []
    not_added = 0

    
    for root_dir, subdir, files in os.walk(dir_path):
        for file in files:
            file_path = root_dir+'/'+file
            total_CSV_files += 1
            date_list = re.findall(r'\d+', file)  # get all numbers from the CSV
            all_numbers.append(date_list)

            if len(date_list) == 1 or len(date_list) == 2 and len(date_list[0]) > 4:  # This 2 list_Digit size format is handeled(1)['5112015'], (2)['28122016', '2'].
                if len(date_list[0]) == 6:
                    date_in_str = date_list[0]
                    date = '0'+ date_in_str[0]
                    month = '0'+ date_in_str[1]
                    year = date_in_str[2:]
                    in_sequence = year, month, date
                    in_format = '-'.join(in_sequence)
                    length_6.append(in_format)
                    write_to_csv(file_path, in_format)

                if len(date_list[0]) == 7:
                    #print("Original formar:", date_list)
                    date_in_str = date_list[0]
                    date_and_month = date_in_str[:3]
                    Not_converted = "111 212 312 211 311"
                    if date_and_month in Not_converted:
                        not_added += 1 
                        print("This date format couldn't converted:", file)
                    else:
                        check = date_in_str[1:3]
                        if int(check) > 12:
                            date = date_in_str[:2]
                            month = '0'+date_in_str[2]
                            year = date_in_str[3:]
                            in_sequence = year, month, date
                            in_format = '-'.join(in_sequence)
                            write_to_csv(file_path, in_format)
                            #print(in_format)
                            
                        else:
                            chek_2digit = "10 11 12"
                            if check in chek_2digit:
                                date = '0'+date_in_str[0]
                                month = date_in_str[1:3]
                                year = date_in_str[3:]
                                in_sequence = year, month, date
                                in_format = '-'.join(in_sequence)
                                write_to_csv(file_path, in_format)
                                #print(in_format)
                            else:
                                accep_date = "10 20 30"
                                if date_and_month[0:2] in accep_date:
                                    date = date_in_str[0:2]
                                    month = '0'+date_in_str[2]
                                    year = date_in_str[3:]
                                    in_sequence = year, month, date
                                    in_format = '-'.join(in_sequence)
                                    write_to_csv(file_path, in_format)
                                    #print(in_format)
                                else:
                                    date = '0'+date_in_str[0]
                                    month = '0'+date_in_str[2]
                                    year = date_in_str[3:]
                                    in_sequence = year, month, date
                                    in_format = '-'.join(in_sequence)
                                    write_to_csv(file_path, in_format)
                                    #print(in_format)
                    length_7.append(date_in_str)
                
                if len(date_list[0]) == 8:
                    date_in_str = date_list[0]
                    date = date_in_str[:2]
                    month = date_in_str[2:4]
                    year = date_in_str[4:]
                    in_sequence = year, month, date
                    in_format = '-'.join(in_sequence)
                    write_to_csv(file_path, in_format)
                    length_8.append(in_format)
            elif len(date_list) == 2 and len(date_list[0]) == 4 and len(date_list[1]):
                dd_mm = date_list[0]
                date = dd_mm[:2]
                month = dd_mm[2:]
                year = date_list[1]
                in_sequence = year, month, date
                in_format = '-'.join(in_sequence)
                write_to_csv(file_path, in_format)
                ddmm_yyyy.append(in_format)
            elif len(date_list) == 2 and len(date_list[0]) == 2 or len(date_list[0]) == 1 and len(date_list[1]) == 4:
                if 'march' in file:
                    date = date_list[0]
                    if len(date) == 1:
                        date = '0' + date
                        month = '03'
                        year = date_list[1]
                        in_sequence = year, month, date
                        in_format = '-'.join(in_sequence)
                        write_to_csv(file_path, in_format)
                else:
                    print("Check Your month in words is 'march' and in lowercase:", file)

                date_year.append(in_format)
            elif len(date_list) == 3:            
                date = date_list[0]
                month = date_list[1]
                year = date_list[2]
                if len(date) == 1 or int(date) <= 31 and len(month) == 2 and int(month) <= 12 and len(year) == 4:
                    if len(date) == 1:
                        date = '0' + date
                    if len(month) == 1:
                        month = '0' + month
                    in_sequence = year, month, date
                    in_format = '-'.join(in_sequence)
                    write_to_csv(file_path, in_format)
                    well_formated.append(in_format)
            else:
                reming_dates += 1
                print("Remining format files: ", file)

    print("\nTotal Number of 6 digit file DONE:",len(length_6))
    print("Total Number of 7 digit file DONE:",len(length_7))
    print("Total Number of 8 digit file DONE:",len(length_8))
    print("Total Number of well_formated Date file DONE:",len(well_formated))
    print("DDMM_YYYY DONE: ", len(ddmm_yyyy))
    print("Date and year only DONE: ", len(date_year))
    print("6D, 7D, 8D, YY_MM_DD, Month & year Total:", len(length_6)+len(length_7)+len(length_8)+len(well_formated)+len(ddmm_yyyy)+len(date_year))
    print("Numbers of file date couldn't added is:", not_added)
    print("Remining format files: ", reming_dates)
    print('\n\n')
    print("Number of total CSV files: ", total_CSV_files)
    print("lenght of All got numbers from csv:", len(all_numbers))


def check_date_added(dir_path):
    total_files = 0
    added = 0
    not_added = 0
    for root_dir, subdir, files in os.walk(dir_path):
        for file in files:
            total_files += 1
            file_path = root_dir+'/'+file
            df = pd.read_csv(file_path)
            if 'Date' in df.columns:
                added += 1
            else:
                not_added += 1
                print("Date is not added in this file:", file)
    print("\nNumbers of file scaned:", total_files)
    print("Number of date added files:", added)
    print("Number of date is not added in files:", not_added)


directory_path = './data'
append_date_column(directory_path)
check_date_added(directory_path)
