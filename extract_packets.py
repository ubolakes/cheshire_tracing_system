input_path = "target/sim/vsim/transcript"
output_path = "packets.txt"

# extracts packets as text
with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line.startswith("# "):
                packet = line[2:]  # removes '# '
                if len(packet) == 320 and all(c in '01' for c in packet):
                    outfile.write(packet + '\n')

# converts packet as text into binary file
with open(output_path, 'r') as f:
    binary_string = f.read().replace('\n', '').replace(' ', '')

# checks the line contains only 1s and 0s
if any(bit not in '01' for bit in binary_string):
    raise ValueError("The file contains invalid characters. Only '1' and '0' are allowed.")

# Converti la stringa binaria in dati binari
byte_array = bytearray(int(binary_string[i:i+8].ljust(8, '0'), 2) for i in range(0, len(binary_string), 8))

# Scrivi i dati binari sul file
with open("packets.bin", 'wb') as f:
    f.write(byte_array)