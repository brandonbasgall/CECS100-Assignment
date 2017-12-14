### = comment directed at you
# = explaining code to teacher


import turtle

candFile = open("Candidates.txt",'r')
numCandidates = int(candFile.readline())    # get number of candidates
print("Number of Candidates = ", numCandidates)
print(" ")


candidates = [ [], [] ]     # a list of lists of candidates in the 2 districts
for aLine in candFile:      # get names of candidates in the 2 districts
    nameLine = aLine.split()
    if int(nameLine[0]) == 1:       # candidate is in district 1
        candidates[0] = candidates[0] + [nameLine[1]]       #add name to district 1
    else:
        candidates[1] = candidates[1] + [nameLine[1]]       #add name to district 2


# lists of votes for candidates in the 2 districts, in votes as a list of lists
votes = [ [0]*len(candidates[0]), [0]*len(candidates[1]) ]
print("Number of candidates in district 1: ", len(candidates[0]))
print(candidates[0])
print(" ")
print("Number of candidates in district 2: ", len(candidates[1]))
print(candidates[1])


SmithCount = 0      ### The way I thought of doing it was setting occurance of names to 0,
JohnsonCount = 0    ### and then counting each time one of the five names showed up.
LeroyCount = 0
PrattCount = 0
LanceCount = 0


ballotInput = open("Ballots.txt",'r')       # open and read the ballots file
votes = ballotInput.read()
list_of_votes = votes.split()       # split contents into words


for word in list_of_votes:      ### When a name is counted, adds 1 to their count.
    if "Leroy" in word:         ### This is used for graph.
        LeroyCount = LeroyCount + 1

    if "Smith" in word:
        SmithCount = SmithCount + 1

    if "Johnson" in word:
        JohnsonCount = JohnsonCount + 1

    if "Pratt" in word:
        PrattCount = PrattCount + 1

    if "Lance" in word:
        LanceCount = LanceCount + 1
        

### However, this is wrong, and I'm having trouble figuring out how to count occurances
### of names without writing a check for each name individually. I'd appreciate it if you could
### point me in the direction of how to do that. By the way if this is going to interfere with
### your studying, please let me know, I don't want to take up any important time.
