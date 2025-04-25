from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import math

from folder_handler import get_files_within_folder, extract_name

#Colours of for corresponding plots (files i guess):
#file1-red, file2-skyblue, etc...
colours = ['red', 'skyblue', 'orange', 'purple', 'green']

#Generates a bar on ax axis from a given df labeled from the source file with axis y_axis
def generate_bars(ax: plt.Axes, df_arr: list, in_files: list, x_positions: list, width: int, y_axis: str) -> None:
    for i in range(len(df_arr)):
        ax.bar(x_positions+(i-1)*width, df_arr[i][y_axis], width=width, 
                        color=colours[i], edgecolor=colours[i], label=(extract_name(in_files[i])))
        

#Generates a plot on ax axis from a given df labeled from the source file with axis y_axis
def generate_plots(ax: plt.Axes, df_arr: list, in_files: list, x_positions: list, width: int, y_axis: str) -> None:
    for i in range(len(df_arr)):
        ax.plot(x_positions, df_arr[i][y_axis], 
                        color=colours[i], label=(extract_name(in_files[i])))
        # print(extract_name(in_files[i]))
        # print(df_arr[i])
        
#Gets the maximum value of each column from an array of DFs
def get_df_arr_max(df_arr: list) -> int:
    current_max = -1
    for df in df_arr:
        current_max = max(current_max, float(df.max()['time']))
    
    return current_max

#Precise Documentation in AnaliserGuide.ipynb
def analise(in_folder: str, out_filename: str, max_y_scale: str, x_axis: str, x_label: str, y_axis: str, y_label: str, log: bool, plot: bool, msec: bool, save_plt: bool = True) -> None:
    df_arr = []

    in_files = get_files_within_folder(in_folder)

    #Loading files into dataframes
    for file in in_files:
        df = pd.read_csv(file)
        df['time'] = pd.to_numeric(df['time'], errors='coerce')

        df_arr.append(df)


    #Creating the plot
    fig, ax = plt.subplots(figsize=(12, 6))

    #Width of a bar if applicable
    width = 0.15


    #Calculating positions of labels
    x_data = df_arr[0][x_axis]
    x_positions = np.arange(len(x_data))

    #Delogifying if applicable
    if log:
        labels = [str(round(math.e**n)) for n in x_data]
    else:
        labels = [str(n) for n in x_data]

    #Generating a plot(line) or a bar
    if plot:
        generate_plots(ax, df_arr, in_files, x_positions, width, y_axis)
    else:
        generate_bars(ax, df_arr, in_files, x_positions, width, y_axis)


    #Setting up labels and title
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(out_filename, fontsize=14)

    #Applying y axis limit if applicable
    if(max_y_scale != None):
        ax.set_ylim(top=max_y_scale)

    #Applying x axis limit
    ax.set_xlim(left=0-(width*2))


    #Setting up x ticks and labels
    ax.set_xticks(x_positions)
    ax.set_xticklabels(labels, rotation=45)



    #Turning data from sec to msec (or usec)
    if msec:
        arr_max = get_df_arr_max(df_arr) #Using the highest value of the df_arr as the highest y axis label (and tick)
        
        if max_y_scale is not None: #If max_y_scale is defined, using it instead of df_arr max value
            arr_max = max_y_scale
        
        #Making new y label positions
        y_label_pos = np.linspace(0, arr_max, 5) #Creating 5 equadistant points from 0 to arr_max
        y_labels = [round(y * 1000000, 2) for y in y_label_pos]  # convert to ms
        
        ax.set_yticks(y_label_pos) #Setting Ticks to the 5 points generated before
        ax.set_yticklabels(y_labels) #Setting labels to delogified ones


    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.legend()



    plt.tight_layout()
    #Saving the final plot if applicable
    if(save_plt):
        plt.savefig(f'{out_filename}.png')
    else:
        plt.show()


analise('example_datasets/insertion_batch_random_unsorted/', 'AVL vs Treap vs java.util.TreeMap Batch Insertion Unsorted', None, 'n', 'Amount of elements to insert (n)', 'time', 'Time Spent (msec)', False, False, True)