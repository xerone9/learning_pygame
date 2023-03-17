from PIL import Image

filename = "assets/spawns/enemy7.gif"

frames = []
resized_py_game_image_object = []
with Image.open(filename) as im:
    for i in range(im.n_frames):
        im.seek(i)
        frame = im.copy()
        frame.save(f"frame_{i}.png")