import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data_C02_emission.csv')

#pretvoriti object u category
object_podaci = data.select_dtypes(include =['object']).columns
for values in object_podaci:
    data[values] = data[values].astype('category')

# a) Histogram - emission c02 plinova

plt.figure()
data['CO2 Emissions (g/km)'].plot(kind='hist',bins = 20)
plt.show()

#Komentirajte
# Na x osi histograma se nalazi vrijednost C02 emisije dok se na y osi nalazi broj/kolicina podataka
# koja odgovara tom broju C02 emisije, npr za C02 emission = 600 vidimo da ima jako mal broj podataka koje odgovaraju
# tome podatku i zato je dosta nisko, dok od 200-300 imamo najveći broj ili frekvenciju 

# b) CO2 Emissions (g/km) , Fuel Consumption City (L/100km)

data.plot.scatter(x = 'CO2 Emissions (g/km)', y = 'Fuel Consumption City (L/100km)', c='Fuel Type', cmap = "cool", s=50)
plt.show()

#Komentirajte
# Po grafu rasprsenja je vidljivo da se podaci krecu linearno tj. sto je veci Fuel consumption to je veci Emission
# Vidimo da obicni benzin tip goriva ima nizak co2 emission i consumption dok Z tip goriva ima veci ujedno E tip goriva
# ima znatno veci fuel consumption od ostalih za isti CO2 emission

# c) Razdioba izvangradske potrosnje s obzirom na tip goriva, Fuel Consumption Hwy (L/100km) , Fuel Type

data.boxplot(column = 'Fuel Consumption Hwy (L/100km)', by='Fuel Type')
plt.show()

#Komentirajte

#Na grafovima su vidljive sve vrijednosti Tipa Fuela i fuel consumptiona, za svaki podatak je viljdiva
#minimalna vrijednost, 25%,50% 75% i maximalna vrijednost grupe podataka, za D tip goriva se moze uociti
# da ima podatke koji su malo ispod i malo iznad minimalne vrijednosti i maksimalne vrijednosti grupe sto moze
# ukazivati gresku kod prikupljanja podataka
# na Z tipu goriva su vidljiva velika odstupanja gdje su podaci puno udaljeni od max vrijednosti te ih ima jako puno sto
# ukazuje na gresku

# d) broj vozila po tipu goriva, groupby i stupcasti dijagram
# e) potrebno zajedno prikazati sa d) zadatkom

new_data = data.groupby(['Fuel Type'])['Make'].count()
new_data2 = data.groupby(['Cylinders'])['CO2 Emissions (g/km)'].mean()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

new_data.plot(kind='bar', ax=ax1)
ax1.set_title('Broj vozila po tipu goriva')
ax1.set_xlabel('Tip goriva')
ax1.set_ylabel('Broj vozila')

new_data2.plot(kind='bar', ax=ax2)
ax2.set_title('Prosjecna C02 emisija s obzirom na broj cilindara')
ax2.set_xlabel('Broj cilindara')
ax2.set_ylabel('Prosjecna CO2 emisija')

plt.show()




