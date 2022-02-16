def AddDie(oldspread, size):
    newspread = {}
    newspread['inf'] = oldspread['inf']+1
    newspread['sup'] = oldspread['sup']+size
    oldspreadlist = [oldspread[i] for i in range(oldspread['inf'], oldspread['sup']+1)]
    for i in range(newspread['inf'],newspread['sup']+1):
        newspread[i] = sum(oldspreadlist[max(i-size-oldspread['inf'],0):min(i-oldspread['inf'],oldspread['sup'])])
    return newspread
def PrintHP(level, size, bonus, fulllist):
    current = {}
    current['inf'] = 1
    current['sup'] = size
    for i in range(1,size+1):
        current[i] = 1
    for i in range(level-1):
        current = AddDie(current, size)
    HPlist = []
    currentHP = 0
    for i in range(level, size*level+1):
        currentHP += current[i]
        HPlist.append(currentHP)
    if fulllist == 1:
        for i in range(level, size*level+1):
            print ("{} : {:.4}%".format(i+bonus, 100*HPlist[i-level] / currentHP))
    HPpercentlist = [item / currentHP for item in HPlist]
    milestones = []
    thresholds = [0.05 * (i+1) for i in range(19)]
    thresholds.insert(0,0.01)
    thresholds.append(0.99)
    for milestone in thresholds:
        for i, value in enumerate(HPpercentlist):
            if value >= milestone:
                milestones.append(i+current['inf']+bonus)
                break
    milestones = list(dict.fromkeys(milestones))
    print ("Summary for {}d{} + {}: ".format(level, size, bonus))
    for value in milestones:
        print ("{:.4}% chance of death at {} damage".format(100*HPpercentlist[value-bonus-current['inf']],value))
    return current       
while True:
    dice = int(input("number: "))
    size = int(input("size: "))
    bonus = int(input("bonus: "))
    PrintHP(dice,size,bonus,fulllist=0)
        
        
           
