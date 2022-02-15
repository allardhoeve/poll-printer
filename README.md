# Poll an Ultimaker printer over LAN

```
./poll.py           # will poll 192.168.10.18
./poll.py 10.1.1.1  # will poll 10.1.1.1

watch -n 1 ./poll.py 10.10.10.10  # refresh every second
```

# Output

Will output:

1. Current opinion of Opinicus on printer state
2. Current opinion of Opinicus on print job state and result
3. If no active job: state and result of latest history item if present
4. Current opinion of Cluster on printer state
5. Current opinion of Cluster on print job state (Cluster has no notion of result)
6. Current opinion of Cluster on latest history item if present
