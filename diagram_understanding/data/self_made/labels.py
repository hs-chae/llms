class Label:
    def __init__(self, name, candidates):
        self.name = name
        self.candidates = candidates


empty_label = Label('empty_label', [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",
                                    " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",])

capitals = Label('capitals', ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
                                "Q","R","S","T","U","V","W","X","Y","Z"])

small_letters = Label('small_letters', ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
                                "q","r","s","t","u","v","w","x","y","z"])