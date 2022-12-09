class UptoDay8:
    @staticmethod
    def project_day_8():
        totalEven = 0
        totalOdd = 0
        print('Which Program U want to Run')
        which = input('Type "EvenOdd", "FizzBuzz" program: ')
        if which == 'EvenOdd':
            for evens in range(1, 101):
                if evens % 2 == 0:
                    totalEven += evens

                else:

                    totalOdd += evens
            print(f"Total Even {totalEven} : Total Odd {totalOdd}")
        elif which == 'FizzBuzz':
            for evens in range(1, 101):
                if evens % 3 == 0:
                    print('Fizz')

                elif evens % 5 == 0:
                    print('Buzz')
                else:
                    print(evens)
