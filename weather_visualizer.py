"""
Weather Trends Visualizer - SOLUTION 1: Non-Blocking Display
============================================================
Both charts will appear simultaneously without waiting for you to close one.

Author: Generated for internship project
Date: August 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def load_weather_data(file_path):
    """
    Load weather data from CSV file
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        print(f"✓ Successfully loaded {len(df)} records from {file_path}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found!")
        return None
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None

def create_line_chart(df, save_path=None):
    """
    Create a line chart showing temperature variation over time
    """
    # Create figure with specific size and position
    plt.figure(figsize=(12, 6))
    
    # Plot the line chart
    plt.plot(df['Date'], df['Temperature'], 
             color='red', linewidth=2, marker='o', 
             markersize=4, label='Daily Temperature')
    
    # Customize the chart
    plt.title('Daily Temperature Trends', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Add grid for better readability
    plt.grid(True, alpha=0.3)
    
    # Add legend
    plt.legend()
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the chart if path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✓ Line chart saved as '{save_path}'")
    
    # Display the chart NON-BLOCKING
    plt.show(block=False)  # This is the key change!
    
    return plt.gcf()  # Return figure reference

def create_bar_chart(df, save_path=None):
    """
    Create a bar chart showing temperature variation over time
    """
    # Create figure with specific size
    plt.figure(figsize=(15, 6))
    
    # Create bar chart
    colors = ['lightcoral' if temp < 30 else 'orange' if temp < 35 else 'red' 
              for temp in df['Temperature']]
    
    bars = plt.bar(df['Date'], df['Temperature'], 
                   color=colors, alpha=0.7, edgecolor='black', linewidth=0.5)
    
    # Customize the chart
    plt.title('Daily Temperature - Bar Chart', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Add grid for better readability
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars (every 3rd bar to avoid clutter)
    for i, bar in enumerate(bars):
        if i % 3 == 0:  # Show every 3rd value to avoid overcrowding
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                    f'{height}°C', ha='center', va='bottom', fontsize=8)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the chart if path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✓ Bar chart saved as '{save_path}'")
    
    # Display the chart NON-BLOCKING
    plt.show(block=False)  # This is the key change!
    
    return plt.gcf()  # Return figure reference

def display_statistics(df):
    """
    Display basic statistics about the weather data
    """
    print("\n" + "="*50)
    print("📊 WEATHER DATA STATISTICS")
    print("="*50)
    print(f"📅 Date Range: {df['Date'].iloc[0]} to {df['Date'].iloc[-1]}")
    print(f"🌡️  Average Temperature: {df['Temperature'].mean():.1f}°C")
    print(f"🔥 Highest Temperature: {df['Temperature'].max():.1f}°C")
    print(f"❄️  Lowest Temperature: {df['Temperature'].min():.1f}°C")
    print(f"📏 Temperature Range: {df['Temperature'].max() - df['Temperature'].min():.1f}°C")
    print(f"📈 Standard Deviation: {df['Temperature'].std():.1f}°C")
    
    # Find extreme days
    max_temp_day = df.loc[df['Temperature'].idxmax()]
    min_temp_day = df.loc[df['Temperature'].idxmin()]
    
    print(f"\n🔥 Hottest Day: {max_temp_day['Date']} ({max_temp_day['Temperature']}°C)")
    print(f"❄️  Coolest Day: {min_temp_day['Date']} ({min_temp_day['Temperature']}°C)")

def main():
    """
    Main function to run the weather visualization program
    """
    print("🌤️  Weather Trends Visualizer - SIMULTANEOUS DISPLAY")
    print("="*55)
    
    # Get file path from user
    while True:
        file_path = input("\n📁 Enter the path to your weather CSV file (or press Enter for 'weather_data.csv'): ").strip()
        
        # Use default file if no input
        if not file_path:
            file_path = "weather_data.csv"
        
        # Check if file exists
        if os.path.exists(file_path):
            break
        else:
            print(f"❌ File '{file_path}' not found. Please enter a valid file path.")
    
    # Load the data
    df = load_weather_data(file_path)
    if df is None:
        return
    
    # Display data preview
    print("\n📋 Data Preview (first 5 rows):")
    print(df.head())
    
    # Display statistics
    display_statistics(df)
    
    # Create visualizations
    print("\n🎨 Creating visualizations...")
    
    # Create both charts simultaneously
    print("\n📈 Generating line chart...")
    line_fig = create_line_chart(df, "temperature_line_chart.png")
    
    print("📊 Generating bar chart...")
    bar_fig = create_bar_chart(df, "temperature_bar_chart.png")
    
    # Optional: Show additional analysis
    print("\n" + "="*55)
    print("✅ BOTH CHARTS DISPLAYED SIMULTANEOUSLY!")
    print("="*55)
    print("📁 Charts saved as:")
    print("   • temperature_line_chart.png")
    print("   • temperature_bar_chart.png")
    print("\n🎉 Weather analysis completed successfully!")
    print("\n💡 TIP: Both charts are now open! You can view them side by side.")
    print("📝 Close the chart windows when you're done viewing them.")
    
    # Keep the program running until user decides to exit
    input("\n⏸️  Press Enter to exit and close all charts...")

if __name__ == "__main__":
    main()
    