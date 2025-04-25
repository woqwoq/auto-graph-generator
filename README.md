# Automated Graph Plotter

This project provides a way to automate generation of graphs such as benchmarking performance data (insertion times) for different tree structures, like AVL trees, Treaps, and Java's `TreeMap`, based on benchmark datasets. The data is represented in CSV files, which are read, processed, and plotted using Python and libraries like Pandas and Matplotlib.

## Project Overview

The `Analiser.py` script is designed to automate and plotting graphs. The script reads CSV files from a specified folder(s), processes the data, and generates either bar charts or line plots.

### Features:
- Reads multiple CSV files containing benchmarking data.
- Generates either bar plots or line plots depending on user's needs.
- Supports logarithmic transformations for the x-axis.
- Converts time data into milliseconds (or microseconds) for finer granularity.
- Automatically adjusts axis limits and formats.
- Saves the generated plot as a PNG image.

## Why?

This script was written during my COMP20280/COMP20290 project assignment, where we had to analyse different algorithms/data structures based on the given research paper. 
The script greatly decreased the time it took us to visualise the data as it needs just a single function call to generate graph for a folder of CSV's. Because of that, remaking a graph was as simple as `python3 Analiser.py`.

## Functionality

The core function of this project is `analise()`. This function processes the benchmarking data, generates a plot, and saves or displays the output.

## Constraints
The script takes a string name/path of the folder, where `.csv` files are located. Each file will be treated as a unique bar/line on the final graph. Because of that, each `.csv` file *SHOULD* have exactly same columns.  
The script can support up to 5 bar entries/lines at one graph. This number can be greatly improved by optimising `width` parameter and adding more entries in `colours`.

## Example Input, Usage and Sample Output
Running the following command
```python
analise(
  'example_datasets/insertion_batch_random_unsorted/', 
  'AVL vs Treap vs java.util.TreeMap Batch Insertion Unsorted',
  None,
  'n',
  'Amount of elements to insert (n)',
  'time',
  'Time Spent (msec)',
  False,
  False,
  True)
```
With input files of style
```
n,time
100,3.3727052E-6
115,3.0904815E-6
132,3.6590287E-6
152,3.5965163E-6
```
Will result in this graph
![Insertion Time Plot](AVL%20vs%20Treap%20vs%20java.util.TreeMap%20Batch%20Insertion%20Unsorted.png)


### `analise()` function

```python
def analise(in_folder: str, out_filename: str, max_y_scale: str, x_axis: str, x_label: str, y_axis: str, y_label: str, log: bool, plot: bool, msec: bool, save_plt: bool = True) -> None:
```
### Parameters
* in_folder: Path to the folder containing the CSV files.

* out_filename: The name of the output image file (without extension).

* max_y_scale: Optional maximum value for the y-axis scale.

* x_axis: Column name for the x-axis (e.g., 'n' for number of elements).

* x_label: Label for the x-axis.

* y_axis: Column name for the y-axis (e.g., 'time' for time spent).

* y_label: Label for the y-axis.

* log: Boolean flag to apply logarithmic scale to the x-axis.

* plot: Boolean flag to generate a line plot (True) or bar plot (False).

* msec: Boolean flag to convert time to milliseconds.

* save_plt: Boolean flag to save the plot as a PNG image (default is True).
