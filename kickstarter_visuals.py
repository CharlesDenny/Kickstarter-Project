import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

df = pd.read_csv("kickstarter_2018_clean.csv")

useful = df[['category', 'main_category' ,'usd_goal_real','days_elapsed', 'state']]

useful.category = pd.Categorical(useful.category)
#print(useful.category)
useful.main_category = pd.Categorical(useful.main_category)
useful.usd_goal_real = pd.Categorical(useful.usd_goal_real)
useful.days_elapsed = pd.Categorical(useful.days_elapsed)
useful.state = pd.Categorical(useful.state)

categories = []
main_categories = []

for i in range(0, 331674):
    newcat = useful.category[i]
    newmaincat = useful.main_category[i]
    if newcat in categories:
        pass
    else:
        categories.append(newcat)
    if newmaincat in main_categories:
        pass
    else:
        main_categories.append(newmaincat)
        
#print(categories)
#print(main_categories)

main_categories_data = []
successes = 0
failures = 0
total = 0
success_rate = 0
failure_rate = 0

for i in range(0, 15):
    main_category_data = {'main_category': main_categories[i], 'successes': successes, 'failures': failures, 'total': total, 'success_rate': success_rate, 'failure_rate': failure_rate}   # successes, failures, total
    main_categories_data.append(main_category_data)
    #print(main_categories_data[i]['main_category'])

for i in range(0, 331674):
    main_category = useful.main_category[i]
    state = useful.state[i]
    for i in range(0, 15):
        if main_category == main_categories_data[i]['main_category']:
            if state == 'successful':
                main_categories_data[i]['successes'] += 1
            if state == 'failed':
                main_categories_data[i]['failures'] += 1
            main_categories_data[i]['total'] += 1
            
for i in range(0, 15):
    main_categories_data[i]['success_rate'] =  main_categories_data[i]['successes']/main_categories_data[i]['total']
    main_categories_data[i]['failure_rate'] =  main_categories_data[i]['failures']/main_categories_data[i]['total']
    
#print(main_categories_data)

for i in range(0, 15):
    labels = 'Success', 'Failure'
    sizes = [main_categories_data[i]['success_rate']*100, main_categories_data[i]['failure_rate']*100]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=['green', 'red'], labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(main_categories_data[i]['main_category'], bbox={'facecolor':'0.8', 'pad':5})
    plt.show()

    
objects = []
resultdata = []



for i in range(0, 15):
    objects.append(main_categories_data[i]['main_category'])
    resultdata.append(main_categories_data[i]['success_rate']*100)
    
df = pd.DataFrame({'objects' : objects , 'resultdata' : resultdata})
df = df.sort_values('resultdata')
    
#print(objects)

#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
#resultdata = [10,8,6,4,2,1]
plt.figure(figsize=(20, 10))  # width:20, height:3
plt.bar(y_pos, resultdata, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Success Rate (%)')
plt.title('Success Rates For Each Main Category')


    
# https://stackoverflow.com/questions/49015957/how-to-get-python-graph-output-into-html-webpage-directly
    
