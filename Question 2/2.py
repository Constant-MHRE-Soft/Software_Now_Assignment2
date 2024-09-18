def separate_and_convert(s):
    if len ( s ) < 16:
        return "String too short!"

    digits = ''.join ( [char for char in s if char.isdigit ()] )
    letters = ''.join ( [char for char in s if char.isalpha ()] )

    result_digits = ''.join ( [chr ( int ( digits[i] ) + 48 ) for i in range ( len ( digits ) ) if
                               int ( digits[i] ) % 2 == 0] )

    result_letters = [ord ( char ) for char in letters if char.isupper ()]

    return result_digits, result_letters
example_string = "56aWlg19845ktr235702avmH155s785fS31D0e"
converted = separate_and_convert ( example_string )
print ( "Converted numbers to ASCII:", converted[0] )
print ( "ASCII values of upper-case letters:", converted[1] )
