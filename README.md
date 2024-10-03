# Nmap Output Parser

This Python script parses the output of an Nmap scan and extracts the domain name (DNS), open ports, and IP address from the report. The extracted information is then written to a CSV file for easy review and further analysis.

## Features
- Extracts IP addresses, DNS names, and open ports from Nmap output files.
- Outputs the extracted data in CSV format with columns for domain name, port, and IP address.

## Prerequisites
- Python 3.x
- Nmap tool (for generating the scan report)

## Usage

### Step 1: Run Nmap and save the output
Run an Nmap scan and save the output to a file.

```bash
nmap -Pn -sT example.com > nmap_output.txt
```

### Step 2: Parse the Nmap output
Run the script with the Nmap output file as the input and specify the output CSV file.

```bash
python nmap_parser.py <input_nmap_output_file> <output_csv_file>
```

Example:

```bash
python nmap_parser.py nmap_output.txt output.csv
```

### Example CSV Output
The resulting CSV file will contain the following columns:

| Domain Name    | Port  | IP Address  |
|----------------|-------|-------------|
| example.com    | 80    | 192.168.1.1 |
| example.com    | 443   | 192.168.1.1 |

## Script Breakdown
- **Regex patterns**:
  - `ip_pattern`: Extracts the domain name (DNS) and IP address from the Nmap report.
  - `open_port_pattern`: Extracts open TCP ports.
  
- **Main function**:
  - `parse_nmap_output(input_file, output_file)`: Reads the Nmap report, parses the necessary data, and writes it to a CSV file.

## Error Handling
The script expects exactly two arguments: the input file (Nmap output) and the output CSV file. If these are not provided, the script will display the following usage message and exit:

```bash
Usage: python nmap_parser.py <input_nmap_output_file> <output_csv_file>
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

