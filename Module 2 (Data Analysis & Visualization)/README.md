# Module 2: Data Analysis & Visualization

## 📌 Course: Applied AI and Research Paper Publication: Python to Model Development

---

## 🧰 Libraries Used
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing and array operations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical data visualization

---

## 📂 Topics Covered

### 🔹 Topic 01 — Pandas
- Pandas data structures: Series and DataFrame
- Loading datasets (`read_csv`)
- Exploring data: `head()`, `tail()`, `describe()`, `info()`
- Selecting columns, `loc[]` indexing
- Splitting data into X (independent) and y (dependent)
- Handling null values: `isnull()`, `dropna()`, `fillna()`
- Forward fill (`ffill`) and Backward fill (`bfill`)
- Detecting outliers using IQR method

### 🔹 Topic 02 — Null Value Handling
- Loading and inspecting null datasets
- Column-wise null value count
- Filling nulls with mean (numeric columns)
- Filling nulls with mode (categorical columns)
- Safe handling using `.copy()` to preserve original data

### 🔹 Topic 03 — NumPy
- 1D, 2D, 3D array creation
- Array properties: `ndim`, `shape`, `size`, `dtype`
- Built-in arrays: `zeros`, `ones`, `full`, `eye`, `empty`, `arange`, `linspace`
- Random arrays: `rand`, `randint`, `randn`
- Indexing and slicing
- Flattening, stacking (`vstack`, `hstack`), transpose
- Reshape, square, square root
- Element-wise operations: sum, subtract, multiply, divide
- Dot product, mean, median, std, min, max
- Array comparison and accuracy check
- Broadcasting
- Null value handling: `np.isnan()`, `np.nan_to_num()`
- Saving and loading arrays: `np.save()`, `np.load()`

### 🔹 Topic 04 — Matplotlib
- Line plot with color, linestyle, marker, alpha
- Shorthand format (`'r--s'`)
- Multiple line plots with legend
- Bar chart (single, grouped, stacked, horizontal)
- Adding value labels on bars using `plt.text()`
- Histogram with bins, edgecolor, alpha
- Pie chart with explode, autopct, label/pct distance
- Scatter plot with color, size, alpha

### 🔹 Topic 05 — Seaborn
- Color palettes
- Built-in datasets: `tips`, `dowjones`
- Scatter plot with `hue`, `size`, `style`
- `relplot` with `col`, `col_wrap`
- Line plot and distribution plot (`displot`, `histplot`)
- Categorical plots: `countplot`, `stripplot`, `boxplot`, `violinplot`, `barplot`
- Pairplot with hue
- Heatmap with annotations, color map, correlation matrix
- Linear regression plot (`regplot`)

---

## 🛠️ Environment
- **Google Colab** — All notebooks were created and executed in Google Colab
- **Dataset** — Iris dataset, Null Iris dataset, Tips dataset, Dowjones dataset

---

## 📁 Folder Structure
```
Module-2-Data-Analysis/
├── 01_pandas_basics.ipynb
├── 02_null_value_handling.ipynb
├── 03_numpy.ipynb
├── 04_matplotlib.ipynb
├── 05_seaborn.ipynb
└── README.md
```