# Convert a non-negative integer num to its English words representation.



class Solution:
    def numberToWords(self, num: int) -> str:
        ones = { 1:"One", 2:"Two" , 3:"Three" , 4:"Four" , 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 0:""}

        teen = {11: "Eleven" , 12:"Twelve" , 13:"Thirteen" , 14:"Fourteen" , 15:"Fifteen" ,16:"Sixteen", 17:"Seventeen" , 18:"Eighteen", 19:"Nineteen"}

        tens = { 1:"Ten", 2:"Twenty" , 3:"Thirty" , 4:"Forty" , 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety", 0:""}


        def process_three(num):
            first_digit, second_digit, third_digit = 0,0,0 
            third_digit = num//100
            first_digit= num%10
            num=num//10
            second_digit = num%10

            if first_digit and second_digit and third_digit: #111
                
                x = ""
                x+= ones[third_digit]
                x+= " Hundred"
                if second_digit == 1 :
                    x+= " "
                    a = int(second_digit)*10+int(first_digit)
                    x+= teen[a]
                    return x
                
                else:
                    x+= " "
                    x+= tens[second_digit]
                    x+= " "
                    x+= ones[first_digit]
                    return x 

            if not first_digit and second_digit and not third_digit: #010
                x = tens[second_digit]
                return x

            if not first_digit and second_digit and third_digit: #110
                x = ""
                x+= ones[third_digit]
                x+= " Hundred "
                x+= tens[second_digit]
                
                return x 
            
            if not first_digit and not second_digit and third_digit: #100
                x = ""
                x+= ones[third_digit]
                x+= " Hundred"
                
                return x
            
            if first_digit and not second_digit and third_digit: #101
                x = ""
                x+= ones[third_digit]
                x+= " Hundred "
                x+= ones[first_digit]
                
                return x
            
            if first_digit and second_digit and not third_digit: #011
                if second_digit == 1 :
                    x = int(second_digit)*10+int(first_digit)
                    return teen[x]
                
                else:
                    x = "" 
                    x+= tens[second_digit]
                    x+= " "
                    x+= ones[first_digit]
                    return x 

            if first_digit and not second_digit and not third_digit: #001
                return ones[first_digit]

            if not first_digit and not second_digit and not third_digit: #000
                return ""

        if not num:
            return "Zero"
        
        num = str(num)
        if len(num) < 4: 
            res= process_three(int(num))
        
        else:
            if len(num)<7:
                hundreds = process_three(int(num[len(num)-3:len(num)]))
                thousands = process_three(int(num[0:len(num)-3]))
                res = ""
                if thousands:
                    res= thousands +" Thousand "+ hundreds
                else:
                    res = hundreds 

            elif len(num)<10:
                res=  ""
                hundreds = process_three(int(num[len(num)-3:len(num)]))
                thousands =  process_three(int(num[len(num)-6:len(num)-3]))
                millions =  process_three(int(num[0:len(num)-6]))
                
                res+= (millions+" Million ") if millions else "" 
                res+=  (thousands+ " Thousand ") if thousands else ""
                res+= hundreds

            else:

                res = ""
                hundreds = process_three(int(num[len(num)-3:len(num)])) 
                thousands = process_three(int(num[len(num)-6:len(num)-3])) 
                millions = process_three(int(num[len(num)-9:len(num)-6])) 
                billions = process_three(int(num[0:len(num)-9]))
                
                res += (billions+ " Billion ") if billions else "" 
                res+= (millions+" Million ") if millions else "" 
                res+=  (thousands+" Thousand ") if thousands else ""
                res+= hundreds
                
            
        return res.strip()

# sol = Solution()
# print(sol.numberToWords(101))