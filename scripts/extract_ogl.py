#!/usr/bin/env python3

from unicodedata import normalize

from lxml import etree

def tei(name):
    return "{http://www.tei-c.org/ns/1.0}" + name

def akeys(el):
    return set(el.attrib.keys())


xml_lang = "{http://www.w3.org/XML/1998/namespace}lang"

filenames = [
    ("orig/tlg2022.tlg007.opp-grc1.xml", "text/orat27.txt"),
    ("orig/tlg2022.tlg008.opp-grc1.xml", "text/orat28.txt"),
    ("orig/tlg2022.tlg009.opp-grc1.xml", "text/orat29.txt"),
    ("orig/tlg2022.tlg010.opp-grc1.xml", "text/orat30.txt"),
    ("orig/tlg2022.tlg011.opp-grc1.xml", "text/orat31.txt"),
]

for fin, fout in filenames:

    with open(fout, "w") as g:
        tree = etree.parse(open(fin))

        body = tree.xpath("/tei:TEI/tei:text/tei:body", namespaces={"tei": "http://www.tei-c.org/ns/1.0"})[0]

        for child in body:
            if child.tag == tei("div"):

                assert akeys(child) in [{xml_lang, "n", "type"}], akeys(child)
                assert child.text.strip() == ""
                assert child.tail.strip() == ""
                assert len(child) > 0

                assert child.attrib[xml_lang] == "grc"
                assert child.attrib["type"] == "edition"
                assert child.attrib["n"] == f"urn:cts:greekLit:tlg2022.tlg{fin[16:19]}.opp-grc1"

                for gchild in child:
                    if gchild.tag == tei("pb"):
                        assert akeys(gchild) in [{"n"}], akeys(gchild)
                        assert gchild.text is None
                        assert len(gchild) == 0
                        pb = gchild.attrib["n"]
                        assert gchild.tail.strip() == ""

                    elif gchild.tag == tei("head"):

                        assert gchild.attrib == {}
                        assert gchild.text.strip()
                        assert gchild.tail.strip() == ""
                        assert len(gchild) == 0

                        print("#", normalize("NFC", gchild.text.strip()), file=g)

                    elif gchild.tag == tei("div"):

                        assert akeys(gchild) in [{"n", "subtype", "type"}], akeys(gchild)
                        assert gchild.text is None or gchild.text.strip() == ""
                        assert gchild.tail.strip() == ""
                        assert len(gchild) > 0

                        assert gchild.attrib["type"] == "textpart"
                        assert gchild.attrib["subtype"] == "chapter"
                        print(file=g)
                        print(file=g)
                        print("## CHAPTER", normalize("NFC", gchild.attrib["n"]), file=g)
                        print(file=g)

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
                                assert ggchild.tail.strip() == ""
                            elif ggchild.tag == tei("p"):
                                assert ggchild.attrib == {}
                                if ggchild.text.strip():
                                    print(normalize("NFC", ggchild.text.strip()), file=g)
                                assert ggchild.tail is None or ggchild.tail.strip() == ""

                                for g3child in ggchild:
                                    if g3child.tag == tei("lb"):
                                        assert akeys(g3child) in [{"n"}], akeys(g3child)
                                        assert g3child.text is None
                                        assert len(g3child) == 0
                                        assert g3child.tail
                                        if g3child.tail.strip():
                                            print(normalize("NFC", g3child.tail.strip()), file=g)
                                    elif g3child.tag == tei("note"):
                                        pass  # @@@
                                    elif g3child.tag == tei("pb"):
                                        assert akeys(g3child) in [{"n"}], akeys(g3child)
                                        assert g3child.text is None
                                        assert len(g3child) == 0
                                        pb = g3child.attrib["n"]
                                        assert g3child.tail
                                        if g3child.tail.strip():
                                            print(normalize("NFC", g3child.tail.strip()), file=g)
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
