import subprocess
import json

url = "https://api.pipedream.com/sources/dc_2Eu7X4x/sse"
auth_header = "Authorization: Bearer 360d90f4549def76cc1e370e71832b67"

# Create a curl command that streams the SSE data and outputs it to stdout
curl_cmd = ["curl", "-s", "-N", "-H", auth_header, url]

# Start the subprocess and capture its stdout and stderr streams
proc = subprocess.Popen(curl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Read SSE data line by line from the stdout stream
for line in proc.stdout:
    # Ignore any SSE data that isn't JSON-formatted
    if line.startswith(b"data: {"):
        # Strip the "data: " prefix from the line and parse the JSON-formatted data
        event_data = json.loads(line[6:])
        # Process the event data as needed
        data = event_data
        body = data['event']['body']
        print(body)





# Print only the event data from the response body
event_data = data.decode("utf-8")
print(event_data)
