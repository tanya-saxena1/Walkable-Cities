import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class training_model(nn.Module):
    def __init__(self, input):
        super(training_model, self,).__init__()
        self.fc = nn.Linear(input, 1)

    def forward(self, x):
        return self.fc(x)
    
class new_data_stuff(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.X = self.data[['latitude', 'longitude']].values
        self.y = self.data['score'].values.reshape(-1, 1)
        self.scaler = StandardScaler()
        self.X = self.scalar.fit_transform(self.X)

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return torch.FloatTensor(self.X[index]), torch.FloatTensor(self.y[index])
    
#hyperparams
learning_rate = 0.01
num_epochs = 100
batch_size = 50

dataset = new_data_stuff('cities.csv')
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])

train_load = DataLoader(dataset = train_dataset, batch_size = batch_size, shuffle = True)
test_load = DataLoader(dataset = test_dataset, batch_size = batch_size, shuffle = False)

model = training_model(input_size = 2)
criteria = nn.MSELoss()
optimiser = optim.SGD(model.parameter(), lr = learning_rate)

for epoch in range(num_epochs):
    for inputs, targets in train_load:
        optimiser.zero_grad()
        output = model(input)
        loss = criteria(output, input)
        loss.backward()
        optimiser.step()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

model.eval()
with torch.no_grad():
    total_loss = 0
    for input, target in test_load:
        output = model(input)
        total_loss += criteria(output, targets).item()

average_loss = total_loss / len(test_load)
print("Test Loss:", average_loss)

