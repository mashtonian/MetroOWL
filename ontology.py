from owlready2 import sync_reasoner_pellet, default_world, onto_path, get_ontology
from helper import pause_for_menu
from constants import SEMANTICS_COURSEWORK_OWL_FILE, SEMANTICS_COURSEWORK_PATH


def init_ontology():
    onto_path.append(SEMANTICS_COURSEWORK_PATH)
    ontology = get_ontology(SEMANTICS_COURSEWORK_OWL_FILE)
    ontology.load()
    return ontology


metro_ontology = init_ontology()


def print_entities(entities):
    for e in entities:
        print(e)
    pause_for_menu()


def print_classes():
    print_entities(metro_ontology.classes())


def print_individuals():
    print_entities(metro_ontology.individuals())


def print_object_properties():
    print_entities(metro_ontology.object_properties())


def print_data_properties():
    print_entities(metro_ontology.data_properties())


def show_reb_props():
    for p in metro_ontology.Rebibbia.get_properties():
        for value in p[metro_ontology.Rebibbia]:
            print(".%s == %s" % (p.python_name, value))
    pause_for_menu()


def run_reasoner():
    sync_reasoner_pellet(infer_property_values=True)
    pause_for_menu()


def count_entities_via_sparql(sparql):
    no_entities = default_world.sparql(sparql)
    print("Query: ")
    print(sparql)
    print()
    print("Count: ", list(no_entities)[0][0])
    pause_for_menu()


def count_classes_via_sparql():
    count_entities_via_sparql("""
SELECT (COUNT(?x) AS ?nb)
{ ?x a owl:Class . }
""")


def count_object_properties_via_sparql():
    count_entities_via_sparql("""
SELECT (COUNT(?x) AS ?nb)
{ ?x a owl:ObjectProperty . }
""")


def count_data_properties_via_sparql():
    count_entities_via_sparql("""
SELECT (COUNT(?x) AS ?nb)
{ ?x a owl:DatatypeProperty . }
""")


def count_named_individuals_via_sparql():
    count_entities_via_sparql("""
SELECT (COUNT(?x) AS ?nb)
{ ?x a owl:NamedIndividual . }
""")


def show_terminus_stations_via_sparql():
    sparql = """
PREFIX metro: <http://www.semanticweb.org/mashton/ontologies/2022/3/untitled-ontology-12#>
SELECT ?x ?y where
{ ?x metro:isTerminusOf ?y }
    """

    terminii = default_world.sparql(sparql)
    print("Query: ")
    print(sparql)
    print()
    print(list(terminii)[0])
    pause_for_menu()
