import pandas as pd
from lxml import etree

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "cbc": "urn:dgpe:names:draft:codice:schema:xsd:CommonBasicComponents-2",
    "cac": "urn:dgpe:names:draft:codice:schema:xsd:CommonAggregateComponents-2",
    "cac-place-ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonAggregateComponents-2",
    "cbc-place-ext": "urn:dgpe:names:draft:codice-place-ext:schema:xsd:CommonBasicComponents-2",
}

PARSER_SEGURO = etree.XMLParser(resolve_entities=False, no_network=True)


def leer_fichero(ruta):
    arbol = etree.parse(ruta, PARSER_SEGURO)
    raiz = arbol.getroot()
    entradas = raiz.findall("atom:entry", NS)
    licitaciones = []
    for entrada in entradas:
        licitacion = {
            "expediente": entrada.findtext(
                "cac-place-ext:ContractFolderStatus/cbc:ContractFolderID", namespaces=NS
            ),
            "objeto_del_contrato": entrada.findtext(
                "cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:Name",
                namespaces=NS,
            ),
            "importe": entrada.findtext(
                "cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:BudgetAmount/cbc:TaxExclusiveAmount",
                namespaces=NS,
            ),
            "codigo_cpv": entrada.findtext(
                "cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode",
                namespaces=NS,
            ),
            "organo_de_contratacion": entrada.findtext(
                "cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyName/cbc:Name",
                namespaces=NS,
            ),
            "adjudicatario": entrada.findtext(
                "cac-place-ext:ContractFolderStatus/cac:TenderResult/cac:WinningParty/cac:PartyName/cbc:Name",
                namespaces=NS,
            ),
            "estado": entrada.findtext(
                "cac-place-ext:ContractFolderStatus/cbc-place-ext:ContractFolderStatusCode",
                namespaces=NS,
            ),
            "resultado": entrada.findtext(
                "cac-place-ext:ContractFolderStatus/cac:TenderResult/cbc:ResultCode",
                namespaces=NS,
            ),
        }
        licitaciones.append(licitacion)
    return licitaciones


def guardar_csv(licitaciones, ruta):
    df = pd.DataFrame(licitaciones)
    df.to_csv(ruta, index=False)



