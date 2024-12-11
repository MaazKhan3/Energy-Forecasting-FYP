# Wind and Solar Energy Forecasting System

![Renewable Energy](https://via.placeholder.com/1000x300?text=Renewable+Energy+Forecasting+System)  
_A comprehensive system for renewable energy forecasting and analysis._

## Overview
This project focuses on developing an intelligent energy forecasting system to harness wind and solar energy effectively. The system predicts energy generation using historic and real-time data, advanced machine learning models, and energy-specific parameters. The ultimate goal is to facilitate efficient renewable energy planning and provide actionable insights to users and stakeholders.

## Key Features
- **Wind Energy Forecasting:** Predict future wind speeds using LSTM models and estimate energy output for various turbine models.
- **Solar Energy Forecasting:** (Upcoming) Predict energy generation based on solar irradiance, weather data, and panel specifications.
- **Recommender System:** (Upcoming) Suggest optimal renewable energy solutions based on user budget and available installation area.
- **Smart Grid Mapping:** Visualize energy predictions and comparisons on an interactive dashboard.

## Methodology

### 1. Wind Energy Forecasting
- Extracted features:
  - Wind speed, wind height, wind direction, air density, turbulence intensity, and shear coefficient.
- Turbine-specific features:
  - Rated power, cut-in speed, cut-out speed, rated speed, rotor diameter, and power curves.
- Data Collection:
  - Integrated with the NASA API for historic wind speed data.
  - Extracted turbine specifications from [en.wind-turbine-models.com](https://en.wind-turbine-models.com/).
     ![image](https://github.com/user-attachments/assets/43df3798-7463-412b-aaca-d4c8debd0066)
- Model Training:
  - Developed a time series forecasting model using LSTM to predict future wind speeds.
    ![image](https://github.com/user-attachments/assets/8bf279e7-2877-410d-b3ad-1aac73077da8)

- Energy Prediction:
  - Used turbine-specific power curves to validate calculated energy outputs.
    ![image](https://github.com/user-attachments/assets/6320167f-0ccc-4237-93ae-1a7c96a66718)


### 2. Solar Energy Forecasting (Upcoming in FYP-II)
- Develop a similar system for predicting solar energy using solar irradiance and weather conditions.
- Analyze region-specific energy generation potential for solar panels.

### 3. Recommender System (Upcoming in FYP-II)
- Provide recommendations for renewable energy systems based on user-defined constraints such as budget and area.

### 4. Smart Grid Integration (Upcoming in FYP-II)
- Map findings on a smart grid dashboard to provide actionable insights into energy generation and consumption patterns.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/energy-forecasting-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd energy-forecasting-system
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your NASA API key in the configuration file (e.g., `config.json`).

## Usage

### Running the Wind Energy Forecasting System
1. Prepare the historic wind speed dataset using the NASA API:
   ```bash
   python fetch_wind_data.py --location <location_coordinates>
   ```
2. Train the LSTM model:
   ```bash
   python train_lstm.py
   ```
3. Predict wind speeds and calculate energy output:
   ```bash
   python energy_forecast.py --location <location_coordinates>
   ```

### Future Modules
- Solar Energy Forecasting and Smart Grid visualization will be integrated in FYP-II.

## Results
- **Wind Energy Forecasting:** Achieved high accuracy in predicting wind speeds with an MAE of less than 0.5 m/s.
- **Energy Calculation Validation:** Deviation from turbine power curves remained under 5%.
- **Scalability:** Demonstrated robust performance across diverse geographic regions.

## Roadmap
1. Develop solar energy forecasting module.
2. Implement a recommender system for renewable energy solutions.
3. Create an interactive smart grid visualization.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- NASA for providing historic wind speed data via their API.
- [en.wind-turbine-models.com](https://en.wind-turbine-models.com/) for detailed turbine specifications.
- Open-source libraries and tools used in this project.

---

_"Harnessing the power of wind and sun to build a sustainable future."_
