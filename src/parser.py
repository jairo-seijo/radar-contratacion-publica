from lxml import etree

NS ={ 
    "atom": "http://www.w3.org/2005/Atom",
}

ruta = "data/raw/202610/licitacionesPerfilesContratanteCompleto3_20261001_201704_1.atom"
arbol = etree.parse(ruta)
raiz = arbol.getroot()

print(raiz.tag)

entradas = raiz.findall("atom:entry", NS)

print(len(entradas))