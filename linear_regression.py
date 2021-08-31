import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
x_axis = df.columns[0]
y_axis = df.columns[1]

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)
    for i in range(n):
        #x = points.iloc[i].time
        #y = points.iloc[i].score

        x = getattr(points.iloc[i], x_axis)        
        y = getattr(points.iloc[i], y_axis)

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = m_now - b_gradient * L
    return m, b

m = 0
b = 0
L = 0.00001
epoch = 500

for i in range(epoch):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, df, L)

print(f"Linear regression calculated for the relation of {x_axis} and {y_axis}.")
print(m, b)
plt.scatter(getattr(df, x_axis), getattr(df, y_axis), color='black')
plt.plot(list(range(30, 500)), [m * x + b for x in range(30, 500)], color='red')
plt.title(f"Linear Regression of {x_axis} & {y_axis}")
plt.show()