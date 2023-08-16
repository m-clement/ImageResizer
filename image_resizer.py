from PIL import Image

def resize_image(x, y):

    # Open the image file
    # Change the name and the path as per your choice
    image = Image.open('test.jpg')
    
    # Print the current size of the image
    print(f"Previous size : {image.size}")
    
    # Resize the image based on the given dimensions
    resized_image = image.resize((x,y))
    
    # Save the resized image
    # Change the name and the path as per your choice
    resized_image.save('test_resized.jpg')

# Get the desired width and height from the user
x = int(input("Enter width as an integer: "))
y = int(input("Enter height as an integer: "))

# Call the function to resize the image
resize_image(x, y)
