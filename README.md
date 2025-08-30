# Weather Trends Visualizer 🌡️

A comprehensive Python application for visualizing daily temperature trends using interactive charts. This project demonstrates data analysis and visualization techniques using real weather data, perfect for understanding temperature patterns and climate analysis.

## 📊 Features

- **Dual Chart Display**: Simultaneously displays both line charts and bar charts
- **Interactive Visualization**: Non-blocking chart display allows viewing multiple charts at once
- **Statistical Analysis**: Comprehensive weather data statistics including averages, extremes, and ranges
- **Professional Styling**: High-quality charts with customizable colors and formatting
- **Data Export**: Automatic saving of charts as high-resolution PNG files
- **Error Handling**: Robust file validation and user-friendly error messages
- **CSV Data Support**: Easy integration with standard weather data formats

## 🚀 Project Overview

This weather visualization system takes daily temperature data from a CSV file and creates two types of professional charts:

1. **Line Chart**: Shows temperature trends over time with clear markers and grid lines
2. **Bar Chart**: Displays temperature distribution with color-coding based on temperature ranges:
   - 🔵 Light coral: Cool temperatures (<30°C)
   - 🟠 Orange: Moderate temperatures (30-35°C)  
   - 🔴 Red: Hot temperatures (>35°C)

## 📁 Project Structure

```
weather_visualization/
│
├── weather_visualizer.py       # Main application file
├── weather_data.csv            # Sample temperature dataset
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
│
└── Generated Output Files/
    ├── temperature_line_chart.png
    └── temperature_bar_chart.png
```

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Clone or Download the Project
```bash
# Download all project files to your local directory
# Ensure you have:
# - weather_visualizer.py
# - weather_data.csv  
# - requirements.txt
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install pandas matplotlib
```

### Step 3: Verify Installation
```bash
python -c "import pandas, matplotlib; print('All libraries installed successfully!')"
```

## 🖥️ How to Run the Project

### Method 1: Using Default Dataset
1. **Navigate to project directory:**
   ```bash
   cd weather_visualization
   ```

2. **Run the application:**
   ```bash
   python weather_visualizer.py
   ```

3. **When prompted for file path, press Enter to use default:**
   ```
   📁 Enter the path to your weather CSV file (or press Enter for 'weather_data.csv'): 
   [Press Enter]
   ```

### Method 2: Using Custom Dataset
1. **Run the application:**
   ```bash
   python weather_visualizer.py
   ```

2. **Provide your CSV file path:**
   ```
   📁 Enter the path to your weather CSV file (or press Enter for 'weather_data.csv'): your_data.csv
   ```

## 📊 Expected Output

### Console Output
```
🌤️  Weather Trends Visualizer - SIMULTANEOUS DISPLAY
=======================================================

✓ Successfully loaded 31 records from weather_data.csv

📋 Data Preview (first 5 rows):
         Date  Temperature
0  2025-07-01         29.5
1  2025-07-02         28.6
2  2025-07-03         31.9
3  2025-07-04         35.4
4  2025-07-05         30.9

==================================================
📊 WEATHER DATA STATISTICS
==================================================
📅 Date Range: 2025-07-01 to 2025-07-31
🌡️  Average Temperature: 27.0°C
🔥 Highest Temperature: 37.4°C
❄️  Lowest Temperature: 20.0°C
📏 Temperature Range: 17.4°C
📈 Standard Deviation: 4.8°C

🔥 Hottest Day: 2025-07-07 (37.4°C)
❄️  Coolest Day: 2025-07-24 (20.0°C)

🎨 Creating visualizations...

📈 Generating line chart...
✓ Line chart saved as 'temperature_line_chart.png'
📊 Generating bar chart...
✓ Bar chart saved as 'temperature_bar_chart.png'

=======================================================
✅ BOTH CHARTS DISPLAYED SIMULTANEOUSLY!
=======================================================
📁 Charts saved as:
   • temperature_line_chart.png
   • temperature_bar_chart.png

🎉 Weather analysis completed successfully!

💡 TIP: Both charts are now open! You can view them side by side.
📝 Close the chart windows when you're done viewing them.

⏸️  Press Enter to exit and close all charts...
```

### Visual Output
- **Two chart windows will open simultaneously**
- **Line Chart**: Red line with circular markers showing temperature trends
- **Bar Chart**: Color-coded bars representing daily temperatures
- **Both charts saved as PNG files** in the project directory

## 📈 Sample Data Format

Your CSV file should follow this format:

```csv
Date,Temperature
2025-07-01,29.5
2025-07-02,28.6
2025-07-03,31.9
2025-07-04,35.4
...
```

**Requirements:**
- `Date` column: YYYY-MM-DD format
- `Temperature` column: Numeric values (Celsius)
- No missing values in required columns

## 🎯 Key Features Explained

### 1. Simultaneous Chart Display
Unlike traditional plotting systems, this application uses `plt.show(block=False)` to display both charts at the same time without waiting for one to close.

### 2. Temperature Categorization
The bar chart automatically color-codes temperatures:
- **Light Coral**: Cool days (<30°C)
- **Orange**: Moderate days (30-35°C)
- **Red**: Hot days (>35°C)

### 3. Statistical Analysis
Provides comprehensive statistics including:
- Central tendency (mean, median)
- Variability (standard deviation, range)
- Extreme values (hottest/coolest days)

## 🔧 Customization Options

### Modify Chart Colors
Edit the `create_bar_chart()` function:
```python
colors = ['your_cool_color' if temp < 30 else 'your_moderate_color' if temp < 35 else 'your_hot_color' 
          for temp in df['Temperature']]
```

### Change Chart Size
Modify the `figsize` parameter:
```python
plt.figure(figsize=(width, height))  # Default: (12, 6) for line, (15, 6) for bar
```

### Add More Statistics
Extend the `display_statistics()` function with additional metrics.

## 🐛 Troubleshooting

### Common Issues and Solutions

**1. ImportError: No module named 'pandas'**
```bash
pip install pandas matplotlib
```

**2. FileNotFoundError: weather_data.csv**
- Ensure the CSV file is in the same directory as the Python script
- Check the file name spelling and extension

**3. Charts not displaying**
- Install tkinter: `pip install tk`
- Try running with Python instead of python3

**4. Permission denied when saving files**
- Run from a directory where you have write permissions
- Check if files are already open in another application

**5. Encoding issues with CSV**
- Ensure your CSV file is saved with UTF-8 encoding
- Check for special characters in date/temperature values

### System Requirements
- **Windows**: Python 3.7+, Works with Command Prompt/PowerShell
- **macOS**: Python 3.7+, Works with Terminal
- **Linux**: Python 3.7+, May require additional GUI libraries

## 📚 Learning Outcomes

This project demonstrates:
- **Data Loading**: Using pandas to read CSV files
- **Data Validation**: Error handling and data type checking
- **Statistical Analysis**: Calculating descriptive statistics
- **Data Visualization**: Creating professional charts with matplotlib
- **User Interface**: Interactive command-line applications
- **File I/O**: Saving charts and handling file paths

## 🤝 Contributing

To extend this project:
1. Add more chart types (scatter plots, histograms)
2. Implement data filtering options
3. Add support for multiple weather parameters
4. Create interactive web dashboards
5. Integrate real-time weather APIs

## 📄 License

This project is created for educational purposes as part of an internship program. Feel free to use and modify for learning and development.

## 👨‍💻 Author

**Internship Project**  
*Data Visualization and Analysis*  
*August 2025*

---

**🌟 Happy Weather Analysis! 🌡️📊**
