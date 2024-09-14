import csv

def load_lookup_table(lookup_file):
    lookup_table = {}
    with open(lookup_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            port = row['dstport']
            protocol = row['protocol'].lower()  # Normalizing the protocol to lowercase
            tag = row['tag']
            lookup_table[(port, protocol)] = tag
    return lookup_table
def process_flow_log(flow_log_file, lookup_table):
    tag_counts = {}
    port_protocol_counts = {}
    untagged_count = 0

    # Mapping the protocols
    protocol_mapping = {'6': 'tcp', '17': 'udp', '1': 'icmp'}

    with open(flow_log_file, 'r') as file:
        for line in file:
            fields = line.split()
            dstport = fields[5]
            protocol_num = fields[7]
            protocol = protocol_mapping.get(protocol_num, 'unknown')

            # Lookup tag
            tag = lookup_table.get((dstport, protocol), 'Untagged')

            # Count for tag
            if tag not in tag_counts:
                tag_counts[tag] = 0
            tag_counts[tag] += 1

            # Count for port/protocol combination
            if (dstport, protocol) not in port_protocol_counts:
                port_protocol_counts[(dstport, protocol)] = 0
            port_protocol_counts[(dstport, protocol)] += 1

    return tag_counts, port_protocol_counts
def write_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, 'w') as f:
        # Write tag counts
        f.write("Tag Counts:\n")
        f.write("Tag,Count\n")
        for tag, count in tag_counts.items():
            f.write(f"{tag},{count}\n")

        # Write port/protocol combination counts
        f.write("\nPort/Protocol Combination Counts:\n")
        f.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            f.write(f"{port},{protocol},{count}\n")
def main():
    lookup_file = 'lookup.csv'  # CSV file location with lookup data
    flow_log_file = 'flow_logs.txt'  # Flow log file location
    output_file = 'output.txt'  # Output file location to write the results

    # Loading the lookup table
    lookup_table = load_lookup_table(lookup_file)

    # Processto  the flow logs and get the counts
    tag_counts, port_protocol_counts = process_flow_log(flow_log_file, lookup_table)

    # adding the output into output file
    write_output(tag_counts, port_protocol_counts, output_file)
    print("Processing complete. Results written to", output_file)

if __name__ == '__main__':
    main()
