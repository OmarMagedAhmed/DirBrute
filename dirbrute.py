# DirBrute - simple directory brute-forcer
# Notes: For authorized testing only. Do not use against systems you don't own or have permission to test.

import requests

target_url = input('[+] Enter Target URL: ')
file_name = input('[+] Upload Directories File: ')

if not target_url.startswith('http://') and not target_url.startswith('https://'):
	target_url = "http://" + target_url

# Define main function
def request(url):
	try:
		return requests.get(url)
	except requests.exceptions.ConnectionError:
		pass

# Open file and check it
try:
	file = open(file_name, 'r')
except FileNotFoundError:
	print(f"[!] ERROR: File '{file_name}' not found. Exiting.")
	exit()

print(f"[*] Starting scan on {target_url}...")

for line in file:
	directory = line.strip()
	full_url = target_url.rstrip('/') + '/' + directory
	response = request(full_url)
	if response:
		print(f'[+] Found: {full_url} [Status: {response.status_code}]')

file.close()

print('[*] Scan finished.')