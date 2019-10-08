import tabula
import DataUtils
from DataUtils import compute_coord_from_object as coord
from DataUtils import get_frame_by_coord as fram_cor
from   DataUtils import cpt
import ast


positions = {
    "fix_rate": {
        "start": {
            "x": cpt(14.26),
            "y": cpt(210.65)

        },
        "end": {
            "x": cpt(189),
            "y": cpt(221)
        }
    },
    "variable_rate": {
        "start": {
            "x": cpt(14.26),
            "y": cpt(132.45)

        },
        "end": {
            "x": cpt(189),
            "y": cpt(161)
        }
    },
}


print(fram_cor("triodos", "https://www.triodos.be/downloads/downloads-fr/tarifs-et-conditions/liste-tarifs-credit-hypothecaire.pdf", coord(positions, "variable_rate"), 1))

print(fram_cor("triodos", "https://www.triodos.be/downloads/downloads-fr/tarifs-et-conditions/liste-tarifs-credit-hypothecaire.pdf", coord(positions, "fix_rate"), 1))