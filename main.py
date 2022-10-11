# Blade Idle Options Optimization

import numpy as np
import numbas
from tabulate import tabulate

# Pseudo code:
# List of all options

# Initialize all options to a default(opt atk > figure atk > hyper crit > crit > super crit)
# 	Go through list and calculate if swapping option will be an increase. If so, how much?
# 	Adjust the one the increases damage the most

DEBUG_PRINTS = False

ENUM_OPTION_ATK = 0
ENUM_SPR_OPTATK = 1
ENUM_CRITDMG___ = 2
ENUM_SPRCRITDMG = 3
ENUM_HYPCRITDMG = 4

def option_name(enum):
    return {
        "Option Attack": ENUM_OPTION_ATK,
        "Super Option Attack": ENUM_SPR_OPTATK,
        "Crit Damage": ENUM_CRITDMG___,
        "Super Crit Damage": ENUM_SPRCRITDMG,
        "Hyper Crit Damage": ENUM_HYPCRITDMG
    }[enum]

option_name_dict = {
    ENUM_OPTION_ATK: "Option Attack",
    ENUM_SPR_OPTATK: "Super Option Attack",
    ENUM_CRITDMG___: "Crit Damage",
    ENUM_SPRCRITDMG: "Super Crit Damage",
    ENUM_HYPCRITDMG: "Hyper Crit Damage"
}


def main():

    base_stats = np.array([
    #    OPTION_ATK | SPR_OPTATK | CRITDMG___ | SPRCRITDMG | HYPCRITDMG
         100,         100,         100,         100,         100       
    ], dtype=np.float32)

    num_options = numbas.option_matrix.shape[0]
    num_stats = base_stats.shape[0]

    # Setup Decision Matrix
    decision_matrix = np.zeros([num_options,num_stats])
    # Initialize Decision Matrix
    Init_Matrix_Option = False # Set True if you don't empty starting decision matrix
    if Init_Matrix_Option:
        STAT_TO_START_ON = ENUM_OPTION_ATK # Which option to start at all 1's
        for i in range(num_options):
            decision_matrix[i][STAT_TO_START_ON] = 1


    # Optimization Algorithm
    max_iter = 100
    best_decision_matrix = decision_matrix.copy()
    for iter in range(max_iter):
        
        best_subgroup_decision_matrix = best_decision_matrix.copy()
        best_dmg = calculate_dmg(base_stats, numbas.option_matrix, best_decision_matrix)
        for i in range(num_options):
            best_subgroup_dmg = calculate_dmg(base_stats, numbas.option_matrix, best_subgroup_decision_matrix)
            for j in range(num_stats):
                #cur_decision_matrix = best_subgroup_decision_matrix.copy() # This makes it faster but probably not global maximum
                cur_decision_matrix = best_decision_matrix.copy()
                cur_decision_matrix[i] = np.zeros(num_stats)
                cur_decision_matrix[i][j] = 1
                cur_dmg = calculate_dmg(base_stats, numbas.option_matrix, cur_decision_matrix)
                if cur_dmg > best_subgroup_dmg:
                    best_subgroup_decision_matrix = cur_decision_matrix.copy()
                    best_subgroup_dmg = cur_dmg
                    if DEBUG_PRINTS:
                        print("new group best found")
                        print(cur_dmg)
                        print(best_subgroup_dmg)
                        print(cur_decision_matrix)
                    
        best_subgroup_dmg = calculate_dmg(base_stats, numbas.option_matrix, best_subgroup_decision_matrix)
        if DEBUG_PRINTS:
            print("testing for new best")
            print(best_subgroup_decision_matrix)
            print(best_subgroup_dmg)
            print(best_dmg)
        if best_subgroup_dmg > best_dmg:
            if DEBUG_PRINTS:
                print("new total best found")
            best_decision_matrix = best_subgroup_decision_matrix.copy()
            best_dmg = best_subgroup_dmg
        elif best_subgroup_dmg == best_dmg:
            #if DEBUG_PRINTS:
            print("Maximum reached")
            print("Iterations: " + str(iter))
            break

    decision_matrix = best_decision_matrix.copy()

    # Calculate and print results
    if DEBUG_PRINTS:
        print(numbas.option_matrix)
        print(decision_matrix)
    final_dmg = calculate_dmg(base_stats, numbas.option_matrix, decision_matrix)
    print_results(base_stats, numbas.option_matrix, numbas.name_array, decision_matrix)
    return 0

# Returns total damage as MULTIPLIER not a PERCENTAGE
def calculate_dmg(this_base_stats, this_option_matrix, this_decision_matrix):

    total_stats = this_base_stats.copy()
    num_options = this_option_matrix.shape[0]
    num_stats   = this_option_matrix.shape[1]

    for i in range(num_options):
        for j in range(num_stats):
            total_stats[j] += this_decision_matrix[i][j] * this_option_matrix[i][j]

    total_dmg = 1
    #print(total_stats)
    for i in range(num_stats):
        total_dmg *= total_stats[i] / 100

    if DEBUG_PRINTS:
        print(total_dmg)

    return total_dmg

def print_results(base_stats, option_matrix, name_array, decision_matrix):

    # Tabulate best option for each equipment
    num_options = len(name_array)
    option_string = ""
    output_table = []
    for i in range(num_options):
        table_entry = []
        table_entry.append(name_array[i])
        table_entry.append(str(option_name_dict[np.where(decision_matrix[i] == 1)[0][0]]))
        #print(name_array[i] + ": " + str(option_name_dict[np.where(decision_matrix[i] == 1)[0][0]]))
        output_table.append(table_entry)


    # Calculate and tabulate total stats
    total_stats = base_stats.copy()
    num_options = option_matrix.shape[0]
    num_stats   = option_matrix.shape[1]

    for i in range(num_options):
        for j in range(num_stats):
            total_stats[j] += decision_matrix[i][j] * option_matrix[i][j]

    stat_table = []
    for i in range(num_stats):
        table_entry = []
        table_entry.append(total_stats[i])
        table_entry.append(str(option_name_dict[i]))
        stat_table.append(table_entry)

    # Calculate Final Damage
    final_dmg = calculate_dmg(base_stats, numbas.option_matrix, decision_matrix)

    # Print Results
    print(tabulate(output_table, headers=["Equipment", "Optimal Option"]))
    print("\n")
    print(tabulate(stat_table, headers=["Total", "Option"]))
    print("\n")
    print("Final Total Attack Multiplier: " + str(final_dmg))
    return 0

if __name__ == "__main__":
    main()