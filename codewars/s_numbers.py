"""
In this kata, you'll be given an integer of range 0 <= x <= 99
and have to return that number spelt out in English. A few examples:
"""

def spell_out_numbers(number):
    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ["", "",'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if number < 10:
        return units[number]
    elif number < 20:
        return teens[number-10]
    elif number < 100:
        if number%10 == 0:
            return tens[number//10] 
        else:
            return tens[number//10] +" " + units[number%10]
    
print(spell_out_numbers(40))