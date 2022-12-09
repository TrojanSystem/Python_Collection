class UptoDay8:
    @staticmethod
    def project_day_8():
        totalEven = 0
        totalOdd = 0
        for evens in range(1,101):
            if evens % 2 == 0:
                totalEven += evens

            else:

                totalOdd += evens
        print(f"Total Even {totalEven} : Total Odd {totalOdd}")
