s = 'William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.'.split()
count = 0
array = ['a', 'an', 'the']
for i in s:
    for j in array:
        if i.lower() == j:
            count += 1
print(count)