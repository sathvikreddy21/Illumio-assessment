# Illumio-assessment
This program parses flow log data and maps each row to a tag based on a lookup table. The flow logs are in version 2 format and contain transaction details such as destination port, protocol, and transaction type.The lookup table defines a mapping between destination ports, protocols, and tags, allowing the program to classify each transaction with the appropriate tag. If a tag is not found in the lookup table for a specific port/protocol combination, the transaction is marked as "Untagged."

The program outputs two key reports:

    Tag Counts: A count of matches for each tag found in the lookup table.
    Port/Protocol Combination Counts: A count of matches for each port/protocol combination in the flow log.

## Assumptions:

The program only supports flow logs in version 2 format, as specified in the provided example,
The supported protocols are tcp, udp, and icmp, represented by protocol numbers 6, 17, and 1, respectively.
The lookup table must be a CSV file with three columns: dstport, protocol, and tag.
If a port and protocol combination is not found in the lookup table, the transaction is marked as Untagged.

## Installation

To use this program, ensure you have Python installed on your system. The program does not require any non-default Python libraries.
Usage

**python setup** : [https://docs.python.org/3/using/index.html] 

    Clone the repository or download the Python file.
    Prepare Input Files:
        A flow log file (e.g., flow_log.txt) containing flow log data.
        A lookup table file (e.g., lookup.csv) in CSV format.

## Run the Program:
**python flow_log_parser.py flow_log_file lookup_table_file output_file**

Example:  

    python flow_log_parser.py flow_logs.txt lookup.csv output.csv

**flow_log_file:** Path to the flow log file (e.g., flow_log.txt).

**lookup_table_file:** Path to the lookup table CSV file (e.g., lookup.csv).

**output_file:** Path where the output CSV file will be saved (e.g., output.csv)

## View Output:
The output file contains two sections:

**Tag Counts:** A count of matches for each tag found in the lookup table.

**Port/Protocol Combination Counts:** A count of matches for each port/protocol combination found in the flow log.
## Testing

Tests were done using:
    A sample lookup table (lookup.csv) containing multiple port and protocol mappings.
    A sample flow log (flow_log.txt) that includes a variety of valid and invalid rows.

## Conclusion

The program is designed to be run on any local machine with Python installed, and it does not require any additional dependencies or setup. The logic is straightforward, and the user can easily upload their flow log and lookup table to generate the desired reports.
