class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

        rem = num
        romanLetter = ""

        for i in range(3, -1, -1):
            tens = pow(10, i)
            quo = (int(rem / tens)) * tens
            rem = rem % tens
            print(quo, rem)

            if (i < 3) :
                print(quo)
                if (quo % 5*tens == 4*tens) :
                    # print("yes")
                    print("I am Bishal Sainju")
                # if (quo == 4*tens):
                #     print('yes')
                    # romanLetter += roman.



s = Solution()
s.intToRoman(3400)
# s.intToRoman(3990)