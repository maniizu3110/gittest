
import http.server, socketserver
class ExtendedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/extended":self.send_extended_response()
        else:super().do_GET()
    def send_extended_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = self.get_extended_page()
        self.wfile.write(response.encode())
    def get_extended_page(self):
        return """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Extended Functionality</title></head><body><h1>Welcome to the Extended Functionality of the Web Server</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tempor nisi id odio commodo tincidunt. Maecenas malesuada tortor ut augue fringilla feugiat. Proin vitae odio eu lectus gravida ultrices et eget sem. Quisque in orci mi. Nam malesuada bibendum neque vel venenatis. Nullam a sapien et velit lobortis facilisis. Duis et odio non metus fringilla tincidunt id id nunc. Nunc scelerisque risus ac risus fermentum maximus. In sit amet ultricies justo. Nulla vestibulum mauris ac est convallis suscipit. Fusce dapibus magna eros, quis varius nulla tempor sed.</p><p>Curabitur ullamcorper finibus est, ut elementum sapien dignissim ut. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis imperdiet rhoncus facilisis. Vivamus pharetra ex enim, a bibendum justo accumsan at. Sed venenatis malesuada ligula, vel pretium elit bibendum eu. Morbi lacinia dui et velit fermentum, a eleifend mi ullamcorper. Etiam sodales lorem quis metus convallis, eget pulvinar libero ullamcorper. Fusce vitae consequat est. Suspendisse mollis volutpat turpis, non vestibulum tellus. Proin nec lacus non dolor malesuada cursus id id turpis. Curabitur et quam quis tellus suscipit facilisis a vel orci.</p><p>Phasellus at interdum diam, eget scelerisque dui. Donec tempor, turpis nec condimentum aliquet, enim justo molestie orci, at tristique turpis massa et velit. Mauris id semper sapien. Aliquam erat volutpat. Aenean a urna libero. Pellentesque in urna sollicitudin...
def run(server_class=http.server.HTTPServer, handler_class=ExtendedHTTPRequestHandler):
    PORT = 8000
    with server_class(("", PORT), handler_class) as httpd:
        print("Serving on port", PORT)
        httpd.serve_forever()
if __name__ == "__main__":
    run()