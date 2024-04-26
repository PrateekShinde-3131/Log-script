# Log Monitor and Analyzer

This Python script continuously monitors a specified log file for new entries, counts occurrences of specific keywords or patterns, and generates a summary report including the top error message.

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of Python and terminal/command prompt usage.

## Dependencies

No external dependencies are required for this script as it uses standard Python libraries.

## Installation

1. Ensure Python is installed on your system.
2. Download the `log_monitor.py` script to your desired directory.

## Usage

To use the script, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you saved the `log_monitor.py` file.
3. Run the script using the command: python log_monitor.py
4. The script will start monitoring the specified log file (`log-monitor.log` by default) and output the results to the terminal.
5. To stop the monitoring, press `Ctrl+C`. The script will print a summary report showing the count of each pattern and then exit.

## You can customize the script by modifying the following variables:

- `log_file_path`: Path to the log file you want to monitor.
- `patterns`: Dictionary containing the patterns you want to track in the log file.

## Testing

To test the script, you can manually create a `log-monitor.log` file and add log entries that match the patterns defined in the script. Run the script and verify that it correctly tracks and counts the occurrences of each pattern.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests with improvements to the script.

## License This script is provided "as is", without warranty of any kind, express or implied.


