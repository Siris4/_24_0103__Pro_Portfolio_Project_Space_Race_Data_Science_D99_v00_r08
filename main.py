import pandas as pd
import plotly.express as px

# Load the CSV data into a DataFrame
csv_file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0103__Day99_Pro_Portfolio_Project_Space_Race_Data_Science_241014\NewProject\r00_env_START\r08\space_launches.csv'
df = pd.read_csv(csv_file_path)

# Define a mapping of launch pad locations to countries
# This is a simplified example, you'll need to expand this based on your data
launchpad_to_country = {
    "Kennedy Space Center": "USA",
    "Cape Canaveral": "USA",
    "Vandenberg": "USA",
    "Starbase": "USA",
    "Baikonur Cosmodrome": "Kazakhstan",
    "Plesetsk Cosmodrome": "Russia",
    "Xichang Satellite Launch Center": "China",
    "Jiuquan Satellite Launch Center": "China",
    "Tanegashima Space Center": "Japan",
    "Guiana Space Centre": "French Guiana",
    "Māhia Peninsula": "New Zealand"
    # Add other mappings as needed
}

# Extract the country from the 'Launch Pad' column using the mapping
df['Country'] = df['Launch Pad'].apply(lambda x: next((country for pad, country in launchpad_to_country.items() if pad in x), 'Unknown'))

# Group by country and count the number of launches
country_launch_counts = df.groupby('Country')['Mission'].count().reset_index()

# Rename the columns for clarity
country_launch_counts.columns = ['Country', 'Launches']

# Remove 'Unknown' countries if necessary
country_launch_counts = country_launch_counts[country_launch_counts['Country'] != 'Unknown']

# Use Plotly to create the choropleth map
fig = px.choropleth(country_launch_counts,
                    locations="Country",
                    locationmode="country names",
                    color="Launches",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Space Launches by Country")

# Show the map
fig.show()
