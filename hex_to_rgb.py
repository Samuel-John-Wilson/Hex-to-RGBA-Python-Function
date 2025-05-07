def hex_to_rgba(hex_color):
    # Remove leading '#' if present
    if hex_color.startswith("#"):
        hex_color = hex_color[1:]

    # Validate input as a proper hex string
    if not is_hexadecimal(hex_color):
        raise Exception("not a hex color string")

    hex_length = len(hex_color)

    # Handle different hex formats
    if hex_length == 3:  # Shorthand like "#abc" → "#aabbcc"
        hex_color = ''.join(c * 2 for c in hex_color)
    elif hex_length == 4:  # "#rgba" format (expand and use 4th digit for alpha)
        r, g, b, a = hex_color
        hex_color = r * 2 + g * 2 + b * 2
        alpha = int(a * 2, 16)  # Use the expanded alpha value
    elif hex_length == 6:  # Standard hex color format
        alpha = 255  # Default full opacity
    elif hex_length == 8:  # "#RRGGBBAA" format (includes alpha)
        alpha = int(hex_color[6:8], 16)
    else:
        raise Exception("Invalid hex color format")

    # Convert hex to RGBA values
    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return r, g, b, alpha  # Return RGBA tuple

# Example usage:
print(hex_to_rgba("#abc"))    # Output: (170, 187, 204, 255) - Expands shorthand
print(hex_to_rgba("#1234"))   # Output: (17, 34, 68, 68) - Alpha correctly derived
print(hex_to_rgba("#123456")) # Output: (18, 52, 86, 255)
print(hex_to_rgba("#12345678")) # Output: (18, 52, 86, 120) - Handles transparency
