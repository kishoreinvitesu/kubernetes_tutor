from PIL import Image, ImageDraw

# Create a blank image
width, height = 400, 300
image = Image.new("RGB", (width, height), "skyblue")
draw = ImageDraw.Draw(image)

# Draw the airplane body
body_coords = [(100, 130), (300, 170)]
draw.rectangle(body_coords, fill="gray")

# Draw the nose (triangle)
nose_coords = [(300, 130), (330, 150), (300, 170)]
draw.polygon(nose_coords, fill="darkgray")

# Draw the tail fin
tail_coords = [(100, 130), (80, 100), (100, 150)]
draw.polygon(tail_coords, fill="darkgray")

# Draw the top wing
top_wing_coords = [(140, 110), (260, 110), (240, 130), (160, 130)]
draw.polygon(top_wing_coords, fill="red")

# Draw the bottom wing
bottom_wing_coords = [(140, 170), (260, 170), (240, 190), (160, 190)]
draw.polygon(bottom_wing_coords, fill="red")

# Draw windows
for x in range(130, 270, 30):
    draw.ellipse((x, 140, x+10, 150), fill="lightblue")

# Save image
image.save("airplane.png")
print("Airplane image saved as airplane.png")
