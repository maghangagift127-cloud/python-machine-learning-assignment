from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#data preparation
x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
#data labelling
y = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]
#creating the model
model = LinearRegression()
#training the model
model.fit(x, y)
#prediction
hours = float(input("enter hours studied: "))
prediction = model.predict([[hours]])
print(f"predicted exam score: {prediction[0]:.2f}")
#visualisation using matplotlib
plt.scatter(x, y)
plt.plot(x, model.predict(x))
plt.xlabel("Hours studied")
plt.ylabel("Marks")
plt.show()