
with open('game.txt', "r") as file:
    datas = file.read().split("\n")
    #making a new list with all the data .Splitting by line
    #datas = datas.split('\n')  
coinWriteFile = open("coins.txt", "w")
coins = 0
count = 0
valid = []

while True:
    #breaks the code if the count is more than the length of the list. Out of bounds
    if count >= len(datas):
        False
        break;
    line = datas[count]
    lineList = line.split(' ')
    #if the first word is coin, then it will add the number to coins
    if(lineList[0]== 'coin'):
        #creates a new amt variable to store tha valuue of coin, so that it can later be written in the file
        amt = int(lineList[1])
        coins += int(amt)
        coinWriteFile.write(str(amt))
        coinWriteFile.write("\n")
        valid.append(amt)
        count += 1
        #if it is jump, then it will jump to the index speciifed. 
    elif lineList[0] == 'jump':
        #The index is modified based on the data
        count += int(lineList[1])
    else:
        #if it is either, then count is just incremented
        count += 1
 
'''    
newFile = open("coins.txt",'w')
for coin in valid:
    coin = str(coin)
    newFile.write(coin)
    #rewriting the new file with values from the valid list
    newFile.write('\n')
newFile.close() 
    #prints final value
    '''
print(f"Total coins collected: {coins}")