#!/usr/bin/env python3
import requests
import json

PRINTER="192.168.10.18"
CLUSTER_API="/cluster-api/v1/"
GRIFFIN_API="/api/v1/"

griffin_job = requests.get(f"http://{PRINTER}{GRIFFIN_API}/print_job").json()
griffin_printer = requests.get(f"http://{PRINTER}{GRIFFIN_API}/printer").json()
griffin_history = requests.get(f"http://{PRINTER}{GRIFFIN_API}/history/print_jobs").json()

cluster_printers = requests.get(f"http://{PRINTER}{CLUSTER_API}/printers/").json()
cluster_printjobs = requests.get(f"http://{PRINTER}{CLUSTER_API}/print_jobs/").json()
cluster_history = requests.get(f"http://{PRINTER}{CLUSTER_API}/print_jobs/history").json()


print(f"{PRINTER} Griffin printer state: {griffin_printer['status']}")
if "name" in griffin_job:
    print(f"{PRINTER} Griffin current job: {griffin_job['name']} - {griffin_job['state']} - {griffin_job['result']}")
else:
    job = griffin_history[0]
    print(f"{PRINTER} No running job")
    print(f"{PRINTER} Last griffin history: {job['name']} - {job['result']}")

print()

current_printer = cluster_printers[0]
current_job = cluster_printjobs[0] if cluster_printjobs else None

print(f"{PRINTER} Cluster printer status: {current_printer['status']}")

if current_job:
    print(f"{PRINTER} Cluster current job: {current_job['name']} - {current_job['status']}")
else:
    job = cluster_history[-1]
    print(f"{PRINTER} No running job")
    print(f"{PRINTER} Last cluster history: {job['name']} - {job['status']}")

