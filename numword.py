"""Convert an integer number to the word representation.

We should handle zero:

    >>> num_word(0)
    'zero'

And numbers under a thousand:

    >>> num_word(2)
    'two'

    >>> num_word(-2)
    'negative two'

    >>> num_word(11)
    'eleven'

    >>> num_word(20)
    'twenty'

    >>> num_word(100)
    'one hundred'

    >>> num_word(121)
    'one hundred twenty one'

And numbers over a thousand:

    >>> num_word(1256)
    'one thousand two hundred fifty six'

    >>> num_word(100001)
    'one hundred thousand one'

    >>> num_word(1000000)
    'one million'

And all numbers ranging from -999,999,999,999 to 999,999,999,999 (you
can stop there):

    >>> num_word(-1234567890)  # doctest:+NORMALIZE_WHITESPACE
    'negative one billion two hundred thirty four million
    five hundred sixty seven thousand eight hundred ninety'

    >>> num_word(999999999999)  # doctest:+NORMALIZE_WHITESPACE
    'nine hundred ninety nine billion nine hundred ninety nine million
    nine hundred ninety nine thousand nine hundred ninety nine'

"""

def hundred_convert(num):
    num_str = ''
    single_dig = ['zero', 'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine']
    double_dig = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
    'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'nineteen']
    if num == 0:
        return
    if num >= 100:
        num_str += single_dig[int(num / 100)] + ' hundred'
        string = str(num)
        #reset num to include the numbers after hundred
        num = int(string[1:])
    if num == 0:
        return num_str   
    if num > 10:
        if num_str is not '':
            num_str += ' '
        if num < 20:
            num_str += teens[int(num - 11)]
            return num_str 
        else:
            num_str += double_dig[int(num / 10)] 
        string = str(num)
        #reset num to include the numbers after hundred
        num = int(string[1:])
    if num > 0:
        if num_str is not '':
            num_str += ' '
        num_str += single_dig[int(num)]
    
    return num_str


def num_word(num):
    """Convert word to number."""
    # negative first
    # start at billion
    if num == 0:
        return 'zero'
    num_str = ''
    if num < 0:
        num_str += 'negative'
    #now convert num to absolute vaule
    adj_num = abs(num)

    if adj_num >= 1000000000:
        if num_str != '':
            num_str += ' '
        num_str += hundred_convert(int(adj_num/1000000000)) + ' billion'
        
        string = str(adj_num)
        bil_len = len(string) - 9

        #reset num to include the numbers after bil
        adj_num = int(string[bil_len:])
    if adj_num >= 1000000:
        if num_str != '':
            num_str += ' '
        num_str += hundred_convert(int(adj_num/1000000)) + ' million'
        
        string = str(adj_num)
        mil_len = len(string) - 6
        adj_num = int(string[mil_len:])
    if adj_num >= 1000:
        if num_str != '':
            num_str += ' '
        num_str += hundred_convert(int(adj_num/1000)) + ' thousand'
        
        string = str(adj_num)
        thou_len = len(string) - 3
        adj_num = int(string[thou_len:])
    if adj_num < 1000:
        if adj_num == 0:
            return num_str
        if num_str != '':
            num_str += ' '
        num_str += hundred_convert(adj_num)
    
    return num_str

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT JOB!\n")
