import matplotlib.pyplot as plt

year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
temperature = [25.3, 27.1,24.8, 26.5, 22.9, 23.7, 25.2, 26.8, 24.5, 29.9, 26.1, 28.3]

plt.hist(year, bins = len(temperature), color = 'red', alpha = 1)
plt.xlabel("Years")
plt.ylabel("Temperature")
plt.title("Statistic")
plt.show()
