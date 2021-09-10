#!/usr/bin/env python3

import re

from lxml import etree

def tei(name):
    return "{http://www.tei-c.org/ns/1.0}" + name

def akeys(el):
    return set(el.attrib.keys())


xml_lang = "{http://www.w3.org/XML/1998/namespace}lang"

filename = "orig/tlg2022.tlg007.opp-grc1.xml"

tree = etree.parse(open(filename))

body = tree.xpath("/tei:TEI/tei:text/tei:body", namespaces={"tei": "http://www.tei-c.org/ns/1.0"})[0]

for child in body:
    if child.tag == tei("div"):

        assert akeys(child) in [{xml_lang, "n", "type"}], akeys(child)
        assert child.text.strip() == ""
        assert child.tail.strip() == ""
        assert len(child) > 0

        assert child.attrib[xml_lang] == "grc"
        assert child.attrib["type"] == "edition"
        assert child.attrib["n"] == "urn:cts:greekLit:tlg2022.tlg007.opp-grc1"

        for gchild in child:
            if gchild.tag == tei("pb"):
                assert akeys(gchild) in [{"n"}], akeys(gchild)
                assert gchild.text is None
                assert len(gchild) == 0
                pb = gchild.attrib["n"]
                # print("p", pb)
                assert gchild.tail.strip() == ""

            elif gchild.tag == tei("head"):

                assert gchild.attrib == {}
                assert gchild.text.strip()
                assert gchild.tail.strip() == ""
                assert len(gchild) == 0

                print("#", gchild.text.strip())

            elif gchild.tag == tei("div"):

                assert akeys(gchild) in [{"n", "subtype", "type"}], akeys(gchild)
                assert gchild.text.strip() == ""
                assert gchild.tail.strip() == ""
                assert len(gchild) > 0

                assert gchild.attrib["type"] == "textpart"
                assert gchild.attrib["subtype"] == "chapter"
                assert gchild.attrib["n"] in map(str, range(1, 11)), gchild.attrib["n"]
                print()
                print()
                print("## CHAPTER", gchild.attrib["n"])
                print()

                for ggchild in gchild:
                    if ggchild.tag == tei("lb"):
                        assert akeys(ggchild) in [{"n"}], akeys(ggchild)
                        assert ggchild.text is None
                        assert len(ggchild) == 0
                        assert ggchild.tail.strip() == ""
                    elif ggchild.tag == tei("note"):
                        pass  # @@@
                    elif ggchild.tag == tei("pb"):
                        assert akeys(ggchild) in [{"n"}], akeys(ggchild)
                        assert ggchild.text is None
                        assert len(ggchild) == 0
                        pb = ggchild.attrib["n"]
                        # print("p", pb)
                        assert ggchild.tail.strip() == ""
                    elif ggchild.tag == tei("p"):
                        assert ggchild.attrib == {}
                        print(ggchild.text.strip())
                        assert ggchild.tail is None or ggchild.tail.strip() == ""

                        for g3child in ggchild:
                            if g3child.tag == tei("lb"):
                                assert akeys(g3child) in [{"n"}], akeys(g3child)
                                assert g3child.text is None
                                assert len(g3child) == 0
                                assert g3child.tail
                                print(g3child.tail.strip())
                            elif g3child.tag == tei("note"):
                                pass  # @@@
                            elif g3child.tag == tei("pb"):
                                assert akeys(g3child) in [{"n"}], akeys(g3child)
                                assert g3child.text is None
                                assert len(g3child) == 0
                                pb = g3child.attrib["n"]
                                # print("p", pb)
                                assert g3child.tail
                                print(g3child.tail.strip())
                            # elif g3child.tag == tei("said"):

        #                         print()
        #                         assert akeys(g3child) in [{"who"}, {"rend", "who"}], akeys(g3child)
        #                         assert g3child.text is None
        #                         assert g3child.tail is None
        #                         assert len(g3child) > 0

        #                         assert g3child.attrib["who"] in ["#Εὐθύφρων", "#Σωκράτης"]
        #                         assert g3child.attrib.get("rend") in [None, "merge"]

        #                         for g4child in g3child:
        #                             if g4child.tag == tei("label"):

        #                                 assert g4child.attrib == {}
        #                                 assert g4child.text.strip()
        #                                 assert g4child.tail.strip()
        #                                 assert len(g4child) == 0

        #                                 print(g4child.text.strip(), end=" ")
        #                                 print(g4child.tail.strip(), end=" ")

        #                             elif g4child.tag == tei("milestone"):

        #                                 assert akeys(g4child) in [{"resp", "n", "unit"}], akeys(g4child)
        #                                 assert g4child.text is None
        #                                 assert g4child.tail is None or g4child.tail.strip()
        #                                 assert len(g4child) == 0

        #                                 assert g4child.attrib["resp"] == "Stephanus"
        #                                 assert g4child.attrib["unit"] in ["page", "section"]
        #                                 if g4child.attrib["unit"] == "page":
        #                                     assert g4child.attrib["n"] in map(str, range(2, 17))
        #                                 else:
        #                                     assert re.match("\d{1,2}[a-e]",g4child.attrib["n"])
        #                                     print("{" + g4child.attrib["n"] + "}", end=" ")

        #                                 if g4child.tail:
        #                                     print(g4child.tail.strip(), end=" ")

        #                             elif g4child.tag == tei("del"):

        #                                 assert g4child.attrib == {}
        #                                 assert g4child.text.strip()
        #                                 assert g4child.tail.strip()
        #                                 assert len(g4child) == 0

        #                                 print("[" + g4child.text.strip() + "]", end=" ")
        #                                 print(g4child.tail.strip(), end=" ")

        #                             elif g4child.tag == tei("q"):

        #                                 print("{q}", end=" ")
        #                                 assert g4child.attrib == {}
        #                                 assert g4child.text.strip()
        #                                 assert g4child.tail.strip()

        #                                 print(g4child.text.strip(), end=" {/q} ")

        #                                 for g5child in g4child:
        #                                     if g5child.tag == tei("milestone"):

        #                                         assert akeys(g5child) in [{"resp", "n", "unit"}], akeys(g5child)
        #                                         assert g5child.text is None
        #                                         assert g5child.tail.strip()
        #                                         assert len(g5child) == 0

        #                                         assert g5child.attrib["resp"] == "Stephanus"
        #                                         assert g5child.attrib["unit"] in ["section"]
        #                                         assert re.match("\d{1,2}[a-e]",g5child.attrib["n"])

        #                                         print("{" + g5child.attrib["n"] + "}", end=" ")

        #                                         print(g5child.tail.strip(), end=" ")

        #                                     elif g5child.tag == tei("del"):

        #                                         assert g5child.attrib == {}
        #                                         assert g5child.text.strip()
        #                                         assert g5child.tail.strip()
        #                                         assert len(g5child) == 0

        #                                         print("[" + g5child.text.strip() + "]", end=" ")
        #                                         print(g5child.tail.strip(), end=" ")

        #                                     else:
        #                                         print(g5child.tag)

        #                                 print(g4child.tail.strip(), end=" ")

        #                             elif g4child.tag == tei("quote"):

        #                                 print("{start-quote}", end=" ")

        #                                 assert akeys(g4child) in [{"type"}], akeys(g4child)
        #                                 assert g4child.text is None
        #                                 assert g4child.tail.strip() == ""
        #                                 assert len(g4child) > 0

        #                                 assert g4child.attrib["type"] == "verse"

        #                                 for g5child in g4child:
        #                                     if g5child.tag == tei("l"):

        #                                         assert akeys(g5child) in [{"met"}], akeys(g5child)
        #                                         assert g5child.text.strip()
        #                                         assert g5child.tail is None
        #                                         assert len(g5child) > 0

        #                                         assert g5child.attrib["met"] in ["dactylic"]

        #                                         print(g5child.text, end=" ")

        #                                         for g6child in g5child:
        #                                             if g6child.tag == tei("del"):

        #                                                 assert g6child.attrib == {}
        #                                                 assert g6child.text.strip()
        #                                                 assert g6child.tail.strip()
        #                                                 assert len(g6child) == 0

        #                                                 print("[" + g6child.text.strip() + "]", end=" ")
        #                                                 print(g6child.tail.strip(), end=" ")

        #                                             else:
        #                                                 print(g6child.tag)
        #                                     else:
        #                                         print(g5child.tag)

        #                                 print("{end-quote}", end=" ")
        #                             elif g4child.tag == tei("cit"):

        #                                 # print("@CIT", end=" ")

        #                                 assert g4child.attrib == {}
        #                                 assert g4child.text is None
        #                                 assert g4child.tail.strip()
        #                                 assert len(g4child) > 0

        #                                 for g5child in g4child:
        #                                     if g5child.tag == tei("quote"):

        #                                         print()
        #                                         print("{start-quote}", end=" ")

        #                                         assert akeys(g5child) in [{"type"}], akeys(g5child)
        #                                         assert g5child.text is None
        #                                         assert g5child.tail is None
        #                                         assert len(g5child) > 0

        #                                         assert g5child.attrib["type"] == "verse"

        #                                         for g6child in g5child:
        #                                             if g6child.tag == tei("l"):

        #                                                 assert akeys(g6child) in [{"met"}], akeys(g6child)
        #                                                 assert g6child.text.strip()
        #                                                 assert g6child.tail is None
        #                                                 assert len(g6child) == 0

        #                                                 assert g6child.attrib["met"] in ["c"]

        #                                                 print(g6child.text, end=" ")

        #                                             else:
        #                                                 print(g6child.tag)

        #                                         print("{end-quote}")

        #                                     elif g5child.tag == tei("bibl"):

        #                                         assert g5child.attrib == {}
        #                                         assert g5child.text.strip()
        #                                         assert g5child.tail is None
        #                                         assert len(g5child) == 0

        #                                         # print(g5child.text.strip())
        #                                     else:
        #                                         print(g5child.tag)

        #                                 print(g4child.tail.strip(), end=" ")

        #                             else:
        #                                 print(g4child.tag)
                            else:
                                print(g3child.tag)
                                quit()
                    else:
                        print(ggchild.tag)
                        quit()
            else:
                print(gchild.tag)
                quit()
    else:
        print(child.tag)
        quit()
