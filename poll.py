#!/usr/bin/env python3
import requests
import json
import sys

try:
    PRINTER=sys.argv[1]
except IndexError:
    PRINTER="192.168.10.18"

CLUSTER_API="/cluster-api/v1/"
GRIFFIN_API="/api/v1/"


def dump(data):
    print(json.dumps(data, indent=2))


print(f"Polling printer {PRINTER}")

opinicus_job = requests.get(f"http://{PRINTER}{GRIFFIN_API}/print_job").json()
opinicus_printer = requests.get(f"http://{PRINTER}{GRIFFIN_API}/printer").json()
opinicus_history = requests.get(f"http://{PRINTER}{GRIFFIN_API}/history/print_jobs").json()

cluster_printers = requests.get(f"http://{PRINTER}{CLUSTER_API}/printers/").json()
cluster_printjobs = requests.get(f"http://{PRINTER}{CLUSTER_API}/print_jobs/").json()
cluster_history = requests.get(f"http://{PRINTER}{CLUSTER_API}/print_jobs/history").json()


print(f"{PRINTER} Opinicus printer state: {opinicus_printer['status']}")
if "name" in opinicus_job:
    print(f"{PRINTER} Opinicus current job: {opinicus_job['name']} - {opinicus_job['state']} - {opinicus_job['result']}")
else:
    if opinicus_history:
        job = opinicus_history[0]
        print(f"{PRINTER} No opinicus running job")
        print(f"{PRINTER} Last opinicus history: {job['name']} - {job['result']}")
    else:
        print("{PRINTER} No opinicus history yet")

print()

current_printer = cluster_printers[0]
current_job = cluster_printjobs[0] if cluster_printjobs else None

print(f"{PRINTER} Cluster printer status: {current_printer['status']}")

if current_job:
    print(f"{PRINTER} Cluster current job: {current_job['name']} - {current_job['status']}")
else:
    if cluster_history:
        job = cluster_history[-1]
        print(f"{PRINTER} No running job")
        print(f"{PRINTER} Last cluster history: {job['name']} - {job['status']}")
    else:
        print(f"{PRINTER} No cluster history yet")

if current_printer['faults']:
    print(f"{PRINTER} Cluster faults:")
    for fault in current_printer['faults']:
        print(f"    - {fault['message']:60.60s}")
