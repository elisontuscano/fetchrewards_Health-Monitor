import yaml
import requests
import time
from urllib.parse import urlparse


def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except:
        raise SystemExit("Incorrect File Path or File does not exist") 

def check_health(endpoint):
    method = endpoint.get("method", "GET")
    url = endpoint["url"]
    headers = endpoint.get("headers", {})
    body = endpoint.get("body", None)

    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, timeout=5)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, data=body, timeout=5)
        else:
            print("Unsupported method: ",method)
            return False

        latency = response.elapsed.total_seconds() * 1000
        http_status = response.status_code
        if 200 <= http_status < 300 and latency < 500:
            return True
        
    except requests.RequestException:
        pass

    return False

# Main function to run health checks and uptime
def main(file_path):
    endpoints = load_yaml_file(file_path)
    domain_uptime = {}
    
    for endpoint in endpoints:
        domain = urlparse(endpoint["url"]).netloc
        if domain not in domain_uptime:
            domain_uptime[domain] = {"up_count": 0, "total_count": 0}
    
    try:
        while True:
            #Run health checks
            for endpoint in endpoints:
                domain = urlparse(endpoint["url"]).netloc
                is_up = check_health(endpoint)
                
                domain_uptime[domain]["total_count"] += 1
                if is_up:
                    domain_uptime[domain]["up_count"] += 1

                
            #Log the availability percentages
            for domain, count in domain_uptime.items():
                availability = (count["up_count"] / count["total_count"]) * 100
                availability = str(round(availability)) + "%"
                print(domain,"has",availability,"availability percentage")

            #Run health check every 15 seconds
            time.sleep(15)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        

if __name__ == "__main__":
    file_path = input("Enter the path to the YAML configuration file: " ) or "prompt.yaml"
    main(file_path)