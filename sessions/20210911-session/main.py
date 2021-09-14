import pandas as pd
import matplotlib.pyplot as plt

filename = "../../data/prima-indians-diabetes.csv"
nombres = ["preg", "plas", "pres", "skin",
           "test", "mass", "pedi", "age", "class"]
datos = pd.read_csv(filename, names=nombres)

fig = plt.figure(figsize=(10, 10))
ax = fig.gca()
# datos.hist(ax=ax, color='green')
datos.plot(ax=ax, kind='density', subplots=True, layout=(3, 3))
plt.show()

"""
# Función head()
print(datos.head())

print(datos.shape)

print(datos.dtypes)

pd.set_option('precision', 1)
print(datos.describe())

print(datos.groupby('class').size())

correlacion = datos.corr(method="pearson")
print(correlacion)

print(datos.skew()) """
