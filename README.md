# Health Monitor
The aim of the Assignment is to Run heath check every 15 seconds and log the availability percentage over time.

### Features
* Parse URL endpoints from a YAML file
* Run Health Checks every 15 seconds
* Log Availabilty percentage of each domain


### Future Scope
* Dockerize to run easily.
* Make Extensible: For example letting user select time to monitor.
* Send Email/Alert after custom threshold failure.

### Prerequisites
* Python 3.8 or higher
* `request` and `pyyaml` Python packages


## Installation 

1. **Clone Repository:**
```bash
git clone https://github.com/elisontuscano/fetchrewards_Health-Monitor.git
cd fetchrewards_Health-Monitor
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install dependencies:**
```bash
python Health-Monitor.py
```

4. Enter the path to your YAML file or press enter to use `prompt.yaml` file from current directory.


## How It Works
1. It reads the configuration file in YAML format, parses the endpoints.
2. Execute HTTP request to each endpoint every 15 seconds.
3. It checks if the endpoint is `UP` if it satisfy below conditions.
    1. HTTP response code in the range of 200-299
    2. latency less than 500 ms
4. The program outputs the total percentage of availability by domain in the console.

## Sample Output
```
fetch.com has 67% availability percentage
www.fetchrewards.com has 100% availability percentage
```