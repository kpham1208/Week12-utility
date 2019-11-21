# GITHUB URL
#  Kenny Pham
# CSCI 102 - Section E
#  Week 12 - Part B

def PrintOutput(String_Input):
    print(String_Input)
    
def LoadFile(File_Name):
    with open(File_Name, 'r') as f:
        return [line.strip('\n') for line in f]

def UpdateString(string, character, position):
    string = list(string)
    string[position] = character
    result = ''.join(string)
    print(result)

def FindWordCount(a, string):
        wordcount = 0
        j = 0
        k = j + len(string)
        for line in a:
            if line[j:k] == string:
                wordcount += 1
        return wordcount

def ScoreFinder(players, scores, player):
    j = 0
    k = j + len(player)
    for i in players:
        if i[j:k] == player:
            players[player] = scores[player]
            print('OUTPUT ', player, 'got a score of', score[i])
        else:
            print('OUTPUT player not found')
    
