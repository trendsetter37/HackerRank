def PI_Song(string):
    
    for idx, word in enumerate(string.split()):
        if len(word) != int(PI[idx]):
            return "It's not a pi song." 
    else:
        return "It's a pi song."

#end
if __name__ == '__main__':
    PI = "31415926535897932384626433833"
    for i in range(int(input())):
        print(PI_Song(input()))
        