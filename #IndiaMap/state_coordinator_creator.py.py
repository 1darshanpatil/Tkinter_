#This code creates cordinates.csv based on image
#This code is used to get the coordinates of states
import turtle as T
import pandas as pd
import time
dic = {}
states = []
x_cord = []
y_cord = []


def click_cords(x, y):
    global x_cord, y_cord, states
    states.append(input('state: '))
    x_cord.append(x)
    y_cord.append(y)
    #print(x, y)

scrn = T.Screen()
#/Users/1954513/Desktop/#100_Days_of_Python/#25-Day/
img_path = 'indiamap.gif'
# Image should have to be gif
scrn.addshape(img_path)
T.shape(img_path)
scrn.onscreenclick(click_cords)
scrn.mainloop()


#Creating a .csv file to save above data

dic['states'] = states
dic['x'] = x_cord
dic['y'] = y_cord

df = pd.DataFrame.from_dict(dic)
df.to_csv(f'Storage_created_{time.time()}.csv', index = False)
print('End')











