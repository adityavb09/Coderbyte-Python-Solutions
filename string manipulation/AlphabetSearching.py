/****************************************************************
 *             CODERBYTE ALPHABET SEARCHING CHALLENGE           *
 *                                                              *
 * Problem Statement                                            *
 * Have the function AlphabetSearching(str) take the string     *
 * parameter being passed and return the string true if every   *
 * single letter of the English alphabet exists in the string,  *
 * otherwise return the string false.                           *
 * For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv"    *
 * then your program should return the string true because every*
 * character in the alphabet exists in this string even though  *
 * some characters appear more than once.                       *
 *                                                              *
 * Examples                                                     *
 * Input 1: abcdefghijklmnopqrstuvwxyyyy                        *
 * Output 1: false                                              *
 *                                                              *
 * Input 2: abc123456kmo                                        *
 * Output 2: false                                              *
 ***************************************************************/

import re
def AlphabetSearching(str1):
    str1=str1.lower()
    
    pattern=re.compile(r'[a-z]')
    check=pattern.findall(str1)
    str2=set(check)
    
    if len(str2)==26:
        return True
    else:
        return False
    
print(AlphabetSearching("zacxyjbbkfgtbhdaielqrm45pnsowtuv"))   
print(AlphabetSearching("abc123456kmo"))
print(AlphabetSearching("abcdefghijklmnopqrstuvwxyyyyy"))
