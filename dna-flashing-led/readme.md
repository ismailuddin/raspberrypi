#DNA flashing LED box
This code accompanies the 'DNA flashing LED box' project over at scienceexposure.com. Two scripts are provided:
* FASTA file parser
* LED flashing script

The first file acts as a module, and parses FASTA files by extracting their DNA sequences alongside their ID into a dictionary. Use the `.keys()` function to extract the IDs of the sequences, and the `.values()` function to extract the sequences. These functions maybe applied directly to the dictionary that is returned by running the method `parse_FASTA(filename)` where 'filename' is the full name of the .FASTA file including extension.


### Recommended requirements
* Python 2.7.6 or newer
* Raspberry Pi (any model) with Python GPIO library installed
* Electrical components (LED, 3x 470 Ω resistor, jumper wires). See article page for more details.

### How to run the script
Simply launch from the terminal in RPi using command `sudo python nu_blink.py f`. Argument `f` is replaced with the full name of the .FASTA formatted file including extension. An example .FASTA file is provided, tilted `RTT103.fasta`.


©2015, Ismail Uddin & Science Exposure. www.scienceexposure.com
Link to project: http://www.scienceexposure.com/raspberry-pi/dna-flashing-led-box-raspberry-pi/
