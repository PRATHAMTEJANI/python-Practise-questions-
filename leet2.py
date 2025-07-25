import pandas as pd

data = [
    [100, 'prahtam' , 20 , 'forward' , 'realmadrid'] , 
    [749, 'Riley', 30, 'Winger', 'Barcelona'],
    [155, 'Bob', 28, 'Striker', 'ManchesterUnited'],
    [583, 'Isabella', 32, 'Goalkeeper', 'Liverpool'],
    [388, 'Zachary', 24, 'Midfielder', 'BayernMunich'],
    [883, 'Ava', 23, 'Defender', 'Chelsea'],
    [355, 'Violet', 18, 'Striker', 'Juventus'],
    [247, 'Thomas', 27, 'Striker', 'ParisSaint-Germain'],
    [761, 'Jack', 33, 'Midfielder', 'ManchesterCity'],
    [642, 'Charlie', 36, 'Center-back', 'Arsenal']
]

columns = ['player_id','name','age','position','team']
df = pd.DataFrame(data , columns=columns)
print(df.shape[0])
print(df.shape[1])

