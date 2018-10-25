import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import math


whole_dataset =  pd.read_csv('try_this_all_data.csv')

recall_first_dataset = whole_dataset.loc[whole_dataset['FL_6_DO'] == 'Recall_First']
consideration_first_dataset = whole_dataset.loc[whole_dataset['FL_6_DO'] == 'Consideration_First']

# Preference rating question headers to later extract data

preference_question_order = []

for i in range(1, 50):
    qname = 'Q326_'
    preference_question_order.append(qname+ str(i))

preference_question_order.append('ResponseId')
# print(preference_question_order)

preference_dataset = whole_dataset[preference_question_order]
# print(preference_dataset)

preference_ratings = preference_dataset.as_matrix()
print(preference_ratings.shape)


# Healthiness rating question headers to later extract data

healthiness_question_order = []

for i in range(1, 50):
    qname = 'Q330_'
    healthiness_question_order.append(qname+ str(i))

healthiness_question_order.append('ResponseId')
# print(healthiness_question_order)

healthiness_dataset = whole_dataset[healthiness_question_order]
# print(healthiness_dataset)

healthiness_ratings = healthiness_dataset.as_matrix()
print(healthiness_ratings.shape)

# Frequency rating question headers to later extract data

frequency_question_order = []

for i in range(1, 50):
    qname = 'Q332_'
    frequency_question_order.append(qname+ str(i))

frequency_question_order.append('ResponseId')
# print(frequency_question_order)

frequency_dataset = whole_dataset[frequency_question_order]
# print(preference_dataset)

frequency_ratings = frequency_dataset.as_matrix()
print(frequency_ratings.shape)

# Frequency (YES/NO) rating question headers to later extract data

binary_frequency_question_order = []

for i in range(1, 50):
    qname = 'Q333_'
    binary_frequency_question_order.append(qname+ str(i))

binary_frequency_question_order.append('ResponseId')
# print(binary_frequency_question_order)
binary_frequency_dataset = whole_dataset[binary_frequency_question_order]
# print(preference_dataset)

binary_frequency_ratings = binary_frequency_dataset.as_matrix()
print(binary_frequency_ratings.shape)

pref_ratings = '/Users/adaaka/Desktop/Project1_Year1/pref_ratings'
health_ratings = '/Users/adaaka/Desktop/Project1_Year1/health_ratings'
freq_ratings = '/Users/adaaka/Desktop/Project1_Year1/freq_ratings'
binary_freq_ratings = '/Users/adaaka/Desktop/Project1_Year1/binary_freq_ratings'

np.save(pref_ratings, preference_ratings)
np.save(health_ratings, healthiness_ratings)
np.save(freq_ratings, frequency_ratings)
np.save(binary_freq_ratings, binary_frequency_ratings)
