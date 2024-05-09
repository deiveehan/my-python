import subprocess
import csv

def fetch_pod_metrics(namespace):
    # Command to fetch pod metrics
    command = f"kubectl top pods -n {namespace}"
    try:
        # Run the command and capture the output
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Failed to fetch metrics: {e}")
        return None

def parse_metrics(output):
    lines = output.strip().split("\n")
    headers = lines[0].split()  # Should be ['NAME', 'CPU(cores)', 'MEMORY(bytes)']
    data = []
    total_cpu = 0
    total_memory = 0

    for line in lines[1:]:  # Skip header line
        parts = line.split()
        name = parts[0]
        cpu = int(parts[1].replace('m', ''))  # Convert '100m' to 100
        memory = int(parts[2].replace('Mi', ''))  # Convert '100Mi' to 100
        data.append([name, cpu, memory])
        total_cpu += cpu
        total_memory += memory

    return data, total_cpu, total_memory

def write_csv(data, total_cpu, total_memory, filename='pod_metrics.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name of the App', 'CPU in m', 'Memory in Mi'])
        writer.writerows(data)
        writer.writerow(['Total', total_cpu, total_memory])

def main():
    namespace = 'default'
    output = fetch_pod_metrics(namespace)
    if output:
        data, total_cpu, total_memory = parse_metrics(output)
        write_csv(data, total_cpu, total_memory)
        print(f"Metrics written to pod_metrics.csv with total CPU: {total_cpu}m and total Memory: {total_memory}Mi")

if __name__ == "__main__":
    main()
