#!/usr/bin/env python3
import requests
import time

PRINTER="192.168.10.18"
CLUSTER_API="/cluster-api/v1/"
GRIFFIN_API="/api/v1/"

# cluster_response = requests.get(f"http://{PRINTER}{CLUSTER_API}")
griffin_job_state = requests.get(f"http://{PRINTER}{GRIFFIN_API}/print_job/state").json()
griffin_job_result = requests.get(f"http://{PRINTER}{GRIFFIN_API}/print_job/result").json()
griffin_printer_status = requests.get(f"http://{PRINTER}{GRIFFIN_API}/printer/status").json()

cluster_printers_status = requests.get(f"http://{PRINTER}{CLUSTER_API}/printers/").json()
cluster_printjobs_status = requests.get(f"http://{PRINTER}{CLUSTER_API}/print_jobs/").json()

print(f"{PRINTER} Griffin printer state: {griffin_printer_status}")
print(f"{PRINTER} Griffin job state: {griffin_job_state}")
print(f"{PRINTER} Griffin job result: {griffin_job_result}")

print()

current_printer = cluster_printers_status[0]
current_job = cluster_printjobs_status[0] if cluster_printjobs_status else None

print(f"{PRINTER} Cluster printer status: {current_printer['status']}")

if current_job:
    print(f"{PRINTER} Cluster job status: {current_job['status']}")
else:
    print(f"{PRINTER} No running jobs")


