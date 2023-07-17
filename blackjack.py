from p1_random import P1Random  # imports the module to invoke random numbers between a specified range


class Blackjack:  # holds the respective methods to run BlackJack

    def __init__(self):  # initializes the variables needed to run

        self.user_handcount = 0  # hand count of the inputter/user
        self.user_wins = 0  # total number of inputter/user wins
        self.dealer_handcount = 0  # hand count of the dealer
        self.dealer_wins = 0  # total number of dealer wins
        self.total_num_games = 0  # total number of games played
        self.total_ties = 0  # total number of ties
        self.menu_selection = 1  # enables program to run without an initial input of 1-4
        self.rng = P1Random()
        self.in_progress = True

    @staticmethod
    def menu_options():  # main menu of options
        print('1. Get another card')   # user's turn
        print('2. Hold hand')  # dealer's "turn"
        print('3. Print statistics')  # user wins, dealer wins, total of games, total of ties, percents
        print('4. Exit')  # exit code
        print()

    def input_validity(self):
        i_valid = True
        menu_selection = int(input('Choose an option: '))

        while i_valid:
            if menu_selection in range(1, 5):  # (1,5) - 5 not included
                self.menu_selection = menu_selection
                i_valid = False
            elif menu_selection < 1 or menu_selection > 4:  # error control for not being a valid input
                print('Invalid input!')
                print('Please enter an integer value between 1 and 4.')
                print()
                self.menu_options()
                menu_selection = int(input('Choose an option: '))

    def run_blackjack(self):
        if self.total_num_games == 0:
            print()
            print('START GAME #', self.total_num_games + 1)  # total is shown alongside
            print()
        while self.in_progress:
            if self.menu_selection == 1:  # get another card
                self.get_another_card()
                if self.in_progress:  # enables menu options and "Choose an option to show" without any continuous loop
                    self.menu_options()
                    self.input_validity()

            elif self.menu_selection == 2:  # hold hand
                self.hold_hand()
                self.menu_selection = 1  # reruns the "Card is, Hand is" statement, menu options, and "Choose an option"

            elif self.menu_selection == 3:  # print statistics
                self.blackjack_stats()
                self.menu_options()
                self.input_validity()

            elif self.menu_selection == 4:  # exit code
                exit()

    def get_another_card(self):  # main menu option 1
        num_rand = self.rng.next_int(13) + 1  # for the randomized number between 1 and 13
        print('Your card is a', self.card_amount(num_rand))  # runs to see the card amount/name of that random

        if num_rand < 11:  # regular card number from 1-10
            self.user_handcount += num_rand
            print('Your hand is:', self.user_handcount)
            print()

        elif num_rand >= 11:  # either a Jack, Queen, or King
            self.user_handcount += 10
            print('Your hand is:', self.user_handcount)
            print()

        if self.user_handcount > 21:  # dealer wins because the user has exceeded 21
            self.dealer_wins += 1  # adds to dealer wins
            self.total_num_games += 1
            self.in_progress = False  # initiates resets
            print('You exceeded 21! You lose. ')
            print()
            print('START GAME #', self.total_num_games + 1)  # total is shown alongside
            print()

        elif self.user_handcount == 21:  # user wins because the user's hand has exactly 21
            self.user_wins += 1
            self.total_num_games += 1  # adds to the total number of games played
            self.in_progress = False
            print('BLACKJACK! You win!')
            print()
            print('START GAME #', self.total_num_games + 1)  # total is shown alongside
            print()

    def hold_hand(self):  # main menu option 2
        self.dealer_handcount = self.rng.next_int(11) + 16  # for the randomized number between 16 and 26
        print()
        print('Dealer\'s hand:', self.dealer_handcount)
        print('Your hand is:', self.user_handcount)

        if self.dealer_handcount > 21:  # dealer loses because they have exceeded 21
            self.user_wins += 1
            self.total_num_games += 1
            self.in_progress = False
            print()
            print('You win!')
            print()
            print('START GAME #', self.total_num_games + 1)  # total is shown alongside
            print()

        elif self.user_handcount > self.dealer_handcount:  # in the case that neither the user/dealer reach exactly 21
            self.user_wins += 1
            self.total_num_games += 1
            self.in_progress = False
            print()
            print('You win!')
            print()
            print('START GAME #', self.total_num_games + 1)  # total is shown alongside
            print()

        elif self.dealer_handcount > self.user_handcount:  # dealer wins by higher hand
            self.dealer_wins += 1
            self.total_num_games += 1
            self.in_progress = False
            print()
            print('Dealer wins!')
            print()
            print('START GAME #', self.total_num_games + 1)  # total is shown alongside
            print()

        elif self.dealer_handcount == 21:  # dealer wins by perfect score
            self.dealer_wins += 1
            self.total_num_games += 1
            self.in_progress = False
            print()
            print('Dealer wins!')
            print()
            print('START GAME #', self.total_num_games + 1)  # total is shown alongside
            print()

        elif self.dealer_handcount == self.user_handcount:  # in the case of a tie
            self.total_ties += 1
            self.total_num_games += 1  # adds to total number of games
            self.in_progress = False
            print()
            print("It's a tie! No one wins!")
            print()
            print('START GAME #', self.total_num_games + 1)  # total is shown alongside
            print()

    @staticmethod
    def card_amount(amount):
        cards = {1: 'ACE!', 2: '2!', 3: '3!', 4: '4!', 5: '5!', 6: '6!', 7: '7!', 8: '8!', 9: '9!', 10: '10!',
                 11: 'JACK!', 12: 'QUEEN!', 13: 'KING!'}  # dictionary for each respective card and the equal amount
        if amount == 1:  # ACE
            return cards[amount]
        elif 1 < amount < 11:  # regular number between 2 and 10 (inclusive)
            return cards[amount]
        elif amount >= 11:  # either a Jack, Queen, or King
            return cards[amount]

    def blackjack_stats(self):
        print()
        print('Number of Player wins:', self.user_wins)
        print('Number of Dealer wins:', self.dealer_wins)
        print('Number of tie games:', self.total_ties)
        print('Total # of games played is:', self.total_num_games)
        print(f'Percentage of Player wins: {self.user_wins / self.total_num_games * 100} %')
        print()
        #  user wins divided by total number of games, multiplied by 100 to receive the percentage


def main():
    project = Blackjack()

    while project.in_progress:
        project.run_blackjack()
        project.user_handcount = 0  # reset
        project.dealer_handcount = 0  # reset
        project.in_progress = True  # game is on


main()  # runs Blackjack
