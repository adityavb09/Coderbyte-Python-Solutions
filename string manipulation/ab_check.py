/****************************************************************
 *             CODERBYTE AB CHECKS CHALLENGE                    *
 *                                                              *
 * Problem Statement                                            *
 * Have the function ABCheck(str) take the str parameter being  *
 * passed and return the string true if the characters a and b  *
 * are separated by exactly 3 places anywhere in the string at  *
 * least once (ie. "lane borrowed" would result in true because *
 * there is exactly three characters between a and b).          *
 * Otherwise return the string false.                           *
 *                                                              *
 * Examples                                                     *
 * Input 1: after badly                                         *
 * Output 1: false                                              *
 *                                                              *
 * Input 2: Laura sobs                                          *
 * Output 2: true                                               *
 *                                                              *
 ***************************************************************/

import re
def ABCheck(str1):
    pattern=re.compile(r'[a].{3}[b]')
    match=pattern.search(str1)
    
    return bool(match)
print(ABCheck("after badly"))
print(ABCheck("Laura sobs"))    
print(ABCheck("lane borrowed"))
