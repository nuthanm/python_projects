import json

def generate_http_requests(swagger_json):
    http_file_content = ""

    for path, methods in swagger_json.get('paths', {}).items():
        for method, details in methods.items():
            http_file_content += f"{method.upper()} {path}\n"
            if 'parameters' in details:
                for param in details['parameters']:
                    if param['in'] == 'path':
                        path_param = param['name']
                        path_value = '{{' + path_param + '}}'
                        path = path.replace('{' + path_param + '}', path_value)
            if 'requestBody' in details:
                request_body = details['requestBody']
                content = request_body['content']
                for content_type, schema in content.items():
                    if 'schema' in schema:
                        ref = schema['schema']['$ref']
                        http_file_content += f"Content-Type: {content_type}\n"
                        http_file_content += f"{json.dumps({'data': ref})}\n"  # Placeholder for request body data
            http_file_content += "###\n\n"

    return http_file_content

# Example usage
with open("JsonToHttp.txt", "r") as file:
    swagger_file = file.read()

swagger_json = json.loads(swagger_file)

http_file_content = generate_http_requests(swagger_json)

# Write content to .http file
with open("api_calls.http", "w") as file:
    file.write(http_file_content)

print("HTTP file generated successfully.")
