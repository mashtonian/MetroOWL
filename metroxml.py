import tempfile
import webbrowser
from time import sleep
from xml.dom import minidom

from lxml import etree as etree

from constants import SEMANTICS_COURSEWORK_OWL_FQNAME, SEMANTICS_COURSEWORK_XSLT_FQNAME
from helper import pause_for_menu


def print_xml():
    xml_dom = minidom.parse(SEMANTICS_COURSEWORK_OWL_FQNAME)
    print(xml_dom.documentElement.toprettyxml(newl=''))
    pause_for_menu()


def transform_and_display():
    xml_dom = etree.parse(SEMANTICS_COURSEWORK_OWL_FQNAME)
    xslt = etree.parse(SEMANTICS_COURSEWORK_XSLT_FQNAME)
    transform = etree.XSLT(xslt)
    html_output = transform(xml_dom)
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
        html_output.write(f.name, method="html")
        webbrowser.open(f.name, new=2)
    sleep(1)
    pause_for_menu()
