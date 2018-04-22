# task lotto 2018-04-16
import function_lotto

play_again = 1
while play_again == 1:
    print("\nWelcome to the Lotto Game!\nThe probability of winning is 1 to 13 983 816!")
    numbers = function_lotto.welcome_menu()
    lottery_numbers = function_lotto.Lottery_numbers()
    function_lotto.draw_animation(lottery_numbers)
    hit_numbers = [i for i in numbers if i in lottery_numbers]
    function_lotto.winning_animation(hit_numbers)
    play_again = function_lotto.final_menu(hit_numbers, numbers)
print("Thanks for the game!\nSee you")




























