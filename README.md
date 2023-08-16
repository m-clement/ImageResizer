## Image Resizer

Resize your images easily with this Python script. The script utilizes the `Pillow` library to facilitate image resizing.

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your system.
- **Pillow Library**: Install the Pillow library using pip:
  For Mac
  ```
  pip3 install Pillow
  ```
  For Windows
  ```
  pip install Pillow
  ```

### Usage

1. **Setup**:
   - Clone this repository or download the `image_resizer.py` script.
   - Place the image you want to resize in the same directory as the script. By default, the script expects the image to be named `test.jpg`.

2. **Running the Script**:
   ```bash
   python image_resizer.py
   ```
   Follow the prompts to specify the desired width and height for your resized image. The resized image will be saved as `test_resized.jpg` in the same directory.

### Customization

If you'd like to use a different input or output image name:

1. Open `image_resizer.py`.
2. Modify the line:

   ```python
   image = Image.open('test.jpg')
   ```

   Replace `'test.jpg'` with the path to your image.

3. To change the output filename, modify the line:

   ```python
   resize_image.save('test_resized.jpg')
   ```

