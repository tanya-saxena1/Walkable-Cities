from flask import Flask, request, render_template
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

class training_model(nn.Module):
    def __init__(self, input_size):
        super(training_model, self).__init__()
        self.fc = nn.Linear(input_size, 1)

    def forward(self, x):
        return self.fc(x)

#the data class and other stuff
model = training_model(input_size=2)
model.load_state_dict(torch.load('model_weights.pth')) #add the path of the pre-trained stuff
model.eval()

scaler = StandardScaler()

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])

def predict():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    input_data = torch.FloatTensor(scaler.transform([[latitude, longitude]]))

    with torch.no_grad():
        output = model(input_data)

    return {'prediction': output.item()} #json file idk what to do with this

if __name__ == '__main__':
    app.run(debug=True)

