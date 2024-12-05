import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read()
    
    [rules, updates] = raw_data.split('\n\n')
    
    rules = rules.split('\n')
    rules = [[int(pg) for pg in rule.split('|')] for rule in rules]
    
    updates = updates.split('\n')
    updates = [[int(pg) for pg in update.split(',')] for update in updates]

    sum_mid_pg = 0
    for update in updates:
        correct = True
        for rule in rules:
            # check if rule[0] appears before rule[1] in update
            if rule[0] in update and rule[1] in update and \
                update.index(rule[0]) > update.index(rule[1]):
                correct = False
                break
        
        if correct:
            continue
        
        # correct the update in order
        rules_this_update = {key: 0 for key in update}
        # count how many page numbers are in front of each key (number)
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                rules_this_update[rule[1]] += 1
        # sort keys in order of their value
        update.sort(key=lambda x: rules_this_update[x])
        sum_mid_pg += update[len(update)//2]
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the middle page number after correctly ordering is: {sum_mid_pg}. ')

if __name__ == '__main__':
    main(sys.argv[1])