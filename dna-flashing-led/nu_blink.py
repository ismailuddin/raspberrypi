import RPi.GPIO as GPIO
import time
import sys
from bioseq import parse_FASTA

dna_file = sys.argv[1]
database = parse_FASTA(dna_file)
sequences = database.values()
dna = sequences[0]

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


red = GPIO.PWM(18, 500)
green = GPIO.PWM(23, 500)
blue = GPIO.PWM(24, 500)

def blink(nucleotide):
	if nucleotide == 'A':
		red.start(100)
		green.start(0)
		blue.start(100)
		print('A (purple)')
	elif nucleotide == 'T':
		red.start(0)
		green.start(0)
		blue.start(100)
		print('T (blue)')
	elif nucleotide == 'C':
		red.start(0)
		green.start(100)
		blue.start(0);
		print('C (green)')
	elif nucleotide == 'G':
		red.start(0)
		green.start(100)
		blue.start(100)
		print('G (cyan)')

while True:
	for nt in dna:
		blink(nt)
		time.sleep(1.5)
