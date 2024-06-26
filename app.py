import argparse
from flask import Flask, render_template, Response
from camera import VideoCamera
import flask
from PIL import ImageGrab
from io import BytesIO
import socket

app = Flask(__name__)

camera_enabled = True


@app.route("/")
def index():
    return render_template("index.html")


def gen(camera):
    while True:
        if camera_enabled:
            frame = camera.get_frame()
            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
            )


@app.route("/video_feed")
def video_feed():
    if camera_enabled:
        return Response(
            gen(VideoCamera()), mimetype="multipart/x-mixed-replace; boundary=frame"
        )
    else:
        return "Cámara desactivada"


@app.route("/screen.png")
def serve_pil_image():
    img_buffer = BytesIO()
    ImageGrab.grab().save(img_buffer, "PNG", quality=10)
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype="image/png")


@app.route("/js/<path:path>")
def send_js(path):
    return flask.send_from_directory("js", path)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--camera", choices=["on", "off"], default="off", help="Estado de la cámara"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="Puerto para ejecutar la aplicación Flask",
    )
    args = parser.parse_args()

    if args.camera == "off":
        camera_enabled = False

    app.run(host=get_ip(), port=args.port, debug=True)
