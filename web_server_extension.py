

import http.server
import socketserver

class ExtendedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/extended":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            response = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extended Functionality</title>
</head>
<body>
    <h1>Welcome to the Extended Functionality of the Web Server</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tempor nisi id odio commodo tincidunt. Maecenas malesuada tortor ut augue fringilla feugiat. Proin vitae odio eu lectus gravida ultrices et eget sem. Quisque in orci mi. Nam malesuada bibendum neque vel venenatis. Nullam a sapien et velit lobortis facilisis. Duis et odio non metus fringilla tincidunt id id nunc. Nunc scelerisque risus ac risus fermentum maximus. In sit amet ultricies justo. Nulla vestibulum mauris ac est convallis suscipit. Fusce dapibus magna eros, quis varius nulla tempor sed.</p>

    <p>Curabitur ullamcorper finibus est, ut elementum sapien dignissim ut. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis imperdiet rhoncus facilisis. Vivamus pharetra ex enim, a bibendum justo accumsan at. Sed venenatis malesuada ligula, vel pretium elit bibendum eu. Morbi lacinia dui et velit fermentum, a eleifend mi ullamcorper. Etiam sodales lorem quis metus convallis, eget pulvinar libero ullamcorper. Fusce vitae consequat est. Suspendisse mollis volutpat turpis, non vestibulum tellus. Proin nec lacus non dolor malesuada cursus id id turpis. Curabitur et quam quis tellus suscipit facilisis a vel orci.</p>

    <p>Phasellus at interdum diam, eget scelerisque dui. Donec tempor, turpis nec condimentum aliquet, enim justo molestie orci, at tristique turpis massa et velit. Mauris id semper sapien. Aliquam erat volutpat. Aenean a urna libero. Pellentesque in urna sollicitudin, consequat libero eu, dictum leo. Sed vehicula ligula ac ligula dapibus, ac tristique elit sagittis. Sed vestibulum, arcu eget cursus tempus, sapien dolor rutrum erat, et tincidunt elit justo at mi. Cras cursus eros vel efficitur ultrices. Nunc et enim libero. Vestibulum iaculis, felis eget tristique sollicitudin, urna nisl porta sem, et iaculis nunc risus id mi.</p>

    <p>Sed porttitor bibendum diam, a tincidunt nibh blandit a. In ultricies, neque vel venenatis blandit, sapien est dapibus lacus, eget posuere libero tellus ut ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Etiam congue quam ut velit tempor ullamcorper. Praesent nec dolor ut est cursus bibendum. Quisque ac quam urna. Proin ut ligula metus. Integer non fringilla metus, non suscipit erat. Integer sodales velit a lacinia venenatis. In hac habitasse platea dictumst. Integer sodales enim sed semper pellentesque. Nulla facilisi. Nulla lacinia vulputate ante, et vestibulum nisl ullamcorper eu.</p>

    <p>Vestibulum et aliquam metus. Nulla aliquet sem non dolor ultrices, non placerat mi varius. Ut tristique, quam id ullamcorper volutpat, dolor sapien suscipit ante, id ornare mauris urna ac mi. Phasellus ac diam tortor. Sed eu orci in quam sollicitudin egestas. Proin aliquet dolor vel quam vehicula, a consequat sapien vehicula. Integer viverra nunc quis enim varius facilisis. Integer id tortor nec elit sodales gravida. Aenean consectetur, augue vitae laoreet dapibus, metus massa sollicitudin mi, et viverra erat tellus a est. Curabitur malesuada justo eget purus faucibus, in consectetur ligula sodales. Pellentesque ac facilisis libero, vitae blandit odio. Sed tempor euismod metus, et ullamcorper quam sodales et.</p>
</body>
</html>
"""
            self.wfile.write(response.encode())
        else:
            super().do_GET()

def run(server_class=http.server.HTTPServer, handler_class=ExtendedHTTPRequestHandler):
    PORT = 8000
    with server_class(("", PORT), handler_class) as httpd:
        print("Serving on port", PORT)
        httpd.serve_forever()

if __name__ == "__main__":
    run()
