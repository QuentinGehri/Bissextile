'''The starting files are unrelated to the exercise.

They simply show syntax for writing and testing
  o) a global function
  o) an instance method
Pick the style that best fits the exercise.
Then delete the other one, along with this comment!
'''
class Bissextile:

    def est_bissextile(self, annee):
        if annee % 4 == 0 and ((annee % 100 != 0) or (annee % 400 == 0)):
            return True
        return False



    def affiche_result(self, annee):
        result = Bissextile().est_bissextile(annee)
        phrase = 'l\'année est'
        if result == False:
            phrase += ' pas'
        phrase += ' bissextile'
        return phrase
