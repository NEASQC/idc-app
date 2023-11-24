from flask import Flask, request
from jsonschema import validate, ValidationError
from neasqc_qrbs.knowledge_rep import *
from neasqc_qrbs.qrbs import *

app = Flask(__name__)

idc_deep_schema = {
    "type": "object",
    "properties": {
        "model": {
            "enum": ["cf", "fuzzy", "bayes"] 
        },
        "variables": {
            "type": "object",
            "properties": {
                "t0": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "t1": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "t2": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "t3": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "t4": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "t5": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n0a": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n0b": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n1a": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n1b": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n2a": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n2b": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n3a": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n3b": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "n3c": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "m0": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False },
                "m1": { "type": "number", "minimum": 0.0, "maximum": 1.0, "required": False }
            }
        }
    }
}

idc_schema = {
    "type": "object",
    "properties": {
    "model": {
        "enum": ["cf", "fuzzy", "bayes"] 
    },
    "classification": {
        "type": "object",
        "properties": {
            "tnm": {
                "enum": [
                    "t1n0m0", "t0n1m0", "t1n1m0", "t2n0m0", "t2n1m0",
                    "t3n0m0", "t0n2m0", "t1n2m0", "t3n2m0", "t3n1m0",
                    "t4n0m0", "t4n1m0", "t4n2m0", "txn3m0", "txnym1"
                ],
            },
            "value": {
                "type": "number",
                "minimum": 0.0,
                "maximum": 1.0
            }
        }
    }
    }
}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/idc")
def idc():

    def _get_value(data, tnm):
        return data['classification']['value'] if data['classification']['tnm'] == tnm else 0.0

    data = request.get_json()

    try:
        validate(data, idc_schema)
    except ValidationError as e:
        return "Invalid input data: {}".format(e.message), 400
    
    idc = QRBS()

    t1n0m0 = idc.assert_fact('T1N0M0', 'T1N0M0 classification', _get_value(data, 't1n0m0'))
    t0n1m0 = idc.assert_fact('T0N0M0', 'T0N0M0 classification', _get_value(data, 't0n1m0'))
    t1n1m0 = idc.assert_fact('T1N1M0', 'T1N1M0 classification', _get_value(data, 't1n1m0'))
    t2n0m0 = idc.assert_fact('T2N0M0', 'T2N0M0 classification', _get_value(data, 't2n0m0'))
    t2n1m0 = idc.assert_fact('T2N1M0', 'T2N1M0 classification', _get_value(data, 't2n1m0'))
    t3n0m0 = idc.assert_fact('T3N0M0', 'T3N0M0 classification', _get_value(data, 't3n0m0'))
    t0n2m0 = idc.assert_fact('T0N2M0', 'T0N2M0 classification', _get_value(data, 't0n2m0'))
    t1n2m0 = idc.assert_fact('T1N2M0', 'T1N2M0 classification', _get_value(data, 't1n2m0'))
    t3n2m0 = idc.assert_fact('T3N2M0', 'T3N2M0 classification', _get_value(data, 't3n2m0'))
    t3n1m0 = idc.assert_fact('T3N1M0', 'T3N1M0 classification', _get_value(data, 't3n1m0'))
    t4n0m0 = idc.assert_fact('T4N0M0', 'T4N0M0 classification', _get_value(data, 't4n0m0'))
    t4n1m0 = idc.assert_fact('T4N1M0', 'T4N1M0 classification', _get_value(data, 't4n1m0'))
    t4n2m0 = idc.assert_fact('T4N2M0', 'T4N2M0 classification', _get_value(data, 't4n2m0'))
    txn3m0 = idc.assert_fact('TXN3M0', 'TXN3M0 classification', _get_value(data, 'txn3m0'))
    txnym1 = idc.assert_fact('TXNYM1', 'TXNYM1 classification', _get_value(data, 'txnym1'))

    ia   = idc.assert_fact('IA', 'Stage I-A')
    ib   = idc.assert_fact('IB', 'Stage I-B')
    iia  = idc.assert_fact('IIA', 'Stage II-A')
    iib  = idc.assert_fact('IIB', 'Stage II-B')
    iiia = idc.assert_fact('IIIA', 'Stage III-A')
    iiib = idc.assert_fact('IIIB', 'Stage III-B')
    iiic = idc.assert_fact('IIIC', 'Stage III-C')
    iv   = idc.assert_fact('IV', 'Stage IV')

    rule_ia    = idc.assert_rule(t1n0m0, ia, 1.0)
    rule_ib    = idc.assert_rule(OrOperator(t0n1m0, t1n1m0), ib, 1.0)
    rule_iia   = idc.assert_rule(OrOperator(t0n1m0, OrOperator(t1n1m0, t2n0m0)), iia, 1.0)
    rule_iib   = idc.assert_rule(OrOperator(t2n1m0, t3n0m0), iib, 1.0)
    rule_iiia  = idc.assert_rule(OrOperator(t0n2m0, OrOperator(OrOperator(t1n2m0, t2n0m0), OrOperator(t3n2m0, t3n1m0))), iiia, 1.0)
    rule_iiib  = idc.assert_rule(OrOperator(t4n0m0, OrOperator(t4n1m0, t4n2m0)), iiib, 1.0)
    rule_iiic  = idc.assert_rule(txn3m0, iiic, 1.0)
    rule_iv    = idc.assert_rule(txnym1, iv, 1.0)

    staging_ia    = idc.assert_island([rule_ia])
    staging_ib    = idc.assert_island([rule_ib])
    staging_iia   = idc.assert_island([rule_iia])
    staging_iib   = idc.assert_island([rule_iib])
    staging_iiia  = idc.assert_island([rule_iiia])
    staging_iiib  = idc.assert_island([rule_iiib])
    staging_iiic  = idc.assert_island([rule_iiic])
    staging_iv    = idc.assert_island([rule_iv])

    # MyQlmQPU.MAX_ARITY = 28
    result = {}
    for staging, stage in zip(
        [staging_ia, staging_ib, staging_iia, staging_iib, staging_iiia, staging_iiib, staging_iiic, staging_iv],
        [ia, ib, iia, iib, iiia, iiib, iiic, iv]
    ):
        tag = stage.attribute.lower()
        try:
            MyQlmQPU.execute(idc, [staging], model=data['model'])
            result[tag] = stage.imprecission
        except ValueError as e:
            result[tag] = '{}'.format(e.args[0])

    return result

@app.post("/idc-deep")
def idc_deep():

    def _get_value(data, variable):
        try:
            return data['variables'][variable] 
        except:
            return 0.0
            
    
    data = request.get_json()

    try:
        validate(data, idc_schema)
    except ValidationError as e:
        return "Invalid input data: {}".format(e.message), 400
    
    idc = QRBS()

    t0 = idc.assert_fact('T0', 'No evidence of tumor', _get_value(data, 't0'))
    t1 = idc.assert_fact('T1', 'Size less than or equal to 20mm', _get_value(data, 't1'))
    t2 = idc.assert_fact('T2', 'Size between 20mm and 50mm', _get_value(data, 't2'))
    t3 = idc.assert_fact('T3', 'Size greater than 50mm', _get_value(data, 't3'))
    t4 = idc.assert_fact('T4', 'Tumor involves chest wall', _get_value(data, 't4'))
    t5 = idc.assert_fact('T5', 'Tumor affects skin', _get_value(data, 't5'))

    n0a = idc.assert_fact('N0', 'Absence of cancer in lymph nodes', _get_value(data, 'n0a'))
    n0b = idc.assert_fact('N0', 'Size in lymph nodes less than 0.2mm', _get_value(data, 'n0b'))
    n0 = OrOperator(n0a, n0b)
    n1a = idc.assert_fact('N1', 'From 1 to 3 affected axillary lymph nodes', _get_value(data, 'n1a'))
    n1b = idc.assert_fact('N1', 'Internal lymph nodes affected', _get_value(data, 'n1b'))
    n1 = OrOperator(n1a, n1b)
    n2a = idc.assert_fact('N2', 'From 4 to 9 affected axillary lymph nodes', _get_value(data, 'n2a'))
    n2b = idc.assert_fact('N2', 'No axillary lymph node involvement', _get_value(data, 'n2b'))
    n2 = OrOperator(n2a, n2b)
    n3a = idc.assert_fact('N3', 'More than 10 affected axillary lymph nodes', _get_value(data, 'n3a'))
    n3b = idc.assert_fact('N3', 'Lymph nodes below the collarbone affected', _get_value(data, 'n3b'))
    n3c = idc.assert_fact('N3', 'Superclavicular lymph nodes affected', _get_value(data, 'n3c'))
    n3 = OrOperator(n3a, OrOperator(n3b, n3c))

    m0 = idc.assert_fact('M0', 'No evidence of metastasis', _get_value(data, 'm0'))
    m1 = idc.assert_fact('M1', 'Cancer cells in other organs', _get_value(data, 'm1'))

    t1n0m0 = AndOperator(t1, AndOperator(n0, m0))    
    t0n1m0 = AndOperator(t0, AndOperator(n1, m0))
    t1n1m0 = AndOperator(t1, AndOperator(n1, m0))
    t2n0m0 = AndOperator(t2, AndOperator(n0, m0))
    t2n1m0 = AndOperator(t2, AndOperator(n1, m0))
    t3n0m0 = AndOperator(t3, AndOperator(n0, m0))
    t0n2m0 = AndOperator(t0, AndOperator(n2, m0))
    t1n2m0 = AndOperator(t1, AndOperator(n2, m0))
    t3n2m0 = AndOperator(t3, AndOperator(n2, m0))
    t3n1m0 = AndOperator(t3, AndOperator(n1, m0))
    t4n0m0 = AndOperator(t4, AndOperator(n0, m0))
    t4n1m0 = AndOperator(t4, AndOperator(n1, m0))
    t4n2m0 = AndOperator(t4, AndOperator(n2, m0))
    txn3m0 = AndOperator(n3, m0)
    txnym1 = m1

    ia   = idc.assert_fact('IA', 'Stage I-A')
    ib   = idc.assert_fact('IB', 'Stage I-B')
    iia  = idc.assert_fact('IIA', 'Stage II-A')
    iib  = idc.assert_fact('IIB', 'Stage II-B')
    iiia = idc.assert_fact('IIIA', 'Stage III-A')
    iiib = idc.assert_fact('IIIB', 'Stage III-B')
    iiic = idc.assert_fact('IIIC', 'Stage III-C')
    iv   = idc.assert_fact('IV', 'Stage IV')

    rule_ia    = idc.assert_rule(t1n0m0, ia, 1.0)
    rule_ib    = idc.assert_rule(OrOperator(t0n1m0, t1n1m0), ib, 1.0)
    rule_iia   = idc.assert_rule(OrOperator(t0n1m0, OrOperator(t1n1m0, t2n0m0)), iia, 1.0)
    rule_iib   = idc.assert_rule(OrOperator(t2n1m0, t3n0m0), iib, 1.0)
    rule_iiia  = idc.assert_rule(OrOperator(t0n2m0, OrOperator(OrOperator(t1n2m0, t2n0m0), OrOperator(t3n2m0, t3n1m0))), iiia, 1.0)
    rule_iiib  = idc.assert_rule(OrOperator(t4n0m0, OrOperator(t4n1m0, t4n2m0)), iiib, 1.0)
    rule_iiic  = idc.assert_rule(txn3m0, iiic, 1.0)
    rule_iv    = idc.assert_rule(txnym1, iv, 1.0)

    staging_ia    = idc.assert_island([rule_ia])
    staging_ib    = idc.assert_island([rule_ib])
    staging_iia   = idc.assert_island([rule_iia])
    staging_iib   = idc.assert_island([rule_iib])
    staging_iiia  = idc.assert_island([rule_iiia])
    staging_iiib  = idc.assert_island([rule_iiib])
    staging_iiic  = idc.assert_island([rule_iiic])
    staging_iv    = idc.assert_island([rule_iv])

    result = {}
    for staging, stage in zip(
        [staging_ia, staging_ib, staging_iia, staging_iib, staging_iiia, staging_iiib, staging_iiic, staging_iv],
        [ia, ib, iia, iib, iiia, iiib, iiic, iv]
    ):
        tag = stage.attribute.lower()
        try:
            MyQlmQPU.execute(idc, [staging], model=data['model'])
            result[tag] = stage.imprecission
        except ValueError as e:
            result[tag] = '{}'.format(e.args[0])

    return result
