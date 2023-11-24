# NEASQC IDC application
This is the repository for the Invasive Ductal Carcinoma (IDC) staging application of NEASQC project (WP6).

## Licence
The `LICENCE` file contains the default licence statement as specified in the proposal and partner agreement.

## Running
This application is implemented in Flask, so to run it, clone the repository and run the command:

```
flask --app idc
```

By default, the app will be available at `http://localhost:5000`

## Specification
This application provides two API endpoints for IDC staging:

### /idc

`POST http://YOUR_URL:PORT/idc`

JSON Schema

```
{
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
```

### /idc-deep

`POST http://YOUR_URL:PORT/idc-deep`

JSON Schema

```
{
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
```

