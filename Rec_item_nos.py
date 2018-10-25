import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import math
# Items in the wordpool (N = 50), alphabetically ordered
word_pool = ['burrito', 'casserole', 'cheeseburger', 'cheesecake', 'chili', 'chips', 'chowder', 'cookie', 'cornbread', 'crepe', 'croissant', 'cupcake', 'custard', 'doughnut', 'enchilada', 'granola', 'grits', 'gumbo', 'hamburger', 'hummus', 'jambalaya', 'jelly', 'kebab', 'macaroni', 'macaroon', 'meatball', 'meatloaf', 'muffin', 'nacho', 'noodles', 'oatmeal', 'omelet', 'pancake', 'pasta', 'pizza', 'popcorn', 'pretzel', 'pudding', 'quiche', 'ravioli', 'rice', 'risotto', 'salad', 'sandwich', 'sausage', 'soup', 'spaghetti', 'steak', 'sushi', 'tiramisu']

# print(len(word_pool))
# print(word_pool)

# Word id's for each item
word_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]


# If participants completed recall task first, the question numbers that correspond to items are:
recall_first = ['Q2', 'Q4', 'Q6', 'Q8', 'Q10', 'Q12', 'Q14', 'Q16', 'Q18', 'Q20', 'Q22', 'Q24', 'Q26', 'Q28', 'Q30', 'Q32', 'Q34', 'Q36', 'Q38', 'Q40', 'Q42', 'Q44', 'Q46', 'Q48', 'Q50', 'Q156', 'Q158', 'Q160', 'Q162', 'Q164', 'Q166', 'Q168', 'Q170', 'Q172', 'Q174', 'Q176', 'Q178', 'Q180', 'Q182', 'Q184', 'Q186', 'Q188', 'Q190', 'Q192', 'Q194', 'Q196', 'Q198', 'Q200', 'Q202', 'Q204']

# If participants completed consideration task first, the question numbers that correspond to items are:
consideration_first = ['Q334', 'Q336', 'Q338', 'Q340', 'Q342', 'Q344', 'Q346', 'Q348', 'Q350', 'Q352', 'Q354', 'Q356', 'Q358', 'Q360', 'Q362', 'Q364', 'Q366', 'Q368', 'Q370', 'Q372', 'Q374', 'Q376', 'Q378', 'Q380', 'Q382', 'Q488', 'Q490', 'Q492', 'Q494', 'Q496', 'Q498', 'Q500', 'Q502', 'Q504', 'Q506', 'Q508', 'Q510', 'Q512', 'Q514', 'Q516', 'Q518', 'Q520', 'Q522', 'Q524', 'Q526', 'Q528', 'Q530', 'Q532', 'Q534', 'Q536']

# print(recall_first)
# print(consideration_first)

recall_first_dict = {}
for i in range(len(word_ids)):
   recall_first_dict[recall_first[i]] = word_ids[i]

consideration_first_dict = {}
for i in range(len(word_ids)):
   consideration_first_dict[consideration_first[i]] = word_ids[i]

wordpool_dict = {}
for i in range(len(word_ids)):
   wordpool_dict[word_pool[i]] = word_ids[i]



#whole_dataset =  pd.read_csv('Pilot1_October 8.csv')
#print(whole_dataset.describe())
# Deleted the first rows that do not mean anything
whole_dataset =  pd.read_csv('try_this_all_data.csv')
#print(whole_dataset.describe())

#Making recalled items lower case
# whole_dataset = whole_dataset.applymap(lambda s:s.lower() if type(s) == str else s)

recall_first_dataset = whole_dataset.loc[whole_dataset['FL_6_DO'] == 'Recall_First']
#print(recall_first_dataset)
consideration_first_dataset = whole_dataset.loc[whole_dataset['FL_6_DO'] == 'Consideration_First']
#print(consideration_first_dataset)

#print("H")
recall_first_dataset = recall_first_dataset.applymap(lambda s:s.lower() if type(s) == str else s)
consideration_first_dataset = consideration_first_dataset.applymap(lambda s:s.lower() if type(s) == str else s)

# We extract these datasets so that we can get the recalled item nos from each list

recall_first_recall = ['ResponseId', 'Q54', 'Q56', 'Q58', 'Q60', 'Q62', 'Q64', 'Q66', 'Q68', 'Q70', 'Q72', 'Q74', 'Q76', 'Q78', 'Q80', 'Q82', 'Q84', 'Q86', 'Q88', 'Q90', 'Q92', 'Q94', 'Q96', 'Q98', 'Q100', 'Q102', 'Q104', 'Q106', 'Q108', 'Q110', 'Q112', 'Q114', 'Q116', 'Q118', 'Q120', 'Q122', 'Q124', 'Q126', 'Q128', 'Q130', 'Q132', 'Q134', 'Q136', 'Q138', 'Q140', 'Q142', 'Q144', 'Q146', 'Q148', 'Q150', 'Q152']
recall_first_consider = ['ResponseId','Q208', 'Q210', 'Q212', 'Q214', 'Q216', 'Q218', 'Q220', 'Q222', 'Q224', 'Q226', 'Q228', 'Q230', 'Q234', 'Q236', 'Q238', 'Q240', 'Q242', 'Q244', 'Q246', 'Q248', 'Q250', 'Q252', 'Q254', 'Q256', 'Q258', 'Q260', 'Q262', 'Q264', 'Q266', 'Q268', 'Q270', 'Q272', 'Q274', 'Q276', 'Q278', 'Q279', 'Q281', 'Q283', 'Q285', 'Q287', 'Q289', 'Q291', 'Q293', 'Q295', 'Q297', 'Q299', 'Q301', 'Q303', 'Q305', 'Q307']


consideration_first_consider = ['ResponseId','Q386', 'Q388', 'Q390', 'Q392', 'Q394', 'Q396', 'Q398', 'Q400', 'Q402', 'Q404', 'Q406', 'Q408', 'Q410', 'Q412', 'Q414', 'Q416', 'Q418', 'Q420', 'Q422', 'Q424', 'Q426', 'Q428', 'Q430', 'Q432', 'Q434', 'Q436', 'Q438', 'Q440', 'Q442', 'Q444', 'Q446', 'Q448', 'Q450', 'Q452', 'Q454', 'Q456', 'Q458', 'Q460', 'Q462', 'Q464', 'Q466', 'Q468', 'Q470', 'Q472', 'Q474', 'Q476', 'Q478', 'Q480', 'Q482', 'Q484']
consideration_first_recall = ['ResponseId','Q540', 'Q542', 'Q544', 'Q546', 'Q548', 'Q550', 'Q552', 'Q554', 'Q556', 'Q558', 'Q560', 'Q562', 'Q564', 'Q566', 'Q568', 'Q570', 'Q572', 'Q574', 'Q576', 'Q578', 'Q580', 'Q582', 'Q584', 'Q586', 'Q588', 'Q590', 'Q592', 'Q594', 'Q596', 'Q598', 'Q600', 'Q602', 'Q604', 'Q606', 'Q608', 'Q610', 'Q612', 'Q614', 'Q616', 'Q618', 'Q620', 'Q622', 'Q624', 'Q626', 'Q628', 'Q630', 'Q632', 'Q634', 'Q636', 'Q638']


recall_first_recall_dataset = recall_first_dataset[recall_first_recall]
#print(recall_first_recall_dataset.columns)
recall_first_consider_dataset = recall_first_dataset[recall_first_consider]
#print(recall_first_consider_dataset.columns)


consideration_first_consider_dataset = consideration_first_dataset[consideration_first_consider]
#print(consideration_first_consider_dataset.columns)

consideration_first_recall_dataset = consideration_first_dataset[consideration_first_recall]
#print(consideration_first_recall_dataset.columns)

recalled_ids_recall_first_recall = []
recalled_ids_recall_first_consider = []
recalled_ids_consideration_first_consider = []
recalled_ids_consideration_first_recall = []


# For all the columns except the RespnseId column:
for column in recall_first_recall_dataset.columns[1:]:
    this_question = []
    # Match the recalled item with word id
    for item in recall_first_recall_dataset[column]:
        if item in word_pool:
            this_question.append(wordpool_dict[item])
        else:
            this_question.append((-1))
    recalled_ids_recall_first_recall.append(this_question)



recalled_ids_recall_first_recall = (np.transpose(recalled_ids_recall_first_recall))
# recalled_ids_recall_first_recall = np.c_[(recalled_ids_recall_first_recall, recall_first_recall_dataset['ResponseId'])]
# print(recalled_ids_recall_first_recall)
# print(recalled_ids_recall_first_recall.shape)
# print("Recalled ids Recall First Recall", recalled_ids_recall_first_recall)
print("Recalled ids  Recall First Recall shape", np.array(recalled_ids_recall_first_recall).shape)
##
# For all the columns except the RespnseId column:
for column in recall_first_consider_dataset.columns[1:]:
    this_question = []
    # Match the recalled item with word id
    for item in recall_first_consider_dataset[column]:
        if item in word_pool:
            this_question.append(wordpool_dict[item])
        else:
            this_question.append((-1))
    recalled_ids_recall_first_consider.append(this_question)


recalled_ids_recall_first_consider= (np.transpose(recalled_ids_recall_first_consider))
# recalled_ids_recall_first_consider = np.c_[(recalled_ids_recall_first_consider, recall_first_consider_dataset['ResponseId'])]
# print(recalled_ids_recall_first_consider)
# print(recalled_ids_recall_first_consider.shape)
# print("Recalled ids  Recall First Consider", recalled_ids_recall_first_consider)
print("Recalled ids  Recall First Consider shape", np.array(recalled_ids_recall_first_consider).shape)
##
# For all the columns except the RespnseId column:
for column in consideration_first_consider_dataset.columns[1:]:
    this_question = []
    # Match the recalled item with word id
    for item in consideration_first_consider_dataset[column]:
        if item in word_pool:
            this_question.append(wordpool_dict[item])
        else:
            this_question.append((-1))
    recalled_ids_consideration_first_consider.append(this_question)


recalled_ids_consideration_first_consider = (np.transpose(recalled_ids_consideration_first_consider))
# recalled_ids_consideration_first_consider = np.c_[(recalled_ids_consideration_first_consider, consideration_first_consider_dataset['ResponseId'])]
# print(recalled_ids_consideration_first_consider)
# print(recalled_ids_consideration_first_consider.shape)
# print("Recalled ids Consider first consider", recalled_ids_consideration_first_consider)
print("Recalled ids Consider first consider shape", np.array(recalled_ids_consideration_first_consider).shape)
##
# For all the columns except the RespnseId column:
for column in consideration_first_recall_dataset.columns[1:]:
    this_question = []
    # Match the recalled item with word id
    for item in consideration_first_recall_dataset[column]:
        if item in word_pool:
            this_question.append(wordpool_dict[item])
        else:
            this_question.append((-1))
    recalled_ids_consideration_first_recall.append(this_question)


recalled_ids_consideration_first_recall = (np.transpose(recalled_ids_consideration_first_recall))
# recalled_ids_consideration_first_recall = np.c_[(recalled_ids_consideration_first_recall,consideration_first_recall_dataset['ResponseId'])]
# print(recalled_ids_consideration_first_recall)
# print(recalled_ids_consideration_first_recall.shape)
# print("Recalled ids Consider first recall", recalled_ids_consideration_first_recall)
print("Recalled ids shape", np.array(recalled_ids_consideration_first_recall).shape)


rec_items_rec_rec = '/Users/adaaka/Desktop/Project1_Year1/rec_items_rec_rec'
rec_items_rec_cons = '/Users/adaaka/Desktop/Project1_Year1/rec_items_rec_cons'
rec_items_cons_con = '/Users/adaaka/Desktop/Project1_Year1/rec_items_cons_con'
rec_items_cons_rec = '/Users/adaaka/Desktop/Project1_Year1/rec_items_cons_rec'

np.save(rec_items_rec_rec, recalled_ids_recall_first_recall)
np.save(rec_items_rec_cons, recalled_ids_recall_first_consider)
np.save(rec_items_cons_con, recalled_ids_consideration_first_consider)
np.save(rec_items_cons_rec, recalled_ids_consideration_first_recall)

# Subject IDs
print(recall_first_recall_dataset['ResponseId'])
print(recall_first_consider_dataset['ResponseId'])
print(consideration_first_consider_dataset['ResponseId'])
print(consideration_first_recall_dataset['ResponseId'])