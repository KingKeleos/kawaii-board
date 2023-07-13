from pyngrok import ngrok

def createTunnel():
    ngrok.set_auth_token("2SVuAoN5bFM4mZ50PUVZ2OO6mTR_JPGJmbMvW9Ba8Q7KY4Qm")
    tunnel = ngrok.connect(443).public_url
    print (f"Created ngrok Tunnel {tunnel}")
    return tunnel

def runningTunnels():
    tunnels = ngrok.get_tunnels()
    print(tunnels)