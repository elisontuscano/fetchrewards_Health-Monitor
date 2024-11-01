# Health Monitor
The aim of the Assignment is to Run heath check every 15 seconds and log the availability percentage over time.

### Features
* Parse URL endpoints from a YAML file
* Run Health Checks every 15 seconds
* Log Availabilty percentage of each domain
* Dockerize to run easily


### Future Scope
* Make Extensible: For example letting user select time to monitor
* Send Email/Alert after custom threshold failure

### Prerequisites
* Python 3.8 or higher
* `request` and `pyyaml` Python packages
* Docker (Optional)


## Installation 

1. **Clone Repository:**
```bash
git clone https://github.com/elisontuscano/fetchrewards_Health-Monitor.git
cd fetchrewards_Health-Monitor
```

### Using Python

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Install dependencies:**
    ```bash
    python health-monitor.py
    ```

3. Enter the path to your YAML file or press enter to use `prompt.yaml` file from current directory.

### Using Docker

1. Build Docker Image
    ```bash
    docker build -t health-monitor-app .
    ```

2. Run Docker Image
    ```
    docker run -it --rm health-monitor-app
    ```

3. It will copy the `prompt.yaml` file inside current directory to our container file system. Press enter to use it directly or type `/app/prompt.yaml` when asked for file path

4. To use **Your own Yaml file** use this command
    ```bash
    docker run -it --rm -v "<path-to-your-file>:/app/prompt.yaml" health-monitor-app
    ```

    Replace `<path-to-your-file>` to actual path of your YAML file. 

    1. This will mount your file to `/app/prompt.yaml` file in our container directory.
    2. Press enter to use it directly or type `/app/prompt.yaml` when asked for file path




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