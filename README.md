# Walkable-Cities

## Project Overview
This is a comprehensive machine learning application that predicts location walkability scores using geographical coordinates. The system was developed through rigorous analysis of over 80 cities, evenly split between walkable and unwalkable examples, to evaluate urban infrastructure including sidewalks, road design, and public transportation accessibility.

## Research Methodology
The model was developed through extensive research examining over 80 cities worldwide, with balanced representation between walkable and unwalkable urban environments. Each city was evaluated based on critical pedestrian infrastructure:
1. Sidewalk Quality: Coverage, maintenance, and accessibility
2. Road Design: Pedestrian crossings, traffic calming measures, and safety features
3. Public Transportation: Integration, frequency, and proximity to walkable areas
4. Urban Planning: Mixed-use development and pedestrian-friendly zoning

## Validation and Testing
The tool has been validated through real-world applications across diverse urban landscapes, ensuring it provides meaningful walkability insights for urban planners, real estate professionals, and community developers. The comprehensive training dataset ensures reliable predictions across different city types and geographical regions.

## Project Structure

The model training pipeline (training.py) handles the machine learning workflow, implementing a neural network architecture that learns patterns from urban geographical data. It processes the city dataset through a custom DataLoader class that standardizes coordinate inputs and pairs them with corresponding walkability scores. The training process uses mean squared error loss and stochastic gradient descent optimization over multiple epochs, with built-in validation splits to monitor performance and prevent overfitting, ensuring the model generalizes well to new urban environments.

The class creation (class_creation.py) provides the data infrastructure for generating and processing urban geographical information. It implements a City class that interfaces with the Google Maps API to fetch detailed geocoding data, including central coordinates and bounding boxes for each urban area. The script processes the cities.csv dataset to create structured training data, generating random coordinates within city boundaries that can be used to build comprehensive walkability datasets. This modular approach enables scalable data collection and ensures the machine learning model receives properly formatted geographical inputs for accurate walkability analysis.

## Acknowledgments
This project was completed as part of the Nanyang Technology University SCSE Coding Challenge 2024.
