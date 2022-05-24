from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem
import ontology
import metroxml


def create_and_show_menu():
    menu = ConsoleMenu("Main Menu", "Metro.owl programmatic manipulation")

    sparql_submenu = ConsoleMenu("Perform SPARQL Queries")
    reasoner_submenu = ConsoleMenu("Run Pellet Reasoner - Try viewing properties before and after running Pellet")
    owl_manipulation_submenu = ConsoleMenu("Perform OWL manipulation using Owlready2")
    list_entities_submenu = ConsoleMenu("List entities in the ontology")

    print_xml_item = FunctionItem("Display ontology XML via the DOM", metroxml.print_xml)
    transform_and_display_item = FunctionItem("Transform to HTML using XSLT, display in browser",
                                              metroxml.transform_and_display)
    print_classes_item = FunctionItem("List all classes", ontology.print_classes)
    print_individuals_item = FunctionItem("List all individuals", ontology.print_individuals)
    print_op_item = FunctionItem("List all object properties", ontology.print_object_properties)
    print_dp_item = FunctionItem("List all data properties", ontology.print_data_properties)

    print_rebibbia_props_item = FunctionItem("Show Properties for Rebibbia", ontology.show_reb_props)
    run_reasoner_item = FunctionItem("Run the pellet reasoner", ontology.run_reasoner)

    count_classes_sparql_item = FunctionItem("Count the classes", ontology.count_classes_via_sparql)
    count_op_sparql_item = FunctionItem("Count the object properties",
                                        ontology.count_object_properties_via_sparql)
    count_dp_sparql_item = FunctionItem("Count the data properties",
                                        ontology.count_data_properties_via_sparql)
    count_ni_sparql_item = FunctionItem("Count the named individuals",
                                        ontology.count_named_individuals_via_sparql)
    show_terminii_sparql_item = FunctionItem("List Terminus stations", ontology.show_terminus_stations_via_sparql)

    list_entities_submenu_item = SubmenuItem("List entities in the ontology", list_entities_submenu,
                                             menu=owl_manipulation_submenu)
    list_entities_submenu.append_item(print_classes_item)
    list_entities_submenu.append_item(print_individuals_item)
    list_entities_submenu.append_item(print_op_item)
    list_entities_submenu.append_item(print_dp_item)

    sparql_submenu_item = SubmenuItem("Perform SPARQL Queries", sparql_submenu, menu=owl_manipulation_submenu)
    sparql_submenu.append_item(count_classes_sparql_item)
    sparql_submenu.append_item(count_op_sparql_item)
    sparql_submenu.append_item(count_dp_sparql_item)
    sparql_submenu.append_item(count_ni_sparql_item)
    sparql_submenu.append_item(show_terminii_sparql_item)

    reasoner_submenu_item = SubmenuItem("Run Pellet Reasoner", reasoner_submenu, menu=owl_manipulation_submenu)
    reasoner_submenu.append_item(print_rebibbia_props_item)
    reasoner_submenu.append_item(run_reasoner_item)

    owl_submenu_item = SubmenuItem("Perform OWL manipulation using Owlready2", owl_manipulation_submenu, menu=menu)

    owl_manipulation_submenu.append_item(list_entities_submenu_item)
    owl_manipulation_submenu.append_item(sparql_submenu_item)
    owl_manipulation_submenu.append_item(reasoner_submenu_item)

    menu.append_item(print_xml_item)
    menu.append_item(transform_and_display_item)
    menu.append_item(owl_submenu_item)
    menu.show()
