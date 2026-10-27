#!/usr/bin/env python3
# Sandbox inventory: one local Docker target per catalog environment.
import json, sys
groups = {"widget_qa": "qa-east", "widget_pre": "preprod-east", "widget_prd": "prod-east", "widget_chase": "preprod-chase"}
inv = {g: {"hosts": [e + "-target"]} for g, e in groups.items()}
inv["haproxy"] = {"hosts": []}
inv["_meta"] = {"hostvars": {e + "-target": {"ansible_connection": "local", "target_container": "dagly-governed-widget-" + e,
                                              "ansible_python_interpreter": "/usr/local/ansible/bin/python3"}
                             for e in groups.values()}}
print(json.dumps(inv if "--list" in sys.argv else {}))
