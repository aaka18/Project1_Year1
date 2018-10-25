import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import math
# Items in the wordpool (N = 50), alphabetically ordered
word_pool = ['burrito', 'casserole', 'cheeseburger', 'cheesecake', 'chili', 'chips', 'chowder', 'cookie', 'cornbread', 'crepe', 'croissant', 'cupcake', 'custard', 'doughnut', 'enchilada', 'granola', 'grits', 'gumbo', 'hamburger', 'hummus', 'jambalaya', 'jelly', 'kebab', 'macaroni', 'macaroon', 'meatball', 'meatloaf', 'muffin', 'nacho', 'noodles', 'oatmeal', 'omelet', 'pancake', 'pasta', 'pizza', 'popcorn', 'pretzel', 'pudding', 'quiche', 'ravioli', 'rice', 'risotto', 'salad', 'sandwich', 'sausage', 'soup', 'spaghetti', 'steak', 'sushi', 'tiramisu']

# Word id's for each item
word_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]


# If participants completed recall task first, the question numbers that correspond to items are:
recall_first = ['Q2', 'Q4', 'Q6', 'Q8', 'Q10', 'Q12', 'Q14', 'Q16', 'Q18', 'Q20', 'Q22', 'Q24', 'Q26', 'Q28', 'Q30', 'Q32', 'Q34', 'Q36', 'Q38', 'Q40', 'Q42', 'Q44', 'Q46', 'Q48', 'Q50', 'Q156', 'Q158', 'Q160', 'Q162', 'Q164', 'Q166', 'Q168', 'Q170', 'Q172', 'Q174', 'Q176', 'Q178', 'Q180', 'Q182', 'Q184', 'Q186', 'Q188', 'Q190', 'Q192', 'Q194', 'Q196', 'Q198', 'Q200', 'Q202', 'Q204']

# If participants completed consideration task first, the question numbers that correspond to items are:
consideration_first = ['Q334', 'Q336', 'Q338', 'Q340', 'Q342', 'Q344', 'Q346', 'Q348', 'Q350', 'Q352', 'Q354', 'Q356', 'Q358', 'Q360', 'Q362', 'Q364', 'Q366', 'Q368', 'Q370', 'Q372', 'Q374', 'Q376', 'Q378', 'Q380', 'Q382', 'Q488', 'Q490', 'Q492', 'Q494', 'Q496', 'Q498', 'Q500', 'Q502', 'Q504', 'Q506', 'Q508', 'Q510', 'Q512', 'Q514', 'Q516', 'Q518', 'Q520', 'Q522', 'Q524', 'Q526', 'Q528', 'Q530', 'Q532', 'Q534', 'Q536']

recall_first_dict = {}
for i in range(len(word_ids)):
   recall_first_dict[recall_first[i]] = word_ids[i]

consideration_first_dict = {}
for i in range(len(word_ids)):
   consideration_first_dict[consideration_first[i]] = word_ids[i]

wordpool_dict = {}
for i in range(len(word_ids)):
   wordpool_dict[word_pool[i]] = word_ids[i]


whole_dataset =  pd.read_csv('try_this_all_data.csv')

recall_first_dataset = whole_dataset.loc[whole_dataset['FL_6_DO'] == 'Recall_First']
consideration_first_dataset = whole_dataset.loc[whole_dataset['FL_6_DO'] == 'Consideration_First']
# print(consideration_first_dataset)

recall_first_dataset = recall_first_dataset.applymap(lambda s:s.lower() if type(s) == str else s)
consideration_first_dataset = consideration_first_dataset.applymap(lambda s:s.lower() if type(s) == str else s)

consideration_first_choice_ids = []
# For all the columns except the Recall_display_order column
for choice in consideration_first_dataset['Q486']:
   # print(item)
    this_choice = []
    if choice in word_pool:
        this_choice.append(wordpool_dict[choice])
    else:
        this_choice.append((-1))
    consideration_first_choice_ids.append(this_choice)
print(consideration_first_choice_ids)
print(np.array(consideration_first_choice_ids).shape)


# print(recall_first_dataset['Q486'])
# # Finding the Choice item
#
recall_first_choice_ids = []
for choice in recall_first_dataset['Q310']:
    this_choice = []
    if choice in word_pool:
        this_choice.append(wordpool_dict[choice])
    else:
        this_choice.append((-1))
    recall_first_choice_ids.append(this_choice)
print(recall_first_choice_ids)
print(np.array(recall_first_choice_ids).shape)

choice_recall_first = '/Users/adaaka/Desktop/Project1_Year1/choice_recall_first'
choice_cons_first = '/Users/adaaka/Desktop/Project1_Year1/choice_cons_first'

np.save(choice_recall_first, recall_first_choice_ids)
np.save(choice_cons_first, consideration_first_choice_ids)