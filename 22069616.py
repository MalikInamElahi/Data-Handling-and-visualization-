import pandas as pd
import matplotlib.pyplot as plt


terror_df = pd.read_csv('terrorist-attacks.csv')
gdp_df = pd.read_csv('gdp.csv')
roll_number = '"22069616"'
name = '"Malik InamElahi"'
countries = ['Afghanistan', 'India', 'Pakistan', 'United States', 'Ukraine', 'Japan']

plt.figure(figsize=(17, 10))
# First subplot
plt.subplot(2, 2, 1)
for country in countries:
    country_data = terror_df[terror_df['Entity'] == country]
    country_data_filtered = country_data[country_data['Year'] >= 2000]
    plt.bar(country_data_filtered['Year'], country_data_filtered['Terrorist attacks'], label=f"{country} - Attacks")

plt.title('Number Of Terrorist Attacks', color='red')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.legend()
plt.grid(True)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Second subplot
plt.subplot(2, 2, 2)
attack_methods = [
    'Attack method: Hijacking',
    'Attack method: Hostage Taking (Barricade Incident)',
    'Attack method: Unarmed Assault',
    'Attack method: Facility/Infrastructure Attack',
    'Attack method: Hostage Taking (Kidnapping)',
    'Attack method: Assassination',
    'Attack method: Armed Assault',
    'Attack method: Bombing/Explosion'
]
labels=[]
for label in attack_methods:
  data = label.split(':')
  labels.append(data[1])

# Extract relevant columns from the DataFrame
attack_counts = terror_df[attack_methods].sum()

myexplode = [0, 0, 0, 0, 0, 0, 0.2, 0]
total_attacks = attack_counts.sum()
autopct_values = [f'{(count/total_attacks)*100:.1f}%' for count in attack_counts]

# Plotting the pie chart
wedges, texts, autotexts = plt.pie(attack_counts, autopct='', startangle=90, explode = myexplode, colors=plt.cm.Paired.colors, shadow = True)

# Creating legend with attack method labels and autopct values
legend_labels = [f'{method}: {autopct}' for method, autopct in zip(labels, autopct_values)]
plt.legend(wedges, legend_labels, title='Attack Methods', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('Distribution of Terrorist Attack Methods', color='red')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Third subplot
plt.subplot(2, 2, 3)
for country in countries:
    country_data = terror_df[terror_df['Entity'] == country]
    country_data_filtered = country_data[country_data['Year'] >= 2000]
    plt.barh(country_data_filtered['Year'], country_data_filtered['Terrorism deaths'], label=f"{country} - Deaths")

plt.title('Deaths Count Because Of Terrorists Attacks',color='red')
plt.xlabel('Number of Deaths')
plt.ylabel('Year')
plt.legend()
plt.grid(True)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fourth subplot
plt.subplot(2, 2, 4)

for country in countries:
    country_data = gdp_df[gdp_df['Country'] == country].iloc[:, 1:]
    column_name = '2000'
    column_index = gdp_df.columns.get_loc(column_name)
    selected_columns = gdp_df.columns[column_index::5]
    country_data_selected = country_data[selected_columns]
    plt.plot(selected_columns, country_data_selected.values.flatten(), label=country, marker='o')

plt.xlabel('Year')
plt.ylabel('GDP')
plt.title('GDP Effected Due To Terrorist Attacks And Deaths ', color='red')
plt.grid(True)
plt.legend()

plt.suptitle("TERRORISM AND ITS EFFECTS", fontsize=24)


plt.figtext(0.05, 0.12, "Terrorism Dashboard Overview",  fontsize=12, fontweight='bold')
plt.figtext(0.05, 0.1, "This dashboard elaborates on terrorism and its effects, presenting data from 2000 onwards.",   fontsize=10)
plt.figtext(0.05, 0.08, "Pakistan faced the highest number of terrorist attacks between 2010 to 2015, while Afghanistan saw an increase from 2015 onwards.", fontsize=10)
plt.figtext(0.05, 0.06, "Bombing/Explosion is the most common type, accounting for 49.9% of attacks.",   fontsize=10)
plt.figtext(0.05, 0.04, "Exploring the impact of attacks on human lives.",  fontsize=10)
plt.figtext(0.05, 0.02, "Comparing the economic impact of terrorism, with a focus on countries like USA and Japan, which experience fewer attacks and deaths but have higher GDP.",  fontsize=10)

plt.figtext(0.80, 0.02, f'ID: {roll_number}\nNAME: {name}', fontsize=12, color='black',fontweight='bold')
plt.tight_layout(rect=[0, 0.14, 1, 1])
plt.savefig('22069616.png', dpi=300)

