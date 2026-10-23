from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Data preparation
data = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4],
]

# Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Creating the model
model = KMeans(n_clusters=3, random_state=42, n_init=10)

# Training the model 
model.fit(scaled_data)
labels = model.labels_

# Cluster for each customer
for i in range(len(labels)):
    print(f"Customer {i + 1} belongs to Cluster {labels[i]}")

# Customers per cluster
print()
for c in range(3):
    print(f"Cluster {c}: {list(labels).count(c)} customers")

# Visualisation
spending = [row[0] for row in data]
visits = [row[1] for row in data]

plt.scatter(spending, visits, c=labels)
plt.xlabel("Monthly Spending (KES)")
plt.ylabel("Monthly Visits")
plt.title("Customer Segments")
plt.show()