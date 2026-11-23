"""Public display name; binary originals and source identifiers stay intact."""
import re
NAME=re.compile(r'Магомед(?:а|у|ом|е)?\s+Керимов(?:а|у|ым|е)?',re.I)
def apply_branding(value):
    if isinstance(value,str):return NAME.sub('Kerya',value)
    if isinstance(value,list):return [apply_branding(x) for x in value]
    if isinstance(value,dict):return {k:apply_branding(v) for k,v in value.items()}
    return value
