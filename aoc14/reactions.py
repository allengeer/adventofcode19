def parse_reaction(reaction_text: str):
    [reagents, result] = reaction_text.split("=>")
    reagents = list(map(lambda x: x.strip().split(" "), reagents.split(",")))
    result = result.strip().split(" ")
    return result, reagents

def reaction_list_to_dict(reaction_list: list):
    reaction_dict = {}
    for reaction in reaction_list:
        reaction_dict[reaction.yield_elem] = reaction
    return reaction_dict

class Reaction:
    def __init__(self, reaction_string):
        result, reagents = parse_reaction(reaction_string)
        self.yield_qty = int(result[0])
        self.yield_elem = result[1]
        self.reagents = {}
        for reagent in reagents:
            self.reagents[reagent[1]] = int(reagent[0])