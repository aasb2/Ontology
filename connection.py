from owlready2 import *

onto_path.append("./Ontologies")
onto = get_ontology("PC.owx")
onto.load()
print(list(onto.classes()))
print(onto.Fonte)