# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player (prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'P'

    opponent_history.append(prev_play)
    prediction = 'P'
    count = len(opponent_history)

    if count > 5:
        last_five = "".join(opponent_history[-5:])
        play_order[last_five]=play_order.get(last_five,0)+1

        pot_play = ["".join([*opponent_history[-4:], v])
        for v in ['R','P','S']]

        sb_order ={k: play_order[k] for k in pot_play if k in play_order}

        if sb_order:
            prediction=max(sb_order,key=sb_order.get)[-1:]

    idealAnsw = {'P':'S', 'R':'P', 'S':'R'}

    return idealAnsw[prediction]   

    
# import random

# def player(prev_play, opponent_history=[]):
#     # Append the previous play to the opponent's history
#     opponent_history.append(prev_play)
#     count = len(opponent_history)
#     guess = 'P'
#     char_values = {'R': 2, 'P': 1, 'S': 0}
#     biggest_var = ''
#     Var1 = ''
#     Var2 = ''

#     # Use a default value for the first move
#     if not prev_play:
#         return guess

#     if count < 100:
#         guesslist = ['P', 'P', 'S', 'R', 'S', 'R']
#         return guesslist[count % 6]  # Use modulo to loop through guesslist

#     if count >= 100:
#         check_last_ten = opponent_history[-15:]
#         most_frequent = max(set(check_last_ten), key=check_last_ten.count)

#         if most_frequent == '':
#             most_frequent = 'R'

#         ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
#         Var1 = ideal_response[most_frequent]

#         if opponent_history[count-1] == opponent_history[count-2]:
#             predict = opponent_history[count-1]
#             Var2 = ideal_response[predict]

#     if Var1 and Var2:  # Ensure Var1 and Var2 are not empty
#         if char_values[Var1] > char_values[Var2]:
#             biggest_var = Var1
#         elif char_values[Var2] > char_values[Var1]:
#             biggest_var = Var2
#         else:
#             biggest_var = Var1  # They are equal, default to Var1
#     else:
#         biggest_var = guess  # Default if no valid Var1 or Var2

#     return biggest_var
