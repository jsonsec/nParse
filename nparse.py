import csv
import sys
import re

def parse_nmap_output(input_file, output_file):
    # Prepare data for CSV
    csv_data = []
    current_ip = None
    current_dns = None

    # Regex patterns to extract IP, DNS, and open ports
    ip_pattern = re.compile(r"Nmap scan report for (.+) \(([\d\.]+)\)")
    open_port_pattern = re.compile(r"(\d+)/tcp\s+open")

    # Read the input file line by line
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()

            # Check for IP address and DNS name line
            ip_match = ip_pattern.search(line)
            if ip_match:
                current_dns = ip_match.group(1)
                current_ip = ip_match.group(2)
            
            # Check for open port line
            port_match = open_port_pattern.search(line)
            if port_match and current_ip:
                open_port = port_match.group(1)
                csv_data.append([current_dns, open_port, current_ip])

    # Write the data to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Domain Name', 'Port', 'IP Address'])
        csv_writer.writerows(csv_data)

    print(f"CSV file '{output_file}' has been created with Domain Name, Port, and IP Address.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_nmap_output_file> <output_csv_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    parse_nmap_output(input_file_path, output_file_path)
