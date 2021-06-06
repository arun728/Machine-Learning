import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# num1 = np.arange(1,21,2)
# num2 = np.arange(2,21,2)
# # print(num1)
# # print(num2)

# # plt.plot(num1, num2)
# # plt.xlabel("Number 1")
# # plt.ylabel('Number 2')
# # plt.show()

# df = pd.DataFrame(num1, num2)
# print(df)

# sns.pairplot(data=df);
# plt.show()

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()