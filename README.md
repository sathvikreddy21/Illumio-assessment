# Illumio-assessment
This program parses flow log data and maps each row to a tag based on a lookup table. The flow logs are in version 2 format and contain transaction details such as destination port, protocol, and transaction type.The lookup table defines a mapping between destination ports, protocols, and tags, allowing the program to classify each transaction with the appropriate tag. If a tag is not found in the lookup table for a specific port/protocol combination, the transaction is marked as "Untagged."

The program outputs two key reports:

    Tag Counts: A count of matches for each tag found in the lookup table.
    Port/Protocol Combination Counts: A count of matches for each port/protocol combination in the flow log.

ASSUMPTIONS:
The program only supports flow logs in version 2 format, as specified in the provided example,
The supported protocols are tcp, udp, and icmp, represented by protocol numbers 6, 17, and 1, respectively.
The lookup table must be a CSV file with three columns: dstport, protocol, and tag.
If a port and protocol combination is not found in the lookup table, the transaction is marked as Untagged.

INSTALLATION
To use this program, ensure you have Python installed on your system. The program does not require any non-default Python libraries.
Usage

    Clone the repository or download the Python file.

    Prepare Input Files:
        A flow log file (e.g., flow_log.txt) containing flow log data.
        A lookup table file (e.g., lookup.csv) in CSV format.

    Run the Program:
    python transaction_processor.py flow_log_file lookup_table_file output_file

    EX: python transaction_processor.py flow_log.txt lookup.csv output.csv
    
