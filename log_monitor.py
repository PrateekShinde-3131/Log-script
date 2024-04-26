import subprocess
import logging
import time
import random
from collections import Counter
import threading
import re

# Configure logging to write to a file
logging.basicConfig(filename='log-monitor.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

# Initialize a counter for occurrences of log levels
log_level_counter = Counter()
# Initialize a counter for occurrences of error messages
error_message_counter = Counter()
# Initialize a counter for occurrences of specific patterns
pattern_counter = Counter()

# Define patterns to search for in log entries
patterns = {
    'ERROR': r'ERROR',
    'HTTP_STATUS_200': r'HTTP/1.1" 200',
    'HTTP_STATUS_404': r'HTTP/1.1" 404'
    # Add more patterns here
}

# Function to track and display new log entries in real time
def track_logs():
    try:
        # Start the tail command as a subprocess
        process = subprocess.Popen(['tail', '-f', 'log-monitor.log'], stdout=subprocess.PIPE)
        
        # Loop to read the log file's output in real time
        while True:
            line = process.stdout.readline()
            if line:
                line = line.decode('utf-8')
                print(line, end='')  # Print new log entries in real time
                
                # Check for patterns in the line
                for pattern, regex in patterns.items():
                    if re.search(regex, line):
                        pattern_counter[pattern] += 1

            else:
                break

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nLog tracking interrupted. Exiting.")
        process.kill()

# Main loop to log messages
def log_messages():
    while True:
        try:
            # Randomly select a log level
            log_level = random.choice(log_levels)
            
            # Increment the count for the selected log level
            log_level_counter[log_level] += 1
            
            # Get the log message format for the selected log level
            log_message = formats[log_level]
            
            # Log the message
            logger.log(log_level, log_message)
            
            # If it's an error message, increment its count
            if log_level == logging.ERROR:
                error_message_counter[log_message] += 1
            
            # Sleep for a short interval
            time.sleep(1)
        
        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C)
            print("\nLogging interrupted. Exiting.")
            break

# Start tracking logs in a separate thread
thread = threading.Thread(target=track_logs)
thread.start()

# Start logging messages
log_messages()

# Wait for the log tracking thread to finish
thread.join()

# Print the analysis results
print("Log Level Occurrences:")
for level, count in log_level_counter.items():
    print(f"{logging.getLevelName(level)}: {count}")

# Print the pattern occurrences
print("\nPattern Occurrences:")
for pattern, count in pattern_counter.items():
    print(f"{pattern}: {count}")

# Print the top error message
if error_message_counter:
    top_error_message = error_message_counter.most_common(1)[0]
    print(f"\nTop Error Message: {top_error_message[0]} (Count: {top_error_message[1]})")
else:
    print("\nNo error messages were logged.")
