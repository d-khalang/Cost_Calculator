# Cost_Calculator
Small program to read expenses from a text file and counting all costs

I know it is not very tidy but this is working for me right now. I might clean it up a bit in the future.

Step by step going through its functionality:
Program 1. Opens the ".txt" file.
2. Read and check it line by line.
3. It omits every line that does not have ":" (Because I used ":" sign to show the amount of the expense).
4. If after ":" there is only a number(float), it makes it count.
5. If there is more than 1 number plus "+", it considers all the numbers and adds them to all the previous expenses
6. For all the money I have taken from others, as a refund for what I spent on them. I started the line with "refund ...". Therefore, those lines are subtracted from the expenses.

So, all the costs that obey these a few small rules, will have been taken care of.

For me, there were just 2, or 3 lines breaking these rules. Which were for other accounts or in another language.
Regarding these unknown lines, the program will show them as exceptions so that we can count manually if they are costs with unusual styles.

In the end, every expense is shown in detail and eventually, the final number is the sum of expenditures.