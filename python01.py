import math

signal_power = 8
noise_power = 4
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

print(decibels)