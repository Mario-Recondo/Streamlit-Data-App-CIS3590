# Water Quality Dashboard 

## Description
Streamlit Data App that visualizes water quality data from Biscayne Bay and provides insights through descriptive statistics. Additionally includes NASA's Astronomy Picture of the Day. 

## Key Features 
The dashboard is organized into four tabs:
- Descriptive Statistics: Displays a clean tabular view of telemetry data from Biscayne Bay.
- 2D Data Analysis: A time-series visualization tracking changes in water temperature. 
- 3D Geospatial Mapping: A 3D scatter plot that maps Total Water Column across coordinates, color-coded by temperature. 
- NASA APOD Integration: Utilizes the NASA API to fetch and display the "Astronomy Picture of the Day" with a toggleable info panel for photograph context. 
- Displays Nasa Astronomy Picture of the day photo with optional checkbox to display photo information

**Tech Stack:**
- Language: Python
- Library: Streamlit
- Data Handling: Pandas
- Visualization: Plotly.Express
- API: Nasa APOD API

**Required:**
In order to display NASA APOD, follow these steps to receive an API Key:
- Go to this link: [NASA Open API](https://api.nasa.gov/)
- Fill out the "Generate API Key" section on the page (check email for the API key)
- Under the Browse API tab search "APOD" and click the link
- Follow the instructions on the page
- Add API Key to your .env file within your project 
