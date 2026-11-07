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