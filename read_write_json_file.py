################################# APRIRE FILE, LEGGERE, SCRIVERE E SOVRASCRIVERLO###########################################
import json
with open('gl-dast-report.json', 'r') as f:
    t = f.read()
    parsed_json = json.loads(str(t))
    indent_json = json.dumps(parsed_json, indent=4, sort_keys=True)
    f.close()
with open('gl-dast-report.json', 'w+') as f:
    f.write(indent_json)
    f.close()