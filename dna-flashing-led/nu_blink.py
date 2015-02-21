import RPi.GPIO as GPIO
import time
import sys
from bio-seq import parse_FASTA

dna_file = sys.argv[1]
database = parse_FASTA(dna_file)
sequences = database.values()
dna = sequences[0]

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


pwmRed = GPIO.PWM(18, 500)
pwmGreen = GPIO.PWM(23, 500)
pwmBlue = GPIO.PWM(24, 500)

def blink(nucleotide):
	if nucleotide == 'A':
		pwmRed.start(100)
		pwmGreen.start(0)
		pwmBlue.start(100)
		print('A (purple)')
	elif nucleotide == 'T':
		pwmRed.start(0)
		pwmGreen.start(0)
		pwmBlue.start(100)
		print('T (blue)')
	elif nucleotide == 'C':
		pwmRed.start(0)
		pwmGreen.start(100)
		pwmBlue.start(0)
		print('C (green)')
	elif nucleotide == 'G':
		pwmRed.start(0)
		pwmGreen.start(100)
		pwmBlue.start(100)
		print('G (cyan)')

while True:
	for nt in dna:
		blink(nt)
		time.sleep(1.5)
