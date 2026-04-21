#Read data from file. Assuming format in text file is User: #of entries (per line)
users_and_scores = {}
import os
with open("global_scores.txt", "r") as test: 
    for line in test:
        line = line.strip()
        
        if not line: 
            continue 

        if ":" in line: 
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            value = int(value)

            users_and_scores[key] = value #update dictionary with each key value pair
    
    #Turning the completed dictionary into a sorted list of tuples
    from operator import itemgetter
    mixed_users = list(users_and_scores.items()) 
    sorted_users = (sorted(mixed_users, key=itemgetter(1), reverse=True))
    top_five_users = (list(sorted_users[:5])) #should obtain top 5 users with the highest scores

    #create basic leaderboard using the top 5 users
    import pandas as pd

    headers = ['Username', 'Score']

    df = pd.DataFrame(top_five_users, columns=headers)
    df = df.reset_index()
    df.columns = ['Rank', 'Username', 'Score']
    df['Rank'] += 1
    print(df.to_string(index=False))
