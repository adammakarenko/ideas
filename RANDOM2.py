import pandas as pd
import random
import os

def load_data_and_generate_idea(raw_materials_file, colors_file, themes_file):
    # Load the data
    raw_materials_df = pd.read_csv(raw_materials_file)
    colors_df = pd.read_csv(colors_file)
    themes_df = pd.read_csv(themes_file)
    
    # Select random items
    raw_material = random.choice(raw_materials_df['Raw Materials'])
    color = random.choice(colors_df['Color Names'])
    theme = random.choice(themes_df['Thematic Ideas'])
    
    return raw_material, color, theme

# Set the current working directory to the directory of this script
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

# File names
raw_materials_file = 'raw_materials_for_art.csv'
colors_file = 'matplotlib_colors.csv'
themes_file = 'themes_for_books_movies_life.csv'

# Generate the random art idea
raw_material, color, theme = load_data_and_generate_idea(raw_materials_file, colors_file, themes_file)

# Print the idea to the console
print(f"Create something using:\nMaterial: {raw_material}\nColor: {color}\nTheme: {theme}")
