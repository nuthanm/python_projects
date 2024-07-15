import json

def generate_http_file_from_json(json_data):
    http_file_content = f"@ProgramEntryPoint.API_HostAddress = http://localhost:5031\n\n"

    for item in json_data.get('item', []):
        name = item.get('name')
        request = item.get('request')
        if request:
            method = request.get('method')
            url = request.get('url', {}).get('raw', '')
            headers = request.get('header', [])
            body = request.get('body', {}).get('raw', '')

            http_file_content += f"{method} {url}\n"
            if headers:
                for header in headers:
                    http_file_content += f"{header.get('key')}: {header.get('value')}\n"
            if body:
                http_file_content += f"{body}\n"
            http_file_content += "###\n\n"

    return http_file_content

# Example JSON input
with open("JsonToHttp.txt", "r") as file:
    json_input = file.read()

# Parse JSON input
data = json.loads(json_input)

# Generate .http file content
http_file_content = generate_http_file_from_json(data)

# Write content to .http file
with open("api_calls_swagger.http", "w") as file:
    file.write(http_file_content)

print("HTTP file generated successfully.")
