from string import ascii_lowercase as a_z

"""
Complexity:
  * Time: O(n**2)
  * Space: ?
"""

def is_pangram(sentence):
    for letter in a_z:
        if not letter in sentence.lower():
            return False

    return True
