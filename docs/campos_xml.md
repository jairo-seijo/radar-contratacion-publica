# Campos del XML

- Fichero de ejemplo: licitacionesPerfilesContratanteCompleto3_20261001_201704_1.atom
- Entradas en el fichero: 499


## Numero de expediente

- Ruta: `entry/cac-place-ext:ContractFolderStatus/cbc:ContractFolderID`
- Ejemplo: 117/2026

## Objeto del contrato

- Ruta: `entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cbc:Name`
- Ejemplo: Contratación de una asistencia técnica que...

## Importe

- Ruta: `entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:BudgetAmount/cbc:TaxExclusiveAmount`
- Ejemplo: 157500
- Nota: uso el importe sin IVA porque el IVA varía según el contrato y así los importes son comparables. También existen TotalAmount (con IVA) y EstimatedOverallContractAmount (valor estimado), que usaré en el nivel 5.

## Código CPV

- Ruta: `entry/cac-place-ext:ContractFolderStatus/cac:ProcurementProject/cac:RequiredCommodityClassification/cbc:ItemClassificationCode`
- Ejemplo: 72600000
- Nota: puede haber más de un CPV por licitación (1642 en 499 entradas). En el nivel 1 me quedo con el primero.

## Órgano de contratación

- Ruta: `entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyName/cbc:Name`
- Ejemplo: Consejo de Administración de ICEX España Exportación e Inversiones, E.P.E.
- NIF: `entry/cac-place-ext:ContractFolderStatus/cac-place-ext:LocatedContractingParty/cac:Party/cac:PartyIdentification/cbc:ID` (el que tiene `schemeName="NIF"`). Ejemplo: Q2891001F
- Nota: uso PartyName porque es el nombre oficial del organismo (Contact puede ser una persona o departamento). El NIF funciona como clave primaria: identifica al órgano aunque el nombre se escriba distinto.

## Adjudicatario

- Ruta: `entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cac:WinningParty/cac:PartyName/cbc:Name`
- Ejemplo: CAJA RURAL DE SORIA S.C.C.
- NIF: `entry/cac-place-ext:ContractFolderStatus/cac:TenderResult/cac:WinningParty/cac:PartyIdentification/cbc:ID`. Ejemplo: F42001255
- Nota: solo existe en licitaciones adjudicadas (estado ADJ o RES). En las publicadas (PUB) no aparece.

## Id de la entrada

- Ruta: `entry/id`
- Ejemplo: https://contrataciondelestado.es/sindicacion/licitacionesPerfilContratante/20497159

## Fecha de actualización

- Ruta: `entry/updated`
- Ejemplo: 2026-10-01T12:56:14.120+02:00